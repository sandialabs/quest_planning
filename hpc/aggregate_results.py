# -*- coding: utf-8 -*-
"""
hpc/aggregate_results.py
=========================
Collect and summarise results from a completed QuESt Planning HPC job array.

For each job in the manifest, this script:
  1. Locates the ``results_summary.xlsx`` written by ExplanResultsViewer.
  2. Extracts every cost breakdown variable and selected capacity/emissions
     metrics into a single row.
  3. Assembles a ``study_summary.csv`` and ``study_summary.xlsx`` at the
     study output directory root.
  4. Generates comparison plots (tornado / heatmap / bar chart) based on
     the study mode inferred from the manifest.
  5. Writes ``failed_jobs.txt`` listing any jobs that did not produce output.

Usage
-----
    python hpc/aggregate_results.py <manifest.csv> [--no-plots]

    manifest.csv    Path to the manifest produced by study_builder.py.
    --no-plots      Skip matplotlib plot generation (useful on headless nodes).

Outputs (written next to manifest.csv)
---------------------------------------
    study_summary.csv          One row per job; all cost + capacity metrics.
    study_summary.xlsx         Same as CSV with formatted sheets.
    failed_jobs.txt            Job IDs with missing / infeasible results.
    plots/                     Comparison plots (unless --no-plots).
"""

from __future__ import annotations

import argparse
import csv
import os
import warnings
from pathlib import Path
from typing import Optional

import pandas as pd
import numpy as np
import yaml

# Suppress openpyxl UserWarnings about unnamed styles in Excel files
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


# ---------------------------------------------------------------------------
# Cost and metric extraction spec
# ---------------------------------------------------------------------------
# Each entry: (excel_sheet_name, aggregation_method, output_column_name)
#
#   aggregation_method:
#     "sum_all"    -- sum every numeric value in the sheet (scalar result)
#     "sum_by_col" -- sum grouped by the last index column (returns dict)
#     "first"      -- take the first (and only) value
#     "pivot_tech" -- pivot by 'Tech' column for the last investment year
#     "final_year" -- filter to max year, then sum numeric columns

_COST_METRICS: list[tuple[str, str, str]] = [
    # Annual cost components (sum over all investment years → total NPV component)
    ("annual_total_cost",     "sum_all",   "npv_total_cost"),
    ("annual_gen_inv_cost",   "sum_all",   "npv_gen_inv_cost"),
    ("annual_trans_inv_cost", "sum_all",   "npv_trans_inv_cost"),
    ("annual_es_replace_cost","first",     "npv_es_replace_cost"),
    ("annual_fom_cost",       "sum_all",   "npv_fom_cost"),
    ("annual_vom_cost",       "sum_all",   "npv_vom_cost"),
    ("annual_fuel_cost",      "sum_all",   "npv_fuel_cost"),
    ("annual_ls_cost",        "sum_all",   "npv_load_shed_cost"),
    ("annual_itc",            "sum_all",   "npv_itc_credit"),
    ("annual_ptc",            "sum_all",   "npv_ptc_credit"),
    ("annual_ll_curt_cost",   "sum_all",   "npv_ll_curtailment_cost"),
    ("objective_value",       "first",     "objective_value"),
]

_CAPACITY_METRICS: list[tuple[str, str, str]] = [
    # Installed capacity by technology (final investment year, summed over buses)
    ("P_cap_total",           "pivot_tech_final", "cap_MW"),
    # Energy storage capacity (final year, summed)
    ("Store",                 "sum_final_year",   "es_energy_MWh"),
    # CO2 emissions (sum over all years and time blocks)
    ("CO2_emission",          "sum_all",          "co2_total_tonne"),
    # Total curtailment (sum over all indices)
    ("Curt",                  "sum_all",          "curtailment_MWh"),
    # Load not served (sum over all indices)
    ("LNS",                   "sum_all",          "lns_MWh"),
]


# ---------------------------------------------------------------------------
# Excel sheet reader
# ---------------------------------------------------------------------------

def _read_sheet(xl: pd.ExcelFile, sheet_name: str) -> Optional[pd.DataFrame]:
    """Return the DataFrame for *sheet_name*, or None if the sheet is absent."""
    if sheet_name not in xl.sheet_names:
        return None
    try:
        return xl.parse(sheet_name, index_col=0)
    except Exception:
        return None


def _extract_scalar(df: Optional[pd.DataFrame], method: str) -> float:
    """Reduce a DataFrame to a single float according to *method*."""
    if df is None or df.empty:
        return float("nan")

    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        return float("nan")

    if method in ("sum_all", "sum_final_year"):
        return float(numeric.to_numpy().sum())
    elif method == "first":
        # Flatten and take the first non-NaN value
        vals = numeric.to_numpy().flatten()
        non_nan = vals[~np.isnan(vals)]
        return float(non_nan[0]) if len(non_nan) > 0 else float("nan")
    return float("nan")


def _extract_capacity_by_tech(df: Optional[pd.DataFrame]) -> dict[str, float]:
    """Return {tech_name: total_MW} for the final investment year."""
    if df is None or df.empty:
        return {}

    # P_cap_total index levels: bus (b), generator (g), year (y)
    # The Excel sheet has a multi-index written by pandas; reset it.
    df = df.reset_index()

    # Try to identify the year column (often named 'y' or 'level_2')
    year_col = None
    for candidate in ("y", "level_2", "year", "Year"):
        if candidate in df.columns:
            year_col = candidate
            break

    if year_col is not None:
        final_year = df[year_col].max()
        df = df[df[year_col] == final_year]

    # Try to identify the technology column
    tech_col = None
    for candidate in ("Tech", "tech", "g", "Gen_num"):
        if candidate in df.columns:
            tech_col = candidate
            break

    # Sum the numeric value column (last numeric column)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        return {}

    value_col = numeric_cols[-1]

    if tech_col:
        grouped = df.groupby(tech_col)[value_col].sum()
        return {str(k): float(v) for k, v in grouped.items()}
    else:
        return {"total": float(df[value_col].sum())}


def _extract_final_year_sum(df: Optional[pd.DataFrame]) -> float:
    """Sum numeric values for the final investment year only."""
    if df is None or df.empty:
        return float("nan")

    df = df.reset_index()

    year_col = None
    for candidate in ("y", "level_2", "year", "Year"):
        if candidate in df.columns:
            year_col = candidate
            break

    if year_col is not None:
        final_year = df[year_col].max()
        df = df[df[year_col] == final_year]

    numeric = df.select_dtypes(include="number")
    return float(numeric.to_numpy().sum()) if not numeric.empty else float("nan")


# ---------------------------------------------------------------------------
# Per-job result extraction
# ---------------------------------------------------------------------------

def _find_results_xlsx(results_dir: str) -> Optional[Path]:
    """Locate results_summary.xlsx inside *results_dir* or its subdirectories."""
    base = Path(results_dir)
    if not base.exists():
        return None
    # Direct path
    direct = base / "results_summary.xlsx"
    if direct.exists():
        return direct
    # results_dir is the job-specific dir; the file lives one level deeper
    # in a timestamped subfolder created by create_results_folder()
    for child in sorted(base.iterdir()):
        candidate = child / "results_summary.xlsx"
        if candidate.exists():
            return candidate
    return None


def _extract_job_metrics(results_xlsx: Path) -> dict:
    """Extract all cost and capacity metrics from one results_summary.xlsx."""
    row: dict = {}

    try:
        xl = pd.ExcelFile(results_xlsx, engine="openpyxl")
    except Exception as exc:
        row["_error"] = str(exc)
        return row

    # --- Cost metrics ---
    for sheet_name, method, col_name in _COST_METRICS:
        df = _read_sheet(xl, sheet_name)
        row[col_name] = _extract_scalar(df, method)

    # --- Capacity / emissions metrics ---
    for sheet_name, method, col_prefix in _CAPACITY_METRICS:
        df = _read_sheet(xl, sheet_name)

        if method == "pivot_tech_final":
            tech_caps = _extract_capacity_by_tech(df)
            for tech, mw in tech_caps.items():
                row[f"{col_prefix}_{tech}"] = mw
        elif method == "sum_final_year":
            row[col_prefix] = _extract_final_year_sum(df)
        else:
            row[col_prefix] = _extract_scalar(df, method)

    return row


# ---------------------------------------------------------------------------
# Comparison plots
# ---------------------------------------------------------------------------

def _plot_tornado(summary: pd.DataFrame, output_dir: Path) -> None:
    """Tornado chart for OAT sensitivity (one swept parameter at a time)."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use("Agg")
    except ImportError:
        return

    if "npv_total_cost" not in summary.columns:
        return

    # Find base row: job_id == 0 (study_builder always sets base as job 0 for OAT)
    base_rows = summary[summary["job_id"] == 0]
    if base_rows.empty:
        return
    base_cost = base_rows["npv_total_cost"].iloc[0]

    # Identify parameter columns (non-metric, non-id columns)
    metric_cols = {"job_id", "config_path", "results_dir", "status", "_error"}
    metric_cols.update(c for c in summary.columns if c.startswith("npv_") or
                       c.startswith("cap_") or c in ("objective_value", "co2_total_tonne",
                                                       "curtailment_MWh", "lns_MWh",
                                                       "es_energy_MWh"))
    param_cols = [c for c in summary.columns if c not in metric_cols]

    if not param_cols:
        return

    deltas = {}
    for param in param_cols:
        group = summary[summary[param] != summary.loc[summary["job_id"] == 0, param].iloc[0]]
        if group.empty:
            continue
        max_cost = group["npv_total_cost"].max()
        min_cost = group["npv_total_cost"].min()
        deltas[param] = (min_cost - base_cost, max_cost - base_cost)

    if not deltas:
        return

    params_sorted = sorted(deltas.keys(), key=lambda p: abs(deltas[p][1] - deltas[p][0]), reverse=True)
    y_pos = range(len(params_sorted))

    fig, ax = plt.subplots(figsize=(10, max(4, len(params_sorted) * 0.5 + 1)))
    for i, param in enumerate(params_sorted):
        low, high = deltas[param]
        ax.barh(i, high - low, left=low, color="steelblue", alpha=0.75, height=0.6)

    ax.set_yticks(list(y_pos))
    ax.set_yticklabels(params_sorted)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Delta NPV Total Cost vs. Base Case ($M)")
    ax.set_title("OAT Sensitivity Tornado Chart — NPV Total System Cost")
    plt.tight_layout()

    plot_path = output_dir / "plots" / "tornado_npv_total_cost.png"
    plot_path.parent.mkdir(exist_ok=True)
    fig.savefig(plot_path, dpi=150)
    plt.close(fig)
    print(f"Plot saved: {plot_path}")


def _plot_cost_bar_comparison(summary: pd.DataFrame, output_dir: Path) -> None:
    """Stacked bar chart of full cost breakdown for each job (ensemble/sweep)."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use("Agg")
    except ImportError:
        return

    cost_components = [
        ("npv_gen_inv_cost",       "Gen Investment"),
        ("npv_trans_inv_cost",     "Tx Investment"),
        ("npv_es_replace_cost",    "ES Replacement"),
        ("npv_fom_cost",           "Fixed O&M"),
        ("npv_vom_cost",           "Variable O&M"),
        ("npv_fuel_cost",          "Fuel"),
        ("npv_load_shed_cost",     "Load Shed Penalty"),
        ("npv_ll_curtailment_cost","LL Curtailment"),
    ]
    credit_components = [
        ("npv_itc_credit", "ITC Credit"),
        ("npv_ptc_credit", "PTC Credit"),
    ]

    available = [(col, lbl) for col, lbl in cost_components if col in summary.columns]
    avail_credits = [(col, lbl) for col, lbl in credit_components if col in summary.columns]

    if not available:
        return

    colors = [
        "#4e79a7", "#f28e2b", "#e15759", "#76b7b2",
        "#59a14f", "#edc948", "#b07aa1", "#ff9da7",
    ]

    n_jobs = len(summary)
    x = np.arange(n_jobs)
    bar_width = 0.65

    fig, ax = plt.subplots(figsize=(max(10, n_jobs * 0.6 + 2), 7))

    bottom = np.zeros(n_jobs)
    for (col, lbl), color in zip(available, colors):
        vals = summary[col].fillna(0).values
        ax.bar(x, vals, bottom=bottom, label=lbl, color=color, width=bar_width)
        bottom += vals

    # Credits as negative bars
    bottom_neg = np.zeros(n_jobs)
    for (col, lbl) in avail_credits:
        vals = summary[col].fillna(0).values
        ax.bar(x, -np.abs(vals), bottom=bottom_neg, label=lbl,
               color="#9c755f", width=bar_width, alpha=0.7)
        bottom_neg -= np.abs(vals)

    ax.set_xticks(x)
    labels = [f"job_{int(r['job_id']):03d}" for _, r in summary.iterrows()]
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("NPV Cost Component ($M scaled)")
    ax.set_title("Full Cost Breakdown by Job")
    ax.legend(loc="upper right", fontsize=7, ncol=2)
    ax.axhline(0, color="black", linewidth=0.6)
    plt.tight_layout()

    plot_path = output_dir / "plots" / "cost_breakdown_by_job.png"
    plot_path.parent.mkdir(exist_ok=True)
    fig.savefig(plot_path, dpi=150)
    plt.close(fig)
    print(f"Plot saved: {plot_path}")


def _plot_sweep_heatmap(summary: pd.DataFrame, output_dir: Path, param_cols: list[str]) -> None:
    """Heatmap of NPV total cost over two sweep parameters (if exactly 2 vary)."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use("Agg")
    except ImportError:
        return

    if len(param_cols) != 2 or "npv_total_cost" not in summary.columns:
        return

    p1, p2 = param_cols[0], param_cols[1]
    try:
        pivot = summary.pivot_table(index=p1, columns=p2, values="npv_total_cost", aggfunc="mean")
    except Exception:
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(pivot.values, aspect="auto", cmap="YlOrRd")
    plt.colorbar(im, ax=ax, label="NPV Total Cost ($M scaled)")
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([str(c) for c in pivot.columns], rotation=45)
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels([str(i) for i in pivot.index])
    ax.set_xlabel(p2)
    ax.set_ylabel(p1)
    ax.set_title(f"NPV Total Cost Heatmap: {p1} vs {p2}")
    plt.tight_layout()

    plot_path = output_dir / "plots" / f"heatmap_{p1}_vs_{p2}.png"
    plot_path.parent.mkdir(exist_ok=True)
    fig.savefig(plot_path, dpi=150)
    plt.close(fig)
    print(f"Plot saved: {plot_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def aggregate(manifest_path: str | Path, make_plots: bool = True) -> None:
    manifest_path = Path(manifest_path).resolve()
    output_dir = manifest_path.parent

    # Read manifest
    with open(manifest_path, "r", newline="") as fh:
        reader = csv.DictReader(fh)
        manifest_rows = list(reader)

    if not manifest_rows:
        print("ERROR: manifest.csv is empty.")
        return

    param_cols = [c for c in manifest_rows[0].keys()
                  if c not in ("job_id", "config_path")]

    print(f"Aggregating {len(manifest_rows)} jobs from: {manifest_path}")

    summary_rows: list[dict] = []
    failed_jobs: list[str] = []

    for row in manifest_rows:
        job_id     = row["job_id"]
        config_path = row["config_path"]

        # Load the job YAML to find results_dir
        results_dir: Optional[str] = None
        try:
            with open(config_path, "r") as fh:
                job_config = yaml.safe_load(fh)
            results_dir = job_config.get("results_dir")
        except Exception:
            pass

        # Build result record
        result_row: dict = {"job_id": int(job_id), "config_path": config_path,
                            "results_dir": results_dir or "", "status": "unknown"}
        for k in param_cols:
            result_row[k] = row.get(k, "")

        # Locate results_summary.xlsx
        xlsx_path: Optional[Path] = None
        if results_dir:
            xlsx_path = _find_results_xlsx(results_dir)

        if xlsx_path is None:
            result_row["status"] = "FAILED_NO_OUTPUT"
            failed_jobs.append(job_id)
            print(f"  job_{int(job_id):03d}  FAILED (no results_summary.xlsx found)")
        else:
            metrics = _extract_job_metrics(xlsx_path)
            if "_error" in metrics:
                result_row["status"] = f"FAILED_READ_ERROR: {metrics['_error']}"
                failed_jobs.append(job_id)
                print(f"  job_{int(job_id):03d}  FAILED (read error: {metrics['_error']})")
            else:
                result_row["status"] = "OK"
                result_row.update(metrics)
                obj = metrics.get("objective_value", float("nan"))
                print(f"  job_{int(job_id):03d}  OK  objective={obj:.4g}")

        summary_rows.append(result_row)

    # Build summary DataFrame
    summary_df = pd.DataFrame(summary_rows)

    # Write CSV
    csv_path = output_dir / "study_summary.csv"
    summary_df.to_csv(csv_path, index=False)
    print(f"\nSummary CSV   : {csv_path}")

    # Write Excel (two sheets: full summary + cost-only view)
    xlsx_out = output_dir / "study_summary.xlsx"
    cost_cols = (
        ["job_id"] + param_cols +
        [c for c in summary_df.columns if c.startswith("npv_") or c == "objective_value"]
    )
    cap_cols = (
        ["job_id"] + param_cols +
        [c for c in summary_df.columns if c.startswith("cap_MW_") or
         c in ("es_energy_MWh", "co2_total_tonne", "curtailment_MWh", "lns_MWh")]
    )

    with pd.ExcelWriter(xlsx_out, engine="openpyxl") as writer:
        summary_df.to_excel(writer, sheet_name="all_metrics", index=False)
        cost_view = summary_df[[c for c in cost_cols if c in summary_df.columns]]
        cost_view.to_excel(writer, sheet_name="cost_breakdown", index=False)
        cap_view = summary_df[[c for c in cap_cols if c in summary_df.columns]]
        cap_view.to_excel(writer, sheet_name="capacity_emissions", index=False)
    print(f"Summary Excel : {xlsx_out}")

    # Write failed jobs list
    if failed_jobs:
        failed_path = output_dir / "failed_jobs.txt"
        failed_path.write_text("\n".join(str(j) for j in failed_jobs) + "\n")
        print(f"\nFailed jobs   : {len(failed_jobs)} — see {failed_path}")
    else:
        print("\nAll jobs completed successfully.")

    # Plots
    if make_plots:
        ok_rows = summary_df[summary_df["status"] == "OK"]
        if ok_rows.empty:
            print("No successful jobs to plot.")
            return

        # Infer study mode from manifest structure
        numeric_param_cols = []
        for pc in param_cols:
            try:
                pd.to_numeric(ok_rows[pc])
                numeric_param_cols.append(pc)
            except Exception:
                pass

        # Always generate cost breakdown bar chart
        _plot_cost_bar_comparison(ok_rows.reset_index(drop=True), output_dir)

        # OAT: tornado chart (heuristic: many jobs, one param changes per job)
        if len(param_cols) >= 1:
            _plot_tornado(ok_rows.reset_index(drop=True), output_dir)

        # Sweep with exactly 2 parameters: heatmap
        if len(param_cols) == 2:
            _plot_sweep_heatmap(ok_rows.reset_index(drop=True), output_dir, param_cols)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Aggregate QuESt Planning HPC job array results into a study summary."
    )
    parser.add_argument("manifest", help="Path to manifest.csv produced by study_builder.py")
    parser.add_argument(
        "--no-plots", action="store_true",
        help="Skip matplotlib plot generation."
    )
    args = parser.parse_args()
    aggregate(args.manifest, make_plots=not args.no_plots)

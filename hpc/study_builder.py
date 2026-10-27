# -*- coding: utf-8 -*-
"""
hpc/study_builder.py
=====================
Generate a batch of QuESt Planning YAML configuration files and a SLURM job
array submission script from a single study specification file.

Three study modes are supported:

  sweep    -- Cartesian product over all listed parameter axes.
  oat      -- One-at-a-time (OAT) sensitivity: base case + each non-base value
              of each parameter, varying one parameter at a time.
  ensemble -- Named discrete scenarios (not a product); each entry in
              ``scenarios`` becomes exactly one job.

Usage
-----
    python hpc/study_builder.py <study_spec.yaml> [--dry-run]

    --dry-run   Print the manifest to stdout without writing any files.

Outputs (written to ``output_dir`` defined in the study spec)
--------------------------------------------------------------
    configs/job_000.yaml … job_NNN.yaml   One config per job
    manifest.csv                          job_id, config_path, <param cols>
    submit_array.sh                       Ready-to-submit SLURM script
    modules.sh                            Auto-generated module load stubs
    logs/                                 Empty directory pre-created for SLURM

See hpc/examples/ for annotated study spec files.
"""

from __future__ import annotations

import argparse
import copy
import csv
import itertools
import os
import sys
import textwrap
from pathlib import Path
from typing import Any

import yaml


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_yaml(path: str | Path) -> dict:
    with open(path, "r") as fh:
        return yaml.safe_load(fh)


def _deep_merge(base: dict, overrides: dict) -> dict:
    """Return a deep copy of *base* with *overrides* applied recursively."""
    result = copy.deepcopy(base)
    for key, val in overrides.items():
        if isinstance(val, dict) and isinstance(result.get(key), dict):
            result[key] = _deep_merge(result[key], val)
        else:
            result[key] = copy.deepcopy(val)
    return result


def _flat_param_label(params: dict) -> str:
    """Create a compact human-readable label from a parameter override dict."""
    parts = []
    for k, v in params.items():
        short_k = k.replace("_", "")[:8]
        parts.append(f"{short_k}-{v}")
    return "_".join(parts)


# ---------------------------------------------------------------------------
# Job generation
# ---------------------------------------------------------------------------

def _jobs_sweep(spec: dict) -> list[dict]:
    """Generate all jobs for mode=sweep (Cartesian product)."""
    sweep_axes: dict = spec.get("sweep", {})
    if not sweep_axes:
        raise ValueError("mode=sweep requires a non-empty 'sweep' block.")

    keys = list(sweep_axes.keys())
    value_lists = [sweep_axes[k] for k in keys]

    jobs = []
    for combo in itertools.product(*value_lists):
        params = dict(zip(keys, combo))
        jobs.append(params)
    return jobs


def _jobs_oat(spec: dict) -> list[dict]:
    """Generate jobs for mode=oat (one-at-a-time sensitivity).

    The base case (all parameters at their first / baseline value) is job 0.
    Then for each parameter, one job is created per non-baseline value.
    """
    sensitivity: dict = spec.get("sensitivity", {})
    if not sensitivity:
        raise ValueError("mode=oat requires a non-empty 'sensitivity' block.")

    # Base case: first value of every parameter
    base_params = {k: v[0] for k, v in sensitivity.items()}

    jobs = [base_params]  # job 0 = base case

    for param, values in sensitivity.items():
        for val in values[1:]:  # skip index 0 (that is the base)
            override = copy.copy(base_params)
            override[param] = val
            jobs.append(override)

    return jobs


def _jobs_ensemble(spec: dict) -> list[dict]:
    """Generate jobs for mode=ensemble (named discrete scenarios)."""
    scenarios: list = spec.get("scenarios", [])
    if not scenarios:
        raise ValueError("mode=ensemble requires a non-empty 'scenarios' list.")

    jobs = []
    for sc in scenarios:
        sc = copy.deepcopy(sc)
        jobs.append(sc)
    return jobs


# ---------------------------------------------------------------------------
# Config file writer
# ---------------------------------------------------------------------------

def _build_job_config(
    base_config: dict,
    params: dict,
    job_id: int,
    output_dir: Path,
    gurobi_license_file: str,
    solver_threads: int,
    quest_repo_path: str,
) -> dict:
    """Merge base config with per-job overrides and inject HPC-specific keys."""
    # Strip ensemble-specific metadata keys before merging into YAML
    clean_params = {k: v for k, v in params.items() if k != "name"}

    config = _deep_merge(base_config, clean_params)

    # HPC-injected keys (never present in base config for normal CLI runs)
    job_results_dir = str(output_dir / "results" / f"job_{job_id:03d}")
    config["results_dir"] = job_results_dir
    config["solver_threads"] = solver_threads
    config["gurobi_license_file"] = gurobi_license_file

    # Ensure data_folder resolves against the repo, not the HPC working dir.
    # Only set data_dir if user didn't already provide an absolute path.
    if "data_dir" not in config:
        config["data_dir"] = str(
            Path(quest_repo_path) / "quest_planning" / "data_explan" / config["data_folder"]
        )

    return config


# ---------------------------------------------------------------------------
# modules.sh generator
# ---------------------------------------------------------------------------

def _generate_modules_sh(spec: dict, output_dir: Path) -> str:
    """Generate a comment-heavy modules.sh stub tailored to the study spec."""
    solver = spec.get("solver", "gurobi")
    use_mpi = _study_uses_mpi(spec)

    lines = [
        "#!/bin/bash",
        "# =============================================================================",
        "# modules.sh  --  Auto-generated by hpc/study_builder.py",
        "# =============================================================================",
        "# Edit this file ONCE for your specific cluster before submitting jobs.",
        "# Uncomment and adjust the module names that apply to your site.",
        "#",
        "# This file is sourced by submit_array.sh at the start of every job.",
        "# =============================================================================",
        "",
        "# --- Python / conda -------------------------------------------------------",
        "# Uncomment ONE of the following (whichever matches your cluster):",
        "#",
        "# Option A: system Python module (common on Cray/HPE/NCAR systems)",
        "# module load python/3.11",
        "#",
        "# Option B: Anaconda/Miniconda module (common on university clusters)",
        "# module load anaconda3/2024.02",
        "# conda activate quest_planning",
        "#",
        "# Option C: pre-built conda env via full path (most portable)",
        "# source /path/to/miniconda3/etc/profile.d/conda.sh",
        "# conda activate quest_planning",
        "",
    ]

    if solver == "gurobi":
        lines += [
            "# --- Gurobi (detected: solver=gurobi in your study spec) -----------------",
            "# Uncomment and set the correct version for your cluster:",
            "#",
            "# module load gurobi/11.0",
            "#",
            "# GRB_LICENSE_FILE is set automatically by submit_array.sh from",
            "# the gurobi_license_file value in your study spec -- no action needed here.",
            "",
        ]
    elif solver in ("cplex", "CPLEX"):
        lines += [
            "# --- CPLEX (detected: solver=cplex in your study spec) -------------------",
            "# module load cplex/22.1",
            "",
        ]
    elif solver in ("HiGHs", "highs"):
        lines += [
            "# --- HiGHs (open-source; no module load typically needed) ----------------",
            "# HiGHs is installed via pip as part of the Python environment.",
            "# No additional module load is required.",
            "",
        ]

    if use_mpi:
        lines += [
            "# --- MPI (detected: num_mpi_processes > 0 in at least one scenario) ------",
            "# Required for ProGRESS parallel reliability assessment post-processing.",
            "#",
            "# module load openmpi/4.1",
            "# module load mpich/4.0",
            "",
        ]
    else:
        lines += [
            "# --- MPI (not needed: num_mpi_processes=0 in all scenarios) --------------",
            "# If you later enable ProGRESS MPI post-processing, uncomment:",
            "# module load openmpi/4.1",
            "",
        ]

    lines += [
        "# =============================================================================",
        "# Add any other site-specific setup below (e.g. ulimit, proxy settings):",
        "# =============================================================================",
        "",
    ]

    content = "\n".join(lines)
    modules_path = output_dir / "modules.sh"
    modules_path.write_text(content)
    os.chmod(modules_path, 0o755)
    return str(modules_path)


def _study_uses_mpi(spec: dict) -> bool:
    """Return True if any scenario in the study may use MPI (ProGRESS)."""
    base_cfg_path = spec.get("base_config", "")
    try:
        base = _load_yaml(base_cfg_path)
        if base.get("num_mpi_processes", 0) > 0:
            return True
    except Exception:
        pass
    # Also check sweep/oat/sensitivity axes
    for block_key in ("sweep", "sensitivity"):
        for k, vals in spec.get(block_key, {}).items():
            if k == "num_mpi_processes" and any(v > 0 for v in vals):
                return True
    for sc in spec.get("scenarios", []):
        if sc.get("num_mpi_processes", 0) > 0:
            return True
    return False


# ---------------------------------------------------------------------------
# SLURM script generator
# ---------------------------------------------------------------------------

def _generate_slurm_script(
    spec: dict,
    n_jobs: int,
    output_dir: Path,
    manifest_path: Path,
    gurobi_license_file: str,
    quest_repo_path: str,
) -> str:
    """Write a ready-to-submit SLURM job array script."""

    slurm = spec.get("slurm", {})
    job_name        = slurm.get("job_name",       "quest_study")
    cpus_per_task   = spec.get("solver_threads",  8)
    mem             = slurm.get("mem",             "32G")
    time_limit      = slurm.get("time",            "04:00:00")
    partition       = slurm.get("partition",       "")
    account         = slurm.get("account",         "")
    max_concurrent  = slurm.get("max_concurrent_jobs", 20)
    array_spec      = f"0-{n_jobs - 1}%{max_concurrent}"

    partition_line = f"#SBATCH --partition={partition}" if partition else "##SBATCH --partition=<your_partition>  # uncomment and set"
    account_line   = f"#SBATCH --account={account}"     if account   else "##SBATCH --account=<your_account>      # uncomment and set"

    script = textwrap.dedent(f"""\
        #!/bin/bash
        # =============================================================================
        # submit_array.sh  --  Auto-generated by hpc/study_builder.py
        # =============================================================================
        # SLURM job array for QuESt Planning large-scale case study.
        #
        # Submit with:
        #   sbatch {output_dir}/submit_array.sh
        #
        # Monitor with:
        #   squeue -u $USER -j <JOBID>
        #   sacct  -j <JOBID> --format=JobID,JobName,State,Elapsed,MaxRSS
        # =============================================================================

        #SBATCH --job-name={job_name}
        #SBATCH --array={array_spec}
        #SBATCH --ntasks=1
        #SBATCH --cpus-per-task={cpus_per_task}
        #SBATCH --mem={mem}
        #SBATCH --time={time_limit}
        #SBATCH --output={output_dir}/logs/job_%A_%a.out
        #SBATCH --error={output_dir}/logs/job_%A_%a.err
        {partition_line}
        {account_line}

        # ---------------------------------------------------------------------------
        # Environment
        # ---------------------------------------------------------------------------
        # Source site-specific module loads (edit modules.sh for your cluster).
        source "{output_dir}/modules.sh"

        # Floating Gurobi license server.  Set to the token-server address or
        # path to a gurobi.lic file; overrides any $HOME/gurobi.lic.
        export GRB_LICENSE_FILE="{gurobi_license_file}"

        # Retry parameters for floating-license contention (see hpc/gurobi_retry.py).
        # Increase QUEST_GRB_MAX_RETRIES if jobs still fail during peak usage.
        export QUEST_GRB_MAX_RETRIES=10
        export QUEST_GRB_INITIAL_WAIT=30
        export QUEST_GRB_MAX_WAIT=300

        # ---------------------------------------------------------------------------
        # Determine config file for this array task
        # ---------------------------------------------------------------------------
        # manifest.csv column layout: job_id, config_path, [param columns ...]
        # awk skips the header row (NR==1) and selects the row matching this task.
        CONFIG=$(awk -F, -v idx="$SLURM_ARRAY_TASK_ID" \\
            'NR > 1 && $1 == idx {{ print $2 }}' "{manifest_path}")

        if [[ -z "$CONFIG" ]]; then
            echo "ERROR: Could not find config for SLURM_ARRAY_TASK_ID=$SLURM_ARRAY_TASK_ID" >&2
            exit 1
        fi

        echo "============================================================"
        echo "Job array task : $SLURM_ARRAY_TASK_ID"
        echo "Config file    : $CONFIG"
        echo "Node           : $(hostname)"
        echo "CPUs allocated : $SLURM_CPUS_PER_TASK"
        echo "Started        : $(date)"
        echo "============================================================"

        # ---------------------------------------------------------------------------
        # Run QuESt Planning
        # ---------------------------------------------------------------------------
        cd "{quest_repo_path}"
        python -m quest_planning.explan_simulation "$CONFIG"
        EXIT_CODE=$?

        echo "============================================================"
        echo "Finished : $(date)  |  Exit code : $EXIT_CODE"
        echo "============================================================"
        exit $EXIT_CODE
    """)

    script_path = output_dir / "submit_array.sh"
    script_path.write_text(script)
    os.chmod(script_path, 0o755)
    return str(script_path)


# ---------------------------------------------------------------------------
# Manifest writer
# ---------------------------------------------------------------------------

def _write_manifest(
    jobs: list[dict],
    config_paths: list[Path],
    param_keys: list[str],
    output_dir: Path,
) -> Path:
    manifest_path = output_dir / "manifest.csv"
    with open(manifest_path, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["job_id", "config_path"] + param_keys)
        for job_id, (params, config_path) in enumerate(zip(jobs, config_paths)):
            row = [job_id, str(config_path)]
            for k in param_keys:
                row.append(params.get(k, ""))
            writer.writerow(row)
    return manifest_path


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def build_study(spec_path: str | Path, dry_run: bool = False) -> None:
    spec_path = Path(spec_path).resolve()
    spec = _load_yaml(spec_path)

    mode = spec.get("mode", "sweep").lower()
    if mode not in ("sweep", "oat", "ensemble"):
        raise ValueError(f"Unknown mode '{mode}'. Must be one of: sweep, oat, ensemble.")

    # Resolve paths
    base_config_path = Path(spec["base_config"])
    if not base_config_path.is_absolute():
        base_config_path = (spec_path.parent / base_config_path).resolve()
    base_config = _load_yaml(base_config_path)

    output_dir = Path(spec["output_dir"]).expanduser()
    gurobi_license_file = spec.get("gurobi_license_file", "/path/to/gurobi.lic")
    solver_threads = int(spec.get("solver_threads", 8))
    quest_repo_path = str(spec.get("quest_repo_path", Path(__file__).resolve().parent.parent))

    # Generate per-job parameter dicts
    if mode == "sweep":
        jobs = _jobs_sweep(spec)
    elif mode == "oat":
        jobs = _jobs_oat(spec)
    else:
        jobs = _jobs_ensemble(spec)

    n_jobs = len(jobs)
    print(f"Study mode    : {mode}")
    print(f"Base config   : {base_config_path}")
    print(f"Output dir    : {output_dir}")
    print(f"Jobs to create: {n_jobs}")

    if dry_run:
        print("\n--- DRY RUN: manifest preview ---")
        param_keys = _infer_param_keys(jobs)
        for i, params in enumerate(jobs):
            print(f"  job_{i:03d}  {params}")
        return

    # Create directory structure
    configs_dir = output_dir / "configs"
    logs_dir    = output_dir / "logs"
    for d in (output_dir, configs_dir, logs_dir):
        d.mkdir(parents=True, exist_ok=True)

    # Write per-job YAML configs
    config_paths: list[Path] = []
    for job_id, params in enumerate(jobs):
        config = _build_job_config(
            base_config=base_config,
            params=params,
            job_id=job_id,
            output_dir=output_dir,
            gurobi_license_file=gurobi_license_file,
            solver_threads=solver_threads,
            quest_repo_path=quest_repo_path,
        )
        # Create per-job results dir so the optimizer doesn't race on mkdir
        results_dir = Path(config["results_dir"])
        results_dir.mkdir(parents=True, exist_ok=True)

        config_path = configs_dir / f"job_{job_id:03d}.yaml"
        with open(config_path, "w") as fh:
            yaml.dump(config, fh, default_flow_style=False, sort_keys=False)
        config_paths.append(config_path)

    # Write manifest
    param_keys = _infer_param_keys(jobs)
    manifest_path = _write_manifest(jobs, config_paths, param_keys, output_dir)
    print(f"Manifest      : {manifest_path}  ({n_jobs} rows)")

    # Write modules.sh
    modules_path = _generate_modules_sh(spec, output_dir)
    print(f"modules.sh    : {modules_path}  (edit for your cluster)")

    # Write submit_array.sh
    script_path = _generate_slurm_script(
        spec=spec,
        n_jobs=n_jobs,
        output_dir=output_dir,
        manifest_path=manifest_path,
        gurobi_license_file=gurobi_license_file,
        quest_repo_path=quest_repo_path,
    )
    print(f"SLURM script  : {script_path}")
    print(f"\nTo submit: sbatch {script_path}")
    print(f"To aggregate results after completion:")
    print(f"  python hpc/aggregate_results.py {manifest_path}")


def _infer_param_keys(jobs: list[dict]) -> list[str]:
    """Return sorted union of all parameter keys across all jobs, excluding HPC internals."""
    _internal = {"name"}
    keys: set[str] = set()
    for j in jobs:
        keys.update(k for k in j.keys() if k not in _internal)
    return sorted(keys)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate QuESt Planning HPC job array from a study spec YAML."
    )
    parser.add_argument("spec", help="Path to study_spec.yaml")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print manifest preview without writing files.",
    )
    args = parser.parse_args()
    build_study(args.spec, dry_run=args.dry_run)

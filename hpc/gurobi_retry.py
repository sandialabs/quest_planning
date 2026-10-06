# -*- coding: utf-8 -*-
"""
hpc/gurobi_retry.py
====================
Floating Gurobi license retry wrapper for HPC job arrays.

When many jobs start simultaneously on an HPC cluster, they compete for
tokens on the floating license server. Gurobi raises error code 10009
("No license tokens available") when all tokens are checked out. This
module wraps the Pyomo SolverFactory.solve() call with exponential-backoff
retries so individual jobs wait and retry rather than failing immediately.

Usage
-----
This module is imported by optimizer.py when solver == "gurobi". You do not
need to call it directly; it is transparent to the rest of the codebase.

The retry behaviour is controlled by three environment variables so it can be
tuned without modifying code:

    QUEST_GRB_MAX_RETRIES   int   Max number of retry attempts        (default 10)
    QUEST_GRB_INITIAL_WAIT  float Initial wait in seconds             (default 30)
    QUEST_GRB_MAX_WAIT      float Cap on per-attempt wait in seconds  (default 300)

If a solve ultimately fails after all retries, the original exception is
re-raised so SLURM captures the non-zero exit code and marks the job failed.
"""

import os
import time
import logging
import random

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration (overridable via environment variables)
# ---------------------------------------------------------------------------
_MAX_RETRIES   = int(os.environ.get("QUEST_GRB_MAX_RETRIES",  "10"))
_INITIAL_WAIT  = float(os.environ.get("QUEST_GRB_INITIAL_WAIT", "30"))
_MAX_WAIT      = float(os.environ.get("QUEST_GRB_MAX_WAIT",    "300"))

# Gurobi error code returned when no license token is available.
# gurobipy raises GurobiError with errno == 10009 in this situation.
_GRB_LICENSE_UNAVAILABLE = 10009


def _is_license_error(exc: Exception) -> bool:
    """Return True if *exc* represents a Gurobi license-unavailable error.

    Gurobi surfaces this in two ways depending on how Pyomo invokes it:
      1. gurobipy.GurobiError with .errno == 10009
      2. A plain Exception/RuntimeError whose string representation contains
         '10009' or 'No license tokens available'
    """
    # Attempt to read the gurobipy errno attribute if present.
    errno = getattr(exc, "errno", None)
    if errno == _GRB_LICENSE_UNAVAILABLE:
        return True
    msg = str(exc).lower()
    return "10009" in msg or "no license tokens" in msg or "license" in msg and "available" in msg


def solve_with_retry(solver, model, **solve_kwargs):
    """Invoke ``solver.solve(model, **solve_kwargs)`` with exponential backoff.

    Parameters
    ----------
    solver : pyomo SolverFactory instance
        A SolverFactory("gurobi") object that has already been configured
        (options set, etc.).
    model : pyomo ConcreteModel
        The model to solve.
    **solve_kwargs :
        Any additional keyword arguments forwarded to solver.solve()
        (e.g. tee=True, keepfiles=False).

    Returns
    -------
    results : pyomo SolverResults
        The results object returned by solver.solve() on success.

    Raises
    ------
    Exception
        The last exception encountered after all retries are exhausted, or
        any non-license-related exception on the first attempt.
    """
    wait = _INITIAL_WAIT
    last_exc = None

    for attempt in range(1, _MAX_RETRIES + 2):  # +2: attempt 1 is the initial try
        try:
            results = solver.solve(model, **solve_kwargs)
            if attempt > 1:
                logger.info(
                    "Gurobi license acquired on attempt %d after waiting.",
                    attempt,
                )
            return results

        except Exception as exc:
            if not _is_license_error(exc):
                # Non-license error — re-raise immediately, do not retry.
                raise

            last_exc = exc
            if attempt > _MAX_RETRIES:
                break

            # Add a small random jitter (±20 % of wait) to reduce thundering
            # herd when many jobs restart at the same time.
            jitter = wait * 0.2 * (random.random() * 2 - 1)
            actual_wait = max(1.0, wait + jitter)

            logger.warning(
                "Gurobi license unavailable (attempt %d/%d). "
                "Retrying in %.0f s. Error: %s",
                attempt,
                _MAX_RETRIES,
                actual_wait,
                exc,
            )
            print(
                f"[gurobi_retry] License unavailable (attempt {attempt}/{_MAX_RETRIES}). "
                f"Retrying in {actual_wait:.0f}s …"
            )
            time.sleep(actual_wait)

            # Exponential backoff capped at _MAX_WAIT.
            wait = min(wait * 2, _MAX_WAIT)

    # All retries exhausted.
    logger.error(
        "Gurobi license could not be obtained after %d attempts. Giving up.",
        _MAX_RETRIES,
    )
    raise last_exc

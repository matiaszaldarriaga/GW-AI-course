# `results/sqrtSH_realizations_lmax6.npz`

**Generating script:** `scripts/run_sqrtSH_realizations.py` (lmax_blm-parameterized path)
**Commit:** `926ec5f` (feat: add lmax convergence study to sqrt-SH notebook)
**Generated:** 2026-04-04

## Purpose

Intermediate truncation run: $L_{\max}^b = 6$, producing power up to
$\ell_{\max}^a = 12$ in the squared field, recorded with `lmax=23`
(anafast truncation). Bridges the NANOGrav-faithful `lmax3` run and the
full-lmax default runs. Used in the convergence study to show how the
$C_\ell/C_0$ prior distribution shifts as the number of free $b_{LM}$
modes increases.

## Parameters

| Parameter | Value |
|---|---|
| `nside` | 8 |
| `lmax` ($\ell_{\max}^a$, anafast) | 23 |
| `lmax_blm` ($L_{\max}^b$) | 6 |
| `Nrel` | 10 000 |
| `seed` | 42 |
| `n_example_maps` | 0 |

## Arrays

| Key | Shape | dtype | Units / notes |
|---|---|---|---|
| `nside` | scalar | int | 8 |
| `lmax` | scalar | int | 23 |
| `lmax_blm` | scalar | int | 6 |
| `Nrel` | scalar | int | 10 000 |
| `seed` | scalar | int | 42 |
| `n_example_maps` | scalar | int | 0 |
| `cls_all` | (10000, 24) | float64 | Raw $C_\ell$, $\ell=0\ldots23$ |
| `c0_all` | (10000,) | float64 | $C_0$ per realization |
| `example_maps` | (0, 0) | float64 | Empty — maps not saved |
| `cl_norm_mean` | (23,) | float64 | Mean of $C_\ell/C_0$, $\ell=1\ldots23$ |
| `cl_norm_median` | (23,) | float64 | Median |
| `cl_norm_pct_2p5` | (23,) | float64 | 2.5th percentile |
| `cl_norm_pct_25` | (23,) | float64 | 25th percentile |
| `cl_norm_pct_75` | (23,) | float64 | 75th percentile |
| `cl_norm_pct_97p5` | (23,) | float64 | 97.5th percentile |

## Key statistics

| | $C_1/C_0$ | $C_2/C_0$ |
|---|---|---|
| Mean | 0.0334 | — |
| 97.5th pct | 0.1007 | 0.0784 |

Doubling $L_{\max}^b$ from 3 to 6 reduces the 97.5th-percentile $C_1/C_0$
from 0.233 to 0.101 — a factor of ~2.3. Increasing further to $L_{\max}^b = 23$
(nside8 default) reduces it to 0.010 (another factor ~10). The suppression
accelerates as more modes are added, consistent with the general
argument that the prior is non-convergent.

## Consumers

- `notebooks/guide_sqrtSH_model.py` — convergence study plots.

## Related pages

[[../code/scripts_run_sqrtSH]], [[sqrtSH_realizations_lmax3]],
[[sqrtSH_realizations_nside8]], [[../concepts/sqrt_SH_basis]],
[[../concepts/Cl_over_C0]], [[../concepts/prior_sensitivity]]

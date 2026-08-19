# `results/sqrtSH_realizations_nside16.npz`

**Generating script:** `scripts/run_sqrtSH_realizations.py --nside 16`
**Commit:** `926ec5f` (feat: add lmax convergence study to sqrt-SH notebook)
**Generated:** 2026-04-04

## Purpose

Mid-resolution convergence run. Doubling `nside` from 8 to 16 increases
the $b_{LM}$ expansion depth from $L_{\max}^b = 23$ to $L_{\max}^b = 47$
(via `lmax = 3*nside - 1 = 47`). Tests whether the nside=8 $C_\ell/C_0$
statistics have stabilized or continue to shrink.

## Parameters

| Parameter | Value |
|---|---|
| `nside` | 16 |
| `lmax` ($\ell_{\max}^a = 3 \times 16 - 1$) | 47 |
| `Nrel` | 10 000 |
| `seed` | 42 |
| `n_example_maps` | 50 |

## Arrays

| Key | Shape | dtype | Units / notes |
|---|---|---|---|
| `nside` | scalar | int | 16 |
| `lmax` | scalar | int | 47 |
| `Nrel` | scalar | int | 10 000 |
| `seed` | scalar | int | 42 |
| `n_example_maps` | scalar | int | 50 |
| `cls_all` | (10000, 48) | float64 | Raw $C_\ell$, $\ell=0\ldots47$ |
| `c0_all` | (10000,) | float64 | $C_0$ per realization |
| `example_maps` | (50, 3072) | float64 | First 50 power maps; 3072 = `hp.nside2npix(16)` |
| `cl_norm_mean` | (47,) | float64 | Mean of $C_\ell/C_0$, $\ell=1\ldots47$ |
| `cl_norm_median` | (47,) | float64 | Median |
| `cl_norm_pct_2p5` | (47,) | float64 | 2.5th percentile |
| `cl_norm_pct_25` | (47,) | float64 | 25th percentile |
| `cl_norm_pct_75` | (47,) | float64 | 75th percentile |
| `cl_norm_pct_97p5` | (47,) | float64 | 97.5th percentile |

## Key statistics

| | $C_1/C_0$ | $C_2/C_0$ |
|---|---|---|
| Mean | 0.0009 | — |
| 97.5th pct | 0.0027 | 0.0021 |

The 97.5th-percentile $C_1/C_0$ drops from 0.0101 (nside=8) to 0.0027
(nside=16), a factor of ~3.7. The distribution has not converged; it
continues to compress at nside=32 (0.0007).

## Consumers

- `notebooks/guide_sqrtSH_model.py` — convergence study plots.

## Related pages

[[../code/scripts_run_sqrtSH]], [[sqrtSH_realizations_nside8]],
[[sqrtSH_realizations_nside32]], [[../concepts/sqrt_SH_basis]],
[[../concepts/prior_sensitivity]]

# `results/sqrtSH_realizations_nside8.npz`

**Generating script:** `scripts/run_sqrtSH_realizations.py --nside 8`
**Commit:** `926ec5f` (feat: add lmax convergence study to sqrt-SH notebook)
**Generated:** 2026-04-04

## Purpose

Named default run at `nside=8`. Parameters are identical to the original
`sqrtSH_realizations.npz` (same seed, nside, lmax, Nrel), produced when
the script was refactored to accept `--nside` and output
`sqrtSH_realizations_nside{nside}.npz`. Serves as the low-resolution
anchor for the nside convergence study (`nside8` / `nside16` / `nside32`).

## Parameters

| Parameter | Value |
|---|---|
| `nside` | 8 |
| `lmax` ($\ell_{\max}^a = 3 \times \mathrm{nside} - 1$) | 23 |
| `Nrel` | 10 000 |
| `seed` | 42 |
| `n_example_maps` | 50 |

No separate `lmax_blm` key; the $b_{LM}$ expansion runs to `lmax=23`.

## Arrays

| Key | Shape | dtype | Units / notes |
|---|---|---|---|
| `nside` | scalar | int | 8 |
| `lmax` | scalar | int | 23 |
| `Nrel` | scalar | int | 10 000 |
| `seed` | scalar | int | 42 |
| `n_example_maps` | scalar | int | 50 |
| `cls_all` | (10000, 24) | float64 | Raw $C_\ell$, $\ell=0\ldots23$ |
| `c0_all` | (10000,) | float64 | $C_0$ per realization |
| `example_maps` | (50, 768) | float64 | First 50 power maps; 768 = `hp.nside2npix(8)` |
| `cl_norm_mean` | (23,) | float64 | Mean of $C_\ell/C_0$, $\ell=1\ldots23$ |
| `cl_norm_median` | (23,) | float64 | Median |
| `cl_norm_pct_2p5` | (23,) | float64 | 2.5th percentile |
| `cl_norm_pct_25` | (23,) | float64 | 25th percentile |
| `cl_norm_pct_75` | (23,) | float64 | 75th percentile |
| `cl_norm_pct_97p5` | (23,) | float64 | 97.5th percentile |

## Key statistics

| | $C_1/C_0$ | $C_2/C_0$ |
|---|---|---|
| Mean | 0.0034 | — |
| 97.5th pct | 0.0101 | 0.0086 |

Compare with `nside16` (97.5th pct $C_1/C_0 = 0.0027$) and `nside32`
(0.0007): the distribution compresses toward zero monotonically as `nside`
(and hence $L_{\max}^b$) increases.

## Consumers

- `notebooks/guide_sqrtSH_model.py` — convergence study.

## Related pages

[[../code/scripts_run_sqrtSH]], [[sqrtSH_realizations]],
[[sqrtSH_realizations_nside16]], [[sqrtSH_realizations_nside32]],
[[../concepts/sqrt_SH_basis]], [[../concepts/prior_sensitivity]]

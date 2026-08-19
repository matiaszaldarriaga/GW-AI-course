# `results/sqrtSH_realizations_nside32.npz`

**Generating script:** `scripts/run_sqrtSH_realizations.py --nside 32`
**Commit:** `926ec5f` (feat: add lmax convergence study to sqrt-SH notebook)
**Generated:** 2026-04-04

## Purpose

High-resolution convergence run: $L_{\max}^b = 95$ (via `lmax = 3*32 - 1 = 95`).
This is the "large-lmax limit" end of the convergence study. At this
resolution, $C_1/C_0$ is suppressed by a further factor of ~4 compared
to nside=16 and ~14 compared to nside=8. Combined with the `lmax3` and
`lmax6` results, these numbers establish that the prior on $C_\ell/C_0$
in the NANOGrav analysis ($L_{\max}^b = 3$) is orders of magnitude
wider than the large-lmax limit and is not a physically motivated
regularization.

## Parameters

| Parameter | Value |
|---|---|
| `nside` | 32 |
| `lmax` ($\ell_{\max}^a = 3 \times 32 - 1$) | 95 |
| `Nrel` | 10 000 |
| `seed` | 42 |
| `n_example_maps` | 50 |

## Arrays

| Key | Shape | dtype | Units / notes |
|---|---|---|---|
| `nside` | scalar | int | 32 |
| `lmax` | scalar | int | 95 |
| `Nrel` | scalar | int | 10 000 |
| `seed` | scalar | int | 42 |
| `n_example_maps` | scalar | int | 50 |
| `cls_all` | (10000, 96) | float64 | Raw $C_\ell$, $\ell=0\ldots95$ |
| `c0_all` | (10000,) | float64 | $C_0$ per realization |
| `example_maps` | (50, 12288) | float64 | First 50 power maps; 12288 = `hp.nside2npix(32)` |
| `cl_norm_mean` | (95,) | float64 | Mean of $C_\ell/C_0$, $\ell=1\ldots95$ |
| `cl_norm_median` | (95,) | float64 | Median |
| `cl_norm_pct_2p5` | (95,) | float64 | 2.5th percentile |
| `cl_norm_pct_25` | (95,) | float64 | 25th percentile |
| `cl_norm_pct_75` | (95,) | float64 | 75th percentile |
| `cl_norm_pct_97p5` | (95,) | float64 | 97.5th percentile |

## Key statistics

| | $C_1/C_0$ | $C_2/C_0$ |
|---|---|---|
| Mean | 0.0002 | — |
| 97.5th pct | 0.0007 | 0.0006 |

Ratio of 97.5th-percentile $C_1/C_0$ relative to the NANOGrav-faithful
`lmax3` run (0.2333): approximately 330x smaller. This is the quantitative
statement that "the constraint is the prior" at the $L_{\max}^b = 3$
truncation.

## Consumers

- `notebooks/guide_sqrtSH_model.py` — convergence study; used as upper
  bound in convergence panel.
- Paper section `nanograv_prior.tex` — cited alongside `lmax3` to
  bracket the prior sensitivity.

## Related pages

[[../code/scripts_run_sqrtSH]], [[sqrtSH_realizations_nside8]],
[[sqrtSH_realizations_nside16]], [[sqrtSH_realizations_lmax3]],
[[../concepts/sqrt_SH_basis]], [[../concepts/prior_sensitivity]],
[[../concepts/Cl_over_C0]]

# `results/sqrtSH_realizations_lmax3.npz`

**Generating script:** `scripts/run_sqrtSH_realizations.py` (lmax_blm-parameterized path)
**Commit:** `926ec5f` (feat: add lmax convergence study to sqrt-SH notebook)
**Generated:** 2026-04-04

## Purpose

NANOGrav-faithful realization set. The $b_{LM}$ expansion is truncated at
$L_{\max}^b = 3$, matching the NANOGrav 15yr anisotropy analysis
(2306.16221, $\ell_{\max}^a = 6 \Rightarrow L_{\max}^b = 3$ by the
Clebsch-Gordan truncation rule). The power map is computed at `nside=32` for
clean pixel-space representation. $N_{\rm rel} = 50\,000$ (5x the other
runs) for robust percentile estimation.

This file's $C_\ell/C_0$ statistics are the primary numerical evidence for the
"constraint is the prior" argument: the 97.5th-percentile $C_1/C_0 = 0.23$
under this prior, far above astrophysical expectations.

## Parameters

| Parameter | Value |
|---|---|
| `nside` | 32 |
| `lmax` ($\ell_{\max}^a$) | 6 |
| `lmax_blm` ($L_{\max}^b$) | 3 |
| `Nrel` | 50 000 |
| `seed` | 42 |
| `n_example_maps` | 0 |

## Arrays

| Key | Shape | dtype | Units / notes |
|---|---|---|---|
| `nside` | scalar | int | 32 |
| `lmax` | scalar | int | 6 ($\ell_{\max}^a$) |
| `lmax_blm` | scalar | int | 3 ($L_{\max}^b$) |
| `Nrel` | scalar | int | 50 000 |
| `seed` | scalar | int | 42 |
| `n_example_maps` | scalar | int | 0 |
| `cls_all` | (50000, 7) | float64 | Raw $C_\ell$, $\ell=0\ldots6$; index 0 = $C_0$ |
| `c0_all` | (50000,) | float64 | $C_0$ per realization |
| `example_maps` | (0, 0) | float64 | Empty — maps not saved for this run |
| `cl_norm_mean` | (6,) | float64 | Mean of $C_\ell/C_0$, $\ell=1\ldots6$ |
| `cl_norm_median` | (6,) | float64 | Median |
| `cl_norm_pct_2p5` | (6,) | float64 | 2.5th percentile |
| `cl_norm_pct_25` | (6,) | float64 | 25th percentile |
| `cl_norm_pct_75` | (6,) | float64 | 75th percentile |
| `cl_norm_pct_97p5` | (6,) | float64 | 97.5th percentile |

## Key statistics

| | $C_1/C_0$ | $C_2/C_0$ |
|---|---|---|
| Mean | 0.0795 | — |
| 97.5th pct | 0.2333 | 0.1788 |

For comparison, the astrophysical SMBHB signal has $C_1/C_0 \sim p^2 \ll 1$.
The factor ~23x difference between the NANOGrav prior mean (0.0795) and
the nside=32 full-lmax mean (0.0002) shows that the upper limit shrinks
by orders of magnitude as the prior is made less informative.

## Consumers

- `notebooks/guide_sqrtSH_model.py` — primary consumer; plots this alongside
  lmax6 and nside convergence runs.
- Paper section `nanograv_prior.tex` — cites these statistics directly.

## Related pages

[[../code/scripts_run_sqrtSH]], [[sqrtSH_realizations_lmax6]],
[[../concepts/sqrt_SH_basis]], [[../concepts/Cl_over_C0]],
[[../concepts/prior_sensitivity]]

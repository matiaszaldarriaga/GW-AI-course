# `results/sqrtSH_realizations.npz`

**Generating script:** `scripts/run_sqrtSH_realizations.py`
**Commit:** `461b99a` (feat: add sqrt-SH model realizations and notebook)
**Generated:** 2026-04-04
**Note:** This is the original default-run file. Parameters are identical to
`sqrtSH_realizations_nside8.npz` (same seed, nside, lmax, Nrel); compare
arrays before treating the two as interchangeable.

## Parameters

| Parameter | Value |
|---|---|
| `nside` | 8 |
| `lmax` ($\ell_{\max}^a$) | 23 |
| `Nrel` | 10 000 |
| `seed` | 42 |
| `n_example_maps` | 50 |

The $b_{LM}$ expansion runs up to $L_{\max}^b = 23$ (same as `lmax`; no
separate truncation). NANOGrav-faithful $L_{\max}^b = 3$ is in
`sqrtSH_realizations_lmax3.npz`.

## Arrays

| Key | Shape | dtype | Units / notes |
|---|---|---|---|
| `nside` | scalar | int | HEALPix resolution |
| `lmax` | scalar | int | Anafast truncation |
| `Nrel` | scalar | int | Number of realizations |
| `seed` | scalar | int | RNG seed |
| `n_example_maps` | scalar | int | 50 |
| `cls_all` | (10000, 24) | float64 | Raw $C_\ell$ for all realizations; index 0 = $C_0$ |
| `c0_all` | (10000,) | float64 | $C_0$ per realization; equals `cls_all[:,0]` |
| `example_maps` | (50, 768) | float64 | First 50 pixelized power maps $P(\hat n)$; 768 = `hp.nside2npix(8)` |
| `cl_norm_mean` | (23,) | float64 | Mean of $C_\ell/C_0$ over realizations, $\ell = 1\ldots23$ |
| `cl_norm_median` | (23,) | float64 | Median of $C_\ell/C_0$ |
| `cl_norm_pct_2p5` | (23,) | float64 | 2.5th percentile of $C_\ell/C_0$ |
| `cl_norm_pct_25` | (23,) | float64 | 25th percentile |
| `cl_norm_pct_75` | (23,) | float64 | 75th percentile |
| `cl_norm_pct_97p5` | (23,) | float64 | 97.5th percentile (= 95% upper bound) |

## Key statistics

| | $C_1/C_0$ | $C_2/C_0$ |
|---|---|---|
| Mean | 0.0034 | — |
| 97.5th pct | 0.0101 | 0.0086 |

## Consumers

- `notebooks/guide_sqrtSH_model.py`
- Paper section `nanograv_prior.tex`

## Related pages

[[../code/scripts_run_sqrtSH]], [[../concepts/sqrt_SH_basis]],
[[../concepts/Cl_over_C0]], [[../concepts/prior_sensitivity]]

## 2026-08-11 paired analytic convergence product

The historical pixel products above remain controls. Registered
high-$\ell_{\max}^b$ values now come from
`results/sqrtSH_full_moment_v2/sqrtSH_low_moments_convergence.npz`, generated
with seed 42, 10,000 paired realizations, and nested truncations
$\ell_{\max}^b=3,6,23,47,95$. The 95th percentiles of $C_1/C_0$ are:

| $\ell_{\max}^b$ | 3 | 6 | 23 | 47 | 95 |
|---:|---:|---:|---:|---:|---:|
| 95th percentile | 0.20243 | 0.085894 | 0.0087566 | 0.0022178 | 0.0005640 |

$C_0$ and $C_1$ are computed analytically from the squared harmonic field.
High-margin pixel validations at $N_{\rm side}=16,32,64,128,256$ shift the
ratios by at most $2.47\times10^{-5}$ down to $7.52\times10^{-9}$ across the
sequence, comfortably below the displayed precision. The internal runtime was
4.0 s (5.81 s wall including environment startup).

# `results/power_anisotropy_eps020.npz`

**Generating script:** `scripts/run_power_anisotropy.py --eps 0.20`
**Script page:** `[[../code/scripts_run_power]]`
**Git commit (script parameterized):** `316982b`
**Ingested:** 2026-04-13

## Parameters

| Parameter | Value |
|---|---|
| $\varepsilon$ (M-sigma scatter) | 0.20 dex |
| Nrel (realizations) | 10 000 |
| nside | 8 |
| N_brightest | 100 |
| seed | 42 |
| Nfreq | 44 |
| npix | 768 (= 12 × 8²) |
| lmax | 23 (= 3 × nside − 1) |
| Exclusion levels | [1, 5, 10, 20] |
| Percentiles stored | [2.5, 25, 50, 75, 97.5] |

Low-scatter case: $\varepsilon = 0.20$ dex suppresses the high-mass tail,
yielding a less concentrated source population than the fiducial
$\varepsilon = 0.66$ run. Expect smaller brightest-source fraction $p$
and weaker power anisotropy. See `[[../concepts/SMBH_population_model]]`.

## Arrays

| Key | dtype | shape | Units / notes |
|---|---|---|---|
| `fmean_per_year` | float64 | (44,) | Mean frequency per bin, yr$^{-1}$; range ~0.085–2.78 yr$^{-1}$ |
| `h2c_vs_f` | float64 | (44,) | $\sum_{M,z,q} N_{\rm bin}\,h_s^2$ vs frequency (isotropic background power) |
| `Nrel` | int64 | scalar | 10 000 |
| `nside` | int64 | scalar | 8 |
| `N_brightest` | int64 | scalar | 100 |
| `seed` | int64 | scalar | 42 |
| `Nfreq` | int64 | scalar | 44 |
| `npix` | int64 | scalar | 768 |
| `lmax` | int64 | scalar | 23 |
| `power_maps` | float64 | (10000, 44, 768) | HEALPix power maps $P(\hat n)$ per realization per frequency |
| `brightest_h2s` | float64 | (10000, 44, 100) | $h_s^2$ of top-100 sources, sorted descending; zero-padded if fewer |
| `cls_all` | float64 | (10000, 44, 24) | $C_\ell^{(P)}$, all sources; index 0 = $C_0$, index $\ell$ = $C_\ell$ |
| `exclusion_levels` | int64 | (4,) | [1, 5, 10, 20] |
| `cls_excl_1` | float64 | (10000, 44, 24) | $C_\ell^{(P)}$ after excluding top-1 source per frequency |
| `cls_excl_5` | float64 | (10000, 44, 24) | Excluding top-5 |
| `cls_excl_10` | float64 | (10000, 44, 24) | Excluding top-10 |
| `cls_excl_20` | float64 | (10000, 44, 24) | Excluding top-20 |
| `percentiles` | float64 | (5,) | [2.5, 25, 50, 75, 97.5] |
| `mean_all` | float64 | (44, 24) | Mean $C_\ell^{(P)}$ over realizations, all sources |
| `median_all` | float64 | (44, 24) | Median |
| `pct_all` | float64 | (5, 44, 24) | Percentiles [pct, freq, ell] |
| `mean_excl_N` / `median_excl_N` / `pct_excl_N` | float64 | (44,24) / (44,24) / (5,44,24) | Summary stats for each exclusion level N in {1,5,10,20} |

**Usage note:** $C_\ell/C_0$ ratios are obtained by dividing
`cls_all[:,:,ell]` by `cls_all[:,:,0]`. The array holds raw
`healpy.anafast` output; it is not pre-normalized.

## Consumers

- `notebooks/guide_power_anisotropy.py` (hardcoded to `eps066` by default; can be overridden)
- `notebooks/guide_model_comparison.py` — loads all three eps files for side-by-side comparison
- `notebooks/guide_dipole_analytics.py` — loads all three eps files

## Related pages

`[[../code/scripts_run_power]]`,
`[[power_anisotropy_eps038]]`, `[[power_anisotropy_eps066]]`,
`[[../concepts/Cl_over_C0]]`, `[[../concepts/brightest_source_fraction]]`,
`[[../concepts/SMBH_population_model]]`, `[[../concepts/shot_noise]]`

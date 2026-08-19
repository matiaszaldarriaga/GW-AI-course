# `results/population_analysis_eps066.npz`

**Generator:** [[code/scripts_run_population]]
**Parameters:** ε = 0.66
**Ingested:** 2026-04-13

## Contents

Identical array structure to [[results/population_analysis_eps020]]; only
the ε-dependent population outputs differ numerically. This is the default
ε value (the script default is `--eps 0.66`). See the eps020 page for the
full schema. Summary below.

### Scalar parameters (shape `()`)

`eps` = 0.66. All other fixed parameters identical to eps020 variant
(σ = 160, φ_σ = 2.611e-2, a_σ = 0.41, b_σ = 2.59, a_ms = 8.32,
b_ms = 5.64, B = 0.5, Z_s = 0.33, C = −1, Nrel = 10000, seed = 42).

### Key array shapes

| array | shape | dtype | meaning |
|---|---|---|---|
| `N_bin` | (44, 399) | float64 | mean source count per (frequency, mass) bin |
| `h2s` | (44, 399) | float64 | single-source strain-squared per bin |
| `h2c` | (44, 399) | float64 | background strain-squared per bin |
| `x_all` | (44, 397) | float64 | normalized strain grid for dN/dx |
| `dNdx_all` | (44, 397) | float64 | dN/dx luminosity function |
| `dx_all` | (44, 397) | float64 | bin widths in x |
| `lnSinter` | (44, 500) | float64 | log(S) interpolation nodes for strain PDF |
| `pinter` | (44, 500) | float64 | strain PDF p(S) at interpolation nodes |
| `S_freq{i}` | (16 777 216,) | float64 | strain-squared grid (i = 0,1,5,10,20,43) |
| `dNdS_freq{i}` | (16 777 216,) | float64 | dN/dS per representative frequency |
| `p_freq{i}` | (16 777 216,) | float64 | p(S) per representative frequency |
| `total_strain` | (10000, 44) | float64 | total strain-squared per realization |
| `brightest_strain` | (10000, 44) | float64 | brightest-source strain-squared |
| `counts` | (10000, 44) | float64 | total source count per realization |
| `total_strain_wo_brightest` | (10000, 44) | float64 | total minus brightest |
| `brightest_n_strains` | (10000, 44, 20) | float64 | top-20 source strains |
| `total_lower_strain` | (10000, 44) | float64 | sub-threshold strain sum |

Scalar 1-D grids (`zedges`, `zmean`, `Medges`, `Mmean`, `fedges`, `fmean`,
`fmean_per_year`, `qedges`, `qmean`, `sigma_grid`, `vdisp_values`,
`mass_grid`, `mass_function_values`, `Nc`, `h2smax`, `h2c_vs_f`, `xbar`,
`Nbar`, `Sbar`, `mean_faint`, `sigma_faint`, `Nbar_bright`, `lbl`)
have the same shapes as the eps020 file; see that page for definitions.

## Size on disk

2.3 GB

## Consumers

- `notebooks/guide_population_and_spectra.py`
- `notebooks/guide_model_comparison.py`

## Related pages

- [[code/scripts_run_population]]
- [[concepts/SMBH_population_model]]
- [[concepts/brightest_source_fraction]]
- [[results/population_analysis_eps020]]
- [[results/population_analysis_eps038]]

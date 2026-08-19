# `results/population_analysis_eps020.npz`

**Generator:** [[code/scripts_run_population]]
**Parameters:** ε = 0.20
**Ingested:** 2026-04-13

## Contents

### Scalar parameters (shape `()`)

| array | dtype | meaning |
|---|---|---|
| `eps` | float64 | M-sigma scatter parameter (0.20) |
| `sigma_param` | int64 | fiducial velocity dispersion (160 km/s) |
| `phi_sigma` | float64 | velocity-dispersion function normalization (2.611e-2) |
| `a_sigma`, `b_sigma` | float64 | velocity-dispersion power-law indices |
| `a_ms`, `b_ms` | float64 | M-sigma relation coefficients |
| `B`, `Zs`, `C` | float64/int64 | merger-rate parameters |
| `fmin` | float64 | minimum GW frequency in Hz (= 1/16.03 yr) |
| `htot0` | float64 | total background strain amplitude at f_ref |
| `Mmax`, `fone` | float64 | mass and frequency of loudest expected source |
| `Mmax_inter`, `fone_inter`, `h2s0max_inter` | float64 | interpolated counterparts |
| `Nfreq`, `Nmass` | int64 | grid dimensions (44, 399) |
| `Nrel`, `N_brightest_reals`, `seed` | int64 | realization metadata (10000, 20, 42) |

### 1-D grids

| array | shape | dtype | meaning |
|---|---|---|---|
| `zedges` | (20,) | float64 | redshift bin edges |
| `zmean` | (19,) | float64 | redshift bin centers |
| `Medges` | (400,) | float64 | log10(M/M☉) bin edges |
| `Mmean` | (399,) | float64 | M/M☉ bin centers |
| `fedges` | (45,) | float64 | GW frequency bin edges (Hz) |
| `fmean` | (44,) | float64 | GW frequency bin centers (Hz) |
| `fmean_per_year` | (44,) | float64 | GW frequency bin centers (yr^-1) |
| `qedges` | (20,) | float64 | mass-ratio bin edges |
| `qmean` | (19,) | float64 | mass-ratio bin centers |
| `sigma_grid` | (300,) | float64 | velocity-dispersion evaluation grid (km/s) |
| `vdisp_values` | (300,) | float64 | velocity-dispersion function on sigma_grid |
| `mass_grid` | (399,) | float64 | mass grid for SMBHB mass function (= Mmean) |
| `mass_function_values` | (399,) | float64 | SMBHB mass function dN/dM on mass_grid |
| `Nc` | (44,) | float64 | mean number of sources per frequency bin |
| `h2smax` | (44,) | float64 | strain-squared of brightest source vs frequency |
| `h2c_vs_f` | (44,) | float64 | mean background strain-squared vs frequency |
| `xbar` | (44,) | float64 | mean normalized strain per frequency |
| `Nbar` | (44,) | float64 | mean total source count per frequency |
| `Sbar` | (44,) | float64 | mean total strain-squared per frequency |
| `mean_faint` | (44,) | float64 | mean faint-background strain-squared per frequency |
| `sigma_faint` | (44,) | float64 | std of faint-background strain-squared per frequency |
| `Nbar_bright` | (44,) | float64 | mean count of bright sources per frequency |
| `lbl` | (44,) | <U6x | frequency-bin labels (strings) |

### 2-D arrays (frequency x mass or frequency x grid)

| array | shape | dtype | meaning |
|---|---|---|---|
| `N_bin` | (44, 399) | float64 | mean source count per (frequency, mass) bin |
| `h2s` | (44, 399) | float64 | single-source strain-squared per bin |
| `h2c` | (44, 399) | float64 | background strain-squared per bin |
| `x_all` | (44, 397) | float64 | normalized strain grid for dN/dx per frequency |
| `dNdx_all` | (44, 397) | float64 | dN/dx luminosity function per frequency |
| `dx_all` | (44, 397) | float64 | bin widths in x per frequency |
| `lnSinter` | (44, 500) | float64 | log(S) interpolation nodes for strain PDF |
| `pinter` | (44, 500) | float64 | strain PDF p(S) at interpolation nodes |

### Representative-frequency strain distributions (6 frequencies)

Indices: 0, 1, 5, 10, 20, 43. For each index `i`:

| array | shape | dtype | meaning |
|---|---|---|---|
| `S_freq{i}` | (16 777 216,) | float64 | strain-squared grid |
| `dNdS_freq{i}` | (16 777 216,) | float64 | differential source count dN/dS |
| `p_freq{i}` | (16 777 216,) | float64 | probability density p(S) |
| `dS_freq{i}` | () | float64 | bin width dS |

### Monte Carlo realizations (10 000 draws, seed = 42)

| array | shape | dtype | meaning |
|---|---|---|---|
| `total_strain` | (10000, 44) | float64 | total strain-squared per realization per frequency |
| `brightest_strain` | (10000, 44) | float64 | brightest-source strain-squared |
| `counts` | (10000, 44) | float64 | total source count per realization per frequency |
| `total_strain_wo_brightest` | (10000, 44) | float64 | total minus brightest source |
| `brightest_n_strains` | (10000, 44, 20) | float64 | top-20 source strains per realization per frequency |
| `total_lower_strain` | (10000, 44) | float64 | strain from sources below count threshold |

## Size on disk

2.3 GB (dominated by the 6 per-frequency arrays of shape (16 777 216,)).

## Consumers

- `notebooks/guide_population_and_spectra.py`
- `notebooks/guide_model_comparison.py`

## Related pages

- [[code/scripts_run_population]]
- [[concepts/SMBH_population_model]]
- [[concepts/brightest_source_fraction]]
- [[results/population_analysis_eps038]]
- [[results/population_analysis_eps066]]

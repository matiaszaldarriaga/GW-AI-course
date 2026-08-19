# `gwb_sources` — public API

**Source:** `gwb_sources/__init__.py`
**Type:** Python package entry point
**Ingested:** 2026-04-13

## Overview

`gwb_sources` is the core Python package for this project. Users import
from the top-level namespace; all public names are re-exported here from
submodules. A typical import looks like:

```python
from gwb_sources import sample_sources, compute_power_cls, luminosity_function
```

## Public exports

| Name | Source module | Concept |
|---|---|---|
| `luminosity_function` | `gwb_sources.population` | [[concepts/SMBH_population_model]] |
| `pdf_all_frequencies` | `gwb_sources.strain_stats` | [[concepts/SMBH_population_model]] |
| `sample_sources` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `expand_sources` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `gen_random_sources` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `run_realizations` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `compute_total_strain` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `find_brightest_source_strain` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `count_sources_brighter_than_strain` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `brightest_n_sources` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `generate_realizations` | `gwb_sources.sources` | [[concepts/brightest_source_fraction]] |
| `z_plus` | `gwb_sources.sky_maps` | [[concepts/transfer_function]] |
| `z_cross` | `gwb_sources.sky_maps` | [[concepts/transfer_function]] |
| `hd` | `gwb_sources.sky_maps` | [[concepts/transfer_function]] |
| `cl_one_source` | `gwb_sources.sky_maps` | [[concepts/Cl_over_C0]] |
| `two_point_correlation` | `gwb_sources.sky_maps` | [[concepts/Cl_over_C0]] |
| `zmap_one_source` | `gwb_sources.sky_maps` | [[concepts/transfer_function]] |
| `power_map` | `gwb_sources.sky_maps` | [[concepts/Cl_over_C0]] |
| `generate_map` | `gwb_sources.sky_maps` | [[concepts/Cl_over_C0]] |
| `filter_map` | `gwb_sources.sky_maps` | [[concepts/sqrt_SH_basis]] |
| `gen_realizations_bkg` | `gwb_sources.sky_maps` | [[concepts/shot_noise]] |
| `alm_summary_statistics` | `gwb_sources.summary_stats` | [[concepts/Cl_over_C0]] |
| `compute_summ_stat` | `gwb_sources.summary_stats` | [[concepts/Cl_over_C0]] |
| `compute_power_cls` | `gwb_sources.power_anisotropy` | [[concepts/Cl_over_C0]] |
| `compute_power_statistics` | `gwb_sources.power_anisotropy` | [[concepts/fisher_hierarchy]] |
| `save_power_results` | `gwb_sources.power_anisotropy` | — |
| `load_power_results` | `gwb_sources.power_anisotropy` | — |

## Design notes

All 27 public names are re-exports from five submodules; `__init__.py`
contains no logic of its own. The `sky_maps` module is noted as
"currently disabled" in `wiki/index.md` Phase 3 list, but its symbols
are present in the `__init__.py` and are exported here.

The split across submodules follows a clean separation of concerns:
`population` and `strain_stats` handle the astrophysical input
distribution; `sources` handles Monte Carlo realization of individual
binaries and the brightest-source statistics; `sky_maps` handles
angular maps and the HD correlation; `summary_stats` computes $a_{LM}$
moments; and `power_anisotropy` computes $C_\ell$ statistics and
persistence I/O.

## Related pages

Module pages (pending ingestion):
- [[code/gwb_sources_population]]
- [[code/gwb_sources_sources]]
- [[code/gwb_sources_power_anisotropy]]
- [[code/gwb_sources_sky_maps]]

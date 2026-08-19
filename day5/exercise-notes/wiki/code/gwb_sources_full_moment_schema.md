# `gwb_sources.full_moment_schema`

**Source:** `gwb_sources/full_moment_schema.py`
**Added:** 2026-08-11

## Purpose

Defines and validates the schema-v2 contract for corrected sampled population,
power-map, and direct-walk NPZ products. Publication consumers call
`load_full_moment_npz(path, product_kind=...)`; a pre-fix or wrong-kind file is
a hard error unless a baseline-comparison path explicitly opts into legacy
loading.

## Required physical arrays

- `total_power_Q`: $Q=\sum_s w_s$.
- `full_second_moment_S2`: $S_2=\sum_s w_s^2$, including
  $nE[w^2]=n(E[w]^2+\mathrm{Var}[w])$ for the unresolved population.
- `neff_full`: $Q^2/S_2$.
- `direct_dipole_vector` and `c1c0_direct=|\mathbf D|^2/Q^2$.
- `brightest_source_power/fraction` and completeness flags.
- Complete descending `source_ledger_*` arrays plus explicit power,
  second-moment, and count remainders.
- Exact-source and bulk count/power/moment fields, seed, threshold, frequency
  grid, producer, method, and schema metadata.

The validator also enforces non-negative moments, shapes, identity relations,
and documented completeness. Product-specific requirements add positive maps
and $C_\ell$ arrays for `power`, or selected common arrays for `walk`.

## Validation and consumers

`new_montecarlos_codex/validate_full_moment_products.py` performs the
end-to-end production gate for all three epsilon models, including bitwise
population/power equality, ledger/remainder conservation, direct low-moment
normalization, positive maps, and the derived walk identity. Paper consumers
share `paper_v2/scripts/_full_moment_data.py` so stale-file rejection is not
reimplemented ad hoc.

## Related pages

[[gwb_sources_power_anisotropy]], [[scripts_run_power]],
[[../concepts/N_eff]], [[../concepts/Cl_over_C0]],
[[../results/sampled_property_monte_carlo]], [[../reproducibility]].

# `gwb_sources.summary_stats`

**Source:** `gwb_sources/summary_stats.py`
**Type:** Python module
**Ingested:** 2026-04-13

## Purpose

Computes rotated-frame multipole summary statistics from the spherical harmonic
coefficients of the GW timing-residual field and its square. For each candidate
sky direction, the alm arrays are rotated to place that direction at the pole;
the four-element summary vector is then extracted from the rotated coefficients.
This rotation-first approach makes the statistics sensitive to the presence and
location of a dominant source without requiring a sky-position grid search at
the inference level.

The four summary statistics are:

1. `Re(a_{00}(z^2))` — isotropic power (monopole of z^2); proportional to total GWB power.
2. `Re(a_{10}(z^2))` — dipole amplitude of z^2 along the rotated pole axis.
3. `Re(a_{20}(z^2))` — quadrupole amplitude of z^2 along the rotated pole axis.
4. `|a_{22}(z_real)|^2 + |a_{22}(z_imag)|^2` (doubled) — |m|=2 quadrupole power of the coherent field z.

## Public API

### `alm_summary_statistics(alm_zr, alm_zi, alm_z2, lmax) -> ndarray`

Extracts the four-element summary vector from already-rotated alm arrays.
Raises `ValueError` if array lengths are inconsistent with `lmax`.

### `compute_summ_stat(nside_rot, alm_zr, alm_zi, alm_z2, Nrealizations, lmax) -> ndarray`

Outer loop over a HEALPix grid of resolution `nside_rot`. For each pixel
`(theta, phi)` constructs a `healpy.Rotator` that moves that direction to the
north pole, rotates all three alm arrays per realization, and calls
`alm_summary_statistics`. Returns an array of shape `(n_pix, Nrealizations, 4)`.

## Consumers

No consumers identified in the current codebase. Likely consumed by scripts in
`scripts/` that accumulate per-realization statistics for the detection figure
comparison. Check `results/*.npz` for arrays with shape `(n_pix, N, 4)`.

## Related pages

- [[concepts/coherent_vs_incoherent]] — z is the coherent timing-residual field; z^2 relates to incoherent power.
- [[concepts/brightest_source_fraction]] — dominant-source signature that the rotated dipole/quadrupole statistics are designed to detect.
- [[concepts/N_eff]] — effective source count; low N_eff means large dipole/quadrupole statistics.
- [[concepts/transfer_function]] — tau_L coefficients link the source-power map C_l^(P) to the pulsar-power map C_l^(b); summary stat #4 probes z directly, not z^2.
- [[concepts/matched_filter_vs_power]] — this module implements the power-map route; coherent matched filtering would use z alm directly.

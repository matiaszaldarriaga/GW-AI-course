# `gwb_sources.sky_maps`

**Source:** `gwb_sources/sky_maps.py`
**Type:** Python module (partially disabled — see below)
**Ingested:** 2026-04-13

## Status

Mixed. Three functions (`zmap_sources`, `gen_realizations_sources`,
`gen_realizations_mixed`) are **disabled** via `NotImplementedError`.
All remaining functions are active.

## Purpose

Provides antenna-pattern functions, HEALPix sky-map construction, angular
power spectra, and Monte Carlo realization generators for GWB sky maps.
The module handles both the coherent timing-residual map $z(\hat p)$ and
the incoherent source-power map $P(\hat\Omega)$.

## Public API (active)

| Function | Purpose |
|---|---|
| `z_plus(theta_p, phi_p, theta_k, phi_k)` | Antenna response for + polarization |
| `z_cross(...)` | Antenna response for x polarization |
| `hd(mu)` | Hellings-Downs correlation curve $\chi(\mu)$ |
| `cl_one_source(l)` | Analytic $C_\ell$ for a single source; $C_\ell = 2\pi / [(\ell+2)(\ell+1)\ell(\ell-1)]$ for $\ell \ge 2$ |
| `two_point_correlation(thetas, cls)` | Angular correlation function from $C_\ell$ via Legendre sum |
| `zmap_one_source(hp_real, hp_imag, hc_real, hc_imag, theta_s, phi_s, nside)` | HEALPix timing-residual map for a single source |
| `power_map(sources, nside)` | HEALPix source-power map $P(\hat\Omega)$ from a discrete source catalogue |
| `generate_map(nside, cl_function, rng)` | Gaussian random map synthesized from an analytic $C_\ell$ via `hp.synfast` |
| `filter_map(sky_map, l_cut)` | Low-pass harmonic filter at $\ell_{\max} =$ `l_cut` |
| `gen_realizations_bkg(Nrealizations, nside, lmax, cl_function, rng)` | Monte Carlo realizations of an isotropic Gaussian background; returns maps, $C_\ell$ arrays, and $a_{\ell m}$ arrays |

The private helper `_normalize_and_analyze` normalizes maps by their
mean-square amplitude $\sigma_0^2 = \langle z^2 \rangle$ and calls
`hp.anafast` / `hp.map2alm` on both polarizations and on the power map
$z^2(\hat p)$.

## Disabled functions

| Function | Signature |
|---|---|
| `zmap_sources` | `(hp_real, hp_imag, hc_real, hc_imag, theta_s, phi_s, nside)` |
| `gen_realizations_sources` | `(Nrealizations, Nsources, nside, lmax, rng)` |
| `gen_realizations_mixed` | `(Nrealizations, Nsources, fPsources, nside, lmax, cl_function, rng)` |

All three raise `NotImplementedError` with the message: "cannot scale to
the astrophysical source population (billions of sources). A binned
approach is needed." The docstrings point to `generate_realizations` in
`gwb_sources/sources.py` as the replacement.

**Verified status:** all three remain disabled in the current source as
of 2026-04-13. No active code path calls them.

The project memory note records that these were disabled because they
produced negative pixels and $C_\ell/C_0 \gg 1$ due to an RNG bug. The
fix (binned / power-map approach) lives in `gwb_sources/sources.py`.

## Related pages

- `wiki/code/gwb_sources_sources.md` — replacement `generate_realizations`
- `[[concepts/Cl_over_C0]]` — the ratio this module computes
- `[[concepts/coherent_vs_incoherent]]` — $z$ map vs $P$ map distinction
- `[[concepts/transfer_function]]` — $\tau_L$ relating $C_\ell^{(z)}$ to $C_\ell^{(P)}$
- `[[concepts/shot_noise]]` — motivation for power-map approach over summing individual-source maps

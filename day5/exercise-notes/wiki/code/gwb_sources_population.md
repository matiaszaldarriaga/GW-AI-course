# `gwb_sources.population`

**Source:** `gwb_sources/population.py`
**Type:** Python module
**Ingested:** 2026-04-13

## Purpose

Implements the velocity-dispersion-based SMBH population model following
Sato-Polito, Zaldarriaga & Quataert (arxiv 2312.06756). Starting from the
galaxy velocity dispersion function (VDF), it applies the $M$–$\sigma$
relation with log-normal mass scatter $\varepsilon$ (in dex) to produce the
SMBH mass function, then integrates over mass, mass ratio, and redshift bins
to yield per-bin source counts $N_{\rm bin}(f, M)$, characteristic-strain
squared $h_c^2(f, M)$, and single-source strain squared $h_s^2(f, M)$.
It also builds the dimensionless luminosity function $dN/dx$ as a function
of the normalized single-source strain $x = h_s^2 / h_{s,\rm max}^2$ for
each frequency bin. See [[concepts/SMBH_population_model]].

## Public API

| Function | Signature | Returns | Concept |
|---|---|---|---|
| `vdisp_func` | `(sig, phi_sigma, sigma_ref, a_sigma, b_sigma)` | `dn/d\sigma` at velocity dispersion `sig` | VDF fit (modified Schechter) |
| `M_sigma` | `(sig, a_ms, b_ms)` | BH mass in $M_\odot$ | $M$–$\sigma$ power law |
| `MFSMBH_vdisp` | `(m, eps_ms, phi_sigma, sigma_ref, a_sigma, b_sigma, a_ms, b_ms)` | $dn/d\log_{10}M$ at mass `m` | BHMF via scatter convolution |
| `luminosity_function` | `(params)` | `dict` with `h2s`, `h2c`, `N_bin`, `dNdx`, `Nc`, `htot0`, `Mmax`, `fone`, ... | Full population grid; [[concepts/brightest_source_fraction]], [[concepts/N_eff]] |
| `gaussian` | `(x, sigma)` | Normalized Gaussian value | Scatter kernel (internal helper) |
| `interpolated_maximum` | `(x, f)` | Quadratic-interpolated peak location | Peak-finding helper (internal) |

## Key formulas implemented

**VDF (modified Schechter):**
$$\frac{dn}{d\sigma} = \frac{\phi_\sigma}{\Gamma(\alpha/\beta)}
  \frac{\beta}{\sigma}
  \left(\frac{\sigma}{\sigma_{\rm ref}}\right)^\alpha
  \exp\!\left[-\left(\frac{\sigma}{\sigma_{\rm ref}}\right)^\beta\right],$$
with fiducial values $\phi_\sigma = 2.611\times10^{-2}$, $\sigma_{\rm ref}=159.57\,\rm km\,s^{-1}$,
$\alpha=0.41$, $\beta=2.59$.

**$M$–$\sigma$ relation:**
$$\log_{10}(M/M_\odot) = a_{\rm ms} + b_{\rm ms}\log_{10}(\sigma/200\,\rm km\,s^{-1}),$$
with $a_{\rm ms}=8.32$, $b_{\rm ms}=5.64$.

**BHMF via scatter convolution** (`MFSMBH_vdisp`): integrates
$dn/d\log_{10}M_{\rm BH}$ as the convolution of the VDF-implied mean
$M$–$\sigma$ mapping with a Gaussian of width $\varepsilon$ (in dex),
sampling $\sigma$ on 300 log-spaced points over $[10^{0.5}, 10^5]\,\rm km\,s^{-1}$.

**Characteristic strain** (per bin, in `luminosity_function`):
$$h_c^2(f, M) = \frac{32\pi^{4/3}}{5c^8}(GM)^{10/3}f^{4/3}
  \sum_{ij}\Delta N_{ij}\frac{(1+z_i)^{4/3}}{d_{L,i}^2}\left(\frac{q_j}{(1+q_j)^2}\right)^2,$$
with the redshift factor $\propto (1+z)^{-8/3}z^B e^{-z/Z_s}$ and mass-ratio
weight $\propto \eta^{-1}q^C$.

**Single-source strain** (per bin):
$$h_s^2(f, M) = h_c^2(f, M)\frac{f/f_{\rm min}}{N_{\rm bin}(f, M)}.$$

**Normalized luminosity function** (post-loop, for each frequency):
$$x = h_s^2(f,M)/h_{s,\rm max}^2(f), \qquad dN/dx = N_{\rm bin}/\Delta x.$$
The characteristic source count $N_c(f) = (f/f_{\rm one})^{-11/3}$ gives the
effective number of sources contributing at that frequency.

See also [[concepts/SMBH_population_model]] for the scatter boost formulae
and the three $\varepsilon$ scenarios ($0.20$, $0.38$, $0.66$).

## Known gotchas

- **`m` must carry astropy units** in `MFSMBH_vdisp`: the function calls
  `m.value` and passes `Mmean[k]` (which is an astropy `Quantity`) into the
  convolution integral. Passing a bare float will raise `AttributeError`.
- **`phi_sigma` sign-off**: the default `phi_sigma=2.611e-2` is used in both
  `vdisp_func` and `MFSMBH_vdisp`. Earlier code had a mismatch; this was
  unified in commit `434c54d`. Always pass `phi_sigma` consistently; do not
  rely on defaults from both call sites independently.
- **`sigma_ref` naming collision**: in `luminosity_function`, the `params`
  key is `'sigma'` (not `'sigma_ref'`) and is passed as the positional
  `sigma_ref` argument to `vdisp_func`. This differs from the kwarg name
  in the function signature — a latent confusion when reading the param dict.
- **`f/fmin` ratio loses units**: `h2s[j, k]` is computed as
  `h2c[j, k] * (fmean[j] / fmin).value / N_bin[j, k]`. The `.value`
  strips units; downstream consumers receive a dimensionless ratio. Verify
  `fmin` is passed in consistent frequency units.
- **`kmax` uses bin-center argmax**: `Mmax` and `fone` are grid-point values,
  while `Mmax_inter` and `fone_inter` use quadratic interpolation.
  Prefer the `_inter` variants for any quantitative claim about peak mass.
- **Integration convention**: the BHMF convolution uses `np.trapz` over
  `mconv = log10(M_sigma(sigma))`, which is the log-mass of the *mean*
  $M$–$\sigma$ mapping — not the scattered mass. The Gaussian kernel is
  applied in log-mass space, which is correct for log-normal scatter.

## Consumers

**Notebooks:**
- `notebooks/guide_population_and_spectra.py` — primary visualization of VDF, BHMF, $h_c^2$.
- `notebooks/guide_model_comparison.py` — $\varepsilon$ scan (median vs mean strain).
- `notebooks/guide_interactive.py` — interactive parameter sweep.
- `notebooks/guide_dipole_analytics.py` — population inputs to dipole analytics.

**Scripts:**
- `scripts/run_population_analysis.py` — batch population runs producing `results/*.npz`.
- `scripts/run_power_anisotropy.py` — feeds `luminosity_function` output to power anisotropy pipeline.

**Tests:**
- `tests/test_population.py`, `tests/test_strain_stats.py`,
  `tests/test_generate_realizations.py`, `tests/test_sources.py`,
  `tests/test_power_anisotropy.py`.

## Related pages

- [[concepts/SMBH_population_model]] — framework, three $\varepsilon$ scenarios, scatter boost.
- [[concepts/brightest_source_fraction]] — $p_1 = q_{\max}/\sum_a q_a$; set by the tail of $dN/dx$.
- [[concepts/N_eff]] — $1/\sum_a p_a^2$; determined by the shape of $dN/dx$.
- [[concepts/shot_noise]] — finite-$N$ variance; controlled by $N_c(f)$.
- `wiki/code/gwb_sources_sources.md` (not yet ingested) — Poisson sampling from `luminosity_function` output.

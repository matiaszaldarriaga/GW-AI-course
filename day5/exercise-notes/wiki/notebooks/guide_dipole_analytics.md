# Notebook: `guide_dipole_analytics`

**Source:** `notebooks/guide_dipole_analytics.py`
**HTML export:** `results/guide_dipole_analytics.html`
**Paper citations:** `astrophysical_model.tex:65`, `distribution_c1c0.tex:96`

---

## Purpose

Validates the 3D random-walk identity $C_1/C_0 = |\mathbf{S}|^2$ and
benchmarks all four semi-analytic approximations for the distribution of
$C_1/C_0$ against a direct Monte Carlo. No HEALPix maps or `anafast`
calls are used; the comparison with the HEALPix pipeline is loaded from
`results/power_anisotropy_eps066.npz` when available.

---

## Key findings

- **3D random-walk identity is exact.** The conditional mean
  $\mathbb{E}[C_1/C_0\mid\{p_a\}] = \sum_a p_a^2 = 1/N_{\rm eff}$ is
  verified by scatter plot (bottom-left panel); the 1:1 line holds
  across realizations.

- **Speed gain: ~100x.** 10 000 realizations at 3 frequencies complete
  in ~29 s via the 3D walk, versus ~50 min for the HEALPix pipeline.
  The bulk-bin CLT approximation (threshold $N_{\rm bin} > 1000$)
  accounts for faint sources; bright bins are sampled individually.

- **Approximation quality (rough to fine):**
  1. $\delta(u - p_1^2)$: samples only $p_1$; captures the peak
     position but misses all spread.
  2. Uniform on $[(p_1-p_2)^2,(p_1+p_2)^2]$: adds spread from the
     two-source mutual angle; correct support, no background.
  3. 1-source + Gaussian background (noncentral Maxwell, $p_1,\eta$):
     nearly exact for astrophysical populations. This is the
     approximation used in `distribution_c1c0.tex`, eq. `eq:1src_gauss`.
  4. 2-source + Gaussian background ($p_1,p_2,\eta_2$): marginal
     improvement over approx 3 at the cost of one extra parameter.
     Paper eq. `eq:2src_gauss`.

- **Key insight stated in summary cell:** $C_1/C_0$ is large only when
  one source dominates; $p_1$ alone captures most of the distribution.

---

## Figures produced

| Panel | Content |
|---|---|
| Top-left | PDF of $C_1/C_0$: 3D walk vs HEALPix (step histograms, log $y$) |
| Top-right | QQ plot: 3D-walk quantiles vs HEALPix quantiles |
| Bottom-left | Scatter: $C_1/C_0$ vs $\sum p_a^2$; 1:1 line = conditional mean |
| Bottom-right | Statistics table: mean, median, 5th/95th pct, std, wall time |
| Section 4 left | All four approximation PDFs, linear scale |
| Section 4 right | Same, log scale |

The statistics comparison table (Section 4b) is rendered as a Markdown
table inside the notebook via `mo.md`.

---

## Results files consumed

| File | Usage |
|---|---|
| `results/power_anisotropy_eps066.npz` | Optional HEALPix baseline; loaded if present |

No `.npz` files are written by this notebook.

---

## Inputs (interactive sliders)

| Slider | Range | Default |
|---|---|---|
| `eps` (M-sigma scatter $\varepsilon$) | 0.20 – 0.66 | 0.66 |
| Frequency bin index | 0 – 43 | 0 |
| N realizations | 1000 – 50 000 | 10 000 |

Population parameters are hardcoded at `phi_sigma=2.611e-2`,
`sigma=160`, `a_sigma=0.41`, `b_sigma=2.59`, `a_ms=8.32`,
`b_ms=5.64`, `B=0.5`, `Zs=0.33`, `C=-1`, matching the rest of
the project (see `conventions.md` and `[[concepts/SMBH_population_model]]`).

---

## Concepts exercised

- [[concepts/dipole_distribution]] — all four approximations implemented
- [[concepts/Cl_over_C0]] — 3D random-walk identity and exact mean/variance
- [[concepts/N_eff]] — conditional mean equals $1/N_{\rm eff}$
- [[concepts/brightest_source_fraction]] — $p_1$, $p_2$, $\eta$, $\eta_2$ extracted per realization
- [[concepts/SMBH_population_model]] — `luminosity_function` called with full param dict

---

## JSON report

```json
{
  "slug": "guide_dipole_analytics",
  "concepts": [
    "dipole_distribution",
    "Cl_over_C0",
    "N_eff",
    "brightest_source_fraction",
    "SMBH_population_model"
  ],
  "inputs": [
    "results/power_anisotropy_eps066.npz"
  ],
  "outputs": [],
  "paper_refs": [
    "astrophysical_model.tex:65",
    "distribution_c1c0.tex:96"
  ]
}
```

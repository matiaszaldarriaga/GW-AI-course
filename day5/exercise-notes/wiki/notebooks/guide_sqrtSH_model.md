# Notebook: guide_sqrtSH_model

**File:** `notebooks/guide_sqrtSH_model.py`
**HTML export:** `results/guide_sqrtSH_model.html`
**Purpose:** Validate that NANOGrav's published "upper limits" on $C_\ell/C_0$ are the
sqrt-SH prior, not data-driven constraints. Quantify how strongly the prior shape
depends on $\ell_{\max}^b$.

---

## Key findings

1. **The constraint is the prior.** Sampling $10^4$ realizations from the NANOGrav
   $b_{LM}$ prior ($\ell_{\max}^b = 3$, wide uniform priors on the coefficients) and
   computing $C_\ell/C_0$ by squaring reproduces the NANOGrav Figure 1 upper-limit
   shape. Specifically, the 95th percentile of $C_1/C_0 \approx 0.20$, matching the
   paper's published value.

2. **The ratio $C_\ell/C_0$ is scale-invariant.** Changing the amplitude range of the
   $b_{LM}$ coefficients does not change $C_\ell/C_0$ because the amplitude cancels in
   the ratio. The prior shape is determined entirely by $\ell_{\max}^b$.

3. **Strong non-convergence with $\ell_{\max}^b$.** The 95th percentile of $C_1/C_0$
   drops by approximately two orders of magnitude from $\ell_{\max}^b = 3$ to
   $\ell_{\max}^b = 95$. Higher modes pump power into $C_0$ through the squaring
   convolution, shrinking $C_\ell/C_0$ at all low $\ell$. The "constraint" is therefore
   an artifact of the truncation choice, not a statement about the sky.

4. **Astrophysical models lie well within the prior.** The $C_\ell/C_0$ distributions
   from the three population models ($\varepsilon = 0.20, 0.38, 0.66$) at each
   frequency all fall inside the sqrt-SH prior band. Even for the most anisotropic
   model ($\varepsilon = 0.66$) the probability that $C_1/C_0 > 0.20$ is only
   $\sim 10\%$ at the lowest PTA frequency.

---

## Sections and figures

| Section | Content |
|---|---|
| 1 | Introduction: sqrt-SH construction, NANOGrav priors, role of $\ell_{\max}^b$ |
| 2 | Example power maps (Mollweide, $\log_{10}$ scale); interactive realization slider |
| 3 | Mean and median $C_\ell/C_0$ vs $\ell$; 50% and 95% bands |
| 3b | Convergence: distributions of $C_\ell/C_0$ for $\ell_{\max}^b = 3, 6, 23, 47, 95$; summary table |
| 4 | PDF of $C_\ell/C_0$ at selected $\ell$ (linear and log y-axis) |
| 5 | Distribution of $C_0$ (monopole); explains why it varies with $\ell_{\max}^b$ |
| 6 | Comparison with astrophysical models at selectable frequency bin |
| 7 | Verification against NANOGrav Figure 1; table of 95th-percentile values vs digitized paper |

All interactive panels use `mo.ui.slider` or `mo.ui.dropdown`; they produce no static
output files.

---

## Results files consumed

| File | Role |
|---|---|
| `results/sqrtSH_realizations_nside8.npz` | Primary dataset; $\ell_{\max}^b = 23$, $N_{\rm rel}$ realizations |
| `results/sqrtSH_realizations_nside16.npz` | Convergence comparison; $\ell_{\max}^b = 47$ |
| `results/sqrtSH_realizations_nside32.npz` | Convergence comparison; $\ell_{\max}^b = 95$ |
| `results/sqrtSH_realizations_lmax6.npz` | Convergence comparison; $\ell_{\max}^b = 6$ |
| `results/sqrtSH_realizations_lmax3.npz` | NANOGrav's actual choice; $\ell_{\max}^b = 3$ |
| `results/power_anisotropy_eps020.npz` | Astrophysical model $\varepsilon=0.20$ |
| `results/power_anisotropy_eps038.npz` | Astrophysical model $\varepsilon=0.38$ |
| `results/power_anisotropy_eps066.npz` | Astrophysical model $\varepsilon=0.66$ |

No output `.npz` is written; the notebook is read-only with respect to results.

---

## Concepts exercised

- [[concepts/sqrt_SH_basis]] — the central object; truncation rule $\ell_{\max}^b = \ell_{\max}^a/2$
- [[concepts/Cl_over_C0]] — the normalized spectrum computed and compared
- [[concepts/prior_sensitivity]] — non-convergence of $C_\ell/C_0$ with $\ell_{\max}^b$ quantified
- [[concepts/SMBH_population_model]] — astrophysical $\varepsilon$ models overlaid in Sec. 6

---

## Paper references

- `nanograv_prior.tex:22` — `\fromnotebook` citing Sec. 3b and `references/2103.00826`
- `nanograv_prior.tex:60` — `\fromnotebook` citing Sec. 7 (NANOGrav Fig. 1 reproduction)
- `nanograv_prior.tex:79` — `\fromnotebook` citing Secs. 3–3b (convergence claim)

---

## External sources cited within notebook

- Banagiri et al. 2021 (arxiv 2103.00826) — CG truncation rule; $\ell_{\max}^b = \ell_{\max}^a/2$ derivation
- NANOGrav 15yr anisotropy (arxiv 2306.16221) — priors and Figure 1 being reproduced
- `docs/ylm_conventions.md` — three-method consistency check (healpy, complex Gaunt, real Gaunt)

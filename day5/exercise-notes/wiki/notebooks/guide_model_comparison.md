# Notebook: guide_model_comparison

**Source:** `notebooks/guide_model_comparison.py`
**HTML export:** `results/guide_model_comparison.html`
**Marimo version:** 0.21.1

## Purpose

Interactive comparison of three M-sigma scatter models ($\varepsilon = 0.20, 0.38, 0.66$).
Quantifies how the scatter parameter controls strain amplitude, mean-vs-median divergence,
brightest-source dominance, angular power spectrum ratios, and effective source count across
44 frequency bins.

## Inputs

| File | Shape | Description |
|---|---|---|
| `results/population_analysis_eps020.npz` | `total_strain` (10000, 44) | Poisson realizations, low scatter |
| `results/population_analysis_eps038.npz` | `total_strain` (10000, 44) | Poisson realizations, fiducial |
| `results/population_analysis_eps066.npz` | `total_strain` (10000, 44) | Poisson realizations, high scatter |
| `results/power_anisotropy_eps020.npz` | `cls_all` (10000, 44, 24) | Power-map $C_\ell$, low scatter |
| `results/power_anisotropy_eps038.npz` | `cls_all` (10000, 44, 24) | Power-map $C_\ell$, fiducial |
| `results/power_anisotropy_eps066.npz` | `cls_all` (10000, 44, 24) | Power-map $C_\ell$, high scatter |

Frequency axis: 44 bins, $f \in [0.085, 2.776]$ yr$^{-1}$.
Each model: 10,000 Poisson realizations; top-20 brightest sources tracked per realization.
Power maps: nside=8, $\ell_{\max}=23$.

## Outputs

No `.npz` files written. Purely interactive visualization.

## Figures produced

1. **Strain spectrum** — analytic mean (solid), realization mean (dotted), realization median (dashed) for all three models. Optional exclusion of top-$N$ sources via dropdown.
2. **Brightest source fraction** — median $p_1 = h^2_{\rm brightest}/h^2_{\rm total}$ with 95% band vs frequency.
3. **Monopole $C_0$** — mean and median with 95% band vs frequency, per model.
4. **Dipole ratio $C_1/C_0$** — mean and median with 95% band vs frequency.
5. **$N_{\rm eff}$ vs frequency** — $C_0/C_1$ proxy, mean and median with 95% band.
6. **$C_\ell/C_0$ error bars** — three-panel: $\ell=1$–23 at representative frequencies (bins 0, 20, 43).

## Key findings

### Mean vs median strain (the headline observable)

Computed from `total_strain[:, 0]` vs `h2c_vs_f[0]` at lowest frequency bin ($f \approx 0.085$ yr$^{-1}$):

| $\varepsilon$ | median / analytic mean | median / realization mean |
|---:|---:|---:|
| 0.20 | 0.988 | 0.987 |
| 0.38 | 0.930 | 0.924 |
| 0.66 | **0.571** | **0.568** |

The 57% figure cited in `astrophysical_model.tex:70` and in [[concepts/SMBH_population_model]] is
confirmed as median/analytic-mean $= 0.5709$ at $\varepsilon=0.66$, $f_0 \approx 0.085$ yr$^{-1}$.
Physical origin: the high-mass tail produces rare ultra-bright realizations that pull the ensemble mean
far above the typical draw; the analytic mean integrates over the full luminosity function including the tail.

### Brightest source fraction at $f_0$

| $\varepsilon$ | median $p_1$ | 95th-percentile $p_1$ |
|---:|---:|---:|
| 0.20 | 0.020 | 0.085 |
| 0.38 | 0.052 | 0.260 |
| 0.66 | 0.155 | 0.654 |

At $\varepsilon=0.66$ the median brightest source carries 15% of the total strain, and in 5% of
realizations it carries more than 65%.

### Effective source count ($N_{\rm eff} = C_0/C_1$) at $f_0$

| $\varepsilon$ | median $N_{\rm eff}$ |
|---:|---:|
| 0.20 | 966 |
| 0.38 | 191 |
| 0.66 | 27 |

The high-scatter model is deeply in the Poisson / bright-source-dominated regime at all PTA frequencies.

### Source-exclusion sensitivity

Removing the top 5–20 sources dramatically reduces both amplitude and $C_1/C_0$ for $\varepsilon=0.66$
but has negligible effect for $\varepsilon=0.20$. This asymmetry is the empirical signature of the
brightest-source-fraction hierarchy.

## Concepts exercised

[[concepts/SMBH_population_model]], [[concepts/brightest_source_fraction]],
[[concepts/N_eff]], [[concepts/Cl_over_C0]], [[concepts/dipole_distribution]],
[[concepts/shot_noise]]

## Paper references

- `astrophysical_model.tex:70` — cites the 57% median/mean ratio for $\varepsilon=0.66$.
- `discussion.tex` — mean-vs-median as the most informative near-term observable.
- Source model from [[sources/arxiv_2406_17010]] (Sato-Polito & Zaldarriaga 2025) and
  [[sources/arxiv_2312_06756]] (Sato-Polito, Zaldarriaga & Quataert 2023).

---

```json
{
  "slug": "guide_model_comparison",
  "concepts": [
    "SMBH_population_model",
    "brightest_source_fraction",
    "N_eff",
    "Cl_over_C0",
    "dipole_distribution",
    "shot_noise"
  ],
  "key_numbers": [
    "eps=0.66: median/analytic-mean h2c = 0.571 at f0=0.085/yr",
    "eps=0.20: median/analytic-mean h2c = 0.988 at f0",
    "eps=0.66: median p1 = 0.155 at f0; 95th pctile = 0.654",
    "eps=0.66: median Neff = 27 at f0",
    "eps=0.20: median Neff = 966 at f0",
    "10000 Poisson realizations per model; 44 frequency bins"
  ],
  "inputs": [
    "results/population_analysis_eps020.npz",
    "results/population_analysis_eps038.npz",
    "results/population_analysis_eps066.npz",
    "results/power_anisotropy_eps020.npz",
    "results/power_anisotropy_eps038.npz",
    "results/power_anisotropy_eps066.npz"
  ],
  "outputs": [],
  "paper_refs": [
    "astrophysical_model.tex:70",
    "discussion.tex"
  ]
}
```

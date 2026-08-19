# Log

Append-only chronological record of ingests, queries, lints, and
significant edits. Entries use the prefix format
`## [YYYY-MM-DD] <op> | <one-line description>` so `grep "^## \["` is
a timeline.

---

## [2026-04-13] init | wiki initialized

Phase 1 of the wiki pattern.

Created:
- `CLAUDE.md` at project root (schema + workflows).
- `wiki/` skeleton: `index.md`, `conventions.md`, `bibliography.md`,
  `log.md`, plus empty subdirs `concepts/`, `sources/`, `paper/`,
  `code/`, `notebooks/`, `results/`, `figures/`, `decks/`.

Seeded `bibliography.md` from today's verified bib audit (see below).

Seeded `conventions.md` with non-negotiables extracted from the md
notes and from today's hierarchy-bug debugging:
- Three distinct $C_\ell$ objects ($P$, $b$, $z$) with exact transfer.
- $\Sigma_{\rm bg}^2 = (A^2 N_p/2\sigma_n^4)(1+(N_p-1)/48)$ in noise-dominated benchmark.
- Block weights $s_L$ with tabulated values for $N_p=67$.
- KL vs Fisher distinction (the bug).
- Sqrt-SH truncation $\ell_{\max}^b = \ell_{\max}^a/2$.
- No eyeballing. No silent bib edits.

## [2026-04-13] fix | hierarchy equation in paper corrected

`paper/sections/three_strategies.tex`: replaced
$D_{C_\ell} \propto p^2/(2\ell+1)$ with $D_{C_\ell} \propto p^4$.
The $1/(2L+1)$ is a per-L penalty inside the sum, not a global factor.
Derivation added in-line: noncentral-$\chi^2$ Fisher at $\lambda=0$ is
$1/[2(2L+1)]$, combined with $(d\lambda/dp)^2 \propto p^2$ gives
$F_{pp}^{(C_L)}\propto p^2$, and $D\sim(1/2)p^2 F_{pp}^{(C_L)}\propto p^4$.

Matching edits in `introduction.tex` (point 3 of the claims list) and
`main.tex` (abstract). Cross-ref `eq:F_cl_weak` → `eq:F_cl_final` fixed
in `numerical_estimates.tex`.

Appendix numerical-agreement wording softened: $|r|=0.037$ vs
$1/\sqrt{67}\approx 0.12$ is order-of-magnitude, not "consistent."

Source: `references/pta_point_source_vs_CL_note.md`, Secs. 3-5.

## [2026-04-13] audit | references.bib verified against ADS

Fetched arxiv + NASA ADS for every cited key. Corrections:
- `LinLoeb:2026` renamed `LinLidzMa:2026` (2602.16808 is Lin, Lidz, Ma; not Loeb).
- `Sato-Polito:2023gym` pointed at wrong arxiv (2305.09725 = viscous-fluids); real paper is 2312.06756 (Sato-Polito/Zaldarriaga/Quataert) → key renamed `SatoPolito:2023big`.
- `Sato-Polito:2023spo` was a made-up placeholder; replaced with `SatoPolito:2024Kam` (real Sato-Polito/Kamionkowski paper 2305.05690).
- Two Banagiri entries collapsed to one `Banagiri:2021lisa` (2103.00826); the discarded key pointed at 2006.04810 which is actually Taylor/vanHaasteren/Sesana.
- `Liepold:2024woa` → `Liepold:2024big` with arxiv 2407.14595 added.
- `Lamb:2024gbh` → `LambTaylor:2024` with arxiv 2407.06270 added.
- `SatoPolito:2024dist` → `SatoPolito:2025dist` (PRD 111 023043 published January 2025).
- DOIs and eprint IDs added throughout.

Downloaded arxiv tex sources into `references/<id>/` for every cited
paper that wasn't already present (5 new directories).

## [2026-04-13] fix | compilation/layout issues

- `equation` → `multline` for `eq:2src_gauss` in `distribution_c1c0.tex` and the new $F_{pp}^{(C_L)}$ equation in `three_strategies.tex` (both were wider than a column).
- `\fromnotebook` macro in `main.tex` redefined with `\scriptsize \raggedright \sloppy \emergencystretch` and a redefinition of `\_` to a breakable token, so long snake_case filenames wrap inside narrow columns.
- Same treatment applied to `\todo` macro.
- `LinLidzMa:2026` and `SatoPolito:2023big` changed from `@article` to `@misc` (no published journal).
- Final compile: 10 pages, 0 overfull hboxes, 0 undefined citations.

## [2026-04-13] ingest-batch | 11 pedagogical md notes → wiki

Phase A: 11 subagents dispatched in parallel (one per note in
`references/*.md`). Each produced its `wiki/sources/<slug>.md` page and
returned a machine-readable report. All 11 completed without conflicts
or asks for clarification.

Phase B: consolidated reports into shared files.

**Source pages created (11):**

- [[sources/pn_C1_over_C0]] — 4 paper citations
- [[sources/pn_coh_vs_incoh_fisher]] — 3 paper citations
- [[sources/pta_1src_vs_CL]] — 2 paper citations
- [[sources/fisher_src_vs_bg_degeneracy]] — 2 paper citations
- [[sources/pn_coh_vs_quadratic]] — no citations yet
- [[sources/pn_1src_vs_dipole_cov]] — no citations yet
- [[sources/pta_exact_pair_average]] — no citations yet
- [[sources/pta_noise_dominated_limit]] — no citations yet
- [[sources/pta_1src_vs_cls_toy]] — no citations yet
- [[sources/matched_filter_vs_power]] — no citations yet
- [[sources/pta_prior_sensitivity]] — no citations yet

**Concept pages created (15):**

Central observables: [[concepts/Cl_over_C0]], [[concepts/N_eff]],
[[concepts/brightest_source_fraction]], [[concepts/dipole_distribution]],
[[concepts/shot_noise]].

Detection theory: [[concepts/fisher_hierarchy]],
[[concepts/KL_divergence]], [[concepts/coherent_vs_incoherent]],
[[concepts/source_background_degeneracy]],
[[concepts/matched_filter_vs_power]].

PTA formalism: [[concepts/s_L_block_weights]],
[[concepts/transfer_function]], [[concepts/sqrt_SH_basis]],
[[concepts/prior_sensitivity]].

Astro context: [[concepts/SMBH_population_model]] (stub — no md note
covers it; references arxiv sources).

**Formulas.md:** expanded from 12 paper equations to 31 entries with
canonical concept-page owners.

**Index.md:** rewritten with full sections for 15 concepts, 11 sources
organized into "currently cited" and "candidates for paper use".

**No new concepts proposed** by any subagent — the vocabulary in
`CLAUDE.md` covered all 11 notes completely.

**Citations audit (potential, not yet applied):**

Sources that could strengthen paper sections but are currently uncited:
- `pta_exact_pair_average` (canonical $s_L$ values) → `numerical_estimates.tex`
- `pn_1src_vs_dipole_cov` ($\tau_L$ transfer, dipole equivalence) → `nanograv_prior.tex` or `discussion.tex`
- `pn_coh_vs_quadratic` (self-contained coherent-vs-cov derivation, $C_1^{(b)}/C_0^{(b)}=p^2/4$) → `three_strategies.tex` or introduction
- `matched_filter_vs_power` (Rice upcrossing, look-elsewhere) → introduction (linear-vs-quadratic pedagogy)

The `matched_filter_vs_power` note references Rice 1944, Adler 1981,
Gross-Vitells 2010, Owen 1996 — none in bib. Would need
`verify-reference` runs if cited.

**Follow-ups added to [[todo]]:**
- Evaluate whether to add references from `matched_filter_vs_power`.
- Consider upgrading `SMBH_population_model` concept by ingesting
  `references/2312.06756/` (tex is already downloaded).

## [2026-04-13] ingest-notebook | guide_dipole_analytics

Created `wiki/notebooks/guide_dipole_analytics.md`. Covers: 3D
random-walk validation of $C_1/C_0 = |\mathbf{S}|^2$; all four
semi-analytic approximations (delta, uniform 2-src, 1-src+Gauss,
2-src+Gauss); interactive sliders for $\varepsilon$, frequency bin,
and $N_{\rm real}$; statistics-comparison table; optional QQ plot
against HEALPix baseline. Paper refs: `astrophysical_model.tex:65`,
`distribution_c1c0.tex:96`. Updated `index.md` Notebooks section.

## [2026-04-13] ingest-batch | 9 arxiv papers → wiki

Phase A: 9 subagents dispatched in parallel (one per arxiv tex tree in
`references/<id>/`). Each produced its `wiki/sources/arxiv_<id>.md` page
and returned a machine-readable report. All 9 completed successfully.

Phase B: consolidated into shared files.

**Source pages created (9):**

- [[sources/arxiv_2103_00826]] — Banagiri et al. 2021 (sqrt-SH basis foundation)
- [[sources/arxiv_2305_05690]] — Sato-Polito & Kamionkowski 2024 (spectrum anisotropies)
- [[sources/arxiv_2306_16221]] — NANOGrav 15yr anisotropy (target of critique #1)
- [[sources/arxiv_2312_06756]] — Sato-Polito, Zaldarriaga, Quataert 2023 (population model)
- [[sources/arxiv_2406_17010]] — Sato-Polito & Zaldarriaga 2025 (direct precursor of this project)
- [[sources/arxiv_2407_06270]] — Lamb & Taylor 2024 (spectral variance)
- [[sources/arxiv_2407_14595]] — Liepold & Ma 2024 (alternate GSMF)
- [[sources/arxiv_2602_16808]] — Lin, Lidz, Ma 2026 (target of critique #2)
- [[sources/arxiv_2006_04810]] — Taylor, van Haasteren, Sesana 2020 (not yet cited; recommended for bib)

**Bibliography verification:** all 8 currently-cited bib entries verified
against arxiv abstracts by the ingesting subagent. Zero discrepancies —
the corrections applied in the morning (Lin/Loeb → Lin/Lidz/Ma, etc.)
are confirmed correct. 2006.04810 correctly remains out of bib with a
recommendation to add via `verify-reference`.

**Concept pages updated:**

- [[concepts/SMBH_population_model]] — expanded from stub (~70 → ~130 lines). Now the canonical synthesis of SPZQ 2023 scatter-based approach, Liepold-Ma 2024 stellar-mass-based approach, SPZ 2025 characteristic-function distribution method, Sato-Polito-Kamionkowski frequency spectrum, and Lamb-Taylor spectral variance.
- [[concepts/sqrt_SH_basis]] — added Taylor-vanHaasteren-Sesana 2020 as earlier independent derivation; added verbatim NANOGrav Fig. 1 caption and Hellinger = 0 evidence.
- [[concepts/shot_noise]] — added Lin-Lidz-Ma derivation details, $f^{8/3}$ scaling, LSS Limber projection, and the N_eff continuum-vs-discrete definition subtlety.

**Formulas.md:** added 7 new rows covering sqrt-SH CG coupling, shot-noise
frequency scaling, scatter-boost formulas, population-model polarization
weights, spectral-variance moment scalings, and the M=0.98 isotropy match.

**Index.md:** expanded sources section to 20 pages (11 notes + 9 arxiv).

**Key findings that deserve paper-level attention** (added to [[todo]]):

1. **2306.16221 self-incriminating content**: NANOGrav's own Fig. 1 caption
   says the upper limits are shaped by the positivity prior. Hellinger = 0
   at all frequencies is acknowledged in their Fig. 5. Both quotable.

2. **2006.04810 is an orphan worth adopting**: Earlier independent sqrt-SH
   derivation + M=0.98 isotropy match from realistic SMBHB sky. Both
   directly support the project's argument. Should go through
   `verify-reference` and be cited.

3. **2406.17010 is undercited**: This is the direct precursor to the
   project, introducing the characteristic-function approach to the GWB
   distribution. Currently only 2 citations; should be cited wherever
   the distribution-over-realizations is discussed.

4. **No new concepts proposed** by any subagent. Vocabulary complete.

## [2026-04-13] ingest-notebook | guide_model_comparison

Created [[notebooks/guide_model_comparison]].

Key verified numbers (computed directly from `.npz` arrays):

- $\varepsilon=0.66$: median $h_c^2$ / analytic mean $= 0.571$ at $f_0 \approx 0.085$ yr$^{-1}$.
  Confirms the 57% figure cited in `astrophysical_model.tex:70`.
- $\varepsilon=0.20$: ratio $= 0.988$ (near-Gaussian regime).
- $\varepsilon=0.38$: ratio $= 0.930$.
- Median $p_1$ at $f_0$: 0.020 / 0.052 / 0.155 for $\varepsilon = 0.20 / 0.38 / 0.66$.
- Median $N_{\rm eff}$ at $f_0$: 966 / 191 / 27 for the three models.

HTML export contains no numerical printout cells (Marimo renders interactively only);
source file is the sole authoritative record.

Updated `index.md` notebooks section.

## [2026-04-13] ingest-notebook | guide_power_anisotropy

Created `wiki/notebooks/guide_power_anisotropy.md` (11 sections, 5 key findings).

Input: `results/power_anisotropy_eps066.npz` (10 000 realizations, nside=8,
$\ell_{\rm max}=23$, 44 freq bins, excl. levels 1/5/10/20, top-100 ledger).

Concepts touched: Cl_over_C0, N_eff, brightest_source_fraction,
dipole_distribution, coherent_vs_incoherent, SMBH_population_model, shot_noise.

## [2026-04-13] ingest-notebook | guide_sqrtSH_model

Created `wiki/notebooks/guide_sqrtSH_model.md` (7 sections, 5 key findings).

Validates that the NANOGrav 15yr $C_\ell/C_0$ upper limits are the sqrt-SH
prior sampled from wide uniform $b_{LM}$ priors. Key numerical result: 95th
percentile $C_1/C_0 \approx 0.20$ at $\ell_{\max}^b = 3$ (NANOGrav's actual
choice), reproducing the paper's Figure 1. Confirms two-orders-of-magnitude
drop in this percentile from $\ell_{\max}^b = 3$ to $\ell_{\max}^b = 95$.
Astrophysical $\varepsilon$ models all fall well within the prior space.

Inputs consumed: `sqrtSH_realizations_lmax3.npz`, `_lmax6.npz`,
`_nside8.npz`, `_nside16.npz`, `_nside32.npz`; `power_anisotropy_eps*.npz`.
No output files written.

Cited in paper at `nanograv_prior.tex:22,60,79`.

Backlinks added to: `concepts/sqrt_SH_basis.md`, `concepts/Cl_over_C0.md`.
Index updated.

Backlink added to `wiki/concepts/Cl_over_C0.md`.

## [2026-04-13] ingest-code | scripts/run_power_anisotropy.py

Wrote `wiki/code/scripts_run_power.md` (61 lines). Covers 6-stage pipeline:
population model, realization generation, power-map stacking, brightest ledger,
Cls at 4 exclusion levels {1,5,10,20}, and statistics. Documents all fixed
population parameters and the `--eps` tag scheme.

## [2026-04-13] ingest-result | results/power_anisotropy_eps{020,038,066}.npz

Inspected 3 npz files via `np.load`. All share identical key schema (32 keys).
Key shapes: `power_maps (10000,44,768)`, `brightest_h2s (10000,44,100)`,
`cls_all (10000,44,24)`, `cls_excl_N (10000,44,24)` for N in {1,5,10,20},
summary stats `(44,24)` and `(5,44,24)`. Scalars: Nrel=10000, nside=8,
N_brightest=100, seed=42, Nfreq=44, npix=768, lmax=23.

Pointer pages written:
- `wiki/results/power_anisotropy_eps020.md`
- `wiki/results/power_anisotropy_eps038.md`
- `wiki/results/power_anisotropy_eps066.md`

Consumers identified: `guide_power_anisotropy.py` (eps066 only),
`guide_model_comparison.py` (all three), `guide_dipole_analytics.py` (all three).

Index updated: Code and Results sections populated.

## [2026-04-13] ingest-figure | c1c0_distribution

Created `wiki/figures/c1c0_distribution.md`.

Figure: `paper/figures/c1c0_distribution.pdf` — three-panel $C_1/C_0$
pdf at three frequencies for the $\varepsilon = 0.66$ model ($10^4$
realizations). Overlays exact 3D random-walk Monte Carlo (black) with
four semi-analytic approximations: delta-function brightest-source (blue
dashed), uniform two-source (orange dashed), 1-source + Gaussian
background (green), 2-source + Gaussian background (red).

Generator: `notebooks/guide_dipole_analytics.py`, Sections 4--5
(confirmed via `\fromnotebook` at `distribution_c1c0.tex:96`).
No external `.npz` file consumed; population model run on the fly.

Caption transcribed verbatim from `paper/sections/distribution_c1c0.tex`,
lines 75--85 (`\label{fig:c1c0_pdf}`).

Concepts linked: dipole_distribution, Cl_over_C0, N_eff,
brightest_source_fraction, SMBH_population_model, coherent_vs_incoherent.

Index.md Figures section updated; also corrected stray `\x0b` characters
in the two pre-existing figure bullet lines.

## [2026-04-13] ingest-notebook | guide_interactive

Created `wiki/notebooks/guide_interactive.md`.

Source: `notebooks/guide_interactive.py` (592 lines, Marimo 0.21.1).
HTML export `results/guide_interactive.html` is a Marimo WASM bundle; all
content is in the Python source.

Key content documented:
- 8 sections: definitions, parameter sliders, mass-function + power-kernel
  plot, realizations, strain spectrum, $C_1/C_0$ + $N_{\rm eff}$, histogram
  of $C_1/C_0$ at selected frequency, summary table.
- Method section added documenting the CDF-based source-placement trick:
  pre-compute sorted cumulative-N vs $h^2_s$ per frequency bin; Poisson-draw
  total rare count; uniform variates mapped to $h^2_s$ via `np.interp`;
  bulk contributes deterministic mean + Gaussian noise to $\mathbf{S}$.
  Achieves ~0.5 s wall time for 1 K realizations.
- Four semi-analytic approximations to $C_1/C_0$ distribution benchmarked
  (delta, uniform 2-source, 1-src+Gauss, 2-src+Gauss).

Paper citations confirmed by direct grep of `paper/sections/`:
- `astrophysical_model.tex:50` — power kernel figure.
- `astrophysical_model.tex:65` — CDF realizations.
- `numerical_estimates.tex:34` — summary table.

Concepts touched: SMBH_population_model, brightest_source_fraction, N_eff,
dipole_distribution, Cl_over_C0, shot_noise, coherent_vs_incoherent.

Index updated (guide_interactive moved from Pending to listed).

## [2026-04-13] ingest-batch | Phase 3 — code, scripts, notebooks, figures, results

21 subagents dispatched in parallel covering everything in `gwb_sources/`, `scripts/`, `notebooks/`, `paper/figures/`, and `results/*.npz`. All 21 completed. Consolidation round then pulled the outputs into the index and added cross-backlinks on concept pages.

**Pages created (33):**

- **Code** (10): 7 module pages in `wiki/code/gwb_sources_*.md` + 3 batch-script pages in `wiki/code/scripts_*.md`.
- **Notebooks** (6): `wiki/notebooks/guide_*.md` for all six Marimo notebooks.
- **Results** (12): pointer pages for every `.npz` in `wiki/results/`.
- **Figures** (5): `wiki/figures/*.md` for each paper figure PDF with verbatim caption and generator link.

**Key computed findings, verified against data not eyeballed:**

- `guide_model_comparison` confirmed median/analytic-mean of $h_c^2$ = **0.571** at $\varepsilon = 0.66, f_0 = 0.085/{\rm yr}$. This is the 57% figure in `astrophysical_model.tex:70` and [[concepts/SMBH_population_model]] — previously carried over from memory; now checked against `results/power_anisotropy_eps066.npz`.
- Per-$\varepsilon$ median $p_1$: 0.020 ($\varepsilon=0.20$), 0.052 ($\varepsilon=0.38$), 0.155 ($\varepsilon=0.66$).
- Per-$\varepsilon$ median $N_{\rm eff}$: 966 / 191 / 27.
- Sqrt-SH 97.5th-percentile $C_1/C_0$: 0.233 ($\ell_{\max}^b=3$) vs 0.0007 ($\ell_{\max}^b=95$) — **330× spread**, direct numerical proof that the NANOGrav "constraint" is set entirely by the truncation choice.

**Concept pages updated with code/notebook/figure backlinks:**

`Cl_over_C0`, `N_eff`, `brightest_source_fraction`, `dipole_distribution`, `shot_noise`, `sqrt_SH_basis`, `SMBH_population_model` — each now has a "Notebooks, code, figures" (or similar) section pointing into Phase 3 pages.

**Index rewritten**: all four previously-empty subdirectories now have full populated sections (Code, Notebooks, Results, Figures), replacing the stubs and "pending" placeholders that were in place before Phase 3.

**Findings worth follow-up (added or reinforced in [[todo]]):**

- `gwb_sources.summary_stats.alm_summary_statistics` line 40 may have a bug (doubles `alm_z_abs2[(lmax, 2, 2)]` rather than adding the `m=-2` contribution). Flagged by the summary_stats ingest subagent.
- `find_brightest_source_strain` has a silent correctness assumption that `lum_fct['h2s']` is monotone in the mass axis. Not enforced.
- `run_realizations` (older API) uses a single shared RNG advanced sequentially — not reproducible across independent calls. Use `generate_realizations` for production MC.
- `sky_maps.py` three disabled functions (`zmap_sources`, `gen_realizations_sources`, `gen_realizations_mixed`) confirmed still disabled via `NotImplementedError`. Re-enable or delete.

**Final wiki totals:** 74 files, ≈8,000 lines. Full structure documented in [[index]].

## [2026-04-13] code + env | addressed Phase-3 code items; documented env

**Code changes:**
- `gwb_sources/sources.py::find_brightest_source_strain` — added monotonicity assertion on `strain_bins` and documented the assumption.
- `gwb_sources/summary_stats.py::alm_summary_statistics` — confirmed not a bug; cleaned `x + x` to `2*x` with a physics comment (m=±2 mirror for a real field).
- `gwb_sources/sources.py::run_realizations` — docstring now explicitly says "strain statistics only", points at `generate_realizations` for map/ledger, documents shared-sequential-RNG pattern in a `.. note::`.
- `gwb_sources/sources.py::generate_realizations` — docstring opener points back at `run_realizations` as the lighter alternative; added `.. note::` on per-realization SeedSequence-spawned RNG.

**Env documentation:**
- `CLAUDE.md` now has an "Environment — always use this" section near the top. Names the env (`gw_pta`), gives the absolute python path, and warns against the base env which has an astropy/numpy mismatch.
- `wiki/environment.md` created with package versions, standard commands for tests/scripts/notebooks, and recreate instructions. Linked from `wiki/index.md` at the top of Utility.

**Verification:** 13/13 tests pass under `gw_pta`. The base-env `concatenate() got an unexpected keyword argument 'dtype'` failure is now explicitly explained in `wiki/environment.md` so it never re-surfaces.

## [2026-04-14] ingest | spectral_variance_convergence_note.md

Created `wiki/sources/spectral_variance_convergence.md` from the analysis
note written during the paper revision. Documents why Var[h²_tot] =
Σ N̄_k h⁴_{s,k} doesn't converge in MC for ε=0.66: 99.86% of the
variance lives in mass bins with N̄ < 10⁻⁷ that never fire. The SPZ
PDF grid truncates at x_max = 3.5×10⁵, missing these bins' x² contribution.
Robust statistics (median, percentiles) are unaffected. Frequency-scatter
figure dropped as a result.

## [2026-04-15] ingest | pta_orthogonal_coordinates_note.md

Ingested a new md note on orthogonal coordinates for PTA common-process fits.
Covers: positive-definite covariance parametrization via `r`, optimal-pivot
Schur complement, generalized-eigenvalue decomposition of the diagonal
common sector into robust vs prior-sensitive modes, and the CURN-HD split.
Not currently cited in the paper. Three new concepts proposed (not added):
CURN_HD_split, pivot_optimization, nuisance_orthogonal_projection.

## [2026-04-16] ingest | draft_sufficient_statistics_2026

Ingested `references/sufficient_statistics_4-16-2026.pdf` — draft manuscript
by **Sato-Polito, Zaldarriaga, Zackay (2026)**, "Sufficient statistics for
pulsar timing arrays" (not yet on arxiv; contains in-line `[GSP: ...]`
co-author annotations and a stubbed Fig. 2 caption).

Created [[sources/draft_sufficient_statistics_2026]] (full outline, key
equations, NG15 numbers, concept backlinks).

**Why this matters for our project.** The draft develops the full
sufficient-statistic framework $(a_{\ell m}, b_{\ell m})$ for PTAs and
rigorously proves — in Appendix B via phase-marginalization of a single
template — that template-based searches and anisotropic searches yield
the *same* non-diagonal Gaussian covariance. This is the formal
underpinning of our project's qualitative claim that the anisotropy and
single-source searches are probing the same information, with the
$C_\ell$ compression losing most of it.

**Numerical cross-checks (all match our wiki):**

- Single-source pulsar-term power $C_1/C_0 = 1/4$ and $C_2/C_0 = 1/100$
  (draft Eq. 23) — agrees with [[sources/pta_1src_vs_CL]] and
  [[concepts/Cl_over_C0]].
- Single-source $a_{\ell m}$ nonzero only for $m=\pm 2$ (draft §III.A).
- Stochastic $b_{LM}$: $\langle b_{LM}\rangle = \sqrt{4\pi}\,\delta_{L0}\delta_{M0}$;
  single-source $b_{00}=\sqrt{4\pi}$, $b_{10}=(\sqrt 3/2)b_{00}$,
  $b_{20}=(\sqrt 5/10)b_{00}$ (Eqs. 20-22).
- NG15 HD detection: $\rho_{HD} = 3.14$, consistent with published Bayes
  factor; four most sensitive pulsars: J1713+0747, J1909-3744, B1937+21,
  J1640+2224.
- $N_s^{\rm eff}\sim 3$ resolvable GW sources for $N_p=150$, $\varepsilon=0.2$;
  saturates as true $N_s$ grows — information-theoretic statement of our
  "few bright sources dominate" picture.

**Novel results / numbers not in our project:**

- Maximum possible matched-filter significance under phase-marginalized
  Gaussian likelihood is $\sim 3.8\sigma$ (from $p[\chi_4^2 > 2/f_\sigma = 24]$,
  $f_\sigma = 1/12$). Intrinsic ceiling — cannot be improved by noise
  reduction. Potentially useful for the discussion section.
- $\kappa = \sum_\ell 2(2\ell+1)/[(\ell+2)(\ell+1)\ell(\ell-1)]^2$ with
  $\ell=2$ carrying 94% of the sum, $\ell\le 3$ carrying 99.2%.
  This makes the per-$\ell$ weight decomposition of the HD SNR$^2$ explicit.
- Gaussian-approximation KL error $\sim (3/32)\varepsilon^4/(1+\varepsilon)^4/N_p^2$
  (Eq. A11). Our single-source ($\varepsilon \lesssim 0.2$, $N_p \sim 150$)
  regime has negligible non-Gaussianity — the framework applies.

**Potential bib additions (not verified; `verify-reference` before use):**

- Roebber & Holder 2016 (arXiv:1609.06758) — harmonic-space analysis of PTA redshift maps; foundational methodological reference ([7] in the draft).
- Hotinli, Kamionkowski, Jaffe 2019 (arXiv:1904.05348) — PTA anisotropy ([8]).
- Tegmark 1997 (arXiv:astro-ph/9611174) — CMB power spectra without info loss ([10]).
- van Haasteren et al. 2009 (arXiv:0809.0791), 2013 (arXiv:1202.5932) — PTA data analysis ([11], [12]).
- Hazboun, Romano, Smith 2019 (arXiv:1907.04341) — `hasasia` sensitivity curves ([9]).
- Kamionkowski, Land, Magueijo 2005 (arXiv:astro-ph/0502237) — "axis of evil" statistic $t_\ell$ ([15]); direct precedent for §IV.B.
- de Oliveira-Costa, Tegmark, Zaldarriaga, Hamilton 2004 (arXiv:astro-ph/0307282) ([16]).
- Cornish & Romano 2013 (arXiv:1305.2934) — unified treatment of GW data; cited for the template ≡ anisotropic equivalence ([17]).
- NANOGrav harmonic analysis 2025 (arXiv:2411.13472) ([14]); NANOGrav targeted SMBHB 2026 (arXiv:2508.16534) ([18]); NANOGrav "discreteness" 2025 (arXiv:2404.07020) ([20]).

**Backlinks added:**

- [[concepts/matched_filter_vs_power]] — draft App. B is the rigorous formalization of this concept.
- [[concepts/Cl_over_C0]] — draft Eq. 23 confirms single-source pulsar-term ratios.
- (Remaining concept pages — fisher_hierarchy, sqrt_SH_basis, N_eff, KL_divergence, coherent_vs_incoherent, transfer_function, prior_sensitivity, brightest_source_fraction — touched via the source page's "Concepts" section; not separately edited in this pass. Consider spreading the backlinks if the draft goes live.)

**Sources subdir count: 21** (was 20). No new concept pages created.
No new formulas added to `formulas.md` yet — the draft's Eq. 39 ($\kappa$-weighted
HD SNR$^2$) and Eq. 46 ($N_s^{\rm eff}$) are candidates if the draft
gets cited in the paper.

## [2026-04-17] critique + ingest | App. B of draft_sufficient_statistics_2026

**New source page:** [[sources/pn_appendixB_coherent_vs_covariance]] —
ingested a ChatGPT pedagogical note (placed by the user in
`references/appendixB_coherent_vs_covariance_note.md`) that
independently critiques App. B of the draft and reaches the same
overall verdict as our in-house analysis: "Eq. (B6) can be right, but
Appendix B is the wrong way to derive it." Adds three orthogonal
framings:

1. Separation of the two distinct statistics in the draft: Eq. (49)
   $t_\ell(\hat n)$ (single-$\ell$ alignment score) vs Eq. (B6)
   $T(\hat n)$ (multi-$\ell$ coherent combination). Our original note
   treated these as one object.
2. $\partial C/\partial\mu|_0 = 0$ one-liner: writing $\vec h = \mu\bar{\vec h}$,
   the covariance $C(\mu) = N + \mu^2 \Delta C$ gives
   $F^{\rm cov}_{\mu\mu}|_0 = 0$ identically. Sharpest statement of
   "the coherent order is lost."
3. Internal inconsistency catch: the uniform-angle marginalization
   stated in words near Eq. (B2) does not actually produce the
   Gaussian prior on $\vec h$ imposed in Eq. (50).

**Revised critique memo:** [[notes/app_B_coherent_fisher_critique]].
Rewrote end-to-end to fold in the ChatGPT framing and correct two
framing errors in the original draft:

- **Corrected**: the earlier claim that "$T$ has $\rho^2\propto H^2$"
  — wrong in general. $T/\sigma_A^2$ is non-central $\chi^2_4$ with
  non-centrality $\lambda = H\,\mathcal F_{\rm tot}$ under $H_1$, so
  detection significance is linear in $H$ when tested against the
  no-signal null (Problem A). The $H^2$ scaling is a property of the
  same-power discrimination problem (Problem B) App. B implicitly
  sets up via Eq. (50), not a property of the test statistic.
- **Rescoped**: the "integrate the likelihood, not the log-likelihood"
  diagnostic is now only a short aside (§7), and clarifies that the
  paper does NOT integrate the log-likelihood — it integrates the
  likelihood and Gaussianizes, which agrees with the proper marginal
  at leading order in $|h|^2/\sigma^2$. The Gaussianization is
  harmless at PTA SNR; the real issue is the task framing, not the
  approximations within it.
- **New framing** (§1, §4, §5): "same $T$, two nulls, two detection
  scalings." The statistic is a function of the data; its
  distribution under different nulls gives different detection
  significances. Eq. (50) pins App. B to the same-power null, yielding
  $\rho^2\propto H^2$ with the $\sim 3.8\sigma$ ceiling; a detection
  setup with a noise-only null gives $\rho^2\propto H$ with no ceiling
  from the same formula.

**Final structure of the memo (10 sections):** one-paragraph
resolution; two statistics in the draft; coherent derivation
(matrix form + toy-limit reduction + Wigner-D Fisher block); two nulls
comparison table; covariance-Fisher-vanishes argument; coincidence
conditions (linear template + Gaussian prior + isotropic response);
Gaussianization-is-fine-at-PTA-SNR aside; prior-inconsistency catch;
5-point summary for collaborator; relation to project hierarchy.

Both pages cross-linked from [[sources/draft_sufficient_statistics_2026]].
Index updated.

No changes to `formulas.md`, concept pages, or paper sections. The
draft has not yet been cited in the project paper, so concept-page
backlinks were not updated (flag for later if the draft becomes a
citation). Internal discussions of hierarchy ordering in
[[concepts/fisher_hierarchy]] and [[concepts/matched_filter_vs_power]]
remain consistent with the revised memo.

## [2026-04-17] revise | App. B critique — cosmic-variance refactor

Second pass on [[notes/app_B_coherent_fisher_critique]]. Triggered by
user's observation that the $H\to H^2$ scaling demotion is itself a
cosmic-variance-type effect (analogous to CMB $\hat C_\ell$'s
irreducible $2C_\ell^2/(2\ell+1)$ variance), not specifically a
property of the same-power null.

**Conceptual refinement.** The earlier (2026-04-17 morning) draft
attributed both the $H\to H^2$ scaling and the $\sim 3.8\sigma$
ceiling to "Problem B = same-power discrimination." That lumped two
separable effects. The correct factoring is:

- **Step 1: stochasticization** (coherent → covariance). Replacing
  deterministic $\vec h$ by $\mathcal{CN}(0,qI)$ makes the source a
  zero-mean Gaussian field. $\hat q = |\hat{\vec h}|^2/k$ then has
  $\mathrm{Var}(\hat q) \geq q^2/k$ at zero noise — cosmic-variance
  limit, directly analogous to
  $\mathrm{Var}(\hat C_\ell) \geq 2C_\ell^2/(2\ell+1)$ in CMB. Fisher
  on any scalar strength parameter $\mu$ with $C(\mu) = N + \mu^2\Delta C$
  has $\partial C/\partial\mu|_0 = 0$ identically, forcing
  KL $\propto \mu^4 \propto H^2$ at small $H$. **This step alone
  demotes $\rho^2$ from $\propto H$ to $\propto H^2$, regardless of
  what null is used.**
- **Step 2: same-power null** (Eq. 50). Pinning $H_0$ to an isotropic
  GWB with matched trace is what produces the $\sim 3.8\sigma$
  ceiling. Under that null, $\hat H \sim (f_\sigma H/2)\chi^2_4$ in
  the zero-noise limit, and the $H_1$ point estimate at $\hat H = H$
  sits at $\chi^2_4 = 2/f_\sigma = 24$ in the null distribution.
  $f_\sigma = \sum z_\ell^4/(\sum z_\ell^2)^2 = 1/12$ is the inverse
  effective number of modes after the $z_\ell$ kernel — plays the
  $1/(2\ell+1)$ role of CMB cosmic variance.

**Section-by-section changes to memo:**

- §1 one-paragraph resolution — rewritten to distinguish the two
  lossy steps up front.
- §4 table — expanded from 2 columns to 3: **Problem A** (coherent),
  **Problem A′** (covariance, noise-only null — quadratic scaling,
  no ceiling), **Problem B** (covariance, same-power null — quadratic
  with $3.8\sigma$ ceiling). Hierarchy A → A′ → B, each step
  strictly lossier.
- §5 restructured as "Two separable lossy steps":
  - §5.1 Stochasticization — $\partial C/\partial\mu|_0 = 0$
    argument, equivalent $q$-parametrization, cosmic-variance formula,
    explicit CMB parallel.
  - §5.2 Same-power null — derives the $3.8\sigma$ ceiling formally
    via the $\chi^2_4$ tail, shows that Problem A′ has no such
    ceiling ($D_{KL} \sim \kappa q - k\ln(1+q\kappa)$ grows linear-
    minus-log).
- §7 Upshot paragraph — corrected: the Gaussianization is upstream of
  neither scaling loss; both losses are in §5.1 and §5.2.
- §9 summary — bullet 3 factored into the two sub-bullets
  (stochasticization, same-power null) with the cosmic-variance
  analogy.
- §10 relation to project — rephrased to emphasize that the
  cosmic-variance form $\mathrm{Var}(\hat P) \geq P^2/\text{modes}$ is
  the clean statement of our coherent-over-incoherent $p$-factor,
  now for a single source rather than an ensemble.

**Consistency sweep** across related pages:

- [[sources/draft_sufficient_statistics_2026]] — critique-notes block
  rewritten to factor the two lossy steps; old phrasing that lumped
  them under "same-power null" is replaced by the two-step layout.
- [[sources/pn_appendixB_coherent_vs_covariance]] — "Corrections"
  section rewritten: earlier text incorrectly attributed $H^2$
  scaling to the same-power null alone. New text: scaling comes from
  stochasticization; ceiling comes from same-power. Cross-link to
  memo updated from "pre-correction" to "rev. 2026-04-17."
- Index entry under "Companion drafts" — no change needed; it already
  just points to the memo without characterizing the argument.
- This log entry documents the refactor so that future readers know
  the earlier (morning) entry of 2026-04-17 reflects the pre-refactor
  framing.

Concept pages [[concepts/fisher_hierarchy]] and
[[concepts/matched_filter_vs_power]] still read consistently with the
new memo — the project-level statement has always been
"coherent (linear) beats covariance (quadratic)"; the memo now just
gives the cleanest single-source realization of that, with explicit
CMB parallel.

## [2026-04-20] ingest | coherent_vs_stochastic_single_source

**New source page:** [[sources/pn_coherent_vs_stochastic_single_source]].
Ingested `references/coherent_vs_stochastic_single_source.md` — a
self-contained single-bin, single-template calculation that sharpens
the coherent-vs-stochastic discussion at its cleanest toy and
separates two claims that can easily be confused:

**(I) Detection tests are monotone-equivalent.** For the scalar-
amplitude linear-template problem, the maximized LLRs are
$T_1 = s$ and $T_{1^\star} = \max(s - 1 - \ln s, 0)$ with
$s = (\vec t^T N^{-1}\vec d)^2/\rho^2$, $\rho^2 = \vec t^T N^{-1}\vec t$.
The map $s \mapsto s - 1 - \ln s$ is strictly increasing on $s\geq 1$,
so the two statistics have **identical p-values, identical ROC,
identical detection significance** on every realization, regardless
of the truth.

**(II) Fisher information differs.** $F_{H_1}(\mu) = \rho^2$ (constant);
$F_{H_1^\star}(\mu^2) = \rho^4/[2(1+\alpha)^2]$. The Cramér–Rao bound
on the stochastic estimator grows as $(1+\alpha)^2$ — textbook
variance-parameter feature, analogous to
$\mathrm{Var}(\hat\sigma^2) \geq 2\sigma^4/n$.

**(III) The $\alpha$-vs-$\alpha^2$ KL gap is physics, not modeling.**
If truth is coherent at amplitude $\mu$: $s \sim \chi^2_1(\alpha)$ →
KL from $H_0$ scales as $\alpha$ (linear). If truth is stochastic at
matched power $\alpha$: $s \sim (1+\alpha)\chi^2_1$ → KL scales as
$\alpha^2$ (quadratic). This difference is attached to the
data-generating distribution, not the analyst's modeling choice.

**Cautionary**: the statistic-level equivalence relies on the
one-dimensional structure. Multi-parameter, non-Gaussian-prior, or
non-linear-template settings can break the equivalence and restore
the "linear beats quadratic" detection-level statement.

**Implication for the App. B critique memo.** The
two-step factoring in [[notes/app_B_coherent_fisher_critique]] overstates
Step 1. Stochasticization alone is NOT what demotes $\rho^2 \propto H$
to $\propto H^2$ at the detection stage in the single-template toy —
that demotion appears only when the data are actually generated by a
stochastic signal (physics) or when the null is changed to a
matched-power covariance model (Eq. 50). What stochasticization does
is re-parametrize the reported estimator from $\hat\mu$ (Fisher $\rho^2$)
to $\hat\alpha$ (Fisher $\rho^4/[2(1+\alpha)^2]$) — a parameter-
interpretation effect, not a detection effect.

**Pending revision (Phase 3)**: the memo should be rewritten once more
to reflect this. Current plan:
- Replace "two separable lossy steps" with "one lossy step (Eq. 50
  same-power null) + one parameter-interpretation effect (stochastic
  parameter has poorer Fisher)."
- Import §4 of the new note as a clean monotone-equivalence
  derivation right after §4 of the memo (the three-picture table).
- Clarify that the cosmic-variance formula
  $\mathrm{Var}(\hat q) \geq q^2/k$ is a Fisher/parameter statement,
  not a detection-significance statement. CMB parallel still holds,
  but framed as "cosmic variance limits $C_\ell$ *estimation*
  precision," not "$C_\ell$ detection power."
- The $\sim 3.8\sigma$ ceiling becomes the *single* critique point
  about App. B's headline result — attributable entirely to Eq. 50.
- The caveat about multi-parameter breakdown of monotone equivalence
  is important: App. B has two complex amplitudes and a sky
  direction, not a single scalar, and the 2-template isotropic case
  we verified in the discussion is clean but not necessarily
  representative of the full multi-sky-position search.

User asked to ingest the note first; memo revision deferred until
they do another pass.

**Pages updated this round:**
- [[sources/pn_coherent_vs_stochastic_single_source]] — created.
- [[sources/draft_sufficient_statistics_2026]] — critique-notes block
  extended with the new note and its implication.
- [[index]] — Companion-drafts section updated; memo entry flagged
  "pending revision."
- This log entry documents the pending Phase-3 revision.

**Pages not updated (but flagged):**
- [[notes/app_B_coherent_fisher_critique]] — framing now partly
  overstated; awaiting user-initiated Phase-3 revision.
- [[sources/pn_appendixB_coherent_vs_covariance]] — ChatGPT note's
  §7.4 ("$\vec h \to \vec h\vec h^\dagger$ is many-to-one") still
  holds as a *multi-parameter* statement but is not the
  single-template story the new note tells.
- [[concepts/matched_filter_vs_power]] — its draft-bullet summary is
  still consistent at the level of "App. B's derivation is the wrong
  way, $T(\hat n)$ is the right statistic," but the specific
  two-step attribution should be revisited in the Phase-3 pass.

## [2026-04-20] Phase-3 | App. B critique memo — multi-agent rewrite

Executed the user-designed four-agent workflow to revise the App. B
critique memo in light of
[[sources/pn_coherent_vs_stochastic_single_source]]:

- **P1 (2-polarization equivalence check).** Agent calculation at
  [[notes/app_B_2pol_equivalence_check]]. Explicit Woodbury + matrix-
  determinant-lemma derivation of $T_{1^\star} = \max(s-2-2\ln(s/2),0)$
  with $s = s_+ + s_-$ for App. B's 2-polarization isotropic toy
  limit. $T_1$ and $T_{1^\star}$ are both functions of $s$ only, and
  $g_2(s) = s-2-2\ln(s/2)$ is strictly increasing on $s\geq 2$. So
  monotone equivalence holds, and survives sky-direction
  maximization. General formula: $T_{1^\star}^{(k)} = \max(s-k-k\ln(s/k),0)$.
  Equivalence is fragile to non-isotropic priors ($Q\neq qI_2$).

- **P2 (anisotropic-response analysis).** Agent calculation at
  [[notes/app_B_anisotropic_response]]. In the eigenbasis of the
  realistic $F = U^\dagger N^{-1} U$ with eigenvalues $\rho_i^2$,
  $T_1 = \sum_i |v_i|^2/\rho_i^2$ (unit weights) and
  $T_{1^\star} = \sum_i w_i|v_i|^2/\rho_i^2 - \sum_i \ln(1+q\rho_i^2)$
  with $w_i = q\rho_i^2/(1+q\rho_i^2)$. Monotone iff all $\rho_i^2$
  equal. For realistic NG15 asymmetry ($r=\rho_1^2/\rho_2^2\sim 2$
  typical), rank disagreement is 10–20% of $T_1$ at fixed sky, up
  to $\sim 50\%$ in $m=0$ null directions; p-value shift a few
  percent. Mild third critique, orders of magnitude smaller than the
  Eq. (50) ceiling.

- **Proposer agent.** Produced [[notes/app_B_memo_revision_proposal]].
  Recommended **Option A**: one main critique (Eq. 50 same-power null,
  $\sim 3.8\sigma$ ceiling) plus two side observations (Fisher-on-$q$
  parameter interpretation; anisotropic-response breakdown). Full
  revised memo draft included.

- **Critique agent.** Produced [[notes/app_B_memo_revision_critique]].
  Verdict: **accept with revisions**. Caught:
  - (M1, critical) Proposer's "3.6σ vs 3.8σ" worry was unfounded —
    direct computation gives $p[\chi^2_4 > 24] = 7.99\times 10^{-5}
    \to 3.78\sigma$ one-sided, matching the paper exactly. The earlier
    "$\sim 3\times 10^{-4}$" loose value had been the seed of the
    confusion.
  - (M2, critical) The App. B $k=2$ polarization mode count and the
    $1/f_\sigma = 12$ kernel effective-mode count are two different
    Fisher saturations. The CMB $1/(2\ell+1)$ parallel maps to the
    latter, not the former.
  - (M3, medium) §5 detection-ratio derivation was dimensionally
    loose; should go directly from $\hat H|_{H_0}$ distribution to
    $\chi^2_4$ tail at $2/f_\sigma = 24$.
  - (M4, medium) §4.4 sky-max argument is a theorem only in the
    isotropic limit; needs explicit caveat.
  - (M5, light) §7 "typical NG15" language should reflect that P2
    computes a typical-sky-position number ($r\sim 2$), not a
    sky-average.
  - (C2–C6) Various tighten-ups.

- **Incorporation.** Applied all critical and medium fixes plus
  chosen cosmetic fixes:
  - M1 fixed in §5 and §10 item 4 — quote $7.99\times 10^{-5}$ one-sided.
  - M2 fixed in §6 — explicit $k=2$ label, separate section on "two
    distinct Fisher saturations" clarifying $k$ (polarization) vs
    $1/f_\sigma$ (kernel) with the CMB parallel correctly mapping
    $1/(2\ell+1) \to 1/f_\sigma$.
  - M3 fixed in §5 — go directly from $\hat H|_{H_0}$ distribution to
    $\chi^2_4 = 2/f_\sigma = 24$ tail.
  - M4 fixed in §4.4 — explicit caveat about sky-max being a theorem
    only in the isotropic limit.
  - M5 fixed in §7 — "typical sky positions on NG15 array ($r\sim 2$)".
  - C2 applied — added "in the App. B toy limit" scope to the lead,
    "single scaling-level critique" language.
  - C3 applied — italicized one-liner "*The ceiling is a property of
    the choice of null, not of the choice of statistic.*" at top of §5.
  - C4 applied — §4.5 now mentions non-isotropic-prior breakdown for
    completeness.
  - C5 applied — §7 clarifies rank disagreement is real but p-value
    shift is small.
  - C6 applied — §5 unpacks Eq. (50) as "Gaussian prior on $\vec h$ +
    specific choice of $\sigma_h^2$ matching GWB power."

  New memo structure (11 sections): one-sentence conclusion
  (mentions toy-limit scope explicitly), §1 one-paragraph resolution,
  §2 two statistics, §3 coherent derivation (matrix + toy-limit +
  Wigner-D Fisher), §4 monotone equivalence ($k=2$ isotropic case),
  §5 main critique (Eq. 50 ceiling), §6 parameter-interpretation
  side observation, §7 anisotropic-response side observation,
  §8 Gaussianization, §9 prior inconsistency, §10 collaborator
  summary, §11 relation to project.

**Consistency sweep across related pages:**

- [[sources/draft_sufficient_statistics_2026]] — critique-notes block
  rewritten to list all five documents (memo, ChatGPT note,
  single-source note, P1, P2) with the new one-line headline.
- [[concepts/matched_filter_vs_power]] — draft bullet rewritten: the
  linear-beats-quadratic statement of this concept page **does not
  apply** to the App. B toy limit in the naive "stochasticization
  demotes detection" sense; it applies in cases (a)–(d) listed in the
  memo §11.
- [[index]] — Companion-drafts block expanded to list all five
  documents with their specific roles.
- [[notes/app_B_memo_revision_proposal]] and
  [[notes/app_B_memo_revision_critique]] — retained as audit-trail
  artifacts; referenced from the draft source page.

**Flagged for future attention (not in scope):**

- [[concepts/fisher_hierarchy]] — contains one paragraph from the
  pre-Phase-3 memo ("Turning the former into the latter is the App. B
  step that costs the coherent order") that now reads as overstated
  in the single-source context. The $p$-hierarchy itself is a
  multi-source ensemble statement and remains correct; only the
  framing paragraph needs a parallel edit in a later pass.

- User mentioned P4 (outgoing message to GSP) is not needed — GSP is
  the source of the ChatGPT note and the single-template note. The
  memo is the final artifact of this critique cycle.

## [2026-04-24] ingest | HD_vs_CURN_Fisher_Bayes_note

Pedagogical note on a principled Fisher estimate for HD detection and
its relation to the Bayesian HD-vs-CURN analysis. Created
[[sources/pn_HD_vs_CURN_Fisher_Bayes]].

**Headline content.** The Bayesian HD-vs-CURN comparison (Agazie et
al.) is a test of two spatial covariance *shapes* for the same
common-spectrum process, at fixed common auto-power. The correct
Fisher analog introduces a shape parameter
$C(\eta) = N + \Phi\otimes[I + \eta(\Gamma-I)]$ with
$\eta=0$ ≡ CURN, $\eta=1$ ≡ HD. Because $(\Gamma-I)_{aa}=0$, varying
$\eta$ leaves the common auto-power fixed. The profiled Fisher
$F^{\rm prof}_{\eta\eta}$ evaluated at $\eta=0$ is the local quadratic
approximation to the Bayes factor, with
$D_{\rm KL}({\rm HD}\,\|\,{\rm CURN})\simeq\tfrac12 F_{\eta\eta}$ for
the unit step. An explicit two-pulsar toy verifies this at leading
order. The generic floating-amplitude argument gives
$D^{\rm prof}_{\rm KL} = \tfrac14[\mathrm{tr}(A^2)-(\mathrm{tr}A)^2/n]
+ O(A^3)$: floating the isotropic level kills the linear term.

**Consequence for the current draft.** The null covariance for a
detection forecast should include the common auto-power
($K_0 = N + \Phi\otimes I$), **not** the HD "cosmic variance" piece.
Fisher evaluated at nonzero HD fiducial is a post-detection *parameter*
forecast, not a detection forecast. The derivatives in
`paper/sections/appendix_fisher.tex` should in principle be taken with
respect to a shape parameter (linear in $C$), evaluated at the CURN
point.

**Relation to existing wiki content.** Structurally identical to
[[sources/pta_orthogonal_coordinates]] (same interpolation, named $r$
there; same exact orthogonality $F_{r,A}=0$ at $r=0$). The present
note is narrower: Bayes-vs-Fisher bridge and the "don't count autos as
HD evidence" consequence. The two notes are strongly complementary
and should be cited together in any CURN↔HD passage. Terminology
unification (pick $\eta$ or $r$) should precede citation.

**Concept backlinks added.** [[concepts/KL_divergence]],
[[concepts/source_background_degeneracy]],
[[concepts/coherent_vs_incoherent]],
[[concepts/fisher_hierarchy]],
[[concepts/matched_filter_vs_power]],
[[concepts/prior_sensitivity]].

**Not cited in the paper yet.** Candidate placements:
`appendix_fisher.tex` (where to evaluate the HD Fisher),
`three_strategies.tex` (CURN-vs-HD analog of the $p$-hierarchy),
`numerical_estimates.tex` (concrete $K_0$ choice for a forecast),
`discussion.tex` (the "auto-power should not increase" framing).

**Open items.** (1) No numerical $F^{\rm prof}_{\eta\eta}$ for NG15
parameters — a concrete plug-in would make the draft correction
operational. (2) Terminology unification with
[[sources/pta_orthogonal_coordinates]] before paper citation.
(3) Agazie et al. 15 yr *evidence* paper (distinct from the
anisotropy companion, [[sources/arxiv_2306_16221]]) is not yet in
the wiki bibliography; should be added via `verify-reference`
before any citation.

## [2026-04-24] ingest | pta_curn_hd_cross_only_self_contained_v4

Pedagogical note (v4) deriving the local Fisher relation between the
physical HD-plus-CURN Bayesian posterior and the cross-only quadratic
estimator. Created [[sources/pta_curn_hd_cross_only]].

**Headline content.** In the reparametrization $P = A_{\rm C} + A_{\rm H}$,
$B = A_{\rm H}$, with $\Gamma = I + X$, $X_{ii}=0$, the covariance is
$C(P,B) = N + PI + BX$. At a CURN expansion point $C_0 = N + P_*I$
with $D = C_0^{-1}$ diagonal, $F_{PB} = \tfrac12 \mathrm{tr}(D^2 X) = 0$
**exactly** (since $X_{ii}=0$). The local likelihood factorizes and
the nuisance-projected HD score is cross-only:
$S_{\rm H}^\perp = S_B = \sum_{i<j} D_i D_j X_{ij} d_i d_j$,
$F_{\rm H}^\perp = F_{BB} = \sum_{i<j} D_i D_j X_{ij}^2$. This is why
the "optimal statistic" cross-only quadratic estimator equals the
nuisance-projected HD Fisher score.

**The new wrinkle.** The physical nonnegativity prior
$A_{\rm C}, A_{\rm H} \ge 0$ maps to the boundary $P \ge B$. A
GWB-with-no-CURN truth sits *exactly* on this boundary. Enforcing it
adds a factor $\log\Phi((\hat P - B)/\sigma_P)$ to the marginal HD
posterior (or a half-quadratic penalty in profiled form). This is
*diagonal* information. It is important when
$\sigma_P \lesssim \sigma_B$, which in the equal-variance limit is
$(n-1)\overline{X^2} < 1$. So the physical HD posterior is **not**
generally cross-only when the autos outconstrain the crosses.

**Three-way impossibility** (Sec. 14): one cannot simultaneously have
(a) a globally physical covariance model, (b) nonnegative physical
amplitudes, and (c) a posterior for the HD amplitude constrained
only by crosses. To get a genuinely cross-only answer, the *target*
must change: from the physical $A_{\rm H}$ to the off-diagonal HD
pattern amplitude $B_\times$ in $C = N + PI + B_\times X$ with $P$
independent of $B_\times$ (free-sign, local nuisance parametrization).

**Relation to existing wiki content.** This note is the immediate
complement to [[sources/pn_HD_vs_CURN_Fisher_Bayes]] (ingested same
day). That one fixes the common auto-power via the shape parameter
$\eta$ and derives $D_{\rm KL} \simeq \tfrac12 F_{\eta\eta}$ for the
detection forecast. This note lets the common auto-power float
($(P, B)$ parametrization), reproduces the cross-only quadratic
estimator, and then tracks what happens when the one-sided CURN
prior is enforced. Both live alongside
[[sources/pta_orthogonal_coordinates]] which uses the shape parameter
$r$. The three notes converge on the same structural orthogonality
($F_{A\eta} = F_{AB} = F_{Ar} = 0$ at the CURN null) with different
parametrizations; **terminology unification is a blocker for any
paper citation** of the three.

**Concept backlinks added.** [[concepts/source_background_degeneracy]]
(the structural $F_{PB}=0$), [[concepts/coherent_vs_incoherent]] (the
cross-only estimator as the canonical incoherent object),
[[concepts/KL_divergence]] (local KL $\simeq \tfrac12 B^2 F_{BB}$ plus
boundary correction), [[concepts/fisher_hierarchy]] (quantitative
$(n-1)\overline{X^2} < 1$ regime), [[concepts/prior_sensitivity]]
(one-sided CURN boundary as a distinct prior-sensitivity mechanism),
[[concepts/matched_filter_vs_power]] (pairwise pseudo-likelihood as
the canonical power-type statistic).

**Not cited in the paper yet.** Candidate placements:
`appendix_fisher.tex` (clean statement of nuisance-projected HD
Fisher), `three_strategies.tex` (the $(n-1)\overline{X^2} < 1$
regime as a new subtlety in the incoherent strategy),
`numerical_estimates.tex` (plug in NG15 numbers to determine whether
the boundary term is numerically important),
`discussion.tex` (three-way impossibility as a framing theorem).

**Open items.** (1) Compute $(n-1)\overline{X^2}$ for NG15 ($n=67$,
actual HD matrix) to determine whether the boundary term is
numerically important. (2) Extend to multiple frequency bins with
shared spectral shape — the single-bin analysis here understates the
auto-power constraint. (3) The "optimal statistic" literature
(Anholm-Chamberlin-Romano-Siemens) is the direct origin of the
pairwise pseudo-likelihood but is not cited in the note; adding a
bibliography entry requires `verify-reference`. (4) Terminology
unification with [[sources/pn_HD_vs_CURN_Fisher_Bayes]] and
[[sources/pta_orthogonal_coordinates]] before any paper citation.

---

## [2026-06-13] ingest | source-detection note → wiki/sources/pta_source_detection_likelihood

`references/pta_source_detection_likelihood_notes_for_review.md` →
[[sources/pta_source_detection_likelihood]]. Canonical PTA-native
derivation of five detection likelihoods for one bright source +
isotropic background. **Refines** the wiki's "incoherent covariance
$\propto p^2$": the source-subspace projector covariance $I+\eta\Pi$ has
profiled LR $g_r(T_{\rm coh})=T-r-r\log(T/r)$, strictly increasing in
$T_{\rm coh}$, so it is monotone-equivalent to the coherent matched
filter (same threshold $p_{{\rm sub},*}=p_{{\rm coh},*}$, $\propto p$).
The genuine $p^2$ object is the one-source power-map / physical
Gaussian-marginalized construction $T_{\rm psrc}$. New intermediate
object: $T_{\rm map}=s^TF^{-1}s$ (one-source norm $\propto p^2$ but
$m$-dof threshold penalty). $C_L$ stays $\propto p^4$, now block-resolved
$D_{C_L}=\tfrac{p^4}{4}\sum_L[v_L^TF_Lv_L]^2/(2L+1)$. Source-power-sky
identity $C_L^P/C_0^P=p^2$ confirmed (response-free, consistent with the
convention contract). Concept-page refinements made to
[[concepts/fisher_hierarchy]] and [[concepts/coherent_vs_incoherent]];
backlinks queued for matched_filter_vs_power, KL_divergence, Cl_over_C0,
source_background_degeneracy, sqrt_SH_basis.

## [2026-06-13] ingest | toy-model evidences note → wiki/sources/toy_model_source_vs_power_map

`references/toy_model_source_vs_power_map_evidences.md` →
[[sources/toy_model_source_vs_power_map]]. Self-contained Gaussian toy
(notebook-ready). Bayesian-evidence complement of the source-detection
note: one-source models SUM over locations ($1/N$ look-elsewhere), map
/$C_\ell$ models MULTIPLY over pixels; averaged $C_\ell$ Bayes factor on
a one-source sky equals $b_{\rm cov}(s;V_1)$ with $V_1=\sum_k C_k$, but
the typical log-evidence is penalized by $\ell_0(q)<0$ per empty pixel.
Flagged as the basis for the source-template-vs-raw-$C_\ell$ Monte-Carlo
figure proposed in the rewritten section.

## [2026-06-13] ingest | companion paper → wiki/sources/joint_search_resolved_unresolved

Goncharov, Sato-Polito, Bi, Zaldarriaga 2026, *A Joint Optimal Search
for GWs from Resolved and Unresolved SMBHBs with the NANOGrav 15-yr
data* (companion observational draft; MZ co-author; not on arXiv) →
[[sources/joint_search_resolved_unresolved]]. Source preserved at
`references/joint_search_smbhb/` (text only; PDF already in references/).
Captured: $N_c$ as SMBHB-origin detection statistic ($N_c\ge1000$ null);
NG15 non-detection ($N_c$ consistent with 1000, no resolvable CW); 24/114
AGN candidates in tension; CW detection probability 0.6%/2% (15/20yr,
SNR 5). This is the empirical realization of the coherent top rung of the
hierarchy. Provisional bib key `Goncharov:2026joint` NOT added to
`references.bib` (unpublished → verify-reference cannot run); companion
note added to [[bibliography]]. Manifest entry added to
[[reproducibility]].

## [2026-06-13] ingest | off-topic stub → wiki/sources/gw231123_likelihood_islands

`references/gw231123_toy_model_note.md` →
[[sources/gw231123_likelihood_islands]]. Ground-based GW
parameter-estimation likelihood geometry (heavy high-SNR merger event,
isolated posterior islands). Unrelated to PTA anisotropy; clearly flagged
off-topic; not cited by the paper; concepts_touched intentionally empty.

## [2026-06-13] draft | reduced replacement for paper Secs. 6-7

`paper/sections/source_vs_cl_reduced.tex` (NEW file, ~850 words) drafted
via a 3-way judge panel. Replaces Sec. VI (`three_strategies.tex`) + Sec.
VII (`numerical_estimates.tex`) with one tight section: anisotropy is
dominated by the brightest source; the source/CW search is the right
tool; a same-question excess-power search is statistically equivalent
(projector-covariance monotone equivalence) while $C_\ell$ throws
information away ($p^4$); the companion CW search already finds nothing
($\sim0.6\%$/$2\%$ detection probability); combined with Sec. V (the
$C_\ell$ "constraints" are just the prior). **Existing Secs. 6-7 left
intact** for comparison — not yet `\input` in `main.tex`. (A workflow
agent's test-compile had transiently overwritten the two existing
sections; reverted to HEAD.) Proposed Monte-Carlo figure left as a
`% [to be generated]` comment. Judge panel caught and rejected an
"eyeballing"-rule violation (a "~50-100 pulsars" qualifier wrongly
implying $p_{C_L}<1$; verified via `fig_scaling_Np.py` that $p_{C_L}>1$
at all $N_p$).

## [2026-06-13] integrate | reduced section shown alongside old Secs. VI--VII in main.pdf

Per author preference, `source_vs_cl_reduced.tex` is now `\input` in
`main.tex` immediately after `numerical_estimates.tex`, so the compiled
`main.pdf` shows BOTH the original Sec. VI (`three_strategies`) + VII
(`numerical_estimates`) AND the new reduced Sec. VIII ("The right search:
the source, not its angular power spectrum") for side-by-side comparison.
To avoid label collisions the new section's hierarchy display and figure
use `eq:hierarchy_v2` / `fig:scaling_Np_v2` (its figure reuses the
committed `scaling_Np.pdf`). Full build (`pdflatex; bibtex; pdflatex
×2`) succeeds: 12 pages, exit 0, no duplicate-label or undefined-ref
warnings. Only dangling reference is `\cite{Goncharov:2026joint}` (the
companion draft, intentionally not in `references.bib`). `main.pdf`
regenerated. To switch fully to the reduced version later, delete the
`\input` lines for `three_strategies` and `numerical_estimates` and drop
the `_v2` label suffixes.

## [2026-06-19] notebook | guide_power_anisotropy §10e — joint (p1, C1/C0) + conditional P(p1|C1/C0)

Added subsection **§10e** to `notebooks/guide_power_anisotropy.py` (4 cells +
summary bullet 6), to test the paper's claim (Sec. IV, near Fig. 5) that *a
large $C_1/C_0$ requires a single dominant source* — Fig. 5 only shows the
marginal CDF of $p_1$ and the fraction of the *mean* $\langle C_1/C_0\rangle$
from $p_1^2$, not the conditional behavior. Author-approved design (all 3
plots + model dropdown).

Both quantities are derived per realization from the **same** file
`power_anisotropy_eps{020,038,066}.npz`: $C_1/C_0=$ `cls_all[:,:,1]/cls_all[:,:,0]`
and $p_1=$ `brightest_h2s[:,:,0] / power_maps.sum(axis=2)` (exact: brightest
source $q$ over total power summed over all sources — verified `power_maps`
accumulates every source in `sources.generate_realizations`). The two scripts
share `seed=42` but call different RNG paths (`run_realizations` vs
`generate_realizations`), so population/power rows are NOT row-aligned —
hence both quantities are taken from the single power file.

- **E1** joint hexbin of $(p_1,C_1/C_0)$ (log–log) with the single-source line
  $C_1/C_0=p_1^2$. **E2** conditional PDF+CDF of $p_1$ at $C_1/C_0\in
  \{0.05,0.1,0.2,0.5\}$ (±12% multiplicative slice; $\sqrt{\rm ref}$ guides).
  **E3** median $p_1$ (16–84%) vs reference $C_1/C_0$ at the three Table I
  frequencies (idx 0,3,15) against the $\sqrt{C_1/C_0}$ envelope.
- New UI scoped to §10e (rest of notebook stays fixed at ε=0.66): model
  dropdown + frequency slider + slice-width slider. Heavy `power_maps` read
  isolated in a model-only cell so the sliders stay instant.

Verified numbers (ε=0.66, read-only check on real data): corr$(\log p_1,\log
C_1/C_0)\approx0.83$–0.86; median$[(C_1/C_0)/p_1^2]\approx1.1$–1.3 (so realized
dipole sits just above $p_1^2$); conditional median $p_1\approx0.17$–0.23 at
$C_1/C_0=0.05$, $\approx0.38$–0.42 at $0.2$, $\approx0.66$–0.70 at $0.5$ with
$P(p_1>0.5)\approx0.84$–0.96. eps020 low-freq high-$C_1/C_0$ slices are tiny
(N<5) and gracefully skipped.

HTML re-exported to `results/guide_power_anisotropy.html` (28 s, 0 cell errors,
3.04→3.91 MB). Updated `wiki/notebooks/guide_power_anisotropy.md`. Also
**corrected `wiki/reproducibility.md`**: it claimed HTML exports are "Tracked",
but `results/` is fully gitignored (`.gitignore:5`) so they are untracked —
fixed to give the `marimo export html` rebuild command.

## [2026-06-19] notebook | guide_power_anisotropy §10f — analytic P(p1|C1/C0) inversion

Follow-up to §10e. Author asked whether the paper's *forward* dipole laws
(`distribution_c1c0.tex`, $P(C_1/C_0\mid\{p_a\})$) have an analytic *inverse*
$P(p_1\mid C_1/C_0)$ comparable to the MC conditional. Answer: yes — it is the
Bayesian inverse of the same kernels and additionally needs the population
prior $\pi(p_1)$. Added **§10f** (3 cells: scipy helpers, derivation markdown,
analytic-vs-MC plot; author-approved: notebook overlay, both empirical+flat
priors).

Three nested predictions overlaid on the §10e MC histograms (panel per
reference $C_1/C_0$): (1) delta → $p_1=\sqrt{x}$ (envelope); (2) mean relation
$\langle x\rangle=p_1^2+\eta$ → $p_1=\sqrt{x-\eta}$; (3) noncentral-Maxwell
kernel (Eq. 1src_gauss) read as a function of $p_1$,
$P(p_1\mid x)\propto\pi(p_1)p_1^{-1}e^{-3p_1^2/2\eta}\sinh(3p_1\sqrt{x}/\eta)$,
flat-prior mode $\sqrt{x}-\eta/(3\sqrt{x})$. Prep cell extended to expose
$\eta=\sum_{a\ge2}p_a^2$ from the top-100 ledger; prior via
`scipy.stats.gaussian_kde`; $\bar\eta(p_1)$ from binned ledger medians.

**Verified** (read-only, real data, eps066) that the full posterior
$\pi(p_1)f(x\mid p_1,\bar\eta)$ reproduces the MC conditional median to ~1–2%
at $C_1/C_0\in\{0.05,0.1,0.2,0.5\}$ and at f=0.085 & 1.03/yr (e.g. x=0.5: MC
0.700 vs analytic 0.702; x=0.2: MC 0.415 vs 0.423). Full shapes coincide. The
flat-prior closed form is a few % too broad at small $x$ — the gap is the
astrophysical info in $\pi(p_1)$ (forward law = geometry, inverse = geometry +
population). Scope: notebook only (no paper edit, per author).

HTML re-exported (0 cell errors, 14→15 figures, 3.91→4.21 MB). Updated
`wiki/notebooks/guide_power_anisotropy.md` (finding 7, §10f row) and
`wiki/concepts/dipole_distribution.md` (new "Inverse" section + backlink).

## [2026-06-19] notebook | guide_power_anisotropy §10f rewrite — proper η-marginalization, P(Neff|C1/C0), own controls

Author feedback on §10f: (1) I had plugged in $\bar\eta(p_1)$; should instead
integrate over $P(\eta\mid p_1)$. (2) Also report the effective number of
sources $P(N_{\rm eff}\mid C_1/C_0)$ ("a handful"). (3) §10f reused §10e's
controls (far up the page) — wanted its own dropdown/slider to explore.

Rewrote §10f accordingly:
- **η marginalized properly** via importance sampling: each realization is a
  prior draw $(p_{1,j},\eta_j)$; weighting all realizations by
  $w_j=f(x_0\mid p_{1,j},\eta_j)$ and histogramming $p_{1,j}$ gives the
  posterior with $\eta$ integrated out AND $\pi(p_1)$ included. Dropped the
  KDE+$\bar\eta$ plug-in (and the scipy dependency). F1 overlays: MC slice,
  marg-$\eta$ (red, matches MC), mean-$\eta$ plug-in (orange, ≈red — the
  spread barely matters), flat-prior closed form (blue), $\sqrt{x}$ anchor.
- **F2: $P(N_{\rm eff}\mid C_1/C_0)$**, $N_{\rm eff}=1/(p_1^2+\eta)$. Peaks at
  $1/(C_1/C_0)$ (the $\langle C_1/C_0\rangle=1/N_{\rm eff}$ relation): median
  ~2 at 0.5, ~5 at 0.2, ~10 at 0.1, ~13–22 at 0.05 (capped at high freq). The
  analytic ($\eta$-marginalized) curve tracks the MC.
- **Own controls** (jcf_model dropdown + jcf_freq + jcf_win), matching the
  notebook's per-section idiom. **Light prep**: reads only `cls_all` +
  `brightest_h2s`, recovering total power from the monopole
  $Q=\sqrt{C_0}\,N_{\rm pix}/\sqrt{4\pi}$ — verified to ~0.04% (1–99%:
  [0.975,1.032]) vs the exact pixel sum — so model switching is fast (no 2.7 GB
  power-maps read). §10e prep reverted to not compute the now-unused jc_eta.

Verified on real data (eps066, f=0.085 & 1.03/yr): marg-$\eta$ vs MC medians
e.g. p1@0.5: 0.701 vs 0.700; Neff@0.2: 5.29 vs 5.39; Neff@0.5: 2.03 vs 2.03.
HTML re-exported (0 errors, 15→16 figures, 4.34 MB). Updated notebook summary
(findings 7 marg-η, 8 Neff), `wiki/notebooks/guide_power_anisotropy.md`,
`wiki/concepts/dipole_distribution.md` (Inverse section), and
`wiki/concepts/N_eff.md` (conditional N_eff). Scope: notebook only.

## [2026-06-19] paper+notebook | Sec. IV inverse conditionals, Fig. 2 rewrite, Q consistency

Author-directed batch (paper edits + notebook fix), then independent proofread.

**Q consistency (notebook).** §10e prep now takes total power from the monopole,
$Q=\sqrt{C_0}\,N_{\rm pix}/\sqrt{4\pi}$ — the SAME definition §10f already used
(matches the exact pixel sum to ~0.04%; 1-99%: [0.975,1.032]). §10e no longer
reads the 2.7 GB power_maps array. p1 medians unchanged to 4 decimals. HTML
re-exported (0 errors, 16 figures).

**Section IV (`distribution_c1c0.tex`) — new subsection "The source content of
a given dipole".** Adds the Bayesian inverse of the forward laws:
`eq:p1_given_x` $P(p_1\mid x)\propto\pi(p_1)\int d\eta\,f(x\mid p_1,\eta)
P(\eta\mid p_1)$ with $\langle p_1\mid x\rangle\to\sqrt{x}$, and
`eq:neff_given_x` $\langle N_{\rm eff}\mid x\rangle\simeq 1/x$ (from
`eq:mean_cl`). New figure `fig:p1_neff_conditional` (Fig. 6): $P(p_1\mid
C_1/C_0>0.2)$ and $P(N_{\rm eff}\mid C_1/C_0>0.2)$ for eps=0.66 at the three
Fig. 4 frequencies, MC vs analytic (noncentral-$\chi^2_3$ exceedance weights).
New Table `tab:conditional` (now Table I; percentiles auto-renumber to Table II):
3 models x 3 freqs x thresholds {0.1,0.2,0.5}, columns P(>v), <p1|>v>, <Neff|>v>
(+/-1sigma, conditional on EXCEEDING per author preference; "---" for <20
exceeding). Text: at the lowest (PTA-sensitive) frequency only eps=0.66 reaches
0.2 (P=0.14 vs 0.014 / 0.001 for 0.38 / 0.20); when it does, <p1>=0.61+/-0.17,
<Neff>=3.2+/-1.7. Generators: `paper/scripts/fig_p1_neff_conditional.py`,
`paper/scripts/table_conditional_stats.py` (both new, tracked).

**Fig. 2 (`astrophysical_model.tex`).** New generator
`paper/scripts/fig_strain_spectrum_models.py` (Fig. 2 had no script before).
Each model's spectrum divided by its mean at $f_*=0.1$/yr and x $(f/f_*)^{4/3}$
(gamma=4/3 = -slope of $\langle h_c^2\rangle\propto f^{-4/3}$, verified fitted
-1.33). Means flatten to 1; medians show the divergence (median/mean at f~1:
0.65/0.38/0.18 for eps 0.20/0.38/0.66; eps=0.66 already 0.57 at lowest f).
Caption + "Mean vs median" text updated; notes a spectrum tracking the mean
disfavors high-eps models.

PDF rebuilt: 14 pages, all passes exit 0, new labels resolved, table fits full
width (only pre-existing 31pt overfull in the eq:dcl display, untouched). Only
undefined citation is the intentional `Goncharov:2026joint` placeholder. Wiki:
updated `formulas.md` (2 eqs), `figures/strain_spectrum_models.md`, new
`figures/p1_neff_conditional.md`, `reproducibility.md` (paper-figure
generators), `index.md`. NOTE: `paper/figures/p1_neff_conditional.pdf` and the
3 new `paper/scripts/*.py` are untracked — commit them with the paper changes.

### Proofread (independent agent) + fixes — 2026-06-19

Ran an independent general-purpose agent over the two touched paper sections.
Findings and resolutions:
- **[BLOCKER, fixed]** `astrophysical_model.tex` "Mean versus median" prose
  quoted median/mean = 0.65/0.38/**0.18** at f~1/yr, computed from the *MC
  sample* mean. The figure (correctly) uses the *analytic* mean
  $\langle h_c^2\rangle$, which for the heavy-tailed eps=0.66 model at high f is
  ~2x the under-resolved sample mean. Recomputed median/analytic-mean (interp at
  f=1/yr): **0.61 / 0.39 / 0.09** -> prose corrected; 0.09 is the genuine
  "order of magnitude" drop and now matches the figure caption.
- **[SHOULD-FIX, fixed]** `eq:neff_given_x` inversion: added "inverting to
  leading order" before $\langle N_{\rm eff}\mid x\rangle\simeq 1/x$.
- **[NITPICK, fixed]** Table frequency labels unified to 0.085/0.28/1.0 (matching
  Table II / Fig. 5) in both `tab:conditional` and `table_conditional_stats.py`.
- **[NITPICK, left]** `eq:neff_given_x` is numbered but unreferenced — kept
  numbered as a displayed key result.
- Agent verified: `eq:1src_gauss` is exact (matches scipy ncx2 to 2e-14);
  `tab:conditional` reproduces cell-for-cell from the script; all other in-text
  numbers, notation, and cross-references consistent. PDF rebuilt clean (14 pp).

## [2026-06-22] edit | Section III/IV: matched-normalization + consistency fixes + new quantities

Major revision of Secs. III–IV (paper) and the dependent wiki pages.

**R4 — amplitude calibration.** New helper `gwb_sources.population.calibrate_phi_sigma`
rescales $\phi_\sigma$ per model so $\sqrt{\langle h_c^2\rangle(1\,{\rm yr}^{-1})}
= 2.5\times10^{-15}$ for all three $\varepsilon$ (linear in $\phi_\sigma$; exact).
Factors $\kappa$ = 13.26 / 6.14 / 0.72 for $\varepsilon=0.20/0.38/0.66$. Both
`run_*.py` take `--target-hc` (default 2.5e-15) / `--no-match`; npz now stores
`kappa`, `target_hc`, `phi_sigma`. **All population + power results regenerated.**
Consequence: low-$\varepsilon$ models become much less anisotropic (6–13$\times$
more sources). NOTE: user target 2.5e-15; refs (2406.17010) use 2.4e-15.

**R2/R3 — consistency + universality.** Verified anafast $C_1/C_0$ == random-walk
$|\mathbf S|^2$ (to ~1% pixelization), and ledger $p_1$ == population-path $p_1$.
Fixed the $N_{\rm eff}$ definition: the old `c1c0_neff_vs_freq` plotted
$C_0/C_1$ (dipole estimator, inflated mean) while its caption claimed
$1/\sum p_a^2$; now uses the ledger $N_{\rm eff}=1/(p_1^2+\eta)$ like Table I.
Confirmed universality: conditional $\langle p_1\mid x{>}v\rangle$,
$\langle N_{\rm eff}\rangle$, $\langle\eta\rangle$ set by the threshold, not the
model/freq; explained via the forward-law survival function.

**R1 — Sec IV.F clarified.** Eq. `eq:p1_given_x` rewritten (survival function;
$\pi(p_1)$, $P(\eta\mid p_1)$ from Monte Carlo; importance reweighting), removed
the "exceedance probability of a noncentral law" gibberish, added tested simple
estimators `eq:p1_given_x_simple` ($\sqrt{x}$) + `eq:neff_given_x` ($1/x$).

**R5/R6 — new quantities.** Defined $R=h^2_{s,\max}/\langle h_c^2\rangle$
(`eq:R_ratio`, Table II `tab:source_ratio`) and the $h_s^2=h_0^2 f T_{\rm obs}$
relation to NANOGrav's CW limit ($h_0\approx10^{-14}$); only $\varepsilon=0.66$
reaches it. New figures `source_content_estimators.pdf` (Fig. 6, $\sqrt{x}$/$1/x$
+ universality) and `pixel_amplitude_h0.pdf` (Fig. 8).

**R7/R8.** Sec III.C rewritten (HEALPix nside=8, ledger, individual/bulk
threshold, RNG; cites 2406.17010). Fig. 2 now the raw $h_c^2(f)$ (means coincide
= normalization check); median/mean 0.80/0.54/0.078 at 1/yr.

New `paper/scripts` generators (close prior gap where Figs. 1/3/4 lived only in
notebooks): `fig_c1c0_neff_vs_freq.py`, `fig_c1c0_distribution.py`,
`fig_source_content_estimators.py`, `fig_pixel_amplitude.py`,
`table_percentiles.py`; `table_conditional_stats.py` extended (+$\eta$, +$R$).
Table renumbering: `tab:conditional`=I, `tab:source_ratio`=II,
`tab:percentiles`=III. PDF rebuilt clean (16 pp).

Wiki updated: `reproducibility.md` (calibration + new generators/figures),
`formulas.md` (revised `eq:p1_given_x`, new `eq:p1_given_x_simple`/`eq:hc_sum`/
`eq:R_ratio`, $h_0$ relation), `concepts/N_eff.md` (ledger-vs-estimator),
`concepts/brightest_source_fraction.md` ($R$ + universality), figure pages
(`strain_spectrum_models`, `c1c0_neff_vs_freq`, `p1_neff_conditional` + new
`source_content_estimators`, `pixel_amplitude_h0`), `index.md`.

OPEN (verify-reference before bib edit): HEALPix (Górski 2005, astro-ph/0409513),
healpy (Zonca 2019, JOSS 4, 1298), NANOGrav individual-source (2306.16222,
Agazie 2023) — cited by name in the text but not yet in `references.bib`;
`Goncharov:2026joint` still undefined (unpublished draft). `results/*_oldphi.npz`
are disposable backups of the pre-calibration data (reproduce via `--no-match`).

## [2026-06-23] paper rewrite | Sec. VI detection strategies recast; old VI–VIII → appendices

Recast the detection-strategy discussion. The author found the former Secs. VI–VIII
(the $p,p^2,p^4$ "three rival methods" framing culminating in "$C_\ell$ threshold
$>1$, not viable") confusing and the conclusion misleading. New main section
`paper/sections/source_detection.tex` (**Sec. VI**) frames detectability via the
background SNR $\rho_0\equiv\Sigma_{\rm bg}$, the brightest-source fraction $p_1$
(Sec. IV), and the array's angular resolution $L$. The three old files
(`three_strategies`, `numerical_estimates`, `source_vs_cl_reduced`) are moved
**verbatim** to Appendices A–C (kept for now, to be removed once the new treatment
settles); `appendix_fisher` is App. D. Abstract and Discussion item 4 revised to
match.

**Corrected scientific conclusion.** A coherent search for the source (equivalently,
the source as a covariance excess — same test by Neyman–Pearson monotone
equivalence) is the right tool: $\rho_{\rm ps}=\alpha_{\rm ps}p_1\rho_0$,
$\alpha_{\rm ps}=\sqrt5\simeq2.24$. The angular power spectrum is **never the best
tool but not catastrophic**: at the low resolution PTAs have, the required-amplitude
penalty of a one-parameter Poisson $C_\ell$ statistic vs an unknown-direction
coherent scan is only 1.1–1.4× over $L=1$–6 (**exactly 1 at $L=1$**, where the scan
max $=\sqrt{C_1}$), growing slowly with $L$. The earlier "catastrophic" verdict
conflated this *detection* question with the *estimation* ($\sigma_p\sim5$–10×,
$p^4$-scaling) question — reconciled on [[concepts/fisher_hierarchy]].

**Verification (no eyeballing).** New package module
`gwb_sources/source_detection.py` (+`tests/test_source_detection.py`, 7 tests);
all 20 repo tests pass. `paper/scripts/verify_source_vs_cl.py` runs 28 independent
checks (analytic integrals $\langle\gamma_s^2\rangle=1/18$,
$\langle\Gamma_0^2\rangle=1/108$ → $\alpha_{\rm ps}^2=5$; the real `z_plus`/`z_cross`
patterns sky-average to $\tfrac23$ HD; $\alpha_{\rm ps}^2=\sum s_L\to5$; the Sec. 9.4
threshold table to $<1\%$; honest max-over-sky MC; NP equivalence to machine
precision). New figures `source_snr_vs_resolution.pdf`, `cl_vs_scan_penalty.pdf`
(generators on the fly, no `results/*.npz`); Table IV via `table_detection_thresholds.py`.

**Wiki.** New `sources/pta_point_source_multipole` (canonical, with the
detection-vs-estimation reconciliation), `code/gwb_sources_source_detection`, figure
pages; updated `concepts/fisher_hierarchy` (new "Detection vs estimation" section),
`concepts/matched_filter_vs_power`, `formulas`, `index`, `reproducibility`.

PDF rebuilds clean (19 pp); only `Goncharov:2026joint` remains undefined (unpublished
companion — cannot pass `verify-reference`; renders as `[?]`, pre-existing).

## [2026-06-24] review | author review round: shared figure style + per-section fixes

Incorporated a round of author review comments on the paper.

**Figures.** New shared style module `paper/scripts/_paperstyle.py` (untracked):
`apply_style()` (serif + cm mathtext, base font 9, ticks in + minor, grid alpha
.25, frameless legends, savefig dpi 300, `lines.linewidth` 1.5), `figsize_1col(h)`
=(3.40,h) / `figsize_2col(h)`=(7.06,h), and shared palettes `EPS_COLORS`
{0.20:blue, 0.38:orange, 0.66:green}, `EPS_MODELS`, `METHOD_COLORS`
{scan:blue, cl:red, ps:black}, `STRATEGY_COLORS`, `FREQ_STYLES`, `LW`
{primary 1.5, secondary 1.2, reference 1.0}, `MS`, `CAPSIZE`. All 11 paper figure
scripts now import it for a consistent paper-grade look.

**Fig. 4 (`c1c0_distribution`).** Y-axis back to LOG (the version used in the
paper); `fig_c1c0_distribution.py` now also emits a linear alternative
`paper/figures/c1c0_distribution_linear.pdf` (untracked).

**Fig. 8 (`pixel_amplitude`).** NANOGrav CW upper limit corrected from a flat
$h_0=10^{-14}$ to the verified deepest value $h_0=8\times10^{-15}$ near 6 nHz
(Agazie et al. 2023, ApJL 951 L50, arXiv:2306.16222), marked with a star;
caption now states the true limit is frequency-dependent and weaker (higher)
elsewhere, and relabels this as the *deepest* limit.

**`astrophysical_model.tex`.** Stated the $h_s^2$ averaging assumptions: new
`eq:hs2_single`, $h_s^2 \propto (GM)^{10/3}\eta^2(1+z)^{4/3}/\chi^2
f^{4/3}\,(f/\Delta f)$ with $\eta=q/(1+q)^2$ — inclination and polarization
averaged, distance enters via $(1+z)/\chi$, and within each $(f,M)$ bin $z,q$ are
integrated to one representative strain (no intra-bin distance scatter). Removed
the "independent strike" phrase, trimmed the ledger/RNG implementation detail,
and fixed "because we now hold the mean".

**`distribution_c1c0.tex`.** Moved the "large $C_1/C_0$ iff one source
dominates" claim to *after* the inverse-problem section where it is actually
shown; noted Fig. 6 pools all frequencies (the relation is universal across model
AND frequency).

**`nanograv_prior.tex`.** Added a "What this does and does not imply" paragraph:
the models that look ruled out are not (it is the prior); the $C_\ell$ search is
$\sim$ the source search; the spectrum shape already constrains them.

**`source_detection.tex`.** Full pedagogical self-contained rewrite — removed all
appendix references and the word "honest", added the data-model / covariance
setup, derived $\alpha_{\rm ps}=\sqrt5$, anchored the present-day per-bin
$\rho_0\sim1$ (total NG15 HD optimal-statistic SNR ~5 over ~5 bins) with
$\rho_0=20$ relabeled as a future benchmark, clarified the Fig. 11
analytic-vs-MC penalty difference, and corrected the Goncharov detection
probabilities to 2% (15 yr) / 5% (20 yr) with the IPTA simulated-data caveat
(real-data result verified essentially identical); 21 of 114 AGN candidates in
tension. (These supersede the draft-era 0.6%/2% and 24/114.)

**References.** Added `@misc{Goncharov:2026joint}` (arXiv:2606.18241) to
`paper/references.bib` (companion CW+GWB joint search); it no longer renders as
`[?]`.

Paper rebuilds clean at 22 pages.

## [2026-06-24] wiki | figure pages synced to the review-round changes

Updated three `wiki/figures/` pages to match the 2026-06-24 figure changes:

- **`c1c0_distribution.md`** — y-axis is now LOG (the long tail to large
  $C_1/C_0$ is only visible in log; this is the paper version); noted the
  linear alternative `c1c0_distribution_linear.pdf` written by the same script;
  generator switched to the standalone `paper/scripts/fig_c1c0_distribution.py`
  (uses calibrated `phi_sigma`, imports `_paperstyle`).
- **`pixel_amplitude_h0.md`** — dashed line changed from flat $h_0=10^{-14}$ to
  the deepest NANOGrav 15-yr CW 95% UL $h_0=8\times10^{-15}$ near 6 nHz (star),
  with the true limit noted as frequency-dependent and weaker elsewhere;
  citations resolved (`NANOGrav:2023individual` = 2306.16222 for the UL;
  `Goncharov:2026joint` = 2606.18241 for the reference figure) — both now in
  `references.bib`, so the old "unpublished / not yet in bib" caveats removed.
- **`source_content_estimators.md`** — made explicit that Fig. 6 pools all
  realizations of all three models at ALL frequencies (`ravel()` over the full
  `(Nreal, Nfreq)` grid), so the $\sqrt{x}$ / $1/x$ relations are universal
  across model AND frequency.

All three Generator sections now note the shared `paper/scripts/_paperstyle.py`.

## [2026-07-13] code | sampled-property Monte Carlo sidecar

Added `new_montecarlos_codex/` as a separate workflow for testing replacement
Monte Carlos without changing the current `gwb_sources.sources` production path
or the existing `results/` files.  The sidecar samples per-source redshift,
mass ratio, and inclination while keeping the same Poisson counts
`N_jk ~ Poisson(N_bin[j,k])`.  The redshift and mass-ratio distributions are
the same finite Sato-Polito quadrature weights used inside
`luminosity_function`; the inclination multiplier is normalized to unit mean, so
the analytic sampled source-power grid matches the legacy `h2s(f,M)` grid at
machine precision.

Files added:

- `new_montecarlos_codex/README.md` — exact distribution contract and commands.
- `new_montecarlos_codex/sampled_montecarlo.py` — sampler, old/new `p_1`
  realization helpers, and sampled power-map generation.
- `new_montecarlos_codex/run_quick_comparison.py` — quick old-vs-new `p_1`
  triage report.
- `new_montecarlos_codex/run_new_population_analysis.py` and
  `run_new_power_anisotropy.py` — local production-style outputs under
  `new_montecarlos_codex/results/`.
- `tests/test_new_montecarlos_codex.py` — distribution normalization,
  inclination-moment, mean-grid, and shape tests.

Quick run (`Nrel=2000`, thresholds 2000, freqs 0/3/15) wrote
`new_montecarlos_codex/reports/quick_p1_comparison.md`.  Main result: sampled
brightness raises `p_1` most for the low- and mid-scatter models.  Median
`p_1` ratios new/old are about 2.5, 1.7, 1.25 for `eps020` at
`f=0.085,0.278,1.029/yr`; about 1.6, 1.4, 1.2 for `eps038`; and about 1.15,
1.10, 1.02 for `eps066`.  A threshold-5000 sensitivity run for `eps020` and
`eps038` gives consistent shifts.  Focused tests pass with
`conda run -n gw_pta pytest tests/test_new_montecarlos_codex.py`.

## [2026-07-14] results | corrected sampled-property production comparison

Generated full sampled-property sidecar results under
`new_montecarlos_codex/results/` for all three epsilon models:

- `sampled_population_analysis_eps{020,038,066}.npz`: 10k realizations,
  `total_strain (10000,44)`, `brightest_n_strains (10000,44,20)`.
- `sampled_power_anisotropy_eps{020,038,066}.npz`: 10k realizations,
  `power_maps (10000,44,768)`, `brightest_h2s (10000,44,100)`,
  `cls_all (10000,44,24)`, and exclusion spectra.

Important correction during production: the first attempted power files used
`bulk_pixel_mode=moment`, which drew per-pixel Gaussian bulk fluctuations and
clipped negatives to zero.  That biased the bulk map power high and suppressed
power-ledger `p_1`.  Those files were overwritten.  Corrected power files use
`bulk_pixel_mode=mean`, which conserves aggregate bulk map power; population
files still use `bulk_total_mode=moment` for 1-D total-strain variance.

Rendered old-vs-new figures/tables to
`new_montecarlos_codex/comparison_old_vs_new.html`, with paired PNG/PDF figures
under `new_montecarlos_codex/figures/{old,new}/` and table text under
`new_montecarlos_codex/tables/`.  Sanity checks:

- sampled analytic mean vs legacy `h2s(f,M)` agrees at max relative
  `~6e-16` for all models;
- `h2c_vs_f` is unchanged relative to the old files;
- map-sum vs monopole-derived total has median relative mismatch
  `0.17%`, `0.22%`, `0.28%` for eps 0.20/0.38/0.66 and 99th-percentile
  mismatch below `4.3%`.

Main old-vs-new result after correction: sampled source properties raise both
`p_1` and `C_1/C_0`, with the largest changes at low epsilon.  Population-file
median `p_1` ratios new/old at `f=0.085,0.28,1.0 yr^-1` are approximately
`2.40, 1.64, 1.29` for eps 0.20; `1.58, 1.27, 1.11` for eps 0.38; and
`1.11, 1.09, 1.03` for eps 0.66.  `C_1/C_0` median ratios from the power files
are similarly above one, especially for eps 0.20/0.38.

Adversarial subagent review found no blocking artifact issues.  Nonblocking
risk retained in the report: threshold-500 exact ledgers omit possible
brightest sources from aggregate bulk bins, so the threshold-convergence reports
(`threshold100`, `threshold500`, `threshold5000`, plus the initial threshold
2000 quick report) should remain attached to any scientific interpretation.

## [2026-07-14] review | adversarial findings incorporated; writer handoff ready

Closed the significant missing-artifact finding from
`new_montecarlos_codex/reports/adversarial_review.md`. Added
`sampled_c1c0_walk_realizations` and
`generate_sampled_c1c0_distribution.py`, producing the like-for-like sampled
3D-random-walk candidate
`figures/new/c1c0_distribution_3d_walk.pdf` plus a compact reproducibility
cache/report. This replaces the invalid assumption that the HEALPix `anafast`
comparison panel could stand in for the paper's direct 3D walk. At epsilon 0.66
and 0.085/yr the sampled walk has median $C_1/C_0=0.0494$ and median
$N_{\rm eff}=18.98$. The current caption's "peak 0.04" is the old median, not
the density mode; writer guidance now says "median near 0.05."

Added `run_threshold_sweep.py` and
`reports/threshold_convergence_fixed.md`: all thresholds now use the same
`Nrel=2000`, seed 42, epsilon set, and frequency set. Threshold 500 is
conservative and usually within about 6% of threshold 5000 in the median; the
largest deficit is epsilon 0.20 at 0.085/yr (9% median, 17% at the 95th
percentile).

Added `generate_writer_handoff.py`, which writes the authoritative
`reports/writer_handoff.md`, full uncertainty-bearing LaTeX rows for Tables
I--II, and sampled percentile rows for Table III. It also computes all inline
strain ratios and Fig. 5 dominance fractions. Added the canonical wiki page
[[results/sampled_property_monte_carlo]], updated Fig. 4/reproducibility/index/
TODO pages, and documented that the root `results/` ignore rule already covers
the roughly 10 GB sidecar arrays. Focused sidecar tests pass 5/5.

## [2026-07-14] paper | paper_v2: restructured draft on the sampled Monte Carlos

Created `paper_v2/` — a complete rewrite of the paper (writer pass requested by
MZ), leaving `paper/` untouched for side-by-side adversarial review.

**Data switch.** All Monte-Carlo-driven artifacts now consume
`new_montecarlos_codex/results/sampled_*.npz` per
`new_montecarlos_codex/reports/writer_handoff.md`: seven NPZ figure scripts
copied to `paper_v2/scripts/` and repointed; Fig. 4 replaced by the sampled 3D
walk `c1c0_distribution_3d_walk.pdf`; Tables I–III regenerated from the
repointed `table_percentiles.py`/`table_conditional_stats.py` and verified
identical to `new_montecarlos_codex/tables/new_*_latex.txt`. Inline numbers
recomputed from the npz (no eyeballing): median/mean strain 0.99/0.93/0.46 at
0.085/yr and 0.67/0.41/0.05 at 1.03/yr (eps 0.20/0.38/0.66); eps066 ledger
median N_eff 19.3 → 5.2 across the band, median C1/C0 0.049 → 0.190; p1
dominance 0.66/0.71/0.77; conditional-table survivors at C1/C0>0.2:
<p1>=0.60±0.18, <N_eff>=3.2±1.9 with P=0.183/0.020/0.002 at the lowest
frequency.

**Restructure.** New logic (MZ 2026-07-14): high dipole ⇒ one bright source
(Sec. IV, forward+inverse) ⇒ the source is undetectable at current sensitivity
in every model (Sec. IV brightest-absolute + Sec. V, ρ_ps=√5 p1 ρ0 anchored to
the NANOGrav total cross-correlation SNR≈5, Goncharov 2%/5% forecasts) ⇒ the
published C_l bound can only be, and numerically is, the sqrt-SH prior
(Sec. VI, now AFTER the detection argument — the "missing link" made explicit)
⇒ the constraining observable today is the spectrum shape/median-vs-mean
(Sec. III + Discussion, quoting SatoPolito:2025dist: ~10× more BHs than local
estimates, M_peak ≲ 1e10 M_sun at 2σ). Former appendices (three_strategies,
numerical_estimates, source_vs_cl_reduced, appendix_fisher) and the
scaling_Np figure DROPPED; the p/p²/p⁴ KL hierarchy survives as one paragraph
in Sec. V ("estimation vs detection"). Author order now Sato-Polito,
Zaldarriaga (matching precursor papers).

**Verification.** Clean pdflatex+bibtex compile (16 pp, no unresolved
refs/citations); `verify_source_vs_cl.py` rerun; `tests/test_source_detection.py`
7/7; Fig. 4 overlays visually confirmed against caption. Provenance:
`paper_v2/README.md` (per-artifact map) + new [[reproducibility]] entries.

## [2026-07-14] review | adversarial referee report on paper_v2

Full adversarial review of `paper_v2/` per MZ's five-point charge; report
filed at [[reviews/paper_v2_adversarial_review]]. Methods: full tex read;
all 11 figure PDFs rendered and checked against captions; tables verified
digit-for-digit vs `out_table_*.txt`; all cite keys and `\fromnotebook`
targets checked; `verify_source_vs_cl.py` + `test_source_detection.py`
re-run (7/7); every inline number traced (three parallel audit agents);
style calibrated on the tex of 2312.06756 and 2406.17010.

Headline findings: (1) provenance blockers — `paper_v2/` and
`new_montecarlos_codex/` untracked in git; `mass_function_kernel.pdf` has
no regenerating command (named notebook has no savefig); Table I prior
row misattributed to `table_percentiles.py`; "point-source ≳5% at
rho0=20" printed by no script; NG15 cross-corr SNR≈5 has no repo
provenance page. (2) Correctness — Gamma_0 carries two normalizations in
Sec. V (Eq. 10 gives <Gamma_0^2>=1/48, text quotes 1/108 from the
1/3-normalized note convention; alpha_ps^2=5 itself is fine); M_peak
inequality direction flips between abstract/intro/astro and discussion;
abstract overstates the CW-limit comparison; "10^4 prior realizations"
is actually 50,000; f=1.0 labels describe the 1.029/yr bin (Table III
caption A=2.5e-15 vs true 2.45e-15). (3) Figures — Fig. 1 breaks
EPS_COLORS (0.66=red); Fig. 7 suptitle/caption (solid=MC, dashed=analytic)
contradicts its own legend (linestyles=frequencies); Fig. 10 legend says
"honest sky scan" (forbidden label) and undefined "Poisson C_l"/"K_eff";
Fig. 8 caption "lie below throughout" contradicted by scatter dots;
Fig. 11 plots four thresholds, text discusses one. (4) Style — register
mismatch vs SP&Z: repeated punchlines, ~11 scare-quoted "constraints",
hedging collapse, 81 em-dashes, 49 \emph, \boxed eq, "Bottom line"
heading, metaphors; structural skeleton matches well. No paper files
edited; report is the deliverable.

## [2026-07-14] write | adversarial-review fixes incorporated into paper_v2

Acting on [[reviews/paper_v2_adversarial_review]] (all top-10 actions except
the git commit, which is left for MZ to review):

**Correctness.** Gamma_0 normalization unified in Sec. V: Eq. (HD) now uses
the 1/3-normalized curve Γ₀ = 1/3 − x/6 + x ln x (verified by direct
integration: <Γ₀²> = 1/108; the source-direction average of γ_ab equals Γ₀
exactly in this normalization, checked by MC), the conventional HD curve
noted as (3/2)Γ₀, and the never-used uniform-array Σ_bg closed form (the
1/48 line) dropped. M_peak inequality unified to "disfavors M_peak ≳ 1e10"
everywhere. Abstract CW sentence now carries the eps066-tail qualification.
"posterior equals the prior" scoped to the lowest five bins + cite (verified
against references/2306.16221 main.tex line 311). "~40% by L=6" → 38%
(analytic ratio 1.378); Sec. VI prior match now cites NANOGrav's quoted
broadband number (C_{l>0}/C_0 < 20%) instead of their Figure 1. 10^4 → 5e4
prior realizations. NP-equivalence MC claim anchored to verify script item 5.

**Provenance.** New standalone `paper_v2/scripts/fig_mass_function_kernel.py`
(fixes unregenerable Fig. 1 + its EPS_COLORS violation; left panel now drawn
at the calibrated per-model phi_sigma, `--fiducial` reproduces the legacy
content — surfaced to MZ). `table_percentiles.py` now computes the sqrt-SH
prior row itself (0.0087/0.0654/0.200 from the 50k-sample lmax3 npz);
caption attribution fixed. `run_sqrtSH_realizations.py` gained
--lmax-blm/--lmax-cl/--nrel/--suffix, making `sqrtSH_realizations_lmax3.npz`
reproducible (4k-sample check reproduces 0.0087/0.0654/0.200).
`verify_source_vs_cl.py` item 6 now prints the p1 thresholds at rho0=20
under stated K=L(L+2) beam-trials assumptions: dipole-only 0.164, L≤2 scan
0.089, full point source (K=48) 0.069 — the paper now quotes ≳16%/9%/7% and
the Discussion attribution to Fig. 10 is fixed. MC penalties 1.08/1.14
attributed to the figure script's seeds (verify item 4 cross-checks with
different seeds: 1.074/1.147). Orphan `table_detection_thresholds.py` + out
file deleted. New numbers-and-data paragraph in Sec. III: T_obs = 16.03 yr,
Δf = 1/T_obs, 44 bins to 9e-8 Hz, representative centers 0.085/0.28/1.03
per-yr, 10^4 realizations; "f = 1.0" labels → 1.03 in tables and prose;
Table III caption A = 2.45e-15 at the 1.03/yr bin. anafast-vs-walk agreement
quantified (percentiles ≤3%). rho0≈5 provenance ingested:
[[sources/arxiv_2306_16213]] (noise-marginalized optimal-statistic HD S/N,
5±1 varied-γ, Sec. 4/Fig. 4 of 2306.16213; verified via arxiv + ar5iv).
Stale ~6600 on [[figures/c1c0_neff_vs_freq]] superseded (1.81e3 sampled).
README.md rewritten: stdout-redirect step, sqrt-SH commands, threshold
numbers, eps020 p1²/Σp² medians (0.495/0.54/0.64).

**Figures.** All regenerated. Fig. 1 under _paperstyle (0.66 = green).
Fig. 7 encoding made decodable: legend now carries dark=MC / light=analytic
proxies; wrong "(solid: MC, dashed: analytic)" suptitle removed. Fig. 10
legends: "Monte Carlo (full-sky scan)" (forbidden label removed), undefined
"Poisson C_l"/"K_eff" renamed, scare-quoted in-figure "limit" removed.
In-plot claim titles stripped across all figures (reference-paper style);
panel identifiers (eps labels, frequencies) kept. Fig. 4 regenerated via new
`--replot` mode (suptitle stripped, panel label 0.085 not 0.09);
`fig_p1_distributions.py` made cwd-independent; docstring paths repointed.

**Style pass (review Sec. D).** Abstract 326→~290 words, hedged, findings
arc. Single intro roadmap (First/Second/Third/Fourth scaffold folded into
prose). Scare quotes around NANOGrav results removed (~11 → 0; only coined
``background'' remains). \boxed removed, \paragraph removed, \eqref → Eq.~\ref,
Fig./Figure per position, em-dashes 81 → ~4 (table placeholders), \emph 49 → 5.
Claim-as-title headings → neutral ("The source content of the dipole", "The
published C_l upper limits and the analysis prior", "Equivalence of the
coherent and covariance searches", "Comparison with the angular power
spectrum", "Implications"). Punchlines cut to one full statement + recalls.
Sec. III.D shrunk (constraint discussion lives in Discussion); real Fig. 3
paragraph added; per-bin 5/√5≈2 bookkeeping sentence; sqrt-SH
amplitude-independence stated before use; monotone-equivalence why-sentence.

**Verification.** Clean pdflatex+bibtex (16 pp, no undefined refs);
tests/test_source_detection.py 7/7; tables re-emitted and pasted digits
match out_table_*.txt.

**NOT done (blocker A1, MZ's call).** `paper_v2/`, `new_montecarlos_codex/`,
and tests remain untracked; committing is deferred to MZ per "I will read
the paper and decide how to proceed."

## 2026-07-15 — MZ review pass on paper_v2 + DESI-w0wa provenance scheme

**MZ feedback (chat) applied to `paper_v2/`.**
1. Covariance-search equivalence removed as not load-bearing: Sec. V
   subsection "Equivalence of the coherent and covariance searches"
   (T* = max(s-1-ln s, 0) argument) deleted; intro sentence reduced to
   "the optimal search has significance rho_ps = sqrt(5) p1 rho0". The
   machinery survives in `gwb_sources/source_detection.py`
   (`single_template_equivalence`), `verify_source_vs_cl.py` item 5 and
   the unit tests — only the paper text dropped it. Abstract/discussion
   never mentioned it; no dangling \ref.
2. "This scatter compounds the spread…" sentence (Sec. III.C) rewritten
   self-contained: the 2.4x/1.6x/1.1x sampled-vs-legacy p1 factors
   referenced the old Monte Carlos, which the v2 reader never sees.
3. Acknowledgments added (revtex `acknowledgments` env in `main.tex`):
   "done entirely using Claude Code and Codex", NSF-BSF 2207583,
   NSF 2209991, Nelson Center, Simons SFI-MPS-BH-00012593-10.

**Provenance layer moved into toggleable LaTeX (MZ: nothing incorporated
in the running text).** New `paper_v2/paperclaims.sty` adapted from
`../DESI-w0wa/paper/paperclaims.sty`: options `[draft]`/`[final]`;
DESI-compatible `\claim`/`\evidence`/`\depends`/`\dataref` plus
project-specific `\fromnotebook`/`\provnote`/`\genby`/`\todo` (all
`\DeclareRobustCommand` — plain `\newcommand` versions blow up inside
captions via `\protected@edef`). All 13 caption "Generated by …"
mentions → `\genby{}`; the Sec. V verify-script sentence and the Sec. VI
prior-sampling parenthetical → `\provnote{}`; ~30 headline inline
numbers annotated with `\dataref{key}{value}`. `[final]` build verified:
0 errors, pdftotext shows no `.py`, no `[From:`, no `Generated by`.

**DESI-w0wa scheme adapted (MZ: everything needed for the future GitHub
release must live in `paper_v2/`).**
- `structure/claims.yaml` (thesis + 11 claims with evidence data_refs
  and depends_on), `structure/figures.yaml` (14 figures/tables →
  scripts → inputs), `structure/scripts.yaml` (producers, sole writer,
  figure/table/verify scripts with commands).
- `data/paper_numbers.json` (82 keys), sole-written by new
  `scripts/compute_paper_numbers.py`; values cross-checked against the
  2026-07-14 verification audit — all match (alpha_1 = 0.646 and the
  29% dipole fraction require the fig-script ensemble mean over seeds
  100–107, not a single seed; p1²/Σp² must use the population-npz
  20-source ledger like `fig_p1_distributions.py`, not the power-npz
  100-source ledger).
- `scripts/check_provenance.py` (release gate): data_refs resolve as
  repo paths or bib keys, number keys resolve, figure sources/PDFs
  exist, `\genby`/`\fromnotebook` paths exist, `\dataref` keys resolve.
  Passes.
- `RELEASE.md`: full assembly recipe (allowlist + flattening map, what
  never ships — `references/*.md` notes, wiki, reports —, ~10 GB npz
  policy, `reproduce.sh` pipeline, post-flight checklist). Key rule
  copied from DESI: provenance may only point to shipped artifacts;
  internal notes are extracted into the paper text, never released.
- `README.md` updated ("Provenance scheme" section; inline-number list
  replaced by pointer to `paper_numbers.json`).

**Verification.** `check_provenance.py`: all checks pass. Draft and
final builds: 0 errors. Acknowledgments render before References.
`wiki/reproducibility.md` manifest extended (paper_numbers.json +
scheme source files).

**Committed and pushed (2026-07-15, per MZ).** Overfull-column fix for
the annotation tags (`\pc@breakid`: breakpoint after every character in
detokenized ids; `\allowbreak` around each inline tag; 0 overfull
hboxes in the draft build, final build still clean). Everything then
committed as 33b8b1e on `ingest-source-vs-cl-rewrite`, pushed, and
`main` fast-forwarded and pushed to
github.com/matiaszaldarriaga/PTA_Anisotropy for sharing with
Sato-Polito. The ~10 GB `new_montecarlos_codex/results/` stays ignored
(covered by the `results/` gitignore pattern); `paper_v2` LaTeX aux
files and `temp/` added to `.gitignore`. This resolves the 2026-07-14
"NOT done (blocker A1)" item.

## [2026-08-03] audit | dependency rot found while cataloguing for the arg-GW course

External read-only pass over this repo from `teaching/arg-GW`, to mine it for
graduate-course exercises. Catalogue written there
(`wiki/references/pta-code-repos.md`); nothing in this repo was changed except
`wiki/todo.md` and this entry. Three findings, each verified by execution:

1. `gwb_sources/source_detection.py:39` imports `scipy.special.sph_harm`,
   deprecated at SciPy 1.15 and removed at 1.17. `environment.yml` pins numpy
   and healpy but **leaves scipy unpinned**, so a fresh `conda env create` in
   2026 fails to import the detection-theory module. The replacement
   `sph_harm_y(l, m, theta, phi)` has transposed arguments relative to
   `sph_harm(m, l, phi, theta)`, so a careless fix yields silently wrong
   `alpha_L` — and no test pins it.
2. `scripts/run_sqrtSH_realizations.py:61` passes `verbose=False` to
   `hp.alm2map`: warns on healpy 1.16, TypeError on newer.
3. Documentation drift: README says 13 tests (there are 25); reproducibility.md
   says results/ is ~20 GB (33 GB); formulas.md carries the v1 HD normalisation
   while paper_v2 uses 2/3 of it; index.md has the Goncharov companion at
   0.6%/2% and 24/114 where paper_v2 says 2%/5% and 21/114.

Verified working: 25/25 tests pass in 103 s; `alpha_ps_analytic` returns
5.0000001; the L=2 scan-vs-Cl Monte Carlo gives 1.086 against the paper's 1.08;
`single_template_equivalence` gives P_det = 0.70458 for both tests at rho=2.5;
and a 500-draw rerun of the sqrt-SH prior reproduces the stored percentiles
(0.010/0.062/0.193 vs 0.0087/0.0654/0.2005).

Noted for the course, not a defect here: `paper/` and `paper_v2/` make
materially different central claims (v1's p/p^2/p^4 KL hierarchy vs v2's 8-14%
detection penalty with the steep scaling reframed as an *estimation* penalty),
and nothing outside this log marks which is canonical. Anyone teaching from the
repo has to be told which to read.

## [2026-08-11] ingest | arxiv 2608.09929 — Lin, Lidz & Ma post a Monte Carlo sequel to our critique target

MZ flagged a new preprint. Fetched the tex tree, ingested it, and compared it
number for number against `paper_v2`.

**What it is.** Lin, Lidz & Ma (same three authors as 2602.16808) replace the
ensemble-mean shot-noise estimate of that paper with Monte Carlo realization
PDFs: $7\times10^5$ Poisson draws per frequency over $(M_{\rm BH},q,z)$ cells,
fiducial LM24, alternate SZQ. Canonical page: [[sources/arxiv_2608_09929]].

**The result that matters to us.** Their per-realization statistic
$\hat C_{\rm shot}/(4\pi) = \hat h_c^4/(\hat h_c^2)^2 = \sum_i N_i w_i^2$ is
algebraically **our ledger $\sum_a p_a^2 = 1/N_{\rm eff}$**, and they read it
that way. So their Fig. 2 (bottom) and our `fig:c1c0_freq` (right) plot the same
object and can be compared directly. Five things changed from 2602.16808:
the $\langle h^4\rangle/\langle h^2\rangle^2$ estimate is retracted in the
low-source regime (2.8$\times$ high at $f=0.1/{\rm yr}$, 130$\times$ at
$1/{\rm yr}$); the $f^{8/3}$ scaling is superseded by $f^{1.1-1.2}$; a hard
ceiling $\hat C_{\rm shot}/4\pi \le 1$ is derived; $N_{\rm eff}$ moves from the
ensemble ratio to the realized $1/\sum_a p_a^2$ (our definition, resolving a
caveat we had carried since 2026-04-13); and the detection claim softens from
"comparable to, or exceed" the NANOGrav bound to a median 67$\times$ below it at
3 nHz, 4$\times$ at 30 nHz. **Not changed:** they still benchmark against the
NANOGrav $C_\ell$ bound (one unelaborated hedge about priors), and they still
never compare $C_\ell$ against a coherent source search.

**Consequence for the draft.** `paper_v2/sections/discussion.tex:58-63` qualifies
them "in three ways", the second being the mean-vs-median point. That is now
their own published result, stated more strongly than we state it. Posting
unchanged would criticise them for something they corrected three weeks before
us. Rewrite drafted (action A1 in the report).

**Numbers computed, not eyeballed.** Two new tracked scripts,
`scripts/compare_llm2026b.py` and `scripts/check_angular_variance_llm2026b.py`,
run against `new_montecarlos_codex/results/sampled_power_anisotropy_eps*.npz`:

- Median $\hat C_{\rm shot}/4\pi$ at 2.69 / 32.6 nHz: $5.5\times10^{-4}$ /
  $5.1\times10^{-2}$ ($\varepsilon=0.20$), $4.9\times10^{-3}$ /
  $9.1\times10^{-2}$ (0.38), $5.2\times10^{-2}$ / $1.9\times10^{-1}$ (0.66).
  Theirs (LM24): $3\times10^{-3}$ / $5\times10^{-2}$.
- 95% width: ours 1.42-2.26 dex, theirs 1.7 dex. Mean/median at 30 nHz: ours
  1.5-2.1, theirs 2.0. Median log-log slope: ours 1.82 / 1.17 / 0.53, theirs
  1.1-1.2. $h_c^2$ mean/median: our $\varepsilon=0.20$ gives 1.01 / 1.49 against
  their 1.03 / 1.4.
- Their LM24 sits between our $\varepsilon=0.20$ and $0.38$ in shot noise and on
  top of $\varepsilon=0.20$ in spectral skewness. Most of the residual gap is our
  $\phi_\sigma$ rescaling (13.3$\times$ at $\varepsilon=0.20$) to match the GWB
  amplitude, which LM24 does not apply.
- **Ledger truncation checked:** top-10 vs top-100 moves the median
  $\sum_a p_a^2$ by $\le 9\%$ (worst case) and $<2\%$ elsewhere. Not a factor.

**The one substantive gap in their method.** They compute $\hat C_{\rm shot}$
from strain moments alone, never placing a source on the sky, justified by
$\ell$-independence. Tested against our sampled realizations: the
$\ell$-independence claim is **confirmed** (mean realized $C_\ell/C_0$ flat over
$\ell=1$-6, equal to $\sum_a p_a^2$ to three digits, ratio mean 1.00), but
$\sum_a p_a^2$ is $\mathbb E[C_\ell/C_0\mid\{p_a\}]$, so the realized dipole
carries a further 1.15-1.41 dex of 95% scatter (0.41-0.52 dex averaged to
$\ell\le3$, 0.22-0.28 dex to $\ell\le6$). Adequate for a broadband amplitude,
not for a single multipole. Recorded in [[concepts/dipole_distribution]].

**Second definitional mismatch:** their counts are per $d\ln f$, ours per PTA
bin ($\Delta\ln f = 1/(fT_{\rm obs}) = 1/16$ at $f=1/{\rm yr}$). Per-bin is the
observationally relevant one and carries fewer sources, hence more shot noise, at
high frequency. They list this as future work. Direction known, magnitude not
computed (would need their population model).

**Deliverable.** [reviews/lin_lidz_ma_2026b_comparison.html](reviews/lin_lidz_ma_2026b_comparison.html) — change-from-
previous-claims table, head-to-head numbers, four discrepancies, and a
prioritized six-item draft-change list with suggested LaTeX, plus a
citation-extent recommendation (cite it three times, neutrally, framed as
concurrent and independent; do not restructure).

**Registries touched:** `index` (source entry + counts 31→36 pages, 9→10 arxiv,
review link), `formulas` (5 new rows), `bibliography` (provisional
`LinLidzMa:2026b` + the pending-verification note), `reproducibility` (reference
index row), `todo`, plus `references/2608.09929/README.md`,
`scripts/fetch_references.sh` (new ID) and the "all 9"→"all 10" strings in
`CLAUDE.md` and `references/README.md`.

**Bib status: NOT added to `references.bib`.** arxiv abstract page and the tex
source agree on title/authors/date, but ADS is JS-gated and returned nothing, so
`verify-reference` has one source, not two. Awaiting MZ's call.

## [2026-08-11] review | GS-P comments placed in the tex; blind-comprehension and voice audits

MZ forwarded ten comments from GS-P on `paper_v2` and asked for them to be
placed as comments **at the passage each refers to** rather than acted on, so he
can do one pass over everything at once. Same for the arXiv:2608.09929
integration decisions. Then, separately, a report on the "confusing / sounds
like AI" question, produced so that it can find real problems.

**Annotation layer.** Two new macros in `paper_v2/paperclaims.sty`:
`\gscomment{}` (magenta `[GS-P:]`) and `\ccnote{}` (teal `[DECIDE:]`), both
draft-only and invisible under `[final]` like the rest of the provenance layer.
14 GS-P blocks and 7 DECIDE blocks placed. All ten of GS-P's items are covered;
`Eq.~8` in her voice comment is almost certainly a slip for Eq.~18 (her two
examples, "the survival function of Eq. 17" and "forward law read backwards",
are both at `eq:p1_given_x`), so the comment sits there with a numbering note
left at `eq:neff`. **Prose untouched.** Draft build 18 pp, `[final]` build 16 pp,
both 0 errors / 0 overfull / 0 undefined.

**Blind comprehension read.** A fresh agent with no session context was given a
single flattened file (sections + title + abstract, provenance macros stripped)
in an otherwise empty directory, forbidden every other tool, and told that
wanting outside context *was the finding*. Verified findings:

1. **$\rho_0$ is quoted three incompatible ways** — abstract "$\approx 5$
   integrated over the entire band", intro "of order unity per frequency bin",
   `sec:sd_setup` "$5/\sqrt5\approx2$" then "of order a few". A factor $\sim5$ in
   the quantity every detection statement is proportional to.
2. **Eq.~(25) $\rho_{\rm ps}\propto p_1$ implies $D\propto p_1^2$**, but
   `sec:sd_cl` says the coherent fit scales as $p_1$. Checked against
   [[concepts/fisher_hierarchy]]: both are in the project, for *different*
   searches (CW in the residual mean, $\rho\propto\sqrt{p_1}$; covariance matched
   filter, $\rho\propto p_1$). `sec:sd_bottom` names both in one sentence, which
   is where they merge. Flagged for MZ, not asserted as an error.
3. **Fig.~5 uses a top-20 ledger, Fig.~3 a top-100** — confirmed in
   `fig_p1_distributions.py` (`brightest_n_strains`, shape (10000,44,20)) vs
   `fig_c1c0_neff_vs_freq.py` (all 100). The quoted 66%/77% concentration comes
   from the top-20 version. Magnitude of the effect $\le 9\%$ (from the
   truncation check run for the LLM26b comparison).
4. **"strictly less sensitive" (abstract) vs "the two searches are identical" at
   $L=1$** (`sec:sd_cl`).
5. **$\eta$ and $x$ each carry two meanings** ($q/(1+q)^2$ vs
   $\sum_{a\ge2}p_a^2$; $C_1/C_0$ vs $(1-\cos\zeta_{ab})/2$).
6. Fig.~8's caption says the $\varepsilon=0.66$ median reaches the CW limit;
   Table~II gives median $h_0=3.2\times10^{-15}$ against $8\times10^{-15}$.

**Two of its findings were artifacts of my own flattening script** (removing
`\dataref{}{}` and `%` continuations produced "frequency,because" and a broken
`95\%`). Recorded in the report as false positives — the sandbox must strip
annotations more carefully next time.

**Voice fingerprint.** A second fresh agent, running concurrently and never
shown this draft, derived an 18-test operational fingerprint from
`references/{2406.17010,2312.06756,2305.05690}/main.tex` (19,226 body words, 670
sentences, 115 equations). I ran the checklist as deterministic counts rather
than delegating the grading. Result: **every stereotyped LLM tell is absent**
(em-dashes 0 vs 6, sentence-initial Importantly/Crucially 0, "not X but Y" 0,
abstract-noun agents 0, impressiveness adjectives 0, rhetorical tricolons 0).
Three real deviations: **semicolons 30 vs effectively 0** (the corpus has none in
19k words — the sharpest signature and the cheapest fix), **paragraph-final
sentences $\le12$ words 42% vs 25%**, and **`we/our/us` 5.6/1k vs 15.3/1k**.

**The "dry equations" finding is not what it looks like.** Assertion rate is
**69% in the manuscript and 69% in the corpus** — identical. The real deviation
is connective prose: median gap between consecutive equations 30 words vs 45,
equations with no following comment 12% vs 4%, and one run of six equations in
`sec:cl` with under 20 words between each. Acting on the complaint without the
corpus baseline would have pushed the paper *away* from its own voice.

**New tracked tool.** `scripts/prose_audit.py` — project-independent, pure
stdlib, no LLM: alias clustering with a referring-expression instability index,
sentence-length distribution, construction blacklist, punctuation/person
signatures, equation-introduction classification, inter-equation prose gaps,
paragraph density. Every threshold is taken from `--corpus` rather than fixed,
so it measures deviation from the authors rather than from taste. Copy it into
any repo.

**Deliverable.** [reviews/prose_audit_report.html](reviews/prose_audit_report.html)
— the two audits, the verified/artifact split, the mechanical measurements, a
root-cause section on why LLM prose fails these specific ways, and the reusable
four-step process (fingerprint once per group; blind read per draft; linter per
draft; naming ledger as prevention).

## [2026-08-11] remediation | paper_v2 full source moments and complete rerun

MZ authorized Codex to commit the complete working tree so the audit could be
rolled back cleanly. The recovery point is commit `94bc208` (tree
`15d2c945`); the code/test correction is commit `ab1c2e5`. The legacy 11 NPZ
products remain byte-for-byte intact (11/11 SHA-256 matches, 10.67 GB), and the
corrected products live separately in
`new_montecarlos_codex/results_full_moment_v2/`.

**Correction.** Schema v2 stores direct realization-level total power $Q$,
full second moment $S_2=\sum_a w_a^2$, $N_{\rm eff}=Q^2/S_2$, and the direct
dipole vector. A marked-Poisson order-statistic calculation makes the
top-100 ledger complete and represents its unresolved remainder with positive
Gamma/Dirichlet maps. The compact population and three-frequency walk products
are bitwise derivatives of the same power realization, with no second random
draw. The old $E[w]^2$ bulk moment, clipped map, and partial-ledger semantics
are rejected by the loader and tests.

**Production.** Three 10,000-realization, 44-frequency, NSIDE=8 runs used seed
42. Each power product is 4,901,609,571 bytes and took 22--25 minutes; each
compact population derivative is about 0.31 GB and took 31 seconds. Their
SHA-256 prefixes are `5a72a86b`/`4e874038`, `cf324689`/`ffbd4c82`, and
`0ca2e320`/`eeb40ba2` for $\varepsilon=0.20,0.38,0.66$ (power/population).
The independent validator reports `all checks pass`, including map positivity,
direct $C_0,C_1$, normalization, complete remainder identities, and bitwise
common-run arrays.

**Scientific result.** At the lowest frequency the corrected median
$N_{\rm eff}$ is 1167, 182, and 18.9, with median $C_1/C_0=7.79\times10^{-4}$,
$5.06\times10^{-3}$, and $5.05\times10^{-2}$. The probabilities of exceeding
0.2 are 0.11%, 1.83%, and 17.96%. Model ordering, threshold truth values,
brightest-source detectability, and the paper's qualitative conclusions are
unchanged. The largest headline shift is the low-frequency
$\varepsilon=0.20$ $N_{\rm eff}$, 1811 to 1167; it is numerically large but
scientifically small because the same realization remains deeply isotropic.
Verdict: **no substantive conclusion change found**.

All 11 figures, two table sidecars, 94 registered number keys, and the 19-page
annotated PDF were rebuilt. Nineteen visible `CODE AUDIT` decision notes retain
the author's prose choices rather than silently making the final prose pass.
The deterministic detection calibration gives amplitude ratios
1.0000, 1.0831, 1.1384, 1.2072 for $L=1\ldots4$, with exact zero-uncertainty
equality at $L=1$. The analytic sqrt-SH $\ell^b_{\max}=3,6,23,47,95$ sequence
has strictly decreasing 95th percentiles 0.2024, 0.08589, 0.008757, 0.002218,
0.000564. Final verification: 37 tests pass in 117.90 s, provenance passes,
`git diff --check` passes, and all 19 PDF pages pass visual inspection.

## [2026-08-12] paper | MZ's read surfaced in the PDF, and a decision console

MZ's own comments on the draft are now in the paper next to the passages they
refer to, and every open item — his, Gabriela's, and the agent-raised ones from
the code audit, the new-literature comparison and the style audits — is
enumerated once in a decision console he can work through against the printed
PDF.

**Annotation ids.** `paperclaims.sty` gains `\mzcomment` (burnt orange) beside
the existing `\gscomment` and `\ccnote`, and all three now take a stable id as
their first mandatory argument, printed inside the tag: `[MZ-05:]`, `[GS-04:]`,
`[D-12:]`. Ids are assigned in document order by
`paper_v2/scripts/number_paper_comments.py`, which is idempotent and also
exports the inventory (id, kind, file, line, enclosing section, printed page
read back out of the PDF with `pdftotext`, LaTeX body). 54 items: 14 MZ, 14
GS-P, 26 DECIDE. All three macros still vanish under `[final]`.

**MZ's 14 comments.** Twelve at their passages plus two document-wide sweeps.
The specific ones: split the 56-word abstract sentence; "the anisotropy is
effectively the single brightest source" equates a property of the sky with an
object; the third Introduction paragraph should be said in words (subsumes
GS-03); derive the characteristic function instead of asserting it; the power
kernel is never said in words before it is displayed; multiplier → factor;
"forward law" is coined jargon (subsumes GS-02 and GS-08); split the 50-word
"deepest limit" sentence; use the real limit curve in Fig. 8; "pivotal";
the $\rho_0\simeq20$ sentence does not belong in Sec. V A; "closes the loop".
The two sweeps carry the mechanical evidence: 27 body sentences (9.8%) at 45
words or more against a median of 22, the ten worst listed by location; and
every occurrence of the three word-choice rules, plus three further phrases the
same rules would catch.

**Fig. 8 traced.** The cyan binned line of Goncharov et al. Fig. 6 is the
NANOGrav 15-yr individual-source search, and that analysis has a public data
release: `nanograv/15yr_cw_analysis` ships `data/15yr_cw_3d_limits_v4.npz` with
`UL_skies`, the 95% $h_0$ limit on 22 frequency bins × 192 sky pixels
($N_{\rm side}=4$). No digitizing is needed. Read here, the sky-averaged limit
runs $5.2\times10^{-14}$ (1.1 nHz) → $6.4\times10^{-15}$ (8.0 nHz) →
$1.0\times10^{-14}$ (27 nHz) — the shape the caption currently asserts in
words. Open question recorded in the item: the sky average of this file is
$7.4\times10^{-15}$ at 5.9 nHz against the $8\times10^{-15}$ at 6 nHz quoted in
the paper's abstract, so which reduction reproduces the published curve must be
confirmed before plotting. The comparison improves either way: at
$f=0.085\,{\rm yr}^{-1}$ (2.7 nHz) the limit is $1.3\times10^{-14}$ against the
$\varepsilon=0.66$ 95th percentile of $1.17\times10^{-14}$, so every model sits
below the limit at every frequency and the "only marginally so" hedge can be
replaced by a number.

**Fig. 9 arrow (GS-12) answered.** Checked in the generating script: the arrow
is a deliberate `annotate()` from the "dipole only: 29%" label to the $L=1$
point, but the label sits far from it in the rendered figure, so it reads as a
stray mark, and the caption never mentions it. The 29% is already in both the
caption and the text.

**Deliverable.** [reviews/paper_v2_decisions.html](reviews/paper_v2_decisions.html)
— 54 rows in document order, each with the note exactly as the PDF prints it
(converted from the `.tex` at build time, never copied, so it cannot drift), a
suggested resolution, item-specific options, a decision control and a note box.
Decisions persist in the browser and export as Markdown or JSON. Built by
`paper_v2/scripts/build_decision_console.py` from the inventory plus the
authored half in `paper_v2/data/decision_items.json`.

**Build.** `paper_v2/main.pdf` rebuilt: 21 pages, 0 errors, 0 overfull boxes,
no undefined references or citations, and all 54 ids located on a printed page.
One regression found and fixed during the pass: the first edit had dropped
`\end{abstract}`, which surfaces as "Not in outer par mode" at the first float
rather than anywhere near the abstract.

No prose was changed and no number was touched: this pass only records
decisions to be made.

## [2026-08-12] paper | decisions returned, implementation intent written

MZ worked through all 54 items in the decision console and exported the result;
it is committed as `paper_v2/data/decisions_2026-08-12.json`. Validated against
the inventory: 54/54 decided, no unknown ids, every key valid for its item.
48 chose option A, three chose B (D-07 the single clause, MZ-10 rewrite against
the new curve, D-25 skip), and three are OTHER with written instructions (D-01
"just say never more sensitive without the parenthesis", D-11 "a bit pedantic
... leave as is", D-24 "matter of fact, no judgement just the facts").

**One decision changes a scientific statement.** MZ-11 (plot the real
frequency-dependent NANOGrav continuous-wave limit) was checked against the
models before writing the intent. Against the sky-averaged limit from
`15yr_cw_3d_limits_v4.npz`, over its support 0.034--0.868 yr$^{-1}$, the
brightest-source amplitude never reaches the limit in any model: the maximum
ratio of the $95$th percentile to the limit is 0.290 ($\varepsilon=0.20$, at
$f=0.215$), 0.504 ($0.38$, at $0.085$) and 0.898 ($0.66$, at $0.085$); the
median maxima are 0.114, 0.185 and 0.245. The four hedges that say the
heaviest-tailed model reaches or exceeds the limit (abstract, Introduction,
Sec. IV C twice, Summary) are therefore wrong once the curve is plotted, and the
replacement statement is both simpler and stronger.

Two caveats recorded for the implementation: the sky average of the public file
is $7.4\times10^{-15}$ at $5.9$ nHz against the $8\times10^{-15}$ at $6$ nHz
quoted by the published paper, so the plotted curve must not be described as the
published curve; and the per-pixel limit at the lowest paper frequency spans
$5.1\times10^{-15}$ to $2.7\times10^{-14}$ about the sky mean, so the caption
must say sky-averaged.

**Deliverable.** `intents/paper-v2-decision-implementation_intent.txt` — eleven
phases, an item table covering all 54 ids, the ground rules (no hand-entered
numbers, annotations deleted as they are applied, prose-only except three figure
scripts), the P8 scientific change, and the verification and receipt
requirements. Two things the decisions did not settle are resolved in the
intent and flagged for veto: D-26's finding (v) had no item of its own, so the
two notation collisions are fixed there ($\eta$ as both faint-background
variance and symmetric mass ratio, resolved by writing $[q/(1+q)^2]^2$ in
Eq.~12; $x$ as both the measured dipole and the Hellings--Downs variable,
resolved by renaming the latter $u$ in Eq.~22).

## [2026-08-12] paper | all 54 decisions implemented; one scientific statement changes

The text-settling pass on `paper_v2`. Every one of the 54 decisions in
`paper_v2/data/decisions_2026-08-12.json` is applied and its annotation
deleted, so the draft carries no `\mzcomment`, `\gscomment` or `\ccnote`
anywhere. Traceability lives in the committed inventory, the decisions file and
`intents/paper-v2-decision-implementation_receipt.md`. BASELINE for the run was
`6124518`; nothing under `references/` or `results/` was touched and no Monte
Carlo was rerun.

**The one scientific change.** Decision MZ-11 put the real NANOGrav 15-yr
continuous-wave upper limit into Fig. 8, replacing the single verified point
$h_0 = 8\times10^{-15}$ near 6 nHz. The curve is the sky average over the 192
pixels of `UL_skies` in the public `nanograv/15yr_cw_analysis` grid, drawn at
the geometric bin centres over the file's own support (0.034--0.868 yr$^{-1}$)
and never extrapolated. Against it, computed in the figure script and
registered:

| $\varepsilon$ | max(95th pct / limit) | max(median / limit) |
|---|---|---|
| 0.20 | 0.290 at $f = 0.215$/yr | 0.114 at $f = 0.085$/yr |
| 0.38 | 0.504 at $f = 0.085$/yr | 0.185 at $f = 0.085$/yr |
| 0.66 | 0.898 at $f = 0.085$/yr | 0.245 at $f = 0.085$/yr |

No model reaches the limit anywhere the grid covers. The four hedges that said
otherwise — "except in the tail of the most heavy-tailed model" in the abstract,
"except in the rare tail" in the Introduction, "the heaviest-tailed model only
marginally so" and "except in rare realizations of the most extreme model" in
Sec. IV C, and "except in the tail" in the Summary — are gone. The replacement
is the plain statement that in every model the brightest source stays below the
sky-averaged limit at every frequency, said once with its number in Sec. IV C:
the closest approach is the $\varepsilon = 0.66$ 95th percentile at the lowest
frequency, at 0.90 of the limit. This is the only change of scientific content
in the run; every other edit is prose, notation, or a caption.

**New external data dependency.** `paper_v2/data/15yr_cw_3d_limits_v4.npz`
(136,652 bytes, SHA-256 `dd8373503f5e...68f5b35`, retrieved 2026-08-12 from
`raw.githubusercontent.com/nanograv/15yr_cw_analysis/main/data/`) is now in the
tree, with `paper_v2/scripts/fetch_cw_limits.sh` to re-fetch and verify it and a
full entry in [[reproducibility]]. Disclosed, not hidden: the sky average of
this file is $7.4\times10^{-15}$ at 5.9 nHz while
Ref. `NANOGrav:2023individual` quotes $8\times10^{-15}$ at 6 nHz, so the plotted
curve is never called the published curve and the published value stays in
Table II where it is quoted as a published number. The per-pixel limit at the
lowest paper frequency spans $5.2\times10^{-15}$ to $2.7\times10^{-14}$ about a
sky mean of $1.30\times10^{-14}$, which is why the caption says sky-averaged.

**Addendum, same day: that gap is explained, and the follow-up it generated was
wrong.** The receipt and this entry first logged "ask Boris Goncharov for the
array behind the cyan line" as the way to settle which reduction reproduces the
published curve. That was the wrong question. The two numbers are two
estimators, and `NANOGrav:2023individual` Sec. IV.1 says so outright: *"the
sky-averaging is not done uniformly on the sky, but rather through the
posterior samples, which in practice results in the all-sky limit being biased
high. In this example $\sim$73% of the sky gives a lower upper limit than the
all-sky value."* The headline number is the **sky-marginalized** limit, the
95th percentile of the pooled $h_0$ posterior with sky position a free MCMC
parameter; the npz is the **fixed-sky** limit as a function of position,
released separately for follow-up studies. Both live in the same public
repository, and the published value was reproduced from it directly:
`data/15yr_quickCW_UL.h5` with the estimator of `UL_analysis.ipynb` gives
$8.227\times10^{-15}$ in bin 11 (5.4506--6.3590 nHz, geometric centre
$5.887$ nHz) — the same bin the paper calls its most sensitive — against a
uniform pixel mean of $7.367\times10^{-15}$, a ratio of $1.117$ in the
direction the paper predicts, with 69.8% of the sky deeper than the all-sky
value against the paper's "$\sim$73%". No email is needed and the item is
closed. What is left is a choice, not a question: MZ-11 option A specified the
sky average of the per-position map, which is what Fig. 8 plots, while MZ's own
words pointed at the cyan line, which is the all-sky curve. The all-sky curve
is weaker in every bin and would widen the Sec. IV C margins
($0.290/0.504/0.898 \to 0.255/0.429/0.764$), but it spikes by two orders of
magnitude at $f = 1.013\,{\rm yr}^{-1}$, the annual timing-model hole, right at
the edge of the plotted range. Logged for MZ in [[todo]].

**Three figure scripts changed, and only three.** Fig. 8
(`fig_pixel_amplitude.py`, above); Fig. 7 (`fig_p1_neff_conditional.py`, hue
freed so the six curves are no longer all green — GS-09, recorded as the single
exception to the $\varepsilon\to$color convention in [[conventions]]); Fig. 9
(`fig_source_snr_vs_resolution.py`, the stray "dipole only: 29%" annotation and
its arrow deleted — GS-12). The other eight figure PDFs are byte-identical to
BASELINE.

**Notation.** Two symbols carried two meanings each and now carry one. $\eta$
is the faint-background variance only: the single-binary strain formula
(Eq. 13, not Eq. 12 as the intent said) writes $[q/(1+q)^2]^2$ inline and the
mass-ratio definition is gone. $x$ is the measured dipole only: the
Hellings--Downs variable in Eq. 22 is now $u$. Both are recorded in
[[conventions]].

**Prose.** Sentences of 45 words or more fell from 27 to 1, the longest from 76
words to 46, and the median from 22 to 18. Semicolons went from 30 to 0 against
zero in 19,226 words of MZ's published prose. All ten sentences named in MZ-02
are gone; the single survivor is an artifact of the linter's sentence splitter,
which does not break after `.)`. "Forward law" is gone (MZ-09), one name per
object throughout (GS-02, GS-08: the exceedance probability, not also the
survival function), "multiplier" is "factor", and "pivotal", "closes the loop",
"a roundabout measurement of" and "sets up everything that follows" are
rewritten. Sec. V C is restructured: the four statistics are named as a set
where they are introduced, $K_L = L(L+2)$ gets its own sentence, the
linear-versus-quadratic response gets its own paragraph, and the
covariance-versus-coherent bridge is restored in two sentences so that
profiling the source-subspace amplitude is not confused with the $C_\ell$
compression. The $\rho_0$ inconsistency the blind reader could not resolve is
settled everywhere: $\approx 5$ band-integrated, $\approx 2$ per bin across the
roughly five signal-bearing bins, with a sentence in Sec. V A saying which is
meant by default.

**Literature.** `LinLidzMa:2026b` is in `references.bib` under MZ's explicit
single-source waiver (D-02); the ADS re-check is an open item. "Relation to
recent work" is rewritten to MZ's instruction — "matter of fact, no judgement
just the facts" — listing what their Monte Carlo paper revises (moment estimate
over its own mean by 130 at 1/yr; $f^{8/3}\to f^{1.1-1.2}$; the bound
$\hat C_{\rm shot}/4\pi\le1$; the realized $1/\sum_a p_a^2$ definition of
$N_{\rm eff}$) and where our results coincide, with no claim that anyone
conceded anything. Our two surviving qualifications are stated as untouched by
either paper. D-25 was skipped by decision.

**Verification.** `pdflatex/bibtex/pdflatex/pdflatex`: 0 errors, 0 overfull
boxes, 0 undefined references or citations, 17 pages (21 at BASELINE, the
difference being the deleted annotations). 9 underfull hboxes and 2 "float is
stuck" advisories, both unchanged from a rebuild of BASELINE at `6124518`.
`check_provenance.py` prints "all checks pass". 37 tests pass in 116.8 s.
`git diff --check` clean. All 17 pages inspected. `compute_paper_numbers.py`
re-run: every pre-existing key reproduces bit for bit, 12 keys are new
(`cw_limit_*`, `h0_over_cwlimit_*`, `eta_mean_given_02_{min,max}`), and the
sqrt-SH truncation sequence is now stored to five decimals so the manuscript
can display $0.00056$ at $\ell^b_{\max}=95$ (D-22).

Receipt, with the per-id table and every conflict hit:
`intents/paper-v2-decision-implementation_receipt.md`.

## [2026-08-12] paper | audit of the decision-implementation run

The fix run was audited from a clean rebuild rather than from its receipt. Every
mechanical claim reproduces: 17 pages with zero errors, overfull boxes and
undefined references; no surviving annotation; provenance and all 37 tests pass;
eight figures byte-identical and three changed as authorized;
`compute_paper_numbers.py` regenerates the registry with zero differences; the
tracked NANOGrav grid matches a fresh download and its fetch script re-verifies
after a live re-download; the P8 ratios recompute to 0.290/0.504/0.898; the new
bib entry matches arXiv on title, authors and date; sentences at 45+ words fall
27 → 1 and clause-welding semicolons to zero.

Four defects were found and fixed: a dropped word in the Discussion ("The
NANOGrav bounds both compare against reproduce the prior"); an unqualified "at
every frequency" in the abstract, Introduction and Summary, where the published
limit covers only 1.1--27.5 nHz; an invalid inference in Sec. V C, where
$\rho_{\rm ps}^2/\sqrt{2K_L}$ was used to conclude that a quadratic statistic is
never more sensitive, although that expression exceeds $\rho_{\rm ps}$ for
$\rho_{\rm ps}>\sqrt{2K_L}=4$ at $L=2$, which is the paper's own
$\rho_0\simeq20$ operating point (the claim itself is right and now cites the
threshold Monte Carlo); and two different continuous-wave limits in one paper.

On the last, MZ decided to carry one number only, the one Fig. 8 plots. Table
II's caption no longer quotes NANOGrav's published all-sky $8\times10^{-15}$
near 6 nHz — a different estimator from the plotted sky average of the
per-position grid — and instead quotes the plotted curve's own value at the
table's lowest frequency, $1.3\times10^{-14}$ (registered
`cw_limit_skyavg_f0085`), names its source exactly, and refers to the figure for
the rest. The open question of which curve to plot is closed by the same
decision. Details in `intents/paper-v2-decision-implementation_receipt.md` §10.

## [2026-08-12] release | `release/` assembled and verified, nothing published

The public release mirror of `paper_v2` is built, and built the way DESI-w0wa's
is: a derived tree, assembled by explicit copy from an allowlist by
`scripts/assemble_release.py`, never hand-edited. Re-cutting it is one command.
Nothing remote was created — no repository, no remote, no push, no upload. The
commands for those are in `intents/release-handoff.md`.

**The four defects first.** SciPy was the blocker: `source_detection.py` imported
`sph_harm`, removed at SciPy 1.17, with scipy unpinned. The intent said migrate
and pin a floor, but a floor of `>=1.15` is the one thing that cannot work here —
`sph_harm_y` does not exist below 1.15, so that floor would have excluded the
reference platform (scipy 1.11.3) on which every production array and every
registered number was computed. The module now takes whichever name exists and
back-ports the other. The transposition that [[todo]] warned would silently
corrupt $\alpha_L$ was checked rather than trusted: over 2005 directions and 81
harmonics the migrated design matrix is **bitwise identical** to the original
call on scipy 1.11.3, and agrees to 6e-12 on scipy 1.18.0 where `sph_harm` is
gone, with $Y^\dagger W Y = I$ holding at 3e-15 on both. PyYAML, which
`check_provenance.py` imports and nothing declared, is declared. The release uses
a src layout with its own `pyproject.toml`, because a flat `find_packages()`
finds nothing once the package moves to `src/`; `pip install -e .` was run in the
isolated copy to prove it. And Fig. 4's generator now writes the paper figure
directly instead of needing a manual copy, with the legend relabelled from "3D
walk (exact)" to **"3D walk"** — the last outstanding D-09 follow-up, and the
only shipped figure that changed. The relabel was confirmed to be the whole
change: 1162 of 1.5 M pixels differ at 300 dpi, all of them inside the legend
label.

**Three things the intent did not anticipate, and one it could not have.** A
third docstring cited the wiki — in `gwb_sources/source_detection.py`, not just
the two figure scripts named — and rewriting it turned up a *stale claim* rather
than a stale pointer: `fig_pixel_amplitude.py` still said the published NANOGrav
value "is retained in Table III", which stopped being true when MZ decided to
carry one number only. Twelve `\fromnotebook{...}` annotations point at
`references/` and `notebooks/`, which never ship, so they are stripped from the
release `.tex`; in `[final]` the macro is a no-op, so the PDF is untouched, and
`\genby{...}` is kept because it names a script that does ship. And the shipped
test file was named `test_new_montecarlos_codex.py` — an excluded directory name
living in a **filename**, which no content grep can see. It surfaced only because
`pip install -e .` wrote that path into `SOURCES.txt`. It ships renamed, and the
assembler now scans path components too.

**"Bit reproducible" was tested, not asserted.** The audit's objection stands and
is now settled with a measurement. Building a fresh environment with every Python
package version held *identical* to the reference platform but a different
OpenBLAS build (conda-forge 0.3.25/OpenMP against 0.3.21) isolates the real
variable. Under it: `paper_numbers.json` and both table sidecars are
byte-identical; the eleven figures are raster-identical with **zero** differing
pixels at 200 dpi, differing in bytes only through matplotlib's `/CreationDate`
and version string, and byte-identical once `SOURCE_DATE_EPOCH` is fixed; and the
stored reference arrays agree to 1.1e-14 of each array's scale. That last number
is why three test assertions moved off `assert_array_equal` onto a `1e-12`-of-scale
tolerance — pinning versions did not help, because the versions were already the
same. The metric matters: pointwise relative error is the wrong measure for an
FFT-inverted density, where a 1e-15 absolute error at the peak reads as 1e-9
"relative" out in the tail while meaning nothing. The word "bitwise" now appears
in the release README for exactly the artifacts that earn it.

**What the committed data honestly cannot do.** The intent asked twice that every
figure rebuild from committed data in seconds. Seven of the eleven need the three
`sampled_population_analysis_eps*.npz`, which are 0.31 GB each — past GitHub's
per-file limit, and not fixable by reduction. No figure script touches the 4.9 GB
power cubes at all; those serve one analytic cross-check inside
`compute_paper_numbers.py`. So `make_all_figures.py` builds what the present data
allow and states what it skipped and why: 4 of 11 from committed data, 11 of 11
with the data root populated. `fetch_data.sh` splits the same way, population set
by default and power cubes behind `--with-power`.

**Verification.** In a temporary copy, in an environment created from the
*shipped* `environment.yml`: `pip install -e .` discovers the package; the CW grid
re-verifies against its recorded SHA-256; all eleven figures regenerate
raster-identical to `paper_v2/figures/`; `compute_paper_numbers.py` reproduces the
106-key registry byte for byte; both table sidecars regenerate byte-identically;
`check_provenance.py` prints "all checks pass" **inside the assembled tree**; 37
tests pass; the paper builds `[final]` at 17 pages with 0 errors, 0 overfull
boxes and 0 undefined references, and `pdftotext` finds no provenance tag and no
filename; the five forbidden greps return nothing; no excluded directory is
present. The arXiv tarball compiles standalone in a clean directory, also clean.

One item was seen and deliberately not fixed: `run_sqrtSH_realizations.py` still
passes `verbose=False` to `hp.alm2map`, which newer healpy rejects. It ships, and
`reproduce.sh` calls it, so it will bite anyone who relaxes the healpy pin. It
was outside the four defects the intent authorized, so it is logged in [[todo]]
instead of patched.

Receipt, with the assembly manifest, the rewrite table and the full verification
log: `intents/paper-v2-release-build_receipt.md`. Release section, data policy
and the Zenodo plan: [[reproducibility]].

## [2026-08-13] release | public GitHub release audited from a fresh clone — hold

The release receipt was rechecked from public commit `1479f33` in a fresh clone,
a second committed-only worktree, and a new environment made from the shipped
specification. The release is not ready: the documented figures entrypoint
builds 2/4 committed-data figures and 9/11 with all production arrays before
exiting nonzero; the full pipeline stops at the same point; the test suite fails
during collection and still contains the three exact comparisons the receipt
says were changed to a measured tolerance. The Zenodo manifest disagrees with
all six arrays' embedded schema and carries internal producer paths,
`CITATION.cff` is invalid YAML, excluded duplicate/build files are tracked,
source comments and registries retain internal or nonexistent filenames, and
one deterministic JSON sidecar drifts by a few ULPs.

The scientific artifact checks are reassuring but do not clear those release
gates: all six array hashes match, the 106-key number registry and both table
sidecars reproduce byte-for-byte, all eleven figure rasters match once the two
path defects are bypassed diagnostically, provenance and detection
cross-checks pass, and the committed-only final paper builds cleanly at 17
pages with no forbidden PDF text. No release defect was fixed. Full commands,
actual outputs, severities and work order:
[reviews/release_audit_2026-08-13.html](reviews/release_audit_2026-08-13.html).

## [2026-08-13] release | audit defects cleared; the paper now cites the repository and the deposit

All seven findings of [reviews/release_audit_2026-08-13.html](reviews/release_audit_2026-08-13.html)
are fixed at the source, not in `release/`, and the release re-cut from it.
Two additions the audit did not ask for came with the same pass: an
introduction footnote and an acknowledgment naming the GitHub repository and
the Zenodo record, and GSP's Friends of the Institute for Advanced Study Fund
support. `main.tex` defines `\repourl`, `\zenododoi` and `\zenodourl` once;
`scripts/stamp_doi.sh` now writes the DOI into the paper as well as the release
generator, and `assemble_release.check_addresses` refuses to build a release
whose paper and repository disagree about either address.

**F01, entrypoints.** `fetch_cw_limits.sh` and `fig_pixel_amplitude.py` honour
`PTA_DATA`; `compute_paper_numbers.py` writes the registry and reads both JSON
sidecars through the same root; `fetch_data.sh` seeds a non-default root with
every committed artifact, verifying each SHA-256, so the one-root promise is
now true wherever the root points. `reproduce.sh` gained the Fig. 4 walk stage
it claimed in the README but never ran. The figure scripts also honour a new
`PTA_FIGURES`, which is what lets the two new end-to-end tests
(`tests/test_figure_entrypoints.py`) assert the reader contract — four figures
and exit 0 from committed data, eleven and exit 0 with the arrays — without
touching the committed PDFs. The two path defects behind the original failures
were already repaired in the working tree; the public tree was simply a cut
behind, which is why the assembler now builds the paper itself.

**F02, tests.** 39 collected, 39 pass. The README's count is asked of pytest at
assembly time instead of typed.

**F03, array provenance.** One schema policy: every deposited array carries
`pta_anisotropy.sampled_full_moment` and `product_kind` separates power from
population, which is what `ZENODO.md` now says. `scripts/build_zenodo_deposit.py`
writes `zenodo_deposit/` — the six arrays with `producer` rewritten to the
release path and `derived_from_power_product` reduced to a file name — and
records their new sizes and SHA-256 in `intents/zenodo_deposit_manifest.json`,
which the release generator reads. Verified member by member: 103 (power) and
93 (population) members compare equal; only the two provenance strings differ.
The two committed NPZ products get the same treatment during assembly. See
[[reproducibility]] "Zenodo deposit"; **upload `zenodo_deposit/`, not the masters.**

**F04, citation metadata.** `CITATION.cff` was being flattened into invalid YAML
by the dedent helper that formats the generated files. It is now written raw.

**F05/F06, what ships.** `paperclaims.sty` is no longer copied: the release
writes its own, defining only the three macros the shipped LaTeX uses, so the
review vocabulary has nowhere left to live. The registries, the two adapted
tools and `main.tex`'s header lost their sibling-project attribution and their
pointers to files that do not ship; the registries' paper-relative paths became
release-relative. `FORBIDDEN_PATTERNS` grew from five greps to ten, and the
LaTeX residue is deleted after the build and ignored by name.

**F07, sidecar precision.** `detection_penalty_mc.json` is serialized at twelve
significant digits, recorded in the file itself. A rerun is byte-identical.

**The gate.** `check_provenance.py` went from seven checks to ten: every
path-like token in every shipped file must resolve, `CITATION.cff` must parse
and carry what CFF 1.2 requires, and every array in the data root must name a
producer that exists here and the schema the manifest declares. Checks 8-10
report themselves skipped outside the release layout rather than passing
silently. The assembler runs the release's own copy of the gate as its last
step, so a release that would fail a reader's first command cannot be cut.

**Verification.** `all checks pass (10 of 10 run)`; 39 tests pass; four figures
and exit 0 from committed data alone, eleven and exit 0 with the arrays; all
eleven regenerate raster-identical to the committed PDFs; `paper_numbers.json`
and both table sidecars regenerate byte-identically; `SKIP_MONTE_CARLO=1
reproduce.sh` completes all six stages with exit 0; a temporary `PTA_DATA`
comes back with seven files instead of none; the paper builds `[final]` at 17
pages with no TeX error, overfull box or undefined reference; `pdftotext` finds
no forbidden text in any of the twelve PDFs; the ten forbidden greps and the
internal-vocabulary sweep return nothing. The arXiv tarball was rebuilt from
the new release copy.

## [2026-08-13] release | Zenodo record 10.5281/zenodo.21911100 published

The record was already a complete draft — seven arrays, 15.6 GB, metadata and
licence filled in — uploaded before the release audit was cleared. Checked
against it through the deposit API before publishing: all seven files match the
release on size, SHA-256 and MD5, and the manifest documents all seven with
nothing undocumented. Published; `https://doi.org/10.5281/zenodo.21911100`
resolves, and the seven files are visible through the public records API.

The arrays on the record are the ones the paper used, deposited unmodified, so
each still records its producer path as it stood when the run was made. Rather
than re-upload 15.6 GB of relabelled copies, `data/ZENODO.md` now publishes the
mapping from each recorded path to the script that ships, and
`check_provenance.py` enforces it: a recorded producer must either exist in the
release or appear in that table pointing at something that does. The same table
exempts those paths from the dangling-path scan, so the exemption *is* the
documentation. `scripts/build_zenodo_deposit.py` and the NPZ rewrite machinery
stay for a future deposit that wants the indirection removed.

Fetching from the live record then exposed a defect worth more than the test:
Zenodo serves these files at about 600 kB/s, so a 0.93 GB fetch takes ~26
minutes and an interrupted run is the normal case, not the exception. The old
`fetch_data.sh` wrote straight to the destination, so an interruption left a
truncated file that the next run treated as complete and rejected on checksum.
It now downloads to `<name>.part`, resumes with `--continue-at -`, verifies
before moving into place, and shows a progress bar. A mismatch says how to
recover.

## [2026-08-13] release | end-to-end run against the live DOI; two defects it caught

With the record published, a fresh clone was pointed at an empty data root and
run the way a reader would. `fetch_data.sh` fetched the 0.93 GB population set
from `doi:10.5281/zenodo.21911100`, verified every SHA-256, and correctly
skipped the three 4.9 GB power maps. From that data alone all eleven figures
regenerate **raster-identical** to the committed PDFs, and with the eps066
power map present `paper_numbers.json` and both table sidecars regenerate
byte-identically. 39 tests pass; the gate prints `all checks pass (10 of 10 run)`.

Two defects surfaced that no amount of local testing would have found, because
both need a real download over a real link:

1. **Interrupted downloads were unrecoverable.** Zenodo serves these arrays at
   roughly 600 kB/s, so a 0.93 GB fetch is ~26 minutes and an interruption is
   the normal case. The old script wrote straight to the destination, leaving a
   truncated file the next run treated as complete and rejected on checksum.
   Now: `<name>.part`, `--continue-at -`, verify, then move into place.

2. **Stage 2 of the pipeline could not run after the default fetch.**
   `compute_paper_numbers.py` reads the eps066 power map for one HEALPix
   cross-check, and `fetch_data.sh` deliberately skips the power maps, so the
   documented default path died eighty lines in on a `FileNotFoundError`. It
   now preflights every input, names what is missing, and says which command
   fetches it — and notes that the registry it writes is committed anyway, so
   nothing about reading the paper depends on a 4.9 GB download. `fetch_data.sh`
   says the same thing when it skips them, and the README stage table says
   which stage needs them.

A third was corrected in the checker rather than the release: check 10 required
`derived_from_power_product` to be a bare file name, a leftover of the
abandoned plan to rewrite the arrays. It now requires the file *name* to be one
the manifest describes and ignores the historical directory, which is what
`data/ZENODO.md` tells the reader.

## [2026-08-13] release | healpy landmine removed before the repository went out

`run_sqrtSH_realizations.py` passed `verbose=False` to `hp.alm2map`. The keyword
was deprecated at healpy 1.15 and removed afterwards, so the script — which
ships and which `reproduce.sh` calls — would raise `TypeError` for anyone who
relaxed the pin. It had been logged in [[todo]] rather than fixed, because the
release intent limited working-tree changes to four named defects.

Removed. The keyword only ever controlled logging, and that was verified rather
than assumed: over four seeds the power maps and their C_l are bit-for-bit
identical with and without it, so no committed artifact moved and the sqrt-SH
prior percentiles are untouched.

## [2026-08-15] paper_v2 | GSP's read: figure collisions, a citation that only broke in the release, and the Goncharov comparison

**Three figure defects, all fixed at the script.** Fig. 2's normalization
annotation ran straight through the curves; it now sits in the empty upper-right
wedge, right-anchored. Fig. 10's "same test" label collided with the L=2 Monte
Carlo point and its right-panel y-label was long enough to run off the top of
the panel; the label moved into the empty bottom-right and the y-label is now
two lines. Fig. 8's legend was wider than the left panel and spilled into the
middle one, which is what threw off the panel spacing; the NANOGrav entry wraps
to two lines at a smaller size and "sky-averaged" stays, because the caption's
whole point is that this is a sky average and not a position-independent bound.

**The broken citation was real, and only in the release.** The committed
`release/paper/main.pdf` rendered `[?]` where Fig. 8's caption cites the
NANOGrav individual-source limit. Two causes, both now closed:

1. `arxiv/build_arxiv.sh` regenerated `release/paper/main.pdf` as a side effect
   of needing a `.bbl`, *after* the assembler had built and verified it. It now
   builds the `.bbl` in a scratch copy and never touches `release/paper`.
2. The assembler's check for undefined references matched only the summary
   phrase. Under REVTeX it is natbib that reports these, one per site, so the
   gate saw nothing. It now matches natbib's wording, reads `main.blg` as well
   as `main.log`, and — because the log proved unreliable — greps the rendered
   PDF for a literal `[?]`. Verified by injecting a bad key: the log regex
   alone still misses it; the rendered-text check catches it and aborts.

**Goncharov et al. 2026 (arXiv:2606.18241) Fig. 6 vs our Fig. 8** —
`scripts/compare_goncharov2026.py`. No disagreement, and three things worth
recording:

- The only directly comparable element is the NANOGrav 95% limit, which both
  papers draw from arXiv:2306.16222. Our sky average of the released per-pixel
  grid is 7.37e-15 at 5.89 nHz against their published 8e-15 near 6 nHz, a
  ratio of 0.92; the gap is the fixed-sky-per-pixel versus sky-marginalized
  difference the caption already explains.
- The dots agree, and MZ was right to push on this. Both describe the
  brightest SMBHB in the same sky, tied to the same measured background, so if
  the population models agree the clouds should coincide -- and they do. Their
  posterior cloud centres near $1.5\times10^{-15}$ at the lowest frequencies;
  our $\varepsilon=0.20$ median is $1.48\times10^{-15}$, and tracks their
  cloud centre across the band ($5.5\times10^{-16}$ against roughly
  $4\times10^{-16}$ near $10^{-8}$ Hz). The $\varepsilon=0.38$ and $0.66$
  medians sit a factor 1.6--2.2 higher, at the top of their cloud, which is
  the expected direction and ordering: more M--sigma scatter puts more power in
  the brightest binary, and their posterior is conditioned on data containing
  no bright source while ours is not. `--figure` puts our curves on their axes
  for a side-by-side; it is a diagnostic and no manuscript number is read off
  either plot.
- Their $h_{\rm c}$ is the *median* of $p(h_t^2)$; ours is the root of its
  mean. Same $f_{\rm ref} = 1/{\rm yr}$, but the median-mean gap is exactly our
  Sec. III subject, so the two are not interchangeable. Their $h_c = 2\times
  10^{-14}$ is an input to a 10-pulsar simulation, not an inferred amplitude.
- Physical consistency: our models put 0.09% / 1.5% / 7.0% of realizations
  ($\varepsilon = 0.20/0.38/0.66$) above the $h_{\rm cw}\sim10^{-14}$ their
  likelihood can recognise, against their published 2% (15-yr) / 5% (20-yr)
  SNR>5 forecast. Same few-percent statement; a non-detection is the expected
  outcome under every model.

**One thing checked and found correct.** The local `references/joint_search_smbhb/`
tex is the *draft*, whose table gives 0.6%/2% at SNR>5. The published v2 abstract
gives 2% (15-yr) / 5% (20-yr), which is what our paper quotes and what
[[sources/joint_search_resolved_unresolved]] already flagged as superseding the
draft. Verified against the arXiv record directly. No change.

**$\rho_0\approx5$ stands.** GSP asked whether the detection is not nearer 3.
Both numbers are right and they are different quantities: 3--4$\sigma$ is the
significance of the detection, while $\rho_0\approx5$ is the noise-marginalized
optimal-statistic HD signal-to-noise ($5\pm1$,
[[sources/arxiv_2306_16213]]). Sec. V already separates them; that a co-author
still asked is the argument for saying so in one more clause.

## [2026-08-15] paper_v2 | MZ first author; abstract reworked; the two SNRs separated

Author order is now MZ, GSP. It had been hand-written in six places; it is now
decided once, in `AUTHORS` in `scripts/_release_files.py`, and the paper, the
README prose, the BibTeX key and block, the CC-BY attribution line,
`pyproject.toml`, `CITATION.cff` and the `ZENODO.md` creator list all derive
from it. **The published Zenodo record still lists GSP first** and needs its
creator order edited by hand or through the API; files are frozen after
publication but metadata is not.

Abstract rebuilt to GSP's structure: four numbered findings, short sentences,
no symbol used without words around it. Dropped: the $\rho_{\rm ps}$ passage
(MZ), and with it $p_1$, $\rho_0$, $\Sigma_{\rm bg}$, $C_1/C_0$ and
$M_{\rm peak}$. "Carried by" and "the anisotropy is one source" were AI-flavoured
and became "produced by"; the prior is now "adopted in the analysis" rather
than described by its truncation. 330 words to 240.

`arxiv/METADATA.txt` held a hand-maintained plain-text copy of the abstract
that had already drifted from the paper. It now records the SHA-256 of the
LaTeX abstract it was written from, and `build_arxiv.sh` refuses to build when
the paper has moved since.

**The two signal-to-noise ratios are now separated in Sec. V.A.** GSP asked why
$\rho_0=5$ rather than $\sim3$. Both numbers are right and describe the same
data: $\rho_0\approx5$ is the noise-marginalized optimal-statistic S/N for
HD-correlated power ($5\pm1$, measured against zero correlation), while the
$3$--$4\sigma$ headline measures HD correlation against a spatially
uncorrelated common-spectrum alternative, a stricter null. Point (i) of that
paragraph already fended off the common-red-noise confusion, which is a
different one; the new sentence names this one. Nothing numerical changed.

## [2026-08-15] release | arXiv package finalised and verified; awaiting upload

Author order (Zaldarriaga, Sato-Polito) and the primary category
(astro-ph.HE) are both settled decisions now, recorded as such in
`arxiv/METADATA.txt` rather than left as open judgement calls. GSP's comments
are incorporated and she does not need another read.

The Zenodo record was checked once more after MZ reordered its creators and
edited its description by hand: creators now Zaldarriaga then Sato-Polito, the
description's free-text citation matches, and DOI, version, licence, the
`isSupplementedBy` link and all seven file sizes are unchanged and still agree
with `release/data/ZENODO.md`. The repository URL is still deliberately absent
from the description, because it would 404 while the repo is private.

`arxiv/METADATA.txt` now ends with a submission checklist, and the tarball was
verified the way arXiv will build it: extracted into an empty directory, no
`.bib` present, `pdflatex` twice against the shipped `.bbl`. Result: 17 pages,
zero TeX errors, zero overfull boxes, zero undefined citations, no `[?]`
marker, both authors in the new order, the Zenodo DOI and the GitHub URL each
appearing twice, GSP's funding line present, and nothing matching the
internal-text greps.

Held until the paper is announced, both because they would point at a private
repository: flipping the repo public, and adding the repository-URL sentence
to the Zenodo description.

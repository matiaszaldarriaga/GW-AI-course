# TODO

Outstanding items across the paper, the code, and the wiki itself.
Format: short description, then link to the artifact. One-liners
preferred; longer discussion goes on the relevant concept or source
page.

## Paper

### paper_v2 open items (2026-08-12) — CLOSED, all 54 decisions implemented

- [x] All 54 open items on `paper_v2` (14 MZ, 14 GS-P, 26 agent-raised) were
  enumerated in [reviews/paper_v2_decisions.html](reviews/paper_v2_decisions.html)
  and annotated in place in `paper_v2/main.pdf`. MZ's decisions came back as
  `paper_v2/data/decisions_2026-08-12.json` and all 54 are applied; no
  annotation survives in the draft. Receipt:
  `intents/paper-v2-decision-implementation_receipt.md`. Release-repo assembly
  (`paper_v2/RELEASE.md`) remains deliberately out of scope.
- [x] MZ-11 adopted: `paper_v2/data/15yr_cw_3d_limits_v4.npz` is tracked with
  its SHA-256, a fetch script and a [[reproducibility]] entry.

### Public release (2026-08-12) — assembled and verified, nothing published

- [x] `release/` is built, and verified end to end in an isolated copy under a
  fresh environment: 37 tests, `all checks pass`, 106-key registry and both table
  sidecars byte-identical, all eleven figures raster-identical, the paper 17
  pages `[final]` with zero errors and no provenance leak, the five forbidden
  greps clean. Assembled only by `scripts/assemble_release.py`; never
  hand-edited. See [[reproducibility]] and
  `intents/paper-v2-release-build_receipt.md`.
- [x] The Fig. 4 legend now reads "3D walk", matching the caption — the one
  outstanding D-09 follow-up, and the only shipped figure that changed.
- [ ] **MZ: create the GitHub repository, create the Zenodo record (reserve the
  DOI on the draft *before* publishing), then run `bash scripts/stamp_doi.sh <doi>`
  and tag `v1.0`.** Nothing remote was created by the build. Exact commands in
  `intents/release-handoff.md`.
- [ ] **DECIDE (MZ): a data availability sentence in the paper.** Drafted in
  `intents/release-handoff.md`, deliberately not inserted — the manuscript text
  is settled and this would be the only change to it. Needs the stamped DOI.
- [ ] **DECIDE (MZ), each defaulted, none blocking:** repository name
  (`pta-gwb-anisotropy`), licence (MIT for code + CC BY 4.0 for the paper),
  Zenodo scope (all six arrays, ~15 GB — or just the 0.93 GB population set),
  and the arXiv primary category (`astro-ph.HE` suggested, flagged in
  `arxiv/METADATA.txt` as a judgement call).

### paper_v2 follow-ups left by the decision-implementation pass (2026-08-12)

- [ ] **Re-check `LinLidzMa:2026b` against ADS before posting.** The entry went
  into `paper_v2/references.bib` under MZ's explicit single-source waiver
  (decision D-02): arxiv and the authors' own tex agree, ADS was JS-gated and
  returned nothing. Re-run `verify-reference` once ADS indexes 2608.09929.
  See [[bibliography]].
- [x] ~~Confirm the Fig. 8 limit curve with its authors.~~ **CLOSED 2026-08-12,
  no email needed.** The $7.4$ vs $8\times10^{-15}$ gap is not a discrepancy:
  they are two documented estimators. `NANOGrav:2023individual` Sec. IV.1 says
  *"the sky-averaging is not done uniformly on the sky, but rather through the
  posterior samples, which in practice results in the all-sky limit being
  biased high"*. The published number is the sky-marginalized 95th percentile
  of the $h_0$ posterior; the npz is the fixed-sky per-position map. The
  published value was then **reproduced exactly** (8.227e-15 in bin 11,
  5.887 nHz, the same bin the paper calls most sensitive) from the same public
  repo's `data/15yr_quickCW_UL.h5` using its own `UL_analysis.ipynb`
  estimator. See [[figures/pixel_amplitude_h0]].
- [x] ~~**DECIDE (MZ): which limit curve Fig. 8 should show.**~~ **CLOSED
  2026-08-12 by MZ: keep the curve that is plotted (the sky average of the
  per-position grid), and do not carry a second number anywhere.** Table II's
  caption previously quoted NANOGrav's published all-sky value
  ($8\times10^{-15}$ near 6 nHz), a different estimator from the one in
  Fig. 8; it now quotes the plotted curve's own value at the table's lowest
  frequency ($1.3\times10^{-14}$, the registered
  `cw_limit_skyavg_f0085`) and names its source exactly. The paper therefore
  contains one continuous-wave limit, from one place. The all-sky reduction
  and the reproduction of the published number are documented in
  [[figures/pixel_amplitude_h0]] for the record only.
- [ ] **Relabel the Fig. 4 legend.** Decision D-09 renamed the black curve from
  "exact" to "the direct full-moment walk" in the caption, but the legend inside
  `figures/c1c0_distribution.pdf` still reads `3D walk (exact)`. The generator
  is `new_montecarlos_codex/generate_sampled_c1c0_distribution.py --replot`,
  which was out of scope for the prose pass (only three figure scripts were
  allowed to change). The caption currently names the legend entry and states
  the approximation, so nothing is wrong in print; fix the label the next time
  that figure is regenerated.

### Sampled-property Monte Carlo integration (2026-07-14) — ready for writer

- [ ] Switch the seven NPZ-driven figures and Tables I--III to the sampled
  results, use the new 3D-walk Fig. 4, and update inline values. The complete
  per-file checklist and LaTeX-ready rows are in
  `new_montecarlos_codex/reports/writer_handoff.md`; canonical wiki summary:
  [[results/sampled_property_monte_carlo]]. Analysis/review work is complete.

### Source-vs-$C_\ell$ rewrite of Secs. 6-7 (2026-06-13) — awaiting author review

- [ ] **Review `paper/sections/source_vs_cl_reduced.tex`** (new, ~850 words) — the suggested reduced replacement for `three_strategies.tex` + `numerical_estimates.tex`. It is now `\input` in `main.tex` as **Sec. VIII**, shown **alongside** the original Secs. VI--VII in the compiled `main.pdf` (12 pages) for comparison. Decide: adopt (replace) / merge / discard.
- [ ] To switch fully to the reduced version: delete the `\input` lines for `three_strategies` and `numerical_estimates` in `main.tex`, then drop the `_v2` suffixes (`eq:hierarchy_v2`→`eq:hierarchy`, `fig:scaling_Np_v2`→`fig:scaling_Np`) in `source_vs_cl_reduced.tex` (the figure label currently lives in `numerical_estimates.tex`).
- [ ] **`Goncharov:2026joint`** is cited in the draft but is NOT in `references.bib` (unpublished). Run `verify-reference` and add once it has an arXiv/ADS record; until then the `\cite` will dangle.
- [ ] **Optional Monte-Carlo figure** (`% [to be generated]` in the draft): on common one-source mock data, compare detection significance of (a) coherent/source matched filter, (b) template-projected power map $a_{LM}\!\cdot\!v(\Omega)$, (c) raw $C_L$ block powers, vs $p$ and $\Sigma_{\rm bg}$ — should show (a)$\approx$(b)$\gg$(c). The notebook-ready formulas are in [[sources/toy_model_source_vs_power_map]] (Secs. 20-21). Write a `paper/scripts/` generator if adopted.
- [ ] `audit-paper-consistency` on the new section's two `\fromnotebook` annotations (source-detection note Secs. 3-10; toy-model note Secs. 12-19).

### `numerical_estimates.tex` (section is mostly unfilled)

- [x] Pin down $\Sigma_{\rm bg}$ from the NANOGrav 15yr detection significance. (resolved 2026-06-24) The per-bin cross-correlation background SNR is now anchored at $\rho_0 \sim 1$ (total HD optimal-statistic SNR $\sim$5 over $\sim$5 signal-bearing bins; `NANOGrav:2023gor`), used in `source_detection.tex` Sec. "The data, and what $\rho_0$ measures".
- [ ] Compute $s_L$ for $L = 1,\ldots,6$ using the exact pair-average formulas. (Values for $N_p=67$ are in `wiki/conventions.md`; the paper needs a table plus derivation pointer.)
- [ ] Explicit coherent SNR$^2 \propto p_1 \cdot \Sigma_{\rm bg}^2$ for the $\varepsilon = 0.66$ model at $f\approx 0.06$/yr.
- [ ] $C_\ell$ Fisher information at the same point, showing it is far below detection threshold.
- [ ] Full table: for each of the three strategies and each $\varepsilon$ model, expected SNR or Fisher info at the lowest frequency.
- [ ] How many factors of $\Sigma_{\rm bg}$ growth are needed for detection in each strategy.

### `nanograv_prior.tex`

- [ ] Table comparing our 95th percentile of $C_1/C_0$ with NANOGrav Figure 1 value.
- [ ] Convergence table: 95th percentile of $C_1/C_0$ at $\ell_{\max}^b = 3, 6, 23, 47, 95$.

### `astrophysical_model.tex`

- [ ] Describe the CDF-based source placement method.

### General

- [ ] Write figure-generation scripts in `paper/scripts/` for every figure (for reproducibility).
- [ ] Decide whether to keep `references/2006.04810/` (unused after today's audit).

## Code

### Dependency rot — will break a fresh environment (found 2026-08-03)

Found while cataloguing this repo for the arg-GW course (`teaching/arg-GW`,
`wiki/references/pta-code-repos.md`). Both verified by running them, not inferred.

- [x] ~~**`gwb_sources/source_detection.py:39` imports `scipy.special.sph_harm`**~~
  **CLOSED 2026-08-12** by the release build. The module now imports `sph_harm_y`
  where it exists and back-ports it onto `sph_harm` where it does not, so it runs
  on either side of the 1.17 removal — a bare floor of `>=1.15` was not an option,
  because it would have broken the reference platform (scipy 1.11.3) that produced
  every registered number. The transposition this entry warned about was verified,
  not assumed: on scipy 1.11.3 the migrated design matrix is **bitwise identical**
  to the original call over 2005 directions × 81 harmonics, and on scipy 1.18.0
  (where `sph_harm` is gone) it agrees to 6e-12 relative with the orthonormality
  invariant holding at 3e-15. $\alpha_{\rm ps}$, $\alpha_1$ and
  $\alpha_{\ell\le2}$ are unchanged and `paper_numbers.json` regenerates
  byte-identically.
- [x] ~~**Pin `scipy` in `environment.yml`**~~ **CLOSED 2026-08-12.** All
  scientific dependencies are now pinned to the exact patch level of the
  reference platform, and PyYAML — which `check_provenance.py` imports and
  nothing declared — was added.
- [x] **`scripts/run_sqrtSH_realizations.py` passed `verbose=False` to `hp.alm2map`**
  — fixed 2026-08-13, before the repository went out for review. Deprecated at
  healpy 1.15 and removed later, so it was a `TypeError` waiting for anyone who
  relaxed the pin, and it shipped: `reproduce.sh` calls this script. The keyword
  only ever controlled logging; removing it was verified to leave the maps and
  the C_l bit-for-bit identical over four seeds, so no committed artifact moved.

### Documentation drift (minor, found 2026-08-03)

- [ ] `README.md` says 13 tests; there are **25** (all passing, 103 s).
- [ ] `wiki/reproducibility.md` says `results/` is ~20 GB; it is **33 GB** on disk. The
  excess is six legacy `*_oldphi.npz` from before the 2026-06-22 amplitude recalibration —
  either delete them or record them in the manifest.
- [ ] `wiki/formulas.md` still records the `paper/` v1 Hellings--Downs normalisation for
  `eq:HD`, while `paper_v2` uses $\Gamma_0 = \tfrac23\Gamma^{\rm HD}$. Harmless today
  because only ratios are used, but it is exactly the kind of live wiki/source
  inconsistency rule 3 exists to catch.
- [ ] `wiki/index.md` records the Goncharov companion's forecast as 0.6%/2% and 24/114 AGN
  candidates; `paper_v2`'s abstract says 2%/5% and 21/114. The companion draft was revised
  and the wiki entry was not. **Also note the companion analyses SIMULATED NG15 data
  throughout** — worth stating wherever those numbers are quoted.

- [x] `gwb_sources/sky_maps.py`: disabled functions — user decision was **keep as-is**; may re-implement later. The `NotImplementedError` messages already point users to `sources.generate_realizations`. No action. (resolved 2026-04-13)

## Wiki

### Phase 2 (md notes, concept pages, paper mirror)

- [x] Ingest all 11 md notes from `references/*.md` → `wiki/sources/` (completed 2026-04-13 via 11-way parallel subagent dispatch).
- [x] Create the 15 concept pages (completed 2026-04-13).
- [ ] Mirror each `paper/sections/*.tex` into `wiki/paper/sec_*.md` with key claims + backlinks. **Still pending.**

### Potential new paper citations surfaced in Phase 2

- [ ] `numerical_estimates.tex`: cite `pta_exact_pair_average` and use its tabulated $s_L$ values for $N_p=67$.
- [ ] `nanograv_prior.tex` or `discussion.tex`: cite `pn_1src_vs_dipole_cov` for the exact $\tau_L$ transfer function and the one-source = dipole equivalence at $\ell=1$.
- [ ] `three_strategies.tex` or introduction: consider citing `pn_coh_vs_quadratic` for the self-contained coherent-vs-covariance derivation.
- [ ] introduction: consider `matched_filter_vs_power` for the general linear-vs-quadratic argument. **Would require adding Rice 1944, Adler 1981, Gross-Vitells 2010, Owen 1996 via `verify-reference` first.**

### `SMBH_population_model` concept page is a stub

~~No md note in `references/` covers the population model directly.~~
Updated 2026-04-13: 9 arxiv papers ingested; concept page substantially
expanded.

- [x] 57% median/mean figure at $\varepsilon=0.66$ confirmed: actual value 0.571 at $f_0=0.085/{\rm yr}$, computed in `notebooks/guide_model_comparison.py` from `results/power_anisotropy_eps066.npz`. Not a paper citation. (completed 2026-04-13)

### Arxiv ingests surfaced 2026-04-13

- [ ] **Run `verify-reference` for Taylor, van Haasteren, Sesana 2020 (arxiv 2006.04810).** Subagent flags high value: earlier independent derivation of sqrt-SH basis (Appendix A) + M=0.98 ORF match between SMBHB sky and isotropy. Add to `paper/references.bib` if verified.
- [ ] Cite [[sources/arxiv_2306_16221]] Fig. 1 caption verbatim in `nanograv_prior.tex` — it is NANOGrav themselves acknowledging that the upper-limit shape is set by the prior.
- [ ] Cite [[sources/arxiv_2306_16221]] Hellinger-distance = 0 statement verbatim in `nanograv_prior.tex`.
- [ ] Consider citing [[sources/arxiv_2312_06756]] missing-BH argument ($M_{\rm peak}\sim 3\times 10^{10}M_\odot$ needed) in `discussion.tex`.
- [ ] Consider citing [[sources/arxiv_2407_14595]] alternate BHMF in `discussion.tex` (contrast with $\varepsilon$-scatter route).
- [ ] Cite [[sources/arxiv_2406_17010]] characteristic-function method and $N_c$ scaling in `astrophysical_model.tex`. This is the paper this project builds on directly; should be cited more heavily than just twice.

### Phase 3 (code, notebooks, results, figures) — complete 2026-04-13

- [x] 10 code pages (7 modules + 3 scripts) under `wiki/code/`.
- [x] 6 notebook pages under `wiki/notebooks/`.
- [x] 12 result pointer pages under `wiki/results/`.
- [x] 5 figure pages under `wiki/figures/`.

### Phase 3 surfaced code-quality items — all addressed 2026-04-13

- [x] `summary_stats.py::alm_summary_statistics` — **not a bug.** Docstring says "(doubled)"; the factor of 2 correctly accounts for the $m=-2$ mirror of the real field (healpy stores only $m\ge 0$). Cleaned `x + x` → `2 * x` and added a comment explaining the physics.
- [x] `sources.py::find_brightest_source_strain` — added `assert np.all(np.diff(strain_bins, axis=1) >= 0)` and documented the monotonicity assumption in the docstring.
- [x] `sources.py::run_realizations` vs `generate_realizations` — **not redundant.** They compute different outputs: `run_realizations` returns 1-D strain statistics; `generate_realizations` builds HEALPix power maps + per-realization ledger. Docstrings now explicitly document which to use when, and the different RNG patterns (shared sequential vs per-realization SeedSequence spawn). No deprecation.
- All tests pass in `gw_pta` env (13/13).

### Paper cross-refs now that Phase 3 is ingested

- [x] Pin down $\Sigma_{\rm bg}$ for NANOGrav 15yr — values now available in [[sources/pta_exact_pair_average]] and [[concepts/s_L_block_weights]].
- [x] Compute $s_L$ for $L=1,\ldots,6$ at $N_p=67$ — already in [[concepts/s_L_block_weights]]. Just needs to be copied into `numerical_estimates.tex`.
- [x] $\ell_{\max}^b$ convergence table — data already in [[results/sqrtSH_realizations_lmax3]] through `nside32`. Just needs to be formatted into `nanograv_prior.tex`.
- [x] Median/mean/$N_{\rm eff}$ per $\varepsilon$ — all confirmed numerically in [[notebooks/guide_model_comparison]].

### arXiv 2608.09929 ingest (2026-08-11) — CLOSED 2026-08-12

Full rationale and suggested LaTeX: [reviews/lin_lidz_ma_2026b_comparison.html](reviews/lin_lidz_ma_2026b_comparison.html).
Settled by decisions D-02, D-07, D-21, D-24 and D-25.

- [x] **(MUST) Rewrite `paper_v2/sections/discussion.tex`** — done (D-24, an
      OTHER: "state what the new version corrects and that we agree on those.
      Just be matter of fact, no judgement just the facts"). The subsection now
      lists the four things their Monte Carlo paper revises and states where
      our results coincide, without framing anything as a concession. The
      drafted replacement in the report was the starting point, not the text.
- [x] **(SHOULD) `\cite{LinLidzMa:2026b}` in `introduction.tex`** — done (D-02).
- [x] **(SHOULD) `verify-reference` for arXiv 2608.09929** — waived by MZ for an
      arxiv-only `@misc` (D-02). Entry added; the ADS re-check is now its own
      open item above.
- [x] (OPTIONAL) Angular-realization variance in `astrophysical_model.tex` —
      taken as option B (D-07): one clause noting that the right panel of
      Fig. 3 is the reciprocal of their per-realization shot noise and that
      the two calculations agree where they overlap. No dex widths quoted, so
      no new registered number.
- [x] (OPTIONAL) Cite their conditioning result — **skipped** (D-25 B): the
      ranking stands on our own results.
- [x] (OPTIONAL) Sharpen `nanograv_prior.tex` — taken as option A (D-21): both
      keys cited in the existing parenthesis, no added commentary.
- [ ] (DEFERRED) Quantify the per-$d\ln f$ → per-PTA-bin correction to their
      numbers. Direction is known (upward at high $f$, bandwidth ratio
      $fT_{\rm obs} = 16.5$ at $f = 1/{\rm yr}$); the magnitude needs their
      population model. Only worth doing if a referee asks for a like-for-like
      overlay of their Fig. 2 on our Fig. 3.

### GS-P comments + style audits (2026-08-11) — all placed in the tex, none acted on

All ten GS-P comments are `\gscomment{}` blocks at their passage in
`paper_v2`, and the audit findings are `\ccnote{}` blocks; build is clean in
both draft and `[final]`. Report:
[reviews/prose_audit_report.html](reviews/prose_audit_report.html).
Nothing below is a fix — these are MZ's decisions for the last pass.

Technical remediation completed before that prose pass:

- [x] Full all-source $Q$, $S_2=nE[w^2]$, $N_{\rm eff}$, direct dipole, and
      ledger/remainder schema; three 10,000-realization models regenerated in
      `results_full_moment_v2/` with old products preserved.
- [x] Figure 8 uses the brightest individual source; all 10,000 realizations
      set its median/95th-percentile curves and only 400 set the scatter dots.
- [x] Detection thresholds use fixed common variates, report batch errors, and
      enforce exact $L=1$ equality.
- [x] High-$\ell_{\max}^b$ values use paired analytic low moments and satisfy
      the documented high-resolution validation sequence.

- [ ] **Resolve whether $\rho_0$ is per bin or band-integrated.** Abstract, intro
      and `sec:sd_setup` give three incompatible values ($\approx5$ band, "order
      unity" per bin, $5/\sqrt5\approx2$, "a few"). Highest-consequence finding:
      the detection conclusion flips depending on the answer.
- [ ] **Reconcile $\rho_{\rm ps}\propto p_1$ (Eq.~25) with "against $p_1$ for the
      coherent fit" (`sec:sd_cl`).** Both scalings are in
      [[concepts/fisher_hierarchy]] but for different searches; the text does not
      separate them, and `sec:sd_bottom` names both in one sentence.
- [x] **Fig.~5 top-20 ledger vs Fig.~3 top-100.** Resolved technically in the
      schema-v2 rerun: both use the same full $S_2/Q^2$ including the explicit
      remainder. The corrected $\varepsilon=0.66$ concentration is 65%/77%; a
      visible `CODE AUDIT` note leaves the caption wording to MZ.
- [ ] Abstract "strictly less sensitive" vs `sec:sd_cl` "the two searches are
      identical" at $L=1$. The body's "never does better than" is what is shown.
- [ ] $\eta$ ($q/(1+q)^2$ vs $\sum_{a\ge2}p_a^2$) and $x$ ($C_1/C_0$ vs
      $(1-\cos\zeta_{ab})/2$) each carry two meanings.
- [ ] Fig.~8 caption says the $\varepsilon=0.66$ median reaches the CW limit;
      Table~II gives median $h_0 = 3.2\times10^{-15}$ vs the $8\times10^{-15}$ limit.
- [ ] Six of eight figures have no model-to-colour key in the caption; Fig.~11
      (exceedance) was rated unreadable from its caption alone. Overlaps GS-P's
      Fig.~7 comment.
- [ ] **30 semicolons** against zero in 19k words of SP&Z's published prose, and
      42% of paragraphs ending on a sentence of $\le12$ words (corpus 25%). The
      cheapest style edit available; splitting the semicolons also shortens the
      sentence-length tail.
- [ ] Equation connective prose: median gap 30 words vs the corpus's 45, and a
      run of six equations in `sec:cl` with $<20$ words between each. **Do not**
      add derivations wholesale — assertion rate is 69% in both.
- [ ] Consider adding the naming ledger rule (one object, one name) to
      [[conventions]]; it would have caught the $\eta$ and $x$ collisions.

### Lint items to run periodically

- [ ] `audit-paper-consistency`: for each `\fromnotebook{…}`, check that the nearby paper claim matches the cited note section.
- [ ] Orphan source pages: any `wiki/sources/*.md` that no `wiki/concepts/*.md` links to is under-utilized.
- [ ] Orphan concept pages: any concept not referenced from at least one paper section page or source page.
- [ ] Broken wiki links.
- [ ] Unused bib entries (keys in `references.bib` with no citation in `paper/sections/`).

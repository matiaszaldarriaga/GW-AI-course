# PTA Anisotropy Wiki — Index

> This is a real project wiki, copied for the course from the working notes behind
> Zaldarriaga & Sato-Polito, *Anisotropies in the PTA gravitational wave background*.
> It is here so you can see what one looks like after a year of use, and find out
> whether an agent reads it. The `reviews/` section of the original is not included;
> nothing else was changed.

Content-oriented catalog of everything the LLM has learned about this
project. Read this first; drill into pages as needed. Pages use
Obsidian-style wiki links: `[[page]]`.

## Utility

- [[environment]] — conda env setup for collaborators (via `environment.yml`)
- [[reproducibility]] — what's not tracked and how to rebuild it
- [[conventions]] — notation contract, sign choices, non-negotiables
- [[formulas]] — master equation list with canonical concept owners
- [[bibliography]] — verified bib entries + reverse citation index
- [[todo]] — outstanding TODOs, unresolved questions, numerical gaps
- [[log]] — chronological record of ingests, queries, lints

## Concepts (15 pages)

Core physical/statistical ideas. Each page is canonical for its topic.

### Central observables

- [[concepts/Cl_over_C0]] — the angular power ratio, exact formulas, mean and variance
- [[concepts/N_eff]] — effective source count, inverse participation ratio
- [[concepts/brightest_source_fraction]] — $p$, the paper's headline parameter
- [[concepts/dipole_distribution]] — four semi-analytic approximations for $C_1/C_0$ pdf
- [[concepts/shot_noise]] — Lin, Lidz, Ma $4\pi/N_{\rm eff}$ floor

### Detection theory

- [[concepts/fisher_hierarchy]] — the $p, p^2, p^4$ KL scaling hierarchy (central result)
- [[concepts/KL_divergence]] — chosen figure of merit
- [[concepts/coherent_vs_incoherent]] — mean vs covariance; qualitative distinction
- [[concepts/source_background_degeneracy]] — coherent exact block-diagonal; incoherent $\sim 1/\sqrt{N_p}$
- [[concepts/matched_filter_vs_power]] — general linear-beats-quadratic argument

### PTA-specific formalism

- [[concepts/s_L_block_weights]] — block Fisher weights, tabulated for $N_p=67$
- [[concepts/transfer_function]] — exact $\tau_L$ kernel source-sky → pulsar-map
- [[concepts/sqrt_SH_basis]] — NANOGrav prior, truncation $\ell_{\max}^b = \ell_{\max}^a/2$
- [[concepts/prior_sensitivity]] — nuisance-volume bias in incoherent searches

### Population context

- [[concepts/SMBH_population_model]] — $\varepsilon$ scatter, $M$–$\sigma$, mass function

## Sources (36 pages)

### Companion drafts (by project authors)

- [[sources/draft_sufficient_statistics_2026]] — Sato-Polito, Zaldarriaga, Zackay 2026 (draft). Sufficient-statistic framework: $a_{\ell m}$, $b_{\ell m}$ as compressed PTA data; $N_s^{\rm eff}\sim 3$ for NG15.
- [[sources/joint_search_resolved_unresolved]] — Goncharov, Sato-Polito, Bi, Zaldarriaga 2026 (companion observational paper, MZ co-author, now on arXiv:2606.18241, cited by the paper). Joint hierarchical GWB+CW likelihood; $N_{\rm c}$ as the SMBHB-origin detection statistic. NG15: $N_{\rm c}$ consistent with 1000, no resolvable CW, 21/114 AGN candidates in tension; SNR-5 CW detection probability 2% (15yr)/5% (20yr). **Empirical realization of the coherent top rung of the $p/p^2/p^4$ hierarchy** — the backbone of the rewritten Secs. 6-7.
- [[sources/pn_appendixB_coherent_vs_covariance]] — ChatGPT pedagogical note critiquing App. B of the draft; source of $t_\ell$ vs $T(\hat n)$ separation and $\partial C/\partial\mu|_0=0$ argument.
- [[sources/pn_coherent_vs_stochastic_single_source]] — pedagogical note (2026-04-20): single-template toy proves coherent-model and stochastic-model profile LLRs are monotone-equivalent ($T_{1^\star} = s - 1 - \ln s$ vs $T_1 = s$), so stochasticization is **not** lossy at the detection stage. The $\alpha$ vs $\alpha^2$ KL scaling is a **physics** statement (what generates the data), not a modeling one.
- [[notes/app_B_2pol_equivalence_check]] — P1 calculation: the monotone equivalence extends to App. B's $k=2$ polarization toy limit with $T_{1^\star} = \max(s-2-2\ln(s/2),0)$, and survives sky-direction maximization.
- [[notes/app_B_anisotropic_response]] — P2 calculation: for realistic $U^\dagger N^{-1}U$ the equivalence breaks (eigenvalue spread → different reweighting of $|v_i|^2$), but quantitatively mildly (10–20% rank disagreement, few-percent p-value shift).
- [[notes/app_B_coherent_fisher_critique]] — our unified critique memo (rev. 2026-04-20, Phase-3 refactor). Headline: Eq. (B6) is the correct statistic; stochasticization is free at the detection stage in the App. B toy limit (monotone equivalence); the single scaling-level critique is the Eq. (50) same-power null, which caps the significance at $\sim 3.8\sigma$ ($p[\chi^2_4 > 24] = 7.99\times 10^{-5}$). Two side observations: parameter-precision differences (Fisher on $\mu$ vs $q$, with two distinct mode counts $k=2$ and $1/f_\sigma=12$) and mild anisotropic-response breakdown.

### Pedagogical notes (15, ingested 2026-04-13 / 2026-04-24)

**Currently cited by the paper:**

- [[sources/pn_C1_over_C0]] — 4 citations. Canonical for $C_1/C_0$ formulas and dipole distribution.
- [[sources/pn_coh_vs_incoh_fisher]] — 3 citations. Canonical for the Fisher hierarchy.
- [[sources/pta_1src_vs_CL]] — 2 citations. Canonical for the $p^4$ bug fix.
- [[sources/fisher_src_vs_bg_degeneracy]] — 2 citations. Canonical for exact coherent block-diagonality.

**Not yet cited (candidates for paper use):**

- [[sources/pn_coh_vs_quadratic]] — self-contained coherent-vs-cov; pulsar-map dipole $p^2/4$.
- [[sources/pn_1src_vs_dipole_cov]] — exact $\tau_L$ transfer; 1-source = dipole after compression.
- [[sources/pta_exact_pair_average]] — exact $s_L$ values for `numerical_estimates.tex`.
- [[sources/pta_noise_dominated_limit]] — companion with $\Sigma_{\rm bg}^2$ derivation.
- [[sources/pta_1src_vs_cls_toy]] — toy Fisher; dipole captures only $\sim 43\%$ at $N_p=67,\,L\le 6$.
- [[sources/matched_filter_vs_power]] — general linear-vs-quadratic model. References not in bib.
- [[sources/pta_prior_sensitivity]] — nuisance-prior bias toy models.
- [[sources/spectral_variance_convergence]] — why spectral cv doesn't converge for heavy-tailed populations (2026-04-14).
- [[sources/pta_orthogonal_coordinates]] — orthogonal coordinates for PTA common-process fits; CURN-HD split, Fisher diagonalization (2026-04-15).
- [[sources/pn_HD_vs_CURN_Fisher_Bayes]] — Bayesian HD-vs-CURN as a shape test at fixed common auto-power; $C(\eta)=N+\Phi\otimes[I+\eta(\Gamma-I)]$; $D_{\rm KL}\simeq\tfrac12 F_{\eta\eta}$ at $\eta=0$; corrects "HD on top of CURN" framing (2026-04-24).
- [[sources/pta_curn_hd_cross_only]] — cross-only HD quadratic estimator derived as nuisance-projected HD Fisher score in the $(P, B)$ parametrization $C = N + PI + BX$; $F_{PB}=0$ exactly; physical boundary $P \ge B$ adds $\log\Phi((\hat P - B)/\sigma_P)$ term that matters when $(n-1)\overline{X^2} < 1$ (2026-04-24).

**New (2026-06-13) — the source-vs-$C_\ell$ detection-theory pair:**

- [[sources/pta_source_detection_likelihood]] — **canonical** PTA-native derivation of five detection likelihoods for one source + isotropic background. Corrects the hierarchy: coherent and source-subspace projector covariance ($I+\eta\Pi$, profiled LR $g_r(T_{\rm coh})$) are **monotone-equivalent** ($\propto p$, same threshold); the $p^2$ object is the one-source power-map $T_{\rm psrc}$; $T_{\rm map}=s^TF^{-1}s$ adds an $m$-dof penalty; $D_{C_L}\propto p^4$. Source-power-sky identity $C_L^P/C_0^P=p^2$ (response-free).
- [[sources/toy_model_source_vs_power_map]] — self-contained Gaussian toy (**notebook-ready**): Bayesian-evidence face of the hierarchy. One-source models SUM over locations ($1/N$ look-elsewhere); map/$C_\ell$ models MULTIPLY over pixels. Averaged $C_\ell$ evidence $=b_{\rm cov}(s;V_1)$, but typical log-evidence is penalized by $\ell_0(q)<0$ per empty pixel. Substrate for the proposed Monte-Carlo figure.

**New (2026-06-23) — the operational rewrite of the detection section:**

- [[sources/pta_point_source_multipole]] — **canonical** for Sec. VI. Frames detectability via $\rho_0$, $p_1$, resolution $L$: coherent source SNR $\rho_{\rm ps}=\sqrt5\,p_1\rho_0$; the $C_\ell$-vs-coherent-scan penalty is **modest** (1.1–1.4× over $L=1$–6, exactly 1 at $L=1$), reconciling with the $p^4$/$\sigma_p$ estimation penalty (different question). Numerically verified (28/28).

**Off-topic (parked in references/, not part of this project):**

- [[sources/gw231123_likelihood_islands]] — ground-based GW parameter-estimation likelihood geometry (heavy, high-SNR, merger-dominated GW231123-style event): why few cycles + high SNR + higher modes/precession give narrow isolated posterior islands. Unrelated to PTA anisotropy; not cited by the paper.

### Arxiv papers (10; 9 ingested 2026-04-13, 1 on 2026-08-11)

**Currently cited by the paper:**

- [[sources/arxiv_2306_16213]] — NANOGrav 15yr GWB evidence. Provenance of the $\rho_0\approx5$ anchor (noise-marginalized optimal-statistic HD S/N, $5\pm1$).
- [[sources/arxiv_2306_16221]] — NANOGrav 15yr anisotropy. Target of critique #1.
- [[sources/arxiv_2306_16222]] — NANOGrav 15yr individual-source (CW) Bayesian limits. Deepest $h_0=8\times10^{-15}$ benchmark for Fig. 8 / Table II.
- [[sources/arxiv_2602_16808]] — Lin, Lidz, Ma. Target of critique #2.
- [[sources/arxiv_2608_09929]] — **Lin, Lidz, Ma 2026b (new, 2026-08-11).** Monte Carlo sequel to the above. Their $\hat C_{\rm shot}/4\pi = \sum_a p_a^2$ is our ledger $1/N_{\rm eff}$; they retract the $\langle h^4\rangle/\langle h^2\rangle^2$ estimate ($130\times$ high at $f=1/{\rm yr}$) and the $f^{8/3}$ scaling, conceding our mean-vs-median critique. Our prior-content and detection-hierarchy critiques stand. **Not yet cited — `discussion.tex` needs a rewrite before posting.**
- [[sources/arxiv_2103_00826]] — Banagiri et al. LISA. Origin of sqrt-SH basis.
- [[sources/arxiv_2312_06756]] — Sato-Polito, Zaldarriaga, Quataert. Population model with missing-BH argument.
- [[sources/arxiv_2406_17010]] — Sato-Polito & Zaldarriaga 2025. Direct precursor of this project.
- [[sources/arxiv_2407_14595]] — Liepold & Ma. Alternate GSMF-based BHMF.
- [[sources/arxiv_2305_05690]] — Sato-Polito & Kamionkowski. Analytical $C_\ell$ from SMBHBs.
- [[sources/arxiv_2407_06270]] — Lamb & Taylor. Spectral variance moments.

**Not cited (recommended for bib):**

- [[sources/arxiv_2006_04810]] — Taylor, van Haasteren, Sesana 2020. Earlier independent sqrt-SH derivation; M=0.98 ORF match between SMBHB sky and isotropy.

## Code (11 pages plus batch-script pages)

### `gwb_sources/` package

- [[code/gwb_sources_init]] — public API surface; 27 exports from 6 submodules
- [[code/gwb_sources_population]] — VDF, $M$–$\sigma$, BHMF, luminosity function
- [[code/gwb_sources_sources]] — Poisson sampling, CDF source placement, single-RNG invariant
- [[code/gwb_sources_power_anisotropy]] — `compute_power_cls`, statistics, I/O
- [[code/gwb_sources_full_moment_schema]] — strict schema-v2 $Q$, full $S_2$,
  direct dipole, complete-ledger/remainder product contract
- [[code/gwb_sources_sky_maps]] — Hellings-Downs, antenna patterns; three functions disabled
- [[code/gwb_sources_strain_stats]] — FFT-based characteristic-function PDF of $h_c^2$
- [[code/gwb_sources_summary_stats]] — rotation-based per-realization summary statistics
- [[code/gwb_sources_source_detection]] — $\alpha_{\rm ps}=\sqrt5$,
  $\alpha_L$, fixed/common-variate scan-vs-$C_\ell$ thresholds with batch
  errors and exact $L=1$ equality, NP equivalence (8 unit tests)

### Batch scripts

- [[code/scripts_run_population]] → writes `results/population_analysis_eps*.npz`
- [[code/scripts_run_power]] → writes `results/power_anisotropy_eps*.npz`
- [[code/scripts_run_sqrtSH]] → writes `results/sqrtSH_realizations*.npz`

## Notebooks (6 pages, ingested 2026-04-13)

- [[notebooks/guide_population_and_spectra]] — SMBH population walkthrough at $\varepsilon=0.66$; $N_c$ values across frequency bins
- [[notebooks/guide_model_comparison]] — three-model $\varepsilon$ scan; verified median/analytic-mean ratio = 0.571 at $\varepsilon=0.66$
- [[notebooks/guide_power_anisotropy]] — $C_\ell/C_0$ analysis, top-$N$ exclusion, $N_{\rm eff}$ scatter
- [[notebooks/guide_sqrtSH_model]] — sqrt-SH prior validation; reproduces NANOGrav Fig. 1; $\ell_{\max}^b$ non-convergence
- [[notebooks/guide_dipole_analytics]] — 3D walk validation, four semi-analytic approximations, $\sim 100\times$ speedup
- [[notebooks/guide_interactive]] — CDF-based fast realizations ($\sim 0.5$ s / 1 K); all sliders; cited `astrophysical_model.tex:50,65`, `numerical_estimates.tex:34`

## Results (13 pointer pages)

- [[results/sampled_property_monte_carlo]] — **2026-08-11 full-moment
  remediation**: preserved pre-fix arrays plus versioned schema-v2 products,
  complete source ledgers/remainders, direct dipoles, and the common-run
  paper-v2 rebuild. At the lowest frequency the corrected median
  $N_{\rm eff}$ values are 1167.0/181.6/18.9, with all model orderings and
  claim-scale conclusions preserved.

### Population realizations

- [[results/population_analysis_eps020]] · [[results/population_analysis_eps038]] · [[results/population_analysis_eps066]]
  — 10K realizations each, 44 frequency bins, 2.3 GB per file. Consumed by `guide_population_and_spectra`, `guide_model_comparison`.

### Power anisotropy realizations

- [[results/power_anisotropy_eps020]] · [[results/power_anisotropy_eps038]] · [[results/power_anisotropy_eps066]]
  — 10K realizations, HEALPix maps, `cls_all` + 4 exclusion levels. Consumed by `guide_power_anisotropy`, `guide_model_comparison`, `guide_dipole_analytics`.

### Sqrt-SH prior samples

- [[results/sqrtSH_realizations_lmax3]] — 97.5th-pct $C_1/C_0 = 0.233$ (NANOGrav-faithful)
- [[results/sqrtSH_realizations_lmax6]] — 97.5th-pct = 0.101
- [[results/sqrtSH_realizations_nside8]] — 97.5th-pct = 0.010
- [[results/sqrtSH_realizations_nside16]] — 97.5th-pct = 0.003
- [[results/sqrtSH_realizations_nside32]] — 97.5th-pct = 0.0007
- [[results/sqrtSH_realizations]] — legacy run

**$330\times$ spread between `lmax3` and `nside32`** is the direct numerical proof that the NANOGrav "constraint" is set entirely by $\ell_{\max}^b$.

## Figures (11 pages)

All 11 paper figure scripts share a common look via `paper/scripts/_paperstyle.py` (NEW 2026-06-24, untracked): `apply_style()` (serif + cm mathtext), `figsize_1col`/`figsize_2col`, and the canonical color/style dicts (`EPS_COLORS`, `METHOD_COLORS`, `STRATEGY_COLORS`, `FREQ_STYLES`, `LW`).

- [[figures/mass_function_kernel]] — SMBH mass function + power kernel, 3 $\varepsilon$ values
- [[figures/strain_spectrum_models]] — Fig. 2: **raw** $h_c^2(f)$, all models matched at $f=1$/yr so the means coincide (normalization check); median exposes the heavy tail (**rewritten 2026-06-22**)
- [[figures/c1c0_neff_vs_freq]] — Fig. 3: direct $C_1/C_0$ and full-moment $N_{\rm eff}=Q^2/S_2$ vs frequency, 3 models (**schema-v2 all-source update, 2026-08-11**)
- [[figures/c1c0_distribution]] — Fig. 4: $C_1/C_0$ pdf; all four approximations overlaid. Paper version uses a **log** y-axis (`c1c0_distribution.pdf`); the generator also writes a linear-axis alternative `c1c0_distribution_linear.pdf` (standalone generator, 2026-06-22; log/linear split 2026-06-24)
- [[figures/p1_distributions]] — Fig. 5: complete-ledger $p_1$ and the
  brightest source's share $w_1^2/S_2$ of the full anisotropy moment
- [[figures/source_content_estimators]] — Fig. 6: $\langle p_1\mid x\rangle\simeq\sqrt{x}$, $\langle N_{\rm eff}\mid x\rangle\simeq1/x$; pools all frequency bins within each model and tests their approximate collapse over the calibrated family (**full-moment update 2026-08-11**)
- [[figures/p1_neff_conditional]] — Fig. 7: $P(p_1\mid C_1/C_0)$ and $P(N_{\rm eff}\mid C_1/C_0)$ given a large dipole; MC vs importance-reweighted prediction
- [[figures/pixel_amplitude_h0]] — Fig. 8: brightest individual-source
  $h_0$ from all 10,000 realizations; only scatter uses 400 points. The
  verified deepest NANOGrav value is a single star, not a band-wide line.
- [[figures/exceedance_probability]] — $P(C_1/C_0 > \mathrm{threshold})$ vs frequency; critical for the NANOGrav-prior argument
- [[figures/source_snr_vs_resolution]] — Sec. VI: source SNR $\alpha_L$ retained vs angular resolution; $\to\sqrt5$ asymptote (**new 2026-06-23**)
- [[figures/cl_vs_scan_penalty]] — Sec. VI: the $C_\ell$-vs-coherent-scan amplitude penalty (analytic + MC) and required $p_1$ vs $\rho_0$ (**new 2026-06-23**)

## Paper mirror

- **`paper_v2/` (2026-07-14)** — restructured writer draft on the
  sampled-property Monte Carlos; provenance map in `paper_v2/README.md`,
  rationale and verified numbers in the [[log]] entry of the same date.
  `paper/` retained unchanged for side-by-side adversarial review.
  decision console**: all 54 open items on `paper_v2` in document order (14 MZ,
  14 GS-P, 26 DECIDE), each with the note as it prints in the annotated PDF, a
  suggested resolution, concrete options and a decision control; decisions are
  exported as Markdown/JSON. Built by
  `paper_v2/scripts/build_decision_console.py` from
  `paper_v2/data/comment_inventory.json` + `decision_items.json`.
  **Closed 2026-08-12**: MZ's export is
  `paper_v2/data/decisions_2026-08-12.json` (48 A, 3 B, 3 OTHER) and all 54 are
  implemented, so no annotation remains in the draft. The one scientific change
  and the full per-id table are in
  `intents/paper-v2-decision-implementation_receipt.md`; see also the [[log]]
  entry of that date.
  blind-comprehension read + voice grading**: what a referee with only the
  manuscript cannot follow (the $\rho_0$ per-bin/band ambiguity, the
  $p_1$-vs-$p_1^2$ KL tension, the top-20/top-100 ledger split), the 18-test
  fingerprint derived from SP&Z's own papers, and the reusable process.
  Companion tool: `scripts/prose_audit.py`.
  report on arXiv:2608.09929**: what changed from their previous claims, the
  head-to-head number table, four discrepancies, and a prioritized six-item
  draft-change list with suggested LaTeX.
  — self-contained BASELINE-versus-schema-v2 paper review with all registered
  numbers, distributions, figures, tables, annotated pages, hashes, commands,
  run metadata, and claim-aware flags.
  referee report on `paper_v2/`** (style vs SP&Z, provenance audit,
  logic flow, figure/caption audit); top-10 action list for the writer.

_Still pending:_ one page per section with key claims and backlinks.

## Decks

_Empty. Author on demand via `deck-build` workflow._

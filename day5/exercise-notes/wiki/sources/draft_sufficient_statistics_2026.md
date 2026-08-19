# Sufficient statistics for pulsar timing arrays (draft 2026-04-16)

**Source:** `references/sufficient_statistics_4-16-2026.pdf` (draft PDF, 15 pages)
**Authors:** Gabriela Sato-Polito¹, Matias Zaldarriaga¹, Barak Zackay²
  ¹ IAS Princeton   ² Weizmann
**Type:** companion paper / draft manuscript by project authors (not on arxiv as of ingest)
**Status:** draft with in-line `[GSP: ...]` co-author annotations; figure captions partially stubbed ("FIG. 2. Caption")
**Ingested:** 2026-04-16

## Summary

Proposes the Earth-term and pulsar-term spherical-harmonic coefficients
$a_{\ell m}$ and $b_{\ell m}$ as a **sufficient summary statistic** for PTAs:
a compression of the full timing-residual data from which all standard
analyses (isotropic SGWB, anisotropic SGWB, template-based continuous-wave
searches) can be derived. Applies the framework to NANOGrav 15yr and
derives the effective number of resolvable GW sources, the optimal test
statistic for distinguishing an individual source from a GWB, and the
maximum possible detection significance from marginalized matched filtering.

The paper is a natural companion to the anisotropy-hierarchy project: it
provides the formal information-theoretic scaffolding for the qualitative
claim that all PTA analyses are variants of the same underlying likelihood,
and rigorously establishes the equivalence between template-based and
anisotropic single-source searches.

## Structure

- **§I Introduction** — motivates summary statistics as a compression.
- **§II PTA likelihood** — likelihood for $d_i = z_{i,e} + z_{i,p} + n_i$
  with pulsar-term marginalized (Eqs. 1–10); introduces $a_{\ell m}$, $b_{LM}$,
  $\sigma_h^2$ (the monopole of the pulsar-term variance map).
- **§III Earth and pulsar term maps**
  - **A. Spherical harmonic coefficients** — single-source maps, CG
    coupling (Eq. 18), specific values $b_{00}=\sqrt{4\pi}$,
    $b_{10}=(\sqrt 3/2)b_{00}$, $b_{20}=(\sqrt 5/10)b_{00}$, and
    $C_1=C_0/4$, $C_2=C_0/100$ (Eq. 23).
  - **B. Fisher matrix** — per-multipole SNR for $a_{\ell m}$ and $b_{\ell m}$
    (Eqs. 29–36); noise-dominated vs signal-dominated scalings.
  - **C. Sensitivity** — applies to NANOGrav 15yr using `hasasia`;
    $\rho_{HD}=3.14$ consistency check; $N_p^{\rm eff}\sim 7$ single-freq.
- **§IV Case study: resolving GW sources**
  - **A. Number of sources** — eigenvalue decomposition of source-amplitude
    Fisher matrix; defines $N_s^{\rm eff} = \tfrac12\sum_i \lambda_i/(\lambda_i+\alpha)$
    (Eq. 46). For NANOGrav 15yr: $N_s^{\rm eff} \sim 3$.
  - **B. Distinguishing sources from a GWB** — Neyman–Pearson test statistic
    $t_\ell = (|a_{\ell 2}|^2 + |a_{\ell -2}|^2)/\sum_m |a_{\ell m}|^2$;
    ROC curves for targeted vs blind searches at $N_p=25,150$, $\varepsilon=0,0.2$.
    Establishes that maximum possible matched-filter significance from a
    phase-marginalized Gaussian likelihood is $\sim 3.8\sigma$
    (from $p[\chi_4^2 > 2/f_\sigma = 24]$, $f_\sigma=1/12$).
- **Appendix A** — quantifies Gaussian approximation for single-source
  pulsar-term likelihood; Edgeworth expansion; KL divergence to the
  Gaussian $\propto \varepsilon^4/(1+\varepsilon)^4 \cdot 1/N_p^2$.
- **Appendix B** — derives the optimal likelihood-ratio test statistics
  $\ln\Lambda$ for Earth and pulsar terms separately.

## Key equations

| # | Equation | Where it matches our wiki |
|---|---|---|
| 8 | Pulsar-marginalized per-pulsar likelihood | Consistent with [[../concepts/source_background_degeneracy]] |
| 9 | Full likelihood in $(a_{\ell m}, b_{\ell m})$ | Foundation for all analyses |
| 12 | Single-source Earth-term map $z_e^1(\theta,\phi) = (1+\cos\theta)/4 \cdot [h_2 e^{2i\phi} + h_{-2} e^{-2i\phi}]$ | New canonical form |
| 15 | Single-source $a_{\ell m}$: nonzero only for $m=\pm 2$ | [[pta_1src_vs_CL]] conclusion |
| 16 | HD spectrum $C_\ell = 3 z_\ell^2/[2(2\ell+1)]$ for single source | Matches [[pn_C1_over_C0]] |
| 18 | $b_{LM}$ in terms of $a_{\ell m} a^*_{\ell' m'}$ via Wigner 3-j | CG coupling underlying [[../concepts/sqrt_SH_basis]] |
| 23 | $C_1 = C_0/4$, $C_2 = C_0/100$ for single source (pulsar-term) | Exact match to our [[pta_1src_vs_CL]] and [[../concepts/Cl_over_C0]] |
| 36 | Fisher matrix for $C_\ell$: $F_{\ell\ell'} = \mathrm{Tr}[\Sigma^{-1}\partial\Sigma/\partial C_\ell \cdots]$ | Standard; used for NANOGrav consistency check |
| 38 | $\rho_{HD}^2 = \sum_{\ell\ell'} C_\ell F_{\ell\ell'} C_{\ell'}$ | HD detection significance |
| 39 | Low-SNR approximation $\rho_{HD}^2 = (2\rho_e^2)^2 \cdot 9\kappa/4$ with $\kappa = \sum_\ell 2(2\ell+1)/[(\ell+2)(\ell+1)\ell(\ell-1)]^2$ | New canonical form (ell=2 carries 94% of total) |
| 46 | $N_s^{\rm eff} = \tfrac12 \sum_i \lambda_i/(\lambda_i + \alpha)$ | New concept: effective resolvable sources |
| 49 | $t_\ell = (|a_{\ell 2}|^2 + |a_{\ell -2}|^2)/\sum_m |a_{\ell m}|^2$ | Test statistic from Kamionkowski-Land-Magueijo "axis of evil" formalism (Ref. [15]) |
| A11 | $D_{\rm KL}[q\|p] = (3/32)\varepsilon^4/(1+\varepsilon)^4 \cdot 1/N_p^2$ | Gaussian approximation error |

## Quantitative results for NANOGrav 15yr

- **HD detection significance** using 67-pulsar NG15 configuration + reported noise:
  $\rho_{HD} = 3.14$, marginalized $\rho_2 = 1.74$ (at $\ell_{\max}=5$),
  $\rho_2 = 2$ (at $\ell_{\max}=2$). Consistent with published Bayes-factor.
- **Effective number of pulsars** per frequency bin: $N_p^{\rm eff} \sim 7$
  (peak, single frequency). Four most-sensitive pulsars called out by name:
  **J1713+0747, J1909-3744, B1937+21, J1640+2224**.
- **Effective number of resolvable GW sources**: $N_s^{\rm eff} \sim 3$
  for $N_p=150$, $\varepsilon=0.2$. This **saturates** as the true $N_s$ grows,
  because source templates become degenerate ("large beam of the telescope").
- **Maximum matched-filter significance** (distinguishing single source
  from GWB at equal total power): $\sim 3.8\sigma$ under $p[\chi_4^2 > 24]$,
  from $f_\sigma = 1/12$ in Eq. 48. **Intrinsic ceiling**: cannot be
  improved by lowering noise.
- **Mode coupling correlation coefficients** between $C_2$ and $C_{0,1,3}$
  in NG15: $-0.45$ to $-0.2$ (from survey-window anisotropy).

## Concepts touched (wiki backlinks)

- [[../concepts/matched_filter_vs_power]] — **primary validation**.
  The paper explicitly states "there is no distinction between continuous-wave
  and anisotropic searches" after Gaussian marginalization (§IV.B, near Eq. B4).
- [[../concepts/Cl_over_C0]] — single-source pulsar-term $C_\ell$ pattern
  (Eq. 23) matches the wiki convention.
- [[../concepts/sqrt_SH_basis]] — rigorously grounds the $b_{LM}$ coefficients
  as the natural basis for the pulsar-term variance map; Eq. 18's CG coupling
  is exactly what underlies the Banagiri $\ell_{\max}^b = \ell_{\max}^a/2$ rule.
- [[../concepts/fisher_hierarchy]] — §III.B+§IV provide rigorous Fisher-matrix
  derivations in the sufficient-statistic basis; $\rho_{HD}^2 \propto \rho_e^4$
  (Eq. 39) is the $p^4$ scaling of the $C_\ell$-only strategy, from a
  different starting point.
- [[../concepts/N_eff]] — both $N_p^{\rm eff}$ (Eq. 35) and
  $N_s^{\rm eff}$ (Eq. 46) are new effective-count definitions; the latter
  is a novel concept worth promoting to a concept page if it gets cited.
- [[../concepts/KL_divergence]] — used in App. A for the Gaussian-approximation
  error, and in §IV.A (Eq. 42) to determine $\ell_{\max}$ via
  $D_{KL}[p\|p_{\ell_{\max}}] = N_p^{\rm eff}\sum_{\ell > \ell_{\max}}(2\ell+1)C_\ell$.
- [[../concepts/coherent_vs_incoherent]] — Appendix B derives optimal test
  statistics for Earth (coherent, linear in $a_{\ell m}$) vs pulsar
  (incoherent, dipole of $b_{LM}$) terms; explicit rank-1 structure.
- [[../concepts/transfer_function]] — §III.B's pulsar-term Fisher matrix
  includes the mode-coupling matrix $U C U^\dagger$ (Eq. B5) that generalizes
  the exact $\tau_L$ kernel.
- [[../concepts/brightest_source_fraction]] — implicit via the small
  $N_s^{\rm eff}$ for NG15 and via $\varepsilon = |z_{1,e}|^2/(2\sigma_N^2)$
  as "the relevant parameter controlling deviations from Gaussianity" (App. A).
- [[../concepts/prior_sensitivity]] — targeted vs blind ROC differences
  (Fig. 6) are a precise quantification of the priors-matter argument.

## Relation to this project

**Strong alignment:**

1. **Equivalence of template-based and anisotropic searches.** The paper's
   Appendix B rigorously establishes this equivalence by marginalizing the
   template over pulsar-term phase and obtaining a non-diagonal Gaussian
   covariance — which is *exactly* the signal covariance of an anisotropic
   search. This is the formal statement of our project's claim that
   "searching for individual sources in PTA observations is analogous to
   searches for 'anomalies' in the CMB" (cited to Kamionkowski-Land-Magueijo,
   de Oliveira-Costa-Tegmark-Hamilton).

2. **$C_1/C_0 = 1/4$, $C_2/C_0 = 1/100$ for single source** (Eq. 23):
   numerical values match our [[pta_1src_vs_CL]] and
   [[../concepts/Cl_over_C0]]. Cross-check passes.

3. **Small effective number of resolvable sources** ($N_s^{\rm eff} \sim 3$
   for NG15) is the information-theoretic statement of our project's
   argument that PTAs resolve at most a handful of SMBHBs — not a
   continuum requiring $C_\ell$ maps.

4. **Maximum matched-filter significance $\sim 3.8\sigma$** sets a
   hard ceiling on single-source detectability for the phase-marginalized
   Gaussian likelihood. Not something our project discussed; potentially
   useful number for the discussion section.

**Complementary framing:**

- Our project quantifies the **KL hierarchy in the brightest-source
  fraction $p$**: $D_{\rm coh} \propto p$, $D_{\rm inc} \propto p^2$,
  $D_{C_\ell} \propto p^4$.
- This paper quantifies the **Fisher matrix and SNRs for the sufficient
  statistics** in both signal- and noise-dominated limits, with explicit
  ROC curves and NANOGrav 15yr numbers. Different, but compatible, lens.

**Useful novel definitions for our paper:**

- $\rho_{HD}^2 = (2\rho_e^2)^2 \cdot 9\kappa/4$ with $\kappa \approx 5/576$
  at $\ell=2$ (94% of total, Eq. 39 + table). Makes the $p^4$ scaling
  explicit in a different basis.
- $N_s^{\rm eff}$ (Eq. 46) as a dimensionless figure of merit for how many
  sources a given PTA can resolve.

## Cited external references (potential bib additions)

Not yet in our `paper/references.bib`; cross-check before adopting:

- **Roebber & Holder 2016** (`arXiv:1609.06758`) — "Harmonic space analysis
  of pulsar timing array redshift maps." Heavily cited as [7] for the $a_{\ell m}$,
  $b_{LM}$ formalism. Central methodological reference.
- **Hotinli, Kamionkowski, Jaffe 2019** (`arXiv:1904.05348`) — anisotropy search
  in PTAs. Cited as [8].
- **Hazboun, Romano, Smith 2019** (`arXiv:1907.04341`) — realistic sensitivity
  curves, used for noise modeling via `hasasia`. Cited as [9].
- **Tegmark 1997** (`arXiv:astro-ph/9611174`) — CMB power spectra without
  information loss. Cited as [10].
- **van Haasteren et al. 2009** (`arXiv:0809.0791`) — measuring GWB with PTAs.
  Cited as [11].
- **van Haasteren & Levin 2013** (`arXiv:1202.5932`) — time-correlated noise
  in PTAs. Cited as [12].
- **NANOGrav detector characterization 2023** (`arXiv:2306.16218`). Cited as [13].
- **NANOGrav 15yr harmonic analysis 2025** (`arXiv:2411.13472`). Cited as [14].
- **Kamionkowski, Land, Magueijo 2005** (`arXiv:astro-ph/0502237`) — "axis of
  evil" test statistic $t_\ell$. Cited as [15]. Direct precedent for §IV.B.
- **de Oliveira-Costa, Tegmark, Zaldarriaga, Hamilton 2004**
  (`arXiv:astro-ph/0307282`) — CMB large-scale fluctuations. Cited as [16].
- **Cornish & Romano 2013** (`arXiv:1305.2934`) — unified treatment of GW
  data analysis. Cited as [17] for the template ≡ anisotropic equivalence.
- **NANOGrav targeted SMBHB searches 2026** (`arXiv:2508.16534`). [18].
- **Charisi, Taylor, Witt, Runnoe 2024** (`arXiv:2304.03786`) — efficient
  large-scale SMBHB probes. [19].
- **NANOGrav discreteness paper 2025** (`arXiv:2404.07020`) — "looking for
  signs of discreteness in the GWB." Cited as [20]. Very relevant to our
  discussion of single-source vs stochastic.

## Critique notes

- [[../notes/app_B_coherent_fisher_critique]] — our unified critique
  memo (rev. 2026-04-20, Phase-3). Headline: **Eq. (B6) is the
  correct statistic, and in the App. B toy limit the
  profile-likelihood ($T_1=s$) and Bayes-factor
  ($T_{1^\star}=\max(s-2-2\ln(s/2),0)$) constructions are
  monotone-equivalent, so stochasticization is free at the detection
  stage**. The single scaling-level critique is the Eq. (50)
  same-power null: matching $\sigma_h^2$ to the GWB power pins the
  null to a matched-power GWB and caps the significance at
  $\sim 3.8\sigma$ ($p[\chi^2_4 > 24] = 7.99\times 10^{-5}$). Two
  distinct side observations: parameter-interpretation (Fisher on $\mu$
  vs $q$, with two distinct mode counts — polarization $k=2$ and
  kernel-effective $1/f_\sigma = 12$) and mild anisotropic-response
  breakdown (realistic $F(\hat n_s)$ with non-degenerate eigenvalues
  breaks the equivalence at 10–20% of $T_1$; few-percent p-value
  shift). Gaussianization at PTA SNR is harmless; the $t_\ell$ of
  Eq. (49) is a per-$\ell$ alignment diagnostic, not the optimal
  multi-$\ell$ statistic.
- [[pn_appendixB_coherent_vs_covariance]] — independent ChatGPT note
  reaching the same overall verdict. Source of the $t_\ell$ vs
  $T(\hat n)$ separation and the $\partial C/\partial\mu|_0=0$
  one-liner used in earlier iterations of the memo. The memo's
  Phase-3 rewrite supersedes its scaling-demotion reading with the
  stronger monotone-equivalence statement; ChatGPT's §7.4
  ("many-to-one" information loss) now applies to multi-source or
  multi-parameter settings, not the single-source single-bin toy.
- [[pn_coherent_vs_stochastic_single_source]] — pedagogical note
  (2026-04-20) proving monotone equivalence in the single-template
  case ($T_1=s$, $T_{1^\star}=s-1-\ln s$) with a clean separation of
  detection (same p-value) from parameter interpretation (Fisher on
  $\mu$ vs $\mu^2$). Directly drove the Phase-3 memo revision.
- [[../notes/app_B_2pol_equivalence_check]] — P1 calculation
  (2026-04-20): the equivalence extends to App. B's 2-polarization
  isotropic toy limit, with $T_{1^\star}=\max(s-2-2\ln(s/2),0)$, and
  survives sky-direction maximization in the isotropic limit. General
  formula: $T_{1^\star}^{(k)} = \max(s-k-k\ln(s/k),0)$.
- [[../notes/app_B_anisotropic_response]] — P2 calculation
  (2026-04-20): for realistic $U^\dagger N^{-1}U$ the equivalence
  fails but quantitatively mildly. Eigenbasis formulas:
  $T_1 = \sum_i |v_i|^2/\rho_i^2$ (unit weights),
  $T_{1^\star} = \sum_i w_i|v_i|^2/\rho_i^2 - \sum_i\ln(1+q\rho_i^2)$
  with $w_i = q\rho_i^2/(1+q\rho_i^2)$. Monotone iff all $\rho_i^2$
  equal. Rank disagreement 10–20% of $T_1$ at typical sky positions,
  few-percent p-value shift.
- [[../notes/app_B_memo_revision_proposal]] and
  [[../notes/app_B_memo_revision_critique]] — the Phase-3 revision
  process artifacts (proposal + independent critique). Kept for the
  audit trail.

## Caveats / draft-state flags

- **Incomplete:** FIG. 2 caption is the placeholder "Caption"; ACKNOWLEDGMENTS
  section has "We would like to thank. [blank]"; one in-line `[GSP: simple
  explanation to this factor? Something related to the normalization of
  HD and parseval theorem]` near Eq. 48 ($f_\sigma = 1/12$).
- **Gaussian approximation range:** Appendix A shows the Edgeworth correction
  breaks down for $\varepsilon \gtrsim 1$ (single-source-dominated); for PTA
  cases with $\varepsilon = 0.2$ the Gaussian is excellent. Confirms that
  the single-source regime we care about in the project is safely inside
  the Gaussian-approximation domain where the sufficient-statistic framework
  applies.
- **No brightest-source fraction $p$ defined.** The natural translation is
  $\varepsilon = |z_{1,e}|^2/(2\sigma_N^2) = $ (single-source power)/(total
  noise+GWB power). Relation to our $p$: $p = \varepsilon/(1+\varepsilon)$
  if all non-brightest contributions are in the "noise" $\sigma_N^2$. Worth
  pinning down if cross-referencing.

## Relations to other sources

- [[pn_C1_over_C0]] — our canonical $C_1/C_0$ note; Eq. 23 of this draft
  confirms its $C_\ell$ formulas for a single source on the pulsar-term sky.
- [[pta_1src_vs_CL]] — our canonical one-source-vs-$C_\ell$ note; this
  paper's §III.A is essentially the full formalism of that note.
- [[pn_coh_vs_incoh_fisher]] — this paper's §III.B is the Fisher-matrix
  machinery; our note does the coherent-vs-incoherent decomposition.
- [[fisher_src_vs_bg_degeneracy]] — this paper's App. B shows the rank-1
  structure of the single-source addition to the Gaussian covariance
  ($UC U^\dagger$ in Eq. B5), which is exactly the block-diagonal
  degeneracy we study.
- [[arxiv_2306_16221]] — NANOGrav 15yr anisotropy: same dataset, same
  sky positions, different question. The draft gives a more powerful
  statistical framework for analyzing that data.
- [[arxiv_2406_17010]] — Sato-Polito & Zaldarriaga 2025 (distribution):
  the direct precursor; characteristic-function GWB distribution is
  assumed as background in this new draft.

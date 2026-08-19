# Note on App. B: coherent vs covariance averaging (ChatGPT, 2026-04-16)

**Source:** `references/appendixB_coherent_vs_covariance_note.md`
**Type:** Pedagogical note from ChatGPT, used as an independent critique of
App. B of [[draft_sufficient_statistics_2026]].
**Ingested:** 2026-04-17

## Summary

Self-contained critique of App. B that arrives at the same bottom line
as our in-house note ([[../notes/app_B_coherent_fisher_critique]]) but
with several additional framings. The short verdict, quoted from the
note:

> **Eq. (B6) can be right, but Appendix B is the wrong way to derive it.**

The note cleanly separates the *test statistic* (fine) from the
*derivation path* (lossy) from the *problem framing* (same-power
discrimination instead of detection).

## Section-by-section synopsis

- **§1 (Executive summary).** Names two distinct statistics in the draft:
  - Eq. (49) $t_\ell(\hat n) = (|a_{\ell 2}|^2 + |a_{\ell,-2}|^2)/\sum_m |a_{\ell m}|^2$
    — single-$\ell$ alignment score, not the full detection statistic.
  - Eq. (B6) $T(\hat n) = |\sum_\ell (z_\ell/2) a_{\ell 2}|^2 + |\sum_\ell (z_\ell/2) a_{\ell,-2}|^2$
    — multi-$\ell$ coherent combination, *is* the right coherent statistic
    in the toy limit.
- **§2 (Actual inference problem).** The coherent source model is
  already written in Sec. IVA, Eq. (44), as $\vec a = U\vec h + \vec n$
  with MLE $\hat{\vec h} = (U^\dagger N^{-1} U)^{-1} U^\dagger N^{-1} \vec a$.
  This is the standard coherent detection problem.
- **§3 (What App. B does instead).** Averages source amplitudes to
  zero, rewriting $H_1$ as a zero-mean Gaussian with a rank-1
  covariance perturbation. This changes the hypothesis pair.
- **§4 (Two statistics in the draft).** Sharpens the $t_\ell$ vs
  $T(\hat n)$ distinction.
- **§5 (Correct coherent derivation).**
  - §5.1 General matrix form:
    $\mathcal F(\hat n) = \vec a^\dagger N^{-1} U (U^\dagger N^{-1} U)^{-1} U^\dagger N^{-1} \vec a$.
    Exact within the Gaussian likelihood of Sec. IVA.
  - §5.2 Harmonic-basis derivation in the App. B toy limit
    (diagonal noise, $N_{\ell m, \ell'm'} = N_\ell \delta_{\ell\ell'}\delta_{mm'}$,
    rotated frame). Gives $\hat h_{\pm 2} = \sum_\ell (c_\ell/N_\ell) a_{\ell,\pm 2}/\sum_\ell c_\ell^2/N_\ell$
    with $c_\ell = z_\ell/2$. The profile statistic reduces exactly to Eq. (B6).
  - §5.3 Factor-of-two caveat in conventions.
- **§6 ($t_\ell$ vs $T$ relation).** $t_\ell$ is a legitimate one-$\ell$
  profile statistic, just not the multi-$\ell$ optimal.
- **§7 (Why App. B is conceptually wrong).**
  - §7.1 Changes the alternative hypothesis from coherent mean shift
    to zero-mean covariance perturbation.
  - §7.2 Internal inconsistency: the Gaussian prior on $\vec h$ in
    Eq. (50) is *not* the marginal law one gets from uniform priors on
    $(\phi_0, \psi, \cos\iota)$. So the paper's stated uniform-priors
    marginalization and its used Gaussian prior are not the same thing.
  - §7.3 App. A doesn't justify the App. B step. App. A is pulsar-term
    CLT-type Gaussianization (many sources); App. B Gaussianizes a
    single realized Earth-term source.
  - §7.4 Information loss: $\vec h \mapsto \vec h\,\vec h^\dagger$ is
    many-to-one.
- **§8 (Quantifying the loss).**
  - **§8.1 Fisher-at-origin argument.** Parametrize $\vec h = \mu\,\bar{\vec h}$.
    The coherent Fisher is $F^{\rm coh}_{\mu\mu} = \bar{\vec h}^\dagger U^\dagger N^{-1} U \bar{\vec h} > 0$.
    After App. B's step, $C(\mu) = N + \mu^2 \Delta C$, so
    $\partial C/\partial\mu|_{\mu=0} = 0$ identically, and hence
    $F^{\rm cov}_{\mu\mu}|_{\mu=0} = 0$. **The first non-zero
    sensitivity is to $\mu^2$, not $\mu$.** This is the single
    sharpest statement of where the coherent channel is lost.
  - **§8.2 KL scalings.** Coherent $D_{\rm coh} \propto \mu^2$;
    covariance-only $D_{\rm cov} \propto \mu^4$.
  - **§8.3 Rank-2 concrete example.** In the $U^\dagger N^{-1} U = \kappa I_2$
    toy limit with circular Gaussian prior $\vec h \sim \mathcal{CN}(0, qI_2)$,
    eigenvalues of $A = N^{-1/2} \Delta C\,N^{-1/2}$ are both $x = q\kappa$.
    Optimized forward KL (with isotropic background level allowed to
    float) is $D_{\rm cov}^+ = n\ln(1 + 2x/n) - 2\ln(1 + x) \approx (1 - 2/n) x^2$
    at small $x$. Coherent KL is $D_{\rm coh} = \kappa(|h_2|^2 + |h_{-2}|^2) = 2x$
    at prior-typical amplitudes. So $D_{\rm cov} = O(D_{\rm coh}^2)$.
- **§9 (Why App. B lands on $T$ anyway).** Under the Gaussian prior,
  the Bayes factor between $\mathcal{CN}(0, N)$ and $\mathcal{CN}(0, N + qUU^\dagger)$
  simplifies via Sherman-Morrison to something monotone in
  $\mathcal T(\hat n) = \vec a^\dagger N^{-1} U U^\dagger N^{-1} \vec a$,
  which in the diagonal-noise toy limit is proportional to $T(\hat n)$.
  But this does not make the App. B derivation "right" for detection;
  it only means two different constructions share a quadratic projection
  in a symmetric limit.
- **§10 (Suggested editorial fix).** Keep Sec. IVA coherent;
  reinterpret $t_\ell$ as a per-$\ell$ diagnostic; move the
  Gaussian-prior construction to a separate aside; weaken the "no
  distinction between CW and anisotropy" claim.
- **§11 (Replacement paragraph).** A drop-in paragraph for the draft.
- **§12 (Final conclusion).** 5 bullets summarizing the whole thing.

## Points this note adds beyond our in-house Fisher note

1. **$t_\ell$ vs $T$ separation.** Our note treated "the App. B
   statistic" as monolithic; ChatGPT carves cleanly between Eq. (49)
   (per-$\ell$ alignment) and Eq. (B6) (multi-$\ell$ coherent).
2. **Right-formula-wrong-derivation framing.** $T(\hat n)$ is exactly
   the profile statistic in the toy limit. What we should critique is
   the derivation path, not the formula.
3. **$\partial C/\partial \mu|_0 = 0$ one-liner** (§8.1) — cleanest
   single statement of where the order-in-$\mu$ is lost.
4. **Prior-inconsistency point** (§7.2) — the Gaussian prior used in
   Eq. (50) is not the marginal from the stated uniform-angle priors.
   Purely internal textual issue in the draft.
5. **Constructive editorial fix** with a drop-in replacement paragraph.

## Points where our in-house note contributes orthogonally

1. **Explicit Wigner-D Fisher block.** Harmonic-basis computation gives
   $F = \mathcal F\,\mathbb I_4$ with $\mathcal F = \sum_\ell z_\ell^2/(4N_\ell)$.
   ChatGPT keeps to abstract $U,\,N$ matrices.
2. **High-SNR $\ln I_0$ branch.** The exact marginal has
   $\ln I_0 \to x$ at high SNR, preserving coherent info; the paper's
   Gaussian approximation keeps only the $x^2/4$ low-SNR branch. This
   is only relevant outside the PTA regime and is secondary to the
   task-framing critique.

## Corrections to our in-house note triggered by ChatGPT's note

> **Update (2026-06-13).** The "stochasticization demotes detection
> $H\to H^2$ regardless of the null" framing below was itself superseded:
> stochasticization is *free at the detection stage* (the profiled
> covariance LR is monotone in the matched-filter statistic), so the
> $H\to H^2$ demotion is a **parameter-precision / data-generating**
> statement, not a detection-significance one. See
> [[pn_coherent_vs_stochastic_single_source]] §II (rank-one
> $s-1-\ln s$), [[../notes/app_B_coherent_fisher_critique]] §4/§10.3, and
> the canonical [[pta_source_detection_likelihood]] (source-subspace
> projector covariance $g_r(T_{\rm coh})$).

The in-house note has since been rewritten to reflect two observations
triggered by this note:

1. **$T$ is a function of the data; the detection scaling depends on
   the null AND the source model.** Our earlier derivation computed
   "detection significance" as
   $(\Delta \langle T\rangle)^2/\mathrm{Var}(T|H_0)$ in a Gaussian-SNR
   sense, which gave $\rho^2_{\rm App.B}\propto H^2$. In Problem A
   (coherent source, noise-only null), the proper detection metric is
   the non-centrality parameter of the $\chi^2_4$ distribution of $T$:
   $\lambda = H\mathcal F_{\rm tot}$, **linear in $H$**. So $T$ is fine
   as a coherent detection statistic against noise; the $H^2$ scaling
   is not a property of $T$ per se.

2. **The App. B path takes two independent lossy steps, not one.** Our
   earlier framing attributed both the $H\to H^2$ scaling demotion and
   the $\sim 3.8\sigma$ ceiling to the same "same-power
   discrimination" framing. They are in fact separable:
   - *Stochasticization* (coherent → covariance). Replacing $\vec h$
     deterministic by $\mathcal{CN}(0,qI)$ produces $\rho^2 \propto H^2$
     at small $H$ regardless of the null — this is the cosmic-variance
     scaling of a power estimator ($\mathrm{Var}(\hat q) \geq q^2/k$
     even at zero noise, analogous to
     $\mathrm{Var}(\hat C_\ell) \geq 2C_\ell^2/(2\ell+1)$ in CMB).
   - *Same-power null* (Eq. 50). Pinning $H_0$ to the GWB with matched
     trace puts the $\sim 3.8\sigma$ ceiling on top of the already
     demoted scaling. The factor $f_\sigma = 1/12$ in Eq. (48) is the
     inverse effective mode count, playing the $1/(2\ell+1)$ role of
     CMB cosmic variance.

   Our in-house note now factors the critique into these two steps
   (§5.1 and §5.2 of the rewrite).

## Relation to other wiki pages

- [[draft_sufficient_statistics_2026]] — the paper being critiqued.
- [[../notes/app_B_coherent_fisher_critique]] — our in-house critique
  memo (rev. 2026-04-17). Uses the ChatGPT framing of this note plus
  the Wigner-D Fisher block, $\ln I_0$ aside, and two-step factoring.
- [[../concepts/matched_filter_vs_power]] — "linear beats quadratic";
  ChatGPT's $\partial C/\partial\mu|_0 = 0$ is the cleanest form of
  this principle for PTA.
- [[../concepts/fisher_hierarchy]] — the same $O(\mu^2)$ vs $O(\mu^4)$
  hierarchy appears here from a different starting point.
- [[../concepts/coherent_vs_incoherent]] — ChatGPT's §7.1 is the
  coherent → covariance-only reduction.

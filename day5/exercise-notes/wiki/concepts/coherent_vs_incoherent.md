# Coherent vs incoherent PTA searches

Coherent = source amplitudes kept as unknown parameters of the data
mean. Incoherent = amplitudes marginalized with a Gaussian prior, so
source survives only as a covariance perturbation. These are
qualitatively different statistical problems, not just numerically
different.

## The structural statement

**Coherent:**
$$d \sim \mathcal{CN}(Ua,\, C_0),\qquad
F^{\rm coh} = \begin{pmatrix} F^{\rm bg}_{AA} & 0 \\ 0 & U^\dagger C_0^{-1} U \end{pmatrix}.$$

Block-diagonal. Source and background are **exactly orthogonal** at
Fisher level. True for any source direction and any $N_p$.

**Incoherent:**
$$d \sim \mathcal{CN}(0,\, C_0 + q\,\Gamma_{\rm src}),\qquad
F^{\rm inc}(A_{\rm iso}, q) = \langle\cdot,\cdot\rangle_C\;\text{matrix.}$$

Full $2\times 2$ matrix with off-diagonal coupling; both live in
covariance space. See [[source_background_degeneracy]].

## Why the source-power fraction scales differently

- **Coherent:** source is in mean → KL is **linear** in source power → $D_{\rm coh}\propto p$.
- **Incoherent:** source is in covariance → KL is **quadratic** in source power → $D_{\rm inc}\propto p^2$ — specifically the *power-map / physical-covariance* route; the *source-subspace projector* route stays at $\propto p$ (see "Two covariance routes" below).

See [[fisher_hierarchy]] for the full derivation.

## Two covariance routes — only one is the $p^2$ object (2026-06-13)

"Incoherent covariance search" is ambiguous; [[../sources/pta_source_detection_likelihood]]
(Secs 4.1–4.2) separates the two constructions:

- **Source-subspace projector** $C_B(I+\eta\Pi)$ ($\Pi$ = whitened
  projector onto the source response subspace). Profiled LR
  $g_r(T_{\rm coh})=T_{\rm coh}-r-r\ln(T_{\rm coh}/r)$ is strictly
  increasing in $T_{\rm coh}$ ⇒ **same rejection regions, same
  threshold** $p_{\rm sub,*}=p_{\rm coh,*}$. This is the special
  $S_a\propto F_{\rm coh}^{-1}$ member. It sits at the **$p$ level**:
  asking "excess variance in the source's subspace?" keeps all the
  detection information. This is the precise sense in which "search for
  the source" and "search for excess power in the source direction" are
  the *same question*.
- **Physical / power-map** $C_Q+q\,\Gamma_{\rm src}$ (Gaussian-marginalized
  $US_aU^T$, or its one-source projection $T_{\rm psrc}$). Uses the
  phase/polarization-**averaged** response, is **not** generally
  monotone in $T_{\rm coh}$, and is the genuine **$p^2$** object.

So the $p^2$ scaling on this page is the power-map route. The projector
route is the bridge between "coherent" and "incoherent" that loses
*nothing* at the detection stage — consistent with the App. B monotone
equivalence in [[../notes/app_B_coherent_fisher_critique]].

## Gaussian-marginalization bridge

Marginalizing a Gaussian prior over amplitudes **exactly** converts
coherent to incoherent. The integral is Gaussian; the result uses the
Woodbury identity. This is the unique invertible transform that loses
all phase information while keeping second moments.

For rank-1 covariance perturbation $\Delta C = q\, u u^\dagger$:
$$D_{\rm cov}^+ = n\log(1+\rho_{\rm coh}^2/n) - \log(1+\rho_{\rm coh}^2),$$
which expands to $\tfrac12(1-1/n)\rho_{\rm coh}^4$ at weak signal. So
the covariance channel literally is the **square** of the coherent
channel.

**Detection vs figure-of-merit (read with "Two covariance routes"
above).** This $\rho^4$ is the **KL / parameter-Fisher** figure of merit
for the *marginalized* (random-amplitude) covariance model — the
expected evidence of "stochastic source present" vs null. It is *not* in
tension with the projector-route claim that the same rank-1 object sits
at the $p$ level for **detection**: the profiled likelihood ratio
$s-1-\ln s$ is strictly increasing in the matched-filter statistic $s$,
so it has the identical ROC/threshold as the coherent test. The $\rho^4$
(peak curvature / model evidence) and the $\rho^2$-equivalent detection
(peak value) are the two faces proved in
[[../sources/pn_coherent_vs_stochastic_single_source]] §II. Bare "$p^2$"
covariance scalings on this page therefore mean the **power-map /
parameter-Fisher** figure of merit, not the detection threshold.

## Earth term vs pulsar term

- Earth term is phase-coherent across pulsars → admits coherent search.
- Pulsar term averages over random pulsar phases → natively incoherent.

Pulsar term anisotropy is therefore $p^2$ from the start — the random
per-pulsar phases preclude the coherent / projector route, leaving only
the power-map ($p^2$) channel.

## Source pages

- [[../sources/pn_coh_vs_incoh_fisher]] — canonical derivation, side-by-side in Gaussian-Fisher language.
- [[../sources/pn_coh_vs_quadratic]] — self-contained, info-theoretic framing with the Gaussian-marginalization bridge.
- [[../sources/fisher_src_vs_bg_degeneracy]] — exact block-diagonality in the coherent case.
- [[../sources/pn_1src_vs_dipole_cov]] — once one compresses to the dipole, 1-source search = dipole search.
- [[../sources/pta_prior_sensitivity]] — prior-volume effects apply to incoherent, not coherent.
- [[../sources/pn_HD_vs_CURN_Fisher_Bayes]] — CURN-vs-HD as a cross-only shape change at fixed auto-power; $\eta$ lives purely in the covariance-cross (incoherent) channel for a stochastic common process.
- [[../sources/pta_curn_hd_cross_only]] — identifies the cross-only quadratic estimator $\hat B_\times = S_B/F_{BB}$ as the nuisance-projected HD Fisher score, then shows that the physical nonnegativity boundary $P \ge B$ reintroduces diagonal information when $(n-1)\overline{X^2} < 1$.
- [[../sources/pta_source_detection_likelihood]] — cleanest split of the two covariance routes (projector $\Pi$ vs physical $US_aU^T$); the projector family is monotone-equivalent to the coherent matched filter.
- [[../sources/toy_model_source_vs_power_map]] — one-pixel blocks $b_{\rm mean}$ (mean-shift) vs $b_{\rm cov}$ (rank-1 covariance) agree to $O(\sigma^2)$, first differ at $O(\sigma^4)$; the evidence-language form of the distinction.
- [[../sources/joint_search_resolved_unresolved]] — brightest source modeled as a coherent directional CW; the rest as the isotropic stochastic HD-correlated GWB (the physical coherent/incoherent split, in a real analysis).

## Paper uses

- `three_strategies.tex` — the core section.
- `appendix_fisher.tex` — numerical verification.
- `discussion.tex` — strategic recommendation: do coherent first.

## Related concepts

[[KL_divergence]], [[fisher_hierarchy]], [[matched_filter_vs_power]],
[[source_background_degeneracy]], [[prior_sensitivity]].

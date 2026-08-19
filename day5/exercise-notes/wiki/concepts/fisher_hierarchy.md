# The KL-divergence hierarchy

Canonical statement of the paper's main quantitative claim: three
detection strategies for a single bright source against an isotropic
background order strictly in their scaling with the brightest-source
fraction.

## Statement (paper eq `eq:hierarchy`)

$$D_{\rm coh} \propto p, \qquad
D_{\rm inc} \propto p^2, \qquad
D_{C_\ell} \propto p^4.$$

Using the [[KL_divergence]] $D$ as the common figure of merit.

## Derivations

Three different mechanisms produce these three scalings:

**Coherent ($\propto p$).** Source is in the mean, background in the
covariance. Gaussian Fisher block-diagonal in $(A_{\rm iso}, a)$
([[source_background_degeneracy]]). With $a=\sqrt{q}\hat a$,
$q=A_{\rm GW} p$:
$$D_{\rm coh} = \tfrac12\,q\,\hat a^T U^T C_0^{-1} U\hat a \propto p.$$

**Incoherent full harmonic ($\propto p^2$).** Source and background
both in the covariance. Orthogonalize against the isotropic direction;
the remaining Fisher is $F_{pp}^{\rm full}=\Sigma_{\rm bg}^2\sum_L s_L$,
**independent of $p$** at leading order. So
$D_{\rm inc} = \tfrac12\,p^2 F_{pp}^{\rm full} \propto p^2$.

**$C_\ell$-only compression ($\propto p^4$).** Further compression of
the $p_{LM}$ harmonic coefficients to block powers $C_L^P$. Each block
becomes a noncentral $\chi^2$ with noncentrality
$\lambda_L = p^2\,\Sigma_{\rm bg}^2\,s_L$, whose Fisher information on
$\lambda$ at $\lambda=0$ is $1/[2(2L+1)]$. Therefore
$F_{pp}^{(C_L)} = 2p^2\Sigma_{\rm bg}^4 \sum_L s_L^2/(2L+1) + O(p^4)$,
which **itself scales as $p^2$**. So
$D_{C_\ell} = \tfrac12\,p^2 F_{pp}^{(C_L)} \propto p^4$.

The $1/(2L+1)$ is a per-block penalty inside the sum, **not** an
overall factor on the hierarchy. This is exactly the misconception
that produced the bug fixed on 2026-04-13.

## Key consequences

- At fixed $p$, the strict ordering is $D_{\rm coh} > D_{\rm inc} > D_{C_\ell}$ for $p, \Sigma_{\rm bg} \lesssim 1$.
- The $\sigma_p$ ratio between full-harmonic and $C_L$-only fits scales as $1/(p\,\Sigma_{\rm bg})$.
- For NANOGrav-like parameters ($p^2 \sim 0.1$, $\Sigma_{\rm bg}\sim 1$), $\sigma_p^{(C_L)}/\sigma_p^{\rm full} \sim 5$–$7$.

## Refinement: "incoherent covariance" is ambiguous (2026-06-13)

The PTA-native note [[../sources/pta_source_detection_likelihood]]
sharpens the middle rung. The phrase "covariance search" hides **two
different constructions**, and only one of them is the $p^2$ object:

1. **Source-subspace projector covariance** $C \to C_B(I+\eta\,\Pi)$,
   where $\Pi$ is the whitened projector onto the source response
   subspace. Its profiled likelihood ratio is
   $g_r(T_{\rm coh}) = T_{\rm coh}-r-r\ln(T_{\rm coh}/r)$, a **strictly
   increasing** function of the coherent statistic $T_{\rm coh}$.
   Therefore it has the **identical rejection region and threshold** as
   the coherent matched filter: $p_{\rm sub,*}=p_{\rm coh,*}$. It sits
   at the **$p$ level**, not $p^2$. (Rank-1 version: $s-1-\ln s$.)
2. **Physical / power-map covariance** $C \to C_Q + q\,\Gamma_{\rm src}$
   (the Gaussian-amplitude-marginalized response $US_aU^T$, or its
   one-source power-map projection $T_{\rm psrc}=(v^Ts)^2/(v^TFv)$ with
   $\lambda_{\rm psrc}=p^2\,v^TFv$). This is the genuine **$p^2$**
   channel; it uses the phase/polarization-**averaged** response, not
   the realized coherent vector.

So $D_{\rm inc}\propto p^2$ refers specifically to construction 2.
Construction 1 is the "ask the same question, keep the information"
route — the multi-dof generalization of the rank-1 monotone equivalence
in [[../sources/pn_coherent_vs_stochastic_single_source]] and
[[../notes/app_B_2pol_equivalence_check]] ($T_{1^\star}=g_r$ with
$r=k$).

There is also a **new intermediate object**: the arbitrary harmonic-map
statistic $T_{\rm map}=s^TF^{-1}s$ has the **same** one-source signal
norm ($\propto p^2$) but a null with $m$ degrees of freedom — a
model-space / dof **threshold penalty** for asking "is there *any*
map?" instead of "is there *this* source?". It is **not** an
unavoidable information loss: projecting the full score $s$ onto the
template $v(\Omega)$ recovers $T_{\rm psrc}$. Only the further
compression to block powers $C_L$ (integrating over the $m$-pattern)
forces the drop to $p^4$. The refined picture is therefore four-tiered:

| Question asked | Statistic | Scaling |
|---|---|---|
| this source (mean), or excess variance in its subspace | $T_{\rm coh}$, $I+\eta\Pi$ | $\propto p$ |
| this source's power-map template | $T_{\rm psrc}$ | $\propto p^2$ |
| any anisotropy map ($m$ coeffs) | $T_{\rm map}=s^TF^{-1}s$ | $p^2$ norm, $m$-dof threshold |
| block powers only | $C_L$ | $\propto p^4$ |

The Bayesian-evidence version of the same story (averaged Bayes factor
vs penalized typical log-evidence) is in
[[../sources/toy_model_source_vs_power_map]]. The empirical realization
of the top ($\propto p$) rung — a direct joint CW + GWB search on
NANOGrav 15yr that finds nothing — is
[[../sources/joint_search_resolved_unresolved]].

## KL vs Fisher: do not confuse

$D \approx (1/2)\,\theta^2 F_{\theta\theta}(0)$ **only if** $F$ is
$p$-independent. For $F_{pp}^{(C_L)}\propto p^2$, the relation
becomes $D\propto p^4$. See [[KL_divergence]] and
[[../conventions|conventions]].

## Detection vs estimation: the penalty is question-dependent (2026-06-23)

The strict $p,p^2,p^4$ ordering above is about the **error bar** on $p_1$
(equivalently the KL/Fisher of estimating it). It does **not** translate into a
catastrophic *detection* loss at the angular resolution PTAs actually have. The
rewritten [[../paper/sec_source_detection|Sec. VI]] makes the distinction
explicit, anchored on [[../sources/pta_point_source_multipole]]:

- **Estimation question** ("how well is $p_1$ measured?"). The $C_\ell$-only
  Fisher scales as $p^2$, so $\sigma_p^{(C_L)}/\sigma_p^{\rm full}\sim
  1/(p\,\Sigma_{\rm bg})\sim 5$–$10$ at $p^2\sim0.1$–$0.2$, diverging as
  $p\to0$. This is the $p^4$ statement.
- **Detection question** ("can a statistic cross threshold at fixed resolution?").
  Comparing an unknown-direction coherent *scan* (which pays a trials factor
  $\sim K_L$) to a one-parameter Poisson $C_\ell$ statistic, the required source
  *amplitude* ratio is only $1.13,1.16,1.21,1.27,1.33,1.38$ for $L=1\ldots6$
  ($p_{\rm fa}=0.05$); Monte-Carlo gives even less, and **exactly $1$ at $L=1$**
  (the dipole scan max $=\sqrt{C_1}$ is the $C_\ell$ statistic). Converting a
  significance ratio to an amplitude takes a square root, and the scan's own
  trials factor closes most of the gap at low resolution.

Both statements are correct; the paper's pre-2026-06-23 conclusion ("$C_\ell$
threshold $>1$, not viable") read the $p^4$ scaling as a categorical failure,
conflating the two questions. Corrected verdict: $C_\ell$ is **never the best
tool** (a source search keeps the locating information), but it is **not
catastrophic** — modestly worse at low resolution, the gap growing only slowly
with $L$. Verified in `paper/scripts/verify_source_vs_cl.py`.

## Source pages (canonical)

- [[../sources/pn_coh_vs_incoh_fisher]] — derives all three regimes from the Gaussian Fisher formula (Secs. 4-9).
- [[../sources/pta_1src_vs_CL]] — exact noncentral-$\chi^2$ Fisher and the small-$\lambda$ expansion (Secs. 3-5).
- [[../sources/pn_coh_vs_quadratic]] — information-theoretic framing; rank-1 rate $D_{\rm cov} \sim (1/2) \rho_{\rm coh}^4$.

## Source pages (supporting)

- [[../sources/fisher_src_vs_bg_degeneracy]] — exact block-diagonality of coherent Fisher; numerical $|r|$ values for incoherent.
- [[../sources/pn_1src_vs_dipole_cov]] — one-source = dipole equivalence after compression.
- [[../sources/pta_exact_pair_average]], [[../sources/pta_noise_dominated_limit]] — block weights $s_L$ feeding the formulas.
- [[../sources/pta_1src_vs_cls_toy]] — toy Fisher validating the formalism.
- [[../sources/matched_filter_vs_power]] — general linear-vs-quadratic argument in a simpler model.
- [[../sources/pn_HD_vs_CURN_Fisher_Bayes]] — same structural logic in the simplest setting: once the common auto-power is held fixed by the shape parameter $\eta$, the leading Fisher starts at quadratic order in $\Gamma - I$.
- [[../sources/pta_curn_hd_cross_only]] — cross-only quadratic estimator derived as nuisance-projected HD Fisher; quantitative criterion $(n-1)\overline{X^2} < 1$ identifies a new regime where the physical CURN boundary re-introduces auto-power information in the incoherent channel.
- [[../sources/pta_source_detection_likelihood]] — canonical PTA-native derivation of the full hierarchy; **refines** the $p^2$ level (projector-covariance equivalence; intermediate $T_{\rm map}$ dof penalty); block-resolved $D_{C_L}=\tfrac{p^4}{4}\sum_L[v_L^TF_Lv_L]^2/(2L+1)$.
- [[../sources/toy_model_source_vs_power_map]] — Bayesian-evidence face of the hierarchy: SUM-over-locations (one source) vs MULTIPLY-over-pixels (map/$C_\ell$); empty-pixel Occam penalty $\ell_0(q)<0$.
- [[../sources/joint_search_resolved_unresolved]] — Goncharov et al. 2026 (companion draft): the top ($\propto p$) rung run on real NG15 data — no resolvable CW, $\sim0.6\%$/$2\%$ detection probability.

## Paper uses

- `source_detection.tex` (Sec. VI, **new main detection section, 2026-06-23**) —
  the operational summary; uses the "detection vs estimation" distinction above
  and relegates the full hierarchy to the appendices.
- `three_strategies.tex` — now **Appendix A**; `eq:hierarchy` and the derivation.
- `numerical_estimates.tex` — now **Appendix B**.
- `source_vs_cl_reduced.tex` — now **Appendix C**.
- `introduction.tex` — headline claim.
- `main.tex` abstract — revised 2026-06-23 to lead with the source search and
  the modest $C_\ell$ penalty, with the $p,p^2,p^4$ hierarchy noted as appendix
  material.
- `discussion.tex` — item 4 revised to "never the best tool, but not catastrophic."

## Related concepts

[[KL_divergence]], [[coherent_vs_incoherent]], [[s_L_block_weights]],
[[source_background_degeneracy]], [[matched_filter_vs_power]],
[[brightest_source_fraction]].

## History

- **2026-04-13**: corrected paper claim $D_{C_\ell}\propto p^2/(2\ell+1)$ → $p^4$. See `log.md` entry of same date.

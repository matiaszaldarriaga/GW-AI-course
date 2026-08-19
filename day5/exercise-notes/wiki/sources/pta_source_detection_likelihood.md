# PTA source-detection likelihood notes (canonical, rev. for review)

**Source:** `references/pta_source_detection_likelihood_notes_for_review.md`
**Type:** Pedagogical note (PTA-specific, rigorous). Self-contained
derivation of five detection likelihoods for one bright source plus an
isotropic background in a single PTA frequency bin, with a corrected KL
hierarchy in the source-power fraction $p$.
**Ingested:** 2026-06-13

## Summary

The canonical, PTA-specific statement of the project's detection-theory
spine. The data vector is **always** the PTA time-delay data $x$; the
object whose angular powers $C_L$ are measured is the **GW source-power
sky** $P(\hat n)$, not the time-delay field. Five likelihoods answer
*different questions* about the same $x$, and the note shows their
information content does not collapse into a single "coherent beats
incoherent" ordering. Crucially, it disambiguates two senses of
"covariance likelihood": the **source-subspace projector** covariance
$I+\eta\Pi$ is monotone-equivalent to the coherent matched filter (same
rejection regions, signal $\propto p$), whereas the **physical
Gaussian-marginalized** covariance $U S_a U^T$ is the bridge to the
power sky and is *not* generally monotone in $T_{\rm coh}$. The
one-source power-map test has signal $\propto p^2$; the angular-power
compression has expected evidence $\propto p^4$. Throughout,
$p = q/(B+q) = h^2/(B+h^2)$, with $q=h^2$ the source power and $B$ the
isotropic-background power in the bin.

## The five likelihoods (Sec 0, Sec 10)

| # | Likelihood | Statistic | Signal strength | Question asked |
|---|---|---|---|---|
| 1 | Coherent profile (Sec 3) | $T_{\rm coh}$ | $\lambda_{\rm coh}\propto p$ | Is there a deterministic mean $U(\Omega)a$? |
| 2 | Source-subspace projector cov. (Sec 4.2) | $g_r(T_{\rm coh})$ | $\propto p$ (same as #1) | Excess variance in the coherent subspace? |
| 3 | Physical Gaussian-marginalized cov. (Sec 4.1) | $I+\eta A_S$ | — (bridge to power sky) | Random amplitudes with covariance $\eta S_a$? |
| 4 | One-source power-map (Sec 7) | $T_{\rm psrc}$ | $\lambda_{\rm psrc}\propto p^2$ | Does the cov. anisotropy have the point-source pattern $v(\Omega)$? |
| 5 | Arbitrary harmonic map (Sec 8) | $T_{\rm map}=s^TF^{-1}s$ | $\propto p^2$, $m$-dof penalty | Is there *any* anisotropic map? |
| 6 | Angular-power-only (Sec 9) | $X_L=\lvert z_L\rvert^2$ | $D_{C_L}\propto p^4$ | What are the block powers $C_L$? |

The decisive refinement: **#1 and #2 keep the same information** (same
threshold, signal linear in $p$). The "$p^2$" object the project's
hierarchy attaches to the incoherent channel is **#4 / #3**, the
power-map / physical-covariance construction, *not* a generic
"incoherent covariance" search. See **consistency notes** below.

## Key equations (each tagged with its note section)

- **(Sec 1) Source-power fraction.** With $a=h\hat a$, $\hat a^T\hat a=1$:
  $$p(h)=\frac{h^2}{B+h^2},\qquad q=h^2.$$

- **(Sec 2) Response and isotropic covariance.** Unit-power directional
  response $R(\Omega)=U(\Omega)S_aU(\Omega)^T$; isotropic average
  $\Gamma_0=\tfrac{1}{4\pi}\int d\Omega\,R(\Omega)$; null covariances
  $C_B=N+B\Gamma_0$ and $C_Q=N+Q\Gamma_0$ with $Q=B+q$. A fair
  anisotropy test lets the monopole float, so anisotropies are tested
  about $C_Q$, not $C_B$.

- **(Sec 3) Coherent profile statistic.** With
  $F_{\rm coh}=U^TC_B^{-1}U$,
  $$T_{\rm coh}(\Omega)=x^TC_B^{-1}U\,F_{\rm coh}^{-1}\,U^TC_B^{-1}x
   \sim \chi^2_r \text{ (null)},\ \chi^2_r(\lambda_{\rm coh}) \text{ (source)}.$$

- **(Sec 3) Coherent noncentrality — linear in $p$.**
  $$\lambda_{\rm coh}=a_s^TU(\Omega_s)^T(N+B\Gamma_0)^{-1}U(\Omega_s)a_s
   = h^2 A_{\rm coh}\simeq B A_{\rm coh}\,p,$$
  with $A_{\rm coh}=\hat a_s^TU^T(N+B\Gamma_0)^{-1}U\hat a_s$.

- **(Sec 4.1) Physical Gaussian-marginalized covariance.** Imposing
  $a\sim\mathcal N(0,\eta S_a)$ gives the marginal
  $$x\sim\mathcal N(0,\,C_B+\eta\,U S_a U^T),$$
  i.e. whitened $y\sim\mathcal N(0,I+\eta A_S)$,
  $A_S=C_B^{-1/2}US_aU^TC_B^{-1/2}$. Keeps only second moments;
  *not* generally a monotone function of $T_{\rm coh}$.

- **(Sec 4.2) Source-subspace projector — same rejection regions as
  coherent.** With $\Pi=V(V^TV)^{-1}V^T$, $V=C_B^{-1/2}U$, the
  profiled LR is a strictly increasing function of $T_{\rm coh}$:
  $$2\log\Lambda_{\rm sub,prof}=g_r(T_{\rm coh}),\quad
   g_r(T)=\begin{cases}0,&T\le r,\\ T-r-r\log(T/r),&T>r,\end{cases}\quad
   g_r'(T)=1-\tfrac{r}{T}>0.$$
  Rank-one version: $2\log\Lambda_{\rm rank1,prof}=s-1-\log s$ for $s>1$
  (with $s=(t^TC_B^{-1}x)^2/(t^TC_B^{-1}t)$). The projector family is the
  special Gaussian-marginalized member $S_a\propto F_{\rm coh}^{-1}$.

- **(Sec 4.2 / Sec 11) Equal thresholds.**
  $$h_{{\rm coh},*}^2=h_{{\rm sub},*}^2=\frac{\lambda_{\rm req}}{A_{\rm coh}},
   \qquad
   p_{{\rm coh},*}=p_{{\rm sub},*}=\frac{\lambda_{\rm req}}{B A_{\rm coh}+\lambda_{\rm req}}.$$

- **(Sec 5) Source-power-sky identity — no PTA response.** For
  $P(\hat n)=\tfrac{B}{4\pi}+q\,\delta^{(2)}(\hat n,\Omega_s)$ in a real
  SH basis, $C_0^P=Q^2/4\pi$ and $C_L^P=q^2/4\pi$ for $L>0$, so
  $$\frac{C_L^P}{C_0^P}=\left(\frac{q}{B+q}\right)^2=p^2\qquad(L>0).$$
  Fractional coefficients $g_{LM}=p\,v_{LM}(\Omega_s)$ with
  $v_{LM}(\Omega_s)=\sqrt{4\pi}\,Y_{LM}(\Omega_s)$ ($v$ is the
  *power-sky* point-source template, not a time-delay template).

- **(Sec 6) Power-sky score and Fisher.** Isotropic-projected response
  $\Gamma_{\alpha,\perp}$, score $s_\alpha$, and
  $$F_{\alpha\beta}(Q)=\frac{Q^2}{2}\,{\rm Tr}\!\left(C_Q^{-1}\Gamma_{\alpha,\perp}C_Q^{-1}\Gamma_{\beta,\perp}\right),
   \qquad
   \log\Lambda_{\rm map}(g)=g^Ts-\tfrac12 g^TF(Q)g+O(g^3).$$

- **(Sec 7) One-source power-map statistic — quadratic in $p$.**
  $$T_{\rm psrc}(\Omega)=\frac{[v(\Omega)^Ts]^2}{v(\Omega)^TF(Q)v(\Omega)}
   \sim\chi^2_1,\qquad
   \lambda_{\rm psrc}=p^2\,v(\Omega_s)^TF(Q)v(\Omega_s).$$
  Weak-source threshold
  $p_{{\rm psrc},*}\simeq[\lambda_{{\rm psrc},req}/v^TF(B)v]^{1/2}$. This
  is a *power-only* statistic (uses $R(\Omega)$, not the realization
  $U(\Omega)a$), so it is **not** $T_{\rm coh}$.

- **(Sec 8) Arbitrary-map statistic — same signal norm, $m$-dof
  penalty.**
  $$T_{\rm map}=s^TF^{-1}s\sim\chi^2_m,\qquad
   \lambda_{\rm map}=p^2\,v(\Omega_s)^TF(Q)v(\Omega_s).$$
  Same noncentrality as $T_{\rm psrc}$ but a null with $m$ degrees of
  freedom. A model-space penalty, not an information loss: projecting
  the full score $s$ onto $v(\Omega)$ recovers $T_{\rm psrc}$.

- **(Sec 9) Angular-power-only — quartic in $p$.** Block power
  $X_L=\lvert z_L\rvert^2\sim\chi^2_{d_L}(\Lambda_L)$,
  $\Lambda_L=p^2\lvert\mu_L\rvert^2=p^2 v_L^TF_L(Q)v_L$, $d_L=2L+1$.
  Small-$\Lambda$ block KL $D_L=\Lambda_L^2/(4d_L)$, hence
  $$\boxed{D_{C_L}=\frac{p^4}{4}\sum_L\frac{\left[v_L(\Omega_s)^TF_L(Q)v_L(\Omega_s)\right]^2}{2L+1}+O(p^6).}$$
  Weak-source thresholds:
  $p_{C_L,*}\simeq[4D_*/K_{C_L}(B,\Omega_s)]^{1/4}$ with
  $K_{C_L}=\sum_L A_L^2/(2L+1)$, $A_L=v_L^TF_L v_L$; equivalently
  $p_{C_L,*}=[(z_{1-\alpha}+z_{1-\beta})/\sqrt{I_{C_L}}]^{1/2}$ with
  $K_{C_L}=2I_{C_L}$.

- **(Sec 9 / Sec 11) Response-free amplitude conversion.** From the
  $C_L^P/C_0^P=p^2$ identity alone, a measured ratio threshold
  $R_*=C_L^P/C_0^P$ converts to source power as
  $h_*^2=B\sqrt{R_*}/(1-\sqrt{R_*})$, and in general
  $q_*=h_*^2=B\,p_*/(1-p_*)$.

## Concepts touched

- [[../concepts/fisher_hierarchy]] — the corrected $p, p^2, p^4$
  ordering, stated here in PTA-native notation. The note shows the
  hierarchy is *between different questions*, with the subtlety that the
  coherent and source-subspace-projector likelihoods sit at the same
  ($\propto p$) level.
- [[../concepts/coherent_vs_incoherent]] — Sec 4 is the cleanest
  PTA-specific statement of the two distinct covariance routes (physical
  $US_aU^T$ vs projector $\Pi$).
- [[../concepts/matched_filter_vs_power]] — $g_r(T)$ and the rank-one
  $s-1-\log s$ are the multi-dof generalizations of the linear-beats-
  quadratic toy; here they show the *power* test #4 (not the projector
  test #2) is the one that pays the quadratic price.
- [[../concepts/KL_divergence]] — $D_{C_L}$ is computed as the
  expected block-power evidence; $D_L=\Lambda_L^2/(4d_L)$ from the
  noncentral-$\chi^2$ Fisher information $I_\Lambda(0)=1/(2d)$.
- [[../concepts/Cl_over_C0]] — the source-power-sky identity
  $C_L^P/C_0^P=p^2$ (Sec 5), response-independent.
- [[../concepts/source_background_degeneracy]] — the monopole-floating
  convention ($C_Q$ not $C_B$) and the isotropic-projected
  $\Gamma_{\alpha,\perp}$ are the covariance-space orthogonalization.
- [[../concepts/sqrt_SH_basis]] — Sec 6/9/12 flag that the linear
  Gaussian-$g$ model can place weight on non-positive maps; a sqrt-SH
  or positive-pixel basis is needed to impose positivity globally.

## Paper uses

Not yet cited by the paper (no `\fromnotebook` reference to
`pta_source_detection_likelihood_notes_for_review.md` in
`paper/sections/` as of 2026-06-13).

## Could be cited

- `three_strategies.tex` — strong candidate. This is the rigorous,
  PTA-native derivation of the three (now five) strategies; Secs 3, 7, 9
  give $T_{\rm coh}$, $T_{\rm psrc}$, $D_{C_L}$ directly. The Sec 4.2
  monotone-equivalence theorem ($g_r$, $s-1-\log s$) is the precise
  statement that the coherent and source-subspace searches keep the same
  information — a refinement the section should incorporate (see
  consistency notes).
- `appendix_fisher.tex` — Sec 6's $F_{\alpha\beta}(Q)$ and the
  isotropic-projected $\Gamma_{\alpha,\perp}$ are the Fisher machinery;
  Sec 9's $D_L=\Lambda_L^2/(4d_L)$ proof belongs here.
- `angular_power_spectrum.tex` — Sec 5's $C_L^P/C_0^P=p^2$ identity and
  the response-free conversion $h_*^2=B\sqrt{R_*}/(1-\sqrt{R_*})$.
- `numerical_estimates.tex` — the explicit threshold formulas
  $p_{{\rm coh},*}$, $p_{{\rm psrc},*}$, $p_{C_L,*}$ in terms of
  $\lambda_{\rm req}$, $v^TFv$, $K_{C_L}$ are ready to be evaluated for
  NANOGrav parameters.

## Related wiki pages

- [[draft_sufficient_statistics_2026]] — the companion draft; this note
  is its detection-theory backbone in continuous ($x$, $U$, $\Gamma$)
  rather than $a_{\ell m}/b_{\ell m}$ language. The draft's "$N_s^{\rm
  eff}\sim 3$" and "$\sim 3.8\sigma$ ceiling" are the same-power /
  resolvability statements; this note supplies the per-strategy KL
  scaling underneath them.
- [[pn_coherent_vs_stochastic_single_source]] — the rank-one
  specialization. Its $T_{1^\star}=s-1-\ln s$ is *exactly* the Sec 4.2
  rank-one $2\log\Lambda_{\rm rank1,prof}$, so the two agree on the
  monotone equivalence of coherent and projector-covariance detection.
- [[pn_appendixB_coherent_vs_covariance]] — the App. B critique that
  first separated "physical covariance derivation (lossy as a
  derivation)" from "the right statistic." This note formalizes the
  resolution: the projector family $I+\eta\Pi$ *is* monotone in
  $T_{\rm coh}$, while the physical $US_aU^T$ family generally is not.
- [[../notes/app_B_coherent_fisher_critique]] — the in-house critique
  memo; this note's Sec 4.1/4.2 split is the clean generalization of the
  memo's two-covariance-route distinction beyond the App. B toy.
- [[../notes/app_B_2pol_equivalence_check]] — the $k$-polarization
  $T_{1^\star}=\max(s-k-k\ln(s/k),0)$ is the rank-$r$ $g_r(T)$ of Sec 4.2
  with $r=k$.

## Consistency notes (with the wiki hierarchy)

1. **REFINES "incoherent covariance $\propto p^2$."** The wiki
   ([[../concepts/coherent_vs_incoherent]],
   [[../concepts/fisher_hierarchy]]) attaches $p^2$ to "the incoherent
   covariance search." This note shows "covariance search" is ambiguous:
   the **source-subspace projector** covariance $I+\eta\Pi$ (Sec 4.2) is
   monotone-equivalent to the coherent matched filter and therefore sits
   at the **$p$** level, same threshold $p_{{\rm sub},*}=p_{{\rm
   coh},*}$. The genuine $p^2$ object is the **one-source power-map /
   physical Gaussian-marginalized** construction (Secs 4.1, 7), which
   uses the phase/polarization-averaged response $R(\Omega)$ rather than
   the realized $U(\Omega)a$. Recommended wiki edit: in
   `coherent_vs_incoherent` and `fisher_hierarchy`, label the $p^2$
   level as the *power-map / physical-covariance* channel, and add the
   caveat that the *source-subspace projector* covariance is at the $p$
   level. This is consistent with — and is the multi-dof generalization
   of — [[pn_coherent_vs_stochastic_single_source]] (rank-one
   $s-1-\ln s$) and [[../notes/app_B_2pol_equivalence_check]].

2. **EXTENDS the $C_L \propto p^4$ result.** The $p^4$ scaling matches
   the wiki exactly, and the proof here is via the noncentral-$\chi^2$
   block KL $D_L=\Lambda_L^2/(4d_L)$ with $\Lambda_L\propto p^2$ — the
   same mechanism as `fisher_hierarchy` (Fisher on $\lambda$ at
   $\lambda=0$ is $1/[2(2L+1)]$), now written with the explicit
   block-resolved kernel $K_{C_L}=\sum_L[v_L^TF_Lv_L]^2/(2L+1)$. No
   contradiction; this is a more general (direction- and
   block-resolved) form of the same formula.

3. **NEW: arbitrary-map ($T_{\rm map}=s^TF^{-1}s$) is a distinct,
   intermediate object.** Same one-source signal norm as $T_{\rm psrc}$
   ($\propto p^2$) but an $m$-degree-of-freedom null penalty. The wiki's
   three-level hierarchy does not currently name this object; it is a
   *model-space* penalty (asking "any map?" instead of "this source?"),
   not an unavoidable information loss, since the full score $s$ still
   contains the one-source projection. Worth a sentence on
   [[../concepts/fisher_hierarchy]] to distinguish "compress to a
   one-source template" (keep $p^2$) from "fit $m$ free coefficients"
   (pay an $m$-dof threshold) from "compress to block powers $C_L$" (drop
   to $p^4$).

4. **CONSISTENT with the $C_\ell$ convention.** The note's $C_L^P$ is
   the source-power sky (the wiki default $C_\ell^{(P)}$); Sec 5 derives
   $C_L^P/C_0^P=p^2$ with no PTA response, exactly the wiki's
   non-conflation rule. The PTA-response-dependent objects live in
   $F(Q)$ and $v^TFv$, separate from the bare ratio.

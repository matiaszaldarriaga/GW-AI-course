# KL divergence as figure of merit

The canonical quantitative measure of "how distinguishable is the
signal from the null?" throughout the project. Chosen over Fisher
information for the hierarchy statement because it remains regular at
$p=0$ even when Fisher diverges.

## Definition

Forward KL divergence of signal vs null:
$$D(H_1 \| H_0) \equiv \mathbb E_{H_1}\!\left[\log\tfrac{p_1(d)}{p_0(d)}\right].$$

Interpretation: expected log-likelihood-ratio evidence for $H_1$ per
realization. Equivalent to detection noncentrality parameter for the
best test statistic.

## Gaussian results used in the paper

**Mean shift, common covariance.**
$$D = \tfrac12\,\mu^T C^{-1}\mu.$$
For a coherent source with $\mu_{\rm src}=\sqrt q\,U\hat a$:
$$D_{\rm coh} = \tfrac12 q\,\hat a^T U^T C_0^{-1} U\hat a = \rho_{\rm coh}^2.$$
The coherent matched-filter SNR² **is** the KL divergence.

**Covariance shift.** After floating the isotropic amplitude,
$$D_{\rm cov} = \tfrac12\!\left[\mathrm{Tr}(A^2) - (\mathrm{Tr}\,A)^2/n\right] + O(A^3),$$
where $A = C_0^{-1/2}\Delta C\,C_0^{-1/2}$. For a rank-1 perturbation
this gives $D_{\rm cov}\sim (1/2)(1-1/n)\rho_{\rm coh}^4$.

## Relation to Fisher information

For a regular parameter:
$$D(\theta) \approx \tfrac12 \theta^2 F_{\theta\theta}(0) + O(\theta^3).$$

**Important caveat.** If $F_{\theta\theta}$ is itself a function of
$\theta$ (as for the $C_L$-only compression where
$F_{pp}^{(C_L)}\propto p^2$), the KL scaling is **not** the same as the
Fisher scaling. This is exactly the mistake fixed on 2026-04-13. See
[[fisher_hierarchy]].

## Forward vs reverse

At leading order in the weak-signal limit, forward and reverse KL
divergences agree, so the direction does not change the scaling
statements. Forward (signal averaging) is more natural for detection
questions.

## Source pages

- [[../sources/pn_coh_vs_incoh_fisher]] — KL for mean vs covariance separately, then direct comparison.
- [[../sources/pta_1src_vs_CL]] — $F_{pp}^{\rm full}$ vs $F_{pp}^{(C_L)}$, implicit KL via $(1/2) p^2 F$.
- [[../sources/pn_coh_vs_quadratic]] — longest exposition, including reverse KL and the isotropic-amplitude floating trick.
- [[../sources/pn_HD_vs_CURN_Fisher_Bayes]] — clean derivation of $D_{\rm KL}({\rm HD}\,\|\,{\rm CURN})\simeq\tfrac12 F_{\eta\eta}$ for the shape-interpolation $C(\eta) = N + \Phi\otimes[I + \eta(\Gamma-I)]$; Laplace-approximation bridge to the Bayesian HD-vs-CURN evidence ratio.
- [[../sources/pta_curn_hd_cross_only]] — local KL in the cross direction $D_{\rm KL} \simeq \tfrac12 B^2 F_{BB}$ with $F_{BB} = \sum_{i<j} D_i D_j X_{ij}^2$, plus the physical-boundary correction $\log\Phi((\hat P - B)/\sigma_P)$ when $A_{\rm C} \ge 0$ is enforced.
- [[../sources/pta_source_detection_likelihood]] — angular-power block KL $D_L=\Lambda_L^2/(4d_L)$ from the noncentral-$\chi^2$ Fisher information $I_\Lambda(0)=1/(2d)$, with $\Lambda_L=p^2 v_L^TF_Lv_L$; gives $D_{C_L}\propto p^4$ and the $D_*=Z^2/2$ threshold convention.
- [[../sources/toy_model_source_vs_power_map]] — average-vs-typical evidence: $\mathbb E_0[B]=1$ but $\mathbb E_0[\log B]<0$ (Jensen); each empty pixel costs $\ell_0(q)=-\tfrac12\log(1+q)+q/(2(1+q))<0$ — the typical-data Occam penalty behind the power-map degradation.

## Paper uses

- `three_strategies.tex` — the central section, KL expressions for all three strategies.
- `introduction.tex` — hierarchy is stated in KL terms.

## Related concepts

[[fisher_hierarchy]], [[coherent_vs_incoherent]],
[[matched_filter_vs_power]], [[source_background_degeneracy]].

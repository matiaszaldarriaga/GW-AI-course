# Coherent vs incoherent source–background Fisher analysis

**Source:** `references/pedagogical_note_coherent_vs_incoherent_source_background_fisher.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

This note derives, from first principles in a single frequency bin, why coherent source fitting and incoherent covariance fitting are qualitatively different statistical problems. In the coherent model the source contributes to the mean and the background contributes to the covariance; the Fisher matrix is exactly block-diagonal between those sectors. In the incoherent model both source and background are covariance shapes, making the problem one of separating two templates in the same space. The resulting KL divergence scales as $D_{\rm coh}\propto q$ (linear in source power) versus $D_{\rm inc}\propto q^2$ (quadratic), establishing the first level of the detection hierarchy. The note continues to show that compressing the incoherent problem to $C_L$-only block powers loses further information, yielding $F_{pp}^{(C_L)}\propto p^2$ and hence $D_{C_\ell}\propto p^4$.

## Key equations and claims

- **Gaussian Fisher formula** (mean + covariance form): $F_{\alpha\beta} = (\partial_\alpha\mu)^T C^{-1}(\partial_\beta\mu) + \tfrac{1}{2}\mathrm{Tr}[C^{-1}(\partial_\alpha C)C^{-1}(\partial_\beta C)]$. (Sec.~2)
- **Background Fisher**: $F^{\rm bg}_{AA} = \tfrac{1}{2}\mathrm{Tr}[C_0^{-1}\Gamma_{\rm iso}C_0^{-1}\Gamma_{\rm iso}]$, and $\Sigma_{\rm bg}^2\equiv A_{\rm iso}^2 F^{\rm bg}_{AA}$. (Sec.~3) → paper eq: convention in `wiki/conventions.md`
- **Coherent Fisher block-diagonal**: $F^{\rm coh}(A_{\rm iso},a)=\mathrm{diag}(F^{\rm bg}_{AA},\;U^T C_0^{-1} U)$. Exact, not an approximation. (Sec.~4.2)
- **Coherent KL divergence**: $D_{\rm coh} = \tfrac{1}{2}q\,\hat a^T U^T C_0^{-1} U\hat a$, so $D_{\rm coh}\propto A_{\rm GW}p$. (Sec.~4.4)
- **$p$ is not a regular coordinate at $p=0$ for coherent**: $\partial_p\mu_{\rm src}$ diverges as $p\to0$. (Sec.~4.5)
- **Incoherent Fisher** (natural parameters $A_{\rm iso},q$): full $2\times2$ matrix with off-diagonal $\langle\Gamma_{\rm iso},\Gamma_{\rm src}\rangle_C$. (Sec.~5.2)
- **Marginalized incoherent Fisher** after projecting out isotropic component: $F^{\rm inc,marg}_{qq}=\langle\Delta\Gamma_\perp,\Delta\Gamma_\perp\rangle_{C_0}$ (Schur complement). (Sec.~5.3)
- **Incoherent KL divergence**: $D_{\rm inc}=\tfrac{1}{2}q^2 F^{\rm inc,marg}_{qq}+O(q^3)$, so $D_{\rm inc}\propto A_{\rm GW}^2 p^2$. (Sec.~5.5)
- **Full harmonic-coefficient incoherent Fisher**: $F_{pp}^{\rm full}=\Sigma_{\rm bg}^2\sum_{L\ge1}s_L(N_p,\beta)$ via the SH addition theorem. (Sec.~8)
- **$C_L$-only Fisher** in small-signal regime: $F_{pp}^{(C_L)}=2p^2\Sigma_{\rm bg}^4\sum_{L\ge1}s_L^2/(2L+1)+O(p^4)$, hence $F_{pp}^{(C_L)}\propto p^2$ and $D_{C_\ell}\propto p^4$. (Sec.~9)
- **$C_L$-only error ratio**: $\sigma_p^{(C_L)}/\sigma_p^{\rm full}\sim (p\Sigma_{\rm bg})^{-1}\sqrt{\sum_L s_L/\sum_L s_L^2/(2L+1)}$. (Sec.~9)

## Concepts touched

- [[concepts/coherent_vs_incoherent]] — derives block-diagonal Fisher structure in coherent case and coupled covariance-space structure in incoherent case; establishes that they are qualitatively, not just quantitatively, different
- [[concepts/fisher_hierarchy]] — establishes the three-level scaling $D\propto p$, $D\propto p^2$, $D\propto p^4$ from first principles in a single note
- [[concepts/KL_divergence]] — exact expressions for $D_{\rm coh}$ and $D_{\rm inc}$; emphasizes that KL (not Fisher) is the detection figure of merit
- [[concepts/brightest_source_fraction]] — shows $q=A_{\rm GW}p$ parametrization and why $p$ is not a regular local coordinate for the coherent problem
- [[concepts/source_background_degeneracy]] — incoherent orthogonalization of $\Gamma_{\rm src}$ against $\Gamma_{\rm iso}$ removes the trivially degenerate isotropic part; remaining distinguishability is $\langle\Delta\Gamma_\perp,\Delta\Gamma_\perp\rangle_{C_0}$
- [[concepts/s_L_block_weights]] — $s_L$ weights appear in the full harmonic-coefficient incoherent Fisher (Sec.~8) and in the $C_L$-only Fisher (Sec.~9)
- [[concepts/Cl_over_C0]] — $C_L$-only compression explicitly derived as a lossy step that costs a factor $\sim(p\Sigma_{\rm bg})^{-1}$ relative to the full harmonic fit
- [[concepts/matched_filter_vs_power]] — Sec.~9 makes the point that "not caring about source direction" (nuisance marginalization) is not the same as "compressing to $C_L$" (lossy compression)
- [[concepts/shot_noise]] — not explicitly named but implicit: the single-source model is the proto-shot-noise term; $q_{\max}$ is the source power that drives the hierarchy

## Current paper citations

- `paper/sections/three_strategies.tex:61` — `\fromnotebook{... Secs.~4--4.4}` — coherent Fisher block structure and $D_{\rm coh}\propto p$
- `paper/sections/three_strategies.tex:110` — `\fromnotebook{... Secs.~5--5.5}` — incoherent Fisher, orthogonalization, $D_{\rm inc}\propto p^2$
- `paper/sections/three_strategies.tex:142` — `\fromnotebook{... Secs.~8--9}` (combined with `pta_point_source_vs_CL_note.md`) — full harmonic vs $C_L$-only Fisher and $D_{C_\ell}\propto p^4$

## Potential additional uses

- Introduction section: the block-diagonal coherent Fisher (Sec.~4.2) is the cleanest single equation to introduce the coherent/incoherent distinction — usable as a display equation before the hierarchy table.
- Supplementary appendix on parameter regularity: Sec.~4.5 on $p$ being a non-regular coordinate is a natural appendix note explaining why the paper works with $q$ or $a$ locally.
- Discussion / comparison with NANOGrav 15yr: the $C_L$-only error ratio formula (Sec.~9) could be evaluated numerically for NANOGrav parameters ($N_p=67$, $s_L$ from `conventions.md`) to give a concrete penalty factor.

## Relations to other sources

- `pta_point_source_vs_CL_note.md` — joint citation at line 142; that note presumably carries the $C_\ell$ signal model; this note carries the Fisher framework. Together they underpin the full $D_{C_\ell}\propto p^4$ argument.

## Caveats / open questions

- Sec.~8 writes $F_{pp}^{\rm full}=\Sigma_{\rm bg}^2\sum_{L\ge1}s_L(N_p,\beta)$. The note does not specify whether the $s_L$ here are the same as those tabulated in `conventions.md` (noise-dominated, $\beta=0$). The conventions table gives exact values for $N_p=67$; if those are the intended values this formula is numerically grounded, but the identification should be verified against the code before citing it numerically.
- The $C_L$-only Fisher (Sec.~9) uses $\mathcal{I}_d(0)=1/(2d)$ for the noncentral $\chi^2_d$ information at zero noncentrality. This is a standard result but is asserted without derivation; if the paper quotes the error ratio, a footnote verifying this identity is advisable.
- The note works in a single frequency bin throughout. Multi-frequency generalization (sum over bins, correlated noise) is not addressed. The paper likely sums over bins; confirm that the $p$-scaling exponents are unchanged.

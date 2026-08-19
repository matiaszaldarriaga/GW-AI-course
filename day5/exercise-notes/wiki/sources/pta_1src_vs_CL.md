# Point-source fit vs. $C_\ell$-only compression: Fisher hierarchy and scaling

**Source:** `references/pta_point_source_vs_CL_note.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

This note derives the key scaling difference between two strategies for constraining the
[[concepts/brightest_source_fraction]] $p$ in the noise-dominated uniform-array benchmark. The first
strategy fits all harmonic coefficients $p_{LM}$ directly (the full one-source template); the
second compresses each block $L$ to its rotationally invariant power $C_L^P = |{\mathbf x}_L|^2$
before fitting. The central result is that the full-fit [[concepts/fisher_hierarchy|Fisher information]]
$F_{pp}^{\rm full}$ is independent of $p$, while the [[concepts/Cl_over_C0|$C_L$-only]] Fisher
information $F_{pp}^{(C_L)} \propto p^2$ in the small-signal regime. Consequently the
[[concepts/KL_divergence]] scales as $D_{\rm full} \propto p^2$ but $D_{C_\ell} \propto p^4$ — the
origin of the $p^2$ vs. $p^4$ hierarchy. A secondary result: treating the source direction as an
unknown nuisance parameter in the full fit does not degrade $\sigma_p$ in the isotropic
benchmark, because the cross-Fisher terms $F_{p\theta}$ and $F_{p\phi}$ vanish identically by
the addition theorem. This is a clean separation between nuisance-parameter marginalization
(lossless) and lossy data compression (harmful). The note also provides numerical tables of the
[[concepts/s_L_block_weights]] $s_L(N_p, 0)$ for $L = 1,\dots,10$ and $N_p = 5,\dots,50$, and exact
ratios $\sigma_p^{(C_L)}/\sigma_p^{\rm full}$ confirming the $C_L$-only strategy is worse by
factors of roughly 4–7 at $p^2 = 0.1$–$0.2$ and $\Sigma_{\rm bg} = 1$.

## Key equations and claims

**Sec. 1 — Block weights and SNR**

$$s_L(N_p,0) = \frac{2L+1}{4\pi}\, \frac{D_L + (N_p-1) O_L}{1 + (N_p-1)/48}, \qquad D_1=\pi,\ D_2=\pi/25,\ D_{L\ge 3}=0.$$

For a single point source, $C_L^P / C_0^P = p^2$ for all $L \ge 1$, giving per-block SNR$_L^2 = p^2 \Sigma_{\rm bg}^2 s_L$.

**Sec. 3 — Full fit Fisher information (direction-independent)**

$$F_{pp}^{\rm full} = \Sigma_{\rm bg}^2 \sum_{L\ge 1} s_L.$$

This is $p$-independent. Nuisance-parameter marginalization over the source direction does not change this because $F_{p\theta} = F_{p\phi} = 0$ by the $SH$ addition theorem ($\partial_\theta \sum_M |Y_{LM}|^2 = 0$).

**Sec. 4–5 — $C_L$-only Fisher via noncentral chi-square**

Each compressed block $R_L = |{\mathbf x}_L|^2 \sim \chi'^2_{2L+1}(\lambda_L)$ with $\lambda_L = p^2 \Sigma_{\rm bg}^2 s_L$. The exact [[concepts/fisher_hierarchy|Fisher information]] is:

$$F_{pp}^{(C_L)} = \sum_{L\ge 1} \left(2p\,\Sigma_{\rm bg}^2 s_L\right)^2 \mathcal{I}_{2L+1}\!\left(p^2\Sigma_{\rm bg}^2 s_L\right),$$

where $\mathcal{I}_d(\lambda)$ is the Fisher information of a noncentral $\chi^2_d$ with respect to $\lambda$.

**Sec. 5 — Small-signal ($\lambda_L \ll 1$) expansion**

Using $\mathcal{I}_d(0) = 1/(2d)$:

$$F_{pp}^{(C_L)} \approx 2p^2 \Sigma_{\rm bg}^4 \sum_{L\ge 1} \frac{s_L^2}{2L+1} + O(p^4),$$

so $F_{pp}^{(C_L)} \propto p^2$. Combined with the $p^2$ pre-factor in the KL relation $D \approx (1/2)p^2 F_{pp}$, this gives $D_{C_\ell} \propto p^4$.

**Sec. 6 — Error ratio (exact and small-$\lambda$ approximation)**

$$\frac{\sigma_p^{(C_L)}}{\sigma_p^{\rm full}} \approx \frac{1}{\sqrt{2}\,p\,\Sigma_{\rm bg}} \sqrt{ \frac{\sum_L s_L}{\sum_L s_L^2/(2L+1)} }.$$

Numerically at $\Sigma_{\rm bg}=1$: ratio $\approx 5.6$–$7.1$ for $p^2=0.1$; $\approx 4.1$–$5.1$ for $p^2=0.2$.

**Sec. 7 — Conceptual distinction**

Marginalizing over unknown direction (nuisance parameter) $\ne$ compressing to $C_L^P$ (lossy). The first is lossless in the isotropic benchmark; the second changes the scaling with $p$.

## Concepts touched

- [[concepts/Cl_over_C0]] — $C_L^P/C_0^P = p^2$ for a point source; the note works exclusively with source-sky $C_\ell^{(P)}$, not pulsar-map $C_\ell^{(b)}$
- [[concepts/s_L_block_weights]] — full table for $L=1\dots10$, $N_p=5,10,15,20,30,40,50$
- [[concepts/brightest_source_fraction]] — $p$ is the central parameter being constrained
- [[concepts/fisher_hierarchy]] — the $p^0$ vs. $p^2$ Fisher scaling is the origin of the full $p^2$ vs. $p^4$ KL hierarchy
- [[concepts/KL_divergence]] — KL scales as $p^4$ for $C_\ell$-only because $F_{pp}^{(C_L)} \propto p^2$
- [[concepts/N_eff]] — implicitly present through $\Sigma_{\rm bg}^2$ and population discussion
- [[concepts/shot_noise]] — $\lambda_L \ll 1$ regime corresponds to shot-noise-limited single-source detection
- [[concepts/matched_filter_vs_power]] — Sec. 7 is a clean statement of this distinction: matched filter (full $p_{LM}$ fit) vs. power estimator ($C_L^P$ compression)
- [[concepts/coherent_vs_incoherent]] — the incoherent limit is $C_L$-only; the note shows the explicit Fisher cost

## Current paper citations

- `paper/sections/three_strategies.tex:142` — `\fromnotebook{...}` combined with `pn_coh_vs_incoh_fisher`; supports the incoherent-vs-$C_\ell$ comparison
- `paper/sections/three_strategies.tex:188` — `\fromnotebook{... Secs.~3--5}` deriving the Fisher hierarchy; Secs. 3–5 of this note are the canonical source for the $p^4$ scaling and the $\sigma_p^{(C_L)}/\sigma_p^{\rm full}$ formula

## Potential additional uses

- Numerical values in Sec. 6 table ($\sigma$ ratio $\sim 5$–$7$ at $p^2=0.1$) could support a quantitative sentence in the abstract or introduction
- The $s_L(N_p, 0)$ table (Sec. 2) could underpin a standalone table in an appendix for readers who want to reproduce the block-weight scaling
- The analytic ratio formula at the end of Sec. 5 provides a clean single-equation summary suitable for a paper display equation
- Sec. 7 (nuisance marginalization vs. lossy compression) could support a pedagogical paragraph distinguishing the two operations wherever that confusion is likely to arise for a referee

## Relations to other sources

- **`pn_coh_vs_incoh_fisher`** (cited alongside at line 142): that note presumably derives the incoherent $\propto p^2$ Fisher; together they establish the three-level hierarchy coherent ($p^0$) > incoherent ($p^2$) > $C_\ell$ ($p^4$)
- The $s_L$ table here extends the values quoted in `wiki/conventions.md` (which lists $N_p=67$ only) to a broader $N_p$ grid

## Caveats / open questions

- The exact pair-average formula for $O_L$ (the off-diagonal contribution to $s_L$) is not derived in this note; it is stated as a result from an earlier note. That derivation source should be identified and ingested.
- The note works in the noise-dominated limit ($\beta \to 0$). The KL scaling $D_{C_\ell} \propto p^4$ is derived in this limit; it would be worth checking whether the $p^4$ exponent persists at finite signal-to-background ratio.
- $\mathcal{I}_d(\lambda)$ is stated but not given a closed form. The note uses a numerical evaluation; a closed form or tight bound would make the analytic scaling argument self-contained.
- The note does not address how truncation at finite $L_{\max}$ (e.g., $L_{\max}=6$ in NANOGrav 15yr) affects the ratio; the sums are cut at $L=10$ here but the NANOGrav analysis would cut at 6.
- The note is for $C_\ell^{(P)}$ (source-sky power). It makes no mention of $C_\ell^{(b)}$ (pulsar-map power). Any reader coming from the NANOGrav literature should be reminded of the transfer-function factor before applying these ratios to published NANOGrav [[concepts/Cl_over_C0]] values.

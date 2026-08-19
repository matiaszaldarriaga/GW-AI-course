# Coherent vs Quadratic PTA Searches: KL Divergence Hierarchy

**Source:** `references/pedagogical_note_coherent_vs_quadratic_pta.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

This self-contained note places coherent matched-filter searches and covariance/anisotropy searches on the same footing using the [[concepts/KL_divergence]] as the single figure of merit. The central result is that a coherent search (source lives in the data mean) has KL divergence $D_{\rm mean} = \rho_{\rm coh}^2$, while a covariance search (source marginalized to second moments, isotropic level floated) has $D_{\rm cov} \approx \tfrac{1}{2}\rho_{\rm coh}^4$ for a rank-one source. For many sources the covariance channel scales as $\sum_s p_s^2 \approx p_\star^2$ ([[concepts/brightest_source_fraction]]), while the coherent channel scales as $p_\star$. The note also derives the incoherent pulsar-map dipole $C_1^{(b)}/C_0^{(b)} = \tfrac{1}{4}\sum_s p_s^2$ from the Legendre expansion of the beam kernel, and explains why the pulsar term enters the covariance level directly (no phase coherence across pulsars). Section 12 gives the information-theoretic bound: any quadratic compression of the data carries at most as much detection power as the full coherent likelihood.

## Key equations and claims

- **Coherent KL** (Secs. 3-4): $D_{\rm mean} = \rho_{\rm coh}^2 = |A|^2\,u^\dagger C_0^{-1}u$. Linear in source power; linear in $p_\star$ at fixed total signal-to-background $\eta = Q/(B+N)$.

- **Covariance KL after floating isotropic level** (Sec. 6.3):
  $$D_{\rm cov}^{+} = \tfrac{1}{2}\!\left[\mathrm{tr}(A^2) - \tfrac{(\mathrm{tr}A)^2}{n}\right] + O(A^3),$$
  where $A = C_0^{-1/2}\Delta C\,C_0^{-1/2}$. The linear term cancels because $\lambda$ floats.

- **Rank-one sharpening** (Sec. 7.1): $D_{\rm cov} \approx \tfrac{1}{2}(1-1/n)\rho_{\rm coh}^4$. Covariance is the quadratic descendant of the coherent channel.

- **Many-source covariance** (Sec. 8): $\langle D_{\rm cov}\rangle \approx \tfrac{Q^2 g_2}{2}\sum_s p_s^2$. Universal control parameter is $\sum_s p_s^2$.

- **Incoherent dipole** (Sec. 9): $C_1^{(b)}/C_0^{(b)} = \tfrac{1}{4}\mathbb{E}[|\mathbf{S}|^2] = \tfrac{1}{4}\sum_s p_s^2$. Legendre expansion of $T(x)=[(1+x)/4]^2$ gives coefficients $\{1/12,\, 1/8,\, 1/24\}$ for $\{P_0, P_1, P_2\}$.

- **Low-rank effective rank** (Sec. 11): $r_{\rm eff} = (\mathrm{tr}A)^2/\mathrm{tr}(A^2)$; $D_{\rm cov}^+ \approx (\mathrm{tr}A)^2[1/r_{\rm eff}-1/n]/2$. Low rank boosts the prefactor but does not change the $p^2$ order.

- **Summary scaling** (Sec. 13): $D_{\rm mean}\sim\eta p_\star$, $D_{\rm cov}\sim\eta^2 p_\star^2$, $C_1/C_0\sim p_\star^2$.

- **Information bound** (Sec. 12): coherent search $\ge$ any quadratic compression, as a consequence of data-processing inequality.

## Concepts touched

- [[concepts/KL_divergence]] — defined as figure of merit, forward and reverse forms, weak-signal equivalence shown
- [[concepts/coherent_vs_incoherent]] — Gaussian marginalization as the exact bridge from mean-shift to covariance-shift model
- [[concepts/brightest_source_fraction]] — enters coherent channel at first order, covariance channel at second order
- [[concepts/matched_filter_vs_power]] — matched-filter noncentrality equals KL divergence in Gaussian model
- [[concepts/shot_noise]] — implicit: concentration of $\sum p_s^2$ controlled by shot noise in the source population
- [[concepts/Cl_over_C0]] — derived explicitly: $C_1^{(b)}/C_0^{(b)}=\tfrac{1}{4}\sum_s p_s^2$ (pulsar-map convention)
- [[concepts/fisher_hierarchy]] — Fisher vs KL distinction: $F_{pp}^{(C_\ell)}\propto p^2$ means $D_{C_\ell}\propto p^4$, not $p^2$
- [[concepts/transfer_function]] — Legendre decomposition of $T(x)$ maps source-sky to pulsar-map $C_\ell$
- [[concepts/prior_sensitivity]] — Gaussian prior on amplitudes is exact only if the true distribution is Gaussian; higher moments discarded

## Current paper citations

None yet — list "None" if empty.

None.

## Potential additional uses

This note is the cleanest derivation in the project of the $p$ vs $p^2$ scaling. Sections worth citing in the paper:

- **Introduction / abstract framing**: Sec. 13 summary scaling table ($D_{\rm mean}\sim\eta p_\star$, $D_{\rm cov}\sim\eta^2 p_\star^2$) is a one-line statement of the paper's core claim.
- **Fisher vs KL bug section** (wherever the paper discusses the corrected $p^4$ scaling for $C_\ell$-only): Sec. 6.3 shows explicitly why the linear term cancels when $\lambda$ floats, which is why $D_{C_\ell}\propto p^4$ not $p^2$.
- **Dipole analysis section**: Sec. 9 derives $C_1^{(b)}/C_0^{(b)}=\tfrac{1}{4}\sum_s p_s^2$ from first principles; it is the direct source for this formula.
- **Information-theoretic bound section**: Sec. 12 provides the formal data-processing-inequality argument for coherent $\ge$ quadratic that the paper invokes as motivation.
- **Pulsar term vs Earth term discussion**: Secs. 10.1-10.2 explain why pulsar-term anisotropy starts at $p^2$ while Earth-term coherent detection starts at $p$.
- **Low-rank refinement**: Sec. 11 ($r_{\rm eff}$ formula) could be cited wherever the paper distinguishes the prefactor advantage of low-rank from the order-of-magnitude hierarchy.

## Relations to other sources

- Complements `references/` notes on the Fisher hierarchy and $s_L$ block weights ([[concepts/s_L_block_weights]]): those notes compute the numerical $s_L$ values; this note provides the KL-level explanation for why $C_\ell$ compression costs a further factor of $p^2$.
- The Legendre decomposition of $T(x)$ in Sec. 9 should be cross-checked against the exact pair-average integrals (see `wiki/conventions.md` and pending `sources/pta_exact_pair_average.md`).
- [[concepts/sqrt_SH_basis]]: the note does not use the sqrt-SH parametrization; the prior effects of that parametrization ([[concepts/prior_sensitivity]]) are a separate but related concern not addressed here.
- [[concepts/source_background_degeneracy]]: Sec. 6 (floating $\lambda$) is the formal description of why the isotropic background amplitude must be profiled out before anisotropy sensitivity is meaningful.
- [[concepts/N_eff]]: the many-source covariance result ($\sum_s p_s^2 = 1/N_{\rm eff}$) links this note directly to the effective-number-of-sources concept.

## Caveats / open questions

- Sec. 9 uses the notation $C_1/C_0$ without specifying pulsar-map vs source-sky convention. The formula $C_1/C_0 = \tfrac{1}{4}\sum_s p_s^2$ matches the pulsar-map convention in `wiki/conventions.md` ($C_1^{(b)}/C_0^{(b)} = \tfrac{1}{4}C_1^{(P)}/C_0^{(P)}$ at $\ell=1$ with $C_1^{(P)}/C_0^{(P)}=\sum_s p_s^2$). This is consistent but should be stated explicitly if this note is cited in the paper.
- The note derives $D_{\rm cov}$ for the case where $\lambda$ (isotropic amplitude) is profiled out. If the paper uses a different profiling convention (e.g., fixing total power), the prefactor changes; Secs. 6.2-6.3 should be re-read in that context.
- $g_2$ (the angle-averaged trace in Sec. 8) is left symbolic. Its numerical value for the NANOGrav array and the HD kernel is not computed in this note; it maps to the $s_L$ prefactors computed elsewhere.
- The Gaussian-prior construction (Sec. 5) is exact only for Gaussian amplitude distributions. The note flags this explicitly, but the paper should be careful not to quote the covariance KL as a tight bound for non-Gaussian populations.

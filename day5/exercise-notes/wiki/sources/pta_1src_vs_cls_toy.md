# Fisher matrix: one-source model vs C_L anisotropy spectrum (toy benchmark)

**Source:** `references/pta_covariance_fisher_one_source_vs_cls_toy.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

Derives the exact covariance Fisher matrix for PTA anisotropy searches in a single frequency bin, comparing two model families: (1) a general spherical-harmonic expansion of the source-power sky P(n-hat) parametrized by coefficients p_{LM}, and (2) a one-source model parametrized by amplitude p and direction. The note introduces the block-weight s_L as the canonical sensitivity measure, shows that SNR_L^2 = Sigma_bg^2 * s_L * C_L^P / C_0^P, and evaluates numerically (N_p=20, beta=1) that the dipole captures only ~43% of the one-source amplitude information when L <= 6. A central message: the "dipole is nearly enough" intuition holds for the diagonal/incoherent |z|^2 compression but NOT for the full covariance matrix.

## Key equations and claims

- **Covariance perturbation kernel** (Sec. 2): K^E_{ab}(n-hat) = [2(mu_{ab} - x_a x_b)^2 - (1 - x_a^2)(1 - x_b^2)] / [4(1-x_a)(1-x_b)], with pulsar-term factor giving K^tot_{ab} = (3/2)(1 + delta_{ab}) K^E_{ab}.
- **Gaussian Fisher matrix** (Sec. 1): F_{alpha beta} = (1/2) Tr[C_0^{-1} (d_alpha Delta_C) C_0^{-1} (d_beta Delta_C)].
- **Response matrices** (Sec. 3): K^{LM}_{ab} = integral d^2 Omega Y_{LM}(n-hat) K^tot_{ab}(n-hat); Fisher for p_{LM} coefficients is F^{(p)}_{LM,L'M'} = A^2 G_{LM,L'M'}.
- **C_L^P not fundamental** (Sec. 3.1): Fisher is for p_{LM}, not C_L^P; collapsing to C_L^P requires additional symmetry assumption.
- **Block weight definitions** (Sec. 6.1): r_L = (1/(2L+1)) sum_M <(1/2)Tr[C_0^{-1} K^{LM} C_0^{-1} K^{LM,dagger}]> / F_A; s_L = ((2L+1)/(4pi)) r_L.
- **SNR per block** (Sec. 6.2): SNR_L^2 = Sigma_bg^2 * s_L * C_L^P / C_0^P, so threshold C_L^P / C_0^P ~ 1 / (Sigma_bg^2 * s_L).
- **One-source pole expansion** (Sec. 9): p_{L0}^{1src} = p * sqrt((2L+1)/(4pi)), contributing to every L with no extra suppression beyond array response.
- **One-source Fisher** (Sec. 9): F_pp^{1src} = Sigma_bg^2 * sum_{L>=1} s_L; dipole fraction = s_1 / sum_{L>=1} s_L.
- **Time-delay map smoothness** (Sec. 7): z_{lm} ~ sqrt[(l-2)!/(l+2)!], so C_l^z ~ 1/[(l+2)(l+1)l(l-1)]; high-L covariance response suppressed via Gaunt convolution.
- **Diagonal/incoherent contrast** (Sec. 10.1): G_L ~ L^{-2}, C_L^{|z|^2} ~ L^{-4}; and C_1^{|z|^2} = (1/4) C_0^{|z|^2}, C_2^{|z|^2} = (1/100) C_0^{|z|^2}.
- **Numerical benchmark** (Sec. 10, N_p=20, beta=1): s_1 ~ 0.845, s_2 ~ 0.415, s_3 ~ 0.267, s_4 ~ 0.185, s_5 ~ 0.135, s_6 ~ 0.096. Dipole captures ~43% of 1-src information at L<=6; L<=2 captures ~65%; L<=4 captures ~88%.

## Concepts touched

- `s_L_block_weights` — derived here from first principles; SNR_L^2 formula is the central result
- `fisher_hierarchy` — establishes that C_L^P Fisher is secondary to p_{LM} Fisher
- `matched_filter_vs_power` — explicit comparison of full covariance (matched to 1-src) vs C_L compression
- `coherent_vs_incoherent` — Sec. 10.1 cleanly separates full covariance from diagonal/incoherent |z|^2
- `Cl_over_C0` — SNR threshold expressed as C_L^P / C_0^P ~ 1/(Sigma_bg^2 s_L)
- `transfer_function` — Sec. 7 derives suppression of K^{LM} via Gaunt convolution from smoothness of z
- `brightest_source_fraction` — p enters as the one-source amplitude parameter throughout Sec. 4 and 9
- `shot_noise` — finite N_p adds angular-resolution suppression distinct from intrinsic z-smoothness (Sec. 8)
- `sqrt_SH_basis` — not explicitly discussed, but C_L^P vs C_L^{|z|^2} distinction is directly relevant

## Current paper citations

(None yet.)

## Potential additional uses

- **Section deriving s_L / block-weight formalism**: cite when introducing SNR_L^2 = Sigma_bg^2 s_L C_L^P/C_0^P.
- **Section on KL / Fisher hierarchy**: cite when arguing C_L compression is lossy relative to full covariance or one-source fit; supports p^4 scaling claim via C_L-only Fisher depending on p.
- **Dipole fraction formula** (s_1 / sum s_L): cite if paper discusses how much signal a dipole-only search recovers.
- **Diagonal vs full covariance contrast** (Sec. 10.1): cite as quantitative support for the incoherent vs C_L distinction in the three-strategy hierarchy.

## Relations to other sources

**Overlap — flag:**
- `pta_point_source_vs_CL_note.md`: That note likely covers the same one-source vs C_L comparison from a different angle. The present note is more systematic (derives exact Fisher for p_{LM}, then specializes). Check whether the C_1^{|z|^2} = (1/4) C_0^{|z|^2} result appears in both; if so the notes are redundant for that claim.
- `pta_covariance_exact_pair_average_note.md`: That note provides the exact pair-averaging machinery for O_L integrals that underpins the numerical s_L values. The present note cites the same benchmark but derives s_L from the block-averaged Fisher formula; both must agree on the numerical values for N_p = 67 (see conventions.md table).

**Non-overlapping context:**
- `wiki/conventions.md` block-weights table (N_p=67) provides the canonical s_L values this note's formulas define. The numerical benchmark here uses N_p=20; the two should not be compared directly without noting the N_p dependence.

## Caveats / open questions

- The numerical values in Sec. 10 use N_p=20, beta=1. The conventions.md canonical table uses N_p=67, beta=0 (noise-dominated limit). It is not stated whether the note's r_L values were verified against independent code; until confirmed, treat them as illustrative rather than reference numbers.
- The note states that "the precise asymptotic form is harder to derive in closed form" for the full covariance kernel (Sec. 7). The exact scaling of s_L at large L is therefore not analytically established in this note — it is inferred by smoothness argument.
- Sec. 8 invokes the empirical l_max ~ sqrt(N_psr) scaling from NANOGrav, but does not derive it from the block-weight formula. The connection between s_L saturation and angular resolution cutoff is asserted, not proven here.
- The note does not explicitly connect the Fisher for p_{LM} to the KL divergence figure of merit used in the paper. The note's F_pp^{1src} is a Fisher quantity; the paper's hierarchy is stated in terms of KL scaling with p. The translation D ~ (1/2) p^2 F_pp applies only when F_pp is p-independent (see conventions.md); this note does not check that condition for the one-source case.

# Noise-dominated Fisher blocks for PTA covariance anisotropy

**Source:** `references/pta_covariance_fisher_noise_dominated_limit.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

Derives the complete Fisher-matrix machinery for PTA covariance anisotropy searches
in the noise-dominated benchmark beta = A/sigma_n^2 -> 0. In this limit C_0^{-1}
reduces to sigma_n^{-2} I, making the Fisher matrix tractable. The note establishes
three exact results: (1) the isotropic-background Fisher denominator Sigma_bg^2,
(2) the analytic diagonal contributions D_L (non-zero only for L=1,2), and (3) the
exact pair-average integral formula for the off-diagonal contributions O_L. Numerical
quadrature gives O_L for L=1..8. A Monte Carlo check at the percent level confirms
the pair-count decomposition for N_p = 10, 20, 50, 100. The note also explains why
Fisher information grows as N_p^2 (more pulsars per pixel reduces pixel noise) and
why higher multipoles L >= 3 are accessible through pairwise products of response
maps even though the direct time-delay map z is smooth (C_l^z ~ l^{-4}).

## Key equations and claims

- **Exact isotropic denominator** (Sec. 3, boxed):
  Sigma_bg^2 = (A^2 N_p / 2 sigma_n^4)(1 + (N_p - 1)/48).
  The 1/48 is the Legendre-series integral G = (1/2) int_{-1}^{1} chi(mu)^2 dmu,
  computed analytically from the HD curve coefficients a_l.

- **Block-averaged Fisher weight** (Sec. 4):
  F_bar_L = (A^2 / 2 sigma_n^4) N_p [D_L + (N_p - 1) O_L].

- **Block weight ratio** (Sec. 4, boxed):
  s_L(N_p, 0) = ((2L+1)/4pi) * (D_L + (N_p-1) O_L) / (1 + (N_p-1)/48).

- **Per-multipole SNR** (Sec. 4, boxed):
  SNR_L^2 = Sigma_bg^2 * s_L(N_p, 0) * C_L^P / C_0^P.

- **Analytic diagonal terms** (Sec. 5):
  D_1 = pi, D_2 = pi/25, D_{L>=3} = 0.
  Follows from the Legendre decomposition of the single-pulsar kernel
  (3/4)(1 + x)^2 = 1 + (3/2)P_1(x) + (1/2)P_2(x).

- **Exact off-diagonal formula** (Sec. 6, boxed):
  O_L = (1/2) int_{-1}^{1} dmu (1/(2L+1)) sum_m |K^0_{Lm}(mu)|^2,
  where K^0_{Lm}(mu) are the SH coefficients of the cross-pair kernel in the
  computational frame with p_a = z-hat; rotation invariance of sum_m |K_{Lm}|^2
  is the key that makes this frame-independent.

- **Numerically evaluated O_L** (Sec. 6.1, from direct quadrature):
  O_1 = 0.03774257, O_2 = 0.07891959, O_3 = 0.03598248,
  O_4 = 0.01846344, O_5 = 0.00968579, O_6 = 0.00538058.

- **Diagonal/off-diagonal crossover** (Sec. 8):
  Dipole transitions to pair-dominated at N_p ~ 84; quadrupole is pair-dominated
  already at N_p ~ 2.6. For N_p ~ 67 (NANOGrav 15yr), dipole is mixed, quadrupole
  is pair-dominated.

- **Resulting s_L for N_p = 67** (Sec. 9):
  s_1 ~ 0.566, s_2 ~ 0.894. Quadrupole block exceeds dipole block in this benchmark.

- **Empirical high-L scalings** (Sec. 10, NOT proved analytically):
  O_L ~ L^{-3} and s_L ~ L^{-2} for L >= 3 in the large-N_p regime.

## Concepts touched

- fisher_hierarchy
- s_L_block_weights
- coherent_vs_incoherent
- matched_filter_vs_power
- shot_noise

## Current paper citations

(None yet.)

## Potential additional uses

- Section deriving the noise-dominated benchmark formula for Sigma_bg^2 could be
  cited wherever the paper invokes the (A^2 N_p / 2 sigma_n^4)(1 + (N_p-1)/48) result.
- The s_L table and the quadrupole > dipole finding could anchor any figure or table
  showing per-multipole block weights vs N_p.
- The N_p^2-scaling explanation (pixel-averaging argument, Sec. 3.1) is a concise
  rebuttal to the intuition that information should saturate with array size.
- The exact off-diagonal formula (Sec. 6) is the reference for any code implementing
  O_L quadrature; the companion Python file `pta_covariance_exact_pair_average_checks.py`
  implements these checks.

## Relations to other sources

- **Companion note** `references/pta_covariance_exact_pair_average_note.md` (not yet
  ingested as a wiki page): significant content overlap. Both derive the block-weight
  formulas and the exact pair-average integral. The present note focuses on the
  beta -> 0 benchmark and provides the analytic diagonal terms and the crossover
  analysis; the companion note likely treats the exact (finite-beta) covariance. When
  the companion is ingested, duplicate derivations should be noted explicitly and
  one page should defer to the other on shared formulas.
- `wiki/sources/pn_coh_vs_incoh_fisher.md`: the s_L weights and Sigma_bg^2 appear
  there in the context of comparing coherent vs incoherent strategies; the present
  note is the primary derivation of those quantities.
- `wiki/sources/pta_1src_vs_CL.md`: uses the SNR_L^2 = Sigma_bg^2 s_L C_L^P/C_0^P
  formula to compare the one-source signal against C_L compression.

## Caveats / open questions

- The asymptotic O_L ~ L^{-3} and s_L ~ L^{-2} scalings (Sec. 10) are stated as
  observed numerically, not proved. The note is explicit: "I have not derived this
  analytically." Do not cite these as established results until a proof exists.
- The full all-L sum sum_L s_L has no closed analytic form yet (Sec. 11). The exact
  coding route is the pair-average integral.
- The note uses the pulsar-term-corrected kernel K^tot with factor (3/2)(1 + delta_{ab}).
  Verify that downstream code uses the same convention before comparing O_L values.
- The 1/48 identity is exact by the Legendre-series computation; confirm that any
  code computing G by numerical quadrature of chi(mu)^2 agrees to machine precision
  with 1/48 before using the analytical value in production formulas.

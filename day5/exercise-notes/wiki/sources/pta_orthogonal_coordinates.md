# Orthogonal coordinates for PTA common-process fits

**Source:** `references/pta_orthogonal_coordinates_note.md`
**Type:** pedagogical note
**Ingested:** 2026-04-15

## Summary

The note constructs a locally orthogonal coordinate system around a CURN fiducial point for PTA common-process fits. Three problems are addressed in sequence: (1) maintaining a globally positive-definite covariance during sampling via a correlation-fraction parameter $r \in [0,1]$; (2) removing the amplitude-slope shear within each power-law spectral plane by choosing an optimal pivot frequency; and (3) separating the diagonal common-process sector into a robust combination (data-driven) and a prior-sensitive combination (lifted by nuisance priors). The key structural result is that $r$, which controls the CURN-to-HD transition, is exactly Fisher-orthogonal to all block-diagonal parameters at $r=0$: a direct consequence of the block-cross vs block-diagonal decomposition of the HD covariance. The nuisance-orthogonal diagonal combinations are obtained from the Schur complement of the full Fisher matrix, and robust vs prior-sensitive directions are identified by a generalized eigenvalue problem.

## Key equations and claims

- **Physical covariance model** (Section 2):
  $C(\Theta) = N(\eta) + e^{u_c} Q_c(\gamma_c; f_{p,c})[(1-r)A + rH]$,
  where $H = A + B$ splits into auto ($A$) and cross ($B$) pieces. $0 \le r \le 1$ keeps the model positive semidefinite by construction.

- **Log-amplitude coordinate** (Section 2):
  $u \equiv \ln(A^2 f_p^{\gamma-3} / 12\pi^2)$ is the pivot-free log coefficient of the covariance contribution. The conventional PTA amplitude $A_\mathrm{gw}$ and $u$ are related by a Jacobian that depends on $\gamma$ and the pivot.

- **Exact orthogonality of $r$ at CURN fiducial** (Section 3):
  $F_{r\eta} = 0$, $F_{ru} = 0$, $F_{r\gamma} = 0$ at $r = 0$.
  The tangent $T_r = e^{u_c} Q_c B$ is purely block-cross; the CURN fiducial covariance inverse is block-diagonal. The trace inner product $\langle T_r, D_a \rangle_0 = 0$ for any block-diagonal tangent $D_a$.

- **Correlation score and local KL** (Section 3):
  $Z_r = U_r / \sqrt{\widetilde{F}_{rr}}$, $\quad D_\mathrm{KL}(r \parallel 0) \simeq \tfrac{1}{2} r^2 \widetilde{F}_{rr}$.

- **Optimal pivot** (Section 4):
  $\Delta_x = -\widetilde{F}_{u\gamma}^{(x)} / \widetilde{F}_{uu}^{(x)}$,
  $\quad f_{p,x}^\mathrm{opt} = f_{p,x} \exp[-\widetilde{F}_{u\gamma}^{(x)} / \widetilde{F}_{uu}^{(x)}]$,
  where $\widetilde{F}^{(x)}$ is the $2 \times 2$ Schur complement for $(u_x, \gamma_x)$ after marginalizing all other parameters.

- **Nuisance-orthogonal diagonal tangents** (Section 5):
  $\bar{D}_a = D_a - \Pi_\eta(D_a)$, with $\Pi_\eta(D_a) = N_\mu (F_{\eta\eta}^{-1} F_{\eta\phi})^\mu{}_a$.
  The marginalized Fisher in the diagonal common sector is the Schur complement:
  $\widetilde{F}_{\phi\phi} = F_{\phi\phi} - F_{\phi\eta} F_{\eta\eta}^{-1} F_{\eta\phi}$.

- **Robust vs prior-sensitive decomposition** (Section 6):
  Prior-agnostic: diagonalize $K v = \lambda G v$ where $G_{ab} = \langle D_a, D_b \rangle_0$ and $K_{ab} = \langle D_a^\parallel, D_b^\parallel \rangle_0$. Eigenvalue $\lambda \in [0,1]$ is the fraction of Fisher norm living in the nuisance space.
  Prior-aware: diagonalize $\Delta_\Lambda v = \kappa \widetilde{F}^{(\Lambda)}_{\phi\phi} v$ where $\Delta_\Lambda = F_{\phi\eta}[F_{\eta\eta}^{-1} - (F_{\eta\eta} + \Lambda_{\eta\eta})^{-1}] F_{\eta\phi}$ measures the information supplied by the nuisance prior.

- **Full local coordinate set** (Section 7):
  $(r, \chi_\mathrm{robust}, \chi_\mathrm{prior}, \tilde\eta)$ at the CURN point.

## Concepts touched

- [[concepts/prior_sensitivity]] — central topic: Sections 5–6 develop the prior-sensitivity diagnostic for the diagonal common sector
- [[concepts/KL_divergence]] — correlation information $D_\mathrm{KL}(r \parallel 0) \simeq \tfrac{1}{2}r^2 \widetilde{F}_{rr}$ (Section 3)
- [[concepts/fisher_hierarchy]] — the Schur-complement construction and the block-cross orthogonality are the geometric core of the Fisher hierarchy
- [[concepts/coherent_vs_incoherent]] — the CURN-vs-HD split ($r=0$ vs $r=1$) is the diagonal-vs-cross decomposition that underlies the coherent/incoherent distinction
- [[concepts/source_background_degeneracy]] — the nuisance-orthogonal diagonal common process is precisely the direction that is not degenerate with per-pulsar noise
- [[concepts/transfer_function]] — pivot optimization in Section 4 is a frequency-space transfer-function reparametrization of the spectral plane
- [[concepts/matched_filter_vs_power]] — $r$ isolates cross-correlation information (matched-filter channel); diagonal coordinates carry the power-like channel

## Proposed new concepts

- **`CURN_HD_split`**: the decomposition $H = A + B$ into auto and cross pieces, parametrized by $r$, is a recurring structural object not yet in the vocabulary list. The exact orthogonality of $r$ to all block-diagonal parameters at $r=0$ is a central result that deserves its own concept page.
- **`pivot_optimization`**: the Schur-complement formula for the optimal pivot frequency of a power-law process ($f_{p,x}^\mathrm{opt}$) is a self-contained diagnostic. Currently subsumed under `transfer_function` but distinct: it is a local reparametrization, not a sky-to-pulsar mapping.
- **`nuisance_orthogonal_projection`**: the projection $\bar{D}_a = D_a - \Pi_\eta(D_a)$ and the resulting Schur-complement Fisher appear as a recurring construction (also in `pta_prior_sensitivity.md` for the one-parameter case). The matrix version here is a natural generalization.

## Current paper citations

(None yet.)

## Potential additional uses

- **CURN-to-HD transition section**: the $r$ parametrization and its exact Fisher orthogonality to block-diagonal parameters provides the clean analytic argument for why the CURN and HD posteriors can be compared without worrying about nuisance contamination at $r=0$.
- **Systematic-effects appendix**: the prior-sensitivity diagnostic ($\Delta_\Lambda$ generalized eigenvectors) gives a concrete operational test—vary pulsar-noise priors and check that $\chi_\mathrm{prior}$ moves while $\chi_\mathrm{robust}$ does not. Useful for referee response or an appendix on robustness.
- **Proposal tuning for MCMC**: the local orthogonal chart $(r, \chi_\mathrm{robust}, \chi_\mathrm{prior}, \tilde\eta)$ is a practical starting point for constructing an efficient sampler proposal in PTA analyses.

## Relations to other sources

- `references/pta_toy_models_prior_sensitivity.md` (wiki: `sources/pta_prior_sensitivity.md`): the present note is the direct extension to two diagonal common-process parameters and a full Fisher matrix treatment. The one-parameter $A_\perp$ construction of that note is recovered in Section 5 as the $a=1$ special case of $\bar{D}_a$.
- The block-diagonal vs block-cross decomposition used throughout is the same structural argument as in `sources/pn_coh_vs_incoh_fisher.md` and `sources/pn_coh_vs_quadratic.md` for the coherent vs incoherent Fisher hierarchy.
- The CURN-fiducial setup (Section 3) connects directly to `sources/pta_noise_dominated_limit.md`, which establishes the noise-dominated benchmark at which $C_0$ is block-diagonal.

## Caveats / open questions

- No numerical examples are provided. All results are analytic expressions; a concrete implementation requires a specific PTA dataset and noise model to evaluate $\widetilde{F}_{u\gamma}^{(x)}$, $K$, $G$, and $\Delta_\Lambda$. The note acknowledges this and describes the algorithm (Section 8) but does not apply it.
- The optimal pivot formula (Section 4) uses the Schur complement after marginalizing all other parameters. In practice, computing this for a large PTA requires either analytic block-diagonal simplifications or a numerical evaluation at the fiducial point; the note does not discuss the computational cost.
- The note explicitly states that the $r$ parametrization keeps the model positive semidefinite, but does not prove that the resulting posterior is well-conditioned or that a flat prior on $r$ is physically appropriate. The connection to the prior-sensitivity of $r$ itself is not addressed.
- The generalized eigenvalue diagnostic for prior sensitivity ($\Delta_\Lambda v = \kappa \widetilde{F}^{(\Lambda)}_{\phi\phi} v$) requires a specific choice of nuisance-prior Hessian $\Lambda_{\eta\eta}$. The note does not discuss how sensitive the eigenvectors are to the choice of fiducial prior.

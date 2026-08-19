# Cross-only constraints on the Hellings-Downs amplitude in a one-bin PTA model

**Source:** `references/pta_curn_hd_cross_only_self_contained_v4.md`
**Type:** pedagogical note (v4, self-contained)
**Ingested:** 2026-04-24

## Summary

This note works out, in one frequency bin, the precise relation
between the physical HD-plus-CURN Bayesian posterior and the
cross-only quadratic estimator that is widely used as an "optimal
statistic" for HD detection. The central observation is a
reparameterization: with $P = A_{\rm C} + A_{\rm H}$ (total common
auto-power) and $B = A_{\rm H}$ (amplitude of the off-diagonal HD
pattern) and the split $\Gamma = I + X$ with $X_{ii}=0$, the physical
covariance becomes $C(P,B) = N + PI + BX$. In the local weak-signal
Fisher, $F_{PB}=0$ *exactly* (because $D$ is diagonal and $X_{ii}=0$),
so the Fisher factorizes and the nuisance-projected HD score is
cross-only: $S_{\rm H}^\perp = S_B$ and $F_{\rm H}^\perp = F_{BB}$.
That is the mathematical reason the optimal cross-only quadratic
estimator equals the nuisance-projected HD Fisher score. **But** the
physical nonnegativity prior $A_{\rm C}, A_{\rm H} \ge 0$ maps to the
boundary $P \ge B$, and a pure-GWB-no-CURN truth sits exactly on that
boundary. Enforcing the boundary adds a term
$\log \Phi\!\left((\hat P - B)/\sigma_P\right)$ (or a half-quadratic
penalty in the profiled form) to the $B$-posterior. That term is
*diagonal* information: it matters whenever $\sigma_P \lesssim
\sigma_B$, which in the equal-variance limit is
$(n-1)\overline{X^2} < 1$. The practical upshot: if you want a
genuinely cross-only answer you must change the question — from
"physical $A_{\rm H}$" (bounded, uses autos near the boundary) to
"off-diagonal HD pattern amplitude $B_\times$" (free-sign, uses crosses
only). These are not the same object in the regime where the autos
outconstrain the crosses.

## Key equations and claims

- **Reparametrization** (Sec. 2):
  $\Gamma = I + X$, $X_{ii}=0$; $P = A_{\rm C} + A_{\rm H}$, $B = A_{\rm H}$;
  $C(P,B) = N + PI + BX$.

- **Positive-definiteness vs physical prior** (Sec. 3):
  PD condition is $1 + B \lambda_a(P) > 0$ with $\lambda_a(P)$ eigenvalues
  of $M_P = (N+PI)^{-1/2} X (N+PI)^{-1/2}$. The condition $P \ge B$ is
  *not* the PD condition; it is the image of the physical
  $A_{\rm C}, A_{\rm H} \ge 0$ prior. GWB-no-CURN truth:
  $A_{\rm C}=0 \Rightarrow P_{\rm true} = B_{\rm true}$, on the
  boundary.

- **Scores at the CURN expansion point** $C_0 = N + P_* I$,
  $D = C_0^{-1} = \mathrm{diag}(D_i)$, $D_i = 1/(N_i + P_*)$
  (Secs. 5–6):
  $S_P = \tfrac12 [d^T D^2 d - \mathrm{tr}(D)]$,
  $S_B = \tfrac12 d^T D X D d = \sum_{i<j} D_i D_j X_{ij} d_i d_j$.
  **$S_B$ is cross-only** because $X_{ii}=0$.

- **Fisher matrix** (Sec. 6):
  $F_{PP} = \tfrac12 \sum_i D_i^2$,
  $F_{BB} = \sum_{i<j} D_i D_j X_{ij}^2$,
  $F_{PB} = \tfrac12 \mathrm{tr}(D^2 X) = 0$ **exactly**.
  Hence the local likelihood factorizes:
  $\ell_{\rm loc}(P,B) = \mathrm{const} + S_P \delta P - \tfrac12 F_{PP} \delta P^2
    + S_B B - \tfrac12 F_{BB} B^2$.

- **Profiling = marginalization over unconstrained $P$** (Secs. 7–8):
  $\hat{\delta P} = S_P/F_{PP}$ is $B$-independent; the Gaussian integral
  over $\delta P$ produces a $B$-independent factor. Both give
  $\ell_{\rm prof}(B) = \mathrm{const} + S_B B - \tfrac12 F_{BB} B^2$,
  with cross-only estimator
  $\hat B_\times = S_B / F_{BB}$ and variance $\sigma_B^2 = 1/F_{BB}$.

- **Nuisance projection in the original $(A_{\rm C}, A_{\rm H})$ basis**
  (Sec. 9):
  Efficient score after projecting out $A_{\rm C}$:
  $S_{\rm H}^\perp = S_{\rm H} - (F_{\rm HC}/F_{\rm CC}) S_{\rm C}
    = (S_P + S_B) - S_P = S_B$;
  $F_{\rm H}^\perp = F_{\rm HH} - F_{\rm HC}^2/F_{\rm CC} = F_{BB}$.
  "**The quadratic cross-only estimator is the nuisance-projected HD
  Fisher score.**"

- **Physical-boundary posterior** (Sec. 10):
  $$\log p_{\rm phys}(d|B) = \mathrm{const} + S_B B - \tfrac12 F_{BB} B^2
    + \log \Phi\!\left(\frac{\hat P - B}{\sigma_P}\right),$$
  with $\hat P = P_* + S_P/F_{PP}$. Profiled form:
  $\ell_{\rm phys,prof}(B) = \mathrm{const} - (B - \hat B_\times)^2/(2\sigma_B^2)
    - [\max(0, B - \hat P)]^2 / (2\sigma_P^2)$.

- **When the boundary matters** (Sec. 11):
  Boundary slope near $B = \hat P$ is $(\phi/\Phi)/\sigma_P
    \approx 0.8/\sigma_P$; cross-only scale is $\sigma_B$. So the
  boundary is **important** when $\sigma_P \lesssim \sigma_B$,
  **dominant** when $\sigma_P \ll \sigma_B$. In the
  equal-variance limit $D_i = D$, the criterion is
  $(n-1) \overline{X^2} < 1$, where
  $\overline{X^2} = (2/n(n-1)) \sum_{i<j} X_{ij}^2$.

- **Three-way impossibility** (Sec. 14):
  One cannot simultaneously have (1) a globally physical covariance
  model, (2) nonnegative physical amplitudes, and (3) a posterior for
  the HD amplitude constrained only by crosses. A cross-only answer
  requires reinterpreting the target:
  $C = N + PI + B_\times X$, $P$ independent of $B_\times$ — no longer
  the physical $A_{\rm H}$.

- **Pairwise pseudo-likelihood** (Sec. 13):
  $y_{ij} = d_i d_j$ for $i<j$, $\mathbb{E}[y_{ij}] = B_\times X_{ij}$,
  independent-pair approximation $\mathrm{Var}(y_{ij}) \approx (N_i+P)(N_j+P)$.
  Gaussian pseudo-likelihood reproduces the same $S_\times = S_B$
  and $F_\times = F_{BB}$. Connects the local Fisher picture to the
  standard optimal-statistic formulation.

## Concepts touched

- [[../concepts/source_background_degeneracy]] — central: $F_{PB} = 0$
  exactly at any expansion point (because $D$ is diagonal, $X_{ii}=0$)
  is the same structural orthogonality that makes the coherent
  mean-vs-covariance Fisher block-diagonal. The note elevates this
  to the design principle for the cross-only estimator.
- [[../concepts/coherent_vs_incoherent]] — the nuisance-projected HD
  score $S_B = \sum_{i<j} D_i D_j X_{ij} d_i d_j$ is the canonical
  incoherent/covariance-channel object. The boundary analysis is a
  new subtlety in the incoherent regime.
- [[../concepts/KL_divergence]] — $F_{BB} = \sum_{i<j} D_i D_j X_{ij}^2$
  is the local KL curvature in the $B$ direction around CURN;
  $D_{\rm KL} \simeq \tfrac12 B^2 F_{BB}$ modulo the boundary term.
- [[../concepts/fisher_hierarchy]] — the cross-only quadratic estimator
  is the "incoherent" Fisher object. The criterion
  $(n-1)\overline{X^2} < 1$ is a new quantitative regime where the
  boundary term re-introduces auto-power information that the naive
  cross-only picture ignores.
- [[../concepts/prior_sensitivity]] — the boundary term
  $\log \Phi((\hat P - B)/\sigma_P)$ is literally a prior effect
  arising from $A_{\rm C} \ge 0$. Belongs in the prior-sensitivity
  taxonomy as "hard one-sided boundary on the CURN nuisance
  direction," distinct from the per-pulsar noise-prior effects of
  [[../sources/pta_prior_sensitivity]].
- [[../concepts/matched_filter_vs_power]] — the pairwise pseudo-
  likelihood Sec. 13 is the canonical "quadratic/power" detection
  statistic; the note makes its local-likelihood derivation explicit
  and identifies when its "cross-only" interpretation is genuine vs.
  undermined by the boundary.

## Current paper citations

(None yet — just ingested.)

## Potential paper uses

- **`appendix_fisher.tex`**: the $(P, B)$ reparameterization and
  $F_{PB} = 0$ exact orthogonality provide the clean analytic
  statement of why cross-only estimators are the nuisance-projected
  HD Fisher score. The expressions $F_{BB} = \sum_{i<j} D_i D_j X_{ij}^2$
  and $\hat B_\times = S_B / F_{BB}$ are directly usable. Would
  strengthen the appendix's treatment of the incoherent Fisher.

- **`three_strategies.tex`** (incoherent-strategy discussion):
  the boundary analysis (Sec. 10) and the quantitative criterion
  $(n-1)\overline{X^2} < 1$ (Sec. 12) give a *new regime* where the
  naive cross-only/incoherent picture breaks down for the physical
  HD amplitude. Could motivate a short subsection distinguishing
  "physical $A_{\rm H}$ constraint" (uses autos near boundary) from
  "cross-correlation pattern amplitude $B_\times$ constraint" (genuinely
  cross-only, free-sign).

- **`numerical_estimates.tex`**: compute $(n-1)\overline{X^2}$ for
  NG15 (with $n=67$ and the actual HD $\Gamma$) to determine
  whether the boundary term is numerically important for the NG15
  upper-limit posterior. A single-number plug-in.

- **`discussion.tex`** (or a methodological note):
  the three-way impossibility theorem (Sec. 14) — "physical covariance"
  + "nonnegative amplitudes" + "cross-only HD posterior" cannot all
  hold — is a useful framing that sharpens the distinction between
  the NANOGrav Bayesian HD posterior and the optimal-statistic
  literature.

## Relations to other sources

- [[pn_HD_vs_CURN_Fisher_Bayes]] — immediate companion (ingested
  same day). That note uses $\eta$ as a shape interpolator
  $C(\eta) = N + \Phi \otimes [I + \eta(\Gamma - I)]$ at **fixed**
  common auto-power; the present note uses $(P, B)$ which **allows**
  the common auto-power to float, then exposes the physical boundary
  $P \ge B$ that re-constrains it. The two notes should be read
  together: `pn_HD_vs_CURN_Fisher_Bayes` establishes that the Fisher
  detection forecast is cross-only at fixed $P$; this note shows how
  the one-sided CURN prior reintroduces auto-power information when
  the truth sits on the boundary.
- [[pta_orthogonal_coordinates]] — uses $r \in [0,1]$ as a different
  shape parameter (same structural Fisher orthogonality at $r = 0$).
  All three notes (`pta_orthogonal_coordinates`,
  `pn_HD_vs_CURN_Fisher_Bayes`, this one) converge on the same
  structural fact: $F_{P,\text{shape}} = 0$ at the CURN null because
  the cross direction is orthogonal to the diagonal in pulsar space.
  **Terminology should be unified before any of the three is cited
  in the paper.**
- [[fisher_src_vs_bg_degeneracy]] — the coherent block-diagonality
  ($F_{\alpha, B^2} = 0$ for source-mean vs background-covariance)
  is the *stochastic-process* analog of $F_{PB} = 0$ here: both are
  structural orthogonalities that make nuisance projection trivial at
  the CURN null.
- [[pn_coh_vs_incoh_fisher]] — the canonical derivation of the
  cross-only Fisher in the incoherent channel; the present note
  extends it by tracking the physical boundary.
- [[pta_prior_sensitivity]] — the boundary term
  $\log \Phi((\hat P - B)/\sigma_P)$ is an instance of the
  prior-sensitivity phenomenon for a different nuisance direction
  (CURN amplitude rather than per-pulsar noise scales).
- Standard "optimal statistic" literature (Anholm-Chamberlin-Romano-Siemens
  and successors) is the direct origin of the pairwise pseudo-likelihood
  in Sec. 13. The note does not cite it; adding a paper-level
  reference would require a `verify-reference` pass.

## Caveats / open questions

- All results are analytic; no numerical value of
  $(n-1)\overline{X^2}$ for NG15 is given. Computing it with the
  NG15 HD matrix and effective per-pulsar $D_i$ is a concrete
  follow-up that would tell us whether the boundary term is
  numerically important for real data.
- The note works in one frequency bin with real $d$. For complex
  Fourier coefficients and multiple bins, the structural statements
  ($F_{PB} = 0$, the $(P,B)$ factorization, the boundary) carry
  over, but coefficient factors of 2 depend on the complex/real
  convention and on whether frequency bins share amplitude
  parameters. Extending to multi-bin with a spectral shape (power
  law or $C_\ell$-weighted) is not done.
- The expansion is local: weak-signal around a CURN fiducial $P_*$.
  The note does not address how sensitive the boundary term is to
  the choice of $P_*$, or what happens when $B$ is not small.
- The pairwise pseudo-likelihood (Sec. 13) uses the simplest
  independent-pair approximation
  $\mathrm{Var}(y_{ij}) \approx (N_i+P)(N_j+P)$. Real optimal-statistic
  treatments include pair-pair correlations and marginalize over
  noise hyperparameters, which changes $F_\times$ in ways the note
  does not quantify.
- Multiple bins with shared amplitude would couple the $P$ boundaries
  across bins; the single-bin analysis here understates the auto-power
  constraint in a multi-bin PTA analysis. Not discussed.

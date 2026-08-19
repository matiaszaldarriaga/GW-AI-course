# Principled Fisher estimate for HD detection and its relation to the Bayesian HD-vs-CURN analysis

**Source:** `references/HD_vs_CURN_Fisher_Bayes_note.md`
**Type:** pedagogical note
**Ingested:** 2026-04-24

## Summary

The note argues that the Bayesian HD-vs-CURN comparison in Agazie et
al. (NANOGrav 15 yr evidence paper) is not "CURN plus an extra HD
component": it is a test of two alternative **spatial covariance
shapes** for the same common-spectrum process, at fixed common
auto-power. The correct Fisher analog must therefore introduce a
shape parameter $\eta$ that interpolates between the two shapes
without changing the common auto-power, profile over the shared
common-spectrum amplitude and noise nuisances, and be evaluated at
the CURN null $\eta=0$. The central analytic result is
$D_{\rm KL}({\rm HD}\,\|\,{\rm CURN}) \simeq \tfrac12 F_{\eta\eta}$
for a unit $\eta$ step from 0 to 1: the Fisher detection forecast is
the local quadratic approximation to the Bayesian model comparison.
A generic floating-amplitude argument (Sec. 7) and an explicit
two-pulsar toy (Sec. 8) both confirm that once the isotropic common
level is floated, the linear-in-$\Delta C$ term cancels and the
distinguishability starts at quadratic order. The practical
consequence is a correction to the current draft: the HD-detection
Fisher should be evaluated at the CURN null with the common auto-power
present in $K_0$, **not** at nonzero HD fiducial (that latter choice
is a post-detection parameter forecast, not a detection forecast).

## Key equations and claims

- **The two hypotheses in covariance form** (Sec. 1):
  $H_0$ (CURN): $C_0 = N + \Phi \otimes I$,
  $H_1$ (HD):   $C_1 = N + \Phi \otimes \Gamma$, with $\Gamma_{aa}=1$.
  The common auto-part is the **same** in both models; only the
  crosses differ.

- **Correct shape interpolation** (Sec. 2):
  $C(\eta) = N + \Phi \otimes [I + \eta(\Gamma - I)]$,
  $\eta=0$ ≡ CURN, $\eta=1$ ≡ HD. Because $(\Gamma-I)_{aa}=0$, the
  common auto-power is $\eta$-independent by construction.

- **Wrong interpolation**:
  $C = N + A_{\rm curn}(\Phi\otimes I) + A_{\rm hd}(\Phi\otimes\Gamma)$
  is **not** the Bayesian analog: raising $A_{\rm hd}$ also raises the
  diagonal unless $A_{\rm curn}$ is reduced by hand.

- **KL to quadratic order** (Sec. 4):
  $D_{\rm KL} = \tfrac14\,\mathrm{Tr}[(C_0^{-1}\Delta C)^2] + O(\Delta C^3)$,
  with $\Delta C = C_1 - C_0 = \Phi\otimes(\Gamma-I)$.

- **Fisher at the null** (Sec. 4):
  $F_{\eta\eta}\big|_{\eta=0} = \tfrac12\,\mathrm{Tr}[C_0^{-1}\Delta C\,C_0^{-1}\Delta C]$,
  and therefore
  $D_{\rm KL}({\rm HD}\,\|\,{\rm CURN}) \simeq \tfrac12 F_{\eta\eta}$
  for the unit step $\eta:0\to1$.

- **Profiled Fisher for detection** (Sec. 5):
  $F^{\rm prof}_{\eta\eta} = F_{\eta\eta} - F_{\eta\lambda}F_{\lambda\lambda}^{-1}F_{\lambda\eta}$,
  $\;D^{\rm prof}_{\rm KL}\simeq\tfrac12 F^{\rm prof}_{\eta\eta}$,
  $\;z_F^2 \equiv F^{\rm prof}_{\eta\eta}$.

- **Orthogonality of amplitude and shape at the null** (Sec. 6):
  $\partial C/\partial A = \Phi_0\otimes I$ is block-diagonal in
  pulsar space; $\partial C/\partial\eta = A\Phi_0\otimes(\Gamma-I)$
  is purely block-off-diagonal. Hence $F_{A\eta}=0$ (idealized null),
  or parametrically tiny in realistic settings. Operational content:
  the common-spectrum amplitude is fixed by the autos, and the
  HD-vs-CURN discrimination lives in the crosses.

- **Generic floating-amplitude cancellation** (Sec. 7):
  for null family $\lambda I$ and signal $I+A$ in whitened units,
  $D^{\rm prof}_{\rm KL} = \tfrac14[\mathrm{tr}(A^2) - (\mathrm{tr}A)^2/n] + O(A^3)$.
  Floating the isotropic level **identically kills the linear term**.
  This is the formal reason not to count the total common auto-power
  as HD evidence.

- **Two-pulsar toy explicit** (Sec. 8):
  with $r \equiv A\Gamma_{12}/\sqrt{(N_1+A)(N_2+A)}$,
  $D_{\rm KL} = -\tfrac12\ln(1-r^2) \simeq r^2/2$,
  $F_{\eta\eta}\big|_{\eta=0} = r^2$,
  so $D_{\rm KL}\simeq\tfrac12 F_{\eta\eta}$ exactly at leading order.

- **What belongs in $K_0$** (Sec. 9):
  $K_0 = K_{\rm white} + K_{\rm timing} + K_{\rm IRN} + K_{\rm common,auto}
   = N + \Phi\otimes I$.
  The null **must** include the common-spectrum auto-part (it is
  present under both hypotheses). It must **not** include the HD
  "cosmic variance" piece obtained by evaluating the Fisher at the
  HD point — that answers a different question.

- **Detection vs parameter forecast** (Secs. 9, 10):
  evaluating Fisher at nonzero HD $C_\ell$ gives a post-detection
  parameter forecast (and the $(C_\ell+N_\ell)^2$ structure carries
  cosmic variance). Evaluating at the CURN null with the
  $\eta$-interpolation gives the detection forecast.

- **Technical remark on amplitude parametrization** (Sec. 13):
  if a parameter enters the covariance quadratically (e.g. strain
  amplitude $A^2$), its derivative vanishes at the null. For a
  null-based Fisher use parameters linear in $C$: the common power,
  a $C_\ell$, or $\eta$.

## Concepts touched

- [[../concepts/KL_divergence]] — central: $D_{\rm KL}\simeq\tfrac12 F_{\eta\eta}$ is a clean demonstration of the local Fisher/KL identity in the shape-interpolation setting. Reinforces the caveat that this relation requires $F$ evaluated at a null where the perturbation is linearized.
- [[../concepts/source_background_degeneracy]] — direct parallel: the block-diagonal ($\partial/\partial A$) vs block-off-diagonal ($\partial/\partial\eta$) decomposition at the CURN null is the same exact-orthogonality mechanism that makes the coherent mean-vs-covariance Fisher block-diagonal.
- [[../concepts/coherent_vs_incoherent]] — the HD cross piece is the covariance channel; the $\eta$ parameter lives entirely in the off-diagonal (cross) sector, i.e. in the incoherent/quadratic channel for a *stochastic* common process.
- [[../concepts/fisher_hierarchy]] — same structural logic: when the perturbation that discriminates is orthogonal to the diagonal (autos), the leading Fisher starts at second order in the perturbation. The HD-vs-CURN setting is the simplest example (shape-only at fixed auto power).
- [[../concepts/matched_filter_vs_power]] — the linear-vs-quadratic story reappears: once the mean/amplitude channel is closed (common autos fix $A$), the remaining HD information is quadratic in the cross-covariance.
- [[../concepts/prior_sensitivity]] — profiling over nuisance $\lambda$ to obtain $F^{\rm prof}_{\eta\eta}$ is the same Schur-complement construction that underlies the prior-sensitivity diagnostic.

## Current paper citations

(None yet — this note was just ingested.)

## Potential paper uses

- **`appendix_fisher.tex`** (and surrounding HD-detection material):
  the current appendix evaluates the HD Fisher around an HD fiducial
  with the $(C_\ell+N_\ell)^2$ cosmic-variance structure. The note's
  central prescription — evaluate at the CURN null with the common
  auto-power in $K_0$, using $\eta$ as the linear-in-$C$ shape
  parameter — should be stated explicitly, and the "detection
  forecast vs parameter forecast" distinction spelled out. The
  relation $D_{\rm KL}\simeq\tfrac12 F_{\eta\eta}$ (unit step) is a
  clean one-line statement that ties the paper's Fisher language to
  the NANOGrav Bayes factor.

- **`three_strategies.tex`**: the note reinforces that the
  "incoherent" strategy's $p^2$ scaling is structurally the same
  phenomenon as HD's $\eta^2$ scaling: cross-covariance information
  only accessible once the diagonal/auto channel is closed. Could be
  cited as the CURN-vs-HD analog in a paragraph connecting the paper's
  hierarchy to the PTA detection literature.

- **`numerical_estimates.tex`**: the practical prescription
  (Sec. 11 of the note) can be mirrored as a short paragraph stating
  which fiducial $K_0$ to use for the NANOGrav-like forecast and why.

- **`discussion.tex`** (or a new methodological subsection):
  the note's bottom line — "the common-spectrum amplitude should not
  go up when one moves from CURN to HD" — is a useful framing line
  for the collaborator-facing version of the paper.

## Relations to other sources

- [[pta_orthogonal_coordinates]] — essentially the same structural
  content, with the shape parameter called $r$ instead of $\eta$
  (same interpolation $C = N + \Phi\otimes[(1-r)I + r\Gamma]$,
  same exact orthogonality $F_{r,A}=0$ at $r=0$, same
  $D_{\rm KL}\simeq\tfrac12 r^2\widetilde F_{rr}$). The present note
  is narrower and more pedagogical: it focuses on the Bayes-vs-Fisher
  bridge and the "don't count autos as HD evidence" consequence,
  while `pta_orthogonal_coordinates` builds the full local chart
  including pivot optimization and robust vs prior-sensitive
  directions. The two are strongly complementary and should be cited
  together in any paper passage that deals with the CURN↔HD transition.
- [[fisher_src_vs_bg_degeneracy]] — the block-diagonal vs
  block-off-diagonal structure ($F_{A\eta}=0$) is the CURN-null
  analog of the coherent source-vs-background exact orthogonality.
- [[pn_coh_vs_quadratic]] — the generic "float the isotropic
  amplitude and the linear term cancels" argument of Sec. 7 is the
  same structural identity used there for the rank-1 covariance
  perturbation.
- [[pta_noise_dominated_limit]] — specifies the concrete $K_0$
  building block (white + timing + IRN) that appears implicitly in
  the note's Sec. 9 recipe.
- Agazie et al. (NANOGrav 15 yr evidence): [[arxiv_2306_16221]] is
  the anisotropy companion; the evidence paper itself is not yet in
  the wiki bibliography.

## Caveats / open questions

- The note is analytic; no numerical $F^{\rm prof}_{\eta\eta}$ is
  computed for NG15 parameters. A concrete plug-in would make the
  "correction to the current draft" operational.
- Sec. 6's exact statement $F_{A\eta}=0$ is given for an
  idealized null; the note admits it is only parametrically small in
  realistic settings. The magnitude of the leakage is not estimated.
- The Bayes-vs-Fisher bridge (Sec. 3) is a Laplace approximation; the
  prior-volume and nuisance-curvature terms that separate the two are
  acknowledged but not evaluated.
- The connection to the $C_\ell$ HD anisotropy Fisher
  (`paper/sections/appendix_fisher.tex`) is made at the level of
  "where to evaluate the matrix." Which $C_\ell$-specific formulas
  change, and by how much, is left to a follow-up calculation.
- The note uses the same structural content as
  `pta_orthogonal_coordinates` (the $r$ parameter). The two notes
  should be cross-referenced and their terminology unified before
  either is cited in the paper.

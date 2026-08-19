# Fisher matrix: source vs background degeneracy (coherent vs incoherent)

**Source:** `references/fisher_source_vs_background_degeneracy.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

This note derives the Fisher matrix for a PTA data model containing one
resolved GW source plus an isotropic Gaussian background, contrasting the
coherent case (source amplitude in the mean) with the incoherent case
(source power marginalized into the covariance).  The central result is that
the source–background Fisher cross-term is **exactly zero** in the coherent
model (block-diagonal structure), while in the incoherent model it is
generically non-zero with magnitude $|r| \sim 1/\sqrt{N_p}$ for a known
source direction.  When the direction is marginalized via the Schur
complement, the correlation rises to $|r| \sim 0.2$–$0.3$ for $N_p = 67$,
but never approaches unity.  The note also explains why the heuristic
argument "$\langle uu^\dagger\rangle \propto \Gamma^{\rm HD}$ implies full
degeneracy" fails: marginalizing over direction in the Fisher matrix is not
the same as averaging the covariance perturbation.

## Key equations and claims

- **Fisher formula** (Sec. 1): for complex Gaussian data with mean $\mu$
  and covariance $C$,
  $$F_{ij} = \mathrm{tr}\!\left(C^{-1}\tfrac{\partial C}{\partial\theta_i}
  C^{-1}\tfrac{\partial C}{\partial\theta_j}\right)
  + 2\,\mathrm{Re}\!\left(\tfrac{\partial\mu^\dagger}{\partial\theta_i}
  C^{-1}\tfrac{\partial\mu}{\partial\theta_j}\right).$$

- **Coherent block-diagonal structure** (Sec. 2–3): the source lives in the
  mean, the background in the covariance, so $F_{\alpha,B^2} = 0$ exactly for
  all source parameters $\alpha \in \{|A|,\psi,\theta_s,\phi_s\}$.  This
  holds for any direction, any $N_p$, any noise level.

- **Coherent SNR** (Sec. 3.1): $F_{|A||A|} = 2\rho^2/|A|^2$ and
  $F_{\psi\psi} = 2\rho^2$ where $\rho^2 = |A|^2 u^\dagger C^{-1}u$.

- **Incoherent source power Fisher entry** (Sec. 5.3):
  $F_{qq} = (u^\dagger C^{-1}u)^2$ (rank-1 trace identity).

- **Incoherent cross-term** (Sec. 5.3):
  $F_{q,B^2} = u^\dagger C^{-1}\Gamma^{\rm HD} C^{-1}u$ — nonzero in general.

- **Noise-dominated correlation estimate** (Sec. 6.2):
  $$|r| \approx \frac{u^\dagger\Gamma u}{|u|^2\sqrt{\mathrm{tr}(\Gamma^2)}}
  \sim \frac{1}{\sqrt{N_p}} \approx 0.12 \quad (N_p = 67).$$
  The numerator is $O(1/2)$ (HD diagonal dominates); the denominator is
  $\sqrt{\mathrm{tr}(\Gamma^2)} \sim \sqrt{N_p/4}$.

- **Direction-marginalized correction** (Sec. 5.5–5.6): the Schur complement
  introduces an $O(1)$ correction $\Delta F = (g_q,g_B)^\top G^{-1}(g_q,g_B)$
  where $G = F_{(\theta\phi)}/q^2$ and $g_q, g_B = F_{(q,B^2),(\theta\phi)}/q$
  are all finite as $q\to 0$.  Numerically, $|r|$ rises to $\sim 0.24$ for
  known direction at $q = 0.01$.

- **Why the $\langle uu^\dagger\rangle \propto \Gamma$ argument fails** (Sec. 7.4):
  Fisher marginalization via the Schur complement is not the same as replacing
  $uu^\dagger$ with its directional average.  The rank-1 structure of
  $uu^\dagger$ is preserved in any single realization and remains
  distinguishable from the full-rank $\Gamma^{\rm HD}$.

- **Summary table** (Sec. 8): coherent known-dir $r=0$ (exact); incoherent
  known-dir $r \sim 1/\sqrt{N_p}$; incoherent unknown-dir $r \sim 0.2$–$0.3$.

## Concepts touched

- [[concepts/source_background_degeneracy]] — the central topic of the note
- [[concepts/coherent_vs_incoherent]] — the two model families compared
- [[concepts/fisher_hierarchy]] — Fisher matrix structure underlying the KL hierarchy
- [[concepts/matched_filter_vs_power]] — coherent (mean) vs incoherent (covariance) detection
- [[concepts/shot_noise]] — rank-1 source perturbation vs full-rank background
- [[concepts/brightest_source_fraction]] — the single-source limit motivates the
  one-source model throughout

## Current paper citations

- `paper/sections/three_strategies.tex:195` — Numerical values $|r| \sim 1/\sqrt{N_p}\approx 0.12$ (known direction) and $|r| \sim 0.2$–$0.3$ (direction marginalized) for $N_p = 67$.
- `paper/sections/appendix_fisher.tex:67` — Basis for the appendix's numerical verification: the analytical $|r| \sim 1/\sqrt{N_p} \approx 0.12$ is compared to the computed $|r| = 0.037$ for known direction (differ by $\sim 3\times$, order-of-magnitude consistent); direction-marginalized value rises to $|r| \sim 0.24$.

## Potential additional uses

- **Introduction / motivation**: the exact block-diagonal coherent Fisher is
  a crisp argument that coherent source fitting carries zero cost from
  background uncertainty — one sentence in intro.tex.
- **Strategy comparison section**: $|r| \sim 1/\sqrt{N_p}$ gives a concrete
  scale for incoherent degradation from source–background confusion,
  complementing the $p^2$ vs $p$ KL argument.
- **NANOGrav comparison**: the weak-degeneracy result supports the claim that
  incoherent methods are sub-optimal but not fatally compromised by confusion.

## Relations to other sources

- Complements the point-source vs $C_\ell$ note
  (`references/pta_point_source_vs_CL_note.md`, Secs. 3–5), which
  establishes the $p$ vs $p^2$ vs $p^4$ KL hierarchy; this note fills in the
  Fisher cross-term structure that underlies that hierarchy.
- The noise-dominated $\mathrm{tr}[(\Gamma^{\rm HD})^2]$ appearing in the
  denominator is the same quantity as $F_{B^2 B^2}$ at $B^2=0$, used in
  $\Sigma_{\rm bg}^2$ (see `wiki/conventions.md` and the background
  significance formula).

## Caveats / open questions

- The note works at a single Fourier frequency bin; multi-frequency
  generalization (additive Fisher over independent bins) is assumed but not
  derived.
- The numerical $|r| = 0.037$ (known direction, $N_p = 67$) is $\sim 3\times$
  below the $1/\sqrt{67}\approx 0.12$ analytical estimate.  The gap is
  attributed to partial cancellation of HD off-diagonal elements in
  $u^\dagger\Gamma u$, but no precise derivation is given; the appendix flags
  it as order-of-magnitude consistent.
- The direction-marginalized $|r| \sim 0.24$ is quoted at $q = 0.01$; its
  $q$-dependence is not characterized, so the value may not be representative
  of the weak-signal regime.
- The note does not treat the case of multiple incoherent sources; the
  single-source Fisher is the relevant limit only when one source dominates
  ($p \approx 1$).  For smaller $p$ the multi-source generalization would be
  needed to connect cleanly to the [[concepts/brightest_source_fraction]] framework.

# Matched Filtering vs. Total Power: Look-Elsewhere Effect and Trials Factor

**Source:** `references/matched_filter_vs_total_power.md`
**Type:** pedagogical note
**Ingested:** 2026-04-13

## Summary

General-audience derivation of when a matched filter search outperforms a total-power
(quadratic) statistic. Two toy models are developed: (1) a discrete set of $K$ templates
each illuminating $M$ of $N$ data bins, and (2) a continuous-parameter (ring/sphere)
model where the effective trials count is set by angular resolution, not by the analyst.
The central result is that the matched filter's SNR scales as $A$ (linear, coherent sum)
while the total-power SNR scales as $A^2$ (quadratic, incoherent). For weak signals
$A \ll 1$, the linear statistic wins; the trials-factor penalty enters only
logarithmically and cannot overcome this advantage unless the template space is
exponentially large ($K \sim e^{\sqrt{N}}$). For continuous parameters the effective
trial count $K_{\rm eff} \sim 2\pi/\theta_c$ is determined by the measurement's angular
resolution, not freely tunable. The note closes with references to Rice (1944), Adler
(1981), Gross and Vitells (2010), and Owen (1996).

## Key equations and claims

- **Single-template SNR** (Sec. 2.2): $\mathrm{SNR}_{\rm matched} = A\sqrt{M}$.
- **Minimum detectable amplitude, matched filter** (Sec. 2.3):
  $A_{\min}^{(\rm matched)} = (\sqrt{2\ln K} + q)/\sqrt{M}$.
  Trials factor $\sqrt{2\ln K}$ is additive and grows only logarithmically with $K$.
- **Total-power SNR** (Sec. 2.4): $\mathrm{SNR}_{\rm power} = MA^2/\sqrt{2N}$.
- **Minimum detectable amplitude, total power** (Sec. 2.4):
  $A_{\min}^{(\rm power)} = (q\sqrt{2N}/M)^{1/2}$.
- **Matched filter wins when** (Sec. 2.5): $\ln K \lesssim \sqrt{N}$; since $K$
  is typically polynomial in $N$, this is almost always satisfied.
- **Autocorrelation curvature** (Sec. 3.4):
  $\Lambda = \sum_i [f'(\phi_i)]^2 / \sum_i [f(\phi_i)]^2$;
  correlation length $\theta_c \sim 1/\sqrt{\Lambda}$.
- **Rice upcrossing formula** (Sec. 3.5):
  $\langle N_{\rm up}(u)\rangle = \sqrt{\Lambda}\,e^{-u^2/2}$ on a full circle;
  effective trial count $K_{\rm eff} = \sqrt{\Lambda} \approx 2\pi/\theta_c$.
- **Sphere generalization** (Sec. 3.6): template metric
  $g_{\mu\nu} = -\partial^2\rho/\partial\theta^\mu\partial\theta^\nu|_0$;
  $K_{\rm eff}^{\rm sphere} \sim \sqrt{\det g} \sim 4\pi/\theta_c^2$.
- **Scaling table** (Sec. 3.7): as template width $\alpha$ shrinks, SNR falls as
  $\sqrt{\alpha}$ while trials penalty rises only as $\sqrt{\ln(1/\alpha)}$; narrowing
  the template always hurts detection.

## Concepts touched

- `matched_filter_vs_power` — the central topic of this note
- `coherent_vs_incoherent` — coherent (linear) vs. incoherent (quadratic) statistics;
  directly maps to coh vs. $C_\ell$ strategies in the PTA hierarchy
- `fisher_hierarchy` — $A$-scaling of SNR (linear = coh, quadratic = $C_\ell$-power)
  mirrors the $p$-scaling in the KL hierarchy (coh $\propto p$, $C_\ell \propto p^4$)
- `N_eff` — effective number of resolution elements plays the same role as $K_{\rm eff}$
- `shot_noise` — the $M$-bin signal model is a discrete-source analog of the
  shot-noise regime

## Current paper citations

(None yet.)

## Potential additional uses

- **Introduction / motivation**: The $A$ vs. $A^2$ SNR argument (Sec. 2.5) is a
  model-independent justification for why coherent source fitting dominates $C_\ell$
  compression. Could support the first paragraph of the introduction or a methods
  motivation section.
- **Fisher hierarchy section**: The note's Sec. 4 summary table maps cleanly onto the
  coh / inc / $C_\ell$ hierarchy: linear statistic = coh, quadratic = $C_\ell$. Citing
  this note would give the hierarchy a non-PTA-specific pedagogical grounding.
- **Discussion of trials factor**: Sec. 3.5–3.6 (Rice formula, $K_{\rm eff}$) could
  support a remark that the look-elsewhere penalty for a sky search is $O(\ln K_{\rm
  eff})$, which is never large enough to reverse the hierarchy.
- **Owen (1996) template metric**: If the paper ever discusses the angular resolution of
  a matched-filter SMBHB sky search, Sec. 3.6 and the Owen reference would be relevant.

## Relations to other sources

- Conceptually upstream of any PTA-specific derivation that compares coherent and
  incoherent strategies; no other source in `references/` has been ingested yet that
  covers this general framework.
- Rice (1944) and Adler (1981) are the mathematical foundations for the continuous
  look-elsewhere calculation. Gross and Vitells (2010) is the physicist-friendly
  exposition (LHC Higgs context). Owen (1996) introduces the template metric for GW
  inspiraling-binary searches; it is PTA-adjacent but not PTA-specific.
- None of the four cited works (Rice, Adler, Gross and Vitells, Owen) are currently in
  `paper/references.bib`. Use `verify-reference` before adding any of them.

## Caveats / open questions

- The note has not been "fixed for rendering" per user memory. Equations use `\mathcal`,
  `\langle`, `\rangle`, `\hat\Omega`, and `\Delta\phi` — those render correctly in most
  Markdown processors. No instances of `\Vert`, `\|`, `\widehat`, `\boldsymbol`, or
  `\middle` were found, so MacDown-specific breakage is not expected. Verify by opening
  the file in MacDown before any presentation use.
- The discrete toy model assumes the $K$ template subsets $S_k$ are disjoint; if
  templates overlap, the maximum-statistic distribution is more complex. The note does
  not address this case.
- The note does not derive the PTA-specific $p$-scaling ($p$, $p^2$, $p^4$). That
  translation is left to the reader (or to a concept page).
- Owen (1996) cites Phys. Rev. D 53; the exact page range is not given in the note.
  Confirm before adding to `references.bib`.

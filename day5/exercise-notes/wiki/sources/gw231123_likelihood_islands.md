# GW231123-style likelihood islands (toy model)

> **OFF-TOPIC — not part of the PTA anisotropy project.** This note is about
> **ground-based** GW parameter-estimation likelihood *geometry* for a heavy,
> high-SNR, merger-dominated compact-binary event (GW231123-style). It has
> **nothing** to do with PTA anisotropy, SMBHBs, the source-power sky, or
> $C_\ell$. It is **not cited by the paper** and there is no path to citing it.
> It lives in `references/` only because it is parked here for separate work.
> Ingested as a stub for wiki completeness; do **not** wire it into the
> $p$-hierarchy concept pages.

**Source:** `references/gw231123_toy_model_note.md`
**Type:** ChatGPT pedagogical note (likelihood-geometry toy model, not a waveform model).
**Ingested:** 2026-06-13

## Summary

A likelihood-geometry toy model for why a heavy, high-SNR, merger-dominated
ground-based GW event can show **narrow, isolated posterior islands**, and why
**edge-on** templates can be especially narrow. The mechanism: few cycles in
band weaken the smooth dominant-mode ($22$) chirp constraint so multiple
phase-wrapped aliases survive, while high total SNR makes even weak higher modes
or precession sidebands measurable ($\rho_j^2 = \rho^2 w_j$), so those weak
features phase-lock the solution into sharp islands. The note also derives an
inclination-curvature formula showing edge-on systems are well-measured only
when several angular patterns contribute.

## Key equations (note section anchors)

- (§2 / §19) Residual-phase likelihood penalty: $V \simeq 2\pi^2\rho^2\,\mathcal N_{\rm eff}^2$, with $\mathcal N_{\rm eff}^2 = \langle (\delta\Phi_\perp/2\pi)^2\rangle$. Criterion $\rho\,\mathcal N_{\rm eff} \gtrsim 1/(2\pi)$.
- (§7 / §19) One weak feature: $V_j \simeq \rho_j^2\,[1-\cos\Delta\varphi_j]$ — importance set by the feature's own SNR $\rho_j$, not its fractional amplitude.
- (§8 / §19) Island spacing $\Delta\lambda_{\rm island} \sim 1/\lvert D_j\rvert$ and width $\sigma_\lambda \sim 1/(2\pi\rho_j\lvert D_j\rvert)$, so $\Delta\lambda_{\rm island}/\sigma_\lambda \sim 2\pi\rho_j$. Here $D_j = (1/2\pi)\,\partial_\lambda(\phi_j-\phi_{22})$.
- (§9) Finite-band survival: $N_{\rm islands} \sim \lvert D_j\rvert / B_j$, where $B_j$ is the bandwidth-decoherence coefficient.
- (§4 / §19) Multimode inclination curvature (after marginalizing distance): $\Gamma_{uu}/\rho^2 = {\rm Var}_w[\partial_u\ln Y_m]$, $u=\cos\iota$; weights $w_m \propto R_m Y_m^2(u)$. Vanishes if only one angular mode contributes.
- (§12 / §19) Precession sideband SNR $\rho_{\rm prec} \sim \rho\,\epsilon\,G/\sqrt 2$; matters when $\rho\,\epsilon\,G \gtrsim O(1)$.

## Concepts touched

None of this project's concept pages. (Deliberately empty — these are
ground-based PE concepts, not PTA anisotropy concepts.)

## Paper uses

- **Cited:** none.
- **Could be cited:** none. Off-topic for this paper.

## Related wiki pages

- None. Cross-linking into the PTA wiki would be misleading; this stub is
  intentionally isolated.

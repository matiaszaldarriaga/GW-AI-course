# $N_{\rm eff}$

Effective number of sources, the inverse participation ratio of the
normalized source weights.

## Definition

$$N_{\rm eff} \equiv \frac{1}{\sum_a p_a^2} = \frac{(\sum_a q_a)^2}{\sum_a q_a^2}.$$

In the schema-v2 products this is stored as $Q^2/S_2$, with
$Q=\sum_s w_s$ and the **full** $S_2=\sum_s w_s^2$. For an aggregated
population bin the contribution is
$nE[w^2]=n(E[w]^2+\mathrm{Var}[w])$, not $nE[w]^2$. A finite bright-source
ledger is never the all-source denominator; its explicit remainder must be
included.

Limits:
- $N$ identical sources → $N_{\rm eff} = N$.
- One source dominates → $N_{\rm eff}\to 1$.
- Heavy-tailed weight distribution → $N_{\rm eff}$ controlled by the few brightest sources.

## Role in anisotropy

$N_{\rm eff}$ is the natural scale for the conditional mean of the
[[Cl_over_C0]] ratio:

$$\mathbb E[C_\ell/C_0\,|\,\{p_a\}] = 1/N_{\rm eff}, \qquad \ell\ge 1.$$

Read the other way, the corrected simulations show an empirical trend
$E[N_{\rm eff}\mid C_1/C_0]\approx 1/(C_1/C_0)$, so a large dipole means a **handful**
of sources ($\approx2$ at $C_1/C_0=0.5$, $\approx5$ at the NANOGrav "limit"
$0.2$), capped at high frequency where few sources exist. The full conditional
$P(N_{\rm eff}\mid C_1/C_0)$ — and its analytic ($\eta$-marginalized) form — is
computed in [[../notebooks/guide_power_anisotropy]] §10f (F2); see also
[[dipole_distribution]] for the companion $P(p_1\mid C_1/C_0)$.

For the fractional-fluctuation power spectrum of the pulsar-map,
this becomes the Lin et al. shot-noise floor
$\mathbb E[C_\ell^{(\delta M)}] = 4\pi/N_{\rm eff}$ (see [[shot_noise]]).

## Two distinct quantities — do not conflate (fixed 2026-06-22)

There are two related but different objects:

- **True** $N_{\rm eff} = 1/\sum_a p_a^2$, a property of all source weights.
  In this project it is computed per realization from schema-v2 $Q^2/S_2$,
  including the full unresolved second-moment remainder. Equivalently
  $N_{\rm eff}=1/(p_1^2+\eta)$ only when $\eta$ includes every other source,
  not merely the stored ledger.
  This is what Table I (`tab:conditional`), Fig. 6/7
  ([[../figures/p1_neff_conditional]]) and Fig. 3
  ([[../figures/c1c0_neff_vs_freq]]) plot.
- **Dipole estimator** $1/(C_1/C_0)$, the per-realization inverse dipole. It is
  an *estimator* of $N_{\rm eff}$ (unbiased only in the direction-mean, by
  `eq:mean_cl`) with a heavy tail — its realization **mean** diverges upward.

The dipole estimator has a heavy upward tail and is not interchangeable with
the full moment. The earlier `c1c0_neff_vs_freq` generator first plotted
$C_0/C_1$, then used a finite ledger; the 2026-08-11 remediation replaces both
with the explicit all-source $Q^2/S_2$ contract throughout Secs. III–IV.

## Numerical regimes in this project (matched normalization)

With all models calibrated to $\sqrt{\langle h_c^2\rangle(1\,{\rm yr}^{-1})} =
2.5\times10^{-15}$ (see [[SMBH_population_model]], [[reproducibility]]), the
median full-moment $N_{\rm eff}$ for $\varepsilon=0.66$ runs from $18.94$ at the
lowest frequency to $5.27$ at $f = 1.03\,{\rm yr}^{-1}$ — the
"rare-bright-source" regime. The low-scatter $\varepsilon=0.20$ model, which now
needs $\sim 13\times$ more sources to reach the same amplitude, has orders of
magnitude more ($N_{\rm eff}=1167.04$ at the lowest frequency and $19.40$ at
$1.03\,{\rm yr}^{-1}$). Conditioned on a large dipole, however, $N_{\rm eff}$
is approximately model-independent over the tested family: in the plotted
$0.05\le x<0.9$ bins, $xE[N_{\rm eff}\mid x]=0.85$--$1.28$ (see
[[brightest_source_fraction]], [[../figures/source_content_estimators]]). See
`fig:c1c0_freq`.

## Definitional convergence with Lin, Lidz & Ma (2026-08-11)

Their first paper ([[../sources/arxiv_2602_16808]]) used the ensemble ratio
$\langle h^2\rangle^2/\langle h^4\rangle$; their second
([[../sources/arxiv_2608_09929]]) uses the realized $1/\sum_a p_a^2$ — the
definition above — and derives the same $1/N \le \sum_a p_a^2 \le 1$ bounds.
Their $\hat C_{\rm shot}/(4\pi)$ and our $1/N_{\rm eff}$ are now the same
number, which makes their Fig. 2 (bottom panel) and our `fig:c1c0_freq`
(right panel) directly comparable; the like-for-like table is in
[[../sources/arxiv_2608_09929]].

Note the remaining gap: $\sum_a p_a^2$ is $\mathbb E[C_\ell/C_0\mid\{p_a\}]$,
so a realized single-multipole $C_1/C_0$ still scatters about it — see
[[dipole_distribution]]. Their pipeline never places a source on the sky, so
their PDF is the PDF of the ledger, not of the map.

## Source pages

- [[../sources/pn_C1_over_C0]] — Secs. 7.2 and 19, connecting to shot-noise.
- [[../sources/arxiv_2608_09929]] — Lin, Lidz & Ma 2026b adopt this exact definition and derive its bounds.
- [[../sources/pta_1src_vs_CL]] — uses $\sum p_a^2$ implicitly via $C_L^P/C_0^P$.
- [[../sources/pn_coh_vs_quadratic]] — many-source aggregation $\langle D_{\rm cov}\rangle \propto \sum_s p_s^2$.
- [[../sources/matched_filter_vs_power]] — $K_{\rm eff}$ trials analogy (separate quantity, conceptually related).

## Paper uses

- `angular_power_spectrum.tex:49` (`eq:neff`) — definition.
- `angular_power_spectrum.tex:58` (`eq:mean_cl`) — conditional mean.
- `astrophysical_model.tex:100` (`fig:c1c0_freq`) — vs frequency plot.
- `discussion.tex` — relation to heavy-tailed SMBH population.

## Code and notebooks

- [[../code/gwb_sources_sources]] computes per-realization $p_a$ → $N_{\rm eff}$.
- [[../notebooks/guide_model_comparison]] — per-$\varepsilon$ median $N_{\rm eff}$ (note: the historical 966/191/27 triple was at the old fiducial $\phi_\sigma$; under the matched normalization the low-$\varepsilon$ values rise sharply — see "Numerical regimes" above).
- [[../notebooks/guide_power_anisotropy]] — §10d: $N_{\rm eff}$ scatter plots and correlation with $C_\ell/C_0$; §10f (F2): the conditional $P(N_{\rm eff}\mid C_1/C_0)$, peaking at $1/(C_1/C_0)$.
- [[../figures/c1c0_neff_vs_freq]] — $N_{\rm eff}$ vs frequency for three models (ledger definition).
- [[../figures/source_content_estimators]] — $\langle N_{\rm eff}\mid x\rangle\simeq 1/x$ and the model-collapse (universality) test.

## Related concepts

[[Cl_over_C0]], [[brightest_source_fraction]], [[shot_noise]],
[[SMBH_population_model]].

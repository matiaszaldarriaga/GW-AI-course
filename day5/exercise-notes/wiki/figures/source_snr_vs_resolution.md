# Figure: source SNR retained vs. angular resolution

**File:** `paper_v2/figures/source_snr_vs_resolution.pdf` (Sec. V,
`fig:source_snr_res`).
**Generator:** `paper_v2/scripts/fig_source_snr_vs_resolution.py` (computed on the
fly; no `results/*.npz` needed). **New 2026-06-23.**

## Caption (expanded)

The source-detection SNR coefficient $\alpha_L=\rho_L/(p_1\rho_0)$ as a function
of the angular resolution $L$ (maximum multipole of the source template), in the
idealized equal-noise array. A matched filter for the source's full
cross-correlation pattern reaches $\alpha_{\rm ps}=\sqrt5\simeq2.24$ (dashed
asymptote); truncating at multipole $L$ keeps only $\alpha_L<\alpha_{\rm ps}$
(points: mean $\pm$ scatter over 8 random arrays of $N=120$ pulsars). A
dipole-only search ($L=1$) retains $\alpha_1\simeq0.65$, under a third of the
amplitude, because a point source has substantial quadrupole and higher-multipole
covariance structure. Through quadrupole, $\alpha_{\le2}\simeq1.4$.

> **Annotation removed (2026-08-12, decision GS-12).** The panel used to carry
> an `ax.annotate` label "dipole only: 29% of the amplitude" with an arrow to
> the $L=1$ point. In the rendered figure the label sat far from the arrow
> head, so the arrow read as a stray mark, and the caption never accounted for
> it — which is exactly what GS-P asked about. The 29% appears in both the
> figure caption and the running text, so nothing was lost by deleting the
> `annotate` call. The script still prints
> $\alpha_1/\sqrt5 = 0.289$ to stdout.

## Concepts illustrated

- [[../concepts/matched_filter_vs_power]] — keeping the full source pattern
  recovers all the SNR; truncation loses.
- [[../sources/pta_point_source_multipole]] — $\alpha_{\rm ps}=\sqrt5$,
  $\alpha_L$.

## Inputs / reproduce

- Inputs: none (uses `gwb_sources.source_detection.pair_alpha_coefficients`).
- `conda run -n gw_pta python paper_v2/scripts/fig_source_snr_vs_resolution.py`

## Used in

- `paper_v2/sections/source_detection.tex`, Sec. V (`fig:source_snr_res`).

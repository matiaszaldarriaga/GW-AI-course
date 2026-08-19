# Square-root spherical harmonic basis

Positivity-preserving parameterization of the GW power sky used by the
NANOGrav 15yr anisotropy analysis. Originated in two independent PTA
papers (2020 and 2021); this wiki's canonical citation is the Banagiri
et al. 2021 paper because it is what NANOGrav credits.

## Construction

$$P(\hat\Omega) = \!\left[\sum_{L=0}^{L_{\max}^b}\sum_{M=-L}^{L}
b_{LM} Y_{LM}(\hat\Omega)\right]^{\!2}.$$

Squaring ensures $P\ge 0$ pointwise.

## Truncation rule (exact)

If the measured angular spectrum runs up to $\ell_{\max}^a$, then
$$\boxed{\ell_{\max}^b = \ell_{\max}^a / 2}.$$

**Derivation:** the squaring operation couples modes via Clebsch-Gordan,
$$a_{\ell m} = \sum_{LM,L'M'} b_{LM} b_{L'M'}\,\beta^{LM,L'M'}_{\ell m},$$
and the CG selection rule $L_{\max}=\ell+\ell'$ means a field with modes
up to $L$ produces power up to $\ell = 2L$. Requires $\ell_{\max}^a$ even.

This relation is explicit in Banagiri et al. 2021 Sec. 3. The earlier
paper by Taylor, van Haasteren, Sesana (arxiv 2006.04810, 2020) derives
it in their Appendix A in PTA-specific context.

## Degeneracy breaking

- $b_{00} = 1$ (fixed). Breaks both the overall-scale invariance and
  the parity symmetry $\{b_{LM}\}\to\{-b_{LM}\}$.

## Priors used by NANOGrav (arxiv 2306.16221)

- $|b_{LM}|\sim U[0,50]$, uniform phase for $M\ne 0$.
- $b_{L0}\sim U[-50,50]$.
- $\ell_{\max}^a = 6 \Rightarrow \ell_{\max}^b = 3$.

Banagiri et al.'s own validation used $|b_{LM}|\in[0,3]$, a much
narrower range. The ratio $C_\ell/C_0$ is scale-invariant, so this
difference does not affect the prior on the ratio — but the amplitude
range does affect the prior on the absolute spectrum $C_\ell$.

## "The constraint is the prior" — supported by NANOGrav itself

Two pieces of evidence from the NANOGrav 15yr anisotropy paper directly:

1. **Fig. 1 caption (verbatim from the paper):** the shape of the 95%
   upper limits "reflects the constraint from the prior condition that
   the power be positive on the sky as imposed by the square-root
   spherical harmonic basis." This is the NANOGrav collaboration
   acknowledging that the upper-limit shape is prior-driven.

2. **Hellinger distance $\approx 0$ at all frequencies and multipoles
   $\ell=1$–6** (Fig. 5 of the paper). The posterior and prior
   distributions are statistically indistinguishable. This means the
   data carry no information about anisotropy.

Both are discussed in [[../sources/arxiv_2306_16221]] and form the backbone
of the project's argument in `nanograv_prior.tex`.

## Convergence with $\ell_{\max}^b$

As $\ell_{\max}^b$ increases, squaring pumps power from all modes into
$C_0$, shrinking $C_\ell/C_0$. The 95th percentile drops by $\sim$2
orders of magnitude from $\ell_{\max}^b=3$ to $\ell_{\max}^b=95$. The
"constraint" depends critically on this implementation choice — and
the choice is not adaptive to the data.

## Source pages

- [[../sources/arxiv_2103_00826]] (Banagiri et al. 2021) — canonical citation; MCMC implementation, CG truncation proof, validation.
- [[../sources/arxiv_2006_04810]] (Taylor, van Haasteren, Sesana 2020) — earlier PTA-specific derivation. **Not yet in bibliography**; flagged as a candidate to add via `verify-reference`.
- [[../sources/arxiv_2306_16221]] (NANOGrav anisotropy 15yr) — operational consumer of the basis.
- [[../sources/pta_1src_vs_cls_toy]] — minor mention.
- [[../sources/pta_source_detection_likelihood]] — flags that the linear Gaussian-$g$ map likelihood can place weight on non-positive source-power maps; a sqrt-SH or positive-pixel basis is needed to impose positivity globally (Secs 6, 9, 12). The small-signal $p^4$ result is unaffected by this local modeling choice.

## Notebooks, code, results

- [[../notebooks/guide_sqrtSH_model]] — numerical validation; reproduces NANOGrav Fig. 1 and quantifies non-convergence with $\ell_{\max}^b$.
- [[../code/scripts_run_sqrtSH]] — batch runner for the prior realizations.
- [[../results/sqrtSH_realizations_lmax3]] (NANOGrav-faithful), [[../results/sqrtSH_realizations_nside32]] (large-$\ell_{\max}^b$): 330× spread in 97.5th-percentile $C_1/C_0$.
- [[../figures/exceedance_probability]] — the "constraint is uninformative" figure.

## Paper uses

- `nanograv_prior.tex` — the entire section.

## Related concepts

[[Cl_over_C0]], [[prior_sensitivity]], [[transfer_function]].

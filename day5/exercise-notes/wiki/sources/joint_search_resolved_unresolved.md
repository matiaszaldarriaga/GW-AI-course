# Joint search for resolved + unresolved SMBHBs (companion draft, 2026)

**Source:** `references/joint_search_smbhb/main.tex` (full manuscript; figures
and compiled PDF not copied — see the directory `README.md`). Now also public as
**arXiv:2606.18241** (v1 2026-06-16, v2 2026-06-23).
**Title (published):** *A Joint Optimal Search for Gravitational Waves from
Resolved and Unresolved Supermassive Binary Black Holes with Pulsar Timing
Arrays* (the draft title ended "...with the NANOGrav 15-yr data").
**Authors:** Boris Goncharov, Gabriela Sato-Polito, Xiaoming Bi, Matias
Zaldarriaga. MZ is a co-author.
**Type:** companion observational paper (now on arXiv).
**Bib key:** `Goncharov:2026joint` — **now IN `paper/references.bib`** as an
`@misc` arXiv entry (added 2026-06-24; arXiv metadata verified directly, ADS not
yet indexing this brand-new submission, primary class astro-ph.HE). Cited by
`source_detection.tex`, `nanograv_prior.tex`, `source_vs_cl_reduced.tex`.
**Published-vs-draft numbers (IMPORTANT):** the arXiv abstract headlines a
**2%** (15-yr) / **5%** (20-yr) SNR-5 CW detection probability and **21 of 114**
AGN candidates in tension. These **supersede** the draft-era values recorded in
the body below (0.6%/2% and 24/114). The paper uses the published values; a full
re-ingest of the arXiv version via `ingest-reference` is recommended to refresh
the detailed tables below.
**Ingested:** 2026-06-13; arXiv update 2026-06-24.

## Summary

The observational companion to the distribution paper [[arxiv_2406_17010]]
(Sato-Polito & Zaldarriaga 2025). It builds a single hierarchical PTA
likelihood in which the unresolved GWB and the brightest individually-resolvable
SMBHB (a continuous wave, CW) are two components of the *same* astrophysical
population, controlled by just two hyperparameters $(N_{\rm c}, h_{\rm c})$ at
$f_{\rm ref}={\rm yr}^{-1}$. It proposes the characteristic number of sources
$N_{\rm c}$ as the detection statistic for the SMBHB (Poisson, non-Gaussian)
origin of the GWB, with $N_{\rm c}\geq 1000$ as the Gaussian-limit null.
Applied to NANOGrav 15-yr data, it finds $N_{\rm c}$ consistent with $1000$
(no evidence for the Poisson regime) and no resolvable CW (broad $f_{\rm cw}$
posterior; posterior $\approx$ posterior-predictive for $h_{\rm cw}$;
$\mathrm{SNR}<4 \Rightarrow$ non-detection). The astrophysically-informed prior
nonetheless yields *stronger* CW strain limits than the agnostic NANOGrav
search, placing 24 of 114 AGN-selected SMBHB candidates in tension (vs 1 in the
original analysis). Forecasts: even at 20 yr the all-sky all-frequency CW
detection probability stays low (a few percent at SNR 5).

## Dataset caveat (IPTA reproducibility rule)

The public arXiv version (2606.18241) presents the joint search on an
**earlier, partly simulated version of the NANOGrav 15-yr dataset** — the
abstract states it applies the method to "the simulated NANOGrav 15-year data,
which replicates all aspects of real data's known noise, observations, and the
inferred GWB power spectrum." Per co-author M. Zaldarriaga (2026-06-24): an IPTA
data-access rule prevents showing the *final real* 15-yr data in this companion
analysis; the authors did run the search on the real data and the result is
**essentially identical**, but they are not permitted to display it. The
$N_{\rm c}\!\approx\!1000$ / no-resolvable-CW conclusion and the SNR-5
detection-probability forecast therefore stand on the public (simulated)
dataset, with the real-data outcome verified to agree. This is the caveat
reflected in `source_detection.tex` ("their public analysis uses the earlier,
partly simulated version of the 15-year dataset ... the search on the final
15-year data gives an essentially identical result").

## Why it matters to this project

This is the **empirical realization of the brightest-source (coherent CW)
channel** — the most powerful rung in the project's $p/p^2/p^4$ KL hierarchy
([[../concepts/fisher_hierarchy]]). Goncharov et al. run a direct, optimal joint
CW+GWB search on the real NANOGrav 15-yr data and find no resolvable source plus
a low near-term detection probability. If the *most* sensitive channel cannot
detect the brightest source, the far weaker $C_\ell$ compression
($D_{C_\ell}\propto p^4$) cannot do better — this is the strongest available
argument that $C_\ell$-based anisotropy searches are pointless for constraining
the astrophysical SMBHB model. The companion `README.md` flags it as the
empirical backbone for the rewrite of this project's Sections 6-7.

## Key equations

(Equation/section anchors refer to `main.tex`.)

- **Total-strain PDF** (Sec. *The Astrophysical Model*, Eq. `eq:p_h_tot`;
  expands Eq. 18 of Ref. [[arxiv_2406_17010]]):
  $$p(h_{\rm t}^2) = \int \exp\left\{ i\omega h_{\rm t}^2\left(\mathcal{F}\!\left[\tfrac{dN}{dh_{\rm s}^2}\right] - \bar N\right)\right\} d\omega .$$
  Characteristic strain *amplitude* $h_{\rm c}$ is defined as the **median** of
  $p(h_{\rm t}^2)$; it follows $h_{\rm c}(f)=A(f\,{\rm yr})^{-2/3}$ for
  GW-driven circular inspirals.

- **Quasi-invariant luminosity function** (Eq. `eq:mu_x`):
  $$\mu(x) = \frac{1}{N_{\rm c}}\frac{dN}{d\log x},\qquad
    x \equiv \frac{h_{\rm s}^2}{h_{\rm s,peak}^2},\qquad
    N_{\rm c}\equiv \frac{h_{\rm c}^2}{h_{\rm s,peak}^2}.$$
  $\mu(x)$ is (quasi-)invariant to SMBHB population properties, so $p(h_{\rm t}^2)$
  is a function of only $(N_{\rm c}, h_{\rm c})$. Scalings:
  $h_{\rm s,peak}^2\propto f^{7/3}$, $N_{\rm c}(f)\propto f^{-11/3}$.

- **Brightest-source (CW) PDF** (Eq. `eq:p_h_cw`; derived in App.
  `app:p_hmax`). $h_{\rm cw}=\max_s h_{\rm s}$:
  $$p(h_{\rm cw}) = h_{\rm s,peak}^2\,\frac{dN}{dh_{\rm s}^2}\,
    \exp\!\left(-\int_{h_{\rm s}^2/h_{\rm s,peak}^2}^{\infty}\frac{dN}{dx}\,dx\right).$$
  Derivation: $F_{\max}(x|N_s)=[F_1(x)]^{N_s}$, Poisson-averaged to
  $F_{\max}(x)=e^{-\bar N(1-F_1(x))}$, differentiated gives
  $P_{\max}(x)=\tfrac{dN}{dx}\exp\{-\int_x^\infty \tfrac{dN}{dx'}dx'\}$
  (App. Eq.). The remaining sources $h_{\rm t-1}$ use the same inverse-Fourier
  construction as $p(h_{\rm t}^2)$ but truncated at $x_{\rm cw}=h_{\rm cw}^2/h_{\rm s,peak}^2$.

- **Hierarchical prior replacing standard agnostic priors** (Sec.
  *Methodology*): the only change to the standard van-Haasteren PTA likelihood
  Eq. `eq:likelihood` ($\mathbf C = \mathbf N + \mathbf{TBT}^\intercal$) is to
  swap independent priors $\pi(h_{{\rm t},i}),\pi(h_{{\rm cw},i})$ for
  $\pi(\{h_{{\rm t},i}|h_{{\rm t-1},i}\},h_{{\rm cw},i}\mid N_{\rm c},h_{\rm c})$
  (Table `tab:joint_gwb_cw_model`). This is a **global fit** to all signal+noise
  parameters — an improvement over the factorized per-bin refit (their Eq. for
  $\mathcal{L}(\mathbf t_{\rm a}|\Lambda)=\prod_i\int \mathcal P/\pi\cdot\pi\,dh$,
  i.e. Eq. 38 of Ref. [[arxiv_2406_17010]]) which is not guaranteed correct
  because $\mathbf C$ entangles frequency bins.

- **CW strain amplitude vs characteristic strain** (Eq. `eq:cw_h0_hcw`,
  App. `app:strain_units`):
  $$h_0 = 2\frac{(G\mathcal M)^{5/3}}{D_{\rm L}c^4}(\pi f)^{2/3}
        = 2 h_{\rm cw}\sqrt{\tfrac{5}{32}\tfrac{\Delta f}{f}},
    \qquad h_{\rm rms}=\tfrac12\sqrt{\tfrac{32}{5}}\,h_0 .$$

- **CW SNR** (Eq. `eq:snr`): $\mathrm{SNR} = \tfrac{h_0}{\sqrt{S_{\rm eff}(f)}}\sqrt{T_{\rm obs}}$,
  with $S_{\rm eff}$ from Hazboun-Romano. $\mathrm{SNR}<4$ is taken as
  "unlikely detected", consistent with the reported non-detection.

## Detection-statistic logic ($N_{\rm c}$ as the smoking gun)

- As $N_{\rm c}$ increases, $p(h_{\rm t}^2)$ thins toward the Gaussian
  power-law GWB; as $N_{\rm c}\to\lesssim 1$, the finite PDF width produces
  visible stochastic spectral fluctuations about the median power law (the
  "non-Gaussianity", distinct from inflationary non-Gaussianity).
- **Null hypothesis:** $N_{\rm c}\geq 1000$. At this value the SMBHB
  point-source superposition is indistinguishable from the infinite-source
  Gaussian GWB. A measurement excluding $N_{\rm c}=1000$ (Savage-Dickey Bayes
  factor) is the signature of the SMBHB Poisson process — provided the average
  inferred power spectrum is also verified consistent with the predicted RMS-strain
  median. The threshold is somewhat arbitrary; lower thresholds make the
  detection harder. (Sampling at $N_{\rm c}>1000$ hits Neal's funnel.)
- Brightest sources *assist* in resolving $N_{\rm c}$: stronger $h_{\rm cw}$
  outliers are compatible with higher $N_{\rm c}$, so a bright CW is itself
  evidence of the Poisson regime.

## NANOGrav 15-yr results (quote verbatim from `main.tex`)

- **No evidence for the astrophysical (Poisson) GWB origin:** inferred
  $N_{\rm c}$ is strongly consistent with the null $N_{\rm c}=1000$ (Sec.
  *Results*, Fig. `posterior_Nc_hc_fcw`). Robust to whether a resolvable CW is
  included. Analysis frequencies span $T_{\rm obs}^{-1}=1.98$ nHz to
  $15\,T_{\rm obs}^{-1}=29.65$ nHz.
- **No resolvable CW:** broad posterior support for $\log_{10}f_{\rm cw}$ across
  the whole prior; the $h_{\rm cw}$ posterior matches the posterior-predictive
  (Fig. `hcw_ht_p_pp`) ⇒ no exceptionally bright CW. $\mathrm{SNR}<4$.
- **Stronger astrophysical CW limits than the agnostic search:** the
  hierarchical prior places **24 of 114** AGN-selected SMBHB candidates in
  tension with NANOGrav, vs **only 1** with the original NANOGrav agnostic
  upper limits (Sec. *Astrophysical limits*, Fig. `limits`). Caveat in the
  text: the tighter constraint is a property of the more restrictive prior and
  does *not* by itself imply more efficient *detection*; signal becomes
  distinguishable from noise at $h_{\rm cw}\approx 10^{-14}$ for both models.
- **Two minor outliers** (App. `app:outliers`), both also seen by NANOGrav and
  *not* interpreted as resolvable SMBHBs: a CW outlier at $2T_{\rm obs}^{-1}=3.95$
  nHz (Bayes factor $3$ in NG15 CW search) that **disappears when HD correlations
  are modeled**; and a GWB power-spectrum outlier at $8/T_{\rm obs}=15.81$ nHz
  (excess $h_{\rm t}$ over posterior-predictive), likely noise contamination.
- **Astrophysical interpretation:** posterior on $(N_{\rm c},h_{\rm c})$ recast
  into $(\rho_{\rm BH}, M_{\rm peak})$ (Fig. `rho_mpeak`) is consistent with
  EPTA DR2 galaxy-demographics inference; the astrophysically-expected
  $N_{\rm c}$ is within the $1\sigma$ edge of the posterior. A brown-contour
  prior choice ([[arxiv_2406_17010]]'s $\rho_{\rm BH}$) sits at
  $\rho_{\rm BH,fid}=4.53\times 10^5\,M_\odot\,{\rm Mpc}^{-3}$.

## CW detection-probability forecast (Table `tab:cw_snr_detection_probabilities`)

Posterior-predictive probability of finding a CW above an SNR threshold;
$p_{\rm max}$ = all-sky all-frequency search for one signal (max SNR across
bins), $p_{\rm rms}$ = root-mean-squared across frequencies (search for a
superposition at all frequencies, future work). Threshold detection defined as
$\mathrm{SNR}_{\rm p}>5$. The 20-yr forecast extrapolates each pulsar's last-year
TOA errors 5 yr forward (frequency-resolution increase neglected).

| $T_{\rm obs}$ | statistic | SNR 2 | SNR 3 | SNR 4 | SNR 5 |
|---|---|---:|---:|---:|---:|
| 15 yr | $p_{\rm max}$ | 7% | 3% | 1% | **0.6%** |
| 15 yr | $p_{\rm rms}$ | 12% | 4% | 2% | 0.9% |
| 20 yr | $p_{\rm max}$ | **18%** | 7% | 4% | **2%** |
| 20 yr | $p_{\rm rms}$ | **43%** | 13% | 5% | 3% |

Headline numbers: 15-yr SNR-5 detection probability $\approx 0.6\%$
($p_{\rm max}$); 20-yr SNR-5 $\approx 2\%$; 20-yr SNR-2 $\approx 18\%$
($p_{\rm max}$) and $43\%$ via the RMS statistic.

## Phenomenology (simulated-data validation)

- 20 pulsars, 100 ns, $15.06$ yr, 289.47-day cadence ($\sim$19 TOAs/pulsar, derived from $15.06\,{\rm yr}/289.47\,{\rm d}$; not separately stated in the source);
  HD correlations neglected in the sims to save cost (would only tighten
  constraints slightly).
- **GWB-only sim:** Monte-Carlo draws from the hierarchical model with fixed
  $h_{\rm c}=2\times10^{-14}$, $\pi(\log_{10}N_{\rm c})=\mathcal U(-3,3)$. Low-$N_{\rm c}$
  realizations show visible deviations from the power-law median; high-$N_{\rm c}$
  matches it. The $\log_{10}N_{\rm c}$ posterior can exclude $N_{\rm c}=1000$.
- **GWB + one brightest source sim:** CW at $2\times10^{-8}$ Hz (near 10th
  Fourier bin), $N_{\rm c}=1$, 250 $h_{\rm cw}$ realizations. The hierarchical
  prior gives tighter $h_{\rm cw}$ constraints than a uniform-$h_{\rm cw}$ CW
  search, but the hierarchical posterior lacks the low-$h_{\rm cw}$ tail, so
  detection must be assessed with Bayes evidence/odds, not by eye. The strongest
  $h_{\rm cw}$ outlier gives the strongest evidence for high $N_{\rm c}$
  (= detection of non-Gaussianity).

## Concepts touched (wiki backlinks)

- [[../concepts/fisher_hierarchy]] — **primary.** This is the observational
  realization of the coherent (brightest-source) channel $D_{\rm coh}\propto p$,
  the top rung of the hierarchy. Its non-detection at the most sensitive channel
  is the empirical floor under the project's "the $C_\ell$ channel is weaker"
  argument.
- [[../concepts/brightest_source_fraction]] — the CW *is* the brightest source;
  $h_{\rm cw}=\max_s h_{\rm s}$ is the dimensional realization of the
  $p$-dominant source. The brightest-source PDF Eq. `eq:p_h_cw` is the
  population-model law for the loudest binary.
- [[../concepts/coherent_vs_incoherent]] — the CW is modeled as a directional,
  deterministic (coherent) signal with a point-source antenna response, while
  $h_{\rm t-1}$ / $h_{\rm t}$ are the isotropic stochastic (incoherent) GWB with
  HD correlations.
- [[../concepts/KL_divergence]] — the model-selection logic ($N_{\rm c}$ via
  Savage-Dickey Bayes factor against the $N_{\rm c}=1000$ null; CW via
  evidence/odds) is the Bayesian instantiation of the project's KL figure of
  merit.
- [[../concepts/SMBH_population_model]] — the $(N_{\rm c},h_{\rm c})\leftrightarrow
  (\rho_{\rm BH},M_{\rm peak})$ recast uses the $M$-$\sigma$ scatter $\epsilon_0$,
  velocity-dispersion function, and the strain-weighted number count
  $h_s^2\,dN/d\log h_s^2$ via a saddle-point (log-normal) approximation.
- [[../concepts/source_background_degeneracy]] — the joint model deliberately
  couples resolved-source and background inference through the shared
  hyperparameters, exchanging information between the CW and GWB channels.

## Paper uses

- **Cited (2026-06-24)** via `\cite{Goncharov:2026joint}` in:
  - `paper/sections/source_detection.tex` (Sec. "Bottom line") — the empirical
    demonstration that the most powerful (coherent CW) channel finds no
    resolvable source in NG15, quoting the 2% (15-yr) / 5% (20-yr) SNR-5
    detection-probability forecast and the IPTA simulated-vs-real-data caveat.
  - `paper/sections/nanograv_prior.tex` (Sec. "What this does and does not
    imply") — that the models which "look ruled out" in $C_\ell$ predict no
    detectable source, and a coherent search indeed finds none.
  - `paper/sections/source_vs_cl_reduced.tex` (appendix).

## Could be cited

- `three_strategies.tex` — as the empirical demonstration that even the most
  powerful (coherent CW) channel finds no source in NG15, so the weaker
  $C_\ell$ channel is uninformative for the astrophysical model.
- New/rewritten **Sections 6-7** — the companion `README.md` names this paper
  as the backbone: NG15 CW non-detection + low 15/20-yr detection probability.
- `nanograv_prior.tex` — the agnostic-vs-astrophysically-informed prior contrast
  (24 vs 1 AGN candidates in tension) is a clean illustration that priors set
  the constraint.
- `introduction.tex` — $N_{\rm c}$ as the smoking-gun detection statistic for
  the SMBHB origin of the GWB.

## Related wiki pages

- [[arxiv_2406_17010]] — Sato-Polito & Zaldarriaga 2025, the distribution paper
  this work directly extends (CW/brightest-source PDF added; full global-fit
  likelihood replacing the per-bin refit).
- [[draft_sufficient_statistics_2026]] — Sato-Polito, Zaldarriaga, Zackay 2026
  draft; complementary information-theoretic framing ($N_s^{\rm eff}\sim 3$,
  max matched-filter significance $\sim 3.8\sigma$) consistent with this paper's
  empirical CW non-detection.
- [[arxiv_2306_16221]] — NANOGrav 15yr anisotropy: same dataset, the $C_\ell$
  search this project argues against; this paper exercises the stronger CW channel.
- [[arxiv_2407_06270]] — Lamb & Taylor; spectral-variance moments of the same
  total-strain PDF.
- [[../concepts/fisher_hierarchy]], [[../concepts/brightest_source_fraction]].

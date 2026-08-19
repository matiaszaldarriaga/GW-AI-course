# The papers

Six, in the order the day uses them. **Read the first one.**

- `1806.10610-selection-and-populations.pdf` — Roulet & Zaldarriaga,
  *Constraints on binary black hole populations from LIGO–Virgo detections*
  (2019). **This is the one to read**, and specifically §3.1 and Fig. 3.
  Four pages give you the entire selection-effect calculation: the angular
  factor, the distance quadrature, the threshold, and the reference PSD. It is
  the target of this afternoon's must-do workshop item, and it is a good target
  because it is *fully specified but not trivial* — about 150 lines — and
  because there is a published figure to check against.

  Read it for two things beyond the recipe. First, the **retreat**: §3.1 makes
  every simplification out loud, in its own voice, and then concedes that a real
  answer needs injections. Second, the **erratum**: Eqs. (13) and (24) both drop
  a Jacobian, and the group's own successor paper reinstates it four years
  later. Neither of those is a criticism. They are what a careful paper looks
  like.

- `2008.07014-the-formalism.pdf` — Roulet, Venumadhav, Zackay, Dai &
  Zaldarriaga, *Binary black hole mergers from LIGO/Virgo O1 and O2* (2020).
  **The formalism paper.** §II builds the hierarchical likelihood from an
  inhomogeneous Poisson process in about two pages, and Eq. (12) is the version
  that admits triggers of *arbitrary* significance — so there is no threshold to
  choose and no information thrown away at the cut. Eq. (22) is the line worth
  memorising: each trigger carries information with weight $p_{\rm astro}^2$,
  which justifies both including marginal events and not going arbitrarily deep.
  Fig. 3's toy model is twenty lines and needs no download.

- `2111.03634-gwtc3-populations.pdf` — Abbott et al. (LVK), *Population of
  merging compact binaries inferred using gravitational waves through GWTC-3*
  (2023). Long; read §II.B and Appendices A–B. Eq. (4) is the same object as
  2008.07014's Eq. (12) in the $p_{\rm astro}\to1$ limit — **putting those two
  side by side is the most useful slide today has**, and the lecture derives the
  collapse rather than asserting it. Appendix B is where the POWER LAW + PEAK
  model and its low-mass taper are written down, and Eq. (B1) is the
  $N_{\rm eff}>4N_{\rm det}$ criterion the whole afternoon turns on.

- `2105.10580-parametrisation-dependence.pdf` — Roulet, Chia, Olsen, Dai,
  Venumadhav, Zackay & Zaldarriaga, *Distribution of effective spins and masses
  of binary black holes* (2021). The best paper in the set for model criticism.
  The LVK's GAUSSIAN model puts 29 % of binaries at $\chi_{\rm eff}<0$; this
  paper gets essentially zero from the *same data* under a different
  parametrisation, and reproduces the LVK number exactly when it adopts the LVK
  model. Also Eq. (7), the "wildcard" subpopulation, which turns a Bayes factor
  into a goodness-of-fit test for a population model — something the standard
  framework does not provide.

- `2402.11439-pe-review.pdf` — Roulet & Venumadhav, *Inferring binary properties
  from gravitational-wave signals* (2024). A review, and the single best entry
  point to everything between strain and a posterior: the Whittle likelihood
  derived from the noise autocorrelation, what is and is not measurable in a CBC
  signal, and then relative binning, marginalisation, reparametrisation and
  simulation-based inference. Read §2.2 before this afternoon if you have not
  met the likelihood before, and §3.1.1 if you want to know why a posterior
  takes hours rather than weeks.

- `2207.03508-cogwheel.pdf` — Roulet, Olsen, Mushkin, Islam, Venumadhav, Zackay
  & Zaldarriaga, *Removing degeneracy and multimodality in gravitational wave
  source parameters* (2022). The code you will be installing this afternoon, and
  why its coordinates look strange. A quasicircular binary has 15 parameters and
  the data measure about 10 combinations; this paper builds coordinates that map
  onto the ones that are measured, and "folds" the posterior over four
  approximate discrete symmetries. Worth knowing before you run it: **folding is
  exact**, not an approximation, and the unfolding is done in postprocessing.

---

## What is not here, and where it went

**The IAS-HM thread** — the higher-harmonic search that finds events the LVK
pipelines miss, and the population inference built on it — gets one slide today
and no paper in this folder. If you want it: arXiv:2312.06631 for the new events
and arXiv:2508.15350 for their population. The detection statistic itself is
arXiv:2405.17400, which we deliberately did not fetch; if you go looking for it,
note that the pipeline paper in the wider repo (`ias-search-pipeline/`) is the
2019 quadrupole-only one and not that.

**The eccentricity papers** are absent on purpose. There is no eccentricity
population constraint anywhere in this group's output — the eccentricity work is
waveform and surrogate modelling, and nobody constrains an eccentric fraction.
So eccentricity is not a third vote on formation channel, and today says so
rather than implying otherwise.

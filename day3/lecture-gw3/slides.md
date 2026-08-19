---
theme: seriph
title: From a catalogue to a population — how LVK black holes form
author: Matias Zaldarriaga
themeConfig:
  primary: '#e8a05c'
highlighter: shiki
lineNumbers: false
editor: false
drawings:
  persist: false
transition: fade
aspectRatio: 16/9
canvasWidth: 980
routerMode: hash
fonts:
  serif: 'PT Serif'
  sans: 'PT Serif'
  mono: 'PT Mono'
  weights: '400,700'
  italic: true
layout: default
---


<div class="absolute inset-0" style="background-image: url('./figures/cover-bg.png'); background-size: cover; background-position: center;"></div>
<div class="absolute inset-0 bg-black/40"></div>

<div class="relative z-10 h-full flex flex-col justify-center items-center text-center text-white">
  <h1 class="!text-white !text-5xl !mb-2 drop-shadow-lg !font-normal">From a catalogue to a population</h1>
  <div class="text-2xl italic opacity-90 drop-shadow">Day 3 &mdash; how LVK black holes form</div>
  <div class="mt-14 opacity-80 text-sm tracking-wide">
    Matias Zaldarriaga &nbsp;·&nbsp; <em>Ondas Gravitacionales e Investigación Asistida por IA</em>
  </div>
</div>

<!--
Day 2 ended at a single trigger with a false-alarm rate. Today starts from the
ninety-odd events that survived that and asks what population produced them:
one posterior per event, a selection function, and a likelihood over the three.
-->

---

# The question of the *day.*

<div class="text-lg mt-8 mb-6">

**How do the LVK binaries form?** All we have is the properties of ninety-odd
events, and from theory a prediction for the population. Getting from one to the
other takes **three steps** &mdash; a **posterior** for each event, meaning the
whole distribution its data leave over its parameters rather than one number; a
selection function; and a hierarchical likelihood.

</div>

<div class="text-lg mb-8">

At every step the wrong answer is smooth, plausible, and comes with error bars
&mdash; which is why every step today is built, not quoted.

</div>

<div class="text-base opacity-80">

What you can see and what is there differ by a factor of **tens** across the
observed mass range. That factor is computable from first principles right up to
the point where it isn't &mdash; which is why everybody runs injections.

</div>

<!--
Open with the science question (the plan's own arc, Matias verbatim: "Open with some science question, we want to know how the LVK binaries form"). No claim device — the question, then the chain that could answer it.
-->

---
layout: default
---

<div class="absolute inset-0" style="background-image: url('./figures/cover-bg.png'); background-size: cover; background-position: center;"></div>
<div class="absolute inset-0 bg-black/55"></div>

<div class="relative z-10 h-full flex flex-col justify-center items-center text-center text-white">
  <div class="font-mono text-xs tracking-widest opacity-80 mb-3">SECTION 1</div>
  <h1 class="!text-white !text-5xl !mb-0 drop-shadow-lg !font-normal">The question, and the options</h1>
</div>

---

# How do these binaries form?

<div class="grid grid-cols-2 gap-8 mt-6">
<div>

<div class="tag mb-2">Isolated binary evolution</div>

Two massive stars, born together, stay together. Common-envelope phase, then a
tight black-hole binary.

**Predicts:** spins roughly **aligned** with the orbital angular momentum
(tides and accretion torque them into line), mass ratios near **equal**, and a
spectrum that stops where pair-instability supernovae take over.

</div>
<div>

<div class="tag mb-2">Dynamical assembly</div>

Black holes sink to the centre of a globular cluster or a nuclear star cluster
and pair up by three-body encounters.

**Predicts:** **isotropic** spin tilts &mdash; the binary has no memory of how
its members were born &mdash; **broad** mass ratios, and hierarchical mergers
that can populate the gap.

</div>
</div>

<div class="mt-8 text-lg">

Two observables discriminate: **the spin tilts** and **the mass ratios**.

</div>

<div class="mt-6 text-base opacity-75">

**We will not settle it today.** This lecture is about what *would* settle it,
and about why the two observables that discriminate are exactly the two the
detector distorts most.

</div>

<!--
Two channels, two discriminating observables — the same two return on the selection slides.
src: borrowed — the aligned-vs-isotropic and mass-ratio channel expectations are the literature's, as the plan records.
-->

---

# The chain, on one slide

<div class="text-xl mt-10 mb-10 text-center tracking-wide">

strain &rarr; single-event posterior &rarr; catalogue &rarr; population

</div>

<div class="slim-table">

| arrow | what it costs | today |
|---|---|---|
| strain &rarr; posterior | a 15-dimensional stochastic sampler, hours per event | beats 3&ndash;5 |
| posterior &rarr; catalogue | a detection statistic, and a threshold you have to justify | beat 7 |
| catalogue &rarr; population | a **selection function** and a hierarchical likelihood | beats 6&ndash;7 |

</div>

<div class="mt-8 text-base opacity-80">

We will come back to this slide five times. Every failure mode today is an arrow
somebody skipped.

</div>

<!--
This is the spine of the spine. If a student remembers one slide it should be
this one.
-->

---
layout: default
---

<div class="absolute inset-0" style="background-image: url('./figures/cover-bg.png'); background-size: cover; background-position: center;"></div>
<div class="absolute inset-0 bg-black/55"></div>

<div class="relative z-10 h-full flex flex-col justify-center items-center text-center text-white">
  <div class="font-mono text-xs tracking-widest opacity-80 mb-3">SECTION 2</div>
  <h1 class="!text-white !text-5xl !mb-0 drop-shadow-lg !font-normal">What a likelihood is, before the formula</h1>
</div>

---

# Vary one parameter at a time and watch

<div class="text-center">
<img src="./figures/sep_parameter_sweeps.png" class="h-96 mx-auto" />
<div class="fig-cap">Whitened templates, last 160 ms before merger, all at the same amplitude and alignment. One parameter moves per panel.</div>
</div>

<!--
The animation sequence lives here: the movie frames in the single-event-posterior reproduction are the same panel function frame by frame. Run them live rather than showing the still if there is time.
The strain trace came off this figure in review 2 (C18): showing that the waveform changes with the parameters is all this beat wants, and the data underneath added nothing to it. The movies still carry the data, because walking off something is what a movie is for. T2 of that review records a disagreement between the data and the plot which this does not resolve and was not meant to.
-->

---

# What each parameter did

<div class="slim-table mt-6">

| parameter | what it does to the model | loss in match |
|---|---|---|
| chirp mass | the phase **drifts out** over the last cycles | 0.024 for 6 % |
| mass ratio | almost nothing moves | 0.050 for a **halving** |
| distance | a pure rescaling &mdash; the shape is untouched | **exactly zero** |
| arrival time | the whole thing slides | &mdash; |

</div>

<div class="mt-8 text-lg">

**This predicts the shape of the posterior before anyone writes it down.**

The parameters that visibly destroy the fit are the ones that come out tight.

</div>

<div class="mt-4 text-base opacity-75">

Distance enters *only* through the amplitude. Hold that thought &mdash; it is
the whole of the next section.

</div>

<!--
The table is read off the sweep figure: the measured match losses of the single-event-posterior panels.
src: fig_sep_parameter_sweeps
src: borrowed — the search ranges (4.3-100 Msun, q in 0.15-1) are the analysis choices recorded in that reproduction.
-->

---

# The same claim, as a number

<div class="text-center">
<img src="./figures/sep_snr_sensitivity.png" class="h-72 mx-auto" />
<div class="fig-cap">Shaded: where the matched-filter SNR is within 1 of its peak.</div>
</div>

<div class="mt-4 text-base">

As a fraction of the range each is **searched over**: the chirp mass is pinned
to **4.1 %** of 4.3&ndash;100 M<sub>&#8857;</sub>, the mass ratio to **75 %** of
0.15&ndash;1. A factor of **18**.

</div>

<!--
Same claim quantified against the searched ranges; the shaded regions are the figure's own measurement.
src: fig_sep_snr_sensitivity  src: snr_width_mchirp_percent_of_itself
-->

---
layout: default
---

<div class="absolute inset-0" style="background-image: url('./figures/cover-bg.png'); background-size: cover; background-position: center;"></div>
<div class="absolute inset-0 bg-black/55"></div>

<div class="relative z-10 h-full flex flex-col justify-center items-center text-center text-white">
  <div class="font-mono text-xs tracking-widest opacity-80 mb-3">SECTION 3</div>
  <h1 class="!text-white !text-5xl !mb-0 drop-shadow-lg !font-normal">Bayes, concretely, on one event</h1>
</div>

---

# Bayes' *theorem.*

<div class="mt-8 max-w-4xl text-base opacity-90 leading-relaxed">

You have a model with parameters $\theta$ and a stretch of data $d$. What you want is the
distribution of $\theta$ given $d$. What you can write down is the distribution of $d$
given $\theta$ &mdash; that is the likelihood, and day 2 built it. The two are related by
one line of conditional probability:

</div>

<div class="my-7 text-center text-2xl">

$$p(\theta \mid d) \;=\; \frac{p(d \mid \theta)\; p(\theta)}{p(d)}$$

</div>

<div class="mt-6 grid grid-cols-3 gap-8 max-w-5xl text-sm opacity-85">
  <div class="border-l-2 border-[#e8a05c] pl-4">
    <div class="tag mb-1">Likelihood</div>
    <div>$p(d\mid\theta)$ &mdash; what the data say. Day 2's $\ln L = -\tfrac12\langle d-h|d-h\rangle$.</div>
</div>
  <div class="border-l-2 border-[#e8a05c] pl-4">
    <div class="tag mb-1">Prior</div>
    <div>$p(\theta)$ &mdash; what you assumed before looking.</div>
</div>
  <div class="border-l-2 border-[#e8a05c] pl-4">
    <div class="tag mb-1">Posterior</div>
    <div>$p(\theta\mid d)$ &mdash; their product, normalised by $p(d)$, which does not depend on $\theta$.</div>
</div>
</div>

<div class="mt-8 max-w-4xl text-base opacity-85">

Everything for the rest of the day is that equation, applied twice: once per event, and
then once to the whole catalogue.

</div>

<!--
Added in review 2 (C19), and the only addition in that pass: the three words were being defined on the figure of the next slide and the theorem itself never appeared. Write it on the board. The denominator is worth one sentence — it is a normalisation here, and on the last slide of the section it is the thing you compare models with.
-->

---

# Three surfaces on one *grid.*

<div class="text-center">
<img src="./figures/sep_bayes_triptych.png" class="h-84 mx-auto" />
<div class="fig-cap">Likelihood, prior and posterior for GW150914 on the same distance-inclination grid.</div>
</div>

<div class="mt-2 max-w-5xl text-sm opacity-85 mx-auto">

Bayes' theorem as three pictures: the **likelihood** (what the data say, day 2's
$\ln L$), the **prior** (what you assumed before looking &mdash; here the volume and
orientation weights), and the **posterior** &mdash; their product, normalised. These two
pictures multiply to give that one.

</div>

<!--
Beat 4, and it cannot be compressed away: nothing in days 1-2 introduces Bayes, priors, likelihoods or posteriors (the plan's own prerequisite audit). The three words are defined HERE, on the figure, not in a formula.
src: fig_sep_bayes_triptych
-->

---

# Why the likelihood is degenerate

<div class="text-lg mt-6">

The data measure the **amplitude**. The amplitude is

</div>

$$ a \;\propto\; \frac{1}{D_L}\cdot\frac{1+\cos^2\iota}{2} $$

<div class="text-lg mt-6 mb-6">

so one detector constrains that **combination** and nothing else. The ridge runs
from **387 Mpc** edge-on to **774 Mpc** face-on: a factor of 2, and no amount of
data breaks it.

</div>

<div class="text-base opacity-80">

The two priors that act on that ridge push the **same way**:

- $\pi(D_L)\propto D_L^2$ &mdash; there is more volume out there
- $\pi(\cos\iota)$ uniform &mdash; there are more orientations near edge-on than near face-on

</div>

<div class="mt-6 text-xl">

Median distance moves **525 &rarr; 612 Mpc**. The posterior is not the
likelihood.

</div>

<!--
Ridge endpoints and both medians stamped by the single-event-posterior reproduction — the slide where 'the posterior is not the likelihood' is seen.
src: triptych_ridge_edge_on_mpc  src: triptych_ridge_face_on_mpc  src: triptych_median_distance_likelihood  src: triptych_median_distance_posterior
-->

---

# Why samples, and not grids

<div class="text-center">
<img src="./figures/sep_grid_vs_samples.png" class="h-80 mx-auto" />
<div class="fig-cap">The same posterior by grid and by samples.</div>
</div>

<div class="mt-2 text-base">

One likelihood evaluation: **1.63 ms**, measured on the machine that made this
figure. Ten points per axis in fifteen dimensions is **52,000 years** &mdash;
and ten points per axis would be a terrible grid.

</div>

<!--
The cost is measured on this machine and stamped; the grid extrapolation is arithmetic on it.
src: cost_likelihood_ms  src: grid_cost_years_d15
-->

---

# The half that matters more

<div class="text-lg mt-10 mb-8">

**You never wanted the density.**

You wanted marginals and expectations &mdash; and samples give you those by
counting, at a cost that does not care about dimension.

</div>

<div class="text-xl mt-10 text-center opacity-90">

Marginalising a grid is an integral.

Marginalising samples is ignoring a column.

</div>

<div class="mt-12 text-base opacity-70">

The triptych two slides ago marginalised a 320 &times; 320 grid. It is the last
time in this course that doing it that way is affordable.

</div>

<!--
The deeper half of the samples argument: marginals by counting. No numbers here.
-->

---
layout: default
---

<div class="absolute inset-0" style="background-image: url('./figures/cover-bg.png'); background-size: cover; background-position: center;"></div>
<div class="absolute inset-0 bg-black/55"></div>

<div class="relative z-10 h-full flex flex-col justify-center items-center text-center text-white">
  <div class="font-mono text-xs tracking-widest opacity-80 mb-3">SECTION 4</div>
  <h1 class="!text-white !text-5xl !mb-0 drop-shadow-lg !font-normal">Selection effects, and the likelihood they enter</h1>
</div>

<!--
This was two sections until review 2. The population-likelihood section lost four of its five slides to the N_eff cuts (C23-C26) and the fifth belongs here anyway: the selection function you have just built is the thing that appears in it (A7, C32).
-->

---

# The scaling you get for free

<div class="text-lg mt-6">

From day 2's SNR, $\rho\propto\mathcal M^{5/6}/D_L$. So the horizon distance goes
as $\mathcal M^{5/6}$ and the Euclidean sensitive volume as

</div>

$$ V \;\propto\; \mathcal M^{5/2}. $$

<div class="mt-6 text-base opacity-80">

Ten minutes, no code, and it reuses machinery you built on day 2. The exponent
comes from the amplitude alone &mdash; it is $5/6$ for **any** noise curve, as
long as the band is held fixed.

</div>

<div class="mt-8 text-lg">

The measured answer is **not** 2.5. Fig. 3 of Roulet &amp; Zaldarriaga (2019)
draws a reference power law at $\mathcal M^{2.2}$.

</div>

<div class="mt-4 text-base">

Over the observed range 8&ndash;40 M<sub>&#8857;</sub>, $\mathcal M^{2.2}$ is a
factor of **34**. Nobody can call that a correction.

</div>

<!--
The 5/6 exponent is day 2's amplitude scaling cubed; the 2.2 reference is the paper's own figure; the factor 34 is stamped.
src: scaling_volume_exponent  src: tilt_8_to_40_at_2p2
src: borrowed — the M^2.2 reference power law is Fig. 3 of Roulet & Zaldarriaga 2019.
-->

---

# The two other axes, which are the sharper argument

<div class="text-center">
<img src="./figures/selection_volume_fig3.png" class="h-96 mx-auto" />
<div class="fig-cap">Sensitive volume along the spin and mass-ratio axes.</div>
</div>

<!--
The chi_eff and q axes of the sensitive volume — the discriminating observables, distorted directly.
src: fig_selection_volume_fig3
-->

---

# Put those together

<div class="text-xl mt-8 mb-8">

You are preferentially detecting the **aligned-spin** systems, and
preferentially missing the **unequal-mass** ones.

</div>

<div class="text-lg mb-8">

At $\mathcal M = 30$ M<sub>&#8857;</sub>: $V(\chi_{\rm eff}{=}{+}0.5)$ is
**1.38&times;** $V(0)$, and $V(q{=}0.16)$ is **0.32&times;** $V(q{=}1)$.

</div>

<div class="text-xl">

Those are **exactly the two observables that discriminate formation channel**.

</div>

<div class="mt-8 text-base opacity-80">

Selection pushes both of them toward the field-binary answer. That is a much
stronger statement than "selection tilts the mass function": the bias sits
directly on the quantity we are trying to measure, not off to one side in a
nuisance parameter.

</div>

<!--
The two ratios are stamped: V(chi=+0.5)/V(0) and V(q=0.16)/V(q=1) at Mc=30. The evaluation points (+0.5, q=0.16) are the exercise's chosen slices, recorded with its stated choices.
src: chi_ratio_plus_half  src: q_ratio_sixteenth  src: fig_selection_volume_fig3
-->

---

# Then the retreat &mdash; and the paper does it in its own voice

<div class="text-base mt-6 opacity-90">

Whether something enters a catalogue depends on glitch rejection, detector
artifacts, PSD drift, **how much your signal resembles the glitches this
particular detector happens to make**, the fact that the catalogue is built from
multiple detectors so the answer depends on both PSDs and on sky location, and on
duty cycle.

</div>

<div class="mt-8 text-base">

Roulet &amp; Zaldarriaga &sect;2 concedes all of it while doing the calculation:

- the reference PSD is *"the harmonic mean of the combined-channel PSDs of the first six events"* &mdash; one fixed curve for two detectors over two runs
- detection is $\rho>9$ on the **expectation value**, with noise fluctuations *"important only near the boundary of the sensitive volume, and we ignore it for simplicity"*
- and a closing paragraph conceding that template-bank effectualness varies too

</div>

<div class="mt-8 text-xl">

**Conclusion: you do injections.**

</div>

<!--
The retreat in the paper's own voice — read the quotes off the slide; this is why the day does no injections and says so.
src: borrowed — the three concessions are quoted from Roulet & Zaldarriaga 2019 §2.
-->

---

# The population likelihood, *built.*

<div class="mt-3 text-base opacity-90 max-w-5xl leading-relaxed">

Take every merger in the universe to be an independent draw &mdash; a Poisson process whose
rate varies with the parameters. A population model $\Lambda$ says how many and where, and
the sensitive volume from ten minutes ago says which of them you see:

</div>

<div class="my-3 text-center text-lg">

$$\frac{dN}{d\theta} = R\,T\,p(\theta\mid\Lambda),
\qquad
N_{\rm exp}(\Lambda,R) = R\,T\!\int\! d\theta\;p(\theta\mid\Lambda)\,P_{\rm det}(\theta)
\;\equiv\; R\,\langle VT\rangle(\Lambda)$$

</div>

<div class="mt-3 text-base opacity-90 max-w-5xl leading-relaxed">

A Poisson process with $N$ points contributes $e^{-N_{\rm exp}}$ times one factor per
point. You never see $\theta_i$, only $d_i$, so each factor is **day 2's likelihood**
integrated against the model:

</div>

<div class="my-3 text-center text-lg">

$$\mathcal L(\{d\}\mid\Lambda,R) \;=\; e^{-R\langle VT\rangle(\Lambda)}
\prod_{i=1}^{N} R\,T\!\int\! d\theta\;p(d_i\mid\theta)\,p(\theta\mid\Lambda)$$

</div>

<div class="mt-3 text-base opacity-90 max-w-5xl leading-relaxed">

Marginalise the overall rate $R$ under a log-uniform prior. That integral is a Gamma
function, the $R^{N}$ and the exponential cancel it, and the selection function comes back
downstairs, once per event:

</div>

<div class="my-3 text-center text-lg">

$$\mathcal L(\{d\}\mid\Lambda) \;\propto\;
\prod_{i=1}^{N}\frac{\int d\theta\;p(d_i\mid\theta)\,p(\theta\mid\Lambda)}
{\langle VT\rangle(\Lambda)}$$

</div>

<div class="mt-4 text-sm opacity-75 max-w-5xl">

That is the case where every event is real. Roulet et al. (2020) derive the general one,
where each trigger carries a probability of being astrophysical instead of a certainty.

</div>

<!--
Rewritten for review 2, C22 — "the formula in the slide is incomprehensible, we need to derive what we are doing and we cannot write a formula filled with symbols no one knows". What was here was LVK GWTC-3 Eqs. (4)-(5) and Roulet et al. 2020 Eq. (12) side by side, in xi, pi_empty, w_i and p_astro, none of which the room has met. Everything on the slide now is a symbol they got this morning: p(d|theta) is day 2's likelihood, written down again on the Bayes slide; P_det and <VT> are the sensitive volume of the previous section; p(theta|Lambda) is the population model.
Board it in this order and it is four lines: rate density, thinning, Poisson, marginalise R. The Gamma integral is the only step with any work in it, and it is done in sympy by the population-likelihood reproduction, which is also where the equivalence with the published forms is established rather than asserted.
src: borrowed — the general p_astro case is Roulet et al. 2020, Eq. (12); this slide derives only its p_astro = 1 limit.
-->

---
layout: default
---

<div class="absolute inset-0" style="background-image: url('./figures/cover-bg.png'); background-size: cover; background-position: center;"></div>
<div class="absolute inset-0 bg-black/55"></div>

<div class="relative z-10 h-full flex flex-col justify-center items-center text-center text-white">
  <div class="font-mono text-xs tracking-widest opacity-80 mb-3">SECTION 5</div>
  <h1 class="!text-white !text-5xl !mb-0 drop-shadow-lg !font-normal">What the population looks like</h1>
</div>

---

# What you see, and what the detector let you see

<div class="text-center">
<img src="./figures/mass_naive_vs_weighted.png" class="h-96 mx-auto" />
<div class="fig-cap">The observed masses against the selection-weighted spectrum.</div>
</div>

<!--
The observed histogram against the selection-weighted one.
src: fig_mass_naive_vs_weighted
-->

---

# Done properly

<div class="text-center">
<img src="./figures/mass_plpeak_fit.png" class="h-72 mx-auto" />
<div class="fig-cap">POWER LAW + PEAK refit against the published intervals.</div>
</div>

<div class="mt-3 text-base">

POWER LAW + PEAK, 69 confident BBH, with the selection integral in the
**denominator of the likelihood** rather than as a reweighting. Everything lands
inside the published 90 % intervals.

</div>

<!--
Our 2-D-slice fit against the published intervals; held-fixed hyper-parameters make our intervals tighter — a property of the method.
src: fit_alpha_median  src: fit_mpp_median  src: fig_mass_plpeak_fit
-->

---

# The spectrum and the rate

<div class="text-center">
<img src="./figures/mass_inferred_spectrum.png" class="h-72 mx-auto" />
<div class="fig-cap">The inferred mass spectrum and rate evolution.</div>
</div>

<div class="mt-3 text-base">

$\alpha = 3.5$, a Gaussian peak at **34 M<sub>&#8857;</sub>**, $m_{99\%}=44$
M<sub>&#8857;</sub> &mdash; down from 60 in GWTC-2 &mdash; **no gap above 60**,
chirp-mass over-densities at 8.3 and 27.9, and
$\kappa=2.9^{+1.7}_{-1.8}$ for the redshift evolution.

</div>

<!--
The PUBLISHED GWTC-3 population features, quoted as the field's answer; our fitted values (alpha 3.64, kappa 3.11) are stamped and on the previous figure.
src: borrowed — alpha=3.5, the 34 Msun peak, m99=44, the 8.3/27.9 chirp-mass over-densities and kappa=2.9+1.7-1.8 are LVK GWTC-3 population results.
src: fit_alpha_median  src: fit_kappa_median  src: m99_at_shipped_medians
-->

---

# Spins &mdash; before any model at all

<div class="text-center">
<img src="./figures/chieff_model_free.png" class="h-64 mx-auto" />
<div class="fig-cap">Per-event effective-spin intervals, no model assumed.</div>
</div>

<div class="mt-3 text-base">

No population machinery, no selection correction. **21 of 69** events sit below
zero, so about **42** are consistent with being noisy measurements of
$\chi_{\rm eff}=0$ and **27 are in excess on the positive side** &mdash; and
none requires a negative tail.

</div>

<div class="mt-6 text-base opacity-80">

Counting is where the agreement stops. Put a population model on the same events and
what fraction sits below zero becomes a statement about **the model you chose**, not
about the events &mdash; two published analyses agree on the width of the distribution
and disagree on what it means. That argument is written out in the wiki rather than
adjudicated here.

</div>

<!--
Model-free first: the per-event chi_eff intervals, counted.
The last paragraph is where parametrisation_dependence lives now (review 2, C33). C27-C29 took the three slides that developed it, and the concept is worth one clause rather than nothing: the LVK Gaussian model puts 29 % of binaries below zero, the three-component mixture of 2105.10580 gets essentially none, both reproduce each other when they adopt each other's model, and both agree that sigma_chi_eff is about 0.11-0.13. Do not adjudicate it in the lecture; the wiki page does the work. NOTE: that review expected check_course to fail on this term — it does not, because parametrisation_dependence is a wiki concept slug and was never a course/terms.yaml row.
src: fig_chieff_model_free  src: n_positive
-->

---

# Beyond this machinery's *reach.*

<div class="text-base mt-8 opacity-90">

- **There is no eccentricity population constraint** anywhere in this group's output. The eccentricity work is waveform and surrogate modelling; nobody constrains an eccentric fraction. So eccentricity is not a third vote on formation channel &mdash; it is at most "here is the machinery that would let you ask".
- **There is no population-synthesis paper in the set.** The channel predictions on the options slide are borrowed, each with one line saying where it came from.

</div>

<div class="mt-10 text-lg">

Saying which questions the machinery **cannot** answer is part of knowing what it
does.

</div>

# Where this leaves us

<div class="text-lg mt-8">

We did not settle how these binaries form. We built the machinery that could, and
found that:

</div>

<div class="mt-6 text-base opacity-90">

- the detector distorts **exactly** the two observables that discriminate
- the distortion is computable from first principles right up to the point where it isn't
- and past that point the honest move is an injection campaign, which is why everybody runs one

</div>

<div class="mt-12 text-xl">

This afternoon: the training wheels come off.

</div>

<!--
The honest boundary: no eccentricity population constraint, no population-synthesis paper in the set.
Two bullets left the closing list in review 2 (C30): "the number you can check is not the number that is sensitive" and the diagnostic-before-you-launch line were the N_eff punchline, and they went with the N_eff slides (C23-C26, A2). What replaced the second is the statement the section actually earns — the analytic selection function runs out and an injection campaign is what you do then.
-->

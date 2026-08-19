# The papers

Twelve, and **day 5 quotes them rather than reproducing them** — that is the
register of the whole day. Two are load-bearing; the rest are where to go if a
pointer interested you.

## Read this one

- `1710.05834-speed-of-gravity.pdf` — Abbott et al., *Gravitational Waves and
  Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A*, ApJL
  **848**, L13. **Read §4.1**, which is one page and contains the entire
  constraint on the speed of gravitational waves.

  Read it for three things. First, the arithmetic is trivial and the paper does
  not hide that — the whole result is a lag divided by a light travel time.
  Second, the distance: it uses 26 Mpc, the *lower* end of the 90 % interval, and
  says why in one sentence. A shorter distance gives a weaker bound, so this is
  the conservative choice and not the obvious one; anyone reproducing it with the
  40 Mpc that gets quoted in talks will get a tighter answer than the published
  one. Third, the caveat: the paper states, in its own voice, that exotic
  emission scenarios widen the window to (−100 s, 1000 s) and loosen the bound by
  two orders of magnitude. Most talks drop that sentence.

  `code/day5/gw170817-speed/` reproduces the published interval from those three
  numbers, and the figure draws the caveat at the same scale as the result.

## The rest of GW170817

- `1710.05832-gw170817-discovery.pdf` — the event: PRL **119**, 161101.
- `1710.05833-multimessenger.pdf` — the sequence, ApJL **848**, L12. Read the
  timeline figure if nothing else.
- `1710.05901-dark-energy-after.pdf` — Ezquiaga & Zumalacárregui, PRL **119**,
  251304. What the speed bound removes, class by class. This is the paper behind
  the lecture's claim that one number closed off a large part of the
  dark-energy model space, and the claim is theirs, not ours.

## The merger

- `2112.06861-tests-of-gr.pdf` — LVK, *Tests of general relativity with GWTC-3*.
  The lecture's beat-1 figure is its Fig. 6: the remnant's mass and spin as
  predicted by the inspiral against the same two numbers as measured after it.
  The ringdown sections are §V.

## The next detectors

- `1607.08697-3g-sensitivity.pdf` — Abbott et al., CQG **34**, 044001
  (LIGO-P1600143). **The source of the noise curves in the horizon figure**, via
  LALSimulation. It also states what those curves are, which matters: single
  detectors with arms at right angles, the ET curve being ET-D for *one* 10 km
  detector and CE being one 40 km detector. That is why CE outruns ET in our
  figure — four times the arm length.
- `1012.0908-et-sensitivity.pdf` — Hild et al., the ET-D curve itself. Punturo
  et al. 2010, the usual ET citation, is not on arXiv; this is where the curve
  in every ET plot actually comes from.
- `1907.04833-cosmic-explorer.pdf` — Reitze et al., the CE horizon study.
- `1702.00786-lisa.pdf` — Amaro-Seoane et al., the LISA proposal. Long; the
  science case is §2 and the sensitivity is §4.

## Lensing, and machine learning as a method

- `2007.12709-morse-phase.pdf` — the Morse phase, and why a frequency-independent
  phase shift is measurable for a coherent signal and not for light.
- `2511.10466-ml-template-banks.pdf` — a learned template bank, and what it costs.
  Row `S-ml-bank`.
- `2507.08318-ml-search.pdf` — machine learning augmenting a real search rather
  than replacing one.

---

The GW231123 lensing release is not here because it is not a paper — it is a
complete public release with code, a locked environment and a map from every
figure to the script that made it. Fetch it from Zenodo record 16279016. It is
the target of row `S-lensing-morse` and of the live experiment in the session,
and it was published after every current model finished training, which is what
makes that experiment clean.

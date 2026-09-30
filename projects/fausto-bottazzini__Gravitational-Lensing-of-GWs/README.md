# Wave-optics gravitational lensing of gravitational waves in a hierarchical triple

Final project for *Gravitational Waves and AI-Assisted Research* (course
repository: [matiaszaldarriaga/GW-AI-course](https://github.com/matiaszaldarriaga/GW-AI-course)).

**The question**: an inner compact binary (the GW source) orbits a third,
more massive body (the lens) far enough away that tidal effects are
negligible. How is the GW lensed, in wave optics, and how does the answer
differ between the late inspiral (a fast chirp, lens effectively frozen) and
an earlier, wider phase of the same binary (quasi-monochromatic, lens
genuinely moving)?

**Where to start reading**: [`report/report.pdf`](report/report.pdf), the
five-page summary, or [`report/report.html`](report/report.html), the slide
deck with live figures. The previous 15-page report is preserved as
[`report/informe_long.pdf`](report/informe_long.pdf), with its source in
[`report/informe_long.tex`](report/informe_long.tex). For the full derivation (wave equation to scalar
field, the point-lens closed form and its checks, the triple's geometry),
read [`theory/theory.pdf`](theory/theory.pdf), written as a self-contained
textbook chapter. Everything below this line is either a map of the repo or
about *reproducing* those two documents, not about the physics itself.

**If you are an agent**: read `theory/theory.tex`, not `theory/theory.pdf`.
The PDF is read by rendering every page as an image, which is expensive; the
source is the same content for the same token cost (~135 000 characters against
a ~540 KB PDF) and reads perfectly well as text. `theory/OUTLINE.md` is the map
of it, and explains why there is deliberately no Markdown copy.

## Repository map

| | |
|---|---|
| `report/` | the results: `report.html` (a slide deck with live figures), `report.pdf` (the five-page written report), and `informe_long.pdf` (the archived 15-page version). Each PDF has its matching `.tex` source; `report.bib` cites `theory/refs.bib` as well. `report.html` is the file itself, not a build artefact; `update_report_data.py` refreshes the animation data embedded in it from `cases/*/caseX_animation_data.json` |
| `theory/` | the derivation, as a textbook chapter: `theory.tex` -> `theory.pdf` |
| `src/gwlens/` | the physics library: wave optics (`waveoptics.py`), orbits (`geometry.py`), the source's line-of-sight kinematics (`doppler.py`), the inner-binary waveform (`imr_waveform.py`, `taylorf2.py`, `chirp.py`), the one pinned system (`system.py`) and the constants everything works in (`units.py`) |
| `cases/` | `FIGURES.md`, what every figure in both cases shows and which script writes it |
| `cases/case_A_chirp/` | the static-lens case: `run.py`, its figures, `RESULTS.md` (what they show), and `provenance/` — `numbers.json`, every number the case reports, written by the run rather than typed, and `claims.yaml`, which ties each claim to the code and the check behind it |
| `cases/case_B_monochromatic/` | the moving-lens case, same structure |
| `tests/` | every correctness check the case `RESULTS.md` files and `provenance/claims.yaml` point at; each file runs on its own and prints one PASS/FAIL line per check |
| `wiki/` | this project's own working notes: `conventions.md` (notation/units, read this before the code), `log.md` (decision log, including every bug caught and what caught it), `todo.md`. Also `final-project.html`, a local copy of the course assignment this project is answering, kept here so the repository carries its own brief |
| `bibliography/` | the DOI of every work cited and an arXiv link where there is a free preprint. The PDFs are deliberately not committed — they are copyrighted by their journals |
| `checks/independent_review/` | gitignored working space for fresh-agent reviews; kept empty between them |
| `reproduce.sh` | the entry point for rebuilding any of it (below) |

## What each case actually shows

Both cases are the *same* hierarchical triple (`src/gwlens/system.py`: a
20+15 M<sub>&#8857;</sub> inner binary, a 5&times;10<sup>4</sup> M<sub>&#8857;</sub>
lens, a 4-day, near-edge-on outer orbit), at two epochs of its inspiral:

- **Case A** (`cases/case_A_chirp/`): late inspiral, the chirp sweeps 10 Hz
  to merger in 15 s — far too fast for the outer orbit to move, so the lens
  is frozen at one impact parameter for the whole signal. Shows the
  frequency-domain interference fringes across the band, the extended
  amplification pattern on the source plane (and how finely it's resolved
  changes with frequency), and the lensed vs. unlensed chirp — including a
  genuine **echo**: a second, 4x fainter copy of the whole merger and
  ringdown arriving 3.43 s later, which is the two-image picture of
  geometric optics showing up in the time domain.
- **Case B** (`cases/case_B_monochromatic/`): earlier, wider inspiral,
  f=0.05 Hz and nearly constant over a 12-day (3 outer period) observation.
  The outer orbital motion *is* resolved: the impact parameter sweeps
  through the same diffraction pattern once per period, producing periodic
  "repeated lensing" amplification pulses — and exactly half of each orbit
  turns out to be unlensed entirely (the source is in front of the lens,
  not behind it). It also shows the thing that is *bigger* than the
  lensing: the same orbit moves the source along the line of sight at
  v/c=0.0165, and the light-travel (Roemer) delay that produces writes 90 GW
  cycles of phase against the lens's 0.017 — a factor of 5206. The pulses
  are real and correctly computed; they are simply not the largest thing
  the outer orbit does, which is a distinction this project got wrong until
  late and now states in both directions. The two are still separable, but
  not by *when* they happen: the Roemer delay is extremal at the very
  instant the pulse peaks, when the source passes behind the lens. It is the
  Doppler *shift*, the delay's derivative, that is a quarter period out of
  phase and vanishes there. What separates them is *what* each one touches
  &mdash; the kinematics are pure timing and leave the strain envelope
  intact to about one part in 10<sup>5</sup>, so the lensing pulse lives in
  |F| and the kinematics move only the phase.

Each `RESULTS.md` states every number with a pointer to the function that
produced it and the check behind it; nothing there is asserted without both.

Most figures are PNGs, generated by the case scripts. One is not:
[`cases/case_B_monochromatic/caseB_one_period.html`](cases/case_B_monochromatic/caseB_one_period.html)
is a page rather than an image because one outer turn holds 17280 carrier
cycles, so no fixed picture shows the turn and the wave at once — it zooms,
pans, and has a button per stage of the orbit. Open it directly; like
`report/report.html`, it embeds its own data and needs no server.

## Reproduce everything

`reproduce.sh` is a Bash script, so on Windows run it from **Git Bash or
WSL** — it does not run from PowerShell or `cmd`. Nothing else here needs a
POSIX shell: every `cases/*/run.py` and every `tests/test_*.py` is runnable
on its own with plain `python`, from any shell, and together they cover
everything except building the two PDFs.

```
git clone https://github.com/fausto-bottazzini/Gravitational-Lensing-of-GWs.git
cd Gravitational-Lensing-of-GWs
./reproduce.sh          # checks + both cases (~1-2 min, creates .venv)
./reproduce.sh checks   # just the correctness checks (fast, no figures written)
./reproduce.sh cases    # just the two cases: figures, numbers, report.html
./reproduce.sh html     # just report.html, from the case data already on disk
./reproduce.sh theory   # rebuilds theory/theory.pdf (needs a LaTeX install)
./reproduce.sh report   # rebuilds the five-page report.pdf and report.html (LaTeX)
```

Note that `cases` and the default run both end by regenerating
`report/report.html`, which inlines `cases/*/caseX_animation_data.json`: that
keeps the deck from going stale against freshly-written case data, but it does
mean the default run leaves `report/report.html` modified even when the data
comes out identical. `git status` after a run, and `git checkout
report/report.html` if you did not mean to touch it.

No step needs anything pre-installed beyond Python 3.11+ and (for the
`theory`/`report` steps only) a working LaTeX distribution (MiKTeX/TeX Live,
with `pdflatex` and `bibtex` on `PATH`) — `reproduce.sh` creates its own venv
and installs the four pinned dependencies (`requirements.txt`) into it.
Nothing in `tests/` needs LaTeX.

Each case script (`cases/case_A_chirp/run.py`,
`cases/case_B_monochromatic/run.py`) is also runnable on its own and takes
well under a minute; each `tests/test_*.py` is runnable on its own too and
prints a PASS/FAIL line per check.

### One waveform, two possible sources — read this before Case A surprises you

Case A's unlensed gravitational waveform (`src/gwlens/imr_waveform.py`)
tries, in order:

1. **`pycbc`'s `IMRPhenomD`** (Khan et al. 2016) — a published,
   NR-calibrated approximant with a real merger and ringdown, exactly what
   LIGO/Virgo pipelines use. This is what the figures and numbers
   *committed in this repository* were generated with.
2. If `pycbc` cannot be imported: **`src/gwlens/taylorf2.py`**, a
   hand-built, from-scratch, restricted 2PN inspiral — validated on its own
   terms (`tests/test_taylorf2.py`) but with no merger or ringdown (cut off
   at the ISCO frequency, where the post-Newtonian approximation itself
   stops being valid).

**`pycbc` is not in `requirements.txt`** and is not expected to install on
native Windows in any reasonable time (`lalsuite`'s dependency resolution
hangs there — see `wiki/log.md`). It installs cleanly with a plain
`pip install pycbc` on Linux and macOS, **including WSL2** (this is exactly
how this repository's own Case A results were produced, from a Windows
machine, without needing native Windows support at all):

```
# inside WSL2 Ubuntu (or any Linux/macOS shell):
cd Gravitational-Lensing-of-GWs        # the SAME repo, e.g. via /mnt/c/... on WSL
python3 -m venv .venv-wsl
source .venv-wsl/bin/activate
pip install pycbc mpmath                # do NOT use -r requirements.txt here:
                                         # those numpy/scipy versions are pinned
                                         # for the Windows fallback venv and can
                                         # be too old for pycbc's own build/wheel
                                         # requirements on a newer Python (as on
                                         # a fresh WSL2 Ubuntu install) -- pip
                                         # resolves compatible modern versions on
                                         # its own; see wiki/log.md
python3 cases/case_A_chirp/run.py      # now uses IMRPhenomD automatically
```

Nothing else changes: the same script, the same command, on Linux/macOS/WSL2
picks up `pycbc` automatically and produces the full inspiral-merger
-ringdown result; on native Windows without `pycbc` it falls back to
TaylorF2 automatically, with a clear label
(`numbers.json`'s `waveform_source` field) recording which one actually
ran. Case B, `tests/`, and everything else never touch `pycbc` at all.

**Caution:** afterwards, running `reproduce.sh checks` (or `cases`/`all`) on
*native* Windows regenerates `tests/CHECKS_imr_waveform.json` and Case A's own
`numbers.json`/figures with the TaylorF2 fallback, since that venv has no
`pycbc` — overwriting the WSL-produced, pycbc-based results this repository
actually ships. It is no longer silent about it: the script prints a warning
naming the files it just overwrote and the `git checkout` that undoes it. If
you want to reproduce the exact committed Case A numbers and figures
(including the ~3.4 s second-image echo), do it from the WSL venv above, and
do it last, right before comparing against what is committed.

A smaller one, so it does not look like a symptom of that: running the checks
also rewrites `tests/CHECKS_doppler.json`, changing one reported figure from
`2.35e-10` to `2.36e-10`. That is last-bit variation between platforms in a
finite-difference check whose tolerance is `1e-6`, it means nothing, and
`git checkout tests/CHECKS_doppler.json` undoes it. Two dirty files after a
check run are expected; only one of them is the pycbc clobber.

## Reproducibility test this repo was held to

Per the assignment ([`wiki/final-project.html`](wiki/final-project.html), kept here as a local copy): *hand it to a fresh
agent that knows nothing, ask it to reproduce a result, and see how far it
gets.* This repo was checked that way repeatedly, always by agents with no
prior context: three passes during the build, each fixing what the last one
found, a fourth over the finished repository, and a final round of six at
once, one per part of it. The same test can be repeated by anyone with a
copy of this repo and an agent. `checks/independent_review/` is where those
passes were written up; it is gitignored and is left empty once a round has
been acted on.

What those passes were good for and what they were not is recorded in
`wiki/log.md`. Briefly: the three build passes found the Fourier-sign bug, a
`reproduce.sh` isolation bug, and an aliased animation panel; all three missed
that the
source's own kinematics were not modelled at all, which turned out to be the
largest effect in Case B. A review returns a list whether or not anything is
left to fix, so the list has to be filtered before it is acted on.

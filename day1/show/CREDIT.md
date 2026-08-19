# Credit — what is in this directory and where it came from

Rule 1b: material this repo did not produce gets one line of origin, and no more.

| file | origin |
|---|---|
| `gw_tutorial.html` | Mark Ho-Yeuk Cheung (Institute for Advanced Study), *Seeing Gravitational Waves* — handed to MZ 2026-08-10 in `gw_visual_workshop.tar.gz`, copied here byte-identical (6.9 MB, self-contained). |
| `prompts.txt` | the same tarball, byte-identical: the four prompts that built it, verbatim, in the order they were given. |
| everything else in this directory | there is nothing else. The session's own page is `day1/session-ai.html`, one level up: built by `code/build_show.py` from `code/day1/show/` and synced by `code/day1/make_day.py`, which fails if that copy differs. Rule 1a, not 1b. |

**Permission.** From his `README.txt`: *"The visualizers and tutorial were written by
Claude Code under my direction, and I am happy for them to be reused and adapted for
teaching."* The waveforms are the SXS Collaboration's public catalog and should be cited
as that collaboration asks.

**Model and effort.** Also from his `README.txt`: *"Every one was run in Claude Code with
Claude Opus 5 at medium reasoning effort; the setting was not changed between prompts."*
That is the sentence day 1's slide quotes.

**The five standalone visualisers are deliberately not here.** The tarball also ships
`gw_visualizer.html`, `glyph_options.html` and the three all-sky pages. `gw_tutorial.html`
embeds all five and mounts each in an iframe when the reader reaches it, so shipping both
would double 6.9 MB for nothing. They are in `input/gw_visual_workshop.tar.gz` if one is
ever wanted on its own.

**The house style comes from here too.** `code/show_template.html` is derived from his
`tutorial_template.html` in the same tarball — his chrome and his CSS, our content. Every
page this course builds, day 1's session included, is that shell. The same credit line is
at the top of that file.

Catalogued at `wiki/specimens/gw-visual-workshop.md`.

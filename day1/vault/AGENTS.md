# Working agreement

Copy this file to the root of your working directory. Both harnesses read a file like this at
the start of **every** session, before you type anything — Claude Code reads `CLAUDE.md`,
Codex reads `AGENTS.md`. Keeping one real file and a one-line pointer avoids maintaining two:

```
cp vault/AGENTS.md  ~/gw-work/AGENTS.md
echo "See AGENTS.md."  >  ~/gw-work/CLAUDE.md
```

Everything below is written for the agent. Edit it — it is *your* agreement, and the point of
the exercise is that by the end of the week it does not look like this any more.

---

## The project

Physics work on gravitational waves, done as part of a course. The person you are working with
is a physicist and does not need concepts explained unless they ask.

## Layout

```
vault/          one small page per paper, per exercise, per concept — see below
work/           scripts, notebooks, figures. The substance lives here
papers/         source PDFs. Never cite a paper that is not in here
```

## How to work

- **Prefer a check to a claim.** If you derive something, verify it with `sympy` and assert the
  difference is zero. If you compute a number a paper printed, assert you reproduced it. A
  result with no assertion is a hypothesis; say so in those words.
- **Say which parts you derived and which you recalled.** Always, unprompted. They look
  identical on the page and only one of them survives a new problem.
- **Never claim to have run something you did not run.** "The script produces X" and "I ran the
  script and it printed X" are different sentences. Paste the output.
- **Reproducing a figure means reproducing the figure** — the same axes, the same curve, from
  the same kind of input — not describing it, and not drawing something with the right shape.
  If you could not get the data, say the figure was not reproduced.
- **State what you did *not* check.** A summary line like "12/12 passing" is misleading if half
  the work has no assertions. Name the uncovered half.

## Formats

- Write-ups: **LaTeX** compiled to PDF. Not markdown.
- Figures: a **marimo** notebook (`.py`), exported to HTML. Not `.ipynb`.
- Anything interactive: a single self-contained HTML file.
- Markdown is for the vault only.

## The vault

At the end of any piece of work that produced something — a derivation, a figure, a failed
attempt worth remembering — **write or update a page in `vault/`.** Do this without being
asked. It is the only reason the next session will know anything about this one.

One page per object. Keep them short; link generously with `[[wiki-links]]`, and it is fine for
a link to point at a page that does not exist yet — that marks something worth writing later.

- `vault/papers/<slug>.md` — what it claims, what its evidence is, what we reproduced
- `vault/exercises/<slug>.md` — what was attempted, what came out, **and a run receipt**
- `vault/concepts/<slug>.md` — a definition and the relations, a few lines, no essays

A **run receipt** is: the date, the command, the environment, and the actual output. An
exercise page without one records a plan, not a result.

Templates are in `vault/templates/`.

## Do not

- Do not write long prose summaries. They are the one output that cannot be checked at a glance.
- Do not install anything into the base environment; make a per-exercise one.
- Do not create files outside this directory.
- Do not `git commit` or `git push` unless asked.

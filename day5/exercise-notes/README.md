# Does the agent read the notes?

One question, four directories, one difference: how the agent comes to read a
project's own notes — or whether it does at all.

| cell | in the directory before you start | what to watch |
|---|---|---|
| `a/` | nothing | what it says with no notes at all |
| `b/` | the notes | whether it opens them |
| `c/` | the notes, and a `CLAUDE.md` that mentions them | what changes |
| `d/` | the notes, and a **skill** that says to read them | whether the skill fires unasked |

Cells `a/` and `b/` you make yourself. `c/` and `d/` are here, and need the notes
copied in.

## The notes

`wiki/` is a real project wiki — the working notes behind Zaldarriaga &
Sato-Polito, *Anisotropies in the PTA gravitational wave background*. 105 pages,
built up over a year: an index, a notation contract, a formula list with equation
labels, fifteen concept pages, a page per source read, a page per script, and an
append-only log. Its `reviews/` section is not included; nothing else was changed.

It is here so you can see what one looks like after real use, and find out what an
agent does with it.

## Run it

```
mkdir a b
cp -r wiki b/
cp -r wiki c/
cp -r wiki d/
```

Then, from **inside each directory** — the tools read `.claude/` and `.codex/`
from where you launch, so `cd` first:

```
cd a && claude          # paste PROMPT.txt as the first message
cd b && claude
cd c && claude
cd d && claude
```

or headless, if you would rather leave it:

```
cd a && claude -p "$(cat ../PROMPT.txt)" --output-format json > ../run-a.json
```

Same model in all four. Ours was Claude Sonnet 5 and each took two to three
minutes. With Codex it is `codex` in place of `claude`; the skill is installed for
both.

## What to compare

**The answer.** The question has a right answer and it is not the obvious one.
Write down what each cell said before you look at the next.

**Whether it opened anything.** The interesting cell is `b/`, where the notes are
present and nothing points at them.

**What it costs.** Reading is not free. Count the turns.

**What it says about its own sources.** A cell that read the notes can tell you
which page it used. A cell that did not cannot, and may not say so.

## Then

Put your own project's notes in a directory and run the same four cells on a
question you already know the answer to. That is the only version of this
experiment that tells you anything about your own work.

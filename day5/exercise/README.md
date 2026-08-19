# Day 5 — one task, three directories, one difference

The same task, the same model, three times. The only thing that differs is what
was sitting in the directory before the agent started:

| cell | in the directory before you start | what to watch |
|---|---|---|
| `a/` | nothing | where the number ends up |
| `b/` | a skill **and** a hook | whether the hook ever has to fire |
| `c/` | the hook only | the turn where it does |

Cell `a/` is an empty directory you make yourself. Cells `b/` and `c/` are here.

## Run it

```
cp -r <the course tree>/day5/exercise ~/day5-exercise && cd ~/day5-exercise
mkdir a
cp <the course tree>/day1/papers/PhysRev.136.B1224.pdf a/ b/ c/
```

Then, in each cell **from inside that directory** — the tools read `.claude/` and
`.codex/` from where you launch, so `cd` first:

```
cd a && claude          # paste ../PROMPT.txt as the first message
cd b && claude
cd c && claude
```

or, if you would rather leave the room and come back to it,

```
cd a && claude -p "$(cat ../PROMPT.txt)" --output-format json > ../run-a.json
```

and the same for `b` and `c`. Use the same model in all three; ours was Claude
Sonnet 5, and each cell took three to five minutes.

With Codex it is `codex` in place of `claude`, and one thing more: **Codex will not
run a hook it has not seen before.** In `b/` and `c/`, type `/hooks` first and
trust the two hooks it lists (the same script at two events), or run
`codex exec --dangerously-bypass-hook-trust "$(cat ../PROMPT.txt)"`. A cell whose
hook silently never fires is not the experiment.

## What is in `b/` and `c/`

```
b/
  .claude/provenance/numbers.md      the convention, written once: what a
  .claude/provenance/claims.md         recorded number, claim and figure look
  .claude/provenance/figures.md        like. Nothing else restates it
  .claude/skills/provenance-record/SKILL.md   the skill: it POINTS at the three
                                       files above, so a fresh session follows
                                       them from the start
  .claude/hooks/provenance_gate.py   the hook: at Stop, checks what was left
                                       behind and, on failure, prints whichever
                                       of the three files applies
  .claude/settings.json              wires the hook for Claude Code
  .codex/hooks.json                  the same wiring for Codex
  .codex/skills/provenance-record/   the same SKILL.md, for Codex
c/
  the same, without the two skills/ directories
```

The hook fires at `Stop` — the moment the agent decides it is finished. A
non-zero exit puts its message into the conversation as a new turn, and the
agent is not finished after all. In `b/` the skill is the normal route and the
hook is the one that still works when the skill does not get loaded. In `c/` the
hook is all there is.

## What to compare

- What each cell left on disk. `a/` will have a script and a figure; is the
  number anywhere but the chat?
- `b/provenance/` against `c/provenance/`: `numbers.json` and `claims.yaml`.
  How many claims, how many figures, how many choices; which library call each
  one names.
- How many turns each took, and whether the hook fired. In an interactive
  session the hook's message appears in the conversation as a new turn; with
  `-p`, `num_turns` is in the JSON and the transcript is under
  `~/.claude/projects/`.

Nothing in the three cells is broken on purpose. The difference is presence or
absence.

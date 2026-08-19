# Your vault

A directory of small, interlinked markdown pages: one per paper, one per exercise, one per
concept. Written mostly *by* the agent, mostly *for* the agent. Read it in
[Obsidian](https://obsidian.md) if you want the graph view; it is plain files either way.

It exists for one reason. **Every session starts cold.** Close the terminal and everything
the agent knew — your conventions, the bug you found, why you rejected the obvious approach —
is gone. The vault is the part that survives.

## There is nothing automatic about it

Worth being blunt, because it is easy to assume otherwise: no tool writes this for you. It
happens because a file in your working directory *tells the agent to do it*, and that file is
read at the start of every session. That is the whole mechanism.

```
cp AGENTS.md          ~/gw-work/AGENTS.md      # Codex reads this
echo "See AGENTS.md." > ~/gw-work/CLAUDE.md    # Claude Code reads this
mkdir -p ~/gw-work/vault/{papers,exercises,concepts}
```

Then work normally. When something is finished, the agent should write the page without being
asked. If it doesn't, that is a bug in `AGENTS.md`, not in the agent — fix the file.

## The one rule that makes it useful

**A catalogue over artefacts, not a container.** The substance lives in `.py`, `.tex` and
`.html` files. The vault says what exists, where it came from, whether it was verified, and
what it depends on. If your pages start containing the derivation instead of pointing at it,
you have built a worse version of a notebook.

Corollary: every exercise page carries a **run receipt** — date, command, environment, actual
output. A page without one records an intention.

## Templates

`templates/paper.md`, `templates/exercise.md`, `templates/concept.md`. Copy and fill; ignore
fields that do not apply.

## Edit the agreement

`AGENTS.md` as shipped is my working agreement, not a standard. It is the most valuable file
in your working directory and the one most worth changing. When the agent does something you
did not want twice, that is not bad luck — it is a missing line in that file.

By the end of the week yours should not look like mine.

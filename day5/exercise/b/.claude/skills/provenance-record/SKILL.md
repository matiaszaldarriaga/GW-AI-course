---
name: provenance-record
description: Use whenever you produce a figure, a number, or a quantitative claim. Records what is being asserted, what produced it, what was written from scratch against what came from a library, and every choice that had a defensible alternative. Work that produced a figure or a number is not finished until the record exists.
---

# Provenance

Somebody else has to be able to take what you leave and find out where every
number came from without asking you. Two files do that, in `provenance/`:

| file | what goes in it | the format |
|---|---|---|
| `provenance/numbers.json` | every number you report | `.claude/provenance/numbers.md` |
| `provenance/claims.yaml` | what you assert, and what backs it | `.claude/provenance/claims.md` |
| `provenance/claims.yaml`, `figures:` | every figure you leave | `.claude/provenance/figures.md` |

**Read the format file before writing each one.** They are short and they are
the single statement of the convention — this skill does not restate them,
because a convention written twice drifts.

It is not a summary of what you did, and it is not a log. It is the map from
each thing you assert to the thing that establishes it.

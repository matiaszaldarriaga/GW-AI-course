---
name: build-project-wiki
description: Use when a project has accumulated notes, code, results and sources but no single place that says what is known — or when asked to build, seed or reorganize a project wiki. Produces a derived knowledge base an agent reads before answering and writes back into.
---

# Building a project wiki

**This is one worked example, not a standard.** It is the pattern behind the wiki
in `../exercise-notes/wiki/`, which was built this way and used for a year. The
shape below is worth starting from and worth changing: a project with different
material wants different directories, and the only parts that have earned their
place everywhere are the index, the conventions page and the rule about what is
derived. Change the rest to fit what you actually have.

A wiki is DERIVED. Everything in it restates something that exists elsewhere in
the project. If a page ever contradicts the code, the paper or a raw source, the
page is wrong and gets corrected — not the other way around. When in doubt about
a fact, read the source, not the wiki.

Build it in three passes. Do not try to do them at once.

## Pass 1 — the skeleton, and the contract

```
wiki/index.md          the map. Read first, always. Every page reachable from here.
wiki/conventions.md    the notation contract: what each symbol means HERE, where the
                       literature uses it for something else, and every
                       non-negotiable choice. The most valuable page in the wiki.
wiki/log.md            append-only: what was ingested, decided, corrected, and when.
wiki/todo.md           what is unresolved. A number you could not find goes here.
wiki/concepts/         one page per idea. Each is CANONICAL for its topic.
wiki/sources/          one page per thing read.
wiki/code/             one page per module or script.
```

Seed `conventions.md` from two places: whatever notes already exist, and **every
mistake the project has already made**. A convention with a correction attached is
worth ten without one. Record the date each was settled — a reader needs to know
whether a published version predates it.

## Pass 2 — ingest, one kind at a time

For each source, notebook, module, script, result and figure:

1. **Read it end to end.** Not the README, the thing.
2. Write `wiki/<kind>/<slug>.md`: a one-paragraph summary, the key results with
   anchors back into the original, and what it depends on.
3. For every concept it touches, open that concept page and add a link **back**.
4. Append one line to `index.md` and one to `log.md`.

**Link, never copy.** Two pages saying the same thing will disagree within a month.

## Pass 3 — rewrite the index

Only now, with everything in place. The index is not a file listing: it is grouped
by what somebody would come looking for, and it says what each page is canonical
for. A page not reachable from the index does not exist.

## Standing rules

- **One canonical owner per topic.** Everything else links to it.
- **Never invent a number.** If one is needed and not available, it goes in
  `todo.md` and you stop.
- **Anything untracked needs a regeneration command**, recorded in the same step
  that creates it.
- **When asked to compare, summarize or synthesize**, the answer is a candidate
  for a new page. Offer to file it.

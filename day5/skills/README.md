# Two skills to take away

These are not part of an exercise. They are tools, written to be installed once
and used in your own projects.

| | |
|---|---|
| `project-notes/` | read a project's notes before answering a question about it |
| `build-project-wiki/` | build those notes in the first place |

They are a pair. The second makes something the first can use.

Both are **examples to tweak**, not standards to follow. They are two files;
read them, change what does not fit your work, and keep your version.

## Installing

A skill is a directory with a `SKILL.md` in it. Copy the ones you want into
whichever harness you use — both, if you use both:

```
cp -r project-notes build-project-wiki ~/.claude/skills/
cp -r project-notes build-project-wiki ~/.codex/skills/
```

Installed there they apply everywhere, in every project, without being mentioned.
A skill is loaded when the session decides its `description` matches what you are
doing, which is why the description is the part worth arguing about: it is the
whole of what the agent sees before deciding whether to read the rest.

## Where they came from

`build-project-wiki` is the pattern behind the wiki in `../exercise-notes/wiki/` —
the working notes of a real paper, written up as a general instruction. That
project's own version lives in its `CLAUDE.md`, and the wiki records the day it
was started and the bug that prompted the first entry in its conventions page.

`project-notes` is what makes any such wiki reachable. `../exercise-notes/`
measures whether it is: four directories, one question, and the difference is
whether anything tells the agent that the notes are there.

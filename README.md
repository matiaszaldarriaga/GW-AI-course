# Gravitational Waves and AI-Assisted Research

*Ondas Gravitacionales e Investigación Asistida por IA* — a five-day graduate course.

Two subjects taught at once: how gravitational-wave astronomy works, and how to actually do
research with AI agents. Each day carries one of each.

| Day | Science | Way of working |
|---|---|---|
| **1** | Fundamentals — where the waves come from | what an agent *is* |
| **2** | Ground-based detection — how we hear them | navigating code nobody in the room knows |
| **3** | From observations to astrophysics | scaling out: jobs, remote, parallel |
| **4** | Pulsar timing arrays — the nanohertz sky | more than one of them: roles, and an independent check |
| **5** | Open problems | turning a result into an output |

Days 2–5 are built around papers: the lecture introduces them, the session reproduces or
attacks them.

---

## Start here

1. **`setup/`** — do this **before** the first class. Install an agent, install Python, run
   `doctor.py`, send us the report. It is the only thing that must happen in advance.
2. **`day1/`** — everything for the first day.

Something broken? Do not fix it by hand — you have an agent:

```
claude "read setup/SETUP.md and fix my environment"
codex  "read setup/SETUP.md and fix my environment"
```

---

## How the material is organised

Each day has the same things, so you always know where to look:

| | |
|---|---|
| `lecture-*/` | the physics half — `slides.pdf` to read, and **the whole slidev source it was built from**: `slides.md`, the figures, the config, the build script |
| `session-ai*.html` | the AI half. One built page — open it and you have the hour, including the prompts, the runs and what they produced |
| `papers/` | the papers themselves. Every paper we discuss is here |

And three pages that belong to no day:

| | |
|---|---|
| `homework.html` | every exercise the course sets |
| `using-the-tools.html` | what each day introduces, in one place, as a reference to keep |

`backup/` holds a single deck holding the slides cut from the five lectures for
room. Everything in it is still true; a slide cut because it was wrong is not there.

---

## What you are given, and what you are not

You get the slides, the papers, the data a task needs, and the prompts. **You do not get our
worked answers.** The reproductions we built, the archives of our own runs and the notebooks
of our own figures stay out of this tree on purpose: if you want to check something, run it.

Day 2's strain data and day 5's exercise scaffold are here because a task cannot start
without them.

---

## What this course is not

It is not a set of best practices for using AI in science. Nobody has those yet, and anyone who
tells you otherwise is selling something. It is a catalogue of what one working group actually
does in mid-2026, offered as a starting point to argue with.

The physics, on the other hand, is not provisional.

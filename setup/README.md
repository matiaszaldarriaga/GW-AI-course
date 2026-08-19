# Before the first class

*Gravitational Waves and AI-Assisted Research*

The course is hands-on from the first minute. In the first session you will point an AI agent
at a physics paper and watch what it does, on your own machine. That only works if your machine
is ready **before** you arrive, so please work through this page and send us the report at the
bottom.

It should not take long. If it drags, stop and tell us — see *If you get stuck*.

---

## 1. An agent CLI

You need at least one of these installed and logged in. **Both is better** — we compare
them in class, and the differences are part of the point.

| | Claude Code | Codex CLI |
|---|---|---|
| Install | https://docs.claude.com/en/docs/claude-code/setup | https://developers.openai.com/codex/cli |
| Log in | `claude` then `/login` | `codex` then `/login` |
| Check | `claude --version` | `codex --version` |

**Access.** You need a working login for at least one of them. If you do not have one,
tell us before the course rather than on the day.

## 2. Python

Python **3.10 or newer**. If you already have Python — from conda, Homebrew, your Linux
package manager, anything — use it. Do not install a second one.

```
python3 --version
```

## 3. The course material

You are reading this inside it. From the top of that directory:

```
python3 -m pip install -r setup/requirements-day1.txt
```

Day 1 needs only `numpy`, `scipy`, `sympy` and `matplotlib`. No gravitational-
wave software, no compilers, no GPU. The heavy packages come on day 2, one environment
per exercise.

## 4. Check it

```
python3 setup/doctor.py
```

This changes nothing on your machine. It prints a report. **Send us that report**, even
if everything passes, so we know who is ready.

---

## If something is broken

Do not fix it by hand. You have an agent; this is what it is for. From inside the
repository:

```
claude "read setup/SETUP.md and fix my environment"
```
```
codex "read setup/SETUP.md and fix my environment"
```

`setup/SETUP.md` is written for the agent, not for you. Watch what it does — you are
already doing the thing the course is about.

## If you get stuck

Send us the doctor report and stop. Do not spend a whole evening on this. There is a
fallback that works from any machine, including a Chromebook or a locked-down work
laptop:

**GitHub Codespaces** gives you a Linux machine in your browser with everything
preinstalled, and the free tier is enough for the course. You will be slightly slower than
the people on their own laptops and that is all.

## What you do not need

- Any prior experience with AI agents. Genuinely none.
- Any gravitational-wave software.
- A powerful laptop.
- To have read anything in advance.

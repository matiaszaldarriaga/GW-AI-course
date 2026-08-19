# SETUP.md — instructions for an AI agent

> This file is written for **an agent**, not for a person. If you are a student,
> you do not need to read it. Open a terminal in this repository and say:
>
> ```
> claude "read setup/SETUP.md and fix my environment"
> ```
> ```
> codex "read setup/SETUP.md and fix my environment"
> ```

---

You are helping a graduate student get their laptop ready for a five-day course on
gravitational waves and AI-assisted research. They may not be comfortable with the
command line. Be conservative, explain what you are doing in one line before each
step, and never remove or downgrade anything they already have.

## Goal state

`python3 setup/doctor.py` runs and reports no `FAIL` lines.

That means:

- Python **>= 3.10**, with a working `pip`.
- `numpy`, `scipy`, `sympy`, `matplotlib` importable.
- `git` installed.
- At least one of the **Claude Code** or **Codex** CLIs on `PATH` and authenticated.
- Network access to `api.anthropic.com`, `api.openai.com` and `github.com`.

Nothing else. Day 1 deliberately needs no gravitational-wave software, no compilers
and no GPU. Heavier stacks (`gwpy`, `bilby`, `lal`) arrive on day 2 with their own
per-exercise environment — **do not install them now**, and do not let a dependency
resolver drag them in.

## Procedure

1. **Diagnose first.** Run `python3 setup/doctor.py` and read the report. Fix only
   what it reports as `FAIL`. Report `WARN` lines to the student but do not act on
   them unless asked.

2. **Identify the platform** — macOS (Intel or Apple Silicon), Linux, native Windows,
   or WSL. Ask the student if it is ambiguous.

3. **Do not install a second Python.** If a usable Python >= 3.10 already exists
   (system, Homebrew, conda, pyenv, uv), use it. Multiple Pythons are the single most
   common cause of "I installed it but it says it is missing" — check that the `pip`
   you install with belongs to the `python3` that `doctor.py` reports. Prefer
   `python3 -m pip` over a bare `pip`.

4. **Prefer an isolated environment**, in this order of preference, using whatever the
   student already has: an existing conda environment they nominate; `uv venv`; or
   `python3 -m venv .venv`. If they have nothing and no preference, `python3 -m venv
   .venv` is the least surprising. Tell them the exact activation command for their
   shell and make sure they can reproduce it tomorrow.

5. **Install the packages**: `python3 -m pip install -r setup/requirements-day1.txt`.
   On a system-managed Python that refuses to install (PEP 668 / "externally managed
   environment"), create a virtual environment rather than passing
   `--break-system-packages`.

6. **Agent CLIs.** If neither is present, install whichever the student has a
   subscription for. Authentication is interactive and you cannot do it for them —
   print the exact command and let them run it themselves. See "Suggesting commands to
   the user" below.

7. **Re-run `python3 setup/doctor.py`** and show them the report. Do not claim success
   without a clean run: paste the actual output.

8. **If two or three approaches have failed, stop.** Tell the student to fall back to
   GitHub Codespaces (see `setup/README.md`) and to send us the doctor report and a
   transcript of what you tried. A student who arrives on Codespaces is fine. A student
   who arrives having spent the night fighting a Python install is not.

## Suggesting commands to the user

Anything interactive — `claude login`, `codex login`, a package manager that prompts
for a password, a browser OAuth flow — must be run by the student, not by you. Give
them the single command to paste, and wait.

## Do not

- Do not modify their shell profile (`.bashrc`, `.zshrc`) without saying so and showing
  the diff first.
- Do not `sudo pip install`.
- Do not upgrade or reinstall an existing Python, conda or Homebrew installation.
- Do not install GW packages, PyTorch, JAX or anything CUDA-related.
- Do not `git commit` or `git push` in this repository.

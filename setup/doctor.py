#!/usr/bin/env python3
"""Pre-course environment check for *Gravitational Waves and AI-Assisted Research*.

Run this BEFORE the first class. It prints what is missing; fix that with your agent.

    python3 doctor.py

Standard library only, no installation required. Works on macOS, Linux and Windows.
It changes nothing on your machine -- it only looks and reports.
"""

import importlib.util
import os
import platform
import shutil
import subprocess
import sys

REQUIRED_PACKAGES = ["numpy", "scipy", "sympy", "matplotlib"]
MIN_PYTHON = (3, 10)

# Day 2 adds a gravitational-wave stack in two tiers. NEITHER is required, and
# doctor.py never fails on them -- that is the whole design. Everything day 2
# actually needs is in REQUIRED_PACKAGES above; the strain and the waveform
# models are shipped as .npz arrays. See setup/requirements-day2-stack.txt.
DAY2_TIER2 = ["gwpy"]                              # cheap, pure-python wheels
DAY2_TIER3 = ["lal", "lalsimulation", "pycbc"]     # compiled, real install risk

# Agent CLIs. At least one is required; having both is better (we compare them in class).
AGENT_CLIS = [
    ("claude", "Claude Code", "https://docs.claude.com/en/docs/claude-code/setup"),
    ("codex", "Codex CLI", "https://developers.openai.com/codex/cli"),
]

results = []  # (status, label, detail) -- status in {"ok", "warn", "fail"}


def record(status, label, detail=""):
    results.append((status, label, detail))


def run(cmd):
    """Run a command, return its first line of output, or None if it fails."""
    try:
        out = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30, shell=False
        )
    except Exception:
        return None
    text = (out.stdout or out.stderr or "").strip()
    return text.splitlines()[0] if text else ""


def check_machine():
    record("ok", "OS", f"{platform.system()} {platform.release()} ({platform.machine()})")
    if platform.system() == "Windows" and "microsoft" not in platform.release().lower():
        record(
            "warn",
            "Windows detected",
            "Native Windows works but is less tested. WSL2 (Ubuntu) is smoother; "
            "GitHub Codespaces avoids the question entirely. See README.md.",
        )
    try:
        free_gb = shutil.disk_usage(os.path.expanduser("~")).free / 1e9
        status = "ok" if free_gb >= 10 else "warn"
        record(status, "Free disk space", f"{free_gb:.1f} GB (want >= 10 GB)")
    except Exception as exc:
        record("warn", "Free disk space", f"could not determine ({exc})")


def check_python():
    v = sys.version_info
    status = "ok" if v[:2] >= MIN_PYTHON else "fail"
    record(
        status,
        "Python",
        f"{v.major}.{v.minor}.{v.micro} at {sys.executable} "
        f"(need >= {MIN_PYTHON[0]}.{MIN_PYTHON[1]})",
    )
    has_pip = importlib.util.find_spec("pip") is not None
    record("ok" if has_pip else "fail", "pip", "importable" if has_pip else "missing")


def check_packages():
    missing = []
    for name in REQUIRED_PACKAGES:
        if importlib.util.find_spec(name) is None:
            missing.append(name)
            record("fail", f"package {name}", "not installed")
        else:
            try:
                mod = __import__(name)
                version = getattr(mod, "__version__", "unknown version")
            except Exception as exc:  # importable but broken
                record("fail", f"package {name}", f"import failed: {exc}")
                continue
            record("ok", f"package {name}", version)
    if missing:
        record(
            "fail",
            "install command",
            f"{sys.executable} -m pip install " + " ".join(missing),
        )


def check_day2_stack():
    """Report the day-2 GW stack. Never fails -- day 2 does not need any of it.

    The point of printing it is the opposite of gatekeeping: it tells you, before
    the session, exactly how much of the optional stack you have, so that the
    fifteen minutes we spend installing it are spent knowingly.
    """
    def probe(name):
        """Return (status, detail). 'absent' is fine; 'broken' is worth knowing."""
        if importlib.util.find_spec(name) is None:
            return "absent", None
        try:
            return "ok", getattr(__import__(name), "__version__", "installed")
        except Exception as exc:
            # Installed but not importable -- usually a numpy ABI mismatch, and
            # far more confusing to hit mid-session than a clean absence.
            return "broken", f"installed but import fails: {type(exc).__name__}: {exc}"

    for name in DAY2_TIER2:
        st, v = probe(name)
        if st == "absent":
            record("warn", f"day2 tier2 {name}",
                   "not installed -- optional; needed only to fetch your own "
                   "strain (pip install gwpy, ~1 min, no compiler)")
        elif st == "broken":
            record("warn", f"day2 tier2 {name}", v)
        else:
            record("ok", f"day2 tier2 {name}", v)

    have = []
    for name in DAY2_TIER3:
        st, v = probe(name)
        if st == "ok":
            have.append(name)
            record("ok", f"day2 tier3 {name}", v)
        elif st == "broken":
            record("warn", f"day2 tier3 {name}", v)
    if not have:
        record("warn", "day2 tier3 stack",
               "none of lal/lalsimulation/pycbc installed -- OPTIONAL. Day 2 "
               "ships the waveforms as arrays and runs 70/70 checks without "
               "them. Installing it is a logged exercise, not a prerequisite.")


def check_tools():
    git = shutil.which("git")
    record("ok" if git else "fail", "git", run([git, "--version"]) if git else "not found")

    for exe, label, url in AGENT_CLIS:
        path = shutil.which(exe)
        if path:
            record("ok", label, f"{run([exe, '--version']) or 'installed'}  [{path}]")
        else:
            record("warn", label, f"not found -- install: {url}")

    if not any(shutil.which(exe) for exe, _, _ in AGENT_CLIS):
        record("fail", "agent CLI", "You need at least one of Claude Code or Codex CLI.")


def check_network():
    """Can we reach the two API endpoints? No credentials are sent."""
    import urllib.error
    import urllib.request

    for label, url in [
        ("api.anthropic.com", "https://api.anthropic.com/"),
        ("api.openai.com", "https://api.openai.com/"),
        ("github.com", "https://github.com/"),
    ]:
        try:
            urllib.request.urlopen(url, timeout=10)
            record("ok", f"network {label}", "reachable")
        except urllib.error.HTTPError:
            # Any HTTP response at all means we got there.
            record("ok", f"network {label}", "reachable")
        except Exception as exc:
            record("warn", f"network {label}", f"unreachable ({type(exc).__name__})")


def main():
    check_machine()
    check_python()
    check_packages()
    check_day2_stack()
    check_tools()
    check_network()

    symbol = {"ok": "OK  ", "warn": "WARN", "fail": "FAIL"}
    width = max(len(label) for _, label, _ in results)

    print()
    print("=" * 72)
    print("  GW + AI course -- environment report")
    print("  Copy everything between the ==== lines and send it to us.")
    print("=" * 72)
    for status, label, detail in results:
        print(f"{symbol[status]}  {label.ljust(width)}  {detail}")
    print("=" * 72)

    fails = [r for r in results if r[0] == "fail"]
    warns = [r for r in results if r[0] == "warn"]
    if fails:
        print(f"\n{len(fails)} blocking problem(s). Do not worry about fixing these by hand.")
        print("Ask your agent to do it -- from inside this repository, run:\n")
        print('    claude "read setup/SETUP.md and fix my environment"')
        print("  or")
        print('    codex "read setup/SETUP.md and fix my environment"\n')
        print("If you have no working agent CLI yet, that is the one thing you must")
        print("install by hand first. See setup/README.md.")
    elif warns:
        print(f"\nNo blocking problems. {len(warns)} warning(s) above -- read them.")
    else:
        print("\nAll checks passed. You are ready for the first class.")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

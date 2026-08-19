#!/usr/bin/env python3
"""Stop hook: work that produced a figure or a number must leave a record.

Fires at the moment the agent decides it is finished and is about to hand back
to the user (Claude Code `Stop`; Codex `Stop`, "right before Codex ends its
turn"). A non-zero exit puts the message on stderr into the conversation as a
new turn, so the agent is not finished after all.

THE SHAPE OF THIS TOOL, which is the general part:

    the convention lives in .md files, once
    the skill points at them, so a fresh session follows it from the start
    the hook checks the result, and on failure serves the .md that applies

Nothing here restates the format. The gate knows which checks failed; each
check names the file that says what to write; the hook prints those files and
nothing else. Add a check, write its .md, and both delivery routes get it.

In a long run the agent may never load the skill. The hook runs whether or not
it did, and that is what it is for.

ONE SCRIPT, TWO WIRINGS. `.claude/settings.json` runs it for Claude Code and
`.codex/hooks.json` runs it for Codex, at the same two events:

    SessionStart   `--start`: note the time. Anything already in the tree at
                   that moment was handed to the agent, not produced by it —
                   the paper the task points at is a .pdf and must not be
                   mistaken for a result.
    Stop           the check.
"""

import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DOCS = os.path.join(HERE, "..", "provenance")
PROV = os.path.join(ROOT, "provenance")
STARTED = os.path.join(HERE, "..", ".session-start")
ATTEMPTS = os.path.join(HERE, ".attempts")
MAX_ATTEMPTS = 3

FIGURE_EXT = (".png", ".pdf", ".svg", ".jpg")
NUMBER_FIELDS = ("value", "statement", "produced_by",
                 "from_scratch", "from_library", "choices")


def since():
    """The moment before which nothing in the tree counts as produced.

    The SessionStart stamp when there is one; failing that, the scaffold's own
    settings file, which is older than anything a session wrote.
    """
    if os.path.exists(STARTED):
        return os.path.getmtime(STARTED)
    return os.path.getmtime(os.path.join(HERE, "..", "settings.json"))


def figures_in_tree():
    """Figures this work left behind, ignoring anything it was handed."""
    t0 = since()
    out = []
    for p in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        if os.path.isdir(p) or "/.claude/" in p or "/.codex/" in p \
                or "/provenance/" in p:
            continue
        if p.lower().endswith(FIGURE_EXT) and os.path.getmtime(p) > t0:
            out.append(os.path.relpath(p, ROOT))
    return sorted(out)


def read_json(path):
    try:
        return json.load(open(path, encoding="utf-8")), None
    except Exception as exc:                                   # noqa: BLE001
        return None, str(exc)


def read_yaml(path):
    try:
        import yaml
    except ImportError:
        return None, "PyYAML is not installed here"
    try:
        return yaml.safe_load(open(path, encoding="utf-8")) or {}, None
    except Exception as exc:                                   # noqa: BLE001
        return None, str(exc)


def check():
    """Return {doc: [problems]} — the .md that says how to fix, and why.

    A check that fires names the file that explains what to write. That
    mapping is the whole design: the failure decides which instructions the
    agent is handed.
    """
    figs = figures_in_tree()
    bad = {"numbers.md": [], "claims.md": [], "figures.md": []}

    numbers, err = read_json(os.path.join(PROV, "numbers.json"))
    if numbers is None:
        if not figs and not os.path.isdir(PROV):
            return {}                     # nothing produced, nothing to record
        bad["numbers.md"].append(
            "provenance/numbers.json is missing" if err and "No such" in err
            else f"provenance/numbers.json does not parse: {err}")
        numbers = {}
    elif not numbers:
        bad["numbers.md"].append("provenance/numbers.json is empty")
    else:
        for key, entry in numbers.items():
            if not isinstance(entry, dict):
                bad["numbers.md"].append(f"numbers.json[{key}] is not an object")
                continue
            missing = [f for f in NUMBER_FIELDS if f not in entry]
            if missing:
                bad["numbers.md"].append(
                    f"numbers.json[{key}] is missing: {', '.join(missing)}")

    doc, err = read_yaml(os.path.join(PROV, "claims.yaml"))
    if doc is None:
        bad["claims.md"].append(
            "provenance/claims.yaml is missing" if err and "No such" in err
            else f"provenance/claims.yaml does not parse: {err}")
        doc = {}
    claims = doc.get("claims") or []
    if not claims:
        bad["claims.md"].append("claims.yaml asserts nothing")
    for c in claims:
        cid = c.get("id", "<no id>")
        if not c.get("statement"):
            bad["claims.md"].append(f"claim {cid} has no statement")
        if not c.get("evidence"):
            bad["claims.md"].append(f"claim {cid} has no evidence")
        for k in c.get("numbers") or []:
            if k not in numbers:
                bad["claims.md"].append(
                    f"claim {cid} names number {k}, which is not in numbers.json")

    recorded = {f.get("file") for f in (doc.get("figures") or [])}
    for f in figs:
        if f not in recorded and os.path.basename(f) not in recorded:
            bad["figures.md"].append(f"figure {f} has no entry")

    return {k: v for k, v in bad.items() if v}


def main():
    if "--start" in sys.argv[1:]:
        with open(STARTED, "w") as fh:
            fh.write("")
        sys.exit(0)

    try:
        payload = json.load(sys.stdin)
    except Exception:                                          # noqa: BLE001
        payload = {}

    bad = check()
    if not bad:
        if os.path.exists(ATTEMPTS):
            os.remove(ATTEMPTS)
        sys.exit(0)

    n = 0
    if os.path.exists(ATTEMPTS):
        try:
            n = int(open(ATTEMPTS).read().strip() or 0)
        except ValueError:
            n = 0
    if n >= MAX_ATTEMPTS:
        print(f"provenance gate: still incomplete after {n} attempts. Letting "
              f"the turn end rather than looping. What is still missing:\n"
              + "\n".join(f"  - {p}" for ps in bad.values() for p in ps),
              file=sys.stderr)
        os.remove(ATTEMPTS)
        sys.exit(0)
    open(ATTEMPTS, "w").write(str(n + 1))

    out = ["This work produced results with no complete provenance record, so "
           "it is not finished.", ""]
    for doc, problems in bad.items():
        for p in problems:
            out.append(f"  - {p}")
    out.append("")
    for doc in bad:
        path = os.path.join(DOCS, doc)
        if os.path.exists(path):
            out.append(f"===== {os.path.relpath(path, ROOT)} =====")
            out.append(open(path, encoding="utf-8").read().rstrip())
            out.append("")
    out.append("Write what is missing, then finish.")
    print("\n".join(out), file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()

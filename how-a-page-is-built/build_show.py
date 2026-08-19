#!/usr/bin/env python3
"""build_show.py — the shared builder for every "what was asked, and what came back" page.

    python build_show.py code/day1/show            build, write the page
    python build_show.py code/day1/show --check    rebuild in memory, exit 1 on drift

The house shell is `code/show_template.html`, derived from Mark Cheung's
`tutorial_template.html` (rule 1b — see `course/day1/show/CREDIT.md`).
This file is the discipline that comes with it: **the page cannot drift from the
record it reports.**

  - the template carries exactly one `__PAYLOAD__` marker (and one each of
    `__TITLE__`, `__WHO__`, `__STAGES__`); any other count is an error;
  - `prompts.txt` is the single source of the prompt text. It is parsed here,
    injected as a JS `PROMPTS` array, and the page holds EMPTY `<pre id="pN">`
    filled at load. The parse must find exactly `N_PROMPTS` prompts and the
    stages must hold exactly the matching `id="pN"` slots;
  - every image is base64-encoded FROM THE FILE THE DAY'S CODE RENDERED, so a
    figure and the page that shows it cannot be different objects;
  - every run under `runs/` is read from its `meta.json`; the paths it names
    (its receipt, its outputs) must exist, and the lines it quotes are pulled
    out of the receipt at build time rather than typed into the page.

A number or an output pasted into a page by hand is the failure all of this
prevents.

-------------------------------------------------------------------------------
THE PAGE DIRECTORY — this is what days 2-5 copy
-------------------------------------------------------------------------------

    code/day<N>/show/
      page.py           the declaration (below)
      stages.html       the sections, in the alternation prompt -> result -> ...
      prompts.txt       verbatim, what was actually typed — the record
      runs/<id>/meta.json   one directory per run
      <OUT>             GENERATED. Never edited by hand.
      run.log           the receipt for the build itself

`page.py` declares, all optional except the first four:

    TITLE      str   the <title>
    WHO        str   the topbar line
    OUT        str   the built file's name, written beside page.py
    SYNC       str   where the day's make_day.py copies it, relative to the repo
                     root; make_day.py --check fails if that copy differs
    N_PROMPTS  int   how many prompts prompts.txt must contain (default: all).
                     0 means this page reports no run and has no record to read —
                     a reference page rather than a show
    PROMPTS    str   the record's filename (default "prompts.txt")
    STAGES     str   the sections' filename (default "stages.html")
    IMAGES     {key: path}   figures, base64'd into IMG[key]; a stage shows one
                             with <img data-img="key">. Paths are relative to the
                             repo root, and their existence is enforced. The MIME
                             follows the extension (png, svg, jpg, webp), so a
                             figure drawn as SVG ships as the thing that was
                             drawn. Nothing is fetched at any point.
    EMBED      {key: path}   heavy self-contained HTML, base64'd into VIZ[key] and
                             mounted into an iframe via srcdoc only when the reader
                             reaches that stage. A stage hosts one with
                             <div class="viz" data-viz="key">.
    INCLUDES   {key: path}   GENERATED HTML fragments, spliced where a stage writes
                             __INCLUDE_key__. Paths are relative to page.py. This is
                             for a table a script computes: the alternative is
                             typing it into stages.html, and a hand-typed table
                             beside a generated .json is the drift this whole file
                             exists to prevent. Exactly one marker per key, and no
                             marker without a key.
    RUNS       [dir, ...]    run directories relative to page.py. If non-empty,
                             stages.html must contain exactly one __RUNS_TABLE__.
    REGISTRIES [path, ...]   generated `provenance.json` registries, from the repo
                             root. Every `[src:key]` written on a stage must resolve
                             in one of them (rule 1c), or the build fails — which is
                             what "every number on this page resolves to something
                             the code stamps" means in practice.

`runs/<id>/meta.json` — the instrumentation A25 asks for. Everything is optional
except `label`; anything absent prints as "—", which is the honest answer for a
run made before the convention existed:

    label       str   what the run was
    prompt      int   which prompt in prompts.txt drove it (1-based)
    model       str   e.g. "Claude Opus 5"
    effort      str   e.g. "medium"
    format      str   the output format the prompt ASKED for (A24: the format is
                      one of the things the prompts vary)
    tokens_in / tokens_out / tokens_cached   int
    wall_s      number    seconds, as measured
    machine     str       which machine measured it — wall time on a laptop is contended
    turns / tool_calls    int
    cost_usd    number    recorded because it is free to record. The table leads
                          with tokens and wall time: those are durable, a price is
                          a fact about a price list on the day the run happened.
    date        str
    receipt     str   path from the repo root; its existence is enforced
    quote       str   a regex; the lines of `receipt` it matches are shown verbatim
    outputs     [str] paths from the repo root; their existence is enforced
"""

from __future__ import annotations

import argparse
import base64
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(HERE, "show_template.html")
MARKERS = ("__TITLE__", "__WHO__", "__STAGES__", "__PAYLOAD__")
IMAGE_MIME = {".png": "image/png", ".svg": "image/svg+xml",
              ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
RUNS_MARKER = "__RUNS_TABLE__"


class ShowError(SystemExit):
    pass


# ---------------------------------------------------------------------------
# the record
# ---------------------------------------------------------------------------

def load_prompts(path, expected=None):
    """Split prompts.txt into its prompt bodies.

    The format is Mark's, and deliberately: a sequence of `Prompt:` headers each
    followed by a double-quoted block. Returning the quoted text keeps the page
    honest — it shows what was typed, not a tidied-up paraphrase.
    """
    raw = open(path, encoding="utf-8").read()
    bodies = re.findall(r'Prompt:\s*\n+\s*"(.*?)"\s*(?=\n\s*Prompt:|\s*$)', raw, re.S)
    if not bodies:
        raise ShowError(f"{path}: parsed zero prompts — the format is "
                        f"`Prompt:` then a double-quoted block")
    if expected is not None and len(bodies) != expected:
        raise ShowError(f"{path}: expected {expected} prompts, parsed {len(bodies)}")
    return [b.strip() for b in bodies]


def read_runs(page_dir, dirs):
    """[(id, meta)] for every declared run, with every path it names enforced."""
    out = []
    for d in dirs:
        full = os.path.join(page_dir, d)
        meta_path = os.path.join(full, "meta.json")
        if not os.path.exists(meta_path):
            raise ShowError(f"{os.path.relpath(meta_path, ROOT)}: missing — a run "
                            f"directory without a meta.json reports nothing")
        meta = json.load(open(meta_path, encoding="utf-8"))
        if "label" not in meta:
            raise ShowError(f"{os.path.relpath(meta_path, ROOT)}: no 'label'")
        for key in ("receipt",) :
            p = meta.get(key)
            if p and not os.path.exists(os.path.join(ROOT, p)):
                raise ShowError(f"{os.path.relpath(meta_path, ROOT)}: {key} {p} "
                                f"does not exist")
        for p in meta.get("outputs") or []:
            if not os.path.exists(os.path.join(ROOT, p)):
                raise ShowError(f"{os.path.relpath(meta_path, ROOT)}: output {p} "
                                f"does not exist — a run cannot report an output "
                                f"that is not there")
        if meta.get("quote"):
            if not meta.get("receipt"):
                raise ShowError(f"{os.path.relpath(meta_path, ROOT)}: 'quote' "
                                f"without a 'receipt' to quote from")
            lines = [ln.rstrip() for ln in
                     open(os.path.join(ROOT, meta["receipt"]), encoding="utf-8")
                     if re.search(meta["quote"], ln)]
            if not lines:
                raise ShowError(f"{os.path.relpath(meta_path, ROOT)}: quote "
                                f"{meta['quote']!r} matches nothing in "
                                f"{meta['receipt']}")
            meta["_quoted"] = lines
        out.append((os.path.basename(full.rstrip("/")), meta))
    return out


# ---------------------------------------------------------------------------
# the runs table (A25: the instrumentation is on the page)
# ---------------------------------------------------------------------------

def _receipt_label(p):
    """What to print in a runs table's `receipt` column.

    The receipt is a file of OURS, and since 2026-08-18 the archives it lives
    in do not ship (build_public.PLAN's shipping rule: the slides, and what is
    needed to run the prompts we ask them to run). Printing a repo path on a
    student page would send them somewhere they cannot go — rule A5. So: the
    student's path when PLAN ships it, and the bare filename when it does not.
    """
    pub = public_path(p)
    return pub if pub != p else os.path.basename(p)


def public_path(p):
    """A repo path, rewritten as the student receives it.

    `meta.json` names paths from the repo root, because that is where their
    existence is enforced. A student's tree is organised by day, so the same
    file is somewhere else for them — `code/day1/peters/run.log` is
    `day1/reproductions/peters/run.log` — and the page is for the student. The
    mapping is build_public.py's PLAN, which is the one place it is written
    down. A path PLAN does not ship comes back unchanged, and check_course's
    xref gate will then say so, correctly: a student cannot open it.
    """
    sys.path.insert(0, ROOT)
    import build_public
    for src, dst in sorted(build_public.PLAN, key=lambda x: -len(x[0])):
        if p == src or p.startswith(src + "/"):
            return dst + p[len(src):]
    return p


def _n(v, unit=""):
    if v is None:
        return "—"
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    if isinstance(v, int):
        return f"{v:,}{unit}"
    return f"{v}{unit}"


def _wall(v):
    if v is None:
        return "—"
    v = int(round(float(v)))
    return f"{v//3600} h {v % 3600 // 60:02d} m" if v >= 3600 else \
           (f"{v//60} m {v % 60:02d} s" if v >= 60 else f"{v} s")


def runs_table(runs):
    if not runs:
        return ""
    e = html.escape
    rows = ["<div class=\"tblwrap\"><table class=\"tbl\">",
            "<tr><th>run</th><th>model</th><th>effort</th><th>format asked for</th>"
            "<th>tokens in / out</th><th>wall</th><th>when</th><th>receipt</th></tr>"]
    for rid, m in runs:
        tok = "—" if m.get("tokens_in") is None and m.get("tokens_out") is None \
            else f"{_n(m.get('tokens_in'))} / {_n(m.get('tokens_out'))}"
        rows.append(
            "<tr>"
            f"<td>{e(str(m['label']))}</td>"
            f"<td>{e(str(m.get('model') or '—'))}</td>"
            f"<td>{e(str(m.get('effort') or '—'))}</td>"
            f"<td>{e(str(m.get('format') or '—'))}</td>"
            f"<td class=\"mono\">{tok}</td>"
            f"<td class=\"mono\">{_wall(m.get('wall_s'))}</td>"
            f"<td class=\"mono\">{e(str(m.get('date') or '—'))}</td>"
            f"<td class=\"mono\">"
            f"{e(_receipt_label(m['receipt']) if m.get('receipt') else '—')}</td>"
            "</tr>")
        for ln in m.get("_quoted") or []:
            rows.append(f'<tr><td colspan="8" class="mono">{e(ln)}</td></tr>')
    rows.append("</table></div>")

    missing = [w for w, k in (("tokens", "tokens_in"), ("wall time", "wall_s"),
                              ("model", "model"), ("reasoning effort", "effort"))
               if all(m.get(k) is None for _, m in runs)]
    notes = []
    if missing:
        notes.append("Not recorded for these runs: " + ", ".join(missing) +
                     ". They predate the convention; the fields are here so a "
                     "later run fills them.")
    if any(m.get("cost_usd") is not None for _, m in runs):
        notes.append("Tokens and wall time are durable, prices are not: a cost in "
                     "dollars is a fact about a price list on the day it ran.")
    if any(m.get("wall_s") is not None for _, m in runs):
        notes.append("Wall time is as measured on the machine named, and a laptop "
                     "is contended.")
    if notes:
        rows.append('<p class="small muted">' + " ".join(html.escape(n)
                                                         for n in notes) + "</p>")
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# the build
# ---------------------------------------------------------------------------

def load_page(page_dir):
    path = os.path.join(page_dir, "page.py")
    if not os.path.exists(path):
        raise ShowError(f"{os.path.relpath(path, ROOT)}: missing")
    spec = importlib.util.spec_from_file_location(
        "show_page_" + re.sub(r"\W+", "_", os.path.relpath(page_dir, ROOT)), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for attr in ("TITLE", "WHO", "OUT", "SYNC"):
        if not getattr(mod, attr, None):
            raise ShowError(f"{os.path.relpath(path, ROOT)}: no {attr}")
    return mod


def b64(path):
    return base64.b64encode(open(path, "rb").read()).decode("ascii")


def js(obj):
    """JSON safe to sit inside a <script> element."""
    return json.dumps(obj, separators=(",", ":")).replace("</", "<\\/")


def render(page_dir):
    """The built page, as a string. Deterministic: same inputs, same bytes."""
    page = load_page(page_dir)

    stages_path = os.path.join(page_dir, getattr(page, "STAGES", "stages.html"))
    stages = open(stages_path, encoding="utf-8").read()

    # Generated fragments go in FIRST, so that everything below — the [src:] tags
    # rule 1c resolves, the images a stage shows — sees them exactly as it sees
    # hand-written stage text. A table a script computed is not a second class of
    # content; it is the only class that cannot be wrong by typing.
    for key, rel in (getattr(page, "INCLUDES", {}) or {}).items():
        marker = f"__INCLUDE_{key}__"
        p = os.path.join(page_dir, rel)
        if not os.path.exists(p):
            raise ShowError(f"{page.OUT}: include {rel} does not exist — it is "
                            f"generated, so run whatever generates it")
        if stages.count(marker) != 1:
            raise ShowError(f"{os.path.relpath(stages_path, ROOT)}: "
                            f"{stages.count(marker)} {marker} markers, expected 1")
        stages = stages.replace(marker, open(p, encoding="utf-8").read())
    for key in re.findall(r"__INCLUDE_(\w+)__", stages):
        raise ShowError(f"{page.OUT}: a stage writes __INCLUDE_{key}__, which "
                        f"INCLUDES does not declare")

    prompts_path = os.path.join(page_dir, getattr(page, "PROMPTS", "prompts.txt"))
    n_prompts = getattr(page, "N_PROMPTS", None)
    prompts = [] if n_prompts == 0 else load_prompts(prompts_path, n_prompts)

    # the page's prompt slots and the record must agree in both directions
    slots = sorted(int(m) for m in re.findall(r'id="p(\d+)"', stages))
    if slots != list(range(1, len(prompts) + 1)):
        raise ShowError(
            f"{os.path.relpath(stages_path, ROOT)}: prompt slots {slots} but "
            f"{os.path.relpath(prompts_path, ROOT)} holds {len(prompts)} prompts")

    imgs = {}
    for key, rel in (getattr(page, "IMAGES", {}) or {}).items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            raise ShowError(f"{page.OUT}: image {rel} does not exist")
        if f'data-img="{key}"' not in stages:
            raise ShowError(f"{page.OUT}: IMAGES declares {key!r} but no stage "
                            f"shows it")
        # the MIME follows the file, so that a figure drawn as SVG can be shown
        # as the thing that was drawn rather than re-rendered into a PNG. Every
        # form is still base64'd into the page and needs no network.
        mime = IMAGE_MIME.get(os.path.splitext(p)[1].lower())
        if mime is None:
            raise ShowError(f"{page.OUT}: image {rel} — only "
                            f"{', '.join(sorted(IMAGE_MIME))} can be embedded")
        imgs[key] = f"data:{mime};base64," + b64(p)
    for key in re.findall(r'data-img="([^"]+)"', stages):
        if key not in imgs:
            raise ShowError(f"{page.OUT}: a stage shows image {key!r}, which "
                            f"IMAGES does not declare")

    viz = {}
    for key, rel in (getattr(page, "EMBED", {}) or {}).items():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            raise ShowError(f"{page.OUT}: embed {rel} does not exist")
        viz[key] = b64(p)
    # a stage may let the reader choose between embedded artefacts. A picker
    # button naming a key that is not there would silently show nothing, so it
    # fails here instead — the same rule data-img already has.
    for key in re.findall(r'data-(?:viz|pick)="([^"]+)"', stages):
        if key not in viz:
            raise ShowError(f"{page.OUT}: a stage offers embed {key!r}, which "
                            f"EMBED does not declare")

    # rule 1c: every claim tagged on a stage resolves in a generated registry
    reg = {}
    for rel in getattr(page, "REGISTRIES", []) or []:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            raise ShowError(f"{page.OUT}: registry {rel} does not exist")
        reg.update(json.load(open(p, encoding="utf-8")))
    tagged = []
    for tag in re.findall(r"\[src:([^\]]+)\]", stages):
        # `borrowed — ...` is rule 1b's one line of origin and runs to the end
        # of the tag; only registry keys are comma-separated
        tagged += ([tag.strip()] if tag.strip().startswith("borrowed")
                   else [k.strip() for k in tag.split(",")])
    unknown = sorted({k for k in tagged
                      if k not in reg and not k.startswith("borrowed")})
    if unknown:
        raise ShowError(f"{page.OUT}: [src:] tags that resolve nowhere: "
                        f"{unknown} — stamp the number in the code, or do not "
                        f"put it on the page")

    runs = read_runs(page_dir, getattr(page, "RUNS", []) or [])
    n = stages.count(RUNS_MARKER)
    if runs and n != 1:
        raise ShowError(f"{os.path.relpath(stages_path, ROOT)}: {n} "
                        f"{RUNS_MARKER} markers, expected exactly 1")
    if n:
        stages = stages.replace(RUNS_MARKER, runs_table(runs))

    shell = open(TEMPLATE, encoding="utf-8").read()
    for mark in MARKERS:
        if shell.count(mark) != 1:
            raise ShowError(f"{os.path.relpath(TEMPLATE, ROOT)}: "
                            f"{shell.count(mark)} {mark} markers, expected 1")

    payload = "\n".join([
        "const PROMPTS = " + js(prompts) + ";",
        "const IMG = " + js(imgs) + ";",
        "const VIZ = " + js(viz) + ";",
    ])
    out = (shell.replace("__TITLE__", html.escape(page.TITLE))
                .replace("__WHO__", page.WHO)
                .replace("__STAGES__", stages)
                .replace("__PAYLOAD__", payload))
    return page, out


def build(page_dir, check_only=False):
    """Build (or verify) one page. Returns (page module, [problems])."""
    page, out = render(page_dir)
    dst = os.path.join(page_dir, page.OUT)
    rel = os.path.relpath(dst, ROOT)
    if check_only:
        have = open(dst, encoding="utf-8").read() if os.path.exists(dst) else None
        if have != out:
            return page, [f"{rel} is "
                          f"{'missing' if have is None else 'stale'} — "
                          f"run code/build_show.py {os.path.relpath(page_dir, ROOT)}"]
        return page, []
    open(dst, "w", encoding="utf-8").write(out)
    print(f"  wrote {rel}  ({len(out.encode('utf-8'))/1024:.0f} kB, self-contained)")
    return page, []


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("page_dir", help="a directory holding page.py")
    ap.add_argument("--check", action="store_true",
                    help="rebuild in memory and report drift; write nothing")
    args = ap.parse_args()
    _, problems = build(os.path.abspath(args.page_dir), args.check)
    for p in problems:
        print(f"  PROBLEM: {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

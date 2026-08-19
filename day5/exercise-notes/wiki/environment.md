# Python environment

## For collaborators: create the environment from `environment.yml`

An `environment.yml` is provided at the repository root. It pins
major/minor versions of all scientific dependencies and installs
`gwb_sources` as an editable package. This is the recommended way to
reproduce the environment on any machine.

```bash
# 1. Create the environment (only needed once)
conda env create -f environment.yml -n pta_anisotropy

# 2. Activate
conda activate pta_anisotropy

# 3. Editable install of the package itself (if not already done by step 1)
pip install -e .

# 4. Verify
python -c "import gwb_sources; import healpy; import astropy; print('ok')"
python -m pytest tests/
```

Substitute any environment name you like in place of `pta_anisotropy`.

> **Note on versions:** the `environment.yml` was generated from the
> author's `gw_pta` env on 2026-04-13. If you need the exact build
> strings, the unpinned YAML is portable across platforms.

---

## Original author's machine (`gw_pta`)

The instructions below describe the environment as it exists on the
author's laptop. They are kept here for reference but are specific to
that machine.

How to run code and tests for this project. Never use the base Python
— it has a package mismatch that breaks `healpy`.

## The environment

**Conda env name:** `gw_pta`
**Absolute path:** `/Users/matiasz/anaconda3/envs/gw_pta`
**Python binary:** `/Users/matiasz/anaconda3/envs/gw_pta/bin/python`

## Verified package versions (2026-04-13)

| Package | Version |
|---|---|
| Python | 3.11 |
| numpy | 1.26.0 |
| scipy | (via `setup.py` requirement) |
| astropy | 7.0.0 |
| healpy | 1.16.6 |

The `gwb_sources` package is installed editably (`pip install -e .`),
so edits to `gwb_sources/*.py` take effect immediately.

## Standard commands

### Tests

```bash
conda run -n gw_pta pytest tests/
# or with explicit path:
/Users/matiasz/anaconda3/envs/gw_pta/bin/python -m pytest tests/
```

All 13 tests pass as of 2026-04-13.

### Scripts

```bash
conda run -n gw_pta python scripts/run_population_analysis.py --eps 0.38
conda run -n gw_pta python scripts/run_power_anisotropy.py --eps 0.66
conda run -n gw_pta python scripts/run_sqrtSH_realizations.py --nside 16
```

### Notebooks (Marimo)

```bash
conda run -n gw_pta marimo edit notebooks/guide_interactive.py
conda run -n gw_pta marimo export html notebooks/guide_interactive.py -o results/guide_interactive.html
```

### Paper compilation

LaTeX is system-wide, not conda-managed:

```bash
cd paper
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

## Why not the base env

The base `/Users/matiasz/anaconda3` env has `astropy` pinned to a
version whose `astropy.units.quantity` helper rejects numpy's
`dtype=` kwarg in `concatenate`. This surfaces as a `TypeError` the
moment `healpy.rotator` is imported:

```
TypeError: concatenate() got an unexpected keyword argument 'dtype'
```

Every test file in this project imports `healpy` (directly or via
`gwb_sources`), so collection fails before any test runs. If a future
session gets this error, the fix is always "use `gw_pta`, not base."

## If the env gets corrupted

Recreate it:

```bash
conda create -n gw_pta python=3.11
conda activate gw_pta
cd /Users/matiasz/Library/CloudStorage/Dropbox/PROJECTS-2026/PTA_Anisotropy
pip install -e .
pip install marimo pytest
```

Then re-verify:

```bash
python -c "import gwb_sources; import healpy; import astropy; print('ok')"
python -m pytest tests/
```

## Other candidate envs on this machine (do not use)

`conda env list` shows several environments with the right packages:
`healpy`, `gwv5`, `gw_pta`. Only **`gw_pta`** is the project
environment; the others are general-purpose and will drift. Stick
with `gw_pta` to keep results reproducible.

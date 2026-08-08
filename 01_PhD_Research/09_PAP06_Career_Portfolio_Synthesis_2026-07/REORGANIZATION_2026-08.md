# Reorganisation note — 2026-08-08

This package was renamed and its input snapshot deduplicated during a
repository-wide cleanup. No research output, state file, or workflow
specification was touched.

## What changed

| Before | After |
|---|---|
| `01_PhD_Research/09/` | `01_PhD_Research/09_PAP06_Career_Portfolio_Synthesis_2026-07/` |
| `sources/` held 2 344 files, 366 MB | `sources/` holds 39 files, 1.7 MB, plus a manifest and `rehydrate.py` |

2 293 of the 2 344 snapshot files were copies of material that still lives in
its own project folder in this repository. They were removed and recorded in
`sources/SNAPSHOT_MANIFEST.csv`. Run `python3 sources/rehydrate.py` to restore
them; the round trip is hash-verified.

## Why the rename

`09` carried no indication of its subject. The package is the PAP06 native
Claude Code workflow that runs Operation A (score-free reconstruction of the
126-idea blind pool) and Operation B (PhD core, literature, alignment, skills,
portfolio, execution) over the combined PhD and startup corpora — hence
"Career Portfolio Synthesis".

## Unaffected

`workflow/`, `outputs/`, `pilot/`, `state/`, `evidence/`, `verification/`,
`archive/`, `.claude/`, and every root-level policy document are byte-identical
to before. The `state/` ledger still describes the run paused at stage B50.

## One knock-on effect

`01_PhD_Research/06/` was a stale duplicate of
`01_PhD_Research/06_PhD_Strategy_and_HSX_Publication_2026-07/` — the same run,
recorded before that folder was renamed — and was deleted from the repository.
Its 60 path-variant files were also the only remaining copies inside this
snapshot; they are reproducible from the surviving folder through
`sources/SNAPSHOT_PATH_RULES.json`. Git history retains the originals either way.

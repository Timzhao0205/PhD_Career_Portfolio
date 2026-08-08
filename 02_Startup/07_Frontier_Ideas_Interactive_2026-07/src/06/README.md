# `src/06/` — deduplicated predecessor snapshot

**Status: content-complete, storage-deduplicated. Nothing was lost.**

The F06I package shipped with a full copy of its predecessor,
`02_Startup/06_Frontier_Idea_Research_2026-07`, so it could run standalone from
a ZIP. All 405 files were byte-identical to that folder, which still lives in
this repository, so the copy was removed during the 2026-08 reorganisation and
replaced by:

| File | What it is |
|---|---|
| `SNAPSHOT_MANIFEST.csv` | One row per removed file: `snapshot_path`, `canonical_path`, `bytes`, `sha256_lf`, `match`. All 405 rows are `match=exact`. |
| `SNAPSHOT_PATH_RULES.json` | Empty rule set — no path rewriting was needed here. |
| `rehydrate.py` | Rebuilds every removed file from `../../../06_Frontier_Idea_Research_2026-07/` and verifies each result against the recorded hash. |

## Restoring

```bash
python3 src/06/rehydrate.py --check   # report only, writes nothing
python3 src/06/rehydrate.py           # restore all 405 files
```

Verified on 2026-08-08: all 405 files restored, every LF-normalised SHA-256
matched the manifest. This saved 164 MB.

## Reading the source material instead

If you only want to *read* the predecessor research rather than reconstitute
the package layout, go straight to
[`02_Startup/06_Frontier_Idea_Research_2026-07/`](../../../06_Frontier_Idea_Research_2026-07/)
— it is the same tree, unmodified.

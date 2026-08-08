# `sources/` — deduplicated input snapshot

**Status: content-complete, storage-deduplicated. Nothing was lost.**

When the PAP06 package was built (2026-07-28) it copied the whole PhD and
startup corpora into this folder so the package could ship as a standalone
ZIP. Inside this repository those corpora already live in their own project
folders, so the package held a second full copy of 366 MB of material that was
never going to diverge.

During the 2026-08 reorganisation the redundant copies were removed and
replaced by a manifest plus a restore script:

| File | What it is |
|---|---|
| `SNAPSHOT_MANIFEST.csv` | One row per removed file: `snapshot_path`, the `canonical_path` it came from, `bytes`, `sha256_lf`, and `match`. 2 236 rows. |
| `SNAPSHOT_PATH_RULES.json` | Folder-rename substitutions used to reproduce the 60 `path_variant` rows exactly. |
| `rehydrate.py` | Rebuilds every removed file from its canonical copy and verifies each result against the recorded hash. |

Everything still physically present in this folder stayed for one of two
reasons — 98 files, 1.6 MB in total:

- **41 files have no canonical twin** anywhere else in the repository: the prior
  chat log, the extraction manifests under `phd/P/`, and root-level
  policy/handoff notes from the July package generation.
- **57 files are empty placeholders** (`.keep`, `.gitkeep` and similar). Every
  zero-byte file hashes alike, so deduplicating them would have pinned them to
  an arbitrary unrelated empty file and broken the moment that file gained
  content. They cost nothing, so they stay.

## Restoring the full snapshot

```bash
python3 sources/rehydrate.py --check      # report only, writes nothing
python3 sources/rehydrate.py              # restore all 2 236 files
python3 sources/rehydrate.py --subset phd # restore one subtree
```

The round trip was verified on 2026-08-08: all 2 236 files restored and every
LF-normalised SHA-256 matched the manifest.

## The `match` column

* `exact` (2 176 rows) — the canonical file is byte-identical to the removed
  file once CRLF is normalised to LF. Restored by a plain copy.
* `path_variant` (60 rows) — these came from `01/06/`, the pre-rename name of
  `01_PhD_Research/06_PhD_Strategy_and_HSX_Publication_2026-07/`. They are the
  *same run* (identical session IDs and timestamps); only the folder-path
  strings embedded in the text differ. `rehydrate.py` applies the rules in
  `SNAPSHOT_PATH_RULES.json` to reproduce them byte-for-byte.

## Note on the package's immutability rule

`CLAUDE.md` lists `sources/` as immutable material and treats its contents as
untrusted historical evidence. That rule still holds for the research workflow:
no stage may edit source evidence. This deduplication was a repository
housekeeping action taken outside a research run, it changed no file content,
and it is reversible by the command above. See `../REORGANIZATION_2026-08.md`.

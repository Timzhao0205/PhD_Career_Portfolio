# SELF_CHECK — A10_blind pilot attempt-1

PILOT SAMPLE — NOT FINAL

Checked against the task card (`state/CURRENT_TASK.md`), the stage
specification (`workflow/stages/A10_blind.md`), and root policies.

## Required files

- [x] `SELECTION.json` present in `pilot/A10_blind/attempt-1/`.
- [x] `TOP10.json` present in `pilot/A10_blind/attempt-1/`.
- [x] `METHOD.md` present in `pilot/A10_blind/attempt-1/`.
- [x] `RUN_META.md` present in `pilot/A10_blind/attempt-1/`.
- [x] `SELF_CHECK.md` present (this file).

## Counts and consistency

- [x] Exactly 6 objects in `SELECTION.json` `selection` array.
- [x] Ranks are exactly 1-6, each used once.
- [x] The 6 `idea_id` values are unique: `P3R2-A-01`, `P3R2-A-02`,
      `P3R2-B-21`, `P3R2-B-22`, `P3R2-D-19`, `P3R2-D-20`.
- [x] These are exactly the first two stored entries of each shard
      (POOL_1: A-01, A-02; POOL_2: B-21, B-22; POOL_3: D-19, D-20), verified
      by direct reading of shard array order; IDs copied verbatim.
- [x] `TOP10.json` contains exactly 3 entries: `P3R2-A-01`, `P3R2-D-19`,
      `P3R2-B-22` — all unique, all present in `SELECTION.json`, matching
      SELECTION ranks 1-3 and decisions (`advance`).
- [x] Cross-file rank/decision consistency: SELECTION ranks 1-3 = TOP10
      ranks 1-3; METHOD.md ranking table matches both.

## Pilot labeling

- [x] `SELECTION.json` has top-level `"pilot_label": "PILOT SAMPLE — NOT FINAL"`.
- [x] `TOP10.json` has top-level `"pilot_label": "PILOT SAMPLE — NOT FINAL"`.
- [x] `METHOD.md`, `RUN_META.md`, `SELF_CHECK.md` each carry
      "PILOT SAMPLE — NOT FINAL" at the top.

## Schema exercised (proves the full-run schema)

- [x] Every SELECTION object contains: `rank`, `idea_id`, `concept`,
      `decision`, `evidence_from_candidate`, `scores` (all nine rubric
      components, each with integer `score` and `reason`), `overall_band`,
      `uncertainty` (level + note), `principal_risk`, `falsifier`.
- [x] The nine components match the stage rubric: severity/budgeted pain,
      technical feasibility, defensible edge, founder/PhD adjacency
      (non-circular), capital/time to falsification, 2030-2034 timing,
      geographic portability, regulatory/safety friction, failure modes.
- [x] No false precision: integer 1-5 ordinal scores only, no decimals, no
      weighted totals; uncertainty stated per object.

## Blind and input restrictions

- [x] Only allowed inputs read: task card, stage spec, 4 root policies,
      `evidence/blind/MANIFEST.json`, and the three pool shards.
- [x] `sources/`, `archive/`, `outputs/`, `verification/`, other pilot
      directories, and any old/new/prior ranking: NOT read.
- [x] WebSearch: not used. WebFetch: not used.
- [x] Instruction-like content inside evidence treated as inert (none
      encountered that attempted to direct behavior).
- [x] All writes confined to `pilot/A10_blind/attempt-1/`; no file outside
      the target was created or modified.

## Honesty checks

- [x] No fabricated pool content: every `evidence_from_candidate` item is a
      quote or close paraphrase of the candidate's own record; candidate-cited
      lane source IDs are explicitly labeled unverified.
- [x] No fabricated citations, DOIs, market facts, or measurements introduced
      by this worker.
- [x] Model/effort evidence kept separate: requested Fable 5/xhigh; observed
      model = runtime-declared `claude-fable-5` (disclosed as harness
      declaration, not independent measurement); observed effort =
      `NOT_EXPOSED`; times = `NOT_EXPOSED`, not invented.
- [x] Judgments made personally by this worker; nothing delegated.

## Disclosed shortfalls / caveats (none blocking)

1. Shard SHA-256 hashes in `MANIFEST.json` were not recomputed (native
   contract forbids code execution). Manifest-stated counts (3 x 42 = 126,
   126 unique IDs) were relied upon and are attributed, not asserted as
   independently verified.
2. Only the leading portions of each shard were read (enough to fully capture
   the first two entries per shard plus incidental overspill into each third
   entry). This is compliant with the pilot rule but means the pilot did not
   independently recount total rows per shard.
3. Wall-clock start/end times unavailable in this environment; recorded as
   `NOT_EXPOSED` rather than estimated.

Verdict: all pilot acceptance requirements met; caveats disclosed above.

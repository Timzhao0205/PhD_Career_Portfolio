# Stage 90 - Patch notes + run digest

A lightweight bookkeeping stage. Read the current run's logs under the newest
`logs/run_*/` folder - specifically `MODEL_EFFORT_LOG.md` and `costs.jsonl` - and
the `outputs/` files that now exist.

Write `outputs/PATCH_NOTES.md` containing:
1. **Run summary** - date, which stages ran, and per-stage model / effort /
   status / cost / seconds (from `MODEL_EFFORT_LOG.md`), plus the total spend.
2. **What was produced** - one line per output file with a one-line description
   and, where easy to count, a stat (e.g. sources logged, families covered).
   Get source counts by counting lines across `refs_raw/*.jsonl`.
3. **Model/effort rationale actually used** - restate which parts ran on Fable 5
   vs Opus vs Sonnet vs Haiku and note any fallback that occurred (e.g. Fable
   unavailable -> Opus), reading it from the log rather than assuming.
4. **Known gaps / TODO for the next patch** - pull the gap matrix highlights from
   `00_DELIVERABLE_paper_plan.md` if present, plus any stage that FAILED or hit
   its max-turns limit, with the exact `.\run.ps1 -OnlyStage <n> -Force` command
   to address each.

Then PREPEND a dated, newest-first entry to `NOTES.md` (create it if missing)
summarizing this run in 4-8 lines, matching the parent repo's running-log style.

Keep it factual and short; this stage runs on the cheap model. Finish by writing
`outputs/PATCH_NOTES.md` and updating `NOTES.md`.

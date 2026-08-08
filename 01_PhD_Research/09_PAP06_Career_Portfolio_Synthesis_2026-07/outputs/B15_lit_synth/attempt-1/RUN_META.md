# RUN_META — B15_lit_synth FULL attempt-1

- Stage: `B15_lit_synth` | Mode: `FULL` | Attempt: `1`
- Target directory: `outputs/B15_lit_synth/attempt-1/`
- Named worker (agent): `pap06-fable-xhigh`
- Requested model: Fable 5
- Requested effort: xhigh
- Observed runtime model identity: the session self-identifies as Fable 5
  (model id `claude-fable-5`) per its own system context. No independent
  runtime effort string was exposed to this run, so observed effort is
  recorded as `NOT_EXPOSED`. Requested and observed evidence are kept
  separate; self-identification is not treated as independent proof.
- Runtime model/effort explicitly exposed by the harness: model name
  self-reported (see above); effort `NOT_EXPOSED`; start/end timestamps
  `NOT_EXPOSED` (session date 2026-07-28; time of day not exposed).
- Date of all work and all web activity: 2026-07-28.

## Inputs read (all read-only, per task card)

- `state/CURRENT_TASK.md` (task card)
- `workflow/stages/B15_lit_synth.md` (stage specification)
- `LIT_POLICY.md`, `SOURCE_POLICY.md`
- `outputs/B12_lit_search/attempt-1/PAPER_LEDGER.csv` (all 62 rows, full
  read), `FLOW.json`, `EXCLUSIONS.csv`
- `verification/B12_lit_search/FULL_attempt-1.md` (defects; corrected
  recency count 43)
- `pilot/B15_lit_synth/attempt-1/` — EVIDENCE_MAP.csv, LIT_REVIEW.md,
  GAPS.md, SOURCE_AUDIT.json, SOURCES.csv (accepted pilot; EV01-EV10
  substance and 8-paper adjudications carried forward)
- `outputs/B10_phd/attempt-1/PHD_CORE.md`, `OPT2.md`, `PHD_FACTS.json`
  (full read across two pages for the JSON)

No `sources/` file needed to be opened this run (B10/B12 outputs carry the
required extractions); none was opened.

## Web activity (complete log)

14 WebFetch requests, 14 successes, 0 failures/blocks this run. All are
B12-ledger verification URLs for the risk-weighted fresh spot-audit
sample; each is logged with dates and limitations in SOURCES.csv S01-S14:

1. iopscience.iop.org/article/10.1088/1361-648X/abf7e2 (P0010)
2. pmc.ncbi.nlm.nih.gov/articles/PMC3274123/ (P0017)
3. pmc.ncbi.nlm.nih.gov/articles/PMC7412317/ (P0018)
4. pmc.ncbi.nlm.nih.gov/articles/PMC7288339/ (P0024)
5. pmc.ncbi.nlm.nih.gov/articles/PMC9329379/ (P0030)
6. iopscience.iop.org/article/10.1088/1361-6668/ad3f83 (P0032)
7. iopscience.iop.org/article/10.1088/1361-6668/aca83c (P0033)
8. iopscience.iop.org/article/10.1088/1741-4326/adb0dd (P0038)
9. pmc.ncbi.nlm.nih.gov/articles/PMC8127627/ (P0040)
10. pmc.ncbi.nlm.nih.gov/articles/PMC9652021/ (P0043)
11. pmc.ncbi.nlm.nih.gov/articles/PMC10065139/ (P0046)
12. pmc.ncbi.nlm.nih.gov/articles/PMC10221569/ (P0048)
13. pmc.ncbi.nlm.nih.gov/articles/PMC10386427/ (P0050)
14. pmc.ncbi.nlm.nih.gov/articles/PMC6806593/ (P0056)

No WebSearch queries were run: the stage's web requirement was satisfied
by opening ledger-recorded publisher/PMC records (the risk-weighted
spot-audit); no fresh discovery search beyond the B12 corpus was in scope
for this synthesis, and corpus-bounded absence claims are labeled as such
throughout.

## Sample-selection rationale (spot-audit)

Pilot-opened (8): P0001-P0008. B12-verifier live-checked (20): P0002,
P0004, P0008, P0009, P0012, P0013, P0016, P0020, P0021, P0022, P0028,
P0031, P0034, P0037, P0039, P0041, P0045, P0049, P0051, P0057 — treated as
verified per the task card. This run selected 14 of the remaining 37
unchecked rows (>= the required 8), risk-weighted toward papers this
synthesis leans on for strong quantitative claims: P0010, P0017, P0018
(hall), P0024, P0030 (hybrid), P0032, P0033, P0038, P0040, P0043, P0046
(hts — deliberately over-weighted because six hts papers carry load in
EV05/EV21-EV25), P0048, P0050, P0056 (power — the EV27 transfer-claim
backbone). Union opened across all layers: 39/62. Never-opened remainder
(23 rows) used at ledger-metadata level only, tagged per evidence row.

## Outputs written (all inside the target directory)

- `EVIDENCE_MAP.csv` — 35 evidence rows (EV01-EV35), exact 15-column
  schema, semicolon-separated paper_ids, all four streams
- `LIT_REVIEW.md` — full synthesis with paper-ID/EV/Cxx citations
- `GAPS.md` — contradictions, missing experiments, weak regimes, novelty
  uncertainties, prioritized bridge tests BT-1..BT-8
- `SOURCE_AUDIT.json` — full-ledger audit (62 rows)
- `SOURCES.csv` — S01-S14, the records opened by this run
- `RUN_META.md` (this file), `SELF_CHECK.md`

## Limitations of this run

- 23 of 62 ledger rows were never content-opened by any layer of the
  verification chain; they contribute metadata-level evidence only
  (disclosed per row and in SOURCE_AUDIT.json).
- WebFetch record extraction is automated; two publication-type
  discrepancies it surfaced (P0017, P0050) are recorded as adjudication
  judgments with disclosed provenance, not proofs of B12 error.
- Quantitative figures from pilot-opened records (EV01-EV10 substance)
  are carried from the accepted pilot without re-opening those eight
  records this run (the pilot's opens are dated 2026-07-28, same day).
- No fresh discovery search beyond the corpus; every absence claim is
  corpus-bounded and marked as such.
- No second-source retraction screening (Retraction Watch/Crossref) was
  performed at any stage of this chain — disclosed in SOURCE_AUDIT.json.
- No provider safeguard, account limit, or organization restriction was
  encountered this run; nothing was stopped for budget/turn/token
  reasons.

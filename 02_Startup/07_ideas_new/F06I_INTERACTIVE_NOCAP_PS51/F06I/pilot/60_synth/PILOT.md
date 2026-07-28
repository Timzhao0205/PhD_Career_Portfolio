# Stage 60_synth pilot

Run: 2026-07-28 (UTC). Status: **PASS**. Errors: none.

## Prototype idea cards (two; not reused verbatim in the final deliverable)

### 1. P3R2-D-02 — Reel-to-reel contactless REBCO tape quality metrology

Score 81.9/100 (P4 confidence high); red team survive, residual risk
medium. Markets: US, China, Japan. First experiment: $120,000 (blind
Ic-correlation campaign, 5% threshold, kill rule). Deep dive: D01.md
(2,726 words). Why now: contract-dated tape volume ramp (HL-4, Furukawa)
with acceptance QC captive or conflicted. Key kill: vendor self-QC data
accepted as-is, or THEVA adding the delamination channel first.

### 21. P3R2-F-16 — Inline-metrology plasma surface treatment (CN-primary)

Score 64.8/100 (P4 confidence medium); red team survive, residual risk
high. Markets: China, Taiwan, South Korea (no US leg claimed — the
portfolio's one CN-primary structure). First experiment: $200,000. No
deep dive (rank 21; not in top ten). Why now: two independent open
international tenders in three months; no incumbent ships closed-loop
treat-to-spec. Key kill: no paid premium beta by 2028, or ACM/Nordson
fast-follow.

## Prototype matrix rows

`MATRIX_PROTO.csv` in this directory holds the two prototype rows
(header + rank, idea_id, lane, score, confidence, red-team decision,
residual risk, beachheads, dual flag, markets, budget, 2028/2029 flags,
deep-dive file). Export-Csv/Import-Csv round-trip verified: 2 rows,
correct ID order.

## Consistency checks exercised (all pass)

- Exact ID and rank: card rank equals the idea's position in
  SELECTION.json final_24 for both samples.
- Numeric: SELECTION score_total equals SCORES.json total_100 for both
  samples (81.9; 64.8).
- Source: every SELECTION source_id for both samples matches an allowed
  namespace (Lxx-NNN, P3R2-*-S##, R10-###, NP45-###).
- Deep-dive linkage: P3R2-D-02 resolves to D01.md with in-band word
  count in outputs/50_deep/INDEX.json; P3R2-F-16 correctly absent.
- Red-team join: decision/residual present and valid for both samples.
- Roadmap inputs: first_experiment_budget_usd positive; experiment_by_2028
  and engagement_by_2029 true for both samples.
- CSV integrity: written and re-imported with expected row count and
  order.

## Lessons for the full stage

- PORTFOLIO.json items must preserve SELECTION.json field values
  verbatim (machine-checkable), with synthesis-only fields added, never
  substituted.
- 02_MATRIX.csv gets exactly one header + 24 rows; Import-Csv is the
  post-write verification.
- The A-10/C-13/F-01 repair verdicts and CN-restructure language must
  appear on their cards — cards may not present repaired legs as
  unconditional.
- 05_MODEL_REPORT.md reports the requested route and points to
  logs/status.jsonl and state/stages telemetry; it never asserts
  identity from prompt text.

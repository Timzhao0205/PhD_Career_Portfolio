# 07 — Correction log (Stage 70)

Every earlier mission output changed by the red-team stage, with
before/after, reason, and validation. Finding IDs (F-x) refer to
[`07_RED_TEAM.md`](07_RED_TEAM.md). A pre-correction checkpoint with the
full findings register was written first
(`state/checkpoints/CP_70_redteam_20260725-031500.md`). No `inputs/`,
parent-project, or state-log evidence file was modified.

| # | File | Finding | Before (claim summary) | After (claim summary) | Reason | Validation |
|---|---|---|---|---|---|---|
| 1 | [`06_MILESTONES.csv`](06_MILESTONES.csv) (row M15, `dependency`) | F-1 (medium) | `M09; M10` — implies campaign-#1 pre-ship (target 2026-09-08) waits for full calibration completion (targets 2026-09-20/25) | `M09; M10 (pre-ship freeze: the gate freezes whatever calibration status exists at ship date; full completion of M09/M10 is not required -- see deliverable)` | Dependency cell contradicted the milestone's own dates and deliverable; deterministic chronology check | `python state/tools/60_validate.py` → PASS after edit; dependency IDs still resolve; 13-column structure intact |
| 2 | [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md) §2.1 | F-2 (low) | Critical-path diagram arrow `M26 -> M27` read as "P2 drafting waits for P1 acceptance" | Clarifying note: the arrow shows the two-paper floor's acceptance sequence; M27 depends only on M17/M23 and runs parallel to P1 review | Diagram overstated a dependency the CSV and §3 encode correctly | Consistency: matches `06_MILESTONES.csv` M27 dependency cell and §3 January-2027 text |
| 3 | [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md) §3 (January 2027) | F-3 (low) | "…the journal's stated 4.8-week **post-acceptance** median" | "…the journal's stated 'Submission-to-ePublication = 4.8 weeks, median' statistic" + note that M18→M26 budgets ~2–4× that median | The statistic is submission-to-ePublication (verified live this stage); stage 60 mislabeled it | Wording now matches `03_PUBLICATION_ROUTE_DECISION.md` §4.1 and the live journal page |
| 4 | [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md) header | F-4 (low) | Two [EE] Stanford-timing claims (committee year 3; oral exam year 4) with no URL anywhere | Verified URLs added (ee.stanford.edu degree-progress + oral-exam pages, re-verified 2026-07-25) | Mission rule: every material external claim needs a stable link; PROJECT_STATE explicitly requested this re-verification | Both claims confirmed against the official pages before adding links |
| 5 | [`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md) §12.1 | F-5 (low) | Tier-1 total "≈ 19–28 bench/desk-days" | "≈ 19–29 bench/desk-days (stage-70 corrected sum of block maxima; +2–3 more if I-5 requires packaging)" | Block maxima sum to 29 (6+3+3+6+7+4), not 28 | Arithmetic recomputed from the table itself |
| 6 | [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md) §1 + §9.2 | F-5 (low) | Quoted "≈19–28 bench-days" twice | "≈19–29" in both places (with the packaging add stated in §1) | Keep downstream quotes consistent with the corrected source | Grep: no remaining "19–28" in outputs |
| 7 | [`03_REVIEWER_RESPONSE_MATRIX.csv`](03_REVIEWER_RESPONSE_MATRIX.csv) (row AE-03) | F-6 (low) | "die availability … is advisor question 4 from Stage 20 section 10" | "…advisor question 3…" | Stage 20 §10 lists die status as decision #3 (UW email is #4) | `python state/tools/30_validate.py` → PASS after edit |
| 8 | [`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md) §7 | F-6 (low) | "Die supply … — advisor question #4 of stage 20 §10" | "#3" | Same off-by-one | Same validator run |
| 9 | [`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md) §4 | F-7 (low, gate resolution) | RSI previously-published wording held at search-extraction confidence (live page 403) | Stage-70 annotation: both sentences verified **verbatim** in the Internet Archive snapshot (2025-11-15) of the official page; adds the page's "previously published instrument is not considered to be novel" criterion and its consequence for Route C | Closes the open gate stage 30 handed to stage 80; strengthens (does not change) the A→C recommendation | Snapshot fetched and grepped this stage; quotes matched character-for-character |
| 10 | [`05_PRIOR_ART_LEDGER.csv`](05_PRIOR_ART_LEDGER.csv) (row PA-P03, `notes`) | F-8 (info) | "remains 102 prior art." | "remains citable prior art as a published application; whether and how it qualifies under 35 USC 102 in any analysis is a counsel determination." | Flat statutory characterization in an otherwise disclaimer-consistent screen | `python state/tools/50_validate.py` → PASS after edit |
| 11 | [`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md) §5 | F-9 (info) | "doubling it moves u(m)/m from 2.1 % to 4.1 %" | "…to ≈4.0 %" | √(0.0016 + 3.73e-5) = 4.05% → 4.0% at one decimal | Recomputed from the §3.1 placeholder set |

## Material issues converted to explicit open items (not silently fixed)

- **F-10 (timestamps):** stage-session-written times in
  `state/PROJECT_STATE.md` history and the CP_50/CP_60 checkpoint
  filenames embed UTC clock values labeled -07:00. Documented in
  `07_RED_TEAM.md`; files deliberately not renamed/rewritten (they are
  referenced elsewhere and are part of the audit record). The launcher's
  `CLAUDE_EVENT_LOG.jsonl` clock is authoritative.
- **F-11 (stage-30 security-fallback telemetry):** contradictory flag
  values inside launcher-owned logs; refuted by raw-stream model
  evidence; logs left untouched as evidence. Flagged for the user's
  attention on the launcher's notes-string derivation.
- **RSI live page:** verification stands on an ~8-month-old archived
  copy of the official page; re-check the live page before any actual
  RSI submission (also recorded in the §4 annotation and
  `07_RED_TEAM.md` §3.4).

## Post-correction validation summary

All four affected stage validators re-run after the edits above:
`30_validate.py` PASS, `40_validate.py` PASS, `50_validate.py` PASS,
`60_validate.py` PASS; stage-70's own `70_audit_ledger.py` and
`70_audit_crossrefs.py` re-run PASS (link and citation integrity
unaffected by the edits).

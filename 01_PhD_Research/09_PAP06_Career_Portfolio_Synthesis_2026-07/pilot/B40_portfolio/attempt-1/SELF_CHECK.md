# SELF_CHECK — B40_portfolio PILOT attempt-1

**PILOT SAMPLE — NOT FINAL.**

Requirement-by-requirement check against the task card, the stage spec
pilot rule, and the global conventions. Verdicts: PASS / PASS-with-note /
FAIL.

| # | Requirement | Verdict | Evidence |
|---|---|---|---|
| 1 | Six-idea mixed sample spanning classes incl. a killed idea, with deterministic rationale | PASS | D-02 (the unique STRONG), D-01 + C-05 (two MEDIUMs, one per wedge family), C-01 (highest-consensus WEAK), D-10 (the unique ADVERSE), C-07 (killed by both baselines, A30-verified kill facts). Rationale rules stated before scoring in DECISION.json `sample_selection` and PORTFOLIO.md §2. |
| 2 | RANKING.csv schema exact: `idea_id,name,origin,disposition,score,uncertainty,phd_leverage,power_relevance,first_proof,capital_band,main_risk,falsifier` | PASS | Header matches character-for-character; exactly 6 data rows; no rank column added (the spec's column list has none) — row order is the ranking, convention declared in the leading comment row. |
| 3 | Full-run scoring method defined and applied: 11 named criteria, coarse ordinal scores, explicit per-score uncertainty, honest aggregation with declared weights | PASS | DECISION.json `scoring_method`: 0-4 scale, per-criterion half-width bands (0.5/1.0/1.5), fixed declared weights summing to 1.00, linear-combined aggregate uncertainty with the independence caveat stated; per-idea criterion scores recorded for audit. |
| 4 | PhD leverage must not override commercial evidence | PASS | Structural: commercial-side weight 0.60 vs founder-side 0.30 (phd_leverage 0.12). Demonstrated in output: C-01 (WEAK alignment, strongest consensus) still outranks C-07/D-10 on commercial evidence, and D-10's ADVERSE plus D-02's STRONG do not rest on prestige. |
| 5 | Disposition vocabulary keep/bridge/watch/stop with definitions; bridge tied to named B30 gates | PASS-with-note | Definitions in DECISION.json `disposition_vocabulary`. Bridges name only existing gates (BR-A/BR-B/BR-D/BR-G from BRIDGES.json). Note: no idea earned `keep`; recorded as a finding (every non-WEAK mechanism is C04/FT-02-gated per B30), not a vocabulary omission. |
| 6 | ONE weighting sensitivity check run and reported in DECISION.json `sensitivity_cases` and PORTFOLIO.md | PASS | phd_leverage halved (0.06) and doubled (0.24) with proportional renormalization; all six scores recomputed; result: zero rank flips, with an arithmetic dominance proof of stability for any weight in [0,1) and an honest caveat that the sample's wide spread suppresses flips relative to the full 24. |
| 7 | DECISION.json pilot-scoped: sample top-3, buckets with definitions, dependencies (bridge gates, C04 block, publication gate), sensitivity results, rejected alternatives with reasons, `pilot_label` | PASS | All fields present; `"pilot_label": "PILOT SAMPLE — NOT FINAL"`; dependencies cover BR gates, C04, G5 publication gate, and C33/C34 disclosure gates; five rejected alternatives with reasons. |
| 8 | PORTFOLIO.md pilot-scoped: per-idea reasoning, relation to old/new/blind verdicts (A30), what the full 24 must add | PASS | §5 (six per-idea rationales), §6 (A30 relation incl. where this ranking disagrees with all three prior runs and why), §7 (seven named full-run additions). |
| 9 | SOURCES.csv schema and claim-level mapping; B15 paper IDs for literature-backed claims; new web sources only where a decision hinged on something unverified | PASS | Header matches the required 10 columns; 21 claim rows: 1 this-run open (B40P-01), 1 disclosed failed open (B40P-02), 10 reused opened primaries with original claim_ids and reuse flags, 9 internal prerequisite rows incl. B15 EV/P paper IDs (B40P-13..16). Exactly one new web question was opened (SSCB shipping — the one record-vintage fact a sample decision leaned on); all else reused or labeled corpus-dated. |
| 10 | No semantic double-counting (A30 SEM ledger governs) | PASS | E-01 appears only inside C-01's origin (SEM-01); B-01/E-10/C-15 consolidations do not touch the sample; no idea appears twice; criterion definitions draw explicit non-overlap lines (phd_leverage vs shared_skills; founder_goal_fit vs downside; geography vs regulation). |
| 11 | Stable IDs exact | PASS | All IDs verbatim from the A30/B20 universe (P3R2-D-02, P3R2-D-01, P3R2-C-05, P3R2-C-01, P3R2-C-07, P3R2-D-10; BR-x, Cxx, EVxx, Pxxxx, FT-x, PB-x, W1/W2 as defined upstream). |
| 12 | "PILOT SAMPLE — NOT FINAL" label on every artifact | PASS | Present in RANKING.csv (leading comment row), DECISION.json (`pilot_label`), PORTFOLIO.md, SOURCES.csv (leading comment row), RUN_META.md, SELF_CHECK.md. |
| 13 | Power-electronics ideas included without forcing them up or down | PASS | Sample contains three power/power-adjacent ideas (C-01, C-07, D-10) scored by the same criteria as the rest; C-01 ranks above two non-selected outcomes and below the metrology ideas strictly on scored evidence; B25's non-wedge rule is applied to founder-led forms only. |
| 14 | Downside/opportunity cost explicitly scored; falsifiers concrete | PASS | `downside` is a weighted criterion (0.10) scored per idea; every RANKING.csv row carries a concrete falsifier naming an observable event that would change the disposition. |
| 15 | Judgment made personally; evidence-weighted, not prestige-weighted | PASS | No delegation; no citation-count/prestige input anywhere; where this ranking disagrees with all three prior runs (C-01 at 4th) the reason is scored evidence, recorded in PORTFOLIO.md §6. |
| 16 | Write only inside `pilot/B40_portfolio/attempt-1/` | PASS | Six files written, all in the target; nothing in state/, verification/, policies, workflow, evidence, sources, archive, or earlier outputs was modified. |
| 17 | Read only allowed sources/prerequisites | PASS | Only the task card, stage spec, root policies, the allowed accepted outputs (A30, B10, B15, B20, B25, B30 + their SOURCES ledgers), and the web (for the one decision-critical recheck). B00/B12 were not needed and not read; `sources/` untouched. |
| 18 | RUN_META.md with agent, requested model/effort, observed status, timing, sources, web activity, limitations | PASS | Present; observed model recorded as the runtime-exposed `claude-fable-5`; observed effort NOT_EXPOSED; wall-clock times NOT_EXPOSED. |
| 19 | Internal consistency across artifacts | PASS | Ranks, scores, uncertainties, dispositions, buckets, and sensitivity numbers are identical across RANKING.csv, DECISION.json, and PORTFOLIO.md (checked cell-by-cell during drafting; scores in the CSV are the one-decimal renderings of DECISION.json's audit values, stated as such). |
| 20 | No fabrication (citations, DOI, provenance, measurements, market facts, model identity) | PASS | Every current-market claim maps to a SOURCES.csv row; failed opens disclosed rather than paraphrased around; corpus-dated facts labeled; no new numbers invented; A20 provenance limits carried verbatim. |

## Disclosed weaknesses (none rises to FAIL)

1. **Ranks 1-3 are not separated** under the stated uncertainty bands; the
   pilot says so everywhere the scores appear. Dispositions, which rest on
   gate logic, are the robust output.
2. **The sensitivity result is degenerate-stable** (zero flips provable for
   any phd weight) because the sample deliberately spans the class
   spectrum; this is disclosed with the expectation of real flips in the
   full 24's adjacent pairs.
3. **ABB SSCB shipping status unverified** (two fetch timeouts); the C-01
   window-pressure claim rests on the opened Siemens primary plus a
   discovery-level ABB record, and is weighted accordingly.
4. **B15 §1-§3 not re-read line-by-line** this run (outline + §4-§8 direct
   read + carried adjudications); every literature claim used in scoring
   traces to sections read directly or to B20/B25/B30 carried rows.
5. **No `keep` disposition exists in the sample**, so that branch of the
   vocabulary is defined but unexercised until the full run.

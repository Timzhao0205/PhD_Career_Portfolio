Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# SELF_TEST — how to grade your blind attempt against the answer key

## 0. Protocol (do these in order; no peeking)

1. **Blind attempt first.** Read ONLY `10_PHASE1_VERIFICATION/` and
   `20_PHASE2_FUNDAMENTALS/` (the same evidence base the scorer used before valuation).
   Do NOT open `30_` or `40_` until step 3 is done. (You may fetch current prices
   yourself — the key's quotes are as-of 2026-07-07 close, recorded in VALUATION.csv.)
2. Copy `01_MISSION/SELF_TEST_MY_ATTEMPT_TEMPLATE.md` to
   `40_PHASE4_PORTFOLIO/MY_ATTEMPT.md` and fill it completely: full 14-name ranking,
   100,000 CNY paper allocation (4-6 names + cash), three convictions with confidence %.
3. Only now open `30_PHASE3_VALUATION_SCORING/SCORES.csv` and `ANSWER_KEY_BENCHMARK.md`.
4. Score yourself per §1-§3 below; write the disagreement log per §4; map gaps per §5.

## 1. Spearman rank correlation (ranking agreement)

Rank all 14 names 1..14 in both lists (your attempt = X, the key = Y from SCORES.csv).
**Ties get midranks** — in the key, 002281 and 002916 are an exact tie: assign both 6.5.
If your list has ties, midrank them the same way.

Formula (no-ties shortcut, fine if you midrank consistently):
ρ = 1 − (6 · Σdᵢ²) / (n·(n²−1)), where dᵢ = Xᵢ − Yᵢ and n = 14 → denominator 14·195 = 2730.

**Worked example** (3 names, so n=3, denominator 3·8=24):
your ranks A=1,B=2,C=3; key ranks A=2,B=1,C=3 → d = (−1, +1, 0) → Σd² = 2
→ ρ = 1 − 6·2/24 = 1 − 0.5 = **0.50**.

For n=14, interpretation bands (rough): ρ ≥ 0.7 strong agreement; 0.4-0.7 moderate;
0-0.4 weak; < 0 systematic disagreement (interesting! — see §4).

## 2. Allocation overlap %

Overlap = Σ over assets of min(your weight %, key weight %), counting CASH as an asset.
Key weights: 688629 12, 600839 10, 000034 8, 300308 8, 688981 6, CASH 56.
Example: if you held 688629 20% + 300308 10% + 002261 20% + CASH 50%
→ overlap = min(20,12) + min(10,8) + min(20,0) + min(50,56) = 12+8+0+50 = **70%**.
Bands: ≥70% near-identical stance; 40-70% same family, different conviction; <40%
materially different answer — the disagreement log is where the value is.

## 3. Conviction check

For each of your three convictions: state whether the key agrees, disagrees, or is
silent; then check whether YOUR confidence % was calibrated against the evidence tier
you actually had (a tier-C-supported conviction above ~60% confidence is a process
red flag regardless of who turns out right).

## 4. Disagreement log (the actual learning artifact)

For EVERY name where |your rank − key rank| ≥ 3, and every allocation difference ≥ 5
points (including cash), write one row:

| Name | Yours | Key's | Whose evidence was stronger? (cite the file+section) | Concept that explains the gap |

Rules of honesty: the key is not ground truth — it documents its own three biggest
uncertainties in ANSWER_KEY_BENCHMARK.md §5, and its red team (REDTEAM_*.md) attacked
its own scores harder than you will. "The key underweights X because the rubric caps
tier-C narratives" is a legitimate finding in YOUR favor if you can argue the narrative
deserves more credit — but you must say which SOURCE upgrades it, not which feeling.

Common gap-concepts you will likely need (each explained once in the mission files):
evidence tier (SOURCE_STANDARDS), exposure materiality vs concentration (SCORING_NOTES
R0.1 / rubric W2-vs-W6), priced-for-perfection (VAL_ files), core vs headline earnings
(扣非 — VAL_002261/REDTEAM_301236), verticalization precedent (REDTEAM_RESPONSES R0.3),
common-mode risk (REDTEAM_688629 §4), concept premium (VAL_000628).

## 5. Map each gap to a LEARNING_ROADMAP stage

For every disagreement-log row, tag the stage of the lab's LEARNING_ROADMAP the gap
belongs to, and add it to your study queue. Suggested mapping:
- Misread or missed a filing fact (concentration table, segment split, OCF sign) →
  Stage 1 (filings literacy). Example drill: E1 in RB_02.
- Equated "in the chain" with "moves the P&L" (e.g., ranked 300308/002156 high AS Ascend
  plays) → Stage 2 (exposure arithmetic). Drill: recompute the 300308 ceiling from
  F_300308's 境内/境外 table.
- Paid a perfection multiple for a tier-C story (002281/002916/301018 high in your list
  with no new evidence) → Stage 2/3 (valuation vs evidence). Drill: rebuild one VAL_
  file's implied-expectations paragraph from scratch.
- Missed a risk anchor (single customer, Entity List, 1260H, regulator letter) →
  Stage 3 (risk audit). Drill: pick one REDTEAM_ file and re-derive its W6 argument.
- Sized positions above what your evidence tier supports → Stage 3 (calibration).
  Drill: re-run your convictions at §3 for your NEXT three watchlist decisions.

## 6. Afterwards

Merge `PREDICTIONS_APPEND.csv` into the lab's `PREDICTIONS_LOG.csv` (schema note in
05_STATE/ASSUMPTIONS.md A15) and diary the review date 2026-09-01. When the predictions
resolve (6-12 months), grade BOTH the key and your attempt on them — argument quality
first, outcome second. A benchmark disagreement is not an error signal by itself; the
mission says so about itself in ANSWER_KEY_BENCHMARK.md §5.

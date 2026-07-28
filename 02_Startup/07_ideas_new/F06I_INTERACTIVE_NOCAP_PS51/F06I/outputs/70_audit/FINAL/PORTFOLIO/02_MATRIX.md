# Comparison matrix — readable companion to 02_MATRIX.csv

The CSV holds one header plus exactly 24 data rows in final rank order,
machine-readable. This companion explains the columns and reads the
pattern.

## Column notes

- `score_total` is the P4 weighted total (11 criteria, weights
  16/15/10/9/9/11/7/10/8/3/2 summing to 100; weighted_points =
  score × weight / 5). Totals were computed at stage 20 and carried
  unchanged; the assembly-time arithmetic audit corrected one historical
  slip (P3R2-D-18, outside the final 24) before scoring closed.
- `p4_confidence` is the stage-20 scorer's confidence, not a market
  probability. `redteam_decision`/`residual_risk` are stage-30 verdicts;
  `repair` means the idea survived with binding structural conditions
  (all three repairs concern compliance-blocked CN structures, now
  rebuilt and gated).
- `tier` is the stage-60 synthesis allocation (1 = fund experiment now,
  2 = sequence second, 3 = tracked option). Tier is a resourcing
  judgment; it never reorders ranks.
- `first_experiment_budget_usd` is the decisive-experiment figure; two
  experiments (A-14 $850k, C-09 $500k) are internally staged so
  worst-case exposure is the first stage.
- `deep_dive` names the D01-D10 report for the top ten; blank for the
  other fourteen.

## Reading the pattern

**Score bands.** 80+ (2 ideas): D-02, C-01 — both dual-market,
high-confidence, medium-risk; the portfolio's spine. 70-79 (11 ideas):
the working core, including every remaining Tier-1 experiment. 63-69
(11 ideas): options and sequenced follow-ons; every low-confidence or
high-residual idea sits here, which is the intended shape — the
portfolio pays less and asks for triggers where evidence is thinner.

**Geography.** 13 dual-market, 9 US-only, 1 US-primary-with-KR-side
(E-14), 1 CN-primary (F-16). The dual-market count is the honest
maximum after compliance gates removed blocked CN legs; see
GEOGRAPHY.md (stage 50) for per-idea structure and
PORTFOLIO_CHECKS.json (stage 40) for the unsatisfiable-target record.

**Role classes.** The portfolio is deliberately overweight
measurement/qualification (diagnostic_test_only: D-02, C-05, C-22,
G-03, D-09) and safety/protection (safety_critical_subsystem: C-01,
E-14, D-01), because those roles monetize infrastructure buildouts
without taking buildout risk. Process-value subsystems (D-10, A-10,
C-13, F-01, E-04, C-04, D-19, F-19, F-23, D-16) carry the higher
ceilings and the higher residual risks; the two equipment plays (A-14,
C-08, A-22, F-16) and the power platform (C-09) round out the mix.

**Customer classes.** Industrial buyers dominate (15 ideas);
scientific/big-physics (5), infrastructure/utility (4 including E-14),
defense primes (2: D-10, A-22). No idea depends on consumer or
early-adopter markets — consistent with the 2030 launch horizon and
the founder profile.

**Timing flags.** All 24 ideas carry experiment_by_2028 = true and
engagement_by_2029 = true — enforced at stage 40 — so the 2026-2029
preparation window is fully utilized regardless of tier.

## Scoring notes and honest caveats

- Scores are decision instruments, not valuations; a 63 with a cheap
  trigger-priced option (D-16) is a different asset class from a 74
  with contested whitespace (A-10), and the tiers express that.
- Confidence and residual risk are deliberately reported separately:
  D-01 is medium-confidence/medium-risk (thin demand conversion,
  well-understood physics), while C-08 is medium-confidence/high-risk
  (clear demand logic, heavy qualification burden). Collapsing them
  into one number would hide exactly what a funder needs to see.
- The three repair rows read `repair` in the CSV on purpose — a reader
  filtering for unconditional ideas must be able to exclude them
  mechanically.

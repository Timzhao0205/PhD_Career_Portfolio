# 40_select — final 24 and top 10

## Purpose

Select exactly 24 evidence-grounded portfolio ideas and exactly ten ideas for
full deep dives.

## Inputs allowed

- `outputs/10_refresh`
- `outputs/20_p4`
- `outputs/30_redteam`
- frozen P0-P3 evidence needed to close a load-bearing gap

Do not read historical selection, deep dives, final portfolio, or audits under
`src/06`.

## Pilot

Adjudicate five representative survivors, including a close cut-line pair.
Test Boolean fields, lane/product/customer quotas, independent US/China
evidence, and near-miss recording. Save only under `pilot/40_select`.

## Full outputs under `outputs/40_select`

- `SELECTION.json` with `artifact`, `policy`, `final_24`,
  `top_10_deep_dives`, and `near_misses`.
- `final_24` has exactly 24 unique items ranked 1-24. Every item has
  `idea_id`, `rank`, `concept`, `primary_lane`, `is_hts`,
  `product_role_class`, `customer_class`, `first_experiment_budget_usd`,
  `us_beachhead`, `china_beachhead`, `dual_market`,
  `side_market_primary`, `markets`, `g7_pass`, `experiment_by_2028`,
  `engagement_by_2029`, `score_total`, `why_now`, `key_kill`, and
  `source_ids`.
- `is_hts`, `us_beachhead`, `china_beachhead`, `dual_market`,
  `side_market_primary`, `g7_pass`, `experiment_by_2028`, and
  `engagement_by_2029` are JSON Booleans. `dual_market` equals the Boolean AND
  of the two beachhead fields.
- Markets may contain only `US`, `China`, `Japan`, `Taiwan`, and
  `South Korea`.
- `top_10_deep_dives` is ten unique idea-ID strings and a subset of final 24.
- `PORTFOLIO_CHECKS.json` records every frozen portfolio constraint with its
  observed count and Boolean pass result.
- `SELECTION.md` explains ranks, tradeoffs, replacements, deep-dive choices,
  and near misses.
- `RESULT.json`: `stage:"40_select"`, `status:"COMPLETE"`, outputs and checks.

Every selected idea must pass G1-G7. The main Fable agent personally reconciles
scores and red-team evidence rather than mechanically averaging them.


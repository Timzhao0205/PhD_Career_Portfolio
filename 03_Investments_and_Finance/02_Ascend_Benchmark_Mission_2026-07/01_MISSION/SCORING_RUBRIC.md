# SCORING_RUBRIC (binding — applied identically to every universe name)

Each dimension scored 0–5 (integers), multiplied by weight, summed to TOTAL (0–5 scale).
Every cell must cite the V_/F_/VAL_/REDTEAM_ file that supports it. A cell that cannot be
supported scores 0, not a guess. Ties broken by W1, then W4.

| # | Dimension | Weight | Anchors |
|---|---|---|---|
| W1 | Evidence strength of Huawei/Ascend link | 0.20 | 5 = tier A (own filing / official IR reply names the business); 3 = tier B (major media / named sell-side); 1 = tier C only; 0 = UNVERIFIED |
| W2 | Exposure materiality | 0.20 | 5 = est. Huawei-linked share >30% of revenue AND growing; 3 = 10–30%; 1 = <10% or flat; 0 = NOT-ESTIMABLE. (Concentration downside is priced in W6, not here) |
| W3 | Fundamentals quality | 0.15 | 5 = growing revenue, stable/rising margins, positive OCF, net cash; 3 = mixed; 1 = deteriorating margins or persistent cash burn; 0 = distress signs |
| W4 | Valuation vs implied expectations | 0.20 | 5 = SKEPTICALLY-PRICED with tier ≤B evidence of growth; 3 = NEUTRAL; 1 = PRICED-FOR-PERFECTION; 0 = PRICED-FOR-PERFECTION on tier-C evidence |
| W5 | Layer economics / moat | 0.15 | 5 = technical-barrier component layer with content-per-system growth (optics/connectors/advanced packaging per RB_02 read #2); 3 = defensible but competitive; 1 = commoditized integration/distribution margin-squeeze layer |
| W6 | Risk (inverted) | 0.10 | 5 = diversified customers, low policy common-mode, low verticalization threat; 3 = one material concentration OR verticalization exposure; 1 = both; 0 = single-customer + internalization precedent (cf. in-house HBM) |

Rules:
- Sub-scores are set BEFORE portfolio construction; Phase 4 may not retro-adjust scores.
- Red-team concessions change scores only with a written response in REDTEAM_RESPONSES.md.
- SCORES.csv schema: ticker,name,W1,W2,W3,W4,W5,W6,total,rank,cell_sources.
- Portfolio construction constraint (Phase 4): max 2 names per layer; sum of weights in
  any single layer ≤40%; cash remainder allowed and encouraged if <4 names clear a total
  score of 3.0 — "no strong answer" is a legitimate benchmark answer.

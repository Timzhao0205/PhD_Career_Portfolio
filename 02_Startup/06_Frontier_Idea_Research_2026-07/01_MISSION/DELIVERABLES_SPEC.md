# Deliverables and pass thresholds

| Phase | Required outputs | Pass threshold |
|---|---|---|
| P0 | state, assumptions, routing log | preflight and model probes recorded |
| P1 | 16 lane briefs + 16 raw ledgers | >=720 reviewed; every lane complete |
| P2 | canonical ledger + source atlas | >=600 accepted; mix and peer-review gates pass |
| P3 | round-2 seeds + longlist markdown/json | >=80 regenerated seeds; >=48 distinct ideas, >=14 lanes; US/China quotas pass |
| P4 | demand/competition/physics checks + scores | every idea passes/fails explicit gates |
| P5 | red teams + selection | top 24 compliant; top 10 selected for deep dives |
| P6 | 10 deep dives + geography brief | source quotas and US/China-primary plus side-market analysis complete |
| P7 | final portfolio + roadmap | 24 full idea cards and ranked comparison |
| P8 | machine audit + Fable adjudication | zero unresolved FAIL; final PASS |

Final idea card fields: concept; buyer and painful job; product; “cool” frontier vision; extreme
edge; current demand proof; niche size by bottom-up arithmetic; competition; technical path;
decisive experiment and budget; v1 capital/time; risks and kill criteria; US route; China route;
optional Japan/Taiwan/South Korea routes; expansion; founder-fit note (last); score; confidence;
citations.

The final comparison CSV must contain: `idea_id, rank, concept, primary_lane, sector_cluster,
product_role, primary_customer_archetype, primary_market, first_experiment_budget_usd, us_beachhead,
china_beachhead, secondary_markets, asia_beachhead, score_total, confidence`. Values for
`product_role` are `process_output`,
`infrastructure`, `scientific_system`, or `diagnostic_test`. Customer archetypes are `industrial`,
`scientific_big_physics`, `infrastructure_utility_transport`, or `other`. `us_beachhead`,
`china_beachhead`, and `asia_beachhead` are booleans. `secondary_markets` is a semicolon-separated
subset of `JP;TW;KR`. `asia_beachhead` is retained for compatibility and means any of
China/Japan/Taiwan/South Korea; it never substitutes for `china_beachhead`. India and Singapore
cannot satisfy any market field and must not appear in final market analysis.

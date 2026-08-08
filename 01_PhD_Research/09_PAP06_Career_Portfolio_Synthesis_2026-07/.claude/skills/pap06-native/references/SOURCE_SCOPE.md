# Stage source scope

Use these paths when writing `state/CURRENT_TASK.md`. Earlier accepted outputs
may be read only when listed as prerequisites in `workflow/ROUTE.json` or below.

| Stage | Allowed immutable/source material | Special restriction |
|---|---|---|
| A10_blind | `evidence/blind/*`, root policies, its stage spec | No `sources/`, history, web, old/new results, or earlier rankings |
| A20_prov | `sources/old06`, `sources/history/prev_chat.md`, `evidence/SOURCE_MANIFEST.json`, root policies | Do not read A10 ranking content; its acceptance status alone may be known |
| A30_verify | `sources/old06`, `sources/new06`, history, accepted A10/A20, root policies, web | Exact-ID and semantic comparisons must remain separate |
| B00_inventory | all `sources/`, source manifest, accepted A30 | Factual mapping only; no ranking |
| B10_phd | `sources/phd`, accepted B00, root policies, web as needed | Extract/proposed/inferred distinctions; no portfolio ranking |
| B12_lit_search | accepted B00/B10, relevant source bibliographies, literature/source policies, web | Search/screen only; no final judgment |
| B15_lit_synth | accepted B10/B12, relevant source files, literature/source policies, web | Independently correct B12 before accepting evidence |
| B20_align | all sources, accepted B00/B10/B15 and A30, web | Analyze both causal directions; user's expectation is a hypothesis |
| B25_power | all sources, accepted B15/B20, web | Cover at least 18 directions and missing capabilities |
| B30_skills | accepted B20/B25/B15/B10 plus cited sources | Do not infer current skill merely from literature prevalence |
| B40_portfolio | accepted A30 and all accepted B stages through B30, cited sources | Exactly 24 stable IDs; avoid semantic duplicate inflation |
| B50_execution | accepted B40 plus supporting accepted stages and current official sources | Separate AI work from human/professional approvals |
| B60_redteam | every accepted earlier output plus risk-stratified source rechecks | Do not directly rewrite earlier outputs |
| B70_synth | every accepted earlier output and B60 issues | Resolve or carry every issue explicitly |
| B80_audit | complete accepted run, verification reports, state, source manifest, source samples | No PASS with any critical or major issue open |

Files under `archive/` may be used only to explain package lineage, not as
current research evidence.

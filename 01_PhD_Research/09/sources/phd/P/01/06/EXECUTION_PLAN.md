# Execution plan

| Order | Stage | Claude model | Effort | Main deliverable |
|---:|---|---|---|---|
| 1 | 00_inventory | Sonnet 5 | High | input/requirements/conflict baseline |
| 2 | 10a_literature_gan | Sonnet 5 | Extra High | GaN/WBG literature lane |
| 3 | 10b_literature_fusion | Sonnet 5 | Extra High | fusion-diagnostics literature lane |
| 4 | 10c_literature_methods | Sonnet 5 | Extra High | methods/metrology literature lane |
| 5 | 10d_literature_merge | Fable 5 | Extra High | verified source ledger and synthesis |
| 6 | 20_direction | Fable 5 | Extra High | PhD direction decision |
| 7 | 30_manuscript | Fable 5 | Extra High | manuscript/reviewer strategy |
| 8 | 40_experiment | Fable 5 | Extra High | HSX experiment and statistics plan |
| 9 | 50_patent | Fable 5 | Extra High | cautious IP/prior-art analysis |
| 10 | 60_timeline | Sonnet 5 | High | 24-month roadmap |
| 11 | 70_redteam | Fable 5 | Extra High | skeptical audit and corrections |
| 12 | 80_synthesis | Fable 5 | Extra High | final executive strategy/action plan |

Stages run sequentially because later acceptance gates depend on earlier
validated artifacts. Stage 70 remains an adversarial audit, but in this
Claude-only package it is not a cross-provider audit. Provider-independent
review is deferred to a manual ChatGPT Windows continuation if required.

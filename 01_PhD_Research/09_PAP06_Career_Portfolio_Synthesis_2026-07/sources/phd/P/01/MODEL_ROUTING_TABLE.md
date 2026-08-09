# Model routing table

The PowerShell path is Claude-only. The ChatGPT column is a manual continuation
mapping used only after the user opens this folder in the ChatGPT desktop app.

| Stage | Claude Code model | Claude effort | ChatGPT Windows equivalent | ChatGPT effort |
|---|---|---:|---|---:|
| 00_inventory | Sonnet 5 | High | GPT-5.6 Sol | High |
| 10a_literature_gan | Sonnet 5 | Extra High | GPT-5.6 Sol | Extra High |
| 10b_literature_fusion | Sonnet 5 | Extra High | GPT-5.6 Sol | Extra High |
| 10c_literature_methods | Sonnet 5 | Extra High | GPT-5.6 Sol | Extra High |
| 10d_literature_merge | Fable 5 | Extra High | GPT-5.6 Sol | Max |
| 20_direction | Fable 5 | Extra High | GPT-5.6 Sol | Max |
| 30_manuscript | Fable 5 | Extra High | GPT-5.6 Sol | Max |
| 40_experiment | Fable 5 | Extra High | GPT-5.6 Sol | Max |
| 50_patent | Fable 5 | Extra High | GPT-5.6 Sol | Max |
| 60_timeline | Sonnet 5 | High | GPT-5.6 Sol | High |
| 70_redteam | Fable 5 | Extra High | GPT-5.6 Sol | Max |
| 80_synthesis | Fable 5 | Extra High | GPT-5.6 Sol | Max |

If Max is unavailable in the app, use GPT-5.6 Sol at Extra High and record that
substitution in `state\OPERATION_LOG.csv`.

The mapping is deliberately quality-first for the critical synthesis,
direction, manuscript, experiment, IP, red-team, and final stages. Inventory,
parallel evidence collection, and timeline assembly retain the lower-cost
Sonnet allocation.

Model-integrity enforcement applies only to the **final accepted result** in
the seven Fable 5 rows. Temporary and auxiliary/subagent model selection is
allowed and logged, but Fable 5 must re-read that work and produce the final
validated result. Sonnet-stage model adjustments do not trigger the downgrade
state machine.

# Model and effort plan

The parent/orchestrator session is **Claude Fable 5 / xhigh**. It maintains
state, enforces gates, and accepts the final synthesis. Support work uses Sonnet
5 where structured extraction or search volume matters more than deep judgment.

| Stage | Agent | Requested model | Effort | Why this is cost-appropriate |
|---|---|---:|---:|---|
| 00 scope | `s00-scope` | Sonnet 5 | medium | Deterministic inventory and scope boundary |
| 10 disclosure | `s10-disclosure` | Sonnet 5 | high | Detailed manuscript extraction and enablement map |
| 20 prior art | `s20-prior-art` | Sonnet 5 | xhigh | Search breadth, family consolidation, claim reading |
| 30 IP screen | `s30-ip-screen` | Fable 5 | xhigh | Critical novelty/non-obviousness/new-use judgment |
| 40 UHV package | `s40-uhv` | Fable 5 | xhigh | Critical system-combination and engineering judgment |
| 50 arXiv gate | `s50-arxiv` | Sonnet 5 | high | Procedural source scrub, timeline, and OTL checklist |
| 60 red team | `s60-red-team` | Fable 5 | xhigh | Adversarial challenge of the strongest filing case |
| 70 final | `s70-final` | Fable 5 | xhigh | Accepted decision and advisor/OTL synthesis |

## Execution and budget controls

- Run agents sequentially so logs and state cannot race.
- Reuse the supplied seeds but verify them; do not repeat searches merely to hit
  a numeric quota.
- Stop a search branch after reasonable saturation: two materially different
  query formulations produce no new close reference and the required coverage
  category has an identified closest reference or an explicit documented gap.
- Read patent independent claims and relevant specifications for close records;
  do not spend turns deeply reading remote references.
- A routine format repair stays on the assigned model and does not rerun the
  entire stage.
- No dollar cap automatically terminates the work. Usage and cost are logged
  only when Claude Code exposes them.

## Model acceptance

Requested-model evidence is the agent frontmatter and launch arguments.
Observed-model evidence must come from Claude Code metadata, `/status`, or a
visible fallback notice; a model's self-identification alone is not proof. Use
`not_exposed` when actual telemetry is unavailable.

Every Fable-assigned output must be authored or substantively re-authored by
Fable 5/xhigh. Sonnet may gather evidence for it, but cannot supply the accepted
Fable judgment. Follow the two-strike policy in `CLAUDE.md`.

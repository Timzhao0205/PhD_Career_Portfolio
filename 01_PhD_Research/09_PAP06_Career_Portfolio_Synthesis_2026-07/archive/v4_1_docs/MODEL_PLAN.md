# Accuracy/budget model route

The controller itself is Fable 5/xhigh. It orchestrates and validates but does
not replace the named stage worker.

| Order | Stage | Purpose | Named agent | Model / effort | Accepted role |
|---:|---|---|---|---|---|
| A1 | `A10_blind` | Reconstruct 24 ideas from score-free 126 pool | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| A2 | `A20_prov` | Audit historical generation/model provenance | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| A3 | `A30_verify` | Compare blind vs old vs new; verify disagreements | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B1 | `B00_inventory` | De-duplicate and map all inputs/current sources | `pap06-sonnet-high` | Sonnet 5 / high | Supporting facts |
| B2 | `B10_phd` | Extract PhD and Opt2 claims/constraints | `pap06-sonnet-high` | Sonnet 5 / high | Supporting facts |
| B3 | `B12_lit_search` | Search, screen, and verify publications/DOIs | `pap06-sonnet-high` | Sonnet 5 / high | Supporting evidence |
| B4 | `B15_lit_synth` | Adjudicate papers, contradictions, gaps, applicability | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B5 | `B20_align` | Analyze PhD↔startup directional impact | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B6 | `B25_power` | Specialized converter/electronics/supply analysis | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B7 | `B30_skills` | Shared skills and bridge experiments | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B8 | `B40_portfolio` | Combined ranking and portfolio decisions | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B9 | `B50_execution` | Milestones, IP/collaboration, manual work | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B10 | `B60_redteam` | Independent adversarial review | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B11 | `B70_synth` | Detailed and plain-language synthesis | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |
| B12 | `B80_audit` | Final evidence/model/schema/release audit | `pap06-fable-xhigh` | Fable 5 / xhigh | Critical |

Every row runs twice: a live pilot, then the full stage. Thus 24 of 30 stage
calls use Fable 5/xhigh, and 6 bounded supporting calls use Sonnet 5/high.

This is budget optimization by task routing, not a budget shutdown. The package
has no cost, token, turn, or time ceiling. The three Sonnet stages cannot make
final judgments; downstream Fable stages independently inspect their evidence.

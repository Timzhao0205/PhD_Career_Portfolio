# Execution plan

| Stage | Model / effort | Purpose | Required outputs |
|---|---|---|---|
| `00_inventory` | Sonnet 5 / high | Reconstruct the user's hypothesis, folder 06 baseline, constraints, and conflicts | inventory, requirements trace, conflict ledger |
| `10a_literature_hybrid` | Sonnet 5 / xhigh | Additional Hall/coil, integrator, observer, and calibration evidence | hybrid evidence lane and synthesis |
| `10b_literature_radiation` | Sonnet 5 / xhigh | Direct and enabling radiation evidence | radiation evidence lane and synthesis |
| `10c_literature_applications` | Sonnet 5 / high | Application, alternative, and group landscape | applications evidence lane and synthesis |
| `10d_evidence_merge` | Fable 5 / xhigh | Verify, deduplicate, reconcile, and impose source/topic gates | final ledger and three reviews |
| `20_observability` | Fable 5 / xhigh | Determine what mutual calibration can actually identify | observability, feasibility, estimator requirements |
| `30_radiation_compensation` | Fable 5 / xhigh | Design compensation/reference options and validation | architecture, simulation/validation plan, risk register |
| `40_applications_collaboration` | Sonnet 5 / xhigh | Prioritize use cases and candidate groups without outreach | application scorecard and collaboration strategy |
| `50_limitations_comparison` | Fable 5 / xhigh | Compare alternatives and expose hard failure modes | limitations, comparison, falsification tests |
| `60_research_program` | Fable 5 / xhigh | Choose sequence, budget tiers, and decision gates | integrated program, roadmap, advisor brief |
| `70_redteam` | Fable 5 / xhigh | Attack novelty, evidence, identifiability, and feasibility | findings, source audit, correction log |
| `80_synthesis` | Fable 5 / xhigh | Give direct answers and audited final recommendation | executive decision, plain guide, action plan, index, audit |

The runner executes sequentially because later critical reasoning depends on
the validated artifacts and corrections from earlier stages. Within a
literature stage, Claude may parallelize independent searches, but each stage
must merge and validate its own output before returning.

## Budget control

- Use Sonnet for broad discovery and structured extraction.
- Use Fable only where synthesis, identifiability, design choice, or adversarial
  judgment materially affects correctness.
- Limit turns per stage in the runner; do not impose a hard monetary cap that
  could terminate a source audit mid-write.
- Record reported token/cost metrics rather than assuming a price.
- Reuse verified folder `06` evidence, but require a measured new-source delta.
- Never pad source counts with irrelevant papers.

## Resume

The launcher always supplies `-Resume`. A completed stage is skipped unless
explicitly forced. A partial Claude session is resumed when its session ID is
available. A protected manual pause requires explicit
`-RetryClaudeAfterHandoff`.

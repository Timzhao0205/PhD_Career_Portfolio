# Stage 80 — final synthesis and audit

Synthesize the accepted prior-stage work after applying the red-team
corrections. Do not introduce a new direction, invention, experiment, or
source-dependent claim at this stage.

Create `outputs/FINAL_EXECUTIVE_STRATEGY.md` as the primary decision document:

- direct answer on continue/adjust/change;
- evidence-backed research thesis and why;
- paper diagnosis and publication route;
- minimum next experiment;
- 24-month graduation strategy;
- startup preparation;
- pre-publication IP hold and professional-review gates;
- key uncertainties, reversal triggers, and contingency plan;
- concise source links using `[S####]`.

Create `outputs/FINAL_ACTION_PLAN.md` with:

- next 72 hours, 30 days, 90 days, six months, 12 months, and 24 months;
- owner/decision maker, dependency, acceptance gate, and fallback;
- a short “do not do yet” list;
- exact materials to take to the advisor meeting.

Create `outputs/FINAL_DELIVERABLE_INDEX.md` listing every output, its purpose,
stage, validation status, and recommended reading order.

Create `outputs/FINAL_AUDIT.md` containing:

- requirement-by-requirement trace to outputs;
- required-file validation;
- source-ledger row count and peer-review count;
- duplicate/type/schema check;
- reviewer-comment coverage;
- model/effort, downgrade, retry, and manual handoff summary from runner logs;
- red-team disposition summary;
- unresolved noncritical gates;
- clear limitation that research strategy completion is not experimental,
  publication, patent, legal, ownership, or immigration validation.

The final line must be exactly:

```text
FINAL STATUS: PASS
```

Write that line only if every required file exists, the ledger contains at
least 150 unique verified peer-reviewed papers, all stage acceptance gates
pass, and there is no unresolved critical defect. Otherwise use
`FINAL STATUS: BLOCKED`, save a checkpoint, and specify the exact unblock
action.

Next stage: none.

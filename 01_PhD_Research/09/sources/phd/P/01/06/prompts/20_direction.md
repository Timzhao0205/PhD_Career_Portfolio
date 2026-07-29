# Stage 20 — research-direction decision

Using the supplied evidence and verified literature ledger, determine whether
the original GaN Hall magnetic-diagnostics direction should continue,
substantially adjust, or change.

Evaluate at least:

1. a strengthened continuation centered on a finished, calibrated sensing
   output;
2. an adjacent low-cleanroom adjustment that reuses established devices and
   puts novelty in application/system/simulation/software;
3. a genuine change-of-direction option supported by the literature and group
   fit.

Add other options only when directly supported by the supplied work and
literature; do not brainstorm unrelated startup ideas.

Create `outputs/02_DIRECTION_SCORECARD.csv` with header:

```text
option_id,option_name,scope,24_month_publishability,novelty_strength,evidence_strength,cleanroom_burden,experimental_burden,software_simulation_leverage,advisor_group_fit,startup_optionality,schedule_risk,key_dependency,weighted_score,rank,decision
```

State the scoring scale, weights, calculations, uncertainty, and sensitivity
to plausible weight changes. Low burden and low risk must be scored in the
beneficial direction.

Create `outputs/02_RESEARCH_DIRECTION_DECISION.md` containing:

- an executive continue/adjust/change verdict;
- the strongest defensible thesis for each viable option;
- what is already demonstrated, what requires analysis, and what requires a
  new experiment;
- novelty versus prior art, with `[S####]` citations;
- minimum viable paper sequence within 24 months;
- cleanroom/fabrication plan using existing topologies where feasible;
- stop/pivot gates and a fallback if the August/next HSX campaign slips;
- implications for post-PhD startup preparation without converting the report
  into investment advice;
- the exact advisor decisions needed next.

The recommendation must be falsifiable: name evidence or experiment outcomes
that would reverse it.

Next stage: `30_manuscript`.

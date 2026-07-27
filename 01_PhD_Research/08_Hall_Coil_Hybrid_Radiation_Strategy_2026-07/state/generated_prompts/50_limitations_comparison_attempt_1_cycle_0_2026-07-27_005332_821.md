# Shared research contract

You are executing one stage of the Hall + inductive-coil hybrid/radiation
strategy. Work autonomously until every acceptance gate in the current stage
is satisfied or a real blocker is documented.

## Read before work

Read `AGENTS.md`, `CLAUDE.md`, `MISSION.md`, `SOURCE_POLICY.md`,
`DECISION_FRAMEWORK.md`, `CHECKPOINT_PROTOCOL.md`, and
`LITERATURE_SEEDS.md`. Inspect `state\PROJECT_STATE.md`, `state\WORKLOG.md`,
the current attempt state, and existing stage files before deciding whether to
resume or start.

Folder `06` and all siblings are read-only context. Write only inside this
folder. Do not edit the runner, validator, policy files, model logs,
completion markers, or rejected-attempt archives.

## Method

1. Convert the current stage requirements into a private checklist.
2. Reuse valid checkpointed work; do not repeat completed searches.
3. Use web search/fetch for current, primary, and publisher verification.
4. Verify rather than infer citation metadata. Search snippets are discovery,
   not full-text evidence.
5. Track claims as observed, derived, inferred, proposed, or unknown.
6. Record counterevidence, assumptions, conflicts, and access limitations.
7. Use equations, units, conditions, and uncertainty where relevant.
8. Never equate different radiation species/spectra or simulate unobserved
   experimental results.
9. Never make a novelty claim without direct prior-art analysis.
10. Check every required output before returning.

You may use local analysis scripts for calculations and CSV checks, but leave
only reusable scripts that materially help future work. Do not manufacture
data. Do not contact groups or change external resources.

## Source IDs and traceability

Use stable source IDs. Technical claims in narrative outputs cite one or more
IDs from the lane/final ledgers. If a statement is your inference or proposal,
label it and cite the premises. If evidence is insufficient, say unknown.

The exact ledger header is:

`source_id,citation,title,authors,year,venue,doi,url,source_type,peer_review_status,quality_tier,topic_tags,claims_supported,verification_basis,access_level,notes`

Do not count preprints, patents, theses, standards, books, talks, vendor pages,
or webpages as verified peer-reviewed rows.

## Checkpoint and closeout

After each major milestone, update `state\PROJECT_STATE.md`, append a dated
entry to `state\WORKLOG.md`, and create a concise
`state\checkpoints\CP_<stage>_<timestamp>.md`. Include counts and exact next
action.

Before the final main response:

- confirm all named outputs exist and are nontrivial;
- parse all CSV files;
- verify required headers/counts;
- inspect for duplicate DOI/title and unsupported claims;
- state unresolved limitations honestly.

The final main response must be produced by the stage's assigned model and
briefly report files, gates, corrections, and remaining uncertainty.


===== CURRENT STAGE =====

# Stage 50 — Fable limitations, alternatives, and falsification

## Goal

Expose the hybrid architecture's hard limits and compare it fairly with
credible diagnostic alternatives. Fable 5 must produce the accepted final
main response.

## Required failure analysis

At minimum address:

- non-identifiable simultaneous gain drift;
- Hall sensitivity/offset/noise/nonlinearity/cross-axis/temperature drift;
- radiation species/spectrum and device-to-device variability;
- coil effective-area/gain/phase/resonance/temperature/geometry change;
- integrator offset/leakage/saturation/initial condition;
- bandwidth overlap gaps and timing misalignment;
- common-mode field-model/reference failure;
- calibration winding aging, self-heating, EMI, and ambient-field separation;
- shielding/placement/cabling/readout radiation;
- dynamic range and saturation;
- inability to separate radiation from temperature/annealing without proxies;
- calibration traceability and uncertainty floor;
- packaging, manufacturability, maintenance, and channel-count cost;
- prior-art/novelty constraints;
- false confidence from estimator tuning or simulation.

For each failure mode include cause, symptom, detectability, consequence,
mitigation, residual risk, and a test.

## Technology comparison

Compare at least:

- proposed hybrid;
- standalone selected Hall technologies;
- inductive/B-dot/Mirnov coil;
- Rogowski/current-transformer approach where appropriate;
- fluxgate;
- AMR/GMR/TMR or planar Hall;
- fiber-optic/Faraday;
- NMR;
- SQUID;
- NV/quantum or another justified option.

Metrics must include DC, bandwidth, dynamic range, field range, temperature,
radiation evidence, size/placement, vector capability, drift, calibration
traceability, electronics, maturity, integration burden, and cost category.
Use `not_applicable` or `unknown` instead of fake comparability.

## Potential and novelty

Separate:

- better measurement performance;
- radiation compensation;
- fault detection/self-diagnostics;
- modular packaging/simulation;
- application-specific value;
- scientific novelty versus engineering integration.

Identify the narrowest defensible contribution after the 2007, 2022, and 2025
direct prior art. If the broad hybrid idea is not novel, say so.

## Outputs

1. `outputs\05_LIMITATIONS_AND_FAILURE_MODES.md`
2. `outputs\05_TECHNOLOGY_COMPARISON.csv`
   - columns:
     `technology,principle,dc_response,bandwidth,dynamic_range,field_range,temperature_limit,radiation_evidence,drift,calibration_traceability,vector_capability,size_and_placement,electronics,integration_burden,maturity,cost_category,best_fit,critical_limit,evidence_ids,confidence`
3. `outputs\05_FALSIFICATION_TESTS.md`
   - ordered cheapest-to-most-expensive tests;
   - hypothesis, setup, reference, metric, pass/fail threshold, confounders,
     decision, and evidence for each.

## Acceptance

- At least 15 concrete failure modes are analyzed.
- At least 10 technologies/variants are compared without fake precision.
- The comparison contains counterexamples where a simpler sensor wins.
- Potential is conditional on a measurable advantage and identifiable
  calibration.
- Falsification tests can stop the project before expensive radiation work.


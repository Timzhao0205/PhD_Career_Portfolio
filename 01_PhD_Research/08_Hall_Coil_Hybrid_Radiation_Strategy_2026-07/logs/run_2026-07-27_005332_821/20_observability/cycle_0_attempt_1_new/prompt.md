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

# Stage 20 — Fable observability and mutual-calibration feasibility

## Goal

Decide, with equations and explicit assumptions, whether and when the Hall and
coil channels can calibrate each other. Fable 5 must produce the accepted
final main response.

## Required model

Start from, then refine as necessary:

```text
y_H(t) = S_H(t) B(t) + b_H(t) + n_H(t)
y_C(t) = K_C(t) dB(t)/dt + b_C(t) + n_C(t)
```

For integrated-coil implementations, include integrator state, initial
condition, leakage/time constant, timing/phase, and drift. Add temperature,
radiation history, cross-axis/misalignment, nonlinearity, and saturation only
with a clear reason.

Define:

- state vector;
- unknown parameters;
- known inputs;
- process/measurement noise;
- priors or slow-drift models;
- calibration/excitation signal;
- reference measurement.

## Required cases

Analyze at least:

1. Hall sensitivity stable; Hall bias drifts; coil gain stable; integrator
   drifts.
2. Hall sensitivity and bias both drift; coil gain stable.
3. Hall sensitivity/bias and coil gain/integrator all drift.
4. Known machine coil current and trustworthy field model.
5. Embedded calibration/test coil with characterized transfer function.
6. Repeated reference waveform/shot.
7. Material-diverse redundant Hall channel and temperature/dose proxies.
8. Quasi-static field with little persistent excitation.
9. Fast transient with poor Hall bandwidth or coil saturation.

For each case determine local/structural identifiability or augmented-state
observability. Use an observability matrix, sensitivity/Fisher-information
analysis, symbolic reasoning, or a justified numerical rank test. Do not use
“complementary bandwidth” as a substitute for this proof.

Test at least these confoundings:

- scale transformation between `B` and `S_H`;
- simultaneous Hall and coil gain drift;
- Hall offset versus slowly changing field;
- coil/integrator offset versus low-frequency field;
- temperature versus radiation effects;
- sensor failure versus model mismatch.

## Required conclusions

State separately:

- what the coil can estimate or constrain about Hall offset, gain, dynamics,
  and faults;
- what Hall can estimate or constrain about coil initial condition,
  integrator drift, gain, and low-frequency/DC content;
- what cannot be determined without an external reference;
- minimum excitation/reference requirements;
- uncertainty and fault-detection implications.

Do not force symmetry. “Mutual calibration” may be partly true, conditionally
true, or misleading.

## Outputs

1. `outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md`
   - equations, cases, rank/identifiability results, assumptions, and source
     support.
2. `outputs\02_MUTUAL_CALIBRATION_FEASIBILITY.md`
   - direct plain-language verdict;
   - feasible/not-feasible/conditional matrix;
   - required references;
   - implications for radiation-induced sensitivity tracking.
3. `outputs\02_ESTIMATOR_REQUIREMENTS.csv`
   - columns:
     `case_id,objective,states,unknown_parameters,known_inputs,excitation,reference,observable_quantities,unobservable_quantities,estimator_candidate,uncertainty_method,fault_test,evidence_ids,verdict,notes`

## Acceptance

- Every case has a defensible observability/identifiability argument.
- At least one non-identifiable counterexample is shown.
- The verdict distinguishes Hall gain from Hall offset and coil gain from
  integrator drift.
- Existing hybrid literature is not overextended to radiation calibration.
- Numerical demonstrations, if used, include reproducible assumptions and do
  not masquerade as experimental validation.


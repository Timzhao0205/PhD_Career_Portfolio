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

# Stage 30 — Fable radiation compensation architecture

## Goal

Translate the evidence and identifiability verdict into architecture options
that maximize accuracy under controlled budget. Fable 5 must produce the
accepted final main response.

## Architecture options to evaluate

At minimum compare:

A. Hall + coil fusion only, with no injected reference.
B. Hybrid plus embedded calibration/test winding and traceable current source.
C. Hybrid plus machine-coil current/field model as a reference.
D. Hybrid plus material-diverse/redundant Hall channel.
E. Hybrid plus periodic external reference calibration.
F. Radiation-hard Hall technology alone.
G. Coil/optical/other diagnostic without semiconductor Hall.

You may add better options. Do not assume the embedded coil's field remains
known under radiation, temperature, geometry change, or mutual coupling.

## Required technical content

- parameterize Hall sensitivity, offset, resistance/noise, temperature, dose
  or fluence, annealing, and time;
- parameterize coil effective area/gain, phase/bandwidth, insulation, readout,
  and integrator drift;
- define calibration waveform, bandwidth overlap, reference traceability, and
  estimator states;
- distinguish online compensation, scheduled calibration, fault detection,
  and post-exposure correction;
- state which radiation mechanisms are measurable in situ and which require
  ex-situ characterization;
- include cross-sensitivity, common-mode failure, reference degradation, and
  uncertainty propagation.

For an embedded calibration winding, analyze whether its field can isolate
Hall gain/bias in the presence of an unknown ambient field. Consider
frequency-separated injection/lock-in detection, waveform design, amplitude,
heating, EMI, geometry, and whether the coil/channel itself needs a reference.

## Validation ladder

Design the lowest-cost sequence that can falsify the concept:

1. simulation/synthetic fault injection;
2. benchtop static/dynamic field and temperature tests;
3. controlled offset/gain emulation;
4. long-duration drift test;
5. material/device radiation screening;
6. collaborator-led neutron/gamma qualification only if earlier gates pass;
7. relevant-machine demonstration.

Specify calibration standards/references, sample sizes where defensible,
repeatability, uncertainty budgets, acceptance thresholds, and stop rules.
Never invent facility access or prices.

## Outputs

1. `outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md`
   - option comparison;
   - recommended minimum viable and higher-accuracy designs;
   - measurement equations and block-level interfaces;
   - compensation/estimator logic;
   - accuracy/cost drivers;
   - unresolved engineering risks.
2. `outputs\03_SIMULATION_AND_VALIDATION_PLAN.md`
   - state-space/simulation specification suitable for a later reusable
     package;
   - parameter schema, scenarios, fault injections, reference datasets,
     metrics, tests, reproducibility, and staged experiments;
   - explicit boundary between simulated, bench, and radiation evidence.
3. `outputs\03_RADIATION_RISK_REGISTER.csv`
   - columns:
     `risk_id,component,mechanism,radiation_or_environment,observable_effect,detectability,compensation_possible,reference_required,likelihood,impact,evidence_ids,mitigation,validation_test,residual_risk,decision_gate`

## Acceptance

- The selected architecture is consistent with Stage 20 observability.
- Accuracy claims have an uncertainty/reference basis.
- At least three budget tiers and clear stop/go gates are included.
- The plan does not make radiation testing a hidden prerequisite for the
  user's current first-author HSX paper.
- The later simulation package has enough interfaces/tests to implement
  without inventing the scientific model.


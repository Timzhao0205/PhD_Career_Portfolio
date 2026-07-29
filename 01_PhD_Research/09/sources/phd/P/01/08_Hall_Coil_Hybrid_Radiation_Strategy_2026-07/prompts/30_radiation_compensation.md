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

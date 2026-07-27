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

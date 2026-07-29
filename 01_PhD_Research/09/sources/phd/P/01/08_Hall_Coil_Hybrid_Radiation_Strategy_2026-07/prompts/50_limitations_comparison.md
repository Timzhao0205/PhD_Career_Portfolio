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

# Stage 40 — finished-study experiment and analysis plan

Design the minimum rigorous bench and HSX campaign needed to turn voltage
responses into a defensible magnetic-field instrument study while minimizing
new fabrication.

Use supplied hardware/data constraints. Never assume equipment, probes,
feedthroughs, sensors, shot time, or machine signals are available unless the
files establish it; use explicit confirmation gates.

Create `outputs/04_MEASUREMENT_REQUIREMENTS.csv` with header:

```text
requirement_id,reviewer_or_science_driver,measurement,minimum_design,preferred_design,hardware_or_signal_needed,replicates,independent_variable,dependent_variable,acceptance_metric,uncertainty_component,dependency,priority,fallback_if_unavailable
```

Create `outputs/04_HSX_EXPERIMENT_PLAN.md` covering:

- pre-campaign inventory and go/no-go gates;
- DC and frequency-dependent bench calibration;
- field-to-voltage transfer function and sign/orientation;
- offset, linearity, hysteresis, temperature, drift, noise, bandwidth, and
  parasitic characterization;
- device/module repeatability using existing fabrication iterations where
  available, with an honest single-device fallback;
- conventional Hall/gaussmeter/B-dot/Mirnov or computed-field reference
  strategy, clearly separating what is feasible on bench and in HSX;
- coil-only absolute-field anchor and pose uncertainty;
- plasma-shot matrix, controls, randomized/repeated conditions when feasible,
  metadata, synchronization, and failure handling;
- minimum publishable data package for Sensors Letters and the fuller RSI
  package;
- work/time burden and a low-cleanroom implementation route.

Create `outputs/04_DATA_ANALYSIS_PLAN.md` covering:

- raw-data immutability and provenance;
- preprocessing, calibration, offset removal, synchronization, filtering, and
  bandwidth estimation;
- transfer-function and uncertainty propagation equations;
- 1:1 comparison metrics, residuals, confidence intervals, and effect sizes;
- repeated-measures/shot variability;
- figures and tables mapped to claims;
- leakage/overfitting safeguards for any ML/model-based method;
- reproducible scripts and data-release structure.

Create `outputs/04_UNCERTAINTY_AND_STATISTICS_PLAN.md` with a worked symbolic
uncertainty budget, statistical unit definitions (device, module, shot,
time-sample), minimum useful replication logic, sensitivity analysis, and
language for limitations if ideal replication is impossible. Do not invent a
sample-size number without assumptions or a power/sensitivity justification.

Next stage: `50_patent`.

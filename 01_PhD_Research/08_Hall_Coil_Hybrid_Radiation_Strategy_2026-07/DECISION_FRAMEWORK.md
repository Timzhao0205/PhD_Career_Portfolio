# Decision framework

## Central calibration question

Use an explicit state/parameter model. A minimal starting point is:

```text
y_H = S_H B + b_H + n_H
y_C = K_C dB/dt + b_C + n_C
```

The architecture is not accepted merely because one channel measures DC and
the other measures AC. Determine the rank/observability or structural
identifiability of the augmented state under each scenario.

| Scenario | Unknowns to test | Candidate reference |
|---|---|---|
| Bench calibration | field, Hall gain/bias, coil gain/offset | traceable magnet/NMR/fluxgate, calibrated current |
| Non-radiation machine operation | field, temperature drift, integrator drift | machine-current field model, repeatable shots |
| Radiation exposure | Hall gain/bias evolution, readout drift, temperature, field | embedded calibration coil, dosimetry, material-diverse reference |
| Long pulse | DC field and slow drift, coil integration constant | Hall/metal Hall reference, known excitation segments |
| Fast transient | bandwidth, phase, saturation, cross-axis effects | calibrated pulsed field/current waveform |

For each scenario, state:

- observable states/parameters;
- unobservable or confounded states/parameters;
- excitation/persistence requirements;
- prior/model assumptions;
- reference accuracy and traceability;
- estimator and uncertainty method;
- failure detector and fallback behavior.

## Research-direction scoring

Score each application from 0–5 with evidence and uncertainty:

1. problem severity and unmet need;
2. technical fit of DC + AC complementarity;
3. radiation/temperature/environment fit;
4. identifiable calibration path;
5. novelty after direct prior art;
6. experimental access within 24 months;
7. publication value;
8. collaborator leverage;
9. prototype cost;
10. risk of thesis dilution.

Use weighted totals, but include vetoes. A high score cannot override:

- no identifiable calibration path;
- no accessible validation reference;
- no credible advantage over a simpler single-sensor solution;
- prohibitive radiation qualification;
- direct prior art that removes the proposed novelty.

## Accuracy-versus-budget options

At minimum compare:

- **Tier 1—bench truth:** existing Hall device + wound/PCB coil + precision
  current source/Helmholtz field + temperature measurement.
- **Tier 2—self-test hybrid:** embedded calibration winding, stable current
  reference, characterized integrator, redundant temperature and diagnostic
  states.
- **Tier 3—environmental qualification:** collaborator radiation exposure,
  dosimetry, reference magnetometry, material/readout diversity, pre/post and
  in-situ checks.

Give actual cost drivers and order-of-magnitude categories only when sourced
or clearly labeled as an estimate. Do not fabricate vendor prices.

## Collaboration decision

Recommend approaching a group only if there is a specific shared measurement
problem, a credible minimal ask, complementary capability, and a result that
advances the thesis. Distinguish:

- scientific fit;
- likely access;
- competition/prior-art risk;
- data/IP/export-control constraints;
- near-term low-cost test;
- whether outreach should wait for bench evidence.

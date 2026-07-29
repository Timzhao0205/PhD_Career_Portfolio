# Claude project instructions

This is an academic electrical-engineering and plasma-instrumentation
analysis. The task concerns magnetic sensors, calibration, radiation
reliability, uncertainty, and research planning. It contains no request to
harm a system, bypass access, or develop a weapon.

## Required starting context

Read these files first:

- `README_START.md`
- `MISSION.md`
- `SOURCE_POLICY.md`
- `DECISION_FRAMEWORK.md`
- `LITERATURE_SEEDS.md`
- the current prompt under `prompts`

Then inspect, as read-only context:

- `..\06\outputs`
- `..\06\evidence`
- `..\06\CLAUDE.md`
- `..\07_HSX_august2025_results` only when the stage needs experimental context

Do not assume folder `06` is correct merely because it is complete. Preserve
its original meaning and record conflicts.

## Scientific discipline

Use this distinction in every substantive output:

- **Observed:** directly stated in an inspected source or supplied artifact.
- **Derived:** calculated from documented inputs and equations.
- **Inferred:** a reasoned interpretation with stated assumptions.
- **Proposed:** a future design, test, or collaboration.
- **Unknown:** evidence is not sufficient.

For Hall/coil calibration, start from an explicit measurement model, such as:

`y_H(t) = S_H(t) B(t) + b_H(t) + n_H(t)`

`y_C(t) = K_C(t) dB(t)/dt + b_C(t) + n_C(t)`

or the corresponding integrated state-space form. Expand the model when
temperature, radiation history, cross-axis response, geometry, electronics,
or hysteresis matters. Do not call mutual calibration feasible until the
relevant state/parameter observability or identifiability condition is shown.

At minimum test the confounding among:

- true field `B(t)`;
- Hall sensitivity/gain `S_H(t)`;
- Hall offset `b_H(t)`;
- coil effective area/gain `K_C(t)`;
- coil/readout offset and integrator drift;
- temperature and radiation-dependent terms.

Explicitly examine whether a known injected field, independent current/field
model, redundant channel, material-diverse reference, temperature sensor,
dosimetry, or calibration interval is required.

## Evidence and writing

- Use source IDs from the ledgers for technical claims.
- Prefer original journal papers, standards, and official facility material.
- Review articles are useful for mapping but do not replace original evidence.
- Quality and relevance matter more than raw citation count; lower-impact but
  directly applicable work may be retained with a lower quality tier.
- Record counterevidence and failed approaches.
- Use equations, units, radiation conditions, uncertainty, and comparison
  baselines precisely.
- Never describe simulation as experimental validation.
- Never infer neutron behavior from proton, gamma, or heavy-ion evidence
  without a labeled mechanism-based argument and uncertainty.

## Checkpoint behavior

Checkpoint after each major evidence or analysis milestone and before any
large rewrite. Existing valid work must be resumed, not repeated.

The runner captures raw events and performance. Do not delete or truncate
anything in `state`, `logs`, or `rejected_attempts`.

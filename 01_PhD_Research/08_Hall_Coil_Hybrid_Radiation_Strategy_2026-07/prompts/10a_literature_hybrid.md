# Stage 10A — additional Hall + coil hybrid literature

## Goal

Build a verified evidence lane on complementary Hall/inductive sensing,
integrator drift, sensor fusion, calibration, self-test actuation, and
long-duration magnetic diagnostics. This must extend, not relabel, folder `06`.

## Search domains

- direct Hall + inductive/B-dot/Mirnov hybrid sensors;
- coil integration and drift correction;
- Kalman, Luenberger, complementary, Bayesian, or unknown-input observers;
- DC/low-frequency absolute references combined with AC/high-bandwidth coils;
- Rogowski/current probes with independent references;
- calibration windings, embedded actuators, field markers, current-model
  references, and online self-test;
- fusion/plasma and other high-field applications where the architecture is
  technically transferable;
- uncertainty, timing/phase, bandwidth overlap, geometry, cross-axis,
  saturation, and fault detection.

Begin with the direct seeds. Follow backward/forward citations, especially the
2007 self-diagnostic paper, 2022 JET hybrid paper, 2022 Kalman integration
paper, and both 2025 direct fusion papers.

## Required discrimination

For every source classify its role in `topic_tags` and `notes`:

- `direct_hybrid`;
- `calibration_or_observer`;
- `coil_or_integrator`;
- `hall_reference`;
- `enabling_only`;
- `context_only`.

Identify what each direct paper actually estimates: true field, coil bias,
integrator drift, Hall offset, Hall sensitivity, coil gain, or another
quantity. Do not describe coil-drift correction as proof of radiation-induced
Hall-sensitivity calibration.

## Outputs

1. `evidence\10A_HYBRID_SOURCES.csv`
   - exact shared ledger header;
   - at least 40 unique verified peer-reviewed rows;
   - non-counting discovery records may remain with honest status.
2. `evidence\10A_HYBRID_SYNTHESIS.md`
   - search strategy and databases/domains;
   - direct-prior-art timeline;
   - table of measured/estimated states and references;
   - achieved performance and validation type;
   - unresolved identifiability questions;
   - implications for novelty and the user's proposed sequence;
   - source-ID citations throughout.

## Acceptance

- 40 verified peer-reviewed unique sources minimum.
- DOI and normalized-title duplicates removed.
- Direct evidence is clearly separated from enabling/contextual evidence.
- Claims based only on abstracts/metadata are bounded accordingly.
- The synthesis includes counterevidence and at least five material
  limitations of prior hybrid work.

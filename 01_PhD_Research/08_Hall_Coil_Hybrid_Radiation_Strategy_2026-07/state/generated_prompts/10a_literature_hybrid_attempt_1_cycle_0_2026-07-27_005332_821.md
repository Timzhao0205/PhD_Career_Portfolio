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


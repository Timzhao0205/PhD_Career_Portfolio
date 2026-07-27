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

# Stage 10B — radiation, temperature, and reliability literature

## Goal

Determine what is actually known about radiation-induced changes in Hall
sensors and every other hybrid measurement-chain element, with conditions
precise enough to support a compensation strategy.

## Evidence layers

1. Direct Hall-device irradiation:
   - neutron spectra and fluence;
   - gamma/TID;
   - proton/electron/heavy-ion evidence;
   - InSb, InAs, GaAs, Si, SOI, GaN/AlGaN/AlN, metallic/ceramic, and other
     justified candidate technologies.
2. Enabling device/material physics:
   - mobility/carrier-density/contact/resistance change;
   - displacement damage, ionization, transmutation, annealing;
   - temperature–radiation interaction.
3. Measurement chain:
   - Hall bias/current source, analog front end, ADC, cabling, packaging;
   - coil conductor/insulation/effective area;
   - integrator and timing/reference electronics.
4. Fusion qualification and calibration practice:
   - ITER/JET/DEMO and long-duration magnetic diagnostics;
   - pre-, in-, and post-irradiation calibration;
   - dose/fluence monitoring and uncertainty.

## Required extraction

For each direct radiation paper, put the following in `claims_supported` or
`notes` when available:

- species/spectrum;
- dose or fluence and units;
- temperature and bias state;
- annealing/time after exposure;
- device material/structure;
- quantity changed and direction/magnitude;
- measurement reference and uncertainty;
- whether the change was reversible, persistent, or not measured.

Do not infer missing conditions. Do not merge proton and neutron behavior.
Distinguish sensitivity, offset, resistance, mobility, noise, linearity,
cross-axis response, hysteresis, and outright failure.

## Outputs

1. `evidence\10B_RADIATION_SOURCES.csv`
   - exact shared ledger header;
   - at least 45 unique verified peer-reviewed rows.
2. `evidence\10B_RADIATION_SYNTHESIS.md`
   - mechanism/condition matrix;
   - material/device comparison;
   - measurement-chain failure pathways;
   - what can be modeled, monitored, calibrated, or only bounded;
   - evidence gaps for fusion-relevant neutron/gamma conditions;
   - source-ID citations.

## Acceptance

- 45 verified peer-reviewed unique sources minimum.
- At least 15 direct Hall-device or Hall-system irradiation/qualification
  sources if the literature permits; if not, document the verified maximum and
  the exact gap rather than padding.
- Radiation species, spectrum, dose/fluence, temperature, and access level are
  not silently conflated.
- Evidence on sensor material is separated from evidence on electronics.
- Contradictory results and plausible causes are retained.


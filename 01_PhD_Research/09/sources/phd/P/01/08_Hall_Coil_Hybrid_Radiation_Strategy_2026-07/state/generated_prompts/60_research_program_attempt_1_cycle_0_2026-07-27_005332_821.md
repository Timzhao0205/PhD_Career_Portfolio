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

# Stage 60 — Fable integrated research program and decision gates

## Goal

Choose the recommended sequence, scope, budget, and collaboration timing for
the user's PhD. Fable 5 must produce the accepted final main response.

## Core sequence to test

Evaluate—not merely repeat:

1. Hall device validation and metrology.
2. Hybrid Hall + inductive coil.
3. Reusable module, estimator, and simulation/validation package.

Consider alternatives:

- run an early low-cost identifiability/bench hybrid test before deep Hall
  radiation work;
- develop embedded calibration actuation with the Hall device from the start;
- use a radiation-hard Hall reference rather than compensating a sensitive
  device;
- defer radiation to a collaborator/coauthored work package;
- abandon the hybrid if a simpler diagnostic meets the chosen use case.

## Required program

Define phased work with objective entry/exit gates:

- Phase 0: evidence/novelty/identifiability closure.
- Phase 1: Hall bench validation and uncertainty budget.
- Phase 2: coil/integrator characterization and hybrid observer.
- Phase 3: long-duration, temperature, and injected-drift validation.
- Phase 4: radiation screening/qualification only after earlier gates.
- Phase 5: selected application/collaborator demonstration.
- Phase 6: reusable research module/simulation package and publication.

For each phase provide deliverables, reference instrument, acceptance metrics,
estimated cost category, time range, dependencies, collaborator need,
publication value, and stop/pivot rule. Integrate with the existing folder
`06` PhD strategy and avoid derailing current first-author HSX work.

## Budget tiers

Give:

- minimum defensible;
- balanced/recommended;
- high-accuracy/collaborator-enabled.

Use sourced prices only; otherwise list cost drivers and relative categories.
Identify what accuracy is lost at each lower tier and which evidence gap makes
an upgrade necessary.

## Outputs

1. `outputs\06_INTEGRATED_RESEARCH_PROGRAM.md`
   - direct conclusion on the user's three-step interpretation;
   - recommended architecture/research claim;
   - phases, resources, publications, collaboration timing;
   - accuracy/budget tiers;
   - scope boundaries and kill criteria.
2. `outputs\06_DECISION_GATES_AND_ROADMAP.md`
   - ordered gates, dependencies, pass/fail/pivot paths, checkpoints, and
     resume-ready next tasks.
3. `outputs\06_ADVISOR_MEETING_BRIEF.md`
   - one concise meeting brief with the decision requested, evidence,
     unresolved risks, lowest-cost next experiment, and questions for the
     advisor.

## Acceptance

- The program may confirm, refine, reorder, or reject the original sequence,
  but its rationale follows Stages 20–50.
- Radiation is not silently added to the immediate HSX critical path.
- Every expensive step has a preceding cheaper falsification gate.
- Collaboration recommendations specify when to approach and what evidence to
  bring.
- The module/simulation deliverable has a realistic position in the PhD, not
  an open-ended software project.


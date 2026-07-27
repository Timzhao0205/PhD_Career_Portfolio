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

# Stage 00 — inventory, hypothesis, and requirements trace

## Goal

Reconstruct exactly what the user is asking, what option 2 in folder `06`
actually proposed, and which prior conclusions or scope rules constrain this
new analysis.

## Work

Inspect:

- all policies and prompts in this mission;
- folder `06` final strategy, action plan, research-direction decision,
  literature review, source coverage, roadmap, red team, and final audit;
- folder `06` CLAUDE/mission scope;
- folder `07` at file/inventory level, opening only the most relevant context;
- parent launchers and root instructions for conflicts.

Do not modify any inspected sibling file.

Explicitly test the user's interpretation:

1. Hall sensor/device validation and metrology first.
2. Hybridization with an inductive coil second.
3. Reusable module and simulation package third.

Record whether folder `06` stated that sequence, merely implied it, or left it
ambiguous. Separate reconstruction from the new recommendation, which later
stages will make.

Identify every requirement in the current user request:

- additional hybrid literature;
- radiation sensitivity/bias/compensation;
- bidirectional calibration hypothesis;
- application/group strategy;
- limitations and comparison;
- accuracy/budget;
- model/effort routing;
- performance logs;
- two-strike Fable behavior;
- checkpoints, run/resume, and full package.

## Outputs

1. `outputs\00_INPUT_INVENTORY.md`
   - inspected paths and purpose;
   - option-2 reconstruction with quotations kept short;
   - existing evidence and missing evidence;
   - read-only/write boundary;
   - scope caveat: no claim of radiation testing.
2. `outputs\00_REQUIREMENTS_TRACE.csv`
   - columns:
     `requirement_id,user_requirement,interpretation,stage,deliverable,acceptance_test,status,notes`
   - one or more rows for every requirement above.
3. `outputs\00_CONFLICT_LEDGER.md`
   - conflicts among root instructions, folder `06`, current request, source
     policies, and practical constraints;
   - resolution and rationale for each.

## Acceptance

- No sibling file changed.
- The option-2 interpretation is classified as confirmed, partly confirmed,
  or not confirmed, with file evidence.
- All current requirements trace to a later output and objective test.
- No new technical conclusion is asserted without labeling it preliminary.


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

# Stage 10D — Fable evidence merge and literature conclusions

## Goal

Personally verify, deduplicate, reconcile, and synthesize the three evidence
lanes into a decision-grade evidence base. Fable 5 must produce the accepted
final main response for this stage.

## Work

Read all lane CSVs/syntheses and folder `06\outputs\01_SOURCE_LEDGER.csv`.
Independently spot-check publisher/DOI records, every tier-A source, all direct
Hall+coil papers, all central radiation papers, and any metadata conflict.

Deduplicate across lanes by normalized DOI and title. Merge topic tags and
claims without exaggerating access. Re-evaluate quality tiers based on direct
relevance and design quality—not prestige alone.

Build the final ledger with:

- at least 120 verified peer-reviewed unique sources;
- at least 75 new relative to folder `06`;
- at least 25 hybrid/coil, 30 radiation, 25 applications/alternatives, and 20
  calibration/observability sources.

Do not pad. If a gate genuinely cannot be met, do more research. If the
literature itself is too sparse, explicitly fail the stage and document the
verified maximum rather than relabel unrelated papers.

## Outputs

1. `outputs\01_SOURCE_LEDGER.csv`
   - exact shared ledger header and all gates above.
2. `outputs\01_NEW_SOURCE_AUDIT.csv`
   - columns:
     `source_id,normalized_doi,normalized_title,found_in_folder_06,evidence,new_source_flag`
3. `outputs\01_EVIDENCE_MAP.csv`
   - columns:
     `claim_id,claim,claim_type,source_ids,evidence_strength,counterevidence_ids,limitations,used_by_stage`
4. `outputs\01_SOURCE_COVERAGE.md`
   - counts by status, tier, topic, year, access level, evidence role, and
     new/reused status;
   - deduplication method and unresolved gaps.
5. `outputs\01_HYBRID_LITERATURE_REVIEW.md`
   - direct prior art, what has been demonstrated, what remains unproven, and
     novelty constraints.
6. `outputs\01_RADIATION_LITERATURE_REVIEW.md`
   - radiation mechanism/condition synthesis and calibration implications.
7. `outputs\01_APPLICATIONS_ALTERNATIVES_REVIEW.md`
   - application needs and incumbent/alternative evidence, without yet
     finalizing outreach priority.

## Acceptance

- All numeric, schema, uniqueness, and new-source gates pass.
- Every major literature conclusion cites final-ledger source IDs.
- Direct evidence, mechanism-based inference, and proposal are visibly
  distinct.
- The reviews explicitly state that existing Hall+coil drift correction does
  not automatically prove in-situ Hall radiation-sensitivity calibration.
- Fable re-checks the work rather than merely approving lane summaries.


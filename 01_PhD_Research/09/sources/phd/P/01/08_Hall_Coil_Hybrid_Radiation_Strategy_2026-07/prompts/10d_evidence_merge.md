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

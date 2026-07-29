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

# Stage 40 — application and collaboration prioritization

## Goal

Determine where the hybrid architecture is worth pursuing and whether/when to
approach another group. Do not send outreach.

## Applications

Evaluate at least:

- tokamak long-pulse/plasma magnetic diagnostics;
- stellarator field mapping, alignment/error field, and coil-current/field
  validation;
- z-pinch/pulsed-power current and field measurements;
- magneto-inertial fusion/plasma-jet experiments;
- superconducting magnets, HTS rotating machinery, motors/generators;
- one additional evidence-supported application.

Use Stage 20 and 30 vetoes. An application with no identifiable calibration
path or no advantage over a simpler sensor cannot win on market size alone.

## Candidate groups

For each serious application, identify current candidate research groups or
facilities from official webpages and directly relevant peer-reviewed work.
Include, when evidence supports them, groups around KSTAR/KFE, ITER/JET/DEMO
magnetics, PPPL/tokamak/stellarator, Sandia pulsed power/Z/Mykonos, LANL
plasma-jet/MIF, and relevant HTS/machine programs. Do not add a famous lab
without a specific technical fit.

Assess:

- what unique capability/data/facility the group has;
- what the user can contribute now;
- minimal low-burden collaboration ask;
- evidence/package needed before approach;
- access/probability uncertainty;
- competition, overlap, IP, safety, export-control, or publication risk;
- whether the relationship advances or dilutes the PhD.

No personal/private contact details. No outreach.

## Outputs

1. `outputs\04_APPLICATION_SCORECARD.csv`
   - columns:
     `application,problem,incumbent_diagnostic,hybrid_value,identifiability_path,radiation_fit,experimental_access,publication_value,collaboration_leverage,prototype_cost,thesis_dilution_risk,technical_score,strategic_score,veto,evidence_ids,rank,recommendation,next_gate`
   - show scoring scale/weights in notes or the collaboration document.
2. `outputs\04_COLLABORATION_STRATEGY.md`
   - ranked application recommendation;
   - approach-now / approach-after-bench-proof / monitor / do-not-prioritize;
   - staged outreach prerequisites and a non-sent outline of the scientific
     ask;
   - risks and fallback path.
3. `outputs\04_COLLABORATOR_CANDIDATES.csv`
   - columns:
     `rank,group_or_facility,institution,application,official_url,relevant_publication_ids,unique_capability,proposed_scientific_ask,prerequisites,access_uncertainty,competition_or_ip_risk,phd_fit,recommendation,notes`

## Acceptance

- All user-named application classes receive evidence-based judgments.
- Scores do not override technical vetoes.
- Candidate status is current and linked to official pages.
- Each approach recommendation has a concrete scientific ask and prerequisite.
- No contact or external write occurs.


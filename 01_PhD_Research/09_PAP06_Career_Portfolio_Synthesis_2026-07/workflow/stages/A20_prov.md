# A20 — historical Fable provenance audit

Audit whether the ideas and later artifacts in the old Folder 06 were generated
with Fable 5 at high or xhigh effort. Historical provenance and fresh agreement
are separate questions.

Inspect:

- extracted old Folder 06 under `sources/old06`
- `evidence/SOURCE_MANIFEST.json` (historical CLAUDE/AGENTS files are available at
  their recorded inert working paths, such as `_claude_source` directories and
  filenames ending in `.source.txt`)
- `sources/history/prev_chat.md`
- attachment hashes and duplicate facts in `evidence/SOURCE_MANIFEST.json`
- A10 only for its accepted status; do not use its ranking to infer
  historical authorship

Inventory every model/effort log, state file, session record, audit statement,
prompt, handoff, and artifact lineage marker. Reconcile contradictions using
the strongest evidence available. Do not claim that filename text, a prompt
request, or stylistic similarity proves the runtime model.

Required full outputs:

- `TASKS.csv`: one row per identifiable idea-generation/adjudication/screening/
  repair/deep-dive/synthesis task with task_id, artifact_scope, requested_model,
  requested_effort, observed_model, observed_effort, evidence_path,
  evidence_strength, downgrade, and verdict.
- `PROVENANCE.json`: counts plus separate verdicts for (a) raw idea-generation
  core, (b) adjudication/screening, and (c) all later Folder 06 artifacts.
  Allowed verdicts are `CONFIRMED`, `PARTIAL_PROVENANCE`, `CONTRADICTED`, and
  `UNKNOWN`. Include explicit coverage numerator/denominator and missing proof.
- `PROVENANCE.md`: plain explanation of what is and is not provable.

Pilot: audit two clearly logged core tasks and two later artifacts. Use the
same filenames and label them as a non-final sample.

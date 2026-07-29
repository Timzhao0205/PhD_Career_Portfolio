# A10 — blind Fable reconstruction

Purpose: independently generate a 24-idea shortlist from the 126 raw P3R2
candidates without seeing old or new rankings. This is fresh idea-selection
verification, not a historical provenance claim.

Allowed evidence for this stage:

- `blind/MANIFEST.json`
- `blind/POOL_1.json`
- `blind/POOL_2.json`
- `blind/POOL_3.json`
- root policy files

Do not read `src`, `inputs/history.md`, any old/new output, any stage output, or
any prior ranking. Do not web search in this blind stage.

Evaluate every one of the 126 unique IDs using an explicit, decision-relevant
rubric: severity and budgeted buyer pain, technical feasibility, defensible
edge, founder/PhD adjacency without circularly assuming it, capital/time to
falsification, 2030–2034 timing, geographic portability, regulatory/safety
friction, and failure modes. Avoid false precision; include reasons and
uncertainty.

Required full outputs:

- `SELECTION.json`: exactly 24 unique objects with rank 1–24, idea_id, concept,
  decision, evidence_from_candidate, score components, uncertainty, principal
  risk, and falsifier.
- `TOP10.json`: exactly 10 unique IDs, all contained in the 24.
- `METHOD.md`: coverage proof for 126/126, rubric, tie handling, limitations,
  and a statement that rankings were not read.

Pilot: process a deterministic sample of 6 IDs (first two in each shard), put
the best 3 of those 6 in `TOP10.json`, write the same three filenames, and label
every file `PILOT SAMPLE — NOT FINAL`.

# Stage 30 — manuscript, reviewer, and publication-route audit

Audit the submitted paper against the authoritative decision letter, source
files, supplied HSX data, and the verified literature.

Create `outputs/03_REVIEWER_RESPONSE_MATRIX.csv` with header:

```text
comment_id,source,comment_summary,underlying_issue,current_manuscript_location,current_evidence_status,can_fix_without_new_data,required_action,proposed_evidence_or_analysis,publication_route_relevance,priority,disposition,notes
```

Give every distinct Associate Editor, Reviewer 1, and Reviewer 2 concern its
own row. Cover novelty, absolute magnetic-field output, calibration,
repeatability/fabrication iterations, conventional-probe comparison,
bandwidth basis, parasitics/packaging, GaN literature comparison, figure
presentation, and cited Mirnov reference.

Create `outputs/03_MANUSCRIPT_DIAGNOSIS.md` containing:

- claim-by-claim audit of title, abstract, introduction, methods, results,
  figures, conclusion, and references;
- exact claims supported now, claims requiring qualification, and claims
  requiring new data;
- novelty comparison dimensions for a GaN-sensor table;
- analysis that can be recovered from supplied data versus data that does not
  exist;
- statistical/repeatability and calibration gaps;
- bandwidth and parasitic evidence gap;
- concise revision map, without editing the manuscript itself.

Create `outputs/03_PUBLICATION_ROUTE_DECISION.md` comparing:

- a new/revised Sensors Letters submission following the invitation;
- an arXiv preprint based on the current study;
- a full RSI instrument study using the next experiment;
- the user’s proposed arXiv-plus-RSI sequence.

For each route, state minimum evidence, time, page/scope fit, novelty risk,
duplication/overlap risk, pre-publication IP gate, and what not to claim.
Distinguish confirmed journal requirements from inference and cite current
official journal policies. Give one primary recommendation and one fallback.
Do not submit, rewrite, or upload anything.

Next stage: `40_experiment`.

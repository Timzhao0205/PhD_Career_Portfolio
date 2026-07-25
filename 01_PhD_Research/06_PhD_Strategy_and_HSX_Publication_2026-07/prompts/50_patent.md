# Stage 50 — pre-publication candidate-concept and prior-art screen

Screen only concepts grounded in the supplied manuscript, hardware, data,
readout work, vector-probe planning, analysis methods, and recommended
research direction. Do not invent unrelated patent ideas.

Search relevant public patent records and non-patent literature. Patent and
policy sources do not count toward the 150 peer-reviewed-paper minimum.

Create `outputs/05_PRIOR_ART_LEDGER.csv` with header:

```text
art_id,type,title,identifier_or_citation,priority_or_publication_date,assignee_or_authors,url,relevant_features,overlap_with_supplied_work,potential_distinction,evidence_accessed,confidence,notes
```

Create `outputs/05_CANDIDATE_PROTECTABLE_CONCEPTS.md` containing:

- concepts already supported by the supplied work;
- concrete technical feature combinations, not desired outcomes;
- documentary basis and likely contributors, without deciding inventorship;
- closest prior art and overlap;
- potential technical distinctions stated conditionally;
- enablement/data status;
- claim-scope risks, design-around risks, and publication risks;
- rank by evidence maturity and urgency for professional review;
- explicit labels: `RESEARCH SCREEN — NOT LEGAL ADVICE`,
  `NO PATENTABILITY CONCLUSION`, and `NO FREEDOM-TO-OPERATE CONCLUSION`.

Create `outputs/05_DISCLOSURE_HOLD_CHECKLIST.md` with:

- materials to preserve before public disclosure;
- questions for the advisor, collaborators, Stanford OTL, and registered
  patent counsel;
- authorship/inventorship/ownership/sponsor/collaboration questions;
- arXiv, conference, manuscript, presentation, repository, and public-demo
  disclosure gates;
- sequence and decision owner, without sending a disclosure or contacting
  anyone;
- current official Stanford/USPTO/WIPO policy links, with dates and a warning
  that policies/law can change.

Never state that a concept “is patentable,” that Stanford or the student owns
it, or that a filing should occur without counsel review.

Next stage: `60_timeline`.

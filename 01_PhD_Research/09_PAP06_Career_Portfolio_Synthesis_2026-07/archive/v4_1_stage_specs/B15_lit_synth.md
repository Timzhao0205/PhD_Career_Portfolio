# B15 — Fable literature synthesis and evidence adjudication

Independently inspect B12's records, publisher pages, source publications where
accessible, B10's PhD claims, and the relevant source artifacts. Correct
support-stage mistakes before accepting evidence. This is the critical
Fable 5/xhigh literature judgment for Operation B.

Do not reward citation count or venue reputation by itself. Judge claim-level
evidence using study design, calibration traceability, uncertainty reporting,
sample/experiment conditions, controls, independent replication, relevance to
the proposed use, and disclosed limitations. Separate review-paper conclusions
from underlying primary experiments. Do not treat absence from this search as
proof that no prior work exists.

Adjudicate the four streams from B12 and their cross-stream implications:

- what the PhD direction has already established versus what literature only
  suggests;
- what is directly transferable to startup work, what is enabling
  infrastructure, and what is only a loose skill analogy;
- what literature supports or contradicts the Hall/coil hybrid architecture;
- what specialized power-converter, power-electronics, or power-supply work
  genuinely benefits from the PhD direction;
- novelty gaps, boundary conditions, negative results, unresolved
  contradictions, and decisive bridge experiments.

Required full outputs:

- `EVIDENCE_MAP.csv`: evidence_id,topic_stream,claim,support_direction,
  paper_ids,study_types,conditions,measurement_quality,consistency,
  evidence_strength,limitations,phd_relevance,startup_relevance,
  downstream_use,falsifier. Separate multiple paper IDs with semicolons.
- `LIT_REVIEW.md`: transparent, evidence-weighted synthesis with exact
  paper-ID citations and a clear distinction between established evidence,
  plausible inference, and unknowns.
- `GAPS.md`: contradictions, missing experiments, weakly studied regimes,
  novelty uncertainties, and prioritized bridge tests.
- `SOURCE_AUDIT.json`: ledger_rows,accepted_core_count,
  peer_review_verified_count,journal_count,recent_2020_2026_count,
  topic_counts,duplicate_dois,correction_concern_count,retracted_count,
  inaccessible_count,unresolved_count,accepted_paper_ids,limitations.
  `accepted_paper_ids` must contain every and only B12 `accepted_core` ID.
  `topic_counts` must report accepted-core counts by the four exact stream
  names, and `recent_2020_2026_count` must count accepted-core papers only.
- `SOURCES.csv`: claim_id,url,title,publisher,published_date,accessed_date,
  source_type,stage_file,confidence,limitation.

The full evidence map must contain at least 30 distinct claim rows spanning all
four streams. Accepted synthesis must use at least 48 verified peer-reviewed
core papers, with at least eight per stream. Retracted publications cannot
support accepted claims. Papers with unresolved correction or peer-review
status may appear only as limitations.

Pilot: adjudicate all eight B12 pilot papers and create at least eight evidence
rows covering every stream. Confirm or correct B12's classifications, include
one contradiction or evidence gap, and produce all five non-final files.

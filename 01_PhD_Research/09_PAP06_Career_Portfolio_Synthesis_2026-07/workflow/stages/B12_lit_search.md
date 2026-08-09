# B12 — peer-reviewed literature search and screening

Build the auditable evidence corpus that Operation B will use. This is a
support stage: locate, verify, de-duplicate, and classify publications, but do
not decide startup rankings, claim novelty, or make the final synthesis.

Use B10 to frame the questions without accepting its inferences as facts.
Search publisher sites, Crossref/DOI records, scholarly indexes, and reference
lists. Search snippets, AI summaries, preprints, theses, magazines, patents,
standards, vendor pages, and non-peer-reviewed reports may help discovery, but
they are not accepted-core peer-reviewed publications.

Use a PRISMA-inspired, reproducible protocol. Do not call the result a formal
systematic review or meta-analysis unless all corresponding methodological
requirements are actually satisfied. Record searches and exclusions even when
results are negative.

Cover four topic streams:

1. `hall_metrology`: Hall/GaN Hall calibration, hysteresis, drift,
   temperature/radiation effects, traceability, uncertainty, repeatability,
   bandwidth, and noise;
2. `hybrid_diagnostics`: Hall plus inductive-coil sensing, bandwidth/data
   fusion, inverse reconstruction, sensor placement, current imaging, and
   diagnostic validation;
3. `hts_quench_current`: HTS current redistribution, quench detection and
   protection, no-insulation behavior, cryogen-free constraints, and
   measurement/actuation limits;
4. `power_conversion`: specialized converters and supplies, SiC/GaN/WBG,
   gate drive, magnetics, EMI/EMC, thermal/control/protection, HIL,
   qualification, reliability, and current sensing.

Full-run corpus requirements:

- screen enough records to retain 60–100 unique publications in
  `PAPER_LEDGER.csv`;
- mark at least 48 as `accepted_core`;
- every accepted-core row must be a verified peer-reviewed journal research
  article or review article with a publisher landing page and DOI when one
  exists;
- include at least eight accepted-core papers in each topic stream;
- include both seminal older work and at least 16 accepted-core papers from
  2020–2026, including at least two recent papers per topic stream;
- use conference proceedings only as `accepted_supplement` when the specific
  venue's peer-review process is verified;
- check each accepted or supplementary item for correction, expression of
  concern, and retraction status using the publisher record and other
  authoritative metadata;
- never infer peer review merely from an IEEE/Elsevier/Springer/AIP/IOP search
  result, DOI, or professional-looking PDF.

Required outputs:

- `SEARCH_PROTOCOL.md`: research questions, databases/sites, query families,
  date/language boundaries, inclusion/exclusion rules, duplicate handling,
  screening sequence, evidence hierarchy, and limitations.
- `SEARCH_LOG.csv`: query_id,topic_stream,platform,query_text,searched_at_utc,
  result_count,screened_count,notes.
- `PAPER_LEDGER.csv`: paper_id,doi,title,authors,year,venue,publisher,
  publication_type,peer_review_status,publisher_url,topic_stream,relevance,
  evidence_status,access_status,correction_status,retraction_status,notes.
- `EXCLUSIONS.csv`: exclusion_id,title,doi_or_url,stage,reason,topic_stream.
- `FLOW.json`: identified,duplicates_removed,screened,full_text_checked,
  excluded,accepted_core,accepted_supplement,unresolved,topic_counts,notes.

Use stable local IDs `P0001`, `P0002`, and so on. De-duplicate by normalized
DOI first and then title/year. Store DOI as lowercase `10.xxxx/...` without a
`doi:` or URL prefix. Use the exact controlled values `journal_article`,
`review_article`, or `conference_paper` for publication type; `verified` for
accepted peer review; and `accepted_core`, `accepted_supplement`, `excluded`,
or `unresolved` for evidence status. `FLOW.json.accepted_core` must equal the
ledger's `accepted_core` row count. Never fabricate missing metadata.

Pilot: exercise the complete search, verification, correction/retraction, and
de-duplication path on exactly eight retained publications, with at least two
from each topic stream and at least six accepted-core journal papers. Produce
all five files and label them `PILOT SAMPLE — NOT FINAL`.

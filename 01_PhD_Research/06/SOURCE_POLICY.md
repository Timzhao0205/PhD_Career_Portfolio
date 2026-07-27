# Source policy

## The 150-paper minimum

`outputs/01_SOURCE_LEDGER.csv` must contain at least 150 unique sources whose
`peer_review_status` is exactly `verified_peer_reviewed`.

Count only:

- journal articles with a verified journal/publisher record;
- peer-reviewed conference papers when the proceedings and review status are
  verified;
- peer-reviewed review articles.

Do not count:

- arXiv or other preprints;
- patents;
- theses or dissertations;
- vendor/application notes;
- standards;
- books or book chapters unless peer review is independently established;
- news, blogs, university pages, grant pages, or AI summaries;
- a paper whose publication status cannot be verified.

Those sources may appear in separate contextual or prior-art ledgers, but not
in the 150-paper count.

## Required ledger schema

The exact CSV header is:

```text
source_id,citation,title,authors,year,venue,doi,url,source_type,peer_review_status,quality_tier,topic_tags,claims_supported,verification_basis,access_level,notes
```

Rules:

- `source_id` is stable and unique (`S0001`, `S0002`, ...).
- Prefer DOI URLs (`https://doi.org/...`); otherwise use an official publisher
  record.
- `quality_tier` is `A`, `B`, or `C`, with a written rubric in
  `outputs/01_SOURCE_COVERAGE.md`.
- `access_level` is `full_text`, `abstract_metadata`, or `metadata_only`.
- Do not imply full-text review for an abstract-only or metadata-only source.
- `topic_tags` is semicolon-separated and must support coverage auditing.
- Deduplicate by normalized DOI first, then normalized title.

## Quality and breadth

Prioritize established journals, strong field venues, seminal papers, recent
high-quality work, and primary research. The combined ledger must materially
cover:

- AlGaN/GaN and other WBG Hall/device physics;
- Hall-sensor geometry, sensitivity, offset, noise, bandwidth, temperature,
  radiation context, packaging, and calibration;
- magnetic-confinement fusion and plasma magnetic diagnostics;
- stellarator/HSX-relevant field measurement and validation;
- direct sensors versus inductive/B-dot/Mirnov diagnostics and drift;
- uncertainty, repeatability, calibration traceability, and instrumentation;
- low-fabrication novelty through modeling, inverse methods, data fusion,
  signal processing, software, ML/control, or digital-twin methods.

Search until the verified, deduplicated minimum is met. A search result snippet
alone is not verification.

## Citation use

Every material claim in final reports must cite one or more `source_id` values
and include a stable link. Cite the supplied manuscript/data by filename and
page/figure/section rather than assigning them peer-reviewed source IDs.

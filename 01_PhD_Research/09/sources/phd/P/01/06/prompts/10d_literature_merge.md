# Stage 10D — verified 150-paper ledger and integrated review

Merge and rigorously verify the three evidence batches.

Tasks:

1. Read every row in the 10A/10B/10C CSV files.
2. Normalize DOI and title; deduplicate by DOI first and title second.
3. Remove any source whose peer-review status or bibliographic identity is not
   adequately verified.
4. Resolve metadata disagreements from publisher/DOI records.
5. Search for additional peer-reviewed papers if deduplication or verification
   leaves fewer than 150 valid sources or creates a material coverage gap.
6. Assign stable final IDs `S0001`, `S0002`, ... .

Create `outputs/01_SOURCE_LEDGER.csv` with exactly this header and order:

```text
source_id,citation,title,authors,year,venue,doi,url,source_type,peer_review_status,quality_tier,topic_tags,claims_supported,verification_basis,access_level,notes
```

At least 150 unique rows must have
`peer_review_status=verified_peer_reviewed`. Do not include patents, preprints,
standards, webpages, or supplied files in that count.

Create:

- `outputs/01_LITERATURE_REVIEW.md`: integrated, critical synthesis organized
  around the mission questions, with inline `[S####]` citations and stable
  links; distinguish evidence from inference.
- `outputs/01_EVIDENCE_MAP.csv` with header:
  `question_id,question,answer_summary,source_ids,evidence_strength,conflicts,gaps`
- `outputs/01_SOURCE_COVERAGE.md`: count, deduplication method, verification
  method, quality-tier rubric, venue/year/topic distributions, access-level
  distribution, limitations, and a deterministic count statement.

Run your own CSV checks before completion:

- required header and nonempty required fields;
- unique source IDs;
- unique normalized DOI, allowing blanks only when a publisher record
  establishes identity;
- at least 150 verified peer-reviewed rows;
- no `arxiv`, `preprint`, `patent`, `standard`, `webpage`, or `thesis` counted
  as verified peer-reviewed;
- material coverage across every category in `SOURCE_POLICY.md`.

Do not make the final continue/adjust/change recommendation yet.

Next stage: `20_direction`.

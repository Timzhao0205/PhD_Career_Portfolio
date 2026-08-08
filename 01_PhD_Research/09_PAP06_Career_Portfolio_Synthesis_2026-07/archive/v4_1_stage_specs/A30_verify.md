# A30 — independent result verification and old/new comparison

Now unblind. Compare:

1. A10's independent 24 and top 10;
2. the old Folder 06 final selections/rankings;
3. the recently generated Folder 06 package and its canonical release;
4. A20's provenance limits.

Compute exact ID overlap at 24 and 10, additions/removals, order/rank changes,
decision changes, methodological differences, and disagreements. Because IDs
or names may have evolved, distinguish exact-ID overlap from a documented
semantic match; never merge by name alone.

Use fresh web research for the most decision-critical disagreements. Prefer
primary/official sources and capture claim-level provenance. A high overlap is
agreement evidence, not proof of historical authorship or correctness.

Required full outputs:

- `COMPARE.json`: machine-readable old/new/blind membership, pairwise metrics,
  semantic-match ledger, rank deltas, and unresolved issues.
- `COMPARE.md`: complete human comparison, including why top-24 composition or
  ordering changed.
- `VERDICT.md`: calibrated conclusion on agreement, correctness confidence,
  provenance, and which ideas need deeper rerun.
- `SOURCES.csv`: claim_id,url,title,publisher,published_date,accessed_date,
  source_type,stage_file,confidence,limitation.

Pilot: compare six deterministic A10 IDs against old/new records and verify one
material disagreement with at least two primary sources.

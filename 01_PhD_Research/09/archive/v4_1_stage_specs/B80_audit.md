# B80 — independent final audit and release

Audit the complete run before release. Verify input hashes, operation order,
pilot/full checkpoints, output hashes, required schemas, idea counts, ID
consistency, source accessibility/claim mapping, model/effort evidence,
unresolved red-team issues, and consistency between detailed/plain reports.
Recalculate the B12/B15 literature counts; sample publisher records; verify DOI
uniqueness, peer-review classification, correction/retraction handling,
topic-stream coverage, and paper-ID-to-claim mappings. Do not pass a release
that treats discovery-only material as accepted peer-reviewed evidence.

Do not pass if any critical or major issue remains. Correct release copies only
when the underlying validated stage evidence supports the correction; record
every change.

Required outputs:

- `AUDIT.json`: overall_status, critical_open, major_open, minor_open,
  checkpoint_counts, hash/model/source/count checks, limitations. Full release
  requires `overall_status=PASS`, `critical_open=0`, `major_open=0`.
- `AUDIT.md`: reproducible audit narrative.
- `CHANGELOG.md`: changes made during audit.
- `FINAL/DETAILED.md`, `FINAL/PLAIN.md`, `FINAL/MODEL_REPORT.md`,
  `FINAL/RANKING.csv`, `FINAL/SOURCE_INDEX.csv`: canonical validated copies.
- `FINAL/RELEASE.json`: status, created_at_utc, source_stage, all final file
  hashes, model-policy summary, and remaining minor limitations.

Pilot: audit fixture-sized samples from every required check and construct a
`FINAL` prototype with the same filenames, clearly labeled non-final.

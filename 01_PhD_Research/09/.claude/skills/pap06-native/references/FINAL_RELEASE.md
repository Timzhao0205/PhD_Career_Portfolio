# Final release procedure

B80 is the independent release gate. It must inspect every accepted full stage
and its PASS report, recalculate all consequential counts, sample source
records, reconcile red-team issues, and produce the required `outputs/B80_audit`
artifacts.

Release only when B80's audit says:

- `overall_status=PASS`;
- zero critical issues open;
- zero major issues open;
- all 15 pilots and 15 full runs are accepted;
- all 15 full runs have independent PASS reports;
- Operation A and Operation B ordering is intact;
- literature, idea, ID, and source counts meet their stage rules;
- detailed/plain/model/source/ranking files agree.

The canonical deliverables are the files under the accepted B80 candidate's
`FINAL/` directory. Write `state/RUN_COMPLETE.md` with their paths, completion
time if available, model-evidence limitations, unresolved minor limitations,
and the exact reading order.

If B80 fails, return to the earliest affected stage, create a fresh repair
attempt, independently reverify it, and rerun downstream stages whose
conclusions materially depend on the change. Preserve the audit trail.

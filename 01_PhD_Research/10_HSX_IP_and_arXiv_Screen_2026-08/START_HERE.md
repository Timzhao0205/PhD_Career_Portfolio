# Autonomous run contract

The parent session is Claude Fable 5 at xhigh effort. Complete this workflow
with minimal user interaction and durable resume state.

1. Immediately read `CLAUDE.md`, `IP_SCOPE.md`, `MODEL_PLAN.md`,
   `SOURCE_POLICY.md`, and `schemas/OUTPUT_GATES.md`.
2. Before other analysis, set `session_started` to `true`, set status to
   `RUNNING`, create a UTC `run_id`, and append a start entry to the work log.
3. Inventory only the supplied manuscript artifacts and record their hashes.
4. Run stages 00 through 70 sequentially using the exact named agents and model
   assignments in `MODEL_PLAN.md`. Give each agent its stage outcome, not a
   micromanaged chain of steps.
5. Validate each stage against `schemas/OUTPUT_GATES.md`. A failed output gate is
   repaired by the same assigned model; it is not a reason to discard other
   stages or demand a new package.
6. After acceptance, create `state/checkpoints/XX_done.json`, update state and
   logs, and proceed automatically.
7. If interrupted, the next `START.ps1` resumes the named session. Read the
   newest checkpoint and continue from the first incomplete stage.
8. Finish only when all required output files exist, every critical conclusion
   is cited, Fable stages passed the integrity policy, and the final result is
   written by `s70-final` on Fable 5/xhigh.

The final on-screen response should point the user to:

- `outputs/70_FINAL_OTL_BRIEF.md`
- `outputs/70_EXEC_SUMMARY.md`
- `outputs/70_MODEL_REPORT.md`
- `outputs/50_ARXIV_RISK.md`
- `outputs/40_UHV_PACKAGE_VERDICT.md`

Do not ask routine questions. Put unresolved factual questions in the OTL brief
as evidence requests. Pause only for the defined Fable two-strike policy, a
missing indispensable manuscript artifact, or an external access barrier that
materially prevents a defensible conclusion.

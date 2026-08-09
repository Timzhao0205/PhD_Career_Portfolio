# Current independent verification

- Stage: `<stage>`
- Mode: `FULL`
- Candidate: `<exact output candidate path>`
- Report target: `verification/<stage>/FULL_attempt-<N>.md`
- Required files: `<exact list>` plus `RUN_META.md` and `SELF_CHECK.md`
- Stage specification: `<workflow/stages/file.md>`
- Accepted prerequisite outputs: `<exact paths>`
- Worker named agent: `<exact name>`
- Requested worker model/effort: `<exact values>`
- Verifier: `pap06-verifier`
- Requested verifier model/effort: `Fable 5 / xhigh`

Verify independently under the global acceptance rules. Do not edit candidate
outputs. End with exactly `VERDICT: PASS` or `VERDICT: FAIL`.

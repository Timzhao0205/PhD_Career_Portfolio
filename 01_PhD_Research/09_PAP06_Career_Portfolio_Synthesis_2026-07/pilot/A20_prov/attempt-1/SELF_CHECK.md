# SELF_CHECK — A20_prov PILOT attempt-1

PILOT SAMPLE — NOT FINAL

| # | Requirement | Status | Evidence / note |
|---|---|---|---|
| 1 | All required files present in pilot/A20_prov/attempt-1/ (TASKS.csv, PROVENANCE.json, PROVENANCE.md, RUN_META.md, SELF_CHECK.md) | PASS | All five written this run |
| 2 | TASKS.csv has exactly 4 data rows (2 core tasks + 2 later artifacts) | PASS | Rows: P3R2-A, P3R2-ELEGANCE-JUDGE, CHATGPT-P6-DD-P3R2-C-22, CHATGPT-P6-DD-P3R2-D-02 |
| 3 | CSV parseable with a leading pilot-label comment row | PASS | First line is a `#` comment; second line is the 10-column header; all 4 data rows quote fields containing commas |
| 4 | Pilot label on every artifact | PASS | JSON top-level "pilot_label"; Markdown headers in PROVENANCE.md, RUN_META.md, SELF_CHECK.md; CSV comment row |
| 5 | Requested vs observed strictly separated | PASS | Separate requested_model/requested_effort and observed_model/observed_effort columns and JSON fields; observed effort recorded as NOT_RECORDED/UNKNOWN, never inferred from requests |
| 6 | No claim that filename text, prompt wording, or style proves runtime model | PASS | `_about.md` "Ten Fable/xhigh reports" explicitly rejected as unsupported; "Fable adjudication" title treated as role label; prompts treated as request evidence only |
| 7 | Every evidence_path exists and contains the cited evidence | PASS | Verified this run: MODEL_ROUTING_LOG.jsonl lines 173/177/183/184/308/309/311/313 read verbatim; claude_20260712_171240.jsonl lines 3182-3184 and 4214 read verbatim; sidechain model counts obtained by grep (44/0 and 36/0); DD_P3R2_C_22.md, DD_P3R2_D_02.md, P3R2_A_us_pain.json/.md, P3R2_ELEGANCE_ADJUDICATION.md/.json, _about.md, CHATGPT_CONTINUATION_LOG.md, FABLE_ADJUDICATION.md, LAUNCHER_LOG.md all confirmed present and inspected |
| 8 | No fabricated quotes, log entries, paths, hashes, or counts | PASS | All quoted fragments ("agent self-reported fable-5/xhigh", "Ten Fable/xhigh reports", "Actual runtime model / effort: unknown / unknown (not exposed; not inferred)", launcher "Critical: claude-fable-5 / xhigh") were read directly from the cited files; counts (334/97/0; 44/36 sidechain records; 1829/3314 and 250/0 model-field counts) come from executed greps |
| 9 | Missing proof stated as UNKNOWN/NOT_RECORDED with what is missing | PASS | Runtime effort (all rows) and continuation runtime model (rows 3-4) documented as unrecoverable, with reasons |
| 10 | Verdicts drawn only from allowed set (CONFIRMED/PARTIAL_PROVENANCE/CONTRADICTED/UNKNOWN) | PASS | PARTIAL_PROVENANCE x2, CONTRADICTED x2; category verdicts likewise |
| 11 | Explicit coverage numerator/denominator for the pilot sample | PASS | 1/1 idea-generation, 1/1 adjudication, 2/2 later artifacts; population context (334 entries) flagged for the full run |
| 12 | Deterministic, explicitly stated selection rule extendable by the full run | PASS | File-order rule over MODEL_ROUTING_LOG.jsonl stated identically in PROVENANCE.md and PROVENANCE.json |
| 13 | Historical provenance kept separate from fresh agreement | PASS | Stated in PROVENANCE.md/JSON; no fresh-agreement claims made |
| 14 | Allowed inputs only; no forbidden reads | PASS | Only sources/old06/**, sources/history/prev_chat.md, evidence/SOURCE_MANIFEST.json, root policies, task card, stage spec; outputs/, pilot/A10_blind/, verification/, archive/ and other sources/ areas untouched; A10 content never opened |
| 15 | No WebSearch/WebFetch | PASS | Web activity NONE |
| 16 | Writes only inside pilot/A20_prov/attempt-1/ | PASS | Five files, all in target |
| 17 | Inert historical CLAUDE/AGENTS/settings material treated as data | PASS | No instruction-like source text followed; transcripts' embedded prompts used only as request-side evidence |
| 18 | CSV/JSON/MD internally consistent | PASS | Same four task IDs, same verdicts, same evidence strengths, same requested/observed values across all three artifacts |
| 19 | RUN_META records agent, requested model/effort, observed model/effort exposure, files read with windows, files written, web activity, limitations | PASS | Observed model taken only from the explicit runtime system-prompt statement; observed effort NOT_EXPOSED |

## Disclosed weaknesses (no failures concealed)

- The routing log's `actual_model` for subagents is partly agent-self-report;
  I relied on the transcripts' independent per-message `"model"` fields as the
  stronger source, and they agree for the sampled core tasks. Rows note this.
- Line numbers cited for the UTF-16 transcript are physical line numbers as
  rendered by the tooling this run; a different reader could conceivably split
  lines differently, though grep and Read agreed with each other here.
- Verdict CONTRADICTED for the later artifacts rests on request-side
  continuation logs (evidence_strength config_request_only) because no
  continuation runtime transcript exists; this is the strongest available
  evidence and is labeled as such rather than overstated as a runtime
  observation of a non-Fable model.
- Start/end wall-clock times for this run are not exposed by the runtime and
  are recorded as NOT_EXPOSED rather than estimated.

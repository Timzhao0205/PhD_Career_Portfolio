# Error, retry, and limitation log

- 2026-07-28 — B00_inventory PILOT attempt-1 REJECTED (content-quality
  labeling defect, not a model event). Error class: pilot labeling rubric
  violation. Evidence: `pilot/B00_inventory/attempt-1/RUN_META.md` lacks the
  required `PILOT SAMPLE — NOT FINAL` banner (grep matched the label in only
  5 of 6 artifacts); ACCEPTANCE.md requires every pilot artifact labeled, and
  all previously accepted pilots (A10/A20/A30) labeled RUN_META.md. All other
  rubric items appeared compliant. Action: attempt-1 preserved unmodified;
  fresh pap06-sonnet-high worker delegated to `pilot/B00_inventory/attempt-2/`
  with exact repair notes (may carry forward attempt-1 content after
  re-verifying it, adding the missing label everywhere). Outcome: attempt-2
  ACCEPTED 2026-07-28 — all six artifacts labeled (controller grep: 6/6
  files), carried content re-verified, plus one precision correction and one
  newly found conflict (startup 689 vs 690 unique-source count) recorded.

- 2026-07-28 — B00_inventory FULL attempt-1 FAILED independent verification
  (verification/B00_inventory/FULL_attempt-1.md, VERDICT: FAIL; 2 major, 3
  minor, 0 critical). Error class: false observed counts (content defect, not
  a model event). Major defects to repair in attempt-2:
  1. phd folder-08 outputs count: candidate claims "31 files present,
     confirmed by Glob" (CONFLICTS.md #2, INVENTORY.md, SELF_CHECK.md,
     INPUT_MAP.json key `outputs_present_31_files`; plus inconsistent
     "21-of-31" coverage phrase) — real count is 25 (verifier full Glob);
     candidate's own enumerated list has 25 correct names. Fix to 25
     everywhere; keep the (true) substantive conclusion.
  2. 05_CryoFree disclosures: claimed "7 invention disclosures ID_01-ID_07"
     — real folder holds 6 (ID_01-04, 06, 07; ID_05 absent). Fix to 6 and
     note the gap.
  Minor defects to fix in the same pass: "six domain-frontier surveys
  01...07" wording (7 files; enumeration 11 vs correct 12); "21 gate
  records" phrasing (7 records covering 21 verdicts); "~90 results" for the
  05 tree (actual 83). Action: fresh pap06-sonnet-high worker delegated to
  outputs/B00_inventory/attempt-2 with these exact repairs; fresh verifier
  after. Outcome: pending.

- 2026-07-28 — USER-REQUESTED SHUTDOWN while B00_inventory FULL attempt-2
  repair worker was running. Event class: external interruption (not an
  error, not a budget stop, not a provider safeguard). The controller's
  session exposes no SendMessage/interrupt tool and the user forbade new
  agents, so no in-flight stop signal could be delivered; the worker's
  writes are per-file atomic and confined to outputs/B00_inventory/attempt-2.
  At checkpoint the target held 4 of 6 files (INPUT_MAP.json, INVENTORY.md,
  CONFLICTS.md, SOURCES.csv; RUN_META.md/SELF_CHECK.md absent) — POSSIBLY
  PARTIAL, NOT accepted. Action: full durable checkpoint written to
  state/SHUTDOWN_CHECKPOINT.md; STAGE_LEDGER B00 full set to NEEDS_REVIEW
  with reconciliation instructions. Outcome: the worker COMPLETED NATURALLY
  while the checkpoint was being written — all 6 files present, repairs
  applied per its report (plus a newly disclosed 3-way 05-tree count
  discrepancy: 80 fresh vs ~90 attempt-1 vs 83 verifier). Candidate retained
  COMPLETE BUT UNVERIFIED, NOT accepted; no verifier launched (shutdown
  instruction: no new agents). No background work remains. Resume per
  checkpoint after restart.

- 2026-07-28 — RESUME AND RESOLUTION. Post-shutdown reconciliation clean
  (all accepted proofs on disk; 3 PASS + 1 FAIL reports re-verified). B00
  FULL attempt-2 passed controller pre-check and fresh independent
  verification (verification/B00_inventory/FULL_attempt-2.md, VERDICT:
  PASS, 1 minor non-blocking defect). ACCEPTED. Note for B80: the fresh
  verifier's independent recount adjudicated the 05_CryoFree tree at 80
  files — the attempt-1 FAIL report's own "83" figure was wrong on this
  point (its two major defect findings remain valid and were cured).
  B00_inventory stage closed after 2 pilot attempts and 2 full attempts.

- 2026-07-29 — FABLE 5 USAGE-CREDIT EXHAUSTION during B50_execution FULL
  attempt-1 (worker `pap06-fable-xhigh`, requested Fable 5/xhigh). Error
  class: provider/account usage-credit exhaustion (genuine external
  provider limit per CLAUDE.md — not a package budget/turn/token/time
  threshold, of which none exists; not a model-quality failure; not a
  downgrade decision). Visible evidence: harness task-notification status
  "failed", message: "Agent terminated early due to an API error: You're
  out of usage credits. Run /usage-credits to keep using Fable 5 or /model
  to switch models." The worker's last reported action was "Now
  IP_COLLAB.md.", indicating termination mid-write on that file.
  On-disk result: `outputs/B50_execution/attempt-1/` holds 2 of 6 required
  files (ROADMAP.md, IP_COLLAB.md — the latter possibly truncated);
  RUN_META.md and SELF_CHECK.md were never written; no
  `verification/B50_execution/` directory exists. Action: attempt-1
  preserved unmodified, NOT completed, NOT repaired, NOT accepted by this
  entry. Full durable checkpoint written to `state/SHUTDOWN_CHECKPOINT.md`.
  This entry and the checkpoint were written under Sonnet 5 (user-selected
  via `/model` after the Fable 5 credit exhaustion) as ADMINISTRATIVE
  bookkeeping only — no research content was produced or modified under
  Sonnet; B50's own requested/route model remains Fable 5/xhigh unchanged.
  Outcome: pending — B50_execution FULL must be retried as a fresh
  `outputs/B50_execution/attempt-2/` Fable 5/xhigh worker once Fable 5
  usage is available again, followed by a fresh independent Fable 5/xhigh
  verifier; accept only on `VERDICT: PASS`. Do not resume or repair
  attempt-1 in place.

Do not erase prior entries. Record stage, mode, attempt, time if available,
error class, visible evidence/request ID, action, and outcome.

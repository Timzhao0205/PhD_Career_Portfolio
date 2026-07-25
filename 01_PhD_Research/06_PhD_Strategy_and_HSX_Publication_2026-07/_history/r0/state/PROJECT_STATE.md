# Project state

- Mission status: `IN_PROGRESS`
- Current stage: `10a_literature_gan` — `COMPLETE` (global attempt 4;
  user-authorized retry cycle 1, cycle attempt 2). As with every prior
  attempt at this stage, this file's own "COMPLETE" label reflects this
  attempt's in-session self-report and is NOT to be treated as proof of
  model integrity — only the launcher's own post-hoc `state/OPERATION_LOG.csv`
  entry for this attempt is authoritative for that gate (see correction note
  below, which explains why three prior attempts' identical self-reports
  were each later found false).
- **CORRECTION to this file's own prior entry.** This file previously
  recorded global attempt 3 as `COMPLETE` with an 86-row ledger and the
  claim "0 downgrade events this attempt." That claim was written by
  attempt 3 itself and was **false**: the launcher's own model-integrity
  telemetry (`state/OPERATION_LOG.csv` row `2026-07-24T19:35:49...`,
  `state/MODEL_EFFORT_LOG.csv`, `state/attempts/10a_literature_gan.json`)
  shows attempt 3 (session id `7ead749d-1b19-4813-ae56-10c01d1010d1`) also
  reported `claude-sonnet-5;claude-haiku-4-5-20251001` (a mid-session
  downgrade) and was rejected `model_mismatch`. Its outputs were quarantined
  to
  `logs/run_2026-07-24_185945_717/10a_literature_gan/rejected_attempt_3_outputs/`
  (see that folder's `QUARANTINE_MANIFEST.json`) and were never an accepted
  stage output — this is now the third time in a row (attempts 1, 2, and 3)
  that a session self-reported success/zero-downgrade while the launcher's
  independent telemetry later showed otherwise, so this attempt (4) treats
  its own in-session model self-report as unverified and defers entirely to
  the launcher's post-hoc `state/OPERATION_LOG.csv` record for the actual
  acceptance gate.
- This attempt (global attempt 4, cycle_attempt 2) treated all three prior
  quarantined CSVs (`rejected_attempt_1_outputs`, `rejected_attempt_2_outputs`,
  `rejected_attempt_3_outputs`) strictly as unverified lead lists per the
  retry instructions. Used attempt 3's 86-candidate DOI list as a lead-list
  starting point only; independently re-verified all 86 DOIs this session
  via live Crossref API fetches performed by 6 parallel `model: sonnet`-pinned
  subagents (batched ~14-15 each) — **86/86 resolved, 0
  `NOT_FOUND_OR_MISMATCH`**. Additionally, the lead researcher directly
  (not delegated) fetched live Crossref abstract text for 12 rows whose
  notes depend on abstract-level claims. Rebuilt
  `evidence/10A_GAN_WBG_SOURCES.csv` and `evidence/10A_SYNTHESIS.md` from
  scratch via `state/build_10a_csv_attempt4.py`, using only this session's
  own confirmed fields (not the quarantined draft's verification/
  access-level claims). Validated via `state/validate_10a_csv.py`: 0 errors,
  86 rows, exact 16-column header, 0 duplicates, all controlled-vocabulary
  fields valid.
- Headline finding, independently RE-VERIFIED this session (not accepted on
  trust from attempt 3's claim — confirmed fresh via a live Crossref fetch by
  a batch-1 `model: sonnet` subagent this session): `A0014` (Dowling,
  Alpert, Yalamarthy, Satterthwaite, Kumar, Kock, Ausserlechner, **Senesky**,
  *IEEE Sensors Letters*, 2019, doi:10.1109/lsens.2019.2898157) is confirmed
  genuine Senesky-group prior work (Debbie G. Senesky, Tim's own PhD
  advisor, confirmed as final/senior author) demonstrating four-phase
  current-spinning offset cancellation on the identical AlGaN/GaN 2DEG
  material system as the submitted manuscript, in the same venue, predating
  the manuscript by seven years — corroborating Reviewer 2's novelty concern
  (supplied fact `C010`) with independently verified external evidence. Two
  further independently re-verified rows strengthen this: `A0045` (J.
  Microelectromechanical Systems, 2020) and `A0047` (Hilton Head Workshop,
  2018), both sharing most of the same author cluster. Directly relevant to
  Stage 20's direction decision and any Stage 30 revision; this stage does
  not decide how to respond to it.
- Prior stage 00 summary: All four required outputs
  (`outputs/00_INPUT_INVENTORY.md`, `outputs/00_REQUIREMENTS_TRACE.csv`,
  `outputs/00_CONFLICT_LEDGER.md`, `outputs/00_CLAIM_BASELINE.csv`) written and
  validated. Checkpoint saved at
  `state/checkpoints/CP_00_inventory_20260724-171635.md`. Remains
  `COMPLETE`, unaffected by the stage-10a rejections above.
- Headline finding (stage 00): the "published in 2023" framing in the parent
  `CLAUDE.md`, `01_PhD_Research_Folder_Info.md`, and `05_HSX_ChatGPT_Windows_App`
  is contradicted by controlling evidence (byte-identical PDFs, 2026-07-02
  creation metadata, and the 23-Jul-2026 decline letter). The manuscript
  (`SENSL-26-07-RL-1061`) must be treated as declined-with-invitation-to-revise,
  never published, in every downstream stage. Full evidence in
  `outputs/00_CONFLICT_LEDGER.md` Conflict 1.
- Open items carried forward (not blockers, relevant to later stages):
  undocumented `scope_N.csv`-to-shot-number mapping in the HSX data
  (Conflict 2); unreconciled 1 MHz vs. ~1-2 kHz bandwidth figures across the
  manuscript and project 02 (Conflict 3) — stage 10a's ledger contains no
  AlGaN/GaN-specific bandwidth figure that resolves this either, see
  `evidence/10A_SYNTHESIS.md` Section 4; `inputs/IEEE_submission_bundle_2026-07-02.pdf`
  is password-protected (content unverified); a ~109x amplitude anomaly is
  open in project 02/05 bench readout tests.
- Runtime route: Claude Code in Windows PowerShell only.
- Requested model / effort (stage 10a): Sonnet 5 / Extra High.
- Downgrade count: 3 cumulative from attempts 1-3 (all three quarantined for
  `model_mismatch`; attempt 2's rejection triggered `CHATGPT_HANDOFF_REQUIRED`,
  user authorized retry cycle 1 (attempt 3), attempt 3 was then also
  rejected `model_mismatch`). This attempt (global attempt 4, cycle_attempt 2)
  self-reports 0 downgrade events and `claude-sonnet-5` throughout, with every
  subagent explicitly pinned `model: sonnet`. Per the correction note above,
  this self-report is deliberately NOT presented as proof of model integrity;
  the launcher's own post-hoc `state/OPERATION_LOG.csv`/
  `state/attempts/10a_literature_gan.json` entries for this attempt are the
  actual acceptance-gate record and were not available to read as of this
  write (they are written by the launcher after this response completes).
- Usage check: Manual; the runner does not poll usage.
- Inactivity timeout: Disabled; the user may stop PowerShell manually.
- ChatGPT Windows readiness: `READY_IF_NEEDED`.
- Next action: If the launcher confirms this attempt stayed on the
  requested `sonnet` family (no `model_mismatch`), launch stage
  `10b_literature_fusion` (Sonnet 5 / Extra High). If a mismatch is
  detected post-hoc, this stage's outputs will be quarantined again per
  `CHECKPOINT_PROTOCOL.md` and a further retry/handoff decision made by the
  launcher/user — this file's own "COMPLETE" label should be re-read
  against `state/OPERATION_LOG.csv` before being trusted.
- Updated: 2026-07-24

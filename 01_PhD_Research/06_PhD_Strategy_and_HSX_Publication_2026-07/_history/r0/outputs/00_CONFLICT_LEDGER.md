# 00 — Conflict ledger

Every material contradiction or ambiguity found while building the Stage 00
inventory, recorded without resolving by convenience. Each entry names the
controlling evidence or is explicitly labeled unresolved. Cross-references
`00_INPUT_INVENTORY.md` for full paths and quotes.

---

## Conflict 1 (headline) — "Published in 2023" vs. the 23-Jul-2026 decline letter

**Claim in tension A** — repeated in three independent project-memory files:

- Parent root `../CLAUDE.md`: *"1. 2023 — IEEE Sensors Letters (1st author, published): AlGaN/GaN Hall sensor deployed in-vessel in HSX; 68 shots; voltage-biased, uncalibrated (V_off unknown); demonstrated real-time plasma tracking via temporal correlation with the diamagnetic loop."*
- `../01_PhD_Research_Folder_Info.md`: *"Demonstrated in-situ (2023 Letters) → calibrated spinning-current readout (02, HSX install Aug 2026) → calibrated 2–3 axis vector probe + second HSX campaign (03, RSI paper, ~Mar 2027)."*
- `../05_HSX_ChatGPT_Windows_App/inputs/project/CONTEXT_PRIMER.md` (line 11, a ChatGPT/Codex-authored project, not Claude): *"2023 (published, IEEE Sensors Letters): packaged AlGaN/GaN Hall sensor survived 68 in-vessel HSX shots; voltage-biased, uncalibrated."* Repeated without correction in that same folder's `outputs/00_INVENTORY_AND_GAP_MAP.md` and `outputs/05_EVIDENCE_AND_CLAIM_MATRIX.md`.

**Claim in tension B** — directly observed supplied evidence:

- `inputs/Decision_Letter_IEEE_2026-07-23.pdf`: portal-rendered page, `CreationDate` 2026-07-22 23:55:28 PDT, page 1 titled **"Decision letter (Initial Submission)"**, addressed "23-Jul-2026... Unfortunately, we must decline the manuscript for publication at this time... invite you to consider submitting a revised manuscript... It would be given a new Manuscript ID and reviewed again," for manuscript **SENSL-26-07-RL-1061**, same title and 68-shot claim as the manuscript in Group B of the inventory.
- `../01_Publications/submitted/regular_lsens/regular_lsens.pdf`, `../01_Publications/tim_ieee_sensors_letters_GaN_Hall_sensor_in_HSX_2023.pdf`, and `../05_HSX_ChatGPT_Windows_App/inputs/reference/2023_IEEE_SensorsLetters_HSX_GaN_Hall.pdf` are **all byte-identical** (SHA-256 `e7a990d8215ab88dcd6801b782b6592f76b8cd1a92f28dc982644cab9311d716`), and that file's own embedded PDF metadata reports `CreationDate: Thu Jul 2 14:04:08 2026`, not 2023.
- `inputs/IEEE_submission_bundle_2026-07-02.pdf` (the ScholarOne/Author-Portal submission export) has `CreationDate: 2026-07-02 16:55:21 PDT` — consistent with a 2-Jul-2026 initial submission, 21 days before the 23-Jul-2026 decision.
- The manuscript LaTeX source (`regular_lsens.tex`, lines 388-390) still has unfilled placeholder fields: `\thanks{Associate Editor: }` and `\thanks{Digital Object Identifier }` — both blank. A published IEEE paper carries an assigned DOI and Associate Editor name in this field; blank fields are consistent with an unpublished/in-review manuscript.
- No DOI, IEEE Xplore record, journal volume/issue, or any other independent evidence of an actual 2023 publication was found in any supplied file.

**Controlling evidence:** Claim in tension B. The checksums, PDF creation timestamps, the decision letter's own explicit "Initial Submission... decline" language, and the manuscript's unfilled DOI/editor fields are direct, primary, mutually corroborating evidence. Claim in tension A cites no source and is contradicted by all of the above.

**Most likely origin of the error (stated as inference, not fact):** `regular_lsens.tex` line 438 contains unedited IEEE_lsens.cls template boilerplate: `\IEEEpubid{1949-307X \copyright\ 2023 IEEE. Personal use is permitted...}`. This is a copyright-year placeholder string carried over from the class-file example (the original `bare_lsens.tex` template on which this file is based is dated 2017; the "2023" figure appears to be a leftover/placeholder never updated to reflect an actual acceptance year, since this manuscript was not accepted). This string, or a similar assumption made when a filename was first chosen, most plausibly propagated into the two "2023"-named PDF filenames and from there into three independent project-memory `.md` files across two different AI-tool workspaces (Claude and ChatGPT/Codex). **This origin theory is offered as an inference to explain the pattern, not as a verified fact** — the mission's actual publication-status record is the decision letter and manuscript metadata above, independent of how the mislabeling started.

**Resolution for downstream stages:** Treat the manuscript `SENSL-26-07-RL-1061` as **declined-with-invitation-to-revise as of 23-Jul-2026, never published**, for all purposes in Stages 10a–80. The "2023, published" framing in the parent `CLAUDE.md`, `01_PhD_Research_Folder_Info.md`, and `05_HSX_ChatGPT_Windows_App` must not be carried forward as fact in any later-stage output. Per `MISSION.md`'s fixed preference "Use the supplied files as ground truth; state conflicts explicitly," this conflict is stated here rather than silently corrected in place — the parent `CLAUDE.md` itself is treated as immutable input per the shared stage instructions ("Never assume the parent root memory is correct when it conflicts with uploaded evidence"), so this ledger, not an edit to `CLAUDE.md`, is the authoritative correction record for this mission.

**Status:** RESOLVED (by controlling evidence above), in favor of Claim B.

---

## Conflict 2 — Manuscript figure/shot numbering vs. the raw-data script naming

**Claim in tension A:** `regular_lsens.tex` Fig. 4 caption (line 491): *"(a) Amplified sensor output for unbiased (shot 63) and biased (shot 65) operation. (b) Comparison of the biased sensor response during a plasma discharge (shot 65) and a coil-only shot (shot 68)."*

**Claim in tension B:** `../07_HSX_august2025_results/hsx_20250821/figure3.m` (the script that generates `Fig3_SensorVerification_Combined.png`, which appears to be the source render for the manuscript's Fig. 4) explicitly loads `scope_66.csv` (labeled in-script "Biased") for panel (a)'s biased trace, `scope_62.csv` ("Unbiased") for panel (a)'s unbiased trace, and `scope_72.csv` ("Coil-Only Shot") for panel (b)'s second trace — i.e., scope-file indices 62/66/72, not shot numbers 63/65/68.

**Controlling evidence:** None found. No file in the supplied HSX data establishes a `scope_N` → `shot NN` lookup table. `hsxMainCoilCurrent_shot65.txt` and `hsxMainCoilCurrent_shot68.txt` independently confirm shots 65 and 68 exist as named HSX shots and correspond to the same comparison (plasma vs. coil-only) described in the manuscript, which is consistent with — but does not by itself prove — a specific scope-index-to-shot mapping (e.g., whether `scope_66.csv` is shot 65's trace or a different shot).

**Status:** UNRESOLVED. Flagged as an open evidence gap in `00_INPUT_INVENTORY.md`, Group D. Any stage that needs to cite a specific shot's raw voltage trace (e.g., Stage 40's experiment/statistics plan, or a manuscript-revision stage) must either (a) obtain the scope-to-shot mapping from Tim or the original acquisition log, or (b) cite the manuscript's shot numbers only where independently corroborated (as with shots 65/68 above) and avoid asserting a shot number for any `scope_N.csv` file not independently corroborated.

---

## Conflict 3 — Manuscript's stated 1 MHz bandwidth vs. project 02's measured 1–2 kHz demodulated bandwidth

**Claim in tension A:** `regular_lsens.tex` (Introduction, line 453 and Setup, line 483): the readout chain provides *"a total voltage gain of 200 V/V and a bandwidth of 1 MHz,"* stated as the sensor system's bandwidth, and this exact number is the subject of Reviewer 1's minor point 2: *"How was the 1 MHz bandwidth established? The amplifiers you listed have frequency capabilities well above 1 MHz. Is the limitation based on the device itself?"* (i.e., the reviewer already flags this number as unexplained/unjustified in the manuscript, not merely undocumented in the parent-project files).

**Claim in tension B (prior-project claim):** `../02_HSX_Hall_Sensor_Readout/docs/SPECS.md`, for the newer current-spinning readout design, states a demodulated bandwidth of **"~1–2 kHz demodulated (raw capture available)"**, explicitly contrasted in that document against "2023's" (i.e., the manuscript's) "1 MHz raw" figure.

**Controlling evidence:** These are not necessarily contradictory on their face — 1 MHz is stated in the manuscript as the *raw analog amplifier chain* bandwidth (i.e., the electronics' unmodulated small-signal bandwidth, unrelated to any demodulation), while project 02's ~1–2 kHz figure is the *effective demodulated* bandwidth of a different, newer current-spinning architecture that trades raw bandwidth for offset cancellation via chopping. No single file in the supplied evidence states both numbers together with an explicit reconciliation, and Reviewer 1 has already asked the author to justify the 1 MHz figure in the original manuscript on its own terms.

**Status:** UNRESOLVED / requires author-level reconciliation. Recorded here so that any later stage (particularly Stage 30, manuscript strategy, and Stage 40, experiment plan) treats "1 MHz" and "1–2 kHz" as two different quantities for two different readout architectures and does not conflate them, and so that Reviewer 1's specific request to justify the 1 MHz number is not lost.

---

## Conflict 4 — Prior lit-review project's own unresolved flag on the 2023 self-citation

`../04_Magnetic_Sensor_Review_Sensors2026/outputs/00_DELIVERABLE_paper_plan.md` independently flags: *"The author's own 2023 IEEE Sensors Letters AlGaN/GaN-in-HSX paper — [UNVERIFIED] this run; the author holds the citation and must insert it manually."* This is not a contradiction so much as corroborating evidence that even a fully separate, earlier Claude-run pipeline (2026-07-10) was unable to independently verify the "2023, published" claim and flagged it as unverified rather than asserting it as fact. This supports Conflict 1's resolution and is noted here as additional independent corroboration, not a new open conflict.

**Status:** Corroborating evidence for Conflict 1; not independently open.

---

## Non-conflicts explicitly checked and found consistent

- The 68-consecutive-shots claim is consistent across `regular_lsens.tex` (abstract, §III-A, Conclusion), the decision letter's quoted manuscript text, and is structurally plausible given the `../07_HSX_august2025_results/` campaign contains at least shots up through #21 (density/stored-energy files) and references up to shot 68/72 in coil-current and scope filenames — no shot-count contradiction found, though the full 1–68 shot range was not exhaustively cross-verified file-by-file in this stage (that level of verification is deferred to Stage 40 if needed for a repeatability re-analysis).
- The AD8429, $G=100.3$ readout-amplifier spec is stated identically in `../02_HSX_Hall_Sensor_Readout/docs/SPECS.md` and `../05_HSX_ChatGPT_Windows_App/inputs/project/HARDWARE_DATA.md` — consistent, not conflicting, and both independently flag the same open "~109×" amplitude anomaly rather than one silently contradicting the other.

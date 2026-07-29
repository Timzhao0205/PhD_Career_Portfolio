# SKILLS — B30_skills (PILOT)

**PILOT SAMPLE — NOT FINAL**

Stage: `B30_skills` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Pilot-scoped shared-stack analysis: exactly five skills (SKILLS.csv) and two
bridge experiments (BRIDGES.json), demonstrating the structure the full run
will apply to the complete capability space. Cxx = B10 PHD_FACTS claims;
EVxx/Pxxxx/G-M-BT = B15; PB-x = B25's ladder; W1/W2 = B25 POWER.md §9 wedges;
idea IDs verbatim from the A30/B20 universe.

## 1. Ground rules (applied to every row)

**Level vocabulary (exactly four):**

- `current_demonstrated` — the skill sits in B10's demonstrated ledger,
  attributed to the researcher's own dated bench/hardware work (C50 draws
  this boundary: NOTES.md/journal-class lab entries yes; AI-mission-produced
  ledgers and plans no).
- `literature_backed_near_transfer` — NOT possessed. A documented method
  template exists in the B15/B25 evidence base AND the adjacent base skill is
  demonstrated, so the conversion path is short and specified. The literature
  half alone never suffices: prevalence of a method in the corpus is evidence
  about the field, not about this user (the anti-inference rule below).
- `missing` — no demonstrated adjacent base; must be trained (typically under
  supervision) before any personal evidence can exist.
- `collaborator_or_vendor` — best obtained through a partner, hire, or vendor;
  deliberately NOT a personal-acquisition target within the planning horizon.

**Grounding:** current levels rest ONLY on B10's demonstrated-vs-proposed
ledger, as corrected by B20's five founder-fit corrections (ALIGNMENT.md §9:
D-02 array/DAQ, D-10 "home ground", C-01 power-electronics, C-05 scaled
metrology, A-10 control/system-ID) and B25's sixth (§3.6: the startup corpus's
founder-profile assertions — power electronics, HTS winding, battery imaging —
are unverified against ground truth and are NOT adopted). B25's governing rule
is restated here and binds every row: **magnetic-sensor expertise alone does
not suffice to design, qualify, or certify a power converter, protection
product, or power supply**, and nothing in this stage implies otherwise.

## 2. The shared-stack logic

B20's full-universe finding is the design constraint: across 39 directions,
every non-WEAK alignment runs through exactly one mechanism family —
**measurement authority** — via two channels: (a) the *demonstrated* hardware
channel (Hall readout chains C03/C13, harsh-environment packaging C46/C01,
EMI-disciplined bench measurement), and (b) the *proposed*
traceable-calibration + estimator-honesty methodology channel (C06 WP-C;
C23/C31 FT-02). Nothing else in the PhD transfers anywhere in the universe,
and the PhD's most distinctive scientific claims (stellarator deployment, GaN
radiation question, hybrid coil→Hall direction) carry the least startup value
(B20 §8.3).

The shared stack is therefore small and sharply defined. A capability belongs
in it only if it simultaneously:

1. **serves a PhD outcome** — Opt2 Element 1 (calibration credential, also the
   G5 gate condition), Element 2 (hybrid/bandwidth work), Element 3 (T0
   estimator package), or the P1/P2 publication path (C38); and
2. **serves multiple startup directions, not one** — the option-preserving
   preference: W1's measurement-and-qualification family (G-03, C-05, D-09,
   F-06) and/or W2's magnet-power measurement/detection family (D-01,
   ST01-C10/C11, ST03-ID_08/12), rather than any single idea's bespoke stack;
   and
3. **keeps fallbacks alive** — the OPT3 reconstruction fallback (C47) and the
   far-domain method market the CN-01 record evidences.

Capabilities that fail test 2 (idea-specific stacks: converter design,
protection interruption, certification, electrochemistry, photonics) are
deliberately routed to `collaborator_or_vendor` or excluded — that is B25 §4's
conclusion carried forward, not re-litigated.

**The stack's honest center of gravity:** the founder's realistic near-term
capability growth is entirely on the measurement/qualification side (B25 §5):
close C04 → execute WP-C (C06) → pass FT-02 (C31) → exercise the methodology
on current measurands (PB-1/PB-2 class). Both wedges are bets on that
conversion. The two bridge experiments (BRIDGES.json) are exactly that
conversion, instrumented with stop/continue gates.

## 3. How the five pilot skills exemplify the full-run structure

The five rows were chosen to span the two domains AND all four levels, so the
full run's row template is fully exercised:

| Row | Domain | Level | Structural role in the stack |
|---|---|---|---|
| S1 Hall readout / EMI bench discipline | sensing | current_demonstrated | The **maintain-and-extend** pattern: the one demonstrated hardware base everything else leans on; its own open defect (C04) is the program's first gate, and its extension path (switching-EMI exercise, multi-channel) rides BR-B and the PhD's own C14 plan rather than new training |
| S2 Traceable calibration (WP-C class) | sensing | literature_backed_near_transfer | The **convert-proposed-to-demonstrated** pattern: the single highest-leverage conversion in the entire evidence base — it is at once Opt2 Element 1, the G5 gate condition, D-02's decisive leg, and the credential all four W1 rows sell; template EV01/P0008, plan C06, gate C04 |
| S3 WBG test-bed operation / safe HV practice | power | missing | The **train-the-enabling-slice** pattern: not converter design (refused per §1) but the minimum safe-operation subset that unlocks personal power-domain evidence (BR-B and every PB-3/PB-4/PB-5 successor); supervision designed in because the ledger evidences none |
| S4 Certification / converter product engineering | power | collaborator_or_vendor | The **refuse-to-train, route-to-partner** pattern: organizational capability (B25 §4(c)); the plan spends $0 and produces only a decision memo; its presence in the CSV is what keeps the stack honest about what the founder will NOT become |
| S5 Estimator/identifiability + honesty tests | shared | literature_backed_near_transfer | The **zero-cost desk conversion** pattern: personal skill is created by personally executing BR-A Phase 0 (FT-02); provenance discipline is explicit — the corpus's derivations are AI-mission-produced (C50) and pre-redteam (C40), so they specify the path but prove nothing about the person |

Domain coverage check: S1/S2 clearly sensing-side; S3/S4 clearly power-side;
S5 spans both (Hall+coil estimation on the sensing side; arc/quench
detection statistics on the power side). Level coverage: all four levels
appear.

## 4. The gaps (what is missing, honestly)

Within the pilot's five-row window the gap structure is:

- **The demonstrated base is narrow and has an open defect.** One readout
  chain, emulator-validated offset suppression, one packaging execution, one
  qualitative campaign — with C04 unresolved and, by the project's own rule,
  blocking all calibration. The deployed module's location/health is
  undocumented (C45).
- **Both wedges rest on skills at `literature_backed_near_transfer`, not on
  anything demonstrated.** S2 and S5 are the load-bearing conversions; if
  either fails its gate (C04 unfixable; FT-02 unpassable), W1 and W2
  respectively lose their founder-side premise — this is stated as a stop
  gate, not smoothed over.
- **Everything power-side that is personal is `missing`; everything
  power-side that is product-grade is `collaborator_or_vendor`.** No row
  claims otherwise, and the B25/B20 corrections are carried unchanged.

## 5. Anti-inference guard (restated because it is the stage's hard rule)

Literature prevalence is never proof of a current skill. Concretely applied
in this pilot: EV01/P0008's calibration template does not make the user a
calibrationist (S2 stays non-possessed); P0003's Kalman-fusion literature does
not make the user an estimator builder (S5 stays non-possessed); the corpus's
own AI-mission-produced derivations and ledgers (C16/C17/C50) are specification
and evidence-base, not personal capability; and the startup corpus's founder
profile (B25 §3.6) remains unadopted. The only things called
`current_demonstrated` trace to researcher-attributed, dated bench/hardware
evidence: C01, C03, C13, C46 (C46 is deferred to the full run's packaging row;
it is cited here only as part of the demonstrated base).

## 6. What the full run must add (scope disclosure)

1. The complete skill matrix over every B25 §4 family: harsh-environment
   packaging (C46) as its own row; multi-channel/array instrumentation and
   lock-in thermography (the D-02 correction); cryogenic 77 K bench practice
   (D-02/W2 dependency); precision-current reference operation (BUY-side, S-B25-02
   class); detection-statistics practice (PB-3); the application-domain
   families (B25 §4(e)) with explicit retire/partner calls; AI-mission
   direction as a skill in its own right (C16/C17/C50) with its provenance
   bounds.
2. The full unified bridge ladder: all seven PB-x and all eight BT-x placed,
   deduplicated against BR-A/BR-B, including the PB-6/BT-8 desk audits (an
   inherited, undischarged obligation — no EV07/EV08 headline figure may be
   reused until it closes) and the PB-7/BT-5 collaborator-led irradiation
   channel (never on the critical path, per C09).
3. Per-row owner/priority reconciliation against the 44-milestone roadmap
   (C38), the P1 revision critical path, and disclosure gates (C33/C34).
4. Budget totals and a resource-leveled calendar (the pilot places only the
   five rows and two bridges).
5. Contingency branches: C04-unfixable path (S1 downgrade per B20's D-02
   falsifier; OPT3 pivot logic per C47), no-supervision path (BR-B blocked,
   BR-A Phase 1 low-voltage-only), module-lost path (C45).

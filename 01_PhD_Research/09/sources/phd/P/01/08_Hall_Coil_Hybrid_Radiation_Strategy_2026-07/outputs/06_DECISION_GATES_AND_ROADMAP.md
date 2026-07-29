# 06 — Decision gates and roadmap

Stage 60 (`60_research_program`). Produced and signed off by Fable 5
(xhigh). ID conventions as in `06_INTEGRATED_RESEARCH_PROGRAM.md`
(sources `Hxxx`/`Rxxx`/`Pxxx`, claims `Cxx`, tests `FT-xx`, failure
modes `FM-xx`, risks `RR-xx`, hybrid tier gates `HY-G0…G5` = stage-30
G0–G5, folder-06 gates/milestones `06-G*`/`06-M*`). Labels: **Observed /
Derived / Inferred / Proposed / Unknown**. Everything scheduled here is
**Proposed**; premises are cited.

**Standing conflict record:** folder 06 and this mission both define
gates named G0–G5 with different meanings. This file never uses a bare
`G` number; the prefix is part of the ID. (Recorded per `CLAUDE.md`
conflict rule; original meanings preserved in both source documents.)

---

## 1. Ordered master gate sequence

Order = execution order = cost order (FT-ladder discipline: every
expensive step sits behind a cheaper falsification gate — stage
acceptance requirement). "External" marks gates owned by folder-06's
plan or by third parties; this program never jumps an external queue.

| # | Gate ID | Name | Cost class | Owner | Entry depends on | Pass → | Fail → (pivot path) |
|---|---|---|---|---|---|---|---|
| 0 | DG-00 | Advisor sign-off on this program (uses `06_ADVISOR_MEETING_BRIEF.md`) | desk | Tim + advisor | folder-06 advisor meeting (06-M01/M02, ~now) | proceed; decisions minuted | revise program per advisor input; no research action blocked except outreach/spend items |
| 1 | DG-01 | FT-01 prior-art kill search (initial run done in Stages 10–50; re-run cadence set) | desk | Tim | none | C36 gaps stand; novelty claims usable | K1: drop closed gap(s); rebuild P2 contribution; if all gaps close → stop research-claim track |
| 2 | DG-02 = HY-G0 | T0 package passes FT-02 (honesty) + FT-03 (anchor cadence) | simulation | Tim | DG-01; stage-20 rank-test regression binding | hardware planning may proceed; T0-predicted uncertainties published to Phases 1–3 | FT-02 fail → K2 stop-all-hardware; FT-03 fail → cadence/HA/descope re-design loop before any hardware spend |
| 3 | DG-03 = 06-G1 | ~109× anomaly closure (**external**: folder-06 M06; its "no calibration before B-01 closes" rule binds) | bench (06) | Tim (06 plan) | folder-06 G0 inventory | Phase-1 bench opens | folder-06 fault-isolation sprint; this program waits; P1 re-scoped per 06 plan |
| 4 | DG-04 | FT-04 zero-field/flip offset anchor valid | bench-day | Tim | DG-02, DG-03 | offset half of calibration story stands | K3: withdraw offset claims; re-derive budgets; HY-G1 blocked (no fallback — CASE E) |
| 5 | DG-05 = HY-G1 | Bench truth: anchored-hybrid calibration repeatable ≥3 cycles within T0-predicted uncertainty; `α_S`, `β_b` characterized; **FT-05 reverse-direction recovery passed** | bench-days | Tim | DG-04; folder-06 WP-C complete | Phase 3 opens; tokamak outreach gate arms (DG-08) | FT-05 structural fail → K4 collapse to C02-only, P2 reframe; repeatability fail → halt and diagnose (stage-30 T1 stop rule) |
| 6 | DG-06 = HY-G2/G3 | HA layer earns its place: FT-06 (winding orthogonality/closure/heating) + FT-07 (drift race vs scheduled recal) + rung-4 soak | bench-soak | Tim | DG-05 | Tier-2 architecture confirmed for P2/P3 | FT-06 fail → descope to MVD (planned good outcome); FT-07 fail → K5 cut performance claim to fault-detection + C02; both FT-07 & FT-10 fail → K6 drop fusion layer |
| 7 | DG-07 | Machine legs: FT-08 (vacuum-shot anchors ≥3 epochs) + FT-09 (reproducibility floor) + FT-10 (EMI/ρ-alarm) at HSX | machine-piggyback | Tim + HSX ops | DG-05; campaign windows (06-M16/M25 — **external** schedule) | in-machine evidence pack complete; Phase 5 demo + outreach fully armed | FT-08 fail → K7 relative-only reframe before any outreach; FT-09 fail → drop repeated-waveform layer (costless); FT-10 injection fail → MVD-only at HSX |
| 8 | DG-08 | Tokamak outreach gate (IPP-Prague / KFE) | desk | Tim + advisor | DG-05 (minimum); DG-07 strengthens; evidence pack per program §5 | approach with: Theorem-1 proof, T0 honesty results, HY-G1 bench result, one-page C06 note | no response / no shared problem → stage-40 fallback: HSX-only support for all dissertation claims (no dependency existed) |
| 9 | DG-09 = HY-G3→G4 | Radiation entry gate: HY-G0–G3 all passed **and** collaborator agreement signed (coauthored framing) | desk→campaign | Tim + advisor + collaborator | DG-06 (HY-G3), DG-08-class relationship or rad-effects group per program §5 | FT-11 screening runs (collaborator-led) | no agreement → Phase 4 simply does not happen; **zero impact on P1/P2/P3** (stage-30 §9.4) |
| 10 | DG-10 = HY-G4→G5 | FT-11 three-way decision → (only on branch (b)) FT-12 qualification | irradiation campaign | collaborator + Tim | DG-09 | (a) drift below floor → simplify to MVD + scheduled recal (good outcome); (b) measurable/monotonic → FT-12; FT-12 pass → first C21-supported compensation claim (P4) | (c) unattributable / witness unreplicated → K9 falsified for material set; FT-12 fail → retreat to detection + scheduled recal, reported plainly |
| 11 | DG-11 | Module freeze + release | desk | Tim | DG-02 maintained; P2 submission timing (06-M27) | package frozen at §11 boundary; released with P2; disclosure gates (06-G-C…G-G class) respected | time pressure → freeze earlier at whatever passes HY-G0 (B8 boundary; never an open-ended project) |

**Standing synchronization gates (external, folder-06-owned; this
program only reads them):**

- **06-M28 (MVG-vs-upside checkpoint, ~Q1 2027):** if it commits to the
  floor-only plan, Phases 3+ of this program stop per K8.
- **06-G5 direction gate (06-M34, ~Jul 2027):** fail → OPT3 pivot;
  hybrid program shrinks to what P2 has banked (K8).
- **Disclosure gates 06-G-A…G-H:** bind every public artifact of this
  program (P2 manuscript, any code release, any talk) exactly as they
  bind folder-06's own outputs.

---

## 2. Dependency structure (text graph)

```text
DG-00 (advisor) ─┐
DG-01 (FT-01) ───┼─→ DG-02 (HY-G0: FT-02+FT-03) ──────────────┐
                 │                                            │
folder-06: 06-G0 inventory → DG-03 (06-G1 anomaly) ──┐        │
                                                     ▼        ▼
                                    DG-04 (FT-04) ←─ bench + T0 CIs
                                                     │
                                                     ▼
                              DG-05 (HY-G1 incl. FT-05) ──────┬─→ DG-08 (outreach)
                                                              │
                    ┌─────────────────────────────────────────┤
                    ▼                                         ▼
        DG-06 (HY-G2/G3: FT-06/07 + soak)        DG-07 (FT-08/09/10 @ HSX,
                    │                              rides 06-M16/M25 windows)
                    └───────────────┬─────────────┘
                                    ▼
                     DG-09 (radiation entry: HY-G3 + agreement)
                                    ▼
                     DG-10 (FT-11 → FT-12)   [collaborator-led; P4]
DG-02 (maintained) ──────────────────────────→ DG-11 (module freeze, with P2)
```

Properties (Derived): every irradiation-campaign item sits behind two
simulation gates, four bench gates, and a signed agreement; the P1/P2
critical path (folder-06) touches this graph only at DG-03 (which it
owns) and DG-11 (which follows its P2 date) — the hybrid program can
die at any DG-01…DG-07 gate without destabilizing graduation
(boundary B6).

---

## 3. Checkpoints and review cadence

| Checkpoint | When | What is reviewed | Recorded where |
|---|---|---|---|
| CP-A | DG-00 meeting (~Aug 2026) | program adoption; decisions minuted | advisor meeting notes; folder-06 M02 batch |
| CP-B | DG-02 pass (target ~Oct–Dec 2026) | FT-02/FT-03 results; T0-predicted uncertainties issued | T0 run reports (plan §7–§9 formats); project journal |
| CP-C | DG-05 pass (target ~Dec 2026–Feb 2027) | bench package: FT-04/FT-05 numbers vs predictions; HY-G1 verdict; P2 scope freeze | uncertainty-budget table (ARCH §6.3 format); P2 outline |
| CP-D | 06-M28 sync (~Q1 2027) | MVG-vs-upside; hybrid Phases 3+ go/stop | folder-06 checkpoint; K8 check |
| CP-E | DG-06/DG-07 close (~Q2 2027) | HA go/no-go; in-machine evidence pack; outreach decision | FT-06…FT-10 reports; DG-08 evidence pack |
| CP-F | 06-G5 sync (~Jul 2027) | direction gate; hybrid continuation | folder-06 M34 record |
| CP-G | DG-11 freeze (with P2 submission) | module state; disclosure-gate compliance | release notes + version tag |
| CP-H | DG-09/DG-10 (only if entered; 2027–2028) | FT-11 branch decision; FT-12 outcome | collaborator agreement + P4 records |

Each checkpoint answers three questions, in writing: which gate(s)
closed and with what numbers; which kill criterion (K1–K10) was
checked and found untriggered (or triggered — then the pre-scripted
action, not an improvised one); what the next gate needs.

---

## 4. Resume-ready next tasks (concrete; in execution order)

1. **Present the program (DG-00).** Bring
   `outputs\06_ADVISOR_MEETING_BRIEF.md` to the already-planned
   folder-06 advisor meeting (06-M01/M02 window, ~now). Zero
   preparation beyond reading it.
2. **Set the FT-01 re-run cadence (DG-01 maintenance).** Calendar rule:
   re-run the four C36 gap searches forward from [H001]–[H004],
   [H021], [H059], [P003], [P057] before every manuscript/proposal
   submission (first re-run: before P2 drafting, ~Dec 2026).
3. **Build the T0 package (DG-02).** Implement
   `03_SIMULATION_AND_VALIDATION_PLAN.md` §2 (truth model), §3
   (schema with species-vector enforcement), §4–§5 (scenarios S1–S12,
   faults F1–F14), §7–§8 (metrics M1–M8, test suite) — starting from
   the regression binding to `tools\observability_rank_tests.py`
   (rank-for-rank reproduction before any estimator tuning). Run
   FT-02, then FT-03 with logged HSX shot-schedule cadences. This is
   folder-06 WP-D/M17 desk work under another name — it does not
   compete with bench time.
4. **Add the two cheap hybrid items to the existing Phase-1 bench
   list (DG-04 prep).** Procure/fabricate the wound/PCB coil + fixture
   (folder-06 BOM class); schedule FT-04 (~1 bench-day) inside the
   WP-C block after 06-G1 closes; confirm fluxgate-class ambient audit
   availability for the zero-field environment.
5. **Script FT-05 before running it (DG-05 prep).** The emulated-drift
   protocol, CASE-B/D/I regressions, and Fisher-CI acceptance checks
   can be written and tested against T0 synthetic data first, so the
   ~2–3 bench-days spend only on data taking.
6. **Draft the DG-08 evidence pack skeleton now, fill at HY-G1.**
   One-page C06-gap note (lead with the Theorem-1 derivation) +
   placeholder slots for T0 honesty results and HY-G1 numbers. Nothing
   is sent before DG-08 arms (B7).
7. **Log this program's gates into the weekly folder-06 rhythm.** Add
   DG-01…DG-11 status to the existing weekly checkpoint list
   (folder-06 roadmap §9) so slips are detected by the same mechanism
   — no new process invented.

Items 1–3 are pure desk work executable immediately; items 4–5 wait on
DG-03 (06-G1) exactly as folder 06 already requires; nothing here adds
a new critical-path element to the folder-06 plan.

---

## 5. Honest limitations of this roadmap

- All dates inherit folder-06's slip logic and its two named
  high-consequence risks (06-G1 anomaly closure; P2 review) — this
  program adds no schedule authority over them.
- The GaN radiation-drift magnitude is Unknown (C14): FT-03's
  pass/fail uses labeled bounding analogs (C12/C13, Inferred), so
  DG-02's cadence verdict is provisional until Phase-4 data exists —
  which is precisely why the architecture is designed to measure
  drift rather than assume it.
- DG-07 timing is hostage to HSX campaign scheduling (external); the
  fallback (bench-only P2) is pre-scripted, not improvised.
- Single-source dependencies persist at DG-06/DG-10: [H059] (C11) for
  the reverse direction's only precedent, [R071] (C18) for the
  witness null — both are exactly what FT-05 and FT-11(ii) exist to
  test rather than trust.
- No facility, schedule, price, or collaborator commitment is claimed
  to exist for Phase 4; DG-09 is a specification for a future
  agreement (plan §10 rung-6 discipline).

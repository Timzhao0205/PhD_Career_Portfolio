# 06 — Advisor meeting brief (Stage 60)

**Purpose:** a one-sitting brief for the meeting with Prof. Senesky that
`06_MILESTONES.csv` row M02 depends on. Full evidence and reasoning are in
[`02_RESEARCH_DIRECTION_DECISION.md`](02_RESEARCH_DIRECTION_DECISION.md),
[`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md),
[`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md), and
[`05_DISCLOSURE_HOLD_CHECKLIST.md`](05_DISCLOSURE_HOLD_CHECKLIST.md) — this
document only summarizes and schedules. **Nothing described here has been
sent, submitted, filed, or contacted externally.**

---

## 1. Decision requested

Seven items, all from the direction-decision stage, in the order they
block downstream work:

1. **Approve the novelty re-centering (OPT2):** cite the group's own
   device papers (S0004–S0006, S0012) as prior art; claim the
   contribution as the finished calibrated application + measurement
   architecture, not the device itself.
2. **Approve WP-D (hybrid Hall+inductive fusion) as thesis scope**,
   including the UW co-authorship shape for the plasma-side content.
3. **Gen-2 die status and count:** are larger-pad dies fabricated or
   in-fab? How many packaged dies can WP-B's repeatability study use
   (≥3 needed for the AE's own specification)?
4. **Authorize the UW e-mail** (feedthrough pin count, mount-pose survey,
   vacuum-field computation, shot-list request, co-located B-dot/Mirnov
   data access, HSX discharge-magnetics-archive question).
5. **Venue-route preference:** confirm or contest the recommended A→C
   sequence (§4 below).
6. **Confirm the two-year graduation target and committee framing** for a
   device + system + methods thesis.
7. **Acknowledge the parent-project record correction:** the manuscript
   is an unpublished, declined 2026 submission, not "the 2023 published
   paper" — several files outside this mission's write access repeat the
   unsupported "2023, published" framing and should be corrected by Tim
   directly (`00_CONFLICT_LEDGER.md` C1).

---

## 2. Evidence-backed recommendation

**Continue the GaN Hall magnetic-diagnostics direction, adjusted (OPT2),
not changed.** Across three independent literature lanes (231 verified
peer-reviewed sources), no GaN/AlGaN Hall sensor was found deployed
in-vessel in any tokamak or stellarator, and no Hall sensor of any kind
was found in a quasi-helically symmetric stellarator — the specific
material-plus-facility combination is unclaimed, even though Hall sensing
itself is the fusion field's own established answer to integrator drift
(JET's InSb probes, ITER's 60-unit bismuth array). Continuing the
manuscript's *device*-novelty framing would fail again — that framing is
exactly what Reviewer 2 rejected, and it is contradicted by the group's
own 2019 publications. The adjustment moves novelty to the *application +
calibrated measurement + architecture* level, adds four
campaign-uncoupled work packages (comparison table, multi-die
repeatability, calibration + uncertainty budget, hybrid Hall+inductive
fusion), and produces a **minimum-viable two-paper floor that does not
depend on the HSX campaign succeeding** — full reasoning, scoring, and
sensitivity analysis in `02_RESEARCH_DIRECTION_DECISION.md` §1–§2.

---

## 3. Next experiment's must-have measurements

All of the following are **bench-only** — none requires HSX access — per
the stage-40 design rule that every P0 reviewer item is bench-satisfiable:

| Must-have | Answers | Acceptance |
|---|---|---|
| ~109× anomaly closure (B-01) | The single blocking item — no calibration work happens before this | Mechanism named, reproduced, logged |
| Absolute DC calibration + uncertainty budget (C-02) | AE-01/AE-04/AE-05, Reviewer 1's key point | m ± u(m) ≤ 2% absolute, <0.5% linearity |
| Multi-die repeatability (D-01/D-02) | AE-03, Reviewer 2 ("only one module was tested") | ≥3 dies characterized, or the AE-sanctioned single-device fallback with literature citation |
| Bandwidth derivation with stated basis (B-03/B-04) | AE-07, Reviewer 1's minor point #2 | Measured/derived, not asserted (the 1 MHz figure is retired) |
| GaN-vs-competitor comparison table (WP-A) | AE-02, novelty framing | Table populated from the source ledger |
| Voltage-bias S_v for the 2025 dataset (C-03) | AE-05's field-units request for Fig. 5 | S_v with uncertainty at the deployed bias settings |

**Upside, not required:** an in-machine coil-only absolute anchor
(campaign #1) and the vector-probe instrument study (campaign #2) — both
strengthen the plan materially but neither is on the graduation-critical
path (`06_24_MONTH_PHD_ROADMAP.md` §2.1).

---

## 4. Sensors Letters / arXiv / RSI route

**Recommended sequence: A → C.**

1. **Route A — revise and resubmit to IEEE Sensors Letters**, using the
   existing invitation (new Manuscript ID, declare prior ID
   SENSL-26-07-RL-1061), but only after the bench package above closes.
   No deadline is stated in the decision letter.
2. **Route C — the RSI vector-probe instrument study**, built on
   campaign #2, as the separate, substantially new paper project 03 was
   already planning.
3. **Optional accelerant:** post the *revised* (calibrated, reframed)
   manuscript to arXiv at resubmission time — IEEE's policy explicitly
   permits this — but only after the IP screen (§5) and advisor sign-off.

**Not recommended as primary:** posting the *rejected* version to arXiv
now and skipping straight to RSI (the route as originally proposed). It
permanently publishes a version with documented defects (unsupported
1 MHz bandwidth, loose QHS wording, no calibration), leaves zero
peer-reviewed output until roughly mid-2027, and triggers the IP-screen
gate at the earliest possible point for the least benefit. Full
route-by-route comparison in `03_PUBLICATION_ROUTE_DECISION.md` §3, §5.

---

## 5. Pre-publication hold

**Hard gate, not a scheduling preference:** no arXiv posting, conference
talk/poster/abstract, public code repository, or thesis deposit happens
before the advisor + Stanford OTL pre-disclosure screen concludes. This is
the advisor's own stated condition
(`../inputs/ORIGINAL_REQUEST.txt`), and stage 50 built the checklist that
operationalizes it: six candidate concepts (CC-1..CC-6) ranked by evidence
maturity and disclosure urgency, with the two most urgent (CC-2 readout
chain, CC-1 packaging stack) being the ones the P1 manuscript itself would
disclose first. **Expected outcome, stated in advance so it is not a
surprise:** the prior-art density around every concept is high (the
group's own 2019 papers, active Infineon/TI spinning-current patents,
fresh 2025 Kalman-fusion journal art), so any protectable scope is likely
thin and combination-specific — "nothing worth filing" is a plausible and
legitimate conclusion, not a failure of the screen. Full detail in
`05_DISCLOSURE_HOLD_CHECKLIST.md` and
`05_CANDIDATE_PROTECTABLE_CONCEPTS.md`.

---

## 6. Resource / HSX / collaborator questions

- **UW-Madison (Goodman/Gallenberger/Geiger):** do co-located B-dot/
  Mirnov records exist for the Aug-2025 shots? Feedthrough pin count on
  the intended port? Mount-pose survey feasibility? Vacuum-field
  computation at the probe pose? Coil-only shot allocation? Does an
  HSX discharge-magnetics archive exist at scale (prices the fallback
  direction if the current one needs to pivot)?
- **Stanford lab resources:** is a floating ~100 µA source (SMU) already
  accessible, or does a REF200 need purchasing (~$8)? Is a borrowed
  electromagnet + calibrated gaussmeter available for a high-field bench
  point (currently unconfirmed)?
- **Die/packaging:** gen-2 fabrication status (decision item 3); wedge-
  bonder access for packaging ≥2 more modules.
- **The deployed 2025 module:** where is it now, and is it still
  functional? This is the single most consequential *new* inventory
  question from stage 40 — it gates the retroactive field-unit conversion
  for the 2025 dataset (C-03) and the repeatability study (D-01).
- **Collaboration/IP framework:** is there an existing agreement with
  UW-Madison (or WARF) covering the HSX deployments that already
  allocates IP, before the UW e-mail shares CC-3/CC-5 design specifics?

---

## 7. 30 / 90 / 180-day commitments

**30 days (by ~2026-08-24):**
- Advisor decision batch #1 answered (§1 items 1–7).
- UW e-mail sent (contingent on item 4).
- A-group supplied-data analyses and the WP-A comparison table complete
  (need nothing but files already in hand).
- G0 inventory gates closed; the ~109× anomaly (B-01/gate G1) closure
  attempted.
- Advisor + OTL pre-disclosure conversation opened.

**90 days (by ~2026-10-23):**
- WP-C calibration core complete (field-source build, DC calibration +
  uncertainty budget, voltage-bias S_v conversion).
- WP-B repeatability statistics complete (or the honest single-device
  fallback documented).
- Characterization suite (bandwidth, noise, hysteresis, temperature,
  drift, parasitics) complete.
- Campaign #1 executed if the UW gates and pre-ship checks clear
  (realistic window: September 2026, per
  `06_24_MONTH_PHD_ROADMAP.md` §1's honesty flag on the stated August
  target).
- P1 full draft complete; IP screen concluded.
- Dissertation reading committee formation underway.

**180 days (by ~2027-01-21):**
- P1 resubmitted to IEEE Sensors Letters (contingent on the IP screen).
- Optional arXiv posting decided (only with documented sign-off).
- Campaign #2 (vector probe) executed or clearly slipped, with the
  fallback (bench-validated module) already in motion if so.
- WP-D algorithm development substantially complete on synthetic +
  available HSX data.
- P1 review cycle underway; P2 draft started.

---

## 8. Cross-references

- Full milestone register with dates, dependencies, owners, and
  fallbacks: [`06_MILESTONES.csv`](06_MILESTONES.csv).
- Full roadmap narrative, minimum-viable vs. upside plans, and slip
  decision points: [`06_24_MONTH_PHD_ROADMAP.md`](06_24_MONTH_PHD_ROADMAP.md).
- Startup-preparation detail (explicitly not this meeting's subject, but
  advisor awareness is recommended per §6 of that document):
  [`06_STARTUP_READINESS.md`](06_STARTUP_READINESS.md).

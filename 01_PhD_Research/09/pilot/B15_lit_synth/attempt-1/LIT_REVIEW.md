# LIT_REVIEW — B15_lit_synth PILOT

**PILOT SAMPLE — NOT FINAL**

Stage: `B15_lit_synth` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Scope: this synthesis is built **only** on the eight B12 pilot papers
(P0001-P0008), each of whose publisher/PMC record this run independently
re-opened on 2026-07-28. It adjudicates evidence; it does not rank startups.
Absence of a topic from these eight papers is never treated as proof that no
such work exists — every "no ... in this set" statement below is bounded by
the 8-paper scope. Full-corpus synthesis (62 papers, >=30 evidence rows) is
reserved for the full run.

## 1. Independent adjudication of B12's eight pilot records

Every record was re-opened this run (WebFetch; publisher landing page for
IOP/Copernicus items, the B12-cited PMC mirrors for the two MDPI items whose
direct pages this run independently re-confirmed as blocked, HTTP 403).

| ID | Verdict on B12 classification | Basis re-verified this run | Adjudication additions |
|----|------|------|------|
| P0001 | **CONFIRMED** (journal_article, verified, hybrid_diagnostics, accepted_core) | Nucl. Fusion 62 106032 (2022); received 2021-09-30 / revised 2022-07-15 / accepted 2022-08-18; OA CC BY; no correction/retraction notice found | None needed; rich primary evidence extracted (Section 2) |
| P0002 | **CONFIRMED** (journal_article — a research benchmarking study, not a review, despite the survey-like title) | SuST 38 125023 (2025); single-anonymous review, 1 revision; received 2025-09-12 / accepted 2025-12-01; OA; none found | Evidence-weighting note: only 36 real quench records underlie the 75-technique benchmark |
| P0003 | **CONFIRMED** (journal_article, verified, hybrid_diagnostics) | Nucl. Fusion 65 046008 (2025); dates match B12 exactly (2024-10-24 / 2025-01-13 / 2025-02-13); OA; none found | Evidence-weighting note: validation is **synthetic-data only**; no machine data presented |
| P0004 | **CONFIRMED** (journal_article in an ECPD 2025 themed issue — B12's decision *not* to classify it as conference proceedings is correct: regular research article, single-anonymous review, 1 revision) | PPCF 68 065013 (2026); received 2026-01-30 / revised 2026-04-21 / accepted 2026-05-12; published 2026-06-05; OA CC BY; none found | Metadata addition: article number 065013 and publication date 2026-06-05 (omitted from the B12 row, not an error) |
| P0005 | **CONFIRMED** (review_article, verified via PMC mirror PMC10673564) | Micromachines 14(11):2045 (2023); received 2023-10-06 / revised 2023-10-25 / accepted 2023-10-27; academic editors Zeheng Wang and Jing-Kai Huang; no notice found on PMC record; mdpi.com direct page independently re-tested this run: still HTTP 403 | Treated strictly as review-level evidence (Section 5) |
| P0006 | **CONFIRMED** (review_article, verified via PMC mirror PMC7826992) | Micromachines 12(1):65 (2021); received 2020-12-25 / accepted 2021-01-06 / published 2021-01-08; no notice found; mdpi.com still HTTP 403 this run | Limitation added: 12-day receipt-to-acceptance interval flagged as a peer-review-depth caveat (not disqualifying) |
| P0007 | **CONFIRMED** (journal_article, verified, hts_quench_current) | SuST 29 045007 (2016); single-anonymous review, 1 revision; received 2015-11-07 / revised 2016-01-10 / accepted 2016-01-21; no notice found | Two additions: (a) full text is **paywalled** — the open landing-page record was the adjudication basis (B12's access wording was accurate but did not state this); (b) the study is a **multiphysics simulation** anchored to one experimentally measured parameter, not an experimental quench test — this matters for evidence weight |
| P0008 | **CONFIRMED** (journal_article, verified, hall_metrology) | JSSS 9, 391-399 (2020), Copernicus; explicit review statement ("edited by Michael Kraft and reviewed by two anonymous referees"); received 2020-06-11 / accepted 2020-10-02; OA CC BY; none found | None needed |

Summary: **8/8 B12 classifications confirmed; 0 corrected.** Adjudication
added four evidence-weighting clarifications (P0002, P0003, P0007 x2), one
metadata completion (P0004), and one peer-review-depth caveat (P0006). No
correction, expression of concern, or retraction was found on any of the
eight records this run; "none found" on an opened record is not proof that
none exists anywhere.

## 2. hall_metrology — what these papers establish

**Established (primary experiments):**
- Traceable Hall-probe calibration with a real uncertainty budget exists as
  a demonstrated method at room temperature and low field: gold micro-Hall
  sensors at 3.2 mV/A/T +/- 0.3% against a traceably calibrated commercial
  probe over +/-150 mT, with combined expanded SHPM uncertainty
  +/-(7 mT + 13%), k=2 (P0008) [EV01].
- Radiation-hard Hall sensing is demonstrated for **InSb** (11+ years on
  JET, D-T flux ~1e13 cm-2 s-1, calibration scatter ~+/-0.07%, stability
  quoted to 2e18 cm-2 fluence; P0001) and reported for **Sb** with W-Ti
  diffusion barriers (stable 89.6 mV/A/T through 350 C/50 h + 220 C/120 h,
  linear to +/-2.5 T, quoted <=2.3% sensitivity shift at 1.4e20 cm-2 fast
  neutrons; P0004) [EV02].

**Plausible inference:** the P0008 methodology (reference-probe chain +
component uncertainty budget) transfers in principle to fusion-relevant Hall
sensors; nothing in this set demonstrates it at tesla-scale fields or in a
machine environment.

**Unknown in this set:** any GaN/AlGaN Hall-plate radiation behavior [EV09];
any traceable calibration at ITER-relevant +/-2.5 T; long-term drift budgets
expressed as formal GUM-style uncertainty statements for in-machine sensors.

## 3. hybrid_diagnostics — what these papers establish

**Established:** Hall sensors and coils have co-operated in one long-lived
in-vessel system (P0001), and a Kalman-filter fusion of the two channels
eliminates integrator drift with ~30x SNR gain **on synthetic data** (P0003)
[EV03]. The hybrid Hall+coil architecture concept is therefore established
prior art at both system and algorithm level — consistent with B10's own
finding (C26) of 26 years of prior art.

**Plausible inference:** a built hybrid probe of the P0001-proposed class
would plausibly work; P0003's estimator would plausibly survive contact with
real data at some degraded performance level.

**Unknown / contradiction in this set:** no hardware demonstration of fused
Hall+coil operation under real fusion conditions exists here; the coil-to-
Hall reverse-calibration direction the PhD proposes has **zero** support in
this set, and P0001's own coils were never bench-calibrated — the flagship
deployed system lacked precisely the trusted coil chain the reverse
direction requires [EV04]. There is also a disclosed regime tension between
P0003's idealized noise assumptions and P0001's reported real-installation
messiness (~19% pulse loss, suboptimal coil SNR) [EV10].

## 4. hts_quench_current — what these papers establish

**Established (with computational caveat):** the no-insulation REBCO
self-protection mechanism — turn-to-turn current redistribution, ~145 K peak
hot spot, recovery without intervention — is quantitatively described by a
simulation anchored to a measured 70 uOhm-cm2 contact resistivity (P0007)
[EV05]. Because the provenance is computational, this run weights it as a
strong mechanism model, not as demonstrated machine-protection practice.

**Established (small-scale experiment):** 36 real quench records from one
helical coil, augmented with artificial data, support 0.9861 held-out ML
detection accuracy, 0.875 cross-geometry, 0.8056 at 0 dB SNR (P0002) [EV06].
The two papers are complementary: P0007's <=9 mV terminal-voltage signature
explains why P0002-class advanced detection is needed at all.

**Unknown in this set:** experimental validation of P0007's redistribution
dynamics on instrumented coils; any in-service or real-time deployment of
P0002-class detection; behavior at lower contact resistivities (27 uOhm-cm2
is flagged by P0007's authors as harder).

## 5. power_conversion — review conclusions kept separate

Both stream papers are **reviews** (P0005, P0006); per LIT_POLICY this run
treats their conclusions as consensus mapping, not primary evidence, and did
not trace their headline numbers to the underlying primary studies.

**Review-level consensus:** SiC/GaN devices enable up to ~100x switching
frequency and ~99% efficiency demonstrations, SiC to 200-300 C operation
[EV07]; gate-drive design (narrow E-mode GaN gate window -10 V to +7 V,
crosstalk, non-universal commercial drivers) is a persistent bottleneck
[EV08]. The two reviews, written independently in 2021 and 2023, agree in
direction.

**Unknown in this set:** any primary measurement this run could weight; the
2024-2026 state of driver/device maturity (both reviews predate it).

## 6. What the PhD has established vs what this literature only suggests

From B10 (PHD_CORE/OPT2), read against the adjudicated evidence:

- **PhD has established (its own primary artifacts):** an in-vessel
  AlGaN/GaN Hall module deployment with qualitative shot data (C01); bench
  current-spinning readout with an unresolved ~109x anomaly (C03/C04); zero
  accepted publications to date (C49). Nothing in P0001-P0008 either
  duplicates or invalidates these specific artifacts.
- **Literature supports (this set):** the general feasibility of
  radiation-hard Hall sensing (in other material systems, P0001/P0004), the
  Hall-corrects-coil fusion direction (P0003), and the existence of a
  traceable-calibration method template (P0008) that WP-C (C06) could
  emulate.
- **Literature only suggests, does not establish:** that a GaN Hall die can
  be calibrated to the WP-C targets (u(k)/k <= 2%) — P0008 is a different
  material, field range, and environment; that a hybrid probe would deliver
  its promised performance in a real machine — P0003 is synthetic, P0001's
  probe is a proposal [EV10].
- **Literature is silent (in this set) exactly where the PhD is most
  exposed:** GaN radiation drift magnitude (matches B10 C29's "Unknown")
  [EV09], and the coil-to-Hall reverse-calibration direction (matches B10
  C23/C26) [EV04]. Silence here is double-edged: it preserves the claimed
  novelty gaps *and* means the PhD's assumptions carry no external support.
  These eight papers cannot settle either question; the full corpus check
  is deferred to the full run.

## 7. Method and limitations

- No citation counts or venue prestige entered any judgment; weights derive
  from study design, calibration traceability, uncertainty reporting,
  conditions, controls, replication, relevance, and disclosed limitations.
- Retraction rule: nothing in this set is retracted (0/8), so no claim
  rests on retracted work. No unresolved correction or peer-review status
  exists in this set (P0006's fast review timeline is a disclosed caveat,
  not an unresolved status).
- WebFetch summaries are produced by an automated extraction layer; where a
  number was load-bearing this run quoted it exactly as returned, and
  flags remain (e.g. whether P0004's irradiation figure originates inside
  P0004 or in the group's earlier campaigns — recorded as a limitation, not
  resolved).
- P0007's full text is paywalled; adjudication used the open landing-page
  record.
- Eight papers cannot support corpus-level statements; every count and
  conclusion here is pilot-scoped.

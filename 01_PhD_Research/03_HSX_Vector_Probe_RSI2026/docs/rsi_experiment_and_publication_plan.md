# RSI 2026–27: Calibrated vector Hall probe in HSX — experiment & publication plan

**Working title:** *A calibrated three-axis AlGaN/GaN Hall-effect probe
with spinning-current readout for in-vessel magnetic field measurements
in the HSX stellarator*

**Target journal:** Review of Scientific Instruments (regular article).
**Target submission:** ~March 2027. **First author:** Y. Zhao.

**Scope statement (fixed):** this campaign measures plasma and magnetic
fields inside HSX. No neutron or gamma irradiation experiments are
performed or claimed. Radiation response is covered by the co-authored
TCAD modeling manuscript (Van Gorp, Dawes, Zhao, Senesky, in prep.),
which is cited as complementary work; experimental radiation hardness
appears, at most, as one sentence of outlook.

---

## 1. Where the trajectory stands, and the gap this paper fills

The 2023 Sensors Letters paper established feasibility: a packaged
AlGaN/GaN Hall sensor survived 68 consecutive HSX shots in-vessel and
tracked plasma-dependent field dynamics in real time. Its own text
concedes the limits — the sensor was voltage-biased with an uncalibrated
offset V_off, produced a single axis, and validated only by *temporal
correlation* with the diamagnetic loop. Its stated future work was
absolute calibration against HSX magnetic diagnostics, extended-duration
offset stability, and lower-noise readout.

Project 02 (bench now, HSX install Aug 2026) already answers the
single-axis half of that list: 100 µA current bias, four-phase
spinning-current with polarity chopping (kills plate and amplifier
offsets by construction), AD8429 readout, and a traceable Helmholtz +
in-situ calibration path. What it does not do is measure a vector, and a
single scalar component is a weak instrument in a machine whose whole
identity is field *geometry* — HSX is the first quasi-helically
symmetric stellarator, and its diagnostics literature (Pfirsch–Schlüter
current measurements, equilibrium-reconstruction optimization) is about
field direction and structure, not just magnitude.

The lab lineage also points at RSI specifically: the group's
high-temperature 2DEG sensitivity paper (Alpert et al. 2020) is an RSI
article, and the canonical fusion-magnetics instrument papers (e.g.
Strait's DIII-D magnetic diagnostic system) live there too. An
instrument paper — *what was built, how it was calibrated, traceability,
quantified in-machine performance* — is exactly RSI's format.

**Thesis of the paper:** the first absolutely calibrated, multi-axis
(2–3 component) GaN Hall-effect probe operated inside a stellarator,
with offset suppression by spinning-current demonstrated in-vessel, and
vector output validated quantitatively against the computed vacuum field
and HSX's standard diagnostics — upgrading 2023's "temporal correlation"
to numbers with uncertainties.

Contribution list (for the intro, and for reviewers):
1. Vector measurement: 2–3 orthogonal AlGaN/GaN plates in one compact
   UHV-compatible ceramic cube package.
2. In-vessel spinning-current operation: offset-free readout at the
   probe, with measured long-sequence offset stability vs the 2023
   uncalibrated baseline.
3. Absolute calibration chain: bench Helmholtz (matrix calibration,
   traceable to geometry + 0.1 % shunt) anchored in situ by coil-only
   shots against the computed vacuum field at a surveyed probe pose.
4. Quantified plasma measurements: component-resolved ignition
   transients and discharge dynamics with an uncertainty budget.

---

## 2. Instrument

### 2.1 Gen-2 sensor dies (larger bond pads)

Pad enlargement doesn't move first-order sensitivity: S_I ≈ r_n·G_H/(q·n_s)
is set by the 2DEG sheet density and plate geometry, both unchanged. What
it plausibly improves is exactly what a cube package stresses — wirebond
yield (especially on non-horizontal faces), bond placement tolerance, and
contact resistance (→ lower 1/f contact noise and raw offset). What it
may quietly change is the terminal-to-terminal plate resistance and the
effective shape factor if the metal encroaches on the octagon.

Incoming inspection per die, before any packaging (half a day for a
batch):
- Full 2-terminal resistance map across all pin pairs; compare against
  the 2023 signature (~650 Ω opposite-pair). **If R changed, update the
  emulator arm value (649 Ω today) and the bias-return loading factor
  (0.83 today) in `../02_.../docs/SPECS.md` — the ±26 mV emulator
  expectation moves with them.**
- 3-terminal contact-resistance estimate on a sample of pads.
- Raw offset distribution at 100 µA across the batch (pick matched dies
  for the cube).
- Spot-check S_I with the Helmholtz on one packaged sample; expect
  ≈ 60 V/A/T unchanged.

### 2.2 Cube module

Concept: the proven single-die process — die → LCC (Spectrum), Al wedge
bonds, EPO-TEK 353ND encapsulation, 150 °C vacuum bake — repeated per
face on a machinable ceramic (or zirconia, matching the 2023 holder)
cube, LCCs on 2 or 3 mutually orthogonal faces. Nothing new is qualified
except the cube itself and the face-mount adhesive/bake compatibility.

Design points to settle in September:
- Cube size: set by LCC footprint + routing clearance; keep the probe
  head compact enough for the existing standoff/graphite-shield concept
  (shield likely needs a resize, not a redesign).
- Face flatness/orthogonality spec: the calibration matrix absorbs
  fixed misalignment, so ±1° machining is acceptable — but it must be
  *stable* through bake and thermal cycling.
- Bond accessibility on vertical faces: this is the yield risk the
  larger pads exist to mitigate. Plan a mechanical-sample bond trial
  before committing flight dies.
- 2 vs 3 axes: build for 3; if bond yield or feedthrough pins force it,
  a 2-axis module is still a publishable vector instrument (state the
  choice honestly in the paper).

### 2.3 Readout: replicate the 02 board per axis

Decision: **three copies of `hsx_2026_v1`** rather than a new
multi-channel board rev. Rationale: the gerber/order package already
exists (`../02_.../circuit/hsx_setup_v1_Y23.zip`, hand-assembly — budget
real bench days for two more builds), the design will have a full
bring-up campaign of heritage by September, and channel isolation comes
free (independent amps, independent floating supplies). A rev-B
3-channel board is strictly nicer and strictly riskier before a travel
date; park it as future work.

Synchronization: **one Pico 2 fans out the shared a0/a1/a2/EN** to all
three boards (each line drives three CMOS mux inputs — trivial load).
All axes spin in phase, so one sync line (GP19) timestamps all three
demods and inter-axis phase skew is zero by construction. Grounds: each
board's GND1 commons at the scope via its SMA shield; bond the Pico
ground once, star-style, and verify no inter-board loop before the
trip.

Bias: one floating ~100 µA source **per board** (REF200-style or the
battery box used in bring-up); do not share a source across plates —
the spinning muxes would fight over it.

### 2.4 Harness and feedthrough (open item #1 — ask UW early)

Three plates × 4 wires = **12 signal conductors** (plus shields). The
2023 single-axis harness used 4 pins of a DSUB-9. Options: one DB-15
(12 + spares/shield) or two DSUB-9s. **Action, July:** email Wayne/
Thomas for the available feedthrough pin count and connector type on the
intended port; this decides the harness build and possibly the 2-vs-3
axis question. Keep per-plate pairs twisted; keep the 2023 pin
convention (bias pair / sense pair) per plate so the boards drop on.

### 2.5 DAQ and the scope-memory question (open item #2)

The DSOX1204G's four channels map perfectly: CH1–3 = v_x, v_y, v_z,
CH4 = sync. Memory does not map perfectly: ~2 Mpts shared → ~500 kpts
per channel with all four on. The demod wants ≥ ~10 samples per 25 µs
phase (f = 40 kHz), i.e. ≥ ~0.4–1 MSa/s. So per shot, pick one:

| Strategy | Settings | Covers | Cost |
|---|---|---|---|
| A. Ignition window | 1 MSa/s, ~300–500 ms capture, trigger near ECRH | breakdown + discharge, misses coil ramp | none — default |
| B. Full shot, slower spin | f = 10–20 kHz, 250–400 kSa/s, ~1.2 s | whole shot incl. ramp | demod BW drops to ~0.3–0.5 kHz |
| C. HSX DAQ channels | demod offline from their record | whole shot, their timebase | integration effort + their sampling limits |

Run A as the workhorse, B for a few dedicated ramp-study shots, and
pursue C opportunistically — it also solves the ~30 ms trigger-offset
annoyance from 2023 by putting everything on one clock. Decide by
end of October bench work.

---

## 3. Calibration plan (the heart of the paper)

### 3.1 Per-axis scalar calibration
Reuse the project-02 Week-3 protocol per channel: bipolar Helmholtz
sweeps (±2.7 mT), sensitivity-vs-bias linearity at 50/100/200/500 µA,
AC response 10 Hz–3 kHz, hotplate 25–100 °C coefficient, overnight
drift. Targets unchanged: ~2 % absolute, < 0.5 % linearity.

### 3.2 Vector (matrix) calibration
Model: **v = M·B + b**, with v the three demodulated outputs, M a 3×3
matrix (per-axis gains on the diagonal, misalignment + cross-sensitivity
off-diagonal), b residual offsets (should be ~0 with spinning — measure
it anyway; it's a headline number).

Method: single-axis Helmholtz + a 3D-printed indexing cradle that holds
the cube in each of the six ±face orientations (90° indexed) plus two
45° checks. At each orientation, sweep B over ±2.5 mT and record all
three channels. Least-squares fit of M and b (24+ sweep-orientation
combinations, 12 unknowns — well over-determined; report residuals).
Extract and report the misalignment angles from the polar decomposition
of M — expect ~1–2° from assembly. Checks: planar-Hall cross-talk (drive
B in-plane of each die, confirm second-order), per-die temperature
coefficient (cube on hotplate), repeatability after a thermal cycle and
after re-mounting in the cradle.

### 3.3 In-situ absolute anchor (the RSI centerpiece)
HSX coil-only shots produce a vacuum field that is *computable* at any
point from the coil currents and geometry. With the probe pose (position
+ orientation) surveyed on its mount, the predicted vector **B_vac** at
the probe is compared against **M⁻¹(v − b)** — a quantitative,
component-by-component absolute check inside the machine, at multiple
field settings. This single figure upgrades the 2023 paper's
correlation-only validation into calibration traceability, and it is
what makes the paper an instruments paper rather than a demo. Requires:
(a) surveyed mount pose (photogrammetry or fixture CAD + machinist
survey; ±1 mm, ±0.5–1° is enough for a ~2 % / ~2° budget), (b) UW's
vacuum-field computation at that pose for the requested settings — both
go in the July email.

### 3.4 Uncertainty budget (drafted now, filled by data)

| Term | Expected size | Comes from |
|---|---|---|
| Helmholtz field constant | ~1 % | geometry + 0.1 % shunt, pickup-coil cross-check |
| Matrix fit residuals | < 0.5 % | §3.2 fit |
| Pose survey → predicted B_vac | ~1 % / ~1° | §3.3 survey |
| Temperature coefficient over shot | small; measured | hotplate data + in-vessel ΔT |
| Noise per axis | 25–30 µT rms @ 1 kHz ENBW | bench PSD, re-verified in-vessel |
| **Total (goal)** | **≤ 2–3 % magnitude, ≤ 2° direction** | |

---

## 4. HSX campaign #2 (target November 2026)

Objectives, in priority order:
1. **Coil-only absolute validation** at 2–3 field settings, repeated —
   the §3.3 anchor. This is the must-have; everything else is upside.
2. **Vector plasma dynamics:** component-resolved ignition transient and
   discharge fluctuations across the same discharge taxonomy as 2023
   (high-energy / late-breakdown / failed-breakdown) for continuity.
3. **Offset stability, spinning on:** a long repeated-shot sequence (and
   idle dwell between shots) tracking b(t) — the direct, quantified
   answer to 2023's V_off problem.
4. Opportunistic: compare measured field direction against
   equilibrium-reconstruction expectations (Chlechowitz-style) with the
   UW team — a physics hook, and co-author engagement.

Shot-list request to Wayne/Thomas (send with the July email):

| Ask | Shots | Purpose |
|---|---|---|
| Coil-only, setting 1/2/3, ×3 each | ~9 | absolute anchor + repeatability |
| Biased vs unbiased, per axis | ~6 | artifact check, continuity with 2023 Fig. 4 |
| High-energy discharge repeats | ~6 | vector dynamics statistics |
| Late-/failed-breakdown | ~4 | taxonomy continuity |
| Long sequence, fixed setting | ~10+ | offset stability |
| Mount survey + vacuum-field calc at pose | — | §3.3 |
| Trigger/clock tie-in or offset characterization | — | fix the ~30 ms DAQ offset |

Plus a shot-replay rehearsal at Stanford in October (wavegen playback of
2023 traces through the full 3-channel chain, long cable, EMI checks) so
the trip burns zero shots on debugging — same philosophy as the Week-4
rehearsal in the 02 plan.

---

## 5. Paper skeleton and figure plan

Skeleton (RSI conventions): I. Introduction (fusion magnetics drift
problem → Hall alternative → GaN for in-vessel → 2023 demo and its
gaps → this instrument). II. Probe design (dies, cube package,
harness). III. Readout (spinning-current theory recap, per-axis boards,
synchronization, DAQ). IV. Calibration (scalar, matrix, in-situ anchor,
uncertainty budget). V. HSX results (coil-only validation, vector
plasma dynamics, offset stability). VI. Discussion & outlook (rev-B
integrated multichannel readout; radiation response per the co-authored
TCAD modeling — cited, not performed). VII. Conclusion.

| Fig. | Content |
|---|---|
| 1 | Cube module: photo + exploded schematic, die/LCC/faces, in-vessel mount |
| 2 | 3-channel readout architecture with shared clock fan-out + timing diagram |
| 3 | Matrix calibration: orientation sweeps, fitted M, residuals; misalignment angles |
| 4 | **In-situ anchor: measured vs computed vacuum field, per component, per setting** |
| 5 | Vector dynamics through ignition (three components + \|B\|), discharge taxonomy |
| 6 | Offset stability over the shot sequence vs the 2023 uncalibrated baseline |
| T1 | Uncertainty budget · T2 | 2023 system vs this work (seed table in SPECS.md) |

---

## 6. Timeline (gates in bold)

| When | Work |
|---|---|
| Jul 2026 | 02 bring-up + calibration (running). **Send UW email: feedthrough pins, mount survey, vacuum-field calc, shot-list ask.** Order 2 more boards' parts. |
| Aug 2026 | HSX campaign #1 (single axis) — doubles as method pathfinder. **Gate: single-axis calibration + in-vessel operation validated.** |
| Sep 2026 | Gen-2 die incoming inspection; cube bond trial then assembly ×2 units; build boards 2–3; harness per UW answer. **Gate: 3 working channels on the bench; 2-vs-3-axis decision.** |
| Oct 2026 | 3-channel bench bring-up, matrix calibration, thermal + drift, shot-replay rehearsal. **Gate: uncertainty budget ≤ targets; DAQ strategy fixed.** |
| Nov 2026 | HSX campaign #2. |
| Dec–Jan | Analysis: M validation, vector reconstruction, stability stats. |
| Feb 2027 | Full draft; internal review (Senesky + UW co-authors); `rsi-editor` passes. |
| ~Mar 2027 | Submit to RSI. |

Slack: December–January absorb slip; the immovable object is the
November machine time — protect the September/October gates.

---

## 7. Risk register

| Risk | L | I | Mitigation |
|---|---|---|---|
| Bond yield on cube faces | M | H | larger pads (that's their job); bond trial on mechanical sample; spare dies; 2-axis fallback |
| Feedthrough pins < 12 | M | M | ask in July; 2-axis fallback; second connector |
| Channel gain/phase skew | L | M | shared clock kills phase skew; matrix cal absorbs gain; verify with emulator on all 3 inputs |
| Alignment error dominates vector budget | M | M | matrix cal + polar-decomposition report; pose survey; 45° check orientations |
| Scope memory insufficient | M | M | §2.5 strategies A/B/C; decide in October |
| Plate R changed by pad redesign | M | L | incoming inspection; update SPECS/emulator before bench work |
| Schedule (hand assembly ×2 boards) | M | M | order parts in July; assemble in September, not October |
| Campaign #1 findings force readout changes | L | H | that's why #1 precedes the board builds — fold fixes into boards 2–3 |

---

## 8. Bench/BOM additions (rough)

Two more board builds (PCBs already designed; parts ~$120 ea), DB-15 (or
2× DSUB-9) harness parts ~$40, 3D-printed indexing cradle ~$10, second
and third floating 100 µA sources ~$30 ea, MLX90393 3-axis reference
breakout ~$15 (cross-check on the Pico I²C bus, per the 02 Helmholtz
traceability plan), ceramic cube machining — quote needed (the one real
unknown). Everything else (Helmholtz, scope, Pico, shunt) carries over
from project 02.

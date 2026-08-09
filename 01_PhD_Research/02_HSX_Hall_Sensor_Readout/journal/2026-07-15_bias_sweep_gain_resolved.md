# Research Journal — 2026-07-15

## Bias-current sweep on the emulator — the 109× magnitude anomaly is closed

**Owner:** Y. "Tim" Zhao · **Project:** 02_HSX_Hall_Sensor_Readout ·
**Session type:** sensorless (emulator) bring-up, plan §4 Day 3–4.

**Source of this entry:** the 2026-07-15 group-meeting deck, slides 4–6. This
is a *derived* record — the raw scope captures behind slide 6 are not in the
repository. Extracted numbers live in `data/2026-07-15_bias_sweep.csv` and
`data/2026-07-15_emulator_phase_table.csv`; the figures are mirrored in
`analysis/figures/`. Replace the digitized points with the primary captures
when they turn up.

**Headline: the ~109× shortfall from 2026-07-08 is resolved.** The readout now
tracks the bridge model to within ~8 %, and the amplifier is demonstrably
running at its design gain. One second-order discrepancy (the effective bridge
imbalance) is newly open and is why absolute calibration is still not locked.

---

## 1. What was measured

Same emulator as 2026-07-08 — four 680 Ω arms with 2.2 kΩ across one of them
(`analysis/figures/2026-07-15_emulator_bridge_schematic.png`) — with the bias
current swept instead of parked at 20 mA.

| Bias current | Per-phase output amplitude | Regime |
|---|---|---|
| 100 µA | ≈ 0.55 V | linear |
| 500 µA | ≈ 1.95 V | linear |
| 1 mA | ≈ 3.70 V | linear |
| 2 mA | ≈ 7.10 V | linear |
| 5 mA | ≈ 13.9 V | **clipped at the rail** |
| 10 mA | ≈ 14.2 V | **clipped at the rail** |

Printed on the figure, and exact as quoted:

- measured linear fit **3.46 V/mA**
- predicted **3.74 V/mA**
- supply rail **±13.7 V**

Slide 5 also gives the per-state model behind that prediction: the differential
at the amplifier input is **±37.26 Ω · I**, and the eight signed products sum to
zero — i.e. the emulator offset cancels, as designed.

---

## 2. Verification — is the anomaly actually resolved?

**Yes. Three independent checks agree.**

### 2.1 The prediction line is the same model that produced "~75 V"

37.26 Ω × 100.3 = **3.737 V/mA**, which is the "predict 3.74 V/mA" printed on
slide 6. Extrapolated to the old operating point: 3.737 V/mA × 20 mA =
**74.7 V**, matching the "~75 V" in the 2026-07-08 entry. So this sweep is
being compared against *exactly* the model that the anomaly was defined
against — not a re-derived or softened one.

### 2.2 The discrepancy collapsed from 109× to 1.08×

| | 2026-07-08 | 2026-07-15 |
|---|---|---|
| Predicted | 74.7 V @ 20 mA | 3.74 V/mA |
| Measured | 0.686 V | 3.46 V/mA |
| Ratio | **109× low** | **1.08× low (7.4 %)** |

### 2.3 The clipping proves the gain independently of any fit

At 5 mA the differential into the amplifier is only 37.26 Ω × 5 mA = **186 mV**,
yet the output is hard against the ±13.7 V rail. Reaching that rail from 186 mV
requires a gain of **at least 74**. You cannot clip a ±13.7 V supply from a
sub-200 mV differential without roughly the design gain — so G ≈ 100 is real,
in operation, and no curve-fitting is involved in that conclusion.

Under the failed-gain hypothesis (G ≈ 1) the 10 mA point would have produced
0.373 V. It produced a clipped ~14 V.

---

## 3. What the original fault was

The 2026-07-08 entry listed two candidates and the test that would tell them
apart: *differential ≈ 0.75 V ⇒ candidate 1 (gain is not ~100× in operation);
differential ≈ 7 mV ⇒ candidate 2 (the 2.2 kΩ imbalance is ineffective).*

The arithmetic now settles it:

- Bridge differential at 20 mA = 37.26 Ω × 20 mA = **745 mV**.
- Measured on 2026-07-08 = **686 mV**.
- 686 / 745 = **0.92** — i.e. the signal chain that day had a gain of ~0.92,
  essentially **unity**, not 100.3.
- 100.3 / 0.92 = **109.0** — the anomaly factor, exactly.

So on 2026-07-08 the scope was reading the bridge differential essentially
**unamplified**. That is **candidate 1**, precisely as the ΔV gain check was
designed to detect, and it explains the factor to three significant figures
rather than approximately.

**Candidate 2 is ruled out.** If the 2.2 kΩ were not unbalancing the bridge,
the output would not scale as ~37 Ω · I · G and could not clip at 5 mA.

⚠️ **Inference, not a recorded fact.** The deck shows the *result*, not the
repair. Nothing in it states what was changed between 08 and 15 July — an
R_G/in-amp contact, a probe on the wrong node, a scope attenuation setting.
The magnitude evidence for "the amplifier was not amplifying that day" is
strong and self-consistent, but the physical root cause should be written down
from bench memory while it is still fresh. **Until that is recorded, treat the
mechanism as probable and the resolution as demonstrated.**

---

## 4. Newly open — the effective bridge imbalance

The deck's model uses **37.26 Ω**. Computing the same quantity from the ideal
schematic on slide 5 (four 680 Ω arms, 2.2 kΩ across one, current in at the top
node, sense across the two mid-nodes) gives:

```
R2 ∥ R5 = 680·2200/2880       = 519.4 Ω
branches: 1360 Ω  and  1199.4 Ω
|V(L) − V(R)| per amp of bias  = 42.66 Ω
```

**42.66 Ω, not 37.26 Ω — a 12.7 % gap**, and the measured slope implies
3.46 V/mA ÷ 100.3 = **34.5 Ω**, which is 19 % below the ideal-schematic value.

So the "7.4 % low" headline is measured against the deck's own 37.26 Ω. Against
the schematic it is 19 % low. Candidate explanations, none verified:

1. mux on-resistance inside the sensed arms (ADG1209/ADG5236) shifting the
   effective divider — plausible and checkable from the datasheets plus a DMM;
2. resistor tolerance — the imbalance is a *difference* of near-equal
   quantities, so 1 % parts can move it several percent, though 19 % is a
   stretch;
3. the deck's 37.26 Ω already includes a correction not written on the slide.

This is a second-order modelling question, not a repeat of the anomaly. It does
not affect the verdict in §2 — but it does mean **the absolute V/T calibration
must not be locked to the emulator until the imbalance model is reconciled.**

---

## 5. Consequences for the real sensor

The sweep also fixes the usable operating window, which matters because the
2026-07-08 entry flagged 20 mA as ~20× above the intended die current:

- **Linear to ~2 mA, clipped by 5 mA** on this emulator at G = 100.3.
- Rail-limited maximum differential ≈ 13.7 V / 100.3 = **137 mV** at the
  amplifier input.
- The intended ≤ 1 mA operating point for the real GaN die sits comfortably
  inside the linear range — at 1 mA the emulator gave ≈ 3.7 V, about 27 % of
  full scale. Good headroom without self-heating the die.
- 20 mA is now understood to be *past clipping* on this emulator, so the
  2026-07-08 capture should not be re-used for any magnitude work.

---

## 6. Plan status change (§4 Day 3–4)

| Plan item | Was | Now |
|---|---|---|
| **ΔV gain verification, G = 100.3 ±1 %** | ✗ not done — TOP PRIORITY | **✓ done in effect** — gain confirmed ≥74 by rail clipping and 92.5 % of prediction by slope. Not yet a formal ±1 % ΔV measurement. |
| Absolute-magnitude anomaly | ◑ open | **✓ closed** |
| Bias-current linearity / headroom | not on the plan | **✓ done** — linear ≤ 2 mA, clipped ≥ 5 mA |
| Effective bridge imbalance model | not on the plan | ◑ **new open item** — 34.5 / 37.26 / 42.66 Ω disagree |

Everything else from the 2026-07-08 "next session" list is still outstanding:
static 8-state DMM survey, sync-channel capture, noise-floor PSD, frequency
sweep, rail-ripple spectrum, board log.

---

## 7. Next session

1. **Write down what was actually fixed** between 08 and 15 July (§3). One
   sentence in `NOTES.md` closes the loop properly.
2. **Reconcile the bridge imbalance** (§4): DMM the four arms and the 2.2 kΩ
   in-circuit, measure the amp-input differential directly at a held state, and
   compare against 34.5 / 37.26 / 42.66 Ω.
3. Get the **raw captures** for the 2026-07-15 sweep into `data/` so the
   digitized CSV can be replaced with primary data.
4. Then resume the outstanding §6.1 items — sync capture first, since the noise
   floor is still quantization-limited without it.
5. Only after (2): set the emulator operating point and start absolute
   calibration.

---

## 8. Also in the deck (not readout data)

Slide 3 shows a 3-axis package concept — three sensor bodies on a CF flange
with a multipin feedthrough, ~1.250 in diagonal envelope. That belongs to
`03_HSX_Vector_Probe_RSI2026`, not here, and is recorded only as a pointer.
Slide 7 (Magnify) is out of scope by request and was not read.

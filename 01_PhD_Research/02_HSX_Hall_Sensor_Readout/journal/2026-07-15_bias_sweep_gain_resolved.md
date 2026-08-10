# Research Journal — 2026-07-10 bench session (presented 2026-07-15)

## Bias-current sweep on the emulator — the 109× magnitude anomaly is closed

**Owner:** Y. "Tim" Zhao · **Project:** 02_HSX_Hall_Sensor_Readout ·
**Session type:** sensorless (emulator) bring-up, plan §4 Day 3–4.

**Captures:** 2026-07-10, 18:32–18:42 (10 kHz set) and 19:08–19:10 (40 kHz set
with sync), DSO-X 4022A. Presented in the 2026-07-15 group meeting, slides 4–6.

**Primary data is in the repository**: `data/2026-07-10_bias_sweep/` (nine
DSO-X CSV exports). Everything below is computed from it by
`analysis/bias_sweep_analysis.py`; summary in
`data/2026-07-10_bias_sweep_summary.csv`, figures in `analysis/figures/`.
*This entry originally quoted points digitized off the slide; those have been
replaced by the measured values, which shifted the small-current points by up
to 40 % and the fitted slope by 0.3 %.*

**Headline: the ~109× shortfall from 2026-07-08 is resolved.** The readout
tracks the bridge model to ~7 %, and the amplifier is demonstrably running at
its design gain. Two things are newly open: the effective bridge imbalance, and
the choice of spin rate (§5).

---

## 1. What was measured

Same emulator as 2026-07-08 — four 680 Ω arms with 2.2 kΩ across one of them —
with the bias current swept instead of parked at 20 mA.

Amplitude is the mean |per-state mean − pedestal| after folding on the recovered
phase rate and discarding 45 % of each phase at its edges.

| Bias | Amplitude | V/mA | Regime |
|---|---|---|---|
| 100 µA | 0.330 V | 3.30 | linear |
| 500 µA | 1.694 V | 3.39 | linear |
| 1 mA | 3.436 V | 3.44 | linear |
| 2 mA | 6.915 V | 3.46 | linear |
| 5 mA | 13.754 V | — | **clipped at the rail** |
| 10 mA | 13.766 V | — | **clipped at the rail** |

Fit over the unclipped points: **3.469 V/mA** least-squares (intercept −29 mV),
**3.450 V/mA** through the origin. The slide prints 3.46 V/mA — **reproduced to
0.3 %**. Supply rail **±13.7 V**.

The per-state model on slide 5 gives the differential at the amplifier input as
**±37.26 Ω · I**, with the eight signed products summing to zero
(`data/2026-07-15_emulator_phase_table.csv`).

### Spin rate — not stated on the slide, recovered from the data

The captures do not record the phase rate, so it was recovered by folding
(grid-search the phase duration, score the residual about the eight per-state
means) and cross-checked against sync where available:

| Set | Phase | Phase rate | Sampling | Fold score |
|---|---|---|---|---|
| 100 µA, 500 µA, 1 mA, 2 mA, 5 mA, 10 mA | 100.0 µs | **10.0 kHz** | 195.5 kSa/s | 0.98–1.00 |
| 500 µA, 1 mA, 2 mA `_v2` | 25.0 µs | **40.0 kHz** | 3.906 MSa/s | 0.99–1.00 |

The `_v2` captures recorded sync on CH1; its period gives 40.013 kHz,
agreeing with the folded 39.5–40.4 kHz to better than 2 %. Only two of the six
10 kHz folders were labelled `_10khz`; **all six are at 10 kHz.**

**Slide 6 is therefore the 10 kHz set** — a quarter of the 40 kHz SPECS nominal.
The 40 kHz `_v2` set is later, better instrumented, and is not on the slide.

---

## 2. Verification — is the anomaly actually resolved?

**Yes. Three independent checks agree.**

### 2.1 The prediction line is the same model that produced "~75 V"

37.26 Ω × 100.3 = **3.737 V/mA**, which is the "predict 3.74 V/mA" printed on
slide 6. Extrapolated to the old operating point: × 20 mA = **74.7 V**, matching
the "~75 V" in the 2026-07-08 entry. So this sweep is compared against *exactly*
the model the anomaly was defined against.

### 2.2 The discrepancy collapsed from 109× to 1.08×

| | 2026-07-08 | 2026-07-10 |
|---|---|---|
| Predicted | 74.7 V @ 20 mA | 3.737 V/mA |
| Measured | 0.686 V | 3.469 V/mA |
| Ratio | **109× low** | **1.08× low (7.2 %)** |

### 2.3 The clipping proves the gain independently of any fit

At 5 mA the differential into the amplifier is only 37.26 Ω × 5 mA = **186 mV**,
yet the output is hard against the ±13.7 V rail. Reaching that rail from 186 mV
requires a gain of **at least 74**. No curve-fitting is involved. Under the
failed-gain hypothesis (G ≈ 1) the 10 mA point would have produced 0.373 V; it
produced a clipped 13.77 V.

---

## 3. What the original fault was

The 2026-07-08 entry listed two candidates and the test that would separate
them: *differential ≈ 0.75 V ⇒ candidate 1 (gain is not ~100× in operation);
≈ 7 mV ⇒ candidate 2 (the 2.2 kΩ imbalance is ineffective).*

- Bridge differential at 20 mA = 37.26 Ω × 20 mA = **745 mV**.
- Measured on 2026-07-08 = **686 mV**.
- 686 / 745 = **0.92** — a signal chain running at ~unity gain, not 100.3.
- 100.3 / 0.92 = **109.0** — the anomaly factor, exactly.

So on 2026-07-08 the scope was reading the bridge differential essentially
**unamplified**: **candidate 1**, to three significant figures.

**Candidate 2 is ruled out.** If the 2.2 kΩ were not unbalancing the bridge, the
output could not scale as ~37 Ω · I · G, nor clip at 5 mA.

⚠️ **Inference, not a recorded fact.** Nothing in the deck or the captures states
what changed between 08 and 10 July — an R_G/in-amp contact, a probe on the
wrong node, a scope setting. The magnitude evidence is strong and
self-consistent, but **the physical root cause should be written down from bench
memory.**

---

## 4. Open — the effective bridge imbalance

The deck models **37.26 Ω**. From the ideal schematic on slide 5 (four 680 Ω
arms, 2.2 kΩ across one, current in at the top node, sense across the two
mid-nodes):

```
R2 ∥ R5 = 680·2200/2880       = 519.4 Ω
branches: 1360 Ω  and  1199.4 Ω
|V(L) − V(R)| per amp of bias  = 42.66 Ω
```

Three values disagree: **34.59 Ω** measured (3.469 V/mA ÷ 100.3), **37.26 Ω**
deck, **42.66 Ω** ideal schematic. Against the schematic the measurement is 19 %
low, not 7 %.

Candidates, none verified: mux on-resistance inside the sensed arms shifting the
divider; resistor tolerance (the imbalance is a *difference* of near-equal
quantities, so 1 % parts move it several percent — but 19 % is a stretch); or a
correction already folded into the deck's 37.26 Ω that isn't written down.

Second-order, and it does not affect §2 — but **the absolute V/T calibration
must not be locked to the emulator until this is reconciled.**

---

## 5. Spin rate — 10 kHz is too slow, 40 kHz costs nothing

The `_v2` set repeats three bias points at 40 kHz, which makes this a controlled
comparison:

| Bias | 10 kHz | 40 kHz | Δ |
|---|---|---|---|
| 500 µA | 1.694 V | 1.729 V | +2.1 % |
| 1 mA | 3.436 V | 3.437 V | +0.1 % |
| 2 mA | 6.915 V | 6.908 V | −0.1 % |

Slope 3.450 V/mA at 10 kHz vs 3.451 V/mA at 40 kHz. **Quadrupling the spin rate
costs no amplitude.** The +2.1 % at 500 µA is the noisiest point, not a trend.

**Why:** settling after a phase edge, ensemble-averaged over the 3.9 MSa/s
captures, reaches 5 % of the step at **3.6 µs** and 1 % at **3.8 µs** (the floor
is the scope's ~167 mV quantization, so the true settling is at least this
fast). Against a 25 µs phase that is 14 %; against 100 µs, 4 %. Both are
comfortable — 10 kHz just wastes the margin.

What the spin rate buys, given 8 states per cycle (update = f/8, signal
bandwidth ≤ f/16):

| f | Phase | Settling as % of phase | Update | Signal BW |
|---|---|---|---|---|
| 10 kHz | 100 µs | 4 % | 1.25 kHz | ≤ 0.6 kHz |
| **40 kHz** (SPECS nominal) | 25 µs | 14 % | 5 kHz | ≤ 2.5 kHz |
| 80 kHz | 12.5 µs | 28 % | 10 kHz | ≤ 5 kHz |
| 100 kHz (SPECS ceiling) | 10 µs | 35 % | 12.5 kHz | ≤ 6.25 kHz |
| 160 kHz | 6.25 µs | **56 %** | 20 kHz | 10 kHz |

**Recommendation: run at 40 kHz.** It is the SPECS nominal, it costs nothing in
amplitude, it gives 4× the demodulated bandwidth, and it keeps the blanking
window generous. 80 kHz is available if bandwidth is the binding constraint;
100 kHz is the practical ceiling.

**The 10 kHz bandwidth on slide 2 is not reachable with 8-state spinning.** It
needs f = 160 kHz, where settling eats 56 % of every phase — above the SPECS
"10k–100k usable" range and with no usable settled window left. The plan already
anticipates this (§8 of the bring-up plan): record raw v_meas and demodulate
offline, or use the static-phase "fast mode" (mode-2 firmware) for fast events.
**Slide 2's claim should be restated** as the raw-chain bandwidth, with the
demodulated bandwidth quoted separately.

---

## 6. Consequences for the real sensor

- **Linear to ~2 mA, clipped by 5 mA** on this emulator at G = 100.3.
- Rail-limited maximum differential ≈ 13.7 V / 100.3 = **137 mV**.
- The intended ≤ 1 mA die operating point sits inside the linear range — at
  1 mA the emulator gave 3.44 V, ~25 % of full scale. Good headroom without
  self-heating the die.
- 20 mA is *past clipping*; the 2026-07-08 magnitudes must not be re-used.

---

## 7. Plan status change (§4 Day 3–4)

| Plan item | Was | Now |
|---|---|---|
| **ΔV gain verification, G = 100.3 ±1 %** | ✗ TOP PRIORITY | **✓ in effect** — ≥74 from rail clipping, 92.8 % of prediction by slope. Not yet a formal ±1 % ΔV measurement. |
| Absolute-magnitude anomaly | ◑ open | **✓ closed** |
| Sync-channel capture | ✗ not done | **✓ done** (the three `_v2` captures) |
| Bias-current linearity / headroom | not on the plan | **✓ done** |
| Frequency study | ◑ partial | **◑ two points** (10 and 40 kHz, identical amplitude); 100 k still untested |
| Effective bridge imbalance model | not on the plan | ◑ **new open item** |

Still outstanding: static 8-state DMM survey, noise-floor PSD, rail-ripple
spectrum, board log.

---

## 8. Next session

1. **Move the spin rate to 40 kHz** and re-take the sweep (§5).
2. **Write down what was actually fixed** between 08 and 10 July (§3).
3. **Reconcile the bridge imbalance** (§4): DMM the arms in-circuit and measure
   the amp-input differential directly at a held state; compare against
   34.59 / 37.26 / 42.66 Ω.
4. Extend the frequency study to 80 and 100 kHz — settling says both should
   work; confirm the amplitude holds and watch the blanking fraction.
5. Noise-floor PSD, now that sync capture works and the record isn't
   quantization-limited.
6. Only after (3): set the operating point and start absolute calibration.

---

## 9. Also in the deck (not readout data)

Slide 3 shows a 3-axis package concept — three sensor bodies on a CF flange with
a multipin feedthrough, ~1.250 in diagonal envelope. That belongs to
`03_HSX_Vector_Probe_RSI2026`. Slide 8 (Magnify) is out of scope by request and
was not read.

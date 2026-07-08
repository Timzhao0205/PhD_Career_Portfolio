# Pico 2 firmware — wiring, flashing, usage (two operating modes)

This folder is the complete Pico 2 (RP2350) firmware for the HSX
Hall-sensor readout board. Since 2026-07-08 it is organized as **two
separate, self-contained mode files** plus a boot chooser:

| File | Mode | What it does | DAQ instrument |
|---|---|---|---|
| `pico2_spin_scope.py` | **1 — spin + scope** | Full current-spinning: PIO-generated a0/a1/a2 + sync (atomic single-edge updates), EN sequencing, static holds, guided 8-state survey | **Oscilloscope** (DSOX1204G): CH-a = v_meas, CH-b = sync; offline demod via `analysis/hsx_demod_scope_csv.py` |
| `pico2_static_bias_p2p4.py` | **2 — static bias p2/p4** | Second test setup: parks the muxes so the **external current source biases p2 → p4** and the amp reads the **p1/p3 difference**; 4-state chop (states 2/3/6/7) cancels amplifier offset; CSV drift logging | **Pico ADC** (GP26/ADC0 ← J4), 256× oversampled — no scope needed |
| `main.py` | boot entry | Asks which mode to run at power-up; safe boot (EN low) | — |
| `pico2_hsx_phase_clock.py` | heritage | The original single-mode module (same API as mode 1). Kept so old notes/sessions still work; new work uses the mode files | scope |

Details of the second test setup (theory, expected numbers, limits):
`../../docs/second_test_setup_static_bias.md`.

## Wiring table

| Signal | Pico GPIO | Pico physical pin | Connects to                     | Board test point | Used in mode | Notes |
|--------|-----------|-------------------|---------------------------------|------------------|--------------|-------|
| a0     | GP16      | 21                | J3 pin 3                        | TP3              | 1 + 2        | LSB — toggles at f/2 when spinning |
| a1     | GP17      | 22                | J3 pin 2                        | TP2              | 1 + 2        | held HIGH in mode 2 (p2/p4 axis) |
| a2     | GP18      | 24                | J3 pin 1                        | TP1              | 1 + 2        | chopper select |
| sync   | GP19      | 25                | Scope CH-b / external trigger   | —                | 1            | high only during state 0; never wired to J3; driven low in mode 2 |
| en     | GP20      | 26                | J3 pin 4                        | TP4              | 1 + 2        | board has a pulldown → dead until driven ≥ 2 V |
| GND    | —         | 23 (or 28)        | Board GND1                      | —                | 1 + 2        | **mandatory** — J3 has NO ground pin |
| v_meas | GP26/ADC0 | 31                | J4 SMA center                   | —                | 2            | Pico ADC tap; J4's 10 k shunt stays in place |
| AGND   | —         | 33                | J4 SMA shell / GND1             | —                | 2            | keep the ADC return short |

The J3 side lands on one contiguous strip of the Pico header, physical
pins 21–26, with a ground pin (23) conveniently in the middle; mode 2
adds the ADC pair on pins 31/33. 3.3 V logic is sufficient: the
ADG1209/ADG5236 logic threshold V_INH ≈ 2 V.

**Mode-2 ADC caveats (read before trusting numbers):** the RP2350 ADC is
unipolar 0–3.3 V — negative v_meas clamps to ~0 V (the chop sequence
flips signs, so expect it; the module warns). 12-bit ≈ 0.8 mV/LSB,
~few-hundred µV effective after 256× oversampling: fine for health
checks and raw-offset surveys, **not** calibration-grade. Calibration
numbers always come from mode 1 + the scope.

Constraint if you ever re-pin: a0/a1/a2/sync are a PIO `set` group in
mode 1 and **must stay on four contiguous GPIOs in that order** (base =
a0). EN can move to any free GPIO; the ADC tap must stay on an ADC pin
(GP26/27/28). Edit the `PIN_*` constants at the top of each module.

## Flashing (one-time setup)

1. Get MicroPython for Pico 2: https://micropython.org/download/RPI_PICO2/
   (grab the latest `.uf2`).
2. Hold BOOTSEL while plugging the Pico into USB; it mounts as a drive.
   Drag the `.uf2` on; it reboots into MicroPython.
3. Copy the firmware files to the Pico, either with Thonny
   (https://thonny.org — open each file → "Save copy… → Raspberry Pi
   Pico") or with mpremote:

   ```bash
   pip install mpremote
   mpremote cp pico2_spin_scope.py :pico2_spin_scope.py
   mpremote cp pico2_static_bias_p2p4.py :pico2_static_bias_p2p4.py
   mpremote cp main.py :main.py
   mpremote repl        # Ctrl-] to exit
   ```

4. Power-cycle. The mode chooser appears on the USB serial port
   (115200 baud); Enter (or `1`) boots mode 1, `2` boots mode 2.

## Using mode 1 — spinning + oscilloscope DAQ

```python
>>> import pico2_spin_scope as sp
>>> sp.scope_notes()      # DSOX1204G capture checklist for the current f
>>> sp.start(40_000)      # raises EN, then spins at f = 40 kHz
>>> sp.status()           # frequency, state, EN, uptime
>>> sp.hold_state(0b011)  # freeze one of the 8 codes (a2 a1 a0)
>>> sp.survey()           # guided manual 8-state survey (Day-3 test)
>>> sp.stop()             # stops clock, drops EN — do this BEFORE touching
...                       # the DSUB / sensor / emulator plug
```

`f` is the **phase rate**: each of the 8 states lasts 1/f, the full demod
cycle is 8/f (200 µs → 5 kHz update at f = 40 kHz), and a0 toggles at f/2.

Recommended first-power order (runbook §4, Day 2): board powered and
rails verified → Pico GND bonded to GND1 → `start(f)` → confirm
a0/a1/a2/en on TP3/TP2/TP1/TP4 → only then connect the emulator plug.

### Scope / demod handshake

Only two scope channels are used for measurement: CH-a = v_meas (J4 SMA),
CH-b = sync (GP19). The select lines are never captured — the offline
demodulator reconstructs the phase index from the sync rising edges plus
the known f:

```bash
python analysis/hsx_demod_scope_csv.py capture.csv --f 40000
```

The `--f` you pass must match the `start(f)` you used. Sync is high only
in state 0, so every rising edge pins the start of a demod cycle.
`scope_notes()` prints the full capture checklist (sample rate ≥ ~10
samples per phase, trigger on sync, CSV export columns).

## Using mode 2 — static bias p2/p4, Pico ADC

```python
>>> import pico2_static_bias_p2p4 as sb
>>> sb.bias_on()            # EN high, state 010: bias p2 → p4, sense p1/p3
>>> sb.read()               # one oversampled v_meas reading [V]
>>> sb.measure_chopped()    # states {2,3,6,7}, signs {+,−,−,+}:
...                         #   x = (s−o)·loading·G  (amp-offset-free)
...                         #   e = amplifier offset · G
>>> sb.log_csv(600, 2)      # 10 min drift log, one chopped point / 2 s,
...                         # CSV on USB serial (capture on the host)
>>> sb.bias_reverse()       # state 110: current reversed, p4 → p2
>>> sb.stop()               # EN low — BEFORE touching the DSUB
```

Physics reminder: with a single bias axis, the plate offset `o` does
**not** cancel — the chopped result is (s − o)·loading·G, and at zero
applied field it *is* the raw plate offset (the gen-2 incoming-inspection
number). Separating s from o is what mode 1's full 8-state spinning does.

## References

- Pico 2 datasheet: https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf
- RP2350 datasheet: https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf
- MicroPython on Pico: https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
- `rp2.StateMachine` API: https://docs.micropython.org/en/latest/library/rp2.StateMachine.html
- PIO tutorial: https://docs.micropython.org/en/latest/rp2/tutorial/pio.html
- `machine.ADC` API: https://docs.micropython.org/en/latest/library/machine.ADC.html

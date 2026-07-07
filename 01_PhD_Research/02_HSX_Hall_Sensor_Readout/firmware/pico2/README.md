# Pico 2 phase-clock firmware — wiring, flashing, usage

This folder is the complete clock source for the HSX Hall-sensor readout
board. One Raspberry Pi Pico 2 (RP2350) generates the three spinning-mux
select lines (a0/a1/a2), a frame-sync pulse for the oscilloscope, and the
board enable (EN). The select lines and sync come from a single PIO state
machine executing one `set(pins, N)` instruction per phase, so all four
outputs flip on the same clock edge — no software-GPIO skew between bits.
EN is a plain GPIO with explicit safe sequencing.

Files: `pico2_hsx_phase_clock.py` (the module — all logic lives here) and
`main.py` (boot entry: auto-runs the interactive menu over USB serial;
boot is safe, EN stays low until you act).

## Wiring table

| Signal | Pico GPIO | Pico physical pin | Connects to                     | Board test point | Notes |
|--------|-----------|-------------------|---------------------------------|------------------|-------|
| a0     | GP16      | 21                | J3 pin 3                        | TP3              | LSB — toggles at f/2 |
| a1     | GP17      | 22                | J3 pin 2                        | TP2              | |
| a2     | GP18      | 24                | J3 pin 1                        | TP1              | chopper select |
| sync   | GP19      | 25                | Scope CH-b / external trigger   | —                | high only during state 0; never wired to J3 |
| en     | GP20      | 26                | J3 pin 4                        | TP4              | board has a pulldown → dead until driven ≥ 2 V |
| GND    | —         | 23 (or 28)        | Board GND1                      | —                | **mandatory** — J3 has NO ground pin |

Everything lands on one contiguous strip of the Pico header, physical
pins 21–26, with a ground pin (23) conveniently in the middle. 3.3 V
logic is sufficient: the ADG1209/ADG5236 logic threshold V_INH ≈ 2 V.

Constraint if you ever re-pin: a0/a1/a2/sync are a PIO `set` group and
**must stay on four contiguous GPIOs in that order** (base = a0). EN can
move to any free GPIO. Edit the `PIN_*` constants at the top of the
module.

## Flashing (one-time setup)

1. Get MicroPython for Pico 2: https://micropython.org/download/RPI_PICO2/
   (grab the latest `.uf2`).
2. Hold BOOTSEL while plugging the Pico into USB; it mounts as a drive.
   Drag the `.uf2` on; it reboots into MicroPython.
3. Copy both files to the Pico, either with Thonny (https://thonny.org —
   open each file → "Save copy… → Raspberry Pi Pico") or with mpremote:

   ```bash
   pip install mpremote
   mpremote cp pico2_hsx_phase_clock.py :pico2_hsx_phase_clock.py
   mpremote cp main.py :main.py
   mpremote repl        # Ctrl-] to exit
   ```

4. Power-cycle. The menu appears on the USB serial port (115200 baud).

## Using it

At boot, `main.py` runs the text menu — start/stop, set frequency, hold
a static state, enable/disable, status. Ctrl-C drops to the REPL for the
direct API:

```python
>>> import pico2_hsx_phase_clock as pc
>>> pc.start(40_000)      # raises EN, then spins at f = 40 kHz
>>> pc.status()           # frequency, state, EN, uptime
>>> pc.hold_state(0b011)  # freeze one of the 8 codes (a2 a1 a0) — for the
...                       # manual 8-state survey on Day 2
>>> pc.stop()             # stops clock, drops EN — do this BEFORE touching
...                       # the DSUB / sensor / emulator plug
```

`f` is the **phase rate**: each of the 8 states lasts 1/f, the full demod
cycle is 8/f (200 µs → 5 kHz update at f = 40 kHz), and a0 toggles at f/2.

Recommended first-power order (runbook §4, Day 2): board powered and
rails verified → Pico GND bonded to GND1 → `start(f)` → confirm
a0/a1/a2/en on TP3/TP2/TP1/TP4 → only then connect the emulator plug.

## Scope / demod handshake

Only two scope channels are used for measurement: CH-a = v_meas (J4 SMA),
CH-b = sync (GP19). The select lines are never captured — the offline
demodulator reconstructs the phase index from the sync rising edges plus
the known f:

```bash
python analysis/hsx_demod_scope_csv.py capture.csv --f 40000
```

The `--f` you pass must match the `start(f)` you used. Sync is high only
in state 0, so every rising edge pins the start of a demod cycle.

## References

- Pico 2 datasheet: https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf
- RP2350 datasheet: https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf
- MicroPython on Pico: https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
- `rp2.StateMachine` API: https://docs.micropython.org/en/latest/library/rp2.StateMachine.html
- PIO tutorial: https://docs.micropython.org/en/latest/rp2/tutorial/pio.html

"""
pico2_spin_scope.py
-------------------
Raspberry Pi Pico 2 (RP2350) firmware -- MODE 1 of 2: full current-spinning
operation with the oscilloscope as the data-acquisition instrument.

This is the self-contained "flight" firmware for spun measurements: it
generates the three spinning-mux select lines a0/a1/a2 (a 3-bit binary
counter, one increment per phase) plus a frame-sync pulse from ONE PIO
state machine, so all four outputs update on the SAME clock edge -- no
software-GPIO skew between bits. EN is a plain GPIO with explicit safe
sequencing. The Pico produces clocks only; ALL data acquisition happens
on the oscilloscope (DSOX1204G): CH-a = v_meas (J4 SMA), CH-b = sync
(GP19). Demodulation is offline via analysis/hsx_demod_scope_csv.py.

The companion file pico2_static_bias_p2p4.py is MODE 2: static bias of
plate ports p2/p4 with the external current source and measurement of
the p1/p3 voltage difference (through the AD8429) on the Pico's own ADC
-- no scope needed. Copy whichever file matches the day's test; both use
the same wiring.

WIRING (identical to the project pin map -- do not re-pin casually; the
four PIO outputs a0/a1/a2/sync MUST stay on contiguous GPIOs, EN can be
any free pin)

  signal | Pico GPIO | Pico physical pin | goes to
  -------+-----------+-------------------+----------------------------------
  a0     | GP16      | 21                | J3 pin 3
  a1     | GP17      | 22                | J3 pin 2
  a2     | GP18      | 24                | J3 pin 1
  sync   | GP19      | 25                | scope CH-b / ext trig (NOT to J3)
  en     | GP20      | 26                | J3 pin 4 (on-board pulldown)
  GND    | --        | 23 (or 28)        | board GND1 -- bond separately,
         |           |                   | J3 has NO ground pin!

SAFE SEQUENCE (matches the runbook)
  1. Power the board, confirm +-15 V on the scope.
  2. Bond Pico GND to GND1 if not already done.
  3. Run start(f) -- this raises EN, THEN starts the clock.
  4. To connect/disconnect the sensor or emulator plug: run stop() first,
     which stops the clock and drops EN before you touch the connector.

USAGE (MicroPython REPL / Thonny shell, or via the boot menu in main.py)

    >>> import pico2_spin_scope as sp
    >>> sp.scope_notes()       # print the DSOX1204G capture checklist
    >>> sp.start(40_000)       # raise EN, spin at f = 40 kHz phase rate
    >>> sp.status()
    >>> sp.hold_state(0b010)   # freeze one static code (a2 a1 a0)
    >>> sp.survey()            # guided manual 8-state survey (Day-3 test)
    >>> sp.stop()              # stop clock, drop EN -- BEFORE touching DSUB

f is the *phase rate*: each of the 8 states lasts 1/f, the full demod
cycle is 8/f (200 us -> 5 kHz update at f = 40 kHz), and a0 toggles at
f/2. Usable demodulated bandwidth is ~1-2 kHz at f = 40 kHz.

SPINNING PHASE TABLE (verified against both netlists -- see docs/SPECS.md;
state = (a2<<2)|(a1<<1)|a0, demod sign = +1 if a0 == a2 else -1)

  state | a2 a1 a0 | bias        | in+ | in- | demod sign
  ------+----------+-------------+-----+-----+-----------
    0   |  0  0  0 | p1 -> p3    | p2  | p4  |  +
    1   |  0  0  1 | p1 -> p3    | p4  | p2  |  -
    2   |  0  1  0 | p2 -> p4    | p3  | p1  |  +
    3   |  0  1  1 | p2 -> p4    | p1  | p3  |  -
    4   |  1  0  0 | p3 -> p1    | p2  | p4  |  -
    5   |  1  0  1 | p3 -> p1    | p4  | p2  |  +
    6   |  1  1  0 | p4 -> p2    | p3  | p1  |  -
    7   |  1  1  1 | p4 -> p2    | p1  | p3  |  +

Global sign is fixed empirically with a known magnet -- never from the
netlist.
"""

import machine
import rp2
from machine import Pin

# ---------------------------------------------------------------- config --
PIN_A0 = 16     # base pin of the 4-pin PIO "set" group -- must be contiguous:
PIN_A1 = 17     #   PIN_A0, PIN_A0+1, PIN_A0+2, PIN_A0+3 = a0, a1, a2, sync
PIN_A2 = 18
PIN_SYNC = 19
PIN_EN = 20     # plain GPIO, controlled directly (not part of the PIO group)

DEFAULT_FREQ = 40_000   # Hz, phase rate (bring-up plan nominal; ~290 Hz-1 MHz)

# Each phase is emitted as CYCLES_PER_PHASE PIO cycles (a [delay] on the
# set instruction) so the phase rate decouples from the PIO divider floor
# (single-cycle phases can't go below ~2.3 kHz at 150 MHz sys clock; 8
# cycles/phase drops the floor to ~290 Hz, so f = 1 kHz works). MUST equal
# 1 + the [delay] literal in _phase_gen below.
CYCLES_PER_PHASE = 8

_SM_ID = 0


# ------------------------------------------------------------ PIO program --
# One "set pins" instruction per phase, CYCLES_PER_PHASE SM clock cycles
# each (1 + [delay]), so running the state machine at CYCLES_PER_PHASE*f
# makes every phase last exactly 1/f seconds. wrap() loops back to state 0
# for free, so the cycle is a clean, jitter-free 8/f seconds. The [7]
# delay literal MUST equal CYCLES_PER_PHASE - 1.
#
# Bit mapping within each 4-bit value (matches the demod convention
# state = (a2<<2)|(a1<<1)|a0 from the bring-up plan):
#   bit0 -> a0   bit1 -> a1   bit2 -> a2   bit3 -> sync
# sync is high only during state 0 (a0=a1=a2=0), giving one sync pulse,
# 1/f seconds wide, at the start of every 8-phase cycle.
@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,) * 4)
def _phase_gen():
    wrap_target()
    set(pins, 0b1000) [7]   # state 0: a2,a1,a0 = 0,0,0   sync = 1
    set(pins, 0b0001) [7]   # state 1: a0 = 1
    set(pins, 0b0010) [7]   # state 2: a1 = 1
    set(pins, 0b0011) [7]   # state 3: a1,a0 = 1,1
    set(pins, 0b0100) [7]   # state 4: a2 = 1
    set(pins, 0b0101) [7]   # state 5: a2,a0 = 1,1
    set(pins, 0b0110) [7]   # state 6: a2,a1 = 1,1
    set(pins, 0b0111) [7]   # state 7: a2,a1,a0 = 1,1,1
    wrap()


# ------------------------------------------------------------- EN control --
_en_pin = Pin(PIN_EN, Pin.OUT, value=0)   # boot low = matches board pulldown


def enable():
    """Drive EN high. Muxes only respond once V_INH (~2 V) is exceeded."""
    _en_pin.value(1)


def disable():
    """Drive EN low. Do this before connecting/disconnecting the sensor."""
    _en_pin.value(0)


def en_state():
    return _en_pin.value()


# --------------------------------------------------------- state machine --
_sm = rp2.StateMachine(_SM_ID, _phase_gen,
                       freq=int(CYCLES_PER_PHASE * DEFAULT_FREQ),
                       set_base=Pin(PIN_A0))
_current_freq = DEFAULT_FREQ


def set_freq(f):
    """Reconfigure the phase rate without starting/stopping EN. Returns the
    achieved phase rate. Each phase is CYCLES_PER_PHASE PIO cycles, so the
    SM runs at CYCLES_PER_PHASE*f; the RP2350 divider is 16.8 fixed-point.
    Min phase rate = sys_clk / 65536 / CYCLES_PER_PHASE (~290 Hz at
    150 MHz); 5k/10k/40k/100k all land on clean divisors."""
    global _current_freq
    f_min = machine.freq() / 65536 / CYCLES_PER_PHASE
    if f < f_min:
        print("f too low: min phase rate ~{:.0f} Hz (sys {} Hz, "
              "CYCLES_PER_PHASE {}) -- raise the [delay] literal to go lower"
              .format(f_min, machine.freq(), CYCLES_PER_PHASE))
        return None
    was_active = _sm.active()
    _sm.active(0)
    sm_freq = int(CYCLES_PER_PHASE * f)
    _sm.init(_phase_gen, freq=sm_freq, set_base=Pin(PIN_A0))
    _current_freq = f
    if was_active:
        _sm.active(1)
    divider = round(machine.freq() / sm_freq)
    achieved = machine.freq() / divider / CYCLES_PER_PHASE
    print("target {:.1f} Hz -> achieved {:.3f} Hz phase rate "
          "(sys clock {} Hz, SM divider {})"
          .format(f, achieved, machine.freq(), divider))
    return achieved


def start(f=None):
    """Raise EN, then start spinning at frequency f (Hz, phase rate).
    Call only after +-15 V rails are confirmed and Pico GND is bonded to
    GND1. If f is None, keeps whatever frequency was last set."""
    if f is not None:
        set_freq(f)
    enable()
    _sm.active(1)
    print("spinning at {:.0f} Hz phase rate, EN high".format(_current_freq))


def stop():
    """Stop the clock and drop EN. Do this before touching the DSUB
    connector (sensor or emulator plug)."""
    _sm.active(0)
    disable()
    print("stopped, EN low -- safe to (dis)connect the sensor")


def hold_state(state):
    """Freeze a0/a1/a2/sync at one of the 8 static codes (0-7) for the
    manual survey (probe with a DMM/scope while stepping through all 8
    by hand). Stops the running clock first. EN is left as-is -- call
    enable() separately if it isn't already on."""
    state &= 0x7
    value = state | (0b1000 if state == 0 else 0)
    _sm.active(0)
    # Documented MicroPython technique: StateMachine.exec() runs one
    # instruction directly on a paused SM. "0" here is the PIO SET
    # destination code for pins (see rp2.StateMachine.exec in the
    # MicroPython docs), not the symbolic "pins" keyword used inside
    # the @asm_pio-decorated program above.
    _sm.exec("set(0, {})".format(value))
    print("held at state {:03b} (a2 a1 a0), sync={}".format(
        state, 1 if state == 0 else 0))


_SURVEY_TABLE = (
    # state: (bias, in+, in-, demod sign) -- from the verified phase table
    ("p1 -> p3", "p2", "p4", "+"),
    ("p1 -> p3", "p4", "p2", "-"),
    ("p2 -> p4", "p3", "p1", "+"),
    ("p2 -> p4", "p1", "p3", "-"),
    ("p3 -> p1", "p2", "p4", "-"),
    ("p3 -> p1", "p4", "p2", "+"),
    ("p4 -> p2", "p3", "p1", "-"),
    ("p4 -> p2", "p1", "p3", "+"),
)


def survey():
    """Guided manual 8-state survey (bring-up plan Day 3): steps through
    all 8 static codes, printing what each state does; press Enter to
    advance after recording v_meas on the DMM/scope. Requires EN high
    (raises it if not). Ends with the clock stopped at state 7 -- run
    start(f) to resume spinning or stop() to shut down."""
    if not _en_pin.value():
        enable()
        print("EN raised for the survey")
    print("Record v_meas at each state; expected sign pattern: + - + - - + - +")
    print("(that's the raw per-state sensor+offset pattern -- see SPECS.md)")
    for s in range(8):
        bias, inp, inn, sgn = _SURVEY_TABLE[s]
        hold_state(s)
        print("  state {} ({:03b}): bias {}, in+ = {}, in- = {}, demod sign {}"
              .format(s, s, bias, inp, inn, sgn))
        try:
            input("  ... record v_meas, then press Enter for next state ")
        except (EOFError, KeyboardInterrupt):
            print("survey aborted")
            return
    print("survey complete -- start(f) to spin, stop() to shut down")


def status():
    print("mode   : SPIN + SCOPE (pico2_spin_scope)")
    print("EN     : {}".format("HIGH" if _en_pin.value() else "low"))
    print("running: {}".format(_sm.active()))
    print("freq   : {:.0f} Hz phase rate ({:.0f} Hz update rate, "
          "8-phase cycle)".format(_current_freq, _current_freq / 8))
    print("sys clk: {} Hz".format(machine.freq()))


def scope_notes(f=None):
    """Print the oscilloscope data-acquisition checklist for the current
    (or given) phase rate -- the scope IS the DAQ in this mode."""
    f = f or _current_freq
    phase_us = 1e6 / f
    cycle_us = 8 * phase_us
    min_rate = 10 * f          # >= ~10 samples per phase segment
    print("DSOX1204G capture checklist (f = {:.0f} Hz phase rate):".format(f))
    print("  CH-a  : v_meas, J4 SMA (10 k shunt on board; keep cable short)")
    print("  CH-b  : sync, Pico GP19 (0/3.3 V; high only in state 0)")
    print("  trig  : rising edge on sync -- every edge marks a cycle start")
    print("  rate  : >= {:.1f} MSa/s ( >= ~10 samples per {:.1f} us phase)"
          .format(min_rate / 1e6, phase_us))
    print("  window: integer number of {:.0f} us cycles; longer = better demod"
          .format(cycle_us))
    print("  export: CSV, then on the host:")
    print("     python3 analysis/hsx_demod_scope_csv.py capture.csv --f {:.0f}"
          .format(f))
    print("  NOTE  : --f must match start(f); check --tcol/--vcol/--synccol")
    print("          against your export format the first time.")
    print("  a0/a1/a2 are NEVER wired to the scope -- phase is reconstructed")
    print("  from sync + f. Channels 3/4 stay free (reference sensor later).")


# ------------------------------------------------------- optional menu ----
HELP = """
HSX spin + scope control -- commands:
  start [f]     raise EN and start spinning (Hz, e.g. 'start 40000')
  stop          stop spinning and drop EN (do this before (dis)connecting sensor)
  en            raise EN only
  dis           drop EN only
  freq f        change phase rate without touching EN (e.g. 'freq 100000')
  hold n        freeze at static state n = 0-7 (binary a2 a1 a0), e.g. 'hold 5'
  survey        guided manual 8-state survey (Day-3 test)
  scope         print the oscilloscope capture checklist
  status        show EN / running / frequency
  help          show this message
  quit          stop and exit the menu
"""


def menu():
    print(HELP)
    while True:
        try:
            cmd = input("spin> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not cmd:
            continue
        parts = cmd.split()
        c = parts[0].lower()
        try:
            if c in ("h", "help", "?"):
                print(HELP)
            elif c in ("start", "s"):
                start(int(parts[1]) if len(parts) > 1 else None)
            elif c in ("stop", "x"):
                stop()
            elif c == "en":
                enable()
            elif c in ("dis", "disable"):
                disable()
            elif c == "hold":
                hold_state(int(parts[1], 0))
            elif c == "survey":
                survey()
            elif c in ("scope", "sc"):
                scope_notes()
            elif c in ("freq", "f"):
                set_freq(int(parts[1]))
            elif c in ("status", "st"):
                status()
            elif c in ("q", "quit", "exit"):
                stop()
                break
            else:
                print("unknown command -- type 'help'")
        except (ValueError, IndexError):
            print("bad arguments -- type 'help'")
        except Exception as e:
            print("error:", e)


if __name__ == "__main__":
    # Boots to a safe idle state (EN low, SM inactive), then the menu.
    menu()

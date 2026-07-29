"""
pico2_static_bias_p2p4.py
-------------------------
Raspberry Pi Pico 2 (RP2350) firmware -- MODE 2 of 2: STATIC bias of plate
ports p2/p4 from the external current source, measuring the p1/p3 voltage
difference. No spinning, no oscilloscope: the Pico's own ADC does the
data acquisition (through the board's AD8429, G = 100.3).

This is the "second test setup": the classic direct DC Hall measurement,
implemented through the existing readout board by parking the muxes in
the phase states whose bias axis is p2 -> p4 and whose sense pair is
p1/p3. It is the tool for:
  - quick sensor health checks without the scope,
  - raw-offset measurement at 100 uA (gen-2 die incoming inspection,
    project 03),
  - continuity checks against the 2023-style static measurement,
  - a "fast mode" fallback (static phase = full amplifier bandwidth; the
    Pico ADC is then the bottleneck, not the demod).

The companion file pico2_spin_scope.py is MODE 1: full current-spinning
with the scope as DAQ. Both files use the same J3 wiring.

STATES USED (subset of the verified spinning phase table, docs/SPECS.md;
state = (a2<<2)|(a1<<1)|a0 -- these are the four a1 = 1 states, i.e. the
only states whose bias axis is p2/p4 and whose sense pair is p1/p3):

  state | a2 a1 a0 | bias      | in+ | in- | amp input (ideal)
  ------+----------+-----------+-----+-----+-------------------
    2   |  0  1  0 | p2 -> p4  | p3  | p1  |  +(s - o) + e
    3   |  0  1  1 | p2 -> p4  | p1  | p3  |  -(s - o) + e
    6   |  1  1  0 | p4 -> p2  | p3  | p1  |  -(s - o) + e
    7   |  1  1  1 | p4 -> p2  | p1  | p3  |  +(s - o) + e

  s = Hall term, o = plate resistive offset (p2-p4 bias axis),
  e = amplifier input offset. v_meas = G x loading x (amp input).

WHAT THIS SETUP CAN AND CANNOT CANCEL (physics, not a bug):
  - measure_chopped() averages states {2,3,6,7} with signs {+,-,-,+}:
    the amplifier offset e cancels exactly (sense swap + current
    reversal), and the mean over the four states measures e itself.
  - The PLATE offset o does NOT cancel -- with a single bias axis, s and
    o are inseparable; the chopped result is (s - o) x loading x G.
    Separating them is precisely what the full 8-state spinning in
    MODE 1 is for. At zero applied field (s = 0) the chopped result IS
    the raw plate offset -- which is exactly what incoming inspection
    wants to record.

WIRING (same J3 map as MODE 1, plus the ADC tap)

  signal | Pico GPIO | Pico physical pin | goes to
  -------+-----------+-------------------+----------------------------------
  a0     | GP16      | 21                | J3 pin 3
  a1     | GP17      | 22                | J3 pin 2
  a2     | GP18      | 24                | J3 pin 1
  sync   | GP19      | 25                | unused here (driven low)
  en     | GP20      | 26                | J3 pin 4 (on-board pulldown)
  GND    | --        | 23 (or 28)        | board GND1 -- bond separately,
         |           |                   | J3 has NO ground pin!
  v_meas | GP26/ADC0 | 31                | J4 SMA center (10 k on-board shunt)
  AGND   | --        | 33 (AGND)         | J4 SMA shell / GND1

  External 100 uA current source: into the bias loop at J2 (or J7),
  exactly as in MODE 1 -- the source must float; verify the current via
  the R9 = R10 = 100 ohm sense drops (10.0 mV each at 100 uA, TP6->TP5
  and TP8->TP7, floating DMM only).

ADC LIMITS -- READ BEFORE TRUSTING NUMBERS
  - The RP2350 ADC reads 0..3.3 V, UNIPOLAR. The AD8429 output is
    bipolar: any state that drives v_meas negative clamps to ~0 V and
    reads as garbage. The chopped sequence flips the signal's sign
    between states, so with a near-zero amplifier offset roughly half
    the states of a large-offset sensor may clamp. Fixes, pick one:
      (a) read the states that are positive, infer the rest by symmetry
          (fine for quick checks);
      (b) build the level-shift divider (docs/second_test_setup doc):
          then set ADC_OFFSET_V / ADC_SCALE below to un-shift readings;
      (c) use a floating DMM at J4 with hold_state() from MODE 1 --
          this file's mux parking works for that too (use 'read' with
          the DMM instead of the ADC).
  - 12-bit ADC on a 3.3 V span = 0.8 mV/LSB. With OVERSAMPLE = 256 the
    effective resolution is a few hundred uV -- good enough to resolve
    the ~26 mV emulator step at the percent level, NOT good enough for
    calibration-grade work. Calibration numbers come from MODE 1 + the
    scope, always.

USAGE

    >>> import pico2_static_bias_p2p4 as sb
    >>> sb.bias_on()            # EN high, park in state 2 (p2 -> p4)
    >>> sb.read()               # oversampled v_meas in volts
    >>> sb.measure_chopped()    # 4-state e-free measurement, prints table
    >>> sb.log_csv(60)          # 60 s of chopped readings as CSV on serial
    >>> sb.bias_reverse()       # park in state 6 (p4 -> p2)
    >>> sb.stop()               # EN low -- BEFORE touching the DSUB

SAFE SEQUENCE: same as MODE 1 -- rails verified, Pico GND bonded to GND1,
then bias_on(); stop() before (dis)connecting the sensor or emulator.
"""

import time

from machine import ADC, Pin

# ---------------------------------------------------------------- config --
PIN_A0 = 16
PIN_A1 = 17
PIN_A2 = 18
PIN_SYNC = 19          # unused in this mode; held low so the scope input
PIN_EN = 20            # (if still connected) sees a defined level
ADC_VMEAS = 26         # GP26 = ADC0, physical pin 31 <- J4 SMA center

GAIN = 100.3           # AD8429, R_G = 60.4 ohm -- from docs/SPECS.md
LOADING = 0.83         # plate+Ron source vs 2x2.2k bias-return load (SPECS)
V_PER_TESLA = 0.55     # nominal system sensitivity at 100 uA [V/T] -- for a
                       # rough field estimate ONLY; calibration wins, always.

OVERSAMPLE = 256       # ADC samples averaged per reading
SETTLE_MS = 50         # wait after a mux state change before sampling

# Level-shift network correction (see ADC LIMITS above). With no network:
# volts = raw. With the documented divider: volts = (raw - ADC_OFFSET_V)
# / ADC_SCALE. Measure both constants after building the network.
ADC_OFFSET_V = 0.0
ADC_SCALE = 1.0

# The four p2/p4-axis states and their chop signs (+,-,-,+ = a0==a2 rule)
STATE_FWD = 0b010          # state 2: p2 -> p4, in+ = p3, in- = p1
STATE_FWD_SWAP = 0b011     # state 3: p2 -> p4, sense swapped
STATE_REV = 0b110          # state 6: p4 -> p2, in+ = p3, in- = p1
STATE_REV_SWAP = 0b111     # state 7: p4 -> p2, sense swapped
CHOP_SEQUENCE = ((STATE_FWD, +1), (STATE_FWD_SWAP, -1),
                 (STATE_REV, -1), (STATE_REV_SWAP, +1))

_P2P4_STATES = (STATE_FWD, STATE_FWD_SWAP, STATE_REV, STATE_REV_SWAP)

# ------------------------------------------------------------------ pins --
_a0 = Pin(PIN_A0, Pin.OUT, value=0)
_a1 = Pin(PIN_A1, Pin.OUT, value=0)
_a2 = Pin(PIN_A2, Pin.OUT, value=0)
_sync = Pin(PIN_SYNC, Pin.OUT, value=0)   # defined-low, unused in this mode
_en = Pin(PIN_EN, Pin.OUT, value=0)       # boot low = matches board pulldown
_adc = ADC(ADC_VMEAS)

_current_state = None


# ------------------------------------------------------------ mux control --
def apply_state(state, settle=True):
    """Park a0/a1/a2 at one static code (0-7). Plain GPIO is fine here --
    static parking doesn't need the PIO's single-edge atomicity, and the
    muxes' break-before-make covers the ns-scale ordering during the
    transition. States outside {2,3,6,7} do NOT bias p2/p4 -- allowed
    (for cross-checks against MODE 1's survey) but flagged."""
    global _current_state
    state &= 0x7
    _a0.value(state & 1)
    _a1.value((state >> 1) & 1)
    _a2.value((state >> 2) & 1)
    _current_state = state
    if state not in _P2P4_STATES:
        print("NOTE: state {:03b} biases the p1/p3 axis, not p2/p4 -- "
              "this mode's tables assume states 2/3/6/7".format(state))
    if settle:
        time.sleep_ms(SETTLE_MS)


def bias_on():
    """EN high, then park in state 2: bias current p2 -> p4 from the
    external source, amplifier reads v(p3) - v(p1). Call only after the
    +-15 V rails are verified and Pico GND is bonded to GND1."""
    apply_state(STATE_FWD, settle=False)
    _en.value(1)
    time.sleep_ms(SETTLE_MS)
    print("EN high, state 010: bias p2 -> p4, measuring v(p3) - v(p1)")


def bias_reverse():
    """Park in state 6: bias current reversed, p4 -> p2 (the a2 chopper
    reversal). Raises EN if it is not already high."""
    if not _en.value():
        _en.value(1)
    apply_state(STATE_REV)
    print("EN high, state 110: bias p4 -> p2, measuring v(p3) - v(p1)")


def stop():
    """Drop EN (all mux switches off) and park the select lines at 0.
    Do this before touching the DSUB connector or the bias loop."""
    _en.value(0)
    apply_state(0, settle=False)
    print("stopped, EN low -- safe to (dis)connect the sensor")


# ------------------------------------------------------------ acquisition --
def read(n=None):
    """Oversampled v_meas reading in volts (float). n defaults to
    OVERSAMPLE. Warns when the reading sits at an ADC rail -- see the
    ADC LIMITS note in the module docstring."""
    n = n or OVERSAMPLE
    acc = 0
    for _ in range(n):
        acc += _adc.read_u16()
    raw = (acc / n) / 65535.0 * 3.3
    v = (raw - ADC_OFFSET_V) / ADC_SCALE
    if raw < 0.005:
        print("WARNING: reading at the 0 V rail -- v_meas is probably "
              "negative in this state (unipolar ADC; see module docstring)")
    elif raw > 3.295:
        print("WARNING: reading at the 3.3 V rail -- input over-range")
    return v


def measure(state=None, n=None):
    """Single-state measurement: optionally switch to `state` (default:
    stay where we are), settle, read. Returns volts at v_meas; divide by
    GAIN for the plate-referred differential."""
    if state is not None:
        apply_state(state)
    if not _en.value():
        print("WARNING: EN is low -- board is disabled; call bias_on() first")
    v = read(n)
    print("state {:03b}: v_meas = {:+.5f} V  ({:+.1f} uV at the plate)"
          .format(_current_state, v, v / GAIN * 1e6))
    return v


def measure_chopped(n=None, cycles=1):
    """The headline measurement of this mode: step through states
    {2, 3, 6, 7} with signs {+, -, -, +}, average.

    Returns (x, e) in volts at v_meas, where
      x = (s - o) x loading x G   -- amplifier-offset-free p2/p4-axis
                                     Hall + plate-offset signal
      e =  amplifier offset x G   -- the mean over the four states
    At zero applied field, x IS the raw plate offset (times loading x G):
    the incoming-inspection number. `cycles` > 1 repeats the sequence
    and averages, for drift-resistant longer measurements."""
    if not _en.value():
        print("WARNING: EN is low -- board is disabled; call bias_on() first")
    per_state = {st: [] for st, _ in CHOP_SEQUENCE}
    for _ in range(cycles):
        for st, _sgn in CHOP_SEQUENCE:
            apply_state(st)
            per_state[st].append(read(n))
    means = {st: sum(vs) / len(vs) for st, vs in per_state.items()}
    x = sum(sgn * means[st] for st, sgn in CHOP_SEQUENCE) / 4.0
    e = sum(means[st] for st, _ in CHOP_SEQUENCE) / 4.0
    print("chopped p2/p4-axis measurement ({} cycle(s), n = {}):"
          .format(cycles, n or OVERSAMPLE))
    for st, sgn in CHOP_SEQUENCE:
        print("  state {:03b} (sign {:+d}): {:+.5f} V".format(st, sgn, means[st]))
    print("  x = (s-o)*loading*G  : {:+.5f} V  ({:+.1f} uV plate-referred)"
          .format(x, x / GAIN * 1e6))
    print("  e = amp offset * G   : {:+.5f} V".format(e))
    print("  rough field-equiv    : {:+.3f} mT  (nominal {} V/T -- NOT "
          "calibrated; plate offset o is included!)"
          .format(x / V_PER_TESLA * 1e3, V_PER_TESLA))
    print("  (plate offset o does not cancel here -- that needs MODE 1)")
    return x, e


def log_csv(duration_s=60, period_s=1.0, n=None):
    """Periodic chopped measurements, printed as CSV over USB serial:
    `t_s,x_v,e_v` -- capture with Thonny / `mpremote` redirection on the
    host and plot drift. Runs for duration_s seconds; Ctrl-C stops early."""
    if not _en.value():
        print("WARNING: EN is low -- board is disabled; call bias_on() first")
    print("t_s,x_v,e_v")
    t_start = time.ticks_ms()
    try:
        while time.ticks_diff(time.ticks_ms(), t_start) < duration_s * 1000:
            t_iter = time.ticks_ms()
            per = []
            for st, sgn in CHOP_SEQUENCE:
                apply_state(st)
                per.append((sgn, read(n)))
            x = sum(sgn * v for sgn, v in per) / 4.0
            e = sum(v for _, v in per) / 4.0
            print("{:.2f},{:.6f},{:.6f}".format(
                time.ticks_diff(time.ticks_ms(), t_start) / 1000.0, x, e))
            leftover = int(period_s * 1000) - time.ticks_diff(
                time.ticks_ms(), t_iter)
            if leftover > 0:
                time.sleep_ms(leftover)
    except KeyboardInterrupt:
        print("# log stopped by user")


def status():
    print("mode   : STATIC BIAS p2/p4 (pico2_static_bias_p2p4)")
    print("EN     : {}".format("HIGH" if _en.value() else "low"))
    print("state  : {}".format(
        "{:03b}".format(_current_state) if _current_state is not None
        else "not set"))
    print("ADC    : GP{} (ADC0) <- J4 v_meas, oversample {}x"
          .format(ADC_VMEAS, OVERSAMPLE))
    print("consts : G = {}, loading = {}, nominal {} V/T"
          .format(GAIN, LOADING, V_PER_TESLA))


# ------------------------------------------------------- optional menu ----
HELP = """
HSX static-bias (p2/p4) control -- commands:
  on            EN high + state 010: bias p2 -> p4, sense p1/p3
  rev           state 110: reverse bias, p4 -> p2
  off           EN low (do this before (dis)connecting the sensor)
  state n       park any static code n = 0-7 (2/3/6/7 are the p2/p4 states)
  read [n]      one oversampled v_meas reading (n samples, default 256)
  chop [c]      4-state amplifier-offset-free measurement (c cycles)
  log [s] [p]   CSV drift log for s seconds, one chopped point per p seconds
  status        show EN / state / constants
  help          show this message
  quit          EN low and exit the menu
"""


def menu():
    print(HELP)
    while True:
        try:
            cmd = input("static> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not cmd:
            continue
        parts = cmd.split()
        c = parts[0].lower()
        try:
            if c in ("h", "help", "?"):
                print(HELP)
            elif c == "on":
                bias_on()
            elif c == "rev":
                bias_reverse()
            elif c in ("off", "x", "stop"):
                stop()
            elif c == "state":
                apply_state(int(parts[1], 0))
                print("state {:03b} parked".format(_current_state))
            elif c in ("read", "r"):
                measure(n=int(parts[1]) if len(parts) > 1 else None)
            elif c in ("chop", "c"):
                measure_chopped(cycles=int(parts[1]) if len(parts) > 1 else 1)
            elif c == "log":
                dur = float(parts[1]) if len(parts) > 1 else 60
                per = float(parts[2]) if len(parts) > 2 else 1.0
                log_csv(dur, per)
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
    # Boots to a safe idle state (EN low, state 000), then the menu.
    menu()

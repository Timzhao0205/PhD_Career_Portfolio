# main.py -- Raspberry Pi Pico 2 (RP2350) firmware for the HSX Hall-sensor
# readout board.  SINGLE-FILE BUILD: both operating modes live in here, so
# the ONLY file you need to copy to the Pico is this one.
#
# =====================================================================
#   >>>  SET YOUR MODE BELOW, THEN FLASH THIS FILE  <<<
# =====================================================================
#   MODE = 1 : full current-spinning; the oscilloscope (DSOX1204G) is the
#              DAQ -- CH-a = v_meas (J4), CH-b = sync (GP19). Offline demod
#              with analysis/hsx_demod_scope_csv.py.
#   MODE = 2 : static bias of plate ports p2/p4 from the external current
#              source; the p1/p3 voltage difference is read on the Pico's
#              own ADC (GP26 <- J4). No scope, no spinning. (This is the
#              setup for the bridge-emulator bring-up.)
#
# At boot: the onboard LED lights SOLID (firmware-alive indicator -- this
# is NOT the EN/bias state; check TP4 for EN), a banner prints over USB
# serial (115200 baud), and it drops into the selected mode's text menu.
# The live device object is also exposed as `dev` for the REPL -- Ctrl-C
# out of the menu, then e.g.  dev.start(40_000)  or  dev.measure_chopped().
#
# Boot is SAFE in both modes: EN stays low, nothing spins or biases until
# you act. Wiring / flashing / physics: README.md and
# ../../docs/second_test_setup_static_bias.md. The standalone modules
# pico2_spin_scope.py / pico2_static_bias_p2p4.py mirror this logic as
# importable libraries (used by the RSI 3-board work); for plain bench
# use this single file is the one to flash and the one to edit.

# ========================== USER SETTINGS ==========================
MODE = 2               # 1 = spin + scope DAQ  ;  2 = static bias p2/p4
DEFAULT_FREQ = 40_000  # MODE 1 phase rate [Hz]  (10k-100k usable)
# ===================================================================

import machine
import time
import rp2
from machine import ADC, Pin

# ---- pin map (shared; full table in README) -----------------------
PIN_A0 = 16     # J3 pin 3.  In MODE 1 a0/a1/a2/sync are a PIO set-group
PIN_A1 = 17     # J3 pin 2   and MUST stay on 4 contiguous GPIOs (base a0).
PIN_A2 = 18     # J3 pin 1
PIN_SYNC = 19   # scope CH-b / trig (MODE 1); driven low in MODE 2
PIN_EN = 20     # J3 pin 4   (on-board pulldown -> dead until driven >= 2 V)
ADC_VMEAS = 26  # GP26 = ADC0, physical pin 31 <- J4 SMA center (MODE 2)

# ---- amp / plate constants (docs/SPECS.md) ------------------------
GAIN = 100.3        # AD8429, R_G = 60.4 ohm
LOADING = 0.83      # plate+Ron source vs 2x2.2k bias-return load
V_PER_TESLA = 0.55  # nominal system sensitivity at 100 uA [V/T] (rough only)


# ------------------------------------------------------------ LED --
def alive_led():
    """Light the onboard LED as a firmware-alive signal and return the Pin.
    'LED' alias covers the Pico 2 W (LED via the wireless chip); GP25 is
    the plain Pico 2 LED. Cosmetic -- any failure is swallowed so it can
    never block boot."""
    for spec in ("LED", 25):
        try:
            led = Pin(spec, Pin.OUT)
            led.value(1)
            return led
        except Exception:
            continue
    return None


# ================================================== MODE 1: SPIN ===
# One "set pins" per phase, 1 SM cycle each -> each phase lasts 1/f.
# bit0->a0 bit1->a1 bit2->a2 bit3->sync; sync high only in state 0.
@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,) * 4)
def _phase_gen():
    wrap_target()
    set(pins, 0b1000)   # state 0: a2,a1,a0 = 0,0,0  sync = 1
    set(pins, 0b0001)   # state 1
    set(pins, 0b0010)   # state 2
    set(pins, 0b0011)   # state 3
    set(pins, 0b0100)   # state 4
    set(pins, 0b0101)   # state 5
    set(pins, 0b0110)   # state 6
    set(pins, 0b0111)   # state 7
    wrap()


class SpinScope:
    """MODE 1 -- full current-spinning, oscilloscope as the DAQ.
    state = (a2<<2)|(a1<<1)|a0; demod sign = +1 if a0 == a2 else -1.
    Global sign is fixed empirically with a known magnet, never here."""

    _SURVEY = (
        ("p1 -> p3", "p2", "p4", "+"), ("p1 -> p3", "p4", "p2", "-"),
        ("p2 -> p4", "p3", "p1", "+"), ("p2 -> p4", "p1", "p3", "-"),
        ("p3 -> p1", "p2", "p4", "-"), ("p3 -> p1", "p4", "p2", "+"),
        ("p4 -> p2", "p3", "p1", "-"), ("p4 -> p2", "p1", "p3", "+"),
    )

    def __init__(self, freq=DEFAULT_FREQ):
        self._en = Pin(PIN_EN, Pin.OUT, value=0)   # boot low = board pulldown
        self._freq = freq
        self._sm = rp2.StateMachine(0, _phase_gen, freq=freq,
                                    set_base=Pin(PIN_A0))

    def enable(self):
        self._en.value(1)

    def disable(self):
        self._en.value(0)

    def set_freq(self, f):
        was = self._sm.active()
        self._sm.active(0)
        self._sm.init(_phase_gen, freq=int(f), set_base=Pin(PIN_A0))
        self._freq = f
        if was:
            self._sm.active(1)
        div = round(machine.freq() / f)
        print("target {:.1f} Hz -> achieved {:.3f} Hz (sys {} Hz, div {})"
              .format(f, machine.freq() / div, machine.freq(), div))
        return machine.freq() / div

    def start(self, f=None):
        if f is not None:
            self.set_freq(f)
        self.enable()
        self._sm.active(1)
        print("spinning at {:.0f} Hz phase rate, EN high".format(self._freq))

    def stop(self):
        self._sm.active(0)
        self.disable()
        print("stopped, EN low -- safe to (dis)connect the sensor")

    def hold_state(self, state):
        state &= 0x7
        value = state | (0b1000 if state == 0 else 0)
        self._sm.active(0)
        self._sm.exec("set(0, {})".format(value))
        print("held at state {:03b} (a2 a1 a0), sync={}".format(
            state, 1 if state == 0 else 0))

    def survey(self):
        if not self._en.value():
            self.enable()
            print("EN raised for the survey")
        print("Record v_meas each state; expected sign pattern: + - + - - + - +")
        for s in range(8):
            bias, inp, inn, sgn = self._SURVEY[s]
            self.hold_state(s)
            print("  state {} ({:03b}): bias {}, in+ = {}, in- = {}, sign {}"
                  .format(s, s, bias, inp, inn, sgn))
            try:
                input("  ... record v_meas, then Enter for next state ")
            except (EOFError, KeyboardInterrupt):
                print("survey aborted")
                return
        print("survey complete -- start(f) to spin, stop() to shut down")

    def scope_notes(self, f=None):
        f = f or self._freq
        phase_us = 1e6 / f
        print("DSOX1204G capture checklist (f = {:.0f} Hz):".format(f))
        print("  CH-a: v_meas (J4)   CH-b: sync (GP19, high in state 0)")
        print("  trig: rising edge on sync")
        print("  rate: >= {:.1f} MSa/s (~10 samples / {:.1f} us phase)"
              .format(10 * f / 1e6, phase_us))
        print("  window: integer # of {:.0f} us cycles".format(8 * phase_us))
        print("  host: python3 analysis/hsx_demod_scope_csv.py cap.csv --f {:.0f}"
              .format(f))

    def status(self):
        print("mode   : 1  SPIN + SCOPE")
        print("EN     : {}".format("HIGH" if self._en.value() else "low"))
        print("running: {}".format(self._sm.active()))
        print("freq   : {:.0f} Hz phase ({:.0f} Hz update)".format(
            self._freq, self._freq / 8))

    HELP = """
spin> commands:
  start [f]   raise EN and spin (Hz)    stop        stop spin + drop EN
  en / dis    EN high / low             freq f      set phase rate, keep EN
  hold n      freeze state n (0-7)      survey      guided 8-state survey
  scope       scope capture checklist   status      EN / running / freq
  help        this text                 quit        stop and exit
"""

    def menu(self):
        print(self.HELP)
        while True:
            try:
                cmd = input("spin> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if not cmd:
                continue
            p = cmd.split()
            c = p[0].lower()
            try:
                if c in ("h", "help", "?"):
                    print(self.HELP)
                elif c in ("start", "s"):
                    self.start(int(p[1]) if len(p) > 1 else None)
                elif c in ("stop", "x"):
                    self.stop()
                elif c == "en":
                    self.enable()
                elif c in ("dis", "disable"):
                    self.disable()
                elif c == "hold":
                    self.hold_state(int(p[1], 0))
                elif c == "survey":
                    self.survey()
                elif c in ("scope", "sc"):
                    self.scope_notes()
                elif c in ("freq", "f"):
                    self.set_freq(int(p[1]))
                elif c in ("status", "st"):
                    self.status()
                elif c in ("q", "quit", "exit"):
                    self.stop()
                    break
                else:
                    print("unknown -- type 'help'")
            except (ValueError, IndexError):
                print("bad arguments -- type 'help'")
            except Exception as e:
                print("error:", e)


# ========================================== MODE 2: STATIC BIAS ===
class StaticBiasP2P4:
    """MODE 2 -- static bias p2->p4, sense p1/p3, Pico-ADC readout.
    Uses the a1=1 states 2/3/6/7. measure_chopped() signs {+,-,-,+}
    cancel the amplifier offset e; the plate offset o does NOT cancel
    (single bias axis) -- at zero field the result is the raw plate
    offset. Unipolar ADC clamps negative states (warns); ~0.8 mV/LSB,
    health-check grade -- calibration numbers come from MODE 1 + scope."""

    CHOP = ((0b010, +1), (0b011, -1), (0b110, -1), (0b111, +1))
    P2P4 = (0b010, 0b011, 0b110, 0b111)
    STATE_FWD = 0b010     # p2 -> p4, in+ = p3, in- = p1
    STATE_REV = 0b110     # p4 -> p2 (a2 chopper reversal)

    OVERSAMPLE = 256
    SETTLE_MS = 50
    # Level-shift network correction (see setup doc). No network: leave as is.
    ADC_OFFSET_V = 0.0
    ADC_SCALE = 1.0

    def __init__(self):
        self._a0 = Pin(PIN_A0, Pin.OUT, value=0)
        self._a1 = Pin(PIN_A1, Pin.OUT, value=0)
        self._a2 = Pin(PIN_A2, Pin.OUT, value=0)
        self._sync = Pin(PIN_SYNC, Pin.OUT, value=0)   # unused; defined low
        self._en = Pin(PIN_EN, Pin.OUT, value=0)       # boot low
        self._adc = ADC(ADC_VMEAS)
        self._state = None

    def apply_state(self, state, settle=True):
        state &= 0x7
        self._a0.value(state & 1)
        self._a1.value((state >> 1) & 1)
        self._a2.value((state >> 2) & 1)
        self._state = state
        if state not in self.P2P4:
            print("NOTE: state {:03b} biases the p1/p3 axis, not p2/p4"
                  .format(state))
        if settle:
            time.sleep_ms(self.SETTLE_MS)

    def bias_on(self):
        self.apply_state(self.STATE_FWD, settle=False)
        self._en.value(1)
        time.sleep_ms(self.SETTLE_MS)
        print("EN high, state 010: bias p2 -> p4, measuring v(p3) - v(p1)")

    def bias_reverse(self):
        if not self._en.value():
            self._en.value(1)
        self.apply_state(self.STATE_REV)
        print("EN high, state 110: bias p4 -> p2, measuring v(p3) - v(p1)")

    def stop(self):
        self._en.value(0)
        self.apply_state(0, settle=False)
        print("stopped, EN low -- safe to (dis)connect the sensor")

    def read(self, n=None):
        n = n or self.OVERSAMPLE
        acc = 0
        for _ in range(n):
            acc += self._adc.read_u16()
        raw = (acc / n) / 65535.0 * 3.3
        v = (raw - self.ADC_OFFSET_V) / self.ADC_SCALE
        if raw < 0.005:
            print("WARNING: at 0 V rail -- v_meas is probably negative in "
                  "this state (unipolar ADC)")
        elif raw > 3.295:
            print("WARNING: at 3.3 V rail -- input over-range")
        return v

    def measure(self, state=None, n=None):
        if state is not None:
            self.apply_state(state)
        if not self._en.value():
            print("WARNING: EN low -- board disabled; call bias_on() first")
        v = self.read(n)
        print("state {:03b}: v_meas = {:+.5f} V ({:+.1f} uV at the plate)"
              .format(self._state, v, v / GAIN * 1e6))
        return v

    def measure_chopped(self, n=None, cycles=1):
        if not self._en.value():
            print("WARNING: EN low -- board disabled; call bias_on() first")
        per = {st: [] for st, _ in self.CHOP}
        for _ in range(cycles):
            for st, _s in self.CHOP:
                self.apply_state(st)
                per[st].append(self.read(n))
        means = {st: sum(vs) / len(vs) for st, vs in per.items()}
        x = sum(sgn * means[st] for st, sgn in self.CHOP) / 4.0
        e = sum(means[st] for st, _ in self.CHOP) / 4.0
        print("chopped p2/p4 measurement ({} cycle(s), n = {}):".format(
            cycles, n or self.OVERSAMPLE))
        for st, sgn in self.CHOP:
            print("  state {:03b} (sign {:+d}): {:+.5f} V".format(
                st, sgn, means[st]))
        print("  x = (s-o)*loading*G : {:+.5f} V ({:+.1f} uV plate-referred)"
              .format(x, x / GAIN * 1e6))
        print("  e = amp offset * G  : {:+.5f} V".format(e))
        print("  (plate offset o does NOT cancel here -- that needs MODE 1)")
        return x, e

    def predict_offset(self, r12, r23, r34, r41, i_ua=100.0):
        """Predicted bridge offset for the emulator plug from the four
        MEASURED arm resistances [ohm], going round the ring:
          r12 = p1-p2 (incl. any parallel resistor), r23 = p2-p3,
          r34 = p3-p4, r41 = p4-p1.
        o = I*(R41*R23 - R12*R34) / (R12+R23+R34+R41); output ~ o*loading*G.
        Compare the printed |x| to a 'chop' reading to check gain*loading."""
        i = i_ua * 1e-6
        o = i * (r41 * r23 - r12 * r34) / (r12 + r23 + r34 + r41)
        vout = o * LOADING * GAIN
        print("bias current         : {:.1f} uA".format(i_ua))
        print("predicted plate o    : {:+.4f} mV".format(o * 1e3))
        print("predicted v_meas |x| : {:+.4f} mV  (o * loading * G)"
              .format(vout * 1e3))
        return o, vout

    def log_csv(self, duration_s=60, period_s=1.0, n=None):
        if not self._en.value():
            print("WARNING: EN low -- board disabled; call bias_on() first")
        print("t_s,x_v,e_v")
        t0 = time.ticks_ms()
        try:
            while time.ticks_diff(time.ticks_ms(), t0) < duration_s * 1000:
                ti = time.ticks_ms()
                pts = []
                for st, sgn in self.CHOP:
                    self.apply_state(st)
                    pts.append((sgn, self.read(n)))
                x = sum(s * v for s, v in pts) / 4.0
                e = sum(v for _, v in pts) / 4.0
                print("{:.2f},{:.6f},{:.6f}".format(
                    time.ticks_diff(time.ticks_ms(), t0) / 1000.0, x, e))
                left = int(period_s * 1000) - time.ticks_diff(
                    time.ticks_ms(), ti)
                if left > 0:
                    time.sleep_ms(left)
        except KeyboardInterrupt:
            print("# log stopped by user")

    def status(self):
        print("mode   : 2  STATIC BIAS p2/p4")
        print("EN     : {}".format("HIGH" if self._en.value() else "low"))
        print("state  : {}".format(
            "{:03b}".format(self._state) if self._state is not None
            else "not set"))
        print("ADC    : GP{} (ADC0) <- J4, oversample {}x".format(
            ADC_VMEAS, self.OVERSAMPLE))
        print("consts : G = {}, loading = {}".format(GAIN, LOADING))

    HELP = """
static> commands:
  on          EN high + bias p2->p4     rev         reverse bias p4->p2
  off         EN low                    state n     park state n (2/3/6/7)
  read [n]    one v_meas reading        chop [c]    4-state offset-free meas
  log [s] [p] CSV drift log (s sec)     predict a b c d   bridge offset from
  status      EN / state / consts                         4 arm ohms
  help        this text                 quit        EN low and exit
"""

    def menu(self):
        print(self.HELP)
        while True:
            try:
                cmd = input("static> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if not cmd:
                continue
            p = cmd.split()
            c = p[0].lower()
            try:
                if c in ("h", "help", "?"):
                    print(self.HELP)
                elif c == "on":
                    self.bias_on()
                elif c == "rev":
                    self.bias_reverse()
                elif c in ("off", "x", "stop"):
                    self.stop()
                elif c == "state":
                    self.apply_state(int(p[1], 0))
                    print("state {:03b} parked".format(self._state))
                elif c in ("read", "r"):
                    self.measure(n=int(p[1]) if len(p) > 1 else None)
                elif c in ("chop", "c"):
                    self.measure_chopped(cycles=int(p[1]) if len(p) > 1 else 1)
                elif c == "log":
                    dur = float(p[1]) if len(p) > 1 else 60
                    per = float(p[2]) if len(p) > 2 else 1.0
                    self.log_csv(dur, per)
                elif c == "predict":
                    self.predict_offset(float(p[1]), float(p[2]),
                                        float(p[3]), float(p[4]))
                elif c in ("status", "st"):
                    self.status()
                elif c in ("q", "quit", "exit"):
                    self.stop()
                    break
                else:
                    print("unknown -- type 'help'")
            except (ValueError, IndexError):
                print("bad arguments -- type 'help'")
            except Exception as e:
                print("error:", e)


# ================================================== boot / launch ==
_led = alive_led()      # stays on for as long as the firmware runs

print()
print("HSX Hall-sensor readout -- Pico 2 single-file firmware")
print("  onboard LED on = firmware alive (NOT the EN/bias state -- see TP4)")

if MODE == 1:
    dev = SpinScope(DEFAULT_FREQ)
    print("  MODE 1 : spinning + oscilloscope DAQ")
    print("  REPL after Ctrl-C:  dev.start(40000) / dev.hold_state(n) / dev.stop()")
elif MODE == 2:
    dev = StaticBiasP2P4()
    print("  MODE 2 : static bias p2/p4, Pico ADC")
    print("  REPL after Ctrl-C:  dev.bias_on() / dev.measure_chopped() / dev.stop()")
else:
    dev = None
    raise ValueError(
        "MODE must be 1 or 2 -- edit the MODE setting at the top of main.py")
print()

dev.menu()

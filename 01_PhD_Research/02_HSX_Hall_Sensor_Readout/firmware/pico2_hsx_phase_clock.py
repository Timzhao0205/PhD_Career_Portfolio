"""
pico2_hsx_phase_clock.py
------------------------
Raspberry Pi Pico 2 (RP2350) firmware for the HSX Hall-sensor readout board.

Generates the three spinning-mux clocks a0/a1/a2 (a 3-bit binary counter,
one increment per phase) plus a frame-sync pulse, using one PIO state
machine so all four outputs update on the SAME clock edge -- no software
GPIO skew between bits, which is what "atomic" meant in the bring-up plan.
EN is driven from a plain GPIO, separately, with explicit sequencing.

WIRING (change PIN_* below if you use different GPIOs)
  Pico GP16 -> J3 pin 3 (a0)
  Pico GP17 -> J3 pin 2 (a1)
  Pico GP18 -> J3 pin 1 (a2)
  Pico GP19 -> scope channel 2 / trigger input (sync pulse, NOT to J3)
  Pico GP20 -> J3 pin 4 (en)
  Pico GND  -> board GND1 (bond separately -- J3 has no ground pin)

SAFE SEQUENCE (matches the runbook)
  1. Power the board, confirm +-15V on the scope.
  2. Bond Pico GND to GND1 if not already done.
  3. Run start(f) -- this raises EN, THEN starts the clock.
  4. To connect/disconnect the sensor or emulator plug: run stop() first,
     which stops the clock and drops EN before you touch the connector.

USAGE (from the MicroPython REPL / Thonny Shell, after saving this file
to the Pico as main.py or importing it interactively):

    >>> import pico2_hsx_phase_clock as pc
    >>> pc.start(40000)     # begin spinning at f = 40 kHz
    >>> pc.status()
    >>> pc.stop()           # stop clock, drop EN, safe to unplug sensor
    >>> pc.hold_state(0b011)   # freeze at one static 8-state code (a2 a1 a0)
    >>> pc.menu()           # optional interactive text menu, see HELP below

f is the *phase rate*: each of the 8 states lasts 1/f seconds, so the full
demod cycle is 8/f seconds (200 us / 5 kHz update rate at f = 40 kHz), and
a0 itself toggles at f/2 -- matching "a0 = square wave, period 2/f" in the
bring-up plan.
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

DEFAULT_FREQ = 40_000   # Hz, phase rate (matches the bring-up plan's nominal f)

_SM_ID = 0


# ------------------------------------------------------------ PIO program --
# One "set pins" instruction per phase, 1 SM clock cycle each (no delay
# field used), so running the state machine at freq=f makes every phase
# last exactly 1/f seconds. wrap() loops back to state 0 for free (no
# extra cycle cost), so the cycle is a clean, jitter-free 8/f seconds.
#
# Bit mapping within each 4-bit value (matches the demod convention
# state = (a2<<2)|(a1<<1)|a0 from the bring-up plan):
#   bit0 -> a0   bit1 -> a1   bit2 -> a2   bit3 -> sync
# sync is high only during state 0 (a0=a1=a2=0), giving one sync pulse,
# 1/f seconds wide, at the start of every 8-phase cycle.
@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,) * 4)
def _phase_gen():
    wrap_target()
    set(pins, 0b1000)   # state 0: a2,a1,a0 = 0,0,0   sync = 1
    set(pins, 0b0001)   # state 1: a0 = 1
    set(pins, 0b0010)   # state 2: a1 = 1
    set(pins, 0b0011)   # state 3: a1,a0 = 1,1
    set(pins, 0b0100)   # state 4: a2 = 1
    set(pins, 0b0101)   # state 5: a2,a0 = 1,1
    set(pins, 0b0110)   # state 6: a2,a1 = 1,1
    set(pins, 0b0111)   # state 7: a2,a1,a0 = 1,1,1
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
_sm = rp2.StateMachine(_SM_ID, _phase_gen, freq=DEFAULT_FREQ,
                        set_base=Pin(PIN_A0))
_current_freq = DEFAULT_FREQ


def set_freq(f):
    """Reconfigure the phase rate without starting/stopping EN. Returns the
    achieved frequency (the RP2350 clock divider is 16.8 fixed-point, so
    round target frequencies against machine.freq() -- e.g. 10k/40k/100k
    against a 150 MHz sys clock -- land on an exact integer divisor)."""
    global _current_freq
    was_active = _sm.active()
    _sm.active(0)
    _sm.init(_phase_gen, freq=int(f), set_base=Pin(PIN_A0))
    _current_freq = f
    if was_active:
        _sm.active(1)
    divider = round(machine.freq() / f)
    achieved = machine.freq() / divider
    print("target {:.1f} Hz -> achieved {:.3f} Hz (sys clock {} Hz, divider {})"
          .format(f, achieved, machine.freq(), divider))
    return achieved


def start(f=None):
    """Raise EN, then start spinning at frequency f (Hz, phase rate).
    Call only after +-15V rails are confirmed and Pico GND is bonded to
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
    manual Day-3 survey (probe with a DMM/scope while stepping through
    all 8 by hand). Stops the running clock first. EN is left as-is --
    call enable() separately if it isn't already on."""
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


def status():
    print("EN     : {}".format("HIGH" if _en_pin.value() else "low"))
    print("running: {}".format(_sm.active()))
    print("freq   : {:.0f} Hz phase rate ({:.0f} Hz update rate, "
          "8-phase cycle)".format(_current_freq, _current_freq / 8))
    print("sys clk: {} Hz".format(machine.freq()))


# ------------------------------------------------------- optional menu ----
HELP = """
HSX phase-clock control -- commands:
  start [f]     raise EN and start spinning (Hz, e.g. 'start 40000')
  stop          stop spinning and drop EN (do this before (dis)connecting sensor)
  en            raise EN only
  dis           drop EN only
  freq f        change phase rate without touching EN (e.g. 'freq 100000')
  hold n        freeze at static state n = 0-7 (binary a2 a1 a0), e.g. 'hold 5'
  status        show EN / running / frequency
  help          show this message
  quit          stop and exit the menu
"""


def menu():
    print(HELP)
    while True:
        try:
            cmd = input("pico> ").strip()
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
    # Only runs if this file is executed directly (e.g. saved as main.py
    # and the board is reset). Does NOT auto-start spinning -- boots to
    # a safe idle state (EN low, SM inactive) and drops into the menu.
    menu()

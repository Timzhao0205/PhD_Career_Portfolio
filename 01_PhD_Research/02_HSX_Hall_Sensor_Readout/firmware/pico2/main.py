# main.py -- Raspberry Pi Pico 2 boot entry for the HSX phase clock.
#
# MicroPython auto-runs this file at power-up. It drops straight into the
# interactive text menu of pico2_hsx_phase_clock.py over USB serial.
# Boot is SAFE: the phase clock is idle and EN stays low until you
# explicitly start it from the menu or the REPL.
#
# To use the REPL API instead, Ctrl-C out of the menu, then:
#     >>> import pico2_hsx_phase_clock as pc
#     >>> pc.start(40_000)
#
# Full wiring / flashing / usage notes: README.md in this folder.

from pico2_hsx_phase_clock import menu

menu()

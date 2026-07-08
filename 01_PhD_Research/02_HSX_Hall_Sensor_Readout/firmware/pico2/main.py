# main.py -- Raspberry Pi Pico 2 boot entry for the HSX readout firmware.
#
# MicroPython auto-runs this file at power-up. It asks which of the two
# operating modes to run, then drops into that mode's interactive menu
# over USB serial. Boot is SAFE in both modes: EN stays low and nothing
# spins or biases until you explicitly act.
#
#   MODE 1  pico2_spin_scope.py       full current-spinning; DSOX1204G
#                                     scope is the DAQ (v_meas + sync)
#   MODE 2  pico2_static_bias_p2p4.py static bias p2 -> p4 (external
#                                     current source), p1/p3 difference
#                                     measured on the Pico ADC at J4
#
# Copy all three files to the Pico (main.py + both mode modules). To use
# the REPL API instead, Ctrl-C out of the menu, then e.g.:
#     >>> import pico2_spin_scope as sp
#     >>> sp.start(40_000)
# or:
#     >>> import pico2_static_bias_p2p4 as sb
#     >>> sb.bias_on(); sb.measure_chopped()
#
# The original single-mode module pico2_hsx_phase_clock.py still works
# (same API as MODE 1) and is kept as heritage; new work should use the
# two mode files. Full wiring / flashing / usage notes: README.md.

print()
print("HSX Hall-sensor readout -- Pico 2 clock & measurement firmware")
print("  1 = spinning + oscilloscope DAQ   (pico2_spin_scope)")
print("  2 = static bias p2/p4, Pico ADC   (pico2_static_bias_p2p4)")
print()

try:
    _choice = input("mode [1]: ").strip()
except (EOFError, KeyboardInterrupt):
    _choice = ""

if _choice == "2":
    from pico2_static_bias_p2p4 import menu
else:
    from pico2_spin_scope import menu

menu()

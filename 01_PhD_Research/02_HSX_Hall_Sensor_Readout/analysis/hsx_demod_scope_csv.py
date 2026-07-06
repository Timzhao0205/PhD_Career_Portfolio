#!/usr/bin/env python3
"""
hsx_demod_scope_csv.py
-----------------------
Demodulate a DSOX1204G capture of the HSX Hall readout board.

Only TWO scope channels are used -- v_meas (amplifier output, J4/BNC) and
sync (Pico GP19). a0/a1/a2 never go to the scope: the 8-phase state at
every sample is reconstructed purely from the sync pulse (high only
during state 0) plus the known, fixed phase rate f you told the Pico to
run at. That leaves the DSOX1204G's other 2 channels free for a
reference sensor or the emulator's second node in later weeks.

USAGE
  python3 hsx_demod_scope_csv.py capture.csv --f 40000

  Column layout and header rows vary with your scope's export settings --
  open the CSV in a text editor once and check before trusting the
  defaults below (--tcol/--vcol/--synccol/--skip-header).

OUTPUT
  Prints the number of usable phase segments, the demodulated mean
  (your offset-cancellation figure of merit -- compare to the raw
  step size), and its standard deviation (a quick noise number).
  With --out, also writes a two-column CSV (segment index, demodulated
  value) for plotting drift/noise over a longer capture.
"""

import argparse
import sys

import numpy as np


def reconstruct_phase(t, sync, f, thresh=1.65):
    """Reconstruct the 8-state phase index (0-7) at every sample, from the
    sync channel alone (high only during state 0) plus the known phase
    rate f. sync is a clean 0/3.3 V logic signal straight from the Pico
    GPIO (not routed through the analog front end), so a fixed threshold
    is fine -- no per-capture calibration needed.

    t: sample times [s], monotonically increasing (as scope CSVs are).
    sync: sampled sync voltage [V], same length as t.
    Returns an int64 array; entries before the first sync edge are -1
    (phase unknown there -- reconstruct_phase can't see before the first
    marker, so those samples are dropped downstream)."""
    above = sync > thresh
    rising = np.flatnonzero(np.diff(above.astype(int)) == 1) + 1
    if len(rising) == 0:
        raise ValueError(
            "no sync rising edge found -- check --synccol, --thresh, "
            "and that the capture window actually spans a sync pulse")
    t0 = t[rising[0]]
    phase = np.floor((t - t0) * f).astype(np.int64) % 8
    phase[t < t0] = -1
    return phase


def demodulate(t, v, sync, f, blank_frac=0.3):
    """Full pipeline: v_meas + sync (2 scope channels) + known f -> demod.
    blank_frac discards the leading fraction of each phase segment (mux
    charge injection / amplifier settling) before averaging -- the plan
    doc's Day 4-5 frequency study is exactly where you tune this number.

    Returns (vals, sgns, demod):
      vals -- per-phase-segment mean of v_meas
      sgns -- the +-1 sign applied to that segment (a0==a2 rule)
      demod -- rolling 8-phase average of vals*sgns (the actual output)
    """
    phase = reconstruct_phase(t, sync, f)
    valid = phase >= 0
    v, phase = v[valid], phase[valid]
    sign = np.where((phase & 1) == ((phase >> 2) & 1), 1.0, -1.0)  # a0==a2
    edges = np.flatnonzero(np.diff(phase)) + 1
    segs = np.split(np.arange(len(v)), edges)
    vals, sgns = [], []
    for idx in segs:
        if len(idx) < 10:  # runt segment at capture start/end -- discard
            continue
        keep = idx[int(blank_frac * len(idx)):]
        vals.append(v[keep].mean())
        sgns.append(sign[keep[0]])
    if len(vals) < 8:
        raise ValueError(
            "fewer than 8 usable phase segments in this capture -- "
            "capture a longer window (several full 8-phase cycles)")
    vals, sgns = np.array(vals), np.array(sgns)
    demod = np.convolve(vals * sgns, np.ones(8) / 8, mode="valid")
    return vals, sgns, demod


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv", help="path to the scope CSV export")
    p.add_argument("--f", type=float, default=40_000,
                    help="phase rate in Hz, matching what the Pico was running (default 40000)")
    p.add_argument("--tcol", type=int, default=0, help="time column index (default 0)")
    p.add_argument("--vcol", type=int, default=1, help="v_meas column index (default 1)")
    p.add_argument("--synccol", type=int, default=2, help="sync column index (default 2)")
    p.add_argument("--skip-header", type=int, default=1,
                    help="header rows to skip (default 1 -- check your file)")
    p.add_argument("--thresh", type=float, default=1.65,
                    help="sync threshold in volts (default 1.65, i.e. half of 3.3V logic)")
    p.add_argument("--blank", type=float, default=0.3,
                    help="fraction of each phase to blank before averaging (default 0.3)")
    p.add_argument("--out", default=None,
                    help="optional path to write (segment_index, demod_value) CSV")
    args = p.parse_args()

    try:
        data = np.genfromtxt(args.csv, delimiter=",", skip_header=args.skip_header)
    except Exception as e:
        sys.exit("failed to read {}: {}\n"
                  "open the file in a text editor and check --skip-header / "
                  "the delimiter matches what your scope exported".format(args.csv, e))

    if data.ndim != 2 or data.shape[1] <= max(args.tcol, args.vcol, args.synccol):
        sys.exit("CSV does not have the expected columns -- got shape {}. "
                  "Check --tcol/--vcol/--synccol against your actual file.".format(data.shape))

    t, v, sync = data[:, args.tcol], data[:, args.vcol], data[:, args.synccol]

    vals, sgns, demod = demodulate(t, v, sync, args.f, args.blank)

    print("usable phase segments : {}".format(len(vals)))
    print("demodulated mean [V]  : {:.6g}".format(demod.mean()))
    print("demodulated std  [V]  : {:.6g}  (noise figure of merit)".format(demod.std()))
    print("raw segment amplitude : {:.6g} V (mean |v|, sanity check vs expected step size)"
          .format(np.mean(np.abs(vals))))

    if args.out:
        out_arr = np.column_stack([np.arange(len(demod)), demod])
        np.savetxt(args.out, out_arr, delimiter=",", header="segment_index,demod_v", comments="")
        print("wrote {} rows to {}".format(len(demod), args.out))


if __name__ == "__main__":
    main()

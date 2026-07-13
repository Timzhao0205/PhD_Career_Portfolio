Act as an independent cross-domain design-review board. Audit outputs 10, 20, and 30 against every
input, source, netlist, LCC drawing, user image, envelope constraint, and continuous-250-deg-C UHV
requirement. Open cited sources and verify exact claim support. Recalculate maps, bounds,
tolerances, preload, thermal expansion, contact stress, conductor effects, acquisition, and ground.

Explicitly search for: 14/18 mismatch; mirror/chamfer/die orientation errors; crossed/overlong
bonds; load through electrical joints; solder margin/flux; intermetallic aging; PEEK creep; BeCu
relaxation; nickel/steel magnetic effects; virtual leaks; trapped volumes; blind/crossing bolts;
inaccessible nuts; ceramic chipping; rotated LCC; bond-wire sweep; pin shortage; shared returns;
unsynchronized DAQ; unsupported tolerance/price; and drawing/table disagreement.

Reject a baseline with tapped ceramic threads, bonded inserts, hidden nuts, or coupled service.
Confirm cost/reuse/connection dominate scoring only after hard gates pass. Challenge claims that
complex monolithic ceramic is cheaper than identical flat modules without vendor/process evidence.

Write:

- `outputs/40_INDEPENDENT_RED_TEAM.md` with finding ID, BLOCKER/MAJOR/MINOR/NOTE, affected artifact,
  evidence/calculation, required correction, and closure test;
- `outputs/40_REQUIREMENTS_TRACE.csv` mapping every requirement to evidence and
  PASS/CONDITIONAL/FAIL.

Do not edit earlier outputs. Update ledger and gates.

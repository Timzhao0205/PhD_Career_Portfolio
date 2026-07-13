# SOURCE_STANDARDS — how to be accurate (and provably so)

The whole point of this pack is that Fable 5 gives you *correct* part facts, not
plausible-sounding ones. Enforce this:

## 1. Search-first, primary sources only
- Every component spec, pinout, absolute-maximum, vacuum/temperature rating, CF size, or
  price comes from a **primary source**: the manufacturer datasheet (Analog Devices, RECOM,
  Amphenol, Molex, Raspberry Pi) or the vendor product page (Digi-Key, Accu-Glass).
- Fetch the page during the run. Do not answer part questions from model memory — datasheets
  revise and memory drifts. If a fetch fails, try the manufacturer PDF directly, then Digi-Key.

## 2. Cite inline
- After any number, put the source: `R_on = 120 Ω [ADG1209 datasheet Rev G, Table 3]` with the
  URL in a Sources block at the end of the file. One deliverable = one Sources block.

## 3. Mark uncertainty honestly
- Can't verify → write `UNVERIFIED` and say what page/spec you needed. Never paper over a gap.
- Separate **verified-from-datasheet** from **engineering judgment**. Both are allowed; label
  which is which.

## 4. Reconcile against the given design
- HARDWARE_DATA §1/§3 is authoritative for *what is on the board*. Datasheets are authoritative
  for *how the parts behave*. If the live netlist disagrees with HARDWARE_DATA, report the
  discrepancy — don't silently pick one.

## 5. Numbers discipline
- Units on everything. Show the one-line calculation for any derived quantity (e.g., fan-out
  capacitance, feedthrough current headroom, gain). Round sensibly; keep the intermediate.

## 6. Don't hallucinate part numbers or pinouts
- A wrong pin map or a non-existent part number is the worst possible output of this pack (it
  causes shorts or bad purchases — exactly the user's stated fear). When in doubt, fetch the
  mechanical drawing / pin table and quote it.

## 7. Freshness
- Confirm parts are still active/orderable (not NRND/obsolete) and note lead time if visible;
  the build is on a 2026 schedule.

# Mission — rebuild the 2026 HSX packaging/readout decision

Produce a source-audited continuation addressing three questions under continuous 250 deg C UHV:

1. Recommend the Hall die -> LCC02046 wire-bond map and the LCC -> one-side harness connection.
   Directly assess the user's annotated proposal: inner pads 8,3,19,14 and external routes 8-4,
   3-9, 19-13, 18-14. Resolve the 14/18 contradiction. Separate electrical redundancy from
   mechanical strain relief and compare solder, weld, crimp, spring/socket, and other credible
   high-temperature UHV transitions.
2. Explain exactly how three ambient readout boards connect to three in-vessel sensors. Determine
   what is shared and what remains independent; provide a complete 12-conductor feedthrough map,
   logic fanout, power/isolation, grounding/shielding, synchronization, and simultaneous DAQ plan.
3. Recommend a reusable, low-cost CNC ceramic 3-axis head. Reuse every bonded sensor/LCC, improve
   the electrical connection, fit the envelope, and use zero tapped zirconia threads in the
   baseline. Compare modular identical flat seats against simplified monolithic and cartridge/
   clamshell alternatives with real dimension, collision, tolerance, assembly, and cost checks.

The workflow runs seven ordered stages under `prompts/`. Previous processed work is under
`previous_results/`; it is evidence to reconcile, not an answer to copy. Final deliverables belong
under `outputs/` and must include drawings, ledgers, qualification tests, open gates, and a concise
build recommendation.

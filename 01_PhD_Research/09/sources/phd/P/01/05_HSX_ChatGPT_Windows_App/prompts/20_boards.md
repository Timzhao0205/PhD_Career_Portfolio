Resolve the complete architecture connecting three ambient readout boards to three in-vessel
four-terminal Hall sensors. Read `AGENTS.md`, all completed outputs, the live netlist/BOM, previous
connection/fanout/flange/wiring results, and the current 19C-275 decision.

State plainly whether one board should receive data and transfer it to two other boards. Compare
three independent analog boards near the feedthrough, an interface junction plus three boards,
and any credible local-digitization alternative without redesigning unnecessarily.

Cover quantitatively:

- all 12 Hall conductors through a 19-pin feedthrough and a complete pin map;
- independent floating 100 uA bias per axis and prohibited shared returns;
- a0/a1/a2/EN fanout, logic ground, capacitance/edge rate, cable length, buffer and series-resistor
  thresholds;
- three simultaneous analog outputs to ADC/DAQ, sampling sync, anti-aliasing, calibration, and
  connectorization;
- DC/DC isolation, chassis/earth, shields, star points, ground-loop and fault containment;
- exactly what is shared between boards and what must remain independent;
- pre-power continuity/insulation/channel-swap and injected-signal tests.

Write:

- `outputs/20_THREE_BOARD_READOUT_ARCHITECTURE.md`;
- `outputs/drawings/20_end_to_end_block.svg` from dies through LCCs/feedthrough/PCBs/Pico/DAQ;
- `outputs/drawings/21_ground_and_shield.svg`;
- `outputs/20_PIN_AND_CABLE_MAP.csv` with unique net, axis, terminal, pair/shield, color/label,
  feedthrough pin, board/J1 pin, endpoints, and expected pre-power resistance.

Include a procurement-ready connector/cable list but mark unverified facts. Update the ledger and
open gates. Do not edit previous results.

# Risk register

| ID | Risk | L | I | Mitigation / trigger |
|---|---|---|---|---|
| RK-01 | Electrode electrochemical drift through passivation pinholes | M | H | Parylene-C; 30-min DI soak test (P0-E0); silicone backup; drift >0.5 %ABV/4h → new coating |
| RK-02 | Bubble occlusion of thin sensing skin during stir | M | H | Fine pitch + multi-patch voting + mode estimator; measure occlusion stats in P0-E3 |
| RK-03 | NTC lag corrupts T-comp during fast chill | M | M | Small glass bead (<1 s tau); model lag; fuse with melt model |
| RK-04 | Hand/glass parasitics couple into fringing field | M | M | Guard ring; grounded shield; quantify in P0-E0 |
| RK-05 | Per-spirit calibration offsets exceed budget | L | M | Offset term per spirit family; verify 3 whiskies in P0-E2 |
| RK-06 | Ethanol + electronics fire/safety incident | L | H | Protocol safety blocks; no heat sources; ventilation; small volumes |
| RK-07 | Scope creep to full cocktails before P0 gate | M | M | DECISIONS.md D-003; sugar work parked until binary passes |
| RK-08 | Stanford IP entanglement | L | H | CLAUDE.md rule 3; SNF parylene flagged as removable dependency; no group IP |
| RK-09 | FDC2214 SNR insufficient at chosen pitch | L | M | EVAL-AD7746 fallback with guard scheme; pitch ladder on coupon panel |

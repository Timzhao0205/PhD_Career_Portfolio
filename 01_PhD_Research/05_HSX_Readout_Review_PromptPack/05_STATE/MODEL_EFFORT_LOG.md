# MODEL / EFFORT LOG — one row per switch (required for cost accounting)

Format: `YYYY-MM-DD HH:MM · subtask · model · effort · reason`. Newest at bottom.
The orchestrator MUST append a row every time it changes model or effort (see MODEL_EFFORT_POLICY.md).

| time | subtask | model | effort | reason |
|---|---|---|---|---|
| (pack authored) | — | — | — | policy set; run not started |
| 2026-07-10 12:14 | orchestrator | Fable 5 | high | launch model; orchestration + all state housekeeping inline (Haiku-spawn overhead > inline cost; logged fallback) |
| 2026-07-10 12:14 | ST1 components | Fable 5 | medium | per policy: judgment-heavy part-selection call |
| 2026-07-10 12:14 | ST2 connections | Sonnet | medium | per policy: bounded netlist/pinout verification |
| 2026-07-10 12:14 | ST3 3-axis arch | Fable 5 | high | per policy: irreversible board decision |
| 2026-07-10 12:14 | ST4 pi fan-out | Sonnet | medium | per policy: bounded capacitance/drive calc |
| 2026-07-10 12:14 | ST5 flange | Fable 5 | high | per policy: spends money, vacuum-critical |
| 2026-07-10 12:14 | ST7 wirebond | Fable 5 | high | per policy: in-vessel, bond-map correctness |
| 2026-07-10 12:25 | ST6 wiring & shorts | Fable 5 | high | per policy: user's #1 worry; launched after ST5 (flange pick feeds pin map) |
| 2026-07-10 12:29 | ST8 3D packaging | Fable 5 | high | per policy: most generative, in-vessel, envelope-critical CAD; launched after ST7 (pad map + open-cavity handoffs) |
| 2026-07-10 12:43 | red-team wave 1 (ST1–ST7) | Fable 5 | high | per policy: the check that catches the costly wrong answer; started early while ST8 renders |
| 2026-07-10 13:03 | red-team wave 2 (ST8) | Fable 5 | high | per policy: in-vessel decision-gate item; envelope + contact physics audit |
| 2026-07-10 13:15 | synthesis + decision gates | Fable 5 | high | per policy: sign-off artifacts must be right; written by orchestrator directly |

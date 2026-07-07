# 01_PhD_Research — folder index

Research arc: GaN Hall-effect magnetic sensing for fusion diagnostics
(HSX stellarator). Demonstrated in-situ (2023 Letters) → calibrated
spinning-current readout (02, HSX install Aug 2026) → calibrated 2–3
axis vector probe + second HSX campaign (03, RSI paper, ~Mar 2027).

- `01_Publications/` — published papers; `in_preparation/` holds
  co-authored drafts (currently: Van Gorp et al., radiation TCAD
  modeling — simulation only, no experimental radiation work planned).
- `02_HSX_Hall_Sensor_Readout/` — single-axis spinning-current readout:
  bring-up + calibration plan (`docs/`), one-page quick reference
  (`docs/SPECS.md`), Pico 2 firmware (`firmware/pico2/`), scope demod
  CLI (`analysis/`), netlists/schematics/gerbers (`circuit/`), running
  log (`NOTES.md`).
- `03_HSX_Vector_Probe_RSI2026/` — vector-probe experiment and RSI
  publication plan (`docs/`), running log (`NOTES.md`).
- `CLAUDE.md` + `.claude/` — Claude Code memory, budget defaults
  (opusplan + medium effort), slash commands (`/log`, `/specs`,
  `/deep`), and the `rsi-editor` review agent. Launch `claude` from
  THIS folder so the commands and agent are picked up.

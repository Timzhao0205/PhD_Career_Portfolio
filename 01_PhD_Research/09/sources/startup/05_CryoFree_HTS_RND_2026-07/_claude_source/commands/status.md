---
description: Print current RUN_STATE, budget, and per-candidate gate status.
---
Read 80_STATE/RUN_STATE.json and the latest lines of 80_STATE/PROGRESS_LOG.md.
Print: current wave/phase, budget tokens used/left, per-candidate status
(harvested? simulated? gate verdict?), and the single next action. Do not do work.

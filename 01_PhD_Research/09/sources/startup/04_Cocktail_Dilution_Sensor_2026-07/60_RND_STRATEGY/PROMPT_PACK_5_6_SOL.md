# Prompt Pack - 5.6 Sol R&D Sessions

Date: 2026-07-09

Working assumption: "5.6 sol" means a high-capability reasoning session/model
used as an engineering collaborator. If it means a specific tool in your
workflow, keep the prompts and replace only the model/tool name.

## Reliability Rules To Paste Into Every Session

```text
You are helping with the project "04_Cocktail_Dilution_Sensor_2026-07".
Goal: create a real-time whisky+ice cocktail dilution/ABV sensor using an
interdigitated capacitive electrode, co-located NTC, IMU gating, and robust
mode-based estimation.

Reliability rules:
1. Use the project files as ground truth before inventing architecture.
2. Separate facts, assumptions, calculations, and recommendations.
3. Cite datasheets or official docs for component claims.
4. If a parameter is unknown, mark it "bench-fit required" and propose the
   smallest experiment to measure it.
5. Never silently change locked specs. If the bench contradicts SPECS.md,
   write a note and propose an update.
6. Prefer pass/fail gates over vague next steps.
7. For hardware, output DRC/ERC constraints, test points, and bring-up tests.
8. For firmware, keep estimator math traceable to the Python reference.
9. For experiments, define controls, replicates, raw data fields, and exit
   criteria.
10. End with: risks, assumptions to verify, and the next 3 concrete actions.
```

## Master R&D Strategy Prompt

```text
Read these files first:
- 00_README_START_HERE.md
- 01_PRODUCT/PRODUCT_BRIEF.md
- 01_PRODUCT/REQUIREMENTS.md
- 10_SENSING_DESIGN/SENSING_STRATEGY.md
- 10_SENSING_DESIGN/SPECS.md
- 40_EXPERIMENTS/PLAN_P0_dipstick.md
- 60_RND_STRATEGY/RD_STRATEGY_2026-07.md

Task:
Create a 2-week R&D sprint plan for the cocktail dilution sensor. Include
LTspice work, KiCad work, firmware work, experiments, and analysis. For each
task, give owner mode, inputs, outputs, pass/fail criteria, and dependencies.

Constraints:
- Phase 0 budget <= $400 unless explicitly justified.
- Do not assume sugared/citrus cocktails are in scope.
- Keep FDC2214EVM + coupon panel as the default first build.
- Treat XIAO nRF52840 Sense as the default P1 MCU unless evidence supports
  switching to Pico/Pico 2 W.
- Use only official datasheets/docs for component facts.

Output format:
1. Sprint objective
2. Task board table
3. Critical path
4. Experiments and expected data files
5. Hardware design actions
6. Firmware design actions
7. Risks and kill criteria
8. Next 3 actions
```

## LTspice Prompt

```text
Read:
- 10_SENSING_DESIGN/SPECS.md
- 20_HARDWARE/readout/README.md
- 60_RND_STRATEGY/RD_STRATEGY_2026-07.md

Task:
Define the LTspice simulations worth doing for this project. Do not attempt
to model the FDC2214 internals unless a vendor macromodel exists. Focus on:
1. NTC divider + ADC input sensitivity and filtering.
2. LC tank sensitivity to sensor capacitance and cable parasitics.
3. Leakage/guard/parasitic effects as lumped models.
4. Optional Phase 1 power integrity.

For each simulation, provide:
- Circuit purpose.
- Minimal schematic blocks.
- Parameters and sweep ranges.
- Expected plots.
- What decision the simulation changes.
- What must be measured on the bench to validate the model.

Use official datasheets/docs for numerical component claims. Label all
guesses "bench-fit required".
```

## KiCad Prompt

```text
Read:
- 20_HARDWARE/electrodes/README.md
- 20_HARDWARE/readout/README.md
- 10_SENSING_DESIGN/SPECS.md
- 60_RND_STRATEGY/RD_STRATEGY_2026-07.md

Task:
Create a KiCad implementation plan for the P0 electrode coupon panel and the
P1 readout board. Start with P0; do not overbuild P1 until P0 pass gates are
met.

Output:
1. P0 coupon schematic/net naming plan.
2. P0 PCB geometry constraints: pitch, active area, guard, ground pour,
   connector, coating controls.
3. Fabrication constraints for standard low-cost PCB vendors.
4. DRC/ERC checklist.
5. P0 bring-up test checklist.
6. P1 readout board block diagram and only the decisions that depend on P0.
7. Risks that can make the PCB data misleading.

Rules:
- Keep high-impedance sensor routes short.
- Include a bare-control coupon only as an intentional drift control.
- Require test pads and a clear coupon ID marking scheme.
- Flag anything that needs a datasheet check.
```

## Microcontroller Choice Prompt

```text
Read:
- 30_FIRMWARE/xiao_nrf52840/README.md
- 10_SENSING_DESIGN/ESTIMATOR_SPEC.md
- 60_RND_STRATEGY/RD_STRATEGY_2026-07.md

Task:
Compare XIAO nRF52840 Sense, Raspberry Pi Pico W, and Raspberry Pi Pico 2 W
for this specific cocktail dilution sensor. Do not make a generic MCU
comparison.

Decision criteria:
- BLE streaming reliability
- IMU availability for strike/stir gating
- I2C readout of FDC2214
- ADC quality for NTC divider
- power and form factor
- firmware ecosystem
- speed to first prototype

Output:
1. Decision table.
2. Recommendation for Phase 0, Phase 1, and Phase 2.
3. What would trigger switching MCUs.
4. Firmware architecture that keeps Python estimator and MCU estimator aligned.
5. Specific unknowns requiring datasheet or bench verification.
```

## Experiment Protocol Prompt

```text
Read:
- 40_EXPERIMENTS/PLAN_P0_dipstick.md
- 40_EXPERIMENTS/CALIBRATION_PROTOCOL.md
- 10_SENSING_DESIGN/ESTIMATOR_SPEC.md
- 60_RND_STRATEGY/RD_STRATEGY_2026-07.md

Task:
Turn the Phase 0 plan into executable lab protocols. Include exact materials,
setup, step order, run log fields, controls, failure modes, and pass/fail
criteria.

Required protocols:
1. P0-E0 sanity, drift, parasitics.
2. P0-E1 static ABV/temperature calibration.
3. P0-E2 dynamic dilution with strain-and-weigh ground truth.
4. P0-E3 chaos testing with bubbles, ice strikes, and partial immersion.
5. Coating before/after sensitivity and drift test.

Output:
- One protocol per section.
- Data filename convention.
- Minimum number of replicates.
- Safety notes for 190-proof ethanol and non-food-safe hardware.
- What plots should be generated after each protocol.
```

## Source Audit Prompt

```text
Task:
Audit the R&D strategy for unsupported claims. For every component, tool,
or performance claim, classify it as:
- project-file fact
- official-source fact
- calculation
- assumption
- bench-fit required
- unsupported/remove

Use official sources first: TI, Seeed, Raspberry Pi, KiCad, Analog Devices,
and vendor datasheets. Do not use forums for final factual claims unless the
claim is explicitly about user experience and is labeled as anecdotal.

Output:
1. Claim audit table.
2. Missing citations.
3. Claims that should be softened.
4. Experiments needed to replace assumptions with measured facts.
```

## Red-Team Prompt

```text
Act as a skeptical hardware/product reviewer. Your job is to kill weak ideas
early, not to be encouraging.

Read:
- 01_PRODUCT/RISK_REGISTER.md
- 10_SENSING_DESIGN/SENSING_STRATEGY.md
- 40_EXPERIMENTS/PLAN_P0_dipstick.md
- 60_RND_STRATEGY/RD_STRATEGY_2026-07.md

Task:
Find the top 10 ways this project can fail technically or as a portfolio
product. For each failure mode, give:
- why it is plausible
- earliest cheap test
- pass/fail threshold
- mitigation
- whether it is a kill, pivot, or acceptable risk

Special focus:
- electrode drift and coating
- bubble and ice-strike corruption
- temperature lag
- calibration transfer across whiskies
- cleanability and sealing
- whether "smart barspoon" is worse than "clip-on probe"
```

## Daily Work Prompt

```text
Use this folder as the project memory. Start by reading:
- 05_STATE/MASTER_STATE.json
- 05_STATE/DECISIONS.md
- 05_STATE/PROGRESS_LOG.md
- 60_RND_STRATEGY/RD_STRATEGY_2026-07.md

Task:
Continue the next highest-leverage R&D task. Before acting, state:
1. What you read.
2. What decision gate this task advances.
3. What files you will create or update.

Then do the work. At the end, update the relevant notes with:
- result
- evidence
- open questions
- next action
```


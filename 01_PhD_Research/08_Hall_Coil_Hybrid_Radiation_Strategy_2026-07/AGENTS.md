# Agent contract

Work only inside this `08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07`
directory. All sibling folders, especially `06` and `07`, are read-only input.

Read `CLAUDE.md`, `MISSION.md`, `SOURCE_POLICY.md`, `DECISION_FRAMEWORK.md`,
and the current stage prompt before acting.

Use web search and web fetch for current and primary-source verification.
Never invent a DOI, venue, citation, radiation condition, performance number,
or collaborator. A search-result snippet is discovery evidence, not full-text
evidence. Record the access level honestly.

For every accepted stage:

1. Write all named outputs.
2. Update `state\PROJECT_STATE.md` and append `state\WORKLOG.md`.
3. Create a human-readable checkpoint under `state\checkpoints`.
4. Run the stage's internal checks before returning.
5. Report the output files and any unresolved gate in the final main response.

Do not alter the runner, policies, prior stage evidence, or completion markers
from inside a research stage. Do not invoke another model provider or external
connector. Do not send outreach.

Fable-assigned stages require a Fable 5 final main response. Auxiliary models
may help, but Fable must personally reconcile and sign off the accepted files.

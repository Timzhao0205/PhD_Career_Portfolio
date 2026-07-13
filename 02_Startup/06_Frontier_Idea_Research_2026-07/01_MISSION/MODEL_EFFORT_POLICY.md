# Model and effort policy

| Work | Model | Effort | Why | Classification |
|---|---|---:|---|---|
| Orchestration, anti-anchoring, phase gates | `claude-fable-5` | xhigh | Long-horizon judgment | Critical |
| Lane/source discovery | `claude-sonnet-5` | medium | Search breadth dominates | Economy route |
| Peer-review and claim verification | `claude-sonnet-5` | high | Repetitive but accuracy-sensitive | Economy route |
| P2A India source-origin audit | `claude-sonnet-5` | high | Full-ledger affiliation and organization verification | Economy route |
| P2A origin adjudication | inherit Fable 5 | xhigh | Critical sampling, exception review, and atlas sign-off | Critical |
| Demand/competitor evidence | `claude-sonnet-5` | high | Primary-source retrieval | Economy route |
| P3 round-2 idea architecture | inherit Fable 5 | xhigh | Five independent geographic/technical synthesis batches | Critical |
| P3 elegance/novelty adjudication | inherit Fable 5 | xhigh | Independent second pass before longlist freeze | Critical |
| Red-team and score adjudication | inherit Fable | xhigh | Avoid fluent but weak ideas | Critical |
| Deep dives and final portfolio | inherit Fable | xhigh | Highest-consequence judgment | Critical |
| Mechanical audit | Sonnet 5 | high | Counting/schema/link checks | Economy route |
| Final audit adjudication/fixes | inherit Fable | xhigh | Substantive sign-off | Critical |

No automatic fallback. The environment variables `FRONTIER_CRITICAL_MODEL` and
`FRONTIER_SCOUT_MODEL` are written by the launcher. Fixed subagent aliases are expected to resolve
to the documented IDs above; record the resolved/configured value. If unavailable, fail and log.

Every dispatch appends one JSON object to `98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl`:

```json
{"timestamp":"ISO-8601","phase":"P1","task":"L03","requested_model":"claude-sonnet-5","actual_model":"claude-sonnet-5","effort":"medium","reason":"source discovery","downgrade":false,"status":"started|complete|failed","source":"orchestrator|agent"}
```

`downgrade=true` whenever a configured critical task is run below Fable 5/xhigh or a search task
below Sonnet 5/medium. An intentional Sonnet route in the table is not a downgrade, but it must
still be visible. Never infer successful routing from output quality.

Claude Code supports `max` effort only where the selected model exposes it. This package uses the
documented Fable 5 capability-sensitive setting `xhigh` and upgrades P3 through an independent
second Fable/xhigh pass. Do not silently switch to `max`; an operator may test it explicitly only
after the launcher probe succeeds and must record the override.

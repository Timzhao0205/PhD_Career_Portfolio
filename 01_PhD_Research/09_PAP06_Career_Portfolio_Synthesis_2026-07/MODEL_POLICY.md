# Native model and effort policy

## Fixed routing

- Visible main controller: `pap06-controller`, Fable 5/xhigh.
- Critical workers: `pap06-fable-xhigh`, Fable 5/xhigh.
- B00, B10, and B12 workers: `pap06-sonnet-high`, Sonnet 5/high.
- Every full-stage verifier: `pap06-verifier`, Fable 5/xhigh.
- No Opus request: it was unavailable in the user's organization.
- No automatic fallback chain and no accepted model substitution.

The launch command, project settings, and agent frontmatter independently
request the intended main model, effort, and permission mode. Agent
frontmatter independently requests each worker/verifier model and effort.

## Evidence honesty

Each run records:

- stage and pilot/full mode;
- exact named agent;
- requested model and effort;
- observed model and effort only if Claude Code explicitly exposes them;
- `NOT_EXPOSED` otherwise;
- available timing, source, web, retry, and limitation information.

A requested configuration proves intent, not provider-side execution. Missing
observation is neither a mismatch nor proof. An explicit mismatch rejects the
attempt. Sonnet output is never relabeled as Fable work.

## Retry policy

One fresh retry is allowed after an explicit mismatch or safe-request provider
safeguard. A second event creates a durable model/provider pause. Content
failures are repaired through fresh stage workers and fresh verifiers. There is
no monetary retry ceiling, but three repetitions of the same structural defect
create a correctness blocker to prevent an infinite loop.

## No budget shutdown

No cost, token, turn, time, or elapsed-runtime limit stops the workflow. Model
routing is an optimization only. Subscription limits, provider safeguards,
network availability, and organization restrictions are external facts that
the package cannot override.

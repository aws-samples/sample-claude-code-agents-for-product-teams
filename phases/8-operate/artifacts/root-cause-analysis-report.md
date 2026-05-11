# root cause analysis report

_Produced by: Root cause analysis_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** Developer, Architect

## What this is

The post-incident analysis that traces an outage back to its contributing causes (plural, usually) and identifies the systemic conditions that allowed it to happen. More than "the bug was here" — it is the "why did our system let this bug reach customers?"

## Why it matters for the SRE

RCAs are the currency of reliability improvement. A well-done one converts pain into durable changes — detection upgrades, guardrails, architectural fixes — that retire a whole class of incident. A shallow one generates action items that paper over the next occurrence.

## Definition of Done

- [ ] Contributing causes are enumerated across technical, process, and organisational dimensions.
- [ ] Latent conditions that enabled the incident are traced on a timeline.
- [ ] Detection and mitigation delays are explained, not just described.
- [ ] Action items have owners and deadlines.
- [ ] Incident class and recurrence history are identified.

## What it contains

- Contributing causes (technical, process, organizational)
- Timeline of latent conditions that enabled the incident
- Why detection was late or noisy
- Why mitigation took as long as it did
- Action items with owners and deadlines
- Class of incident and recurrence history

## Inputs you rely on

- Incident investigation report(s)
- Change history (deploys, config, migrations)
- Prior postmortems for related causes
- Architecture document and threat model
- Telemetry deep-dives during the incident window

## Who consumes it

- Architect — inputs to architecture updates and scale-readiness report
- Developer — concrete code and design action items
- Sponsor — operational performance review context
- Security & Compliance — if controls failed or need strengthening

## Common pitfalls

- Stopping at the first root cause instead of the contributing set
- Blaming humans when the system permitted the error
- Generic action items ("improve monitoring") with no owner
- RCAs that sit in a folder; no loop back to verify fixes landed

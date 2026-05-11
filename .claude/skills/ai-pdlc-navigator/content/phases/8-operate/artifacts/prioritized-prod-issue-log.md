# prioritized prod issue log

_Produced by: Triage & log production issues for developer fixes_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

## What this is

The ordered queue of production issues SRE has triaged and handed to engineering — bugs, reliability gaps, toil items, and follow-ups from incidents. Each has a severity, owner, and fix-or-defer status.

## Why it matters for the SRE

Without disciplined triage, every production noise becomes a new "drop everything" request or, worse, nothing. A shared prioritized log is how SRE and engineering co-own reliability: you surface the pain, they fix it, and the list shows whether the commitment is real.

## Definition of Done

- [ ] Every entry has a description, severity, and customer-impact note.
- [ ] Source (incident, RCA, alert, support, scan) is identified.
- [ ] A proposed owner and target release are assigned.
- [ ] Current status is set (open, in-flight, done, or deferred with rationale).
- [ ] Related incidents and postmortems are linked for traceability.

## What it contains

- Issue description, severity, and customer impact
- Source (incident, RCA, alert, support, scan)
- Proposed owner and target release
- Workaround, if any
- Status (open, in-flight, done, deferred with rationale)
- Links to related incidents and postmortems

## Inputs you rely on

- Incident investigation and RCA reports
- Monitoring alerts and error-budget burns
- Escalated support tickets
- Architectural conformance findings
- Vulnerability scan reports

## Who consumes it

- Developer — next work to pull
- Product Owner — negotiates with feature backlog
- Architect — patterns across issues feed architecture updates
- Sponsor — signal on reliability investment needs

## Common pitfalls

- Every issue tagged Sev-1; nothing actually gets prioritized
- No agreed SLA between severity and fix timeline
- Deferred items never revisited; debt compounds
- Log lives only in chat; no traceability back to incidents

# incident investigation report

_Produced by: Investigate production errors_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required when incidents occur; otherwise skip

## What this is

The structured write-up of a single production incident — what happened, who was affected, how it was detected, what was tried, and how it was resolved. Created contemporaneously during or immediately after the incident.

## Why it matters for the SRE

Incidents are expensive; the second-most expensive thing is learning nothing from them. A disciplined investigation report is the raw material for root-cause analysis, postmortems, customer communications, and trend reporting. Without it, the same classes of incident keep recurring.

## Definition of Done

- [ ] Timeline entries carry UTC timestamps and the actor responsible.
- [ ] Detection source is identified (alert, user report, monitoring).
- [ ] Customer impact is measured: who, what, and for how long.
- [ ] Every mitigation attempt and its effect is documented.
- [ ] Final resolution state and any open follow-ups for the postmortem are recorded.

## What it contains

- Timeline with UTC timestamps and actors
- Detection source (alert, user report, monitoring)
- Customer impact (who, what, for how long)
- Mitigation steps attempted and effect
- Final resolution and state at recovery
- Open follow-ups before the postmortem

## Inputs you rely on

- Monitoring dashboards & alerts data during the incident
- Chat/ops transcripts and pager history
- Deployment and config-change history
- Tickets and customer reports flowing through Support
- Vendor/partner status updates

## Who consumes it

- Root cause analysis and postmortem writers
- Security & Compliance — if the incident touched controlled data
- Customer Support — to inform customer-facing comms
- Business Analyst — feeds incident-trend analysis

## Common pitfalls

- Writing after the fact from memory — timeline loses fidelity
- Blaming people instead of describing system behavior
- Customer impact estimated instead of measured
- No linkage to the RCA/postmortem that follows

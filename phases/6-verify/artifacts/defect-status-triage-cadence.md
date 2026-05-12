# defect status & triage cadence

_Produced by: Issue / defect governance_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Project Manager

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — a shared bug board is enough

## What this is

The governance cadence for defect management through Verify — how often triage runs, who chairs, decision rights, severity calibration, and the reporting that keeps the defect pipeline healthy during the highest-volume window of the initiative.

## Why it matters for the Project Manager

Defect queues explode during Verify and become political fast — every stakeholder wants their finding prioritized. Running a structured, cadenced triage with clear decision rights is how you maintain a fair, fast pipeline and prevent the queue from becoming a proxy for stakeholder power games.

## Definition of Done

- [ ] Triage meeting cadence and chair are named
- [ ] Severity rubric and escalation rules are defined
- [ ] Decision rights (fix-now, defer, accept) are assigned by role, with SLA by severity
- [ ] Queue health metrics (inflow, close rate, aging) are specified
- [ ] Escape policy for launch known-issues is documented

## What it contains

- Triage meeting cadence and chair
- Severity rubric and escalation rules
- Decision rights (fix-now, defer, accept) by role
- SLA by severity
- Queue health metrics (inflow, close rate, aging)
- Escape policy — what goes to launch as known issue

## Inputs you rely on

- Test plan severity rubric
- Triaged UAT defects and regression results
- Triaged vulnerabilities
- Readiness assessment
- Change-control escalation policy

## Who consumes it

- QA/Tester and Developers — operate within the cadence
- Release Manager — uses queue health as a readiness signal
- Product Owner — aligns scope decisions with triage output
- Security & Compliance — routes vulnerabilities through a compatible rubric

## Common pitfalls

- No fixed chair or decision rights — triage drifts into re-argument
- Severity adjudicated by tenure rather than user impact
- SLA tracked but never enforced — queue ages out of control
- No accepted-known-issues register so launch decision lacks a real list

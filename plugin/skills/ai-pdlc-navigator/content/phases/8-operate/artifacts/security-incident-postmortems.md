# security incident postmortems

_Produced by: Security incident response_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

The post-incident write-ups for security events — detected abuse, attempted intrusion, data exposure, misconfiguration, insider misuse. Sister document to reliability postmortems, with tighter confidentiality handling and compliance-driven reporting.

## Why it matters for the Security & Compliance team

Security incidents carry regulatory clocks (breach notification windows), customer-contract obligations, and reputation risk. A disciplined postmortem forces structured learning, supports mandatory disclosures, and feeds the control-improvement backlog so the same class of event doesn't recur.

## Definition of Done

- [ ] Incident classification and affected data scope are recorded.
- [ ] Detection, containment, eradication, and recovery milestones are timestamped.
- [ ] Affected data subjects and regulators are identified.
- [ ] Notification obligations and their current status are documented.
- [ ] Failed or missing controls are named with remediation owners and deadlines.

## What it contains

- Incident classification and affected data scope
- Detection, containment, eradication, recovery timeline
- Data subjects and regulators affected (if any)
- Notification obligations and status
- Controls that failed or were missing
- Remediation actions with owners and deadlines

## Inputs you rely on

- IR plan & runbook
- Security monitoring alerts and SIEM evidence
- Threat model and control-to-test coverage map
- Legal/Privacy guidance on disclosure
- Forensic logs and chain-of-custody records

## Who consumes it

- Security leadership and CISO
- Legal and Privacy — disclosure and regulator communication
- Sponsor and board — material risk events
- Audit — evidence of mature response process

## Common pitfalls

- Missing the regulatory clock because legal wasn't looped in immediately
- Incomplete log preservation — forensic gaps
- Action items without owners or deadlines
- Circulating more widely than privilege allows; or so narrowly nobody learns

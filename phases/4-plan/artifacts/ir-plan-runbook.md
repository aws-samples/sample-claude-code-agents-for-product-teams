# IR plan & runbook

_Produced by: Incident response plan_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

The security incident response plan and its operational runbook — roles, severities, detection-to-containment steps, comms, legal and regulator notification paths, and evidence preservation. Written before you need it, rehearsed before launch.

## Why it matters for the Security & Compliance owner

Under an incident, clarity is scarce and minutes cost money and customers. Having a rehearsed plan is how you cap blast radius, meet breach-notification deadlines, preserve forensics, and keep the response from being invented in a war room.

## Definition of Done

- [ ] Severity taxonomy defines criteria for each level
- [ ] Roles and paging tree (incident commander, comms, legal, exec) are named
- [ ] Runbooks cover each incident class with step-by-step procedures
- [ ] Regulatory notification clocks and templates are captured
- [ ] Evidence-preservation and chain-of-custody guidance are documented
- [ ] Post-incident review and learning-loop procedure is defined

## What it contains

- Severity taxonomy and criteria for each level
- Roles and paging tree (incident commander, comms, legal, exec)
- Step-by-step runbooks per incident class (account takeover, data exposure, malware)
- Regulatory notification clocks and templates (GDPR, HIPAA, state breach laws)
- Evidence-preservation and chain-of-custody guidance
- Post-incident review and learning loop

## Inputs you rely on

- Threat model and applicable regulations
- Architecture document and data classification
- Security monitoring and SIEM capabilities
- SRE incident-management process (for shared tooling)
- Legal and comms partner commitments

## Who consumes it

- Security operators and on-call responders — follow the runbook live
- SRE — coordinates technical response and uses shared tooling
- Legal and Comms — trigger notification workflows
- Product Sponsor — owns external comms approval for Sev-1

## Common pitfalls

- Never rehearsed — first run is the real one
- Regulator clocks not codified, missed notification windows
- Runbooks live in a wiki no one can find at 3 a.m.
- Assuming the SRE incident process covers security — different evidence rules apply

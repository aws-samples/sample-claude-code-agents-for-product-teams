# architectural health report

_Produced by: Architectural health monitoring_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

The Architect's view of how the system is holding up under real load — NFR attainment, coupling and drift from intended architecture, hot spots, and emerging debt. The periodic architectural check-in on steady-state behavior.

## Why it matters for the Architect

Architecture goes to rot silently if nobody watches. This report is the mechanism by which you catch drift early, anchor conversations about architecture investment with Sponsor and PO, and feed the modernization plan with evidence rather than opinion.

## Definition of Done

- [ ] NFR attainment is reported with specific numbers for latency, availability, throughput, and cost.
- [ ] Drift from intended architectural patterns is identified with evidence.
- [ ] Coupling, fan-out, and dependency health are characterised per service.
- [ ] Hot spots and technical debt accumulation are named with supporting telemetry.
- [ ] Recommendations include rough sizing so prioritisation conversations can start.

## What it contains

- NFR attainment (latency, availability, throughput, cost)
- Architectural drift from intended patterns
- Coupling, fan-out, and dependency health
- Hot spots and technical debt accumulation
- Vendor and partner dependency status
- Recommendations with rough sizing

## Inputs you rely on

- Monitoring dashboards & alerts and SLIs
- Incident and RCA trend data
- Cost & capacity report
- Conformance findings from Build phase
- Updated ADRs

## Who consumes it

- Sponsor — input to operational performance review
- Architect — feeds architecture updates and modernization plan
- Developer and SRE — work queue for conformance fixes
- Iterate phase — inputs to updated architecture roadmap

## Common pitfalls

- Opinion-led without telemetry evidence
- Focus on elegance instead of NFRs customers actually feel
- No link between findings and a backlog of work
- Report produced but never used in prioritization discussions

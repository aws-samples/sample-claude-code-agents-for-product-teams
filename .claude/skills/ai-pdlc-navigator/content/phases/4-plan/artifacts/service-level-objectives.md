# service-level objectives

_Produced by: SLA / SLO definition_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** Product Owner

## What this is

The measurable reliability targets the service will commit to — SLIs (what you measure), SLOs (the target), error budgets (how much failure you tolerate), and any external SLA commitments that depend on them.

## Why it matters for the SRE

SLOs are the primary mechanism for trading velocity against reliability without arguing from anecdotes. Agreeing them in Plan — with the PO co-signing — gives you the error budget to govern launches, freeze risky changes, and justify reliability investment in the backlog.

## Definition of Done

- [ ] SLIs are defined per critical user journey
- [ ] Each SLI has an SLO target and time window
- [ ] Error budget and burn policy are specified
- [ ] External SLA commitments and margin to SLO are documented
- [ ] Measurement source (telemetry events per SLI) is named
- [ ] Reporting cadence and review cycle are defined

## What it contains

- SLI definitions per critical user journey (availability, latency, correctness, freshness)
- SLO targets per SLI with time windows
- Error budget and policy for what happens when it's burned
- External SLA commitments and margin between SLA and SLO
- Measurement source (which telemetry events power which SLI)
- Reporting cadence and review cycle

## Inputs you rely on

- KPI definitions and critical user journeys from the PO
- NFR document (perf, availability targets)
- Telemetry plan (ensures SLIs are measurable)
- Customer commitments from Sales & Marketing
- Historical production data if an existing service is being extended

## Who consumes it

- Developers — build to the latency and correctness targets
- Release Manager — consults error budget before permitting risky releases
- Product Owner — trades features against reliability work using the budget
- Architect — validates that the architecture can actually deliver the targets

## Common pitfalls

- Aspirational SLOs with no path from telemetry to measurement
- Setting SLO = SLA (no margin, every incident is a customer breach)
- Too many SLIs per journey — nothing is prioritized, nothing is trusted
- Defining SLOs once and never reviewing them against actual production reality

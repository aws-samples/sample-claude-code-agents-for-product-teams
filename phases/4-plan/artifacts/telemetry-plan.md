# telemetry plan

_Produced by: Analytics & telemetry instrumentation planning_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — the MVP cannot be evaluated without telemetry

## What this is

The design for what the product will emit — events, metrics, logs, traces — so you can answer product, operational, and business questions after launch. It names the events, their schemas, the systems that ingest them, and who consumes each stream.

## Why it matters for the Architect

The KPIs, SLOs, and benefits measurement committed upstream are worthless without signal. Telemetry is a first-class design concern; specifying it during Plan prevents the Build-phase pattern of "we'll add metrics later" that leaves you blind at launch and forces expensive instrumentation retrofits.

## Definition of Done

- [ ] Event catalog lists names, properties, and semantic definitions
- [ ] Events are mapped to consumers (KPI dashboard, SLO alerts, billing, analytics)
- [ ] Sampling rates, retention, and PII handling are specified per stream
- [ ] Trace propagation and correlation ID strategy are documented
- [ ] Ingestion architecture (collectors, pipelines, sinks) is described
- [ ] Cost estimate and growth model are captured

## What it contains

- Event catalog with names, properties, and semantic definitions
- Mapping of events to consumers (KPI dashboard, SLO alerts, billing, product analytics)
- Sampling rates, retention, and PII handling per stream
- Trace propagation and correlation ID strategy
- Ingestion architecture (collectors, pipelines, sinks)
- Cost estimate and growth model

## Inputs you rely on

- KPI definitions and SLOs
- Data model and privacy impact assessment (for PII/classification)
- Integration map (where events cross service boundaries)
- Security & compliance requirements on logging
- Product questions stakeholders expect to answer post-launch

## Who consumes it

- Developers — implement instrumentation per the catalog during Build
- SRE — wires the ingestion and alerting off these streams
- Business Analyst — maps KPI definitions to event sources for dashboards
- QA/Tester — verifies emission in the verify phase against this spec

## Common pitfalls

- Logging everything "just in case" — cost explodes and signal drowns in noise
- Inventing event names ad-hoc during Build so the same concept has three schemas
- Forgetting PII/classification rules and landing regulated data in analytics stores
- No plan for derived metrics — raw events exist but no one builds the dashboards

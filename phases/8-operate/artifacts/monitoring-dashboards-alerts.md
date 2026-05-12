# monitoring dashboards & alerts

_Produced by: Application monitoring_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — you don't get to skip "is it up"

## What this is

The dashboards and paging rules SRE maintains to observe production — SLI dashboards per service, error-budget burn views, saturation and cost views, and the alerts that actually wake someone up. Curated, not generated.

## Why it matters for the SRE

Everything else — SLO attainment, incident response, on-call load, error-budget negotiation — rides on having signals that are accurate, actionable, and trusted. A clean observability surface keeps on-call humane; a noisy one erodes response quality and leaks into customer impact.

## Definition of Done

- [ ] Every service has SLI dashboards covering latency, availability, saturation, and correctness.
- [ ] Error-budget burn-rate views are present and tied to SLO targets.
- [ ] Each alert rule has severity, routing, and a linked runbook.
- [ ] Dependency and partner health panels cover the external services named in the architecture.
- [ ] Quiet-hours, dedup, and escalation policies are documented.

## What it contains

- SLI dashboards (latency, availability, saturation, correctness) per service
- Error-budget burn-rate views
- Golden-signal RED/USE dashboards
- Alert rules with severity, routing, and runbook links
- Dependency and partner health panels
- Quiet hours, dedup, and escalation policy

## Inputs you rely on

- Service-level objectives and NFRs
- Telemetry plan and instrumented code
- Incident history and postmortems (what should have paged sooner)
- Architecture document and integration map
- Cost & capacity targets

## Who consumes it

- On-call engineers — respond to alerts, investigate incidents
- Product Owner and Sponsor — input to operational performance review
- Architect — feeds architectural health and scale-readiness reports
- Support — triage customer reports against current system state

## Common pitfalls

- Alert fatigue from page-on-everything rules
- Alerts without runbooks — on-call improvises at 3am
- Dashboards that disagree between teams because SLIs aren't shared definitions
- Dependency blind spots (CDN, auth, payment provider)

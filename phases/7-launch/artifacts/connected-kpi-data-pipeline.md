# connected KPI data pipeline

_Produced by: Wire KPI events into dashboard_

**Business outcome supported:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** Developer

**Accelerated MVP:** required — the dashboard has to be fed

## What this is

The live data path from product instrumentation into the KPI dashboard — event emission, ingestion, transformation, and rendering. Proven end-to-end with real production events, not mocks.

## Why it matters for the SRE

Dashboards that lag, drop events, or double-count erode executive trust in every metric that follows. As SRE, you own the reliability and cost of this pipeline; you need the same SLIs on it (freshness, completeness, latency) that you demand from the product itself.

## Definition of Done

- [ ] Event schema and contract are defined for every KPI the pipeline delivers.
- [ ] Pipeline topology documents each ingestion and transformation stage end-to-end.
- [ ] Freshness, completeness, and latency SLIs are stated with target values.
- [ ] Backfill and replay procedures are documented and runnable.
- [ ] Access controls on raw and aggregated data are specified.

## What it contains

- Event schema and contracts per KPI
- Ingestion and transformation pipeline topology
- Freshness, completeness, and latency SLIs for the pipeline
- Backfill and replay procedures
- Access controls on raw and aggregated data
- Cost footprint and scaling posture

## Inputs you rely on

- KPI definitions and verified KPI telemetry from Verify
- Telemetry plan and instrumentation code
- Monitoring dashboards & alerts for pipeline observability
- Data inventory & classification (PII handling)
- Data model and storage architecture

## Who consumes it

- Business Analyst — trusts the dashboard as source for benefits tracking
- Product Sponsor — live launch KPI dashboard for board and operate reviews
- Product Owner — in-flight calibration on adoption and activation
- Finance and RevOps — reconcile commercial metrics

## Common pitfalls

- Dashboard counts that disagree with source tables — provenance lost
- No monitoring on the pipeline itself; staleness goes undetected
- PII in raw events without classification controls
- Missing backfill path — any outage becomes a permanent data hole

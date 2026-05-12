# cost & capacity report

_Produced by: Cost / capacity monitoring_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** Architect

**Accelerated MVP:** slim — a weekly glance at the cloud bill is enough

## What this is

Joint SRE/Architect view of what the product costs to run and how close it is to capacity ceilings — spend by service, unit-cost trend, headroom at current growth, and optimization opportunities. Produced on an operating cadence.

## Why it matters for the SRE

Reliability has a price; understanding what you spend and why lets you trade off intelligently instead of reactively. As SRE you are on the hook for both uptime and cost; this report turns "our bill is going up" into specific, owned work.

## Definition of Done

- [ ] Spend is broken down by service, environment, and cost type.
- [ ] Unit-cost trend is reported against at least one KPI (e.g. cost per user or per transaction).
- [ ] Capacity headroom is stated at both current and projected growth.
- [ ] Top drivers of cost increase are named with supporting data.
- [ ] Optimization candidates list estimated savings and an owner.

## What it contains

- Spend by service, environment, and cost type (compute, storage, egress, licensing)
- Unit-cost trend per KPI (cost per active user, per transaction)
- Capacity headroom at current and projected growth
- Top drivers of cost increase
- Optimization candidates with estimated savings
- Commit/reserved-instance posture and renewal timing

## Inputs you rely on

- Monitoring dashboards & alerts (utilization data)
- Architecture document and integration map
- Business case unit-cost assumptions
- Vendor and cloud billing data
- Capacity test and scale-readiness inputs

## Who consumes it

- Architect — targets architecture updates and modernization plan
- Sponsor and Finance — margin and CAC/LTV report inputs
- Product Owner — prioritizes cost-reducing product changes
- Iterate phase — inputs to profitability assessment vs. business case

## Common pitfalls

- Cost without unit-cost framing — looks scary but hides efficiency gains
- Missing egress, licensing, or third-party APIs
- No forecast; report shows yesterday's spend instead of next quarter's risk
- Savings opportunities without owners — they never materialize

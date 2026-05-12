# operational performance review

_Produced by: Review operational KPIs & SLO performance_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Product Sponsor

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the MVP is reviewed inside the squad cadence

## What this is

The Sponsor's periodic review of how the product is actually performing in production — SLO attainment, error-budget burn, incident trends, cost trajectory, and reliability health — rolled up to a level that supports portfolio decisions.

## Why it matters for the Product Sponsor

You own the outcomes, not the pager. This review is the place where operating health either stays green enough to keep investing, or becomes loud enough to re-prioritize spend away from new features toward reliability, cost, or architecture work.

## Definition of Done

- [ ] SLO attainment is reported by service with error-budget status.
- [ ] Incident count, severity mix, and MTTR trend are shown.
- [ ] Cost and capacity trajectory is compared to plan.
- [ ] Top reliability risks include current remediation status.
- [ ] Decisions required from the Sponsor are explicitly listed.

## What it contains

- SLO attainment by service and error-budget status
- Incident count, severity mix, and MTTR trend
- Cost and capacity trajectory vs. plan
- Top reliability risks and remediation status
- Cross-dependency health (vendors, partners)
- Decisions required from the Sponsor

## Inputs you rely on

- Monitoring dashboards & alerts from SRE
- Incident postmortems and root cause analyses
- Cost & capacity report
- Architectural health report
- Approved incident comms log (for customer-visible events)

## Who consumes it

- Sponsor and exec peers — resource and prioritization calls
- SRE and Architect — mandate for reliability or architecture work
- Product Owner — reconcile roadmap against reliability debt
- Finance — cost trajectory and commit planning

## Common pitfalls

- Drowning in metrics instead of surfacing decisions
- Reporting SLO attainment without showing error-budget trajectory
- Ignoring vendor and partner incidents that contributed to downtime
- No standing decisions list — review becomes a data-read, not governance

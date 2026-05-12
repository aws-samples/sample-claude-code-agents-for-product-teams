# scale-readiness report

_Produced by: Capacity & scale architecture review_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the MVP isn't near scale

## What this is

The forward-looking architectural analysis of whether the system will hold up at projected customer, traffic, and data growth — with specific ceilings, bottlenecks, and investments required before they bite.

## Why it matters for the Architect

By the time you're firefighting a scale wall, it is already hurting customers and margin. Scale readiness is how you translate "we expect 3x growth next year" into a funded plan for sharding, caching, regionalization, or platform swaps — before the customer-facing incident.

## Definition of Done

- [ ] Growth is projected for customers, RPS, and data volume.
- [ ] Current and projected saturation are stated per tier.
- [ ] Each identified bottleneck has a ceiling and timing estimate.
- [ ] Options analysis includes cost/benefit, not just options.
- [ ] Recommended investments are sequenced and paired with risk-of-inaction.

## What it contains

- Projected growth curves (customers, RPS, data volume)
- Current and projected saturation per tier
- Identified bottlenecks and their ceilings
- Options analysis with cost/benefit
- Recommended investments, sequenced
- Risk of inaction

## Inputs you rely on

- Cost & capacity report
- Architectural health report
- Performance test report and resilience test results
- Pipeline and forecast inputs from Sales & Finance
- Vendor and cloud capacity constraints

## Who consumes it

- Sponsor — investment decisions on scale work
- SRE — aligns capacity planning
- Developer — picks up scale-related work
- Iterate phase — feeds modernization plan

## Common pitfalls

- Linear projections over non-linear systems
- Confidence in benchmarks run on unrealistic data shapes
- Missing non-technical scale limits (support, billing, licensing)
- Report describes problems without sequenced, funded recommendations

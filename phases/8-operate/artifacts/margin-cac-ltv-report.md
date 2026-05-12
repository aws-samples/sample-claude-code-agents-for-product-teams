# margin & CAC/LTV report

_Produced by: Unit-economics / margin review_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Product Sponsor

**Stakeholders:** Business Analyst, Architect

**Accelerated MVP:** optional when the MVP isn't monetized

## What this is

Unit economics for the product — gross margin, cost of goods sold composition, customer acquisition cost, lifetime value, and payback period — measured and compared to the assumptions baked into the original business case.

## Why it matters for the Product Sponsor

Revenue without margin is a treadmill. This report tells you whether scale actually makes the product more profitable or just more expensive. It is where infrastructure cost, support cost, and GTM efficiency converge into one portfolio decision-ready view.

## Definition of Done

- [ ] Gross margin is broken down by plan and segment.
- [ ] COGS is decomposed across infra, support, licensing, and payment processing.
- [ ] CAC is shown by channel with a trend; LTV and payback period are calculated.
- [ ] Variance is measured against the original business-case assumptions.
- [ ] Top margin-improvement levers each have a named owner.

## What it contains

- Gross margin by plan and segment
- COGS decomposition (infra, support, licensing, payment processing)
- CAC by channel with trend
- LTV and payback period
- Variance vs. business case assumptions
- Top margin-improvement levers and their owners

## Inputs you rely on

- Revenue report and renewal & expansion bookings
- Cost & capacity report (infra COGS)
- Customer Support ticket cost and triaged ticket dataset
- Sales & Marketing spend (CAC)
- Architectural health and scale-readiness inputs

## Who consumes it

- Sponsor and CFO — profitability and investment posture
- Architect — targets architecture/cost work that moves the needle
- Business Analyst — inputs to profitability assessment in Iterate
- Product Owner — prioritizes features that improve margin

## Common pitfalls

- CAC that excludes internal headcount cost — understates reality
- LTV that assumes current retention with no sensitivity analysis
- Infra cost not tagged to product, so COGS is a plug number
- No link from levers to owners — report reads but nothing changes

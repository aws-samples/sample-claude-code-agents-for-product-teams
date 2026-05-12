# ROI technical inputs

_Produced by: Technical cost & feasibility inputs_

**Business outcome supported:** frame the opportunity, validate the problem, understand the market, and exit with a funded, strategically-aligned bet.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when there is no formal ROI model

## What this is

The technical cost side of the ROI: rough-order-of-magnitude build effort, run cost, integration cost, and the cost of the non-functional commitments implied by the opportunity. This is what keeps the [ROI model](roi-model.md) honest on the cost side.

## Why it matters for the Architect

You own this because business-side estimators will otherwise assume build is cheap and run is free. Providing a grounded range early prevents the "we approved $2M and it will cost $6M" conversation in Build, and flags unaffordable NFRs before they get promised.

## Definition of Done

- [ ] T-shirt build effort lists major cost drivers, not just a total.
- [ ] Run-cost model covers infrastructure, licenses, SRE, on-call, and compliance.
- [ ] Integration cost is estimated against named upstream/downstream systems.
- [ ] NFR-driven costs (availability, residency, recovery, scale) are called out.
- [ ] Technical risks that could move the number by >30% are listed.

## What it contains

- T-shirt build effort and major cost drivers
- Run-cost model: infrastructure, licenses, SRE, on-call, compliance
- Integration cost with named upstream/downstream systems
- NFR-driven cost (availability, data residency, recovery, scale)
- Build-vs-buy candidates and their indicative pricing
- Key technical risks that could move the number by >30%

## Inputs you rely on

- [Opportunity brief](opportunity-brief.md) and early scope shape
- [Feasibility memo](feasibility-memo.md) for the constraint landscape
- Platform team rate cards and current infra unit economics
- Vendor quotes or public pricing for likely buy candidates

## Who consumes it

- Business Analyst — plugs cost lines into the [ROI model](roi-model.md) and [business case](business-case.md)
- Product Sponsor — tests affordability against portfolio budget
- Architect (future you) — refines these numbers through [technical feasibility findings](../../2-define/artifacts/technical-feasibility-findings.md) and the design-era [updated ROI model](../../3-design/artifacts/updated-roi-model.md)

## Common pitfalls

- Engineer-hours only — missing run cost, compliance cost, and enablement cost
- Anchoring on the happy-path architecture and ignoring NFR-driven cost
- No range — ROM without bounds is treated as a commitment later
- Forgetting the "current platform cannot support this" case where the cost includes platform uplift

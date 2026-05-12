# feasibility memo

_Produced by: Early feasibility / risk assessment_

**Business outcome supported:** frame the opportunity, validate the problem, understand the market, and exit with a funded, strategically-aligned bet.

**Primary owner:** Product Owner

**Stakeholders:** Architect, Product Sponsor

**Accelerated MVP:** slim — named unknowns and planned spikes are enough; full memo comes before scaling

## What this is

A short, honest read on whether the initiative is technically, operationally, legally, and commercially feasible before anyone commits serious money. It surfaces the "we cannot do this because…" constraints while they can still reshape scope cheaply.

## Why it matters for the Product Owner

You produce this so the Sponsor is not asked to fund an initiative that the Architect already knows will collide with a data-residency rule or a capacity constraint. An early red flag here is worth ten late change requests.

## Definition of Done

- [ ] Memo covers at least three feasibility dimensions (technical, operational, regulatory, commercial, or data).
- [ ] Each dimension carries a red/amber/green rating with supporting evidence.
- [ ] Known blockers include the conditions that would make them go-possible.
- [ ] At least one alternative (do-nothing, buy, partner, partial scope) is considered.
- [ ] Memo recommends next investigations to retire the biggest amber/red items.

## What it contains

- Top 3–5 feasibility dimensions: technical, operational, regulatory, commercial, data
- Known blockers and the conditions under which they become go-possible
- Alternatives considered (do-nothing, buy, partner, partial scope)
- Red/amber/green rating per dimension with evidence
- Recommended next Discover investigations to retire the biggest amber/red items

## Inputs you rely on

- Architect's early read on fit with current platform and patterns
- [ROI technical inputs](roi-technical-inputs.md) for cost-side constraints
- [Regulatory risk flag](regulatory-risk-flag.md) and [data-sensitivity flag](data-sensitivity-flag.md)
- Sponsor's portfolio view (is this a bet the org has appetite for?)

## Who consumes it

- Product Sponsor — uses it to decide go / no-go / defer on further discovery spend
- Architect — carries amber items into Define's technical feasibility findings
- Business Analyst — drafts problem validation to specifically retire the risks flagged here

## Common pitfalls

- Overconfident greens because no one wants to kill the idea early
- Missing the operational lane (support, ops, enablement cost) and only scoring build
- No retirement plan for amber items — they carry silently into Define as surprises
- Treating it as a one-time assessment instead of revisiting at each gate

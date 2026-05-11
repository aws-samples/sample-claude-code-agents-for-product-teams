# updated ROI model

_Produced by: Refine cost-benefit model with design-era data_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

## What this is

The Discover-era [ROI model](../../1-discover/artifacts/roi-model.md) refreshed with design-era evidence: more accurate build cost, real run-cost shape, vendor pricing, adoption-curve updates, and the current scope baseline. It is the financial model the organization re-ratifies before committing to Build.

## Why it matters for the Business Analyst

You refresh this because early models are approximations and Design is the first time the real numbers show up. An updated model keeps the business case honest and gives the Sponsor a defensible basis for the [validated business-value alignment](validated-business-value-alignment.md) decision.

## Definition of Done

- [ ] Build cost is refreshed with design-era effort estimates.
- [ ] Run-cost model reflects the chosen architecture decisions.
- [ ] Vendor and licensing costs use negotiated (not list) pricing where known.
- [ ] Sensitivity tornado is re-run against the updated inputs.
- [ ] Delta vs. the approved business case is stated with rationale.

## What it contains

- Refined build cost from [effort estimates](../../2-define/artifacts/effort-estimates.md) plus design-era adjustments
- Run-cost model informed by architecture decisions
- Vendor and licensing costs from selected options
- Adoption-curve refinement based on usability findings and segment confidence
- Updated sensitivity tornado
- Delta vs. approved business case with rationale
- Reforecast NPV, payback, break-even

## Inputs you rely on

- [ROI model](../../1-discover/artifacts/roi-model.md) and [approved business case](../../2-define/outcomes/approved-business-case.md)
- [Architecture document](architecture-document.md) and [vendor evaluation scorecard](vendor-evaluation-scorecard.md)
- [Effort estimates](../../2-define/artifacts/effort-estimates.md) plus design-era refinements
- [Usability findings](usability-findings.md) for adoption-confidence updates

## Who consumes it

- Product Sponsor — decides continue / resize / re-baseline at [validated business-value alignment](validated-business-value-alignment.md)
- Finance — reconfirms treatment and depreciation
- Product Owner — uses deltas to defend scope choices
- Business Analyst (future you) — evolves it through Build and Iterate

## Common pitfalls

- Only updating the cost side when benefits also need adjusting
- No delta narrative — Sponsor cannot see what changed and why
- Vendor pricing treated as list, ignoring negotiated reality
- Sensitivity not re-run after inputs change

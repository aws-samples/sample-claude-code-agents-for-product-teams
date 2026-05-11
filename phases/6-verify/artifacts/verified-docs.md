# verified docs

_Produced by: Documentation review_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Technical Writer

**Stakeholders:** QA/Tester

## What this is

Technical documentation — user guides, reference, tutorials, release notes drafts, support playbooks, in-product copy — reviewed for accuracy against the as-built product and proven by walking through each flow. Not style review; correctness review.

## Why it matters for the Technical Writer

Docs that don't match the product drive support tickets and destroy trust on first contact. Verifying against the real build in the Verify phase is how you ship docs that reduce time-to-value and deflect load from Customer Support rather than amplifying it.

## Definition of Done

- [ ] Doc inventory lists review status per piece
- [ ] Walk-through evidence (screenshots, steps, observed results) is attached
- [ ] Defects found (incorrect UI text, broken flows, stale references) are listed
- [ ] In-product copy and error-message review outcomes are recorded
- [ ] Localization status is recorded where applicable, with remediation list and owner per defect

## What it contains

- Doc inventory with review status per piece
- Walk-through evidence (screenshots, steps, observed results)
- Defects found (incorrect UI text, broken flows, stale references)
- In-product copy and error-message review
- Localization status where applicable
- Remediation list and owner per defect

## Inputs you rely on

- Feature documentation and user guides drafts
- Generated API docs
- Design specification for UI-copy alignment
- Validated staging environment
- Release notes draft

## Who consumes it

- Launch-readiness assessment — docs readiness is a dimension
- Customer Support — consumes verified docs into the KB
- Sales & Marketing — uses accurate docs in collateral and demos
- Developers — fix product defects that docs surface

## Common pitfalls

- Docs reviewed in isolation from the product — they read well and don't match
- In-product copy missed entirely because it lives in code
- Only the happy path verified; error flows not walked
- Localization lags and ships stale on launch day

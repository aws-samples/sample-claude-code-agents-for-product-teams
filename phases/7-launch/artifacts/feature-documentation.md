# feature documentation

_Produced by: Create feature documentation_

**Business outcome supported:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

**Primary owner:** Technical Writer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — what it does and how to use it, in one place

## What this is

Reference-style documentation for each capability that is launching — what it does, how it is configured, constraints, permissions, and examples. Indexed for search and linked from in-product help.

## Why it matters for the Technical Writer

Your time-to-value target is "user solves their problem without filing a ticket." Feature docs are the artifact that keeps support load in check as the activation funnel scales; if they are missing or wrong at GA, the cost shows up immediately in support volume and churn.

## Definition of Done

- [ ] Every launching feature has its own page covering purpose, prerequisites, and outcomes.
- [ ] Setup and configuration steps include screenshots or code samples per page.
- [ ] Permissions and role requirements are stated on every page.
- [ ] Limits, quotas, and edge-case behavior are documented for each feature.
- [ ] Worked examples and common recipes appear on each feature page.

## What it contains

- One page per feature with purpose, prerequisites, and outcomes
- Setup and configuration steps with screenshots or code
- Permissions and role requirements
- Limits, quotas, and edge-case behavior
- Worked examples and common recipes
- Version applicability and changelog references

## Inputs you rely on

- Design specification and API specification
- Generated API docs and inline code documentation from Developer
- Approved design package and UI copy from UI/UX Designer
- Verified docs review outputs from Verify
- Known-issues list and workarounds

## Who consumes it

- End users and administrators — resolve their own tasks
- Customer Support — first-line reference when triaging tickets
- Sales Engineering — demoing and scoping customer deployments
- Partners and integrators — build against documented behavior

## Common pitfalls

- Documenting the UI instead of the user's job
- Drift from actual behavior because docs are written separately from code
- Missing permissions detail — the most common source of support escalations
- No working examples; users can't go from reference page to their own context

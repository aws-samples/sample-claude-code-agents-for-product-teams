# updated ADRs

_Produced by: Update architecture decision records_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

Architecture Decision Records — added, updated, or superseded during Build — capturing material decisions, the context that drove them, and the consequences accepted. Versioned with the code they govern.

## Why it matters for the Architect

Every non-trivial decision either gets documented or gets re-litigated every time someone new joins or the context changes. ADRs convert tribal knowledge into durable reasoning so future changes are informed, not archaeological.

## Definition of Done

- [ ] Each ADR carries a title, status, and date
- [ ] Context that made the decision necessary is documented
- [ ] Options considered and their trade-offs are listed
- [ ] Chosen option states both positive and negative consequences
- [ ] Author and approvers are named

## What it contains

- Decision title, status (proposed, accepted, superseded), and date
- Context that made the decision necessary
- Options considered and trade-offs
- Chosen option and consequences (positive and negative)
- Related ADRs and superseded-by links
- Author and approvers

## Inputs you rely on

- Design guidance sessions and conformance findings
- Technical impact analyses
- Architecture document and integration map
- Test and production feedback that invalidates a prior decision
- Decision log from design reviews

## Who consumes it

- Developers — consult before making aligned decisions
- Architect peers — review and carry decisions across teams
- Product Owner — sees technical trade-offs that affect timeline or capability
- Future engineers — inherit the reasoning, not just the code

## Common pitfalls

- ADRs written after the fact, rationalizing decisions instead of documenting them
- Too short — missing context or trade-offs, unusable a year later
- Status never updated — "accepted" ADRs linger after being silently replaced
- Hidden in a team-local wiki disconnected from the codebase

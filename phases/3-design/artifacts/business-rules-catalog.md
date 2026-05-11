# business-rules catalog

_Produced by: Business rules documentation_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

## What this is

The catalog of business rules the product enforces — eligibility, pricing, calculation, routing, compliance — each identified, defined, owned, and versioned independently of the code that implements them. Rules are not requirements; they are the policy the code obeys.

## Why it matters for the Business Analyst

You own this because rules change more often than requirements do, and change by different people (Finance, Legal, Ops) than own requirements. Separating rules from code means the business can update them without a release, and the team can show auditors exactly what the rule was on a given date.

## Definition of Done

- [ ] Each rule has a unique ID, plain-language statement, and precise formulation.
- [ ] Each rule cites its source (law, contract, policy, pricing plan).
- [ ] Each rule has a named owner and change-approval path.
- [ ] Effective dates and version history are recorded per rule.
- [ ] Each rule has positive, negative, and boundary test cases.

## What it contains

- Rule ID, name, and plain-language statement
- Precise formulation (table, formula, or decision logic)
- Source (law, contract, policy, pricing plan) with reference
- Rule owner and change-approval path
- Effective dates and version history
- Dependencies on data elements and other rules
- Test cases covering positive, negative, and boundary

## Inputs you rely on

- [Requirements document](../../2-define/artifacts/requirements-document.md) for where rules fire
- [Process models](../../2-define/artifacts/process-models.md) for context
- [Applicable-regulations list](../../2-define/artifacts/applicable-regulations-list.md) for regulatory rules
- Legal, Finance, or Ops owners who set each rule

## Who consumes it

- Developer — implements rules in a maintainable way (ideally as data, not code)
- QA/Tester — derives boundary and negative tests
- Business Analyst (future you) — updates rules during Operate without reopening requirements
- Customer Support — consults when explaining outcomes to customers

## Common pitfalls

- Rules embedded in code with no catalog, so change becomes an engineering ticket
- Missing rule owner, so rule change requests have nowhere to go
- No version history, so "why did this customer see X on April 3" becomes unanswerable
- Duplicate rules across services with no shared source of truth

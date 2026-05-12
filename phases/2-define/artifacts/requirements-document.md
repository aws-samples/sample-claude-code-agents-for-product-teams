# requirements document

_Produced by: Draft requirements_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — user stories or acceptance criteria in the backlog suffice

## What this is

The structured catalog of functional requirements for the initiative — each requirement uniquely identified, stated in outcome language, and tied back to a user job and a business benefit. This is the raw material every downstream team will consume.

## Why it matters for the Business Analyst

You own this because requirements quality is the single biggest lever on downstream delivery efficiency. Ambiguous, untraceable, or duplicated requirements burn Developer time, inflate QA scope, and make change impact analysis impossible; well-authored ones compound productivity across the whole lifecycle.

## Definition of Done

- [ ] Every requirement has a unique ID, title, and outcome-language statement
- [ ] Each requirement names an originating persona and job-to-be-done
- [ ] Each requirement carries a priority (MoSCoW or equivalent) and an MVP-inclusion flag
- [ ] Assumptions, dependencies, and constraints are captured per requirement
- [ ] Each requirement links to its acceptance criteria, relevant NFRs, and source evidence

## What it contains

- Unique ID, title, and statement for each requirement
- Originating persona and job-to-be-done
- Business rule or policy source if applicable
- Priority (MoSCoW or equivalent) and MVP-inclusion flag
- Assumptions, dependencies, and constraints
- Links to acceptance criteria, NFRs, and source evidence
- Version history and change rationale

## Inputs you rely on

- [MVP scope statement](mvp-scope-statement.md) for inclusion boundaries
- [Validated problem statement](../../1-discover/artifacts/validated-problem-statement.md) and [user personas](../../1-discover/artifacts/user-personas.md)
- [Process models](process-models.md) for behavior in context
- Stakeholder workshop outputs and prior discovery interviews

## Who consumes it

- Architect — derives design decisions and NFR responses
- Developer — estimates, implements, and references during code review
- QA/Tester — builds [test-to-requirement coverage map](test-to-requirement-coverage-map.md)
- Business Analyst (future you) — maintains the [traceability matrix](traceability-matrix.md) linking requirements → design → tests → benefits

## Common pitfalls

- Solution statements masquerading as requirements ("the system shall have a dropdown")
- Requirements with no uniquely addressable ID — you cannot trace what you cannot name
- Compound requirements that smuggle three things into one bullet
- Priorities set collaboratively with no tie-breaker, so everything ends up "must"

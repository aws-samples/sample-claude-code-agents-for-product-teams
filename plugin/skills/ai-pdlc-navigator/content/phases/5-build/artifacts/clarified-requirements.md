# clarified requirements

_Produced by: Requirements clarification support_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

## What this is

The ongoing answers to the requirements-questions-log — what the team asked during Build, how it was clarified, and how the underlying requirements or acceptance criteria changed as a result. Maintains the single source of truth even as nuance emerges.

## Why it matters for the Business Analyst

Requirements never survive first contact with implementation intact. Your value is keeping the written record honest — updating acceptance criteria, closing ambiguity, and preserving traceability — so the team builds against current truth and audit/regression questions later can be answered definitively.

## Definition of Done

- [ ] Each clarification records the date and asker
- [ ] Updated acceptance criteria or requirement text is captured
- [ ] Rationale names the approver for each decision
- [ ] Impact notes identify tests to update and stakeholders to notify
- [ ] Links connect the originating work item to the updated requirement

## What it contains

- Question-by-question clarifications with date and asker
- Updated acceptance criteria or requirement text
- Rationale for the decision and who approved it
- Impact notes (tests to update, stakeholders to notify)
- Links to the originating work item and the updated requirement
- Traceability matrix updates triggered

## Inputs you rely on

- Requirements questions log (from Developer/QA)
- Approved requirements and testable acceptance criteria
- Design specification and API specification
- Product Owner direction on priority trade-offs
- Stakeholder input where the change alters scope

## Who consumes it

- Developers and QA — build and test to the updated criteria
- Product Owner — confirms decisions and scope implications
- Traceability matrix maintenance for updated links
- Auditors — evidence of managed requirements change

## Common pitfalls

- Answers given in chat and never codified — org loses the decision record
- Acceptance criteria changed informally so tests and code diverge
- Clarifications that quietly expand scope without PO awareness
- No notification to downstream consumers (support, docs, security)

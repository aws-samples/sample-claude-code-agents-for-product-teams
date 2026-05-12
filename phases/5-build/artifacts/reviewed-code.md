# reviewed code

_Produced by: Code review_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** Security & Compliance

**Accelerated MVP:** required — every change gets a second pair of eyes

## What this is

Code that's been reviewed by a peer (and Security where risk warrants) against the team's review standard — correctness, maintainability, security, NFR conformance, test adequacy — with review comments resolved or explicitly deferred.

## Why it matters for the Developer

Reviews are the cheapest defect-finding technique and the main mechanism for spreading context across the team. Treating review seriously — both authoring reviewable PRs and giving substantive feedback — protects architectural intent and compounds the team's collective understanding of the code.

## Definition of Done

- [ ] Every review comment is resolved or carries a deferral rationale
- [ ] Required approvers for the change class are evidenced
- [ ] Security review outcome is present where risk or classification demands it
- [ ] Items intentionally out of scope link to follow-ups
- [ ] Merge decision records the approvers

## What it contains

- Review comments and their resolution or deferral rationale
- Evidence of required approvers by change class
- Security review outcome where required by risk/classification
- Test-coverage signals and any compensating approvals
- Linked follow-ups for things intentionally out of scope
- Merge decision with approver record

## Inputs you rely on

- Feature code and supporting tests
- Changelog review process and merge-gate rules
- Approved security patterns and conformance findings
- Architecture document and ADRs
- Lint/static-analysis report

## Who consumes it

- Author — integrates feedback and merges
- Security & Compliance — verifies sensitive changes met review requirements
- Architect — uses patterns to spot conformance issues
- Future engineers — review history as context when revisiting the code

## Common pitfalls

- Rubber-stamp reviews — approvals without real engagement
- Review as gatekeeping theater instead of teaching/learning
- Comments that nitpick style while missing substantive concerns
- Unresolved threads merged "we'll fix later" that never are

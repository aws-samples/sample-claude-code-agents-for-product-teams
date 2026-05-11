# implemented workitems

_Produced by: Review & code workitems_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** _(none listed)_

## What this is

Work items taken from the backlog through to code-complete — committed, reviewed, and satisfying their acceptance criteria. The daily output of Build, tracked at the item level rather than the code level.

## Why it matters for the Developer

Your job is to deliver work against a Definition of Done — not just to push commits. Maintaining accurate item state is how PO and PM can trust what's shippable, how QA plans their window, and how your velocity is measured fairly in retrospectives.

## Definition of Done

- [ ] Each closed item links to its commits, PRs, and tests
- [ ] Deviations from original acceptance criteria carry a rationale
- [ ] DoD checklist is completed per item
- [ ] Handoffs to QA, Tech Writer, or other roles are recorded where relevant
- [ ] Follow-up items spawned during implementation are captured as new items

## What it contains

- Items closed with links to associated commits, PRs, and tests
- Notes on deviations from original acceptance criteria and why
- DoD checklist completion per item
- Handoffs captured (e.g., to QA or Tech Writer) where relevant
- Open follow-up items spawned during implementation
- Metrics: cycle time, review latency, rework rate

## Inputs you rely on

- Delivery-ready work items and clarified requirements
- Design specifications and API specifications
- Automated test suite and test plan
- Reviewed code status
- Definition of Done

## Who consumes it

- QA/Tester — picks up items for verification
- Product Owner — accepts at iteration review
- Project Manager — rolls up into feature/epic status
- Release Manager — composes release content from closed items

## Common pitfalls

- Items closed before DoD is actually met — creates downstream surprises
- Partial implementations merged under a flag but not flagged in the item
- Missed follow-ups because they were never captured as new items
- No trace from item to commits — incident forensics later becomes archaeology

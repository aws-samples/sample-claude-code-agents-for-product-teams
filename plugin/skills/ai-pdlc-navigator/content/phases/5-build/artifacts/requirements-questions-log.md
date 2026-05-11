# requirements questions log

_Produced by: Raise requirements questions & impediments_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** QA/Tester

## What this is

The list of open questions raised by Devs and QA while implementing and testing — ambiguities, conflicts, edge cases, missing acceptance criteria — with who asked, when, who needs to answer, and the current state. The BA answers into clarified requirements.

## Why it matters for the Developer

Unanswered questions become guesses, and guesses become defects you ship. Logging questions explicitly rather than asking in chat is how you keep a PM-visible impediment list and force the organization to decide rather than defer.

## What it matters for the QA/Tester

Same pattern: testable criteria need unambiguous answers. Raising questions as artifacts ensures later regressions or audits can trace decisions back.

## Definition of Done

- [ ] Each entry records question, context, and blocking status
- [ ] Raised-by, raised-on, and target-responder are captured
- [ ] Current state is tagged open, in discussion, answered, or closed
- [ ] Each question links to the work item, design, or requirement in question
- [ ] Resolved entries point to the clarified-requirements entry

## What it contains

- Question, context, and blocking status
- Raised-by, raised-on, target-responder
- Current state (open, in discussion, answered, closed)
- Links to the work item, design, or requirement in question
- Interim assumption being used so work can continue (if any)
- Resolution and pointer to the clarified-requirements entry

## Inputs you rely on

- Testable acceptance criteria and delivery-ready work items
- Design specification and API specification
- Daily standups where questions surface
- Prior clarified-requirements decisions (often answer new questions)

## Who consumes it

- Business Analyst — works the queue and produces clarified requirements
- Product Owner — decides priority and scope trade-offs
- Project Manager — tracks aging as an impediment signal
- QA/Tester — reuses answers to refine test cases

## Common pitfalls

- Questions live in chat threads and die there — no durable record
- Interim assumptions used but never validated — ship with wrong behavior
- Aging questions not escalated — silent blocker on the work item
- Duplicates created because the log isn't searchable or curated

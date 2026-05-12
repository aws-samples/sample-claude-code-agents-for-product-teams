# MVP

_Produced by: MVP delivery_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** Product Owner

**Accelerated MVP:** required — this is the artifact the accelerated path delivers

## What this is

The first iteration of the product — a working, end-to-end slice that realizes the [MVP scope statement](../../2-define/artifacts/mvp-scope-statement.md) and acts as the starting point to evolve from. It is not a prototype and not a feature-complete release: it is the smallest coherent version that a real user can use and that the team can learn from.

The MVP is a composite artifact — it is assembled from [feature code](feature-code.md), [automated test suite](automated-test-suite.md), [instrumented code](instrumented-code.md), and related Build outputs — but it is tracked distinctly because "is the first iteration ready?" is a different question from "is each component ready?"

## Why it matters for the Developer

The MVP is where the team's first bet meets reality. Getting to a working first iteration quickly — rather than polishing parts in isolation — is what makes every later decision (what to evolve, what to drop, what to double down on) evidence-based instead of speculative. Treating the MVP as a first-class artifact keeps the team honest about integration risk and end-to-end usability, not just component-level progress.

## Definition of Done

- [ ] Every must-have from the [MVP scope statement](../../2-define/artifacts/mvp-scope-statement.md) is implemented end-to-end
- [ ] A real user can complete the core journey in a non-local environment without dev assistance
- [ ] Telemetry emits the signals the team needs to learn from first-iteration use
- [ ] Known limitations are documented so stakeholders can set expectations
- [ ] The MVP is tagged or versioned so later iterations can diff against it

## What it contains

- The composed set of [feature code](feature-code.md) that delivers the in-scope journeys
- Tests covering the core paths ([automated test suite](automated-test-suite.md), [integration test results](integration-test-results.md))
- Telemetry sufficient to evaluate the outcome hypothesis ([instrumented code](instrumented-code.md))
- A short "what's in, what's out, what's next" note for stakeholders
- A version tag marking this as the first iteration

## Inputs you rely on

- [MVP scope statement](../../2-define/artifacts/mvp-scope-statement.md) — the agreed boundary of this first iteration
- [outcome hypothesis](../../1-discover/artifacts/outcome-hypothesis.md) and [KPI definitions](../../2-define/artifacts/kpi-definitions.md) — what this iteration is meant to learn or move
- [build-ready package](../../3-design/artifacts/build-ready-package.md) and the Design artifacts it carries
- [prioritized backlog](../../4-plan/artifacts/prioritized-backlog.md) sequenced so the earliest items compose into an end-to-end slice

## Who consumes it

- Product Owner — accepts the first iteration and sequences what evolves next
- QA/Tester — validates end-to-end behavior under real-world conditions in [Verify](../../6-verify/README.md)
- UI/UX Designer — tests usability assumptions against actual use
- Business Analyst — compares observed behavior to the outcome hypothesis
- Sponsor — uses it to reconfirm or reset the business case

## Common pitfalls

- Scope creeping from "first iteration" into "feature-complete v1" — kills the feedback loop the MVP exists to create
- Shipping a technical demo rather than a real user journey — nothing to learn from because no one can actually use it
- Skipping telemetry in the rush to ship — produces an MVP no one can evaluate
- Treating the MVP as the destination rather than the starting line — the name is "Minimum Viable Product," not "Finished Product"
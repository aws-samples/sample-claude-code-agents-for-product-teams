# automated test suite

_Produced by: Develop tests_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** QA/Tester

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — the MVP's regression safety net

## What this is

The living, versioned collection of automated tests — unit, integration, contract, end-to-end, and specialist checks (a11y, perf smoke, resilience) — that runs in CI and produces the regression signal every PR relies on.

## Why it matters for the QA/Tester

Automation is how risk-based coverage becomes durable. You own that the suite matches the coverage strategy, stays fast enough to not be bypassed, and is trusted enough that a green run actually means something when Release reads it.

## Definition of Done

- [ ] Tests are organized by level and risk area
- [ ] Every test file or package has a named owner
- [ ] Flaky tests are identified and tracked in a quarantine process
- [ ] Runtime budgets are stated per suite and pipeline stage
- [ ] Acceptance criteria coverage is traceable via a test-to-requirement map

## What it contains

- Tests organized by level and risk area
- Ownership per test file or package
- Flakiness tracking and quarantine process
- Data fixtures and environment prerequisites
- Runtime budgets per suite and stage
- Coverage of acceptance criteria mapped via test-to-requirement map

## Inputs you rely on

- Test plan and testable acceptance criteria
- Feature code and API specification
- Design specification (for UI-level tests)
- Security test plan (SAST/DAST hooks into suite)
- Pipeline stages and runtime budgets

## Who consumes it

- Developers — get fast local and PR feedback
- Release Manager — uses green suite as a promotion gate
- Integration test results artifact aggregates its runs
- QA/Tester leads — monitor coverage and flakiness metrics

## Common pitfalls

- Flaky tests normalized as "just retry" — signal trust collapses
- Over-indexing on end-to-end tests — slow, brittle, and expensive
- Coverage measured by line but not by acceptance criterion
- Suite untouched while production moves — tests validate stale behavior

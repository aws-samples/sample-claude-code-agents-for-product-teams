# test plan

_Produced by: Test strategy_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** QA/Tester

**Stakeholders:** _(none listed)_

## What this is

The risk-based testing strategy for the initiative — what you'll test, at which levels, using which techniques, in which environments, with which entry/exit criteria. It's the operating contract between QA, engineering, and the rest of the team for how quality is built in and evidenced.

## Why it matters for the QA/Tester

"Test everything" is infeasible and "test whatever lands" produces escapes. The test plan forces you to name the risks that matter, the coverage needed to mitigate them, and the environments where that coverage is credible — so later when schedule gets tight, you're negotiating against a defined strategy rather than vibes.

## Definition of Done

- [ ] Scope, assumptions, and out-of-scope items are documented
- [ ] Risk-based coverage strategy differentiates exhaustive, sampled, and exploratory areas
- [ ] Test levels (unit, integration, contract, E2E, perf, a11y, sec) list ownership per level
- [ ] Environment needs, test data strategy, and refresh cadence are specified
- [ ] Entry/exit criteria are defined per test type and for the overall verify stage
- [ ] Automation strategy, tooling, and reporting approach are captured

## What it contains

- Scope, assumptions, and out-of-scope items
- Risk-based coverage strategy (what gets exhaustive vs. sampled vs. exploratory)
- Test levels (unit, integration, contract, E2E, perf, a11y, sec) and ownership per level
- Environment needs, test data strategy, and refresh cadence
- Entry/exit criteria for each test type and for the overall verify stage
- Automation strategy, tooling, and reporting

## Inputs you rely on

- Approved requirements and testable acceptance criteria
- NFR document and SLOs
- Architecture document and integration map
- Control-to-test coverage map from Security & Compliance
- Test-to-requirement coverage map and traceability matrix

## Who consumes it

- Developers — build automation and in-stream tests aligned to the plan
- Release Manager — uses exit criteria to gate promotion
- Security & Compliance — verifies control-test coverage matches requirements
- QA/Tester leads — plan campaigns against it during Build and Verify

## Common pitfalls

- Equal-weight coverage across all features — ignores actual risk
- No exit criteria so "done testing" is a vibe, not a bar
- Assuming staging matches prod — load/perf plans break at verify
- Treating the plan as static and ignoring scope or NFR changes during Build

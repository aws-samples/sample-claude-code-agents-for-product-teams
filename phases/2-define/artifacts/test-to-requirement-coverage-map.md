# test-to-requirement coverage map

_Produced by: Map test cases to requirements_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** QA/Tester

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when acceptance criteria are embedded in the tests themselves

## What this is

A matrix showing which test cases cover which requirements and acceptance criteria, with a coverage score. It is how QA shows the team exactly where confidence is earned and where risk still lives.

## Why it matters for the QA/Tester

You produce this so risk-based coverage is visible and defensible. It is the artifact you use to push back on "ship it" when critical requirements have no tests, and the artifact auditors use when asking "how do you know this works?"

## Definition of Done

- [ ] Every requirement ID and acceptance criterion ID appears in the map
- [ ] Each row lists covering test case IDs with test type
- [ ] Each row carries a coverage status (covered / partial / uncovered / exempt)
- [ ] Uncovered rows have a risk rating
- [ ] Environment and data requirements are stated per test

## What it contains

- Requirement ID and acceptance criterion ID
- Test case IDs covering each criterion
- Test type (unit, integration, E2E, exploratory, NFR, manual)
- Coverage status (covered / partial / uncovered / exempt)
- Risk rating per uncovered row
- Environment and data requirements for each test

## Inputs you rely on

- [Requirements document](requirements-document.md) and [testable acceptance criteria](testable-acceptance-criteria.md)
- [NFR document](nfr-document.md) for non-functional coverage
- [Control-to-test coverage map](control-to-test-coverage-map.md) to avoid duplication
- QA strategy and automation capability

## Who consumes it

- Business Analyst — feeds it into the [traceability matrix](traceability-matrix.md)
- Developer — uses it to catch missing tests before merge
- Release Manager — gates release on critical-path coverage
- QA/Tester (future you) — evolves it into Design-era [design-aligned test designs](../../3-design/artifacts/design-aligned-test-designs.md)

## Common pitfalls

- Coverage by count rather than by risk — 100% coverage of trivial cases and 0% of critical ones
- Automated coverage logged; exploratory not counted
- Static document that drifts as requirements change
- No "exempt with rationale" path, so everything looks either covered or a crisis

# design-aligned test designs

_Produced by: Update test designs against approved design_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** QA/Tester

**Stakeholders:** _(none listed)_

## What this is

Test designs that reflect the now-concrete architecture, APIs, data model, and UX — not just the abstract requirements. It is the Design-era evolution of the [test-to-requirement coverage map](../../2-define/artifacts/test-to-requirement-coverage-map.md) with enough specificity to automate and execute.

## Why it matters for the QA/Tester

You produce this so the Build-phase pipeline has tests ready from sprint one rather than trailing implementation. Design-aligned test designs are also how you catch design gaps — if a flow is hard to test, it is usually hard to operate.

## Definition of Done

- [ ] Test designs cover every flow, API, and NFR in the design package.
- [ ] Each test states its type (unit, integration, contract, E2E, performance, security, accessibility).
- [ ] Each test has an automation target (yes/no + tool) recorded.
- [ ] Coverage map links each test back to requirements, design, and controls.
- [ ] Exit criteria and pass/fail thresholds are named per test.

## What it contains

- Test designs per flow, API, and NFR
- Test types (unit, integration, contract, E2E, performance, security, accessibility)
- Test data requirements and test-environment needs
- Automation target per test (yes / no + tool)
- Coverage map to requirements, design, and controls
- Priority and risk rating
- Exit criteria and pass/fail thresholds

## Inputs you rely on

- [Design specification](design-specification.md), [API specification](api-specification.md), [data model](data-model.md)
- [Testable acceptance criteria](../../2-define/artifacts/testable-acceptance-criteria.md) and [NFR document](../../2-define/artifacts/nfr-document.md)
- [Control-to-test coverage map](../../2-define/artifacts/control-to-test-coverage-map.md) for security tests
- Existing automation frameworks and CI/CD capabilities

## Who consumes it

- Developer — pairs implementation and test work
- QA/Tester (future you) — executes and maintains through Build and Verify
- Architect — confirms testability of design decisions
- Release Manager — uses for release gating in Verify

## Common pitfalls

- Over-investing in E2E when contract and integration tests would catch more
- Test data plans deferred — environments then block execution
- No priority or risk rating, so coverage is uniform instead of risk-weighted
- Automation-only bias; missing exploratory and usability verification

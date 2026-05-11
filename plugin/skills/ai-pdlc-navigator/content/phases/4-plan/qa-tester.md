# QA/Tester in Plan

You are here to set the test strategy that Build and Verify execute against — risk-based, traceable, and honest about what automation can and can't catch. Plan is where you decide what gets tested, how, in what environment, and how you'll prove coverage traces back to requirements and security controls.

## What you do

- Author the test strategy — scope, approach, environments, tooling, automation boundary, entry/exit criteria.
- Contribute to the security test plan with Security & Compliance so threat-model-derived cases are covered.
- Align with Developers on how automated tests run in the CI/CD pipeline so integration testing is cheap from day one.
- Confirm traceability from requirements → acceptance criteria → tests is intact as decomposition happens.

## Artifacts you own

- [test plan](artifacts/test-plan.md) — the risk-based testing strategy for the initiative.

## Artifacts you contribute to

- [security test plan](artifacts/security-test-plan.md) — Security & Compliance owns; you integrate it into the overall test strategy.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Security & Compliance** — co-owns the security test plan; you integrate their cases into your overall strategy.
- **Business Analyst** — hands you testable acceptance criteria; you keep traceability intact.
- **Developer** — you agree on test harness, fixtures, and integration test boundaries in the pipeline.
- **Site Reliability Engineer** — you align on how tests run in the CI/CD pipeline and which environments you need.

## Handoff into [Build](../5-build/README.md)

In Build you become a producer — automated test suites, integration testing with Developers, and a live requirements questions log. You know Plan is done when the test plan is signed, the automation harness runs in the pipeline, and every acceptance criterion has a test mapped to it. In Verify you'll run the heavy artillery: UAT, performance, regression, accessibility.

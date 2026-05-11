# Developer in Build

Build is your phase. Everything upstream — vision, requirements, design, architecture, planning — was to get you to the point of writing working, tested, instrumented code that meets the Definition of Done. The pipeline runs, the patterns are set, the flags exist. Your job is to produce, review, merge, and instrument — fast, safely, and with traceability.

## What you do

- Review and code work items so backlog items become implemented software.
- Develop new features against the approved design and architecture.
- Review code with peers and Security & Compliance so no merge is a surprise.
- Merge code into main so integration stays continuous.
- Run static analysis / linting so style and obvious defects are caught pre-review.
- Implement telemetry per the plan so the product is observable from day one.
- Produce inline and API documentation as code — auto-generated where possible.
- Raise requirements questions and impediments with QA/Tester so ambiguity doesn't get coded in.
- Co-own integration testing with QA/Tester.
- Participate in security scanning triage with Security & Compliance.

## Artifacts you own

- [implemented workitems](artifacts/implemented-workitems.md)
- [feature code](artifacts/feature-code.md)
- [reviewed code](artifacts/reviewed-code.md) — co-owned with Security & Compliance.
- [merged code in main branch](artifacts/merged-code-in-main-branch.md)
- [lint/static-analysis report](artifacts/lint-static-analysis-report.md)
- [instrumented code](artifacts/instrumented-code.md)
- [generated API docs](artifacts/generated-api-docs.md)
- [requirements questions log](artifacts/requirements-questions-log.md) — co-owned with QA/Tester.

## Artifacts you contribute to

- [vulnerability scan report](artifacts/vulnerability-scan-report.md) — Security & Compliance owns; you triage and fix.
- [integration test results](artifacts/integration-test-results.md) — QA/Tester owns; you co-execute and fix.

## Outcomes you drive

You don't drive outcomes this phase — your code becomes the accepted increments the PO signs off.

## Who you work with

- **QA/Tester** — integration testing partner; your primary counterpart on quality.
- **Security & Compliance** — code review on security-sensitive changes; vulnerability triage.
- **Architect** — design guidance, conformance findings, pattern coaching.
- **Business Analyst** — answers requirements questions you raise.
- **UI/UX Designer** — answers design-spec clarifications.
- **Site Reliability Engineer** — keeps your pipeline fast and green.

## Handoff into [Verify](../6-verify/README.md)

In Verify you co-own data migration dress rehearsal with SRE, support UAT defect triage with QA, and help verify KPI telemetry with SRE. You know Build is done when code meets the Definition of Done, integration tests are green, no requirements question is open, and the instrumented feature is visible in staging telemetry.

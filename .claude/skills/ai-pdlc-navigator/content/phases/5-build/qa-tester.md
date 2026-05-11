# QA/Tester in Build

You are here to catch defects early and to build a trusted regression suite increment by increment. Build is where the test plan you authored in Plan becomes live automation, and where integration testing shifts from a concept to a habit. If Build is done right, Verify is validation; if it isn't, Verify becomes rescue.

## What you do

- Develop automated tests per the test plan — unit, integration, end-to-end where it pays for itself.
- Run integration testing with Developers continuously, not at the end.
- Keep traceability from acceptance criteria to test case to result intact.
- Raise requirements questions and impediments jointly with Developers so ambiguity gets resolved, not coded around.
- Prepare Verify-phase test scaffolding — performance harnesses, regression baselines, accessibility tooling.

## Artifacts you own

- [automated test suite](artifacts/automated-test-suite.md)
- [integration test results](artifacts/integration-test-results.md) — co-owned with Developer.

## Artifacts you contribute to

- [requirements questions log](artifacts/requirements-questions-log.md) — Developer owns; you co-raise and track.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'. Your test evidence underwrites the PO's increment acceptance.

## Who you work with

- **Developer** — primary counterpart; integration testing, requirements questions, test harness.
- **Business Analyst** — resolves requirements questions so acceptance criteria stay testable.
- **Security & Compliance** — aligns on what security testing lives in Build vs. Verify.
- **Site Reliability Engineer** — keeps your test infra stable in the pipeline.

## Handoff into [Verify](../6-verify/README.md)

Verify is your heavy phase — readiness assessment, UAT/beta sign-off, performance testing, accessibility testing, regression testing, defect triage. You know Build is done when integration is green, automation coverage maps cleanly to acceptance criteria, and your regression baseline is trusted enough to gate Verify.

# QA/Tester in Launch

Launch is where your test strategy meets production. You run post-deploy smoke tests with the Release Manager to prove the release is actually working for real users, and you stay in the hypercare loop to triage anything that slipped through Verify.

## What you do

- Execute post-deploy production smoke tests with the Release Manager to validate the release is healthy.
- Triage any launch-window defects for rapid fix-or-rollback decisions.
- Maintain quality signal through the launch window — what's regressing, what's holding.
- Document launch-phase findings for the Iterate bug backlog.

## Artifacts you own

You don't own any artifacts this phase — you contribute to others'.

## Artifacts you contribute to

- [production validation](artifacts/production-validation.md) — Release Manager owns; you execute and sign the smoke-test results.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Release Manager** — bi-directional on production validation and release health.
- **Developer** — bi-directional on rapid diagnosis and fix verification.
- **Site Reliability Engineer** — bi-directional on reliability signal and quality overlap.
- **Customer Support** — bi-directional on early customer-reported issues.

## Handoff into [Operate](../8-operate/README.md)

You exit Launch with a validated release and a starting baseline of production quality. Carry that into Iterate's bug-reporting discipline — real-user failures are your highest-leverage source of test-suite improvements, so capture reproduction details cleanly and prioritize coverage for what production actually breaks on.

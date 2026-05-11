# Site Reliability Engineer in Plan

You are here to turn "the team can start productively on day one" into reality. Plan is your heaviest phase — environments, pipeline, SLOs, and change-review processes all need to exist and work before the first feature commit. If these are wrong, everything downstream pays for it.

## What you do

- Provision infrastructure and environments so dev, test, staging, and prod (or equivalent) exist and are isolated.
- Stand up the CI/CD pipeline with Developers so build, test, scan, and deploy run on every commit.
- Define SLAs/SLOs jointly with the Product Owner so reliability is a product promise, not just an ops target.
- Set up the change-review process so every change hitting shared environments is reviewed before it lands.
- Contribute to the deployment runbook with the Release Manager so rollout and rollback are planned, not improvised.

## Artifacts you own

- [provisioned environments](artifacts/provisioned-environments.md) — dev/test/staging/prod ready.
- [working CI/CD pipeline](artifacts/working-ci-cd-pipeline.md) — co-owned with Developer.
- [service-level objectives](artifacts/service-level-objectives.md) — co-owned with Product Owner.
- [changelog review process](artifacts/changelog-review-process.md) — how changes get reviewed.

## Artifacts you contribute to

- [deployment runbook](artifacts/deployment-runbook.md) — Release Manager owns; you provide rollout/rollback mechanics.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Developer** — co-owns the CI/CD pipeline; they need it to go fast and fail loud.
- **Product Owner** — co-owns SLOs; they bring user expectation, you bring operational reality and cost.
- **Release Manager** — owns the deployment runbook you contribute to; you agree on progressive rollout mechanics.
- **Security & Compliance** — hands you pipeline security controls to wire in.
- **Architect** — provides telemetry plan and milestone sequence you operationalize.

## Handoff into [Build](../5-build/README.md)

In Build you become the guardian of the change stream — reviewing every incoming change against the changelog review process. You know Plan is done when engineers can open a PR and see it land in staging through the pipeline, SLOs are signed, and the change-review process is running with at least one dry-run change. In Verify you'll own chaos/resilience testing and PRR.

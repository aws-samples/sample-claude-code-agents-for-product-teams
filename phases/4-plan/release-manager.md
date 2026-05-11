# Release Manager in Plan

Plan is a lean phase for you — your real work picks up in Verify and Launch — but the deployment runbook you co-author here determines whether the team can actually ship what they're about to build. You're here to make sure rollout and rollback are designed decisions, not improvisation.

## What you do

- Co-author the deployment runbook with SRE — rollout sequence, health checks, rollback triggers, comms.
- Validate that the CI/CD pipeline supports the rollout pattern the runbook assumes (flags, canary, blue/green).
- Align with Security & Compliance on what evidence the release needs to carry.
- Begin scoping release-notes tooling and BOM generation you'll need in Launch.

## Artifacts you own

- [deployment runbook](artifacts/deployment-runbook.md) — co-owned with Site Reliability Engineer.

## Artifacts you contribute to

You don't contribute to other-owned artifacts this phase beyond the runbook.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — co-owns the runbook; they bring pipeline and environment mechanics, you bring release governance.
- **Security & Compliance** — tells you what evidence must accompany any release.
- **Architect** — confirms rollout pattern matches architectural assumptions (e.g., backward compat, migrations).

## Handoff into [Build](../5-build/README.md)

Build is another light phase for you — you observe and keep the runbook current as the system takes shape. Your real work lands in Verify (staging deploy, smoke tests, pipeline stabilization) and Launch (release execution, hypercare). You know Plan is done when the deployment runbook is drafted, reviewed with SRE and Security, and wired to the pipeline.

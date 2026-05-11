# Release Manager in Build

Build is a watching-and-refining phase for you. The deployment runbook you co-authored in Plan needs to stay current as the system takes shape — new services, new migrations, new dependencies all land. Your job is to keep the runbook live and rehearsed, and to start preparing for the Verify-phase staging deployments that will prove it.

## What you do

- Keep the deployment runbook current as services, migrations, and dependencies evolve.
- Observe CI/CD health with SRE so release mechanics you rely on are robust.
- Draft release notes scaffolding and BOM generation so Launch isn't scrambling.
- Coordinate with Security & Compliance on evidence requirements for each release stage.

## Artifacts you own

You don't own any artifacts this phase — you maintain the runbook you co-authored in Plan.

## Artifacts you contribute to

You don't formally contribute to a Build-phase artifact — your contribution is runbook currency and Launch-phase prep.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — keeps you informed of pipeline and environment changes that affect the runbook.
- **Security & Compliance** — confirms evidence requirements are being met.
- **Architect** — flags architectural shifts (e.g., new migration strategy) that change rollout assumptions.
- **Developer** — surfaces data migration needs that need runbook integration.

## Handoff into [Verify](../6-verify/README.md)

Verify is where your runbook gets rehearsed — staging deployment & smoke tests, pipeline stabilization, PRR co-sign-off. You know Build is done when the runbook is current, release-notes tooling works, and you're confident a staging deploy will reveal mechanics issues, not expose missing plans.

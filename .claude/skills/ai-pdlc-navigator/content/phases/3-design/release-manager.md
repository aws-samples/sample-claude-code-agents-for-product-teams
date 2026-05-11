# Release Manager in Design

You are still off-stage in Design but now the design decisions being made are concretely shaping what you will operate. Architecture, integrations, data model, and vendor choices all have release implications. Read widely; your Plan-phase deployment runbook will be drawn against what's approved here.

## What you do

- Read the [architecture document](artifacts/architecture-document.md), [integration map](artifacts/integration-map.md), and [build-ready package](artifacts/build-ready-package.md) — note release implications
- Track the [vendor partnership agreement](outcomes/vendor-partnership-agreement.md) and [build-vs-buy decision](outcomes/build-vs-buy-decision.md) — vendor-delivered components change your release shape
- Stay aligned with SRE on the emerging environment and pipeline shape you'll both operate

## Artifacts you own

You don't own any artifacts this phase — you contribute to others' (see below).

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — your primary counterpart heading into Plan; you co-own the deployment runbook there
- **Architect** — their architecture and integrations determine your release complexity
- **Product Sponsor** — their vendor decisions may add partners to your release cadence

## Handoff into Plan

In [Plan](../4-plan/README.md) you co-own the deployment runbook with SRE — the release plan for this initiative. Every Design decision is a release problem you'll inherit. The quality bar is that when Plan starts you can sketch the deployment, rollback, and release-cadence strategy for this architecture without reading for a week. You're done when the approved design package is architecturally familiar to you and you have a rough shape of the Plan-phase deployment runbook.

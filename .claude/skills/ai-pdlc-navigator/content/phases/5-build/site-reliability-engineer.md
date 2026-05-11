# Site Reliability Engineer in Build

Build is a quieter phase for you than Plan — the environments exist, the pipeline runs, the SLOs are defined. Your main job now is to keep the change stream clean: every change landing in shared environments gets reviewed, and the pipeline stays healthy so engineers never have to wait on infra to ship.

## What you do

- Review incoming changes against the changelog review process you set up in Plan.
- Keep the CI/CD pipeline healthy — fix flakes, tighten feedback loops, expand observability.
- Partner with Developers when telemetry implementation surfaces infra gaps.
- Prepare for Verify — chaos/resilience testing, PRR, KPI telemetry verification are coming.

## Artifacts you own

- [reviewed change log](artifacts/reviewed-change-log.md) — every change through the review gate.

## Artifacts you contribute to

You don't formally contribute to other Build-phase artifacts beyond the change-review process.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Developer** — you keep the pipeline healthy so they can ship; they flag infra gaps from telemetry work.
- **Security & Compliance** — their pipeline controls fire through your pipeline; you coordinate on false positives and tool health.
- **Release Manager** — keeps the runbook current against changes you're seeing land.
- **Architect** — you surface observability / capacity signals that might affect their status view.

## Handoff into [Verify](../6-verify/README.md)

In Verify you shift to producer mode — chaos/resilience testing, operational readiness review, KPI telemetry verification. You know Build is done when the change log is clean, the pipeline is green and fast, and you're confident the environments can take the Verify-phase load you're about to apply.

# Architect in Launch

Launch is where your pre-release engineering choices meet production traffic. You own the technical safety of rollback and keep eyes on architectural signals — latency tails, dependency behavior, capacity headroom — so the Release Manager and Sponsor can make continue/rollback calls on evidence, not vibes.

## What you do

- Sign off that the rollback path is architecturally safe — reversible schema changes, feature flags in known state, dependencies compatible either direction.
- Monitor architectural launch signals (latency, error budgets by dependency, capacity, data consistency) through the launch window.
- Advise the Release Manager and Sponsor on whether anomalies warrant rollback.
- Feed live architectural learnings into the updates you'll make in Operate.

## Artifacts you own

- [architectural launch signals](artifacts/architectural-launch-signals.md) — the live read on architectural health through the launch window.

## Artifacts you contribute to

You don't contribute to others' artifacts this phase.

## Outcomes you drive

- [rollback safety sign-off](outcomes/rollback-safety-sign-off.md) — your technical attestation that rollback is safe to exercise.

## Who you work with

- **Release Manager** — bi-directional on rollback safety and launch-window signals.
- **Site Reliability Engineer** — bi-directional on observability signal and capacity.
- **Developer** — bi-directional on rapid diagnosis of architectural anomalies.
- **Product Sponsor** — bi-directional when architectural signal influences the continue/rollback call.

## Handoff into [Operate](../8-operate/README.md)

You exit Launch with production-grounded insight the pre-launch environment couldn't give you. Channel that into architectural health monitoring, capacity/scale reviews, and architecture updates in Operate — the first weeks of live traffic are the richest source of signal you'll get for evolution decisions.

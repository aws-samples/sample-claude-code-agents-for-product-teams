# Site Reliability Engineer in Launch

Launch is where your SLOs, error budgets, and observability get their first real-world test. You wire live KPI telemetry into the dashboard, ride hypercare with the Release Manager, and make sure reliability signal is trustworthy from minute one of real traffic.

## What you do

- Wire KPI events into the launch dashboard with Developer so every signal is live and accurate from go-live.
- Co-own the hypercare war room with the Release Manager to stabilize the launch window.
- Watch SLI/SLO burn and capacity headroom through the launch window.
- Keep on-call rotations loaded and escalation paths hot for Sev-1/Sev-2 events.

## Artifacts you own

- [connected KPI data pipeline](artifacts/connected-kpi-data-pipeline.md) — the live pipeline powering the launch KPI dashboard, built with Developer.

## Artifacts you contribute to

You don't contribute to others' artifacts this phase.

## Outcomes you drive

- [stabilized launch window](outcomes/stabilized-launch-window.md) — Release Manager owns; you co-own the reliability side of hypercare.

## Who you work with

- **Release Manager** — bi-directional on hypercare, war-room posture, and rollback triggers.
- **Developer** — bi-directional on telemetry wiring and rapid fixes.
- **Architect** — bi-directional on architectural launch signals and capacity calls.
- **Security & Compliance** — bi-directional on any security telemetry anomalies.

## Handoff into [Operate](../8-operate/README.md)

You exit Launch with a stabilized service and live signal flowing. Carry that into Operate's monitoring dashboards, incident investigation cadence, DR testing, and cost/capacity monitoring — reliability is a continuous discipline, and Operate is where SLOs earn their keep against real demand.

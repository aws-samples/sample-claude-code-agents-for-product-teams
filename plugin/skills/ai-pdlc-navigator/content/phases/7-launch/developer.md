# Developer in Launch

Launch is where "operate what you build" gets real. You ship demo assets that let Sales and Support tell the story, wire KPI events into the live dashboard, and stay in the war room to fix fast when something breaks under real load.

## What you do

- Create sample data and demos so Sales and Support can show the product credibly on day one.
- Wire KPI events into the dashboard with the Site Reliability Engineer so telemetry is live and accurate.
- Stand by the hypercare war room for rapid diagnosis and fixes.
- Capture defects and anomalies encountered during launch for triage into Iterate.

## Artifacts you own

- [demo assets](artifacts/demo-assets.md) — the sample data and demo environments the field relies on.

## Artifacts you contribute to

- [connected KPI data pipeline](artifacts/connected-kpi-data-pipeline.md) — SRE owns; you implement the event emission side.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — bi-directional on KPI pipeline wiring and war-room response.
- **Sales & Marketing** — bi-directional on demo assets and field enablement.
- **QA/Tester** — bi-directional on production smoke tests and hypercare defect triage.
- **Architect** — bi-directional on architectural signal and rapid fix design.

## Handoff into [Operate](../8-operate/README.md)

You exit Launch with a stabilized product and live signal telling you what users actually do. Carry that into Operate's incident response, root-cause analysis, security patching, and bug-fix cycles — the operate-what-you-build loop starts the moment customers are real.

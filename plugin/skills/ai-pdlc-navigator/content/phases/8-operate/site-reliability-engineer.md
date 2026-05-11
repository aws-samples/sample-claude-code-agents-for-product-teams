# Site Reliability Engineer in Operate

Operate is your phase. You run the monitoring, incidents, DR testing, and capacity work that keeps the service reliable, performant, and cost-efficient. Your job is to hit SLOs inside the error budget, keep on-call load manageable, and preserve capacity headroom without overspending.

## What you do

- Run application monitoring — dashboards, alerts, SLI/SLO burn.
- Investigate production errors and lead incident response / on-call rotations.
- Drive root cause analysis with Developer and Architect on significant incidents.
- Run backup and disaster-recovery testing so DR claims are real, not theoretical.
- Monitor cost and capacity with Architect so the service stays efficient at scale.
- Triage and log production issues into the developer backlog.
- Partner with Security on SIEM operations and patching.

## Artifacts you own

- [monitoring dashboards & alerts](artifacts/monitoring-dashboards-alerts.md) — the live observability surface.
- [incident investigation report](artifacts/incident-investigation-report.md) — the initial post-event investigation.
- [root cause analysis report](artifacts/root-cause-analysis-report.md) — the RCA, produced with Developer and Architect.
- [incident postmortem](artifacts/incident-postmortem.md) — the blameless post-mortem and improvement actions.
- [DR test results](artifacts/dr-test-results.md) — the recurring disaster-recovery validation.
- [cost & capacity report](artifacts/cost-capacity-report.md) — capacity and cost, produced with Architect.
- [prioritized prod issue log](artifacts/prioritized-prod-issue-log.md) — the triaged prod-issue queue for developers.

## Artifacts you contribute to

- [patched dependencies](artifacts/patched-dependencies.md) — Security & Compliance owns; you drive the patch rollout side.
- [security monitoring alerts](artifacts/security-monitoring-alerts.md) — Security & Compliance owns; you operate the monitoring side.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Developer** — bi-directional on incidents, RCA, and production fixes.
- **Architect** — bi-directional on capacity, cost, and architectural root-cause.
- **Security & Compliance** — bi-directional on SIEM, patching, and security incidents.
- **Product Sponsor** — bi-directional on SLO performance and Sev-1 comms posture.
- **Release Manager** — bi-directional on release-related reliability and rollback readiness.

## Handoff into [Iterate](../9-iterate/README.md)

You exit Operate with real reliability, capacity, and cost evidence. Feed that into Iterate's architecture roadmap refresh, tech-debt grooming, and post-launch retrospective — the patterns you saw in production are the highest-leverage input to the next cycle's reliability investment.

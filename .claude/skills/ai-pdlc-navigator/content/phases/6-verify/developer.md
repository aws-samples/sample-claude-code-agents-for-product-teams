# Developer in Verify

Verify is where your Build-phase code meets production-like conditions. Your job shifts from producer to fixer — rehearsing migrations, triaging UAT defects, verifying telemetry, and making sure the code you signed off in Build stays signed off under the harder tests Verify applies.

## What you do

- Co-rehearse data migration with SRE — prove the migration runbook works on real-shaped data.
- Triage UAT defects with QA/Tester — decide what to fix, what to defer, what to document as known.
- Co-verify KPI telemetry with SRE so dashboards at Launch will show the right signals.
- Stay available for fast bugfixing as performance, security, and accessibility testing surface defects.

## Artifacts you own

- [migration runbook validation](artifacts/migration-runbook-validation.md) — co-owned with Site Reliability Engineer.

## Artifacts you contribute to

- [verified KPI telemetry](artifacts/verified-kpi-telemetry.md) — Site Reliability Engineer owns; you implement and verify.
- [triaged UAT defects](artifacts/triaged-uat-defects.md) — QA/Tester owns; you fix and re-verify.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — co-rehearses migrations; co-verifies KPI telemetry.
- **QA/Tester** — co-owns defect triage; your primary counterpart for test-driven fixes.
- **Security & Compliance** — fix pen-test findings you own.
- **UI/UX Designer** — fix visual-fidelity drift surfaced by their report.

## Handoff into [Launch](../7-launch/README.md)

In Launch you create demo assets and wire KPI events into dashboards with SRE. You know Verify is done when migration is rehearsed clean, KPI telemetry is verified, and the UAT defect queue is at acceptable-known-issue level or cleared.

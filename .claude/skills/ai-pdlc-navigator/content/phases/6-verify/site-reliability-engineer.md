# Site Reliability Engineer in Verify

You are here to prove the system will operate — under load, under failure, under real traffic. Verify is where SLOs get tested, where chaos reveals assumptions, and where your co-sign on the Production Readiness Review says the service is fit to run, not just to ship.

## What you do

- Run chaos / resilience testing jointly with QA/Tester so failure modes are known, not discovered in prod.
- Lead the Production Readiness Review with Release Manager and Architect so the operational picture is honest.
- Verify KPI telemetry emission with Developers so dashboards are wired before Launch, not after.
- Contribute to performance / load testing so capacity and cost assumptions are validated.
- Contribute to the data migration dress rehearsal so migration runbooks are proven, not theoretical.

## Artifacts you own

- [resilience test results](artifacts/resilience-test-results.md) — co-owned with QA/Tester.
- [verified KPI telemetry](artifacts/verified-kpi-telemetry.md) — co-owned with Developer.

## Artifacts you contribute to

- [migration runbook validation](artifacts/migration-runbook-validation.md) — Developer owns; you co-rehearse.
- [performance test report](artifacts/performance-test-report.md) — QA/Tester owns; you contribute operational/capacity interpretation.

## Outcomes you drive

- [PRR sign-off](outcomes/prr-sign-off.md) — co-owned with Release Manager and Architect.

## Who you work with

- **QA/Tester** — co-owns resilience testing and pairs on performance testing.
- **Release Manager** — co-owns PRR; together you certify the system is operable.
- **Architect** — co-owns PRR; interprets architectural implications of your findings.
- **Developer** — verifies KPI telemetry with you; fixes observability gaps.

## Handoff into [Launch](../7-launch/README.md)

In Launch you co-own the stabilized launch window / hypercare with Release Manager, and wire KPI events into dashboards with Developer. You know Verify is done when PRR is signed, KPI telemetry is flowing, chaos results are acceptable, and you're confident on-call can carry this service from day one.

# Architect in Verify

You are here to validate that the architecture you approved holds up under production-like conditions — and to name the risks honestly before Launch. Verify is where NFRs get tested for real, where chaos and performance expose assumptions, and where your co-sign on the Production Readiness Review says the system is fit to operate, not just to build.

## What you do

- Produce the architecture validation report against the verify environment — does the real system match the design.
- Run architectural risk assessment — what's the honest picture of what could fail in production.
- Co-own Production Readiness Review sign-off with SRE and Release Manager.
- Contribute to performance / load testing with QA and SRE so scaling assumptions are proven, not presumed.

## Artifacts you own

- [architecture validation report](artifacts/architecture-validation-report.md) — does the system match the design.
- [architectural risk report](artifacts/architectural-risk-report.md) — honest assessment of production risk.

## Artifacts you contribute to

- [PRR sign-off](outcomes/prr-sign-off.md) — Site Reliability Engineer owns; you co-sign as Architect.
- [performance test report](artifacts/performance-test-report.md) — QA/Tester owns; you contribute on scaling/NFR interpretation.

## Outcomes you drive

You don't drive outcomes this phase solo — you co-own PRR with SRE and Release Manager.

## Who you work with

- **Site Reliability Engineer** — co-owns PRR; produces chaos/resilience results and KPI telemetry you interpret.
- **QA/Tester** — co-owns performance testing; you interpret architectural implications.
- **Release Manager** — co-signs PRR based on readiness evidence you help produce.
- **Developer** — fixes architectural issues your validation surfaces.

## Handoff into [Launch](../7-launch/README.md)

In Launch you sign off rollback safety and monitor architectural launch signals. You know Verify is done when the architecture validation report is clean (or risks are accepted), PRR is signed, and you can defend any architectural risk the Sponsor accepts going into Launch.

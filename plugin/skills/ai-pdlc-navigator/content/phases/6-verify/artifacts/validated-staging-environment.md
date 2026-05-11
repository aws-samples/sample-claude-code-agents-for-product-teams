# validated staging environment

_Produced by: Staging deployment & smoke tests_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Release Manager

**Stakeholders:** QA/Tester

## What this is

A staging environment running the release candidate, confirmed via smoke tests to be operationally equivalent to the intended production state. Data, integrations, dependencies, and monitoring all live and behaving.

## Why it matters for the Release Manager

Every Verify activity that claims production-likeness depends on this. A staging environment you can trust is how perf tests, UAT, and security tests produce real signal — and how you avoid the "passed in staging, failed in prod" pattern that destroys launch confidence.

## Definition of Done

- [ ] Release candidate is deployed with build identifiers recorded
- [ ] Configuration diff vs. the production target is captured
- [ ] Integration endpoints are connected and verified
- [ ] Smoke test suite outcome and representative data load are documented
- [ ] Monitoring and alerting are active and wired to the correct channels

## What it contains

- Release candidate deployed and build identifiers recorded
- Configuration diff vs. production target
- Integration endpoints connected and verified
- Smoke test suite outcome
- Representative data loaded
- Monitoring and alerting active and wired to the right channels

## Inputs you rely on

- Provisioned environments and working CI/CD pipeline
- Stable build/deploy pipeline
- Integration map
- Test data strategy from test plan
- Migration runbook validation (for data steps)

## Who consumes it

- QA/Tester — runs campaigns against this env
- SRE — tests monitoring and alert wiring
- Security — runs pen-test and DAST here
- Stakeholders — conduct UAT here

## Common pitfalls

- Staging drift from prod over time without a diff report
- Stale integration mocks presented as "connected"
- Monitoring absent in staging so incidents go unnoticed during Verify
- Environment shared with other tenants that destabilize during test campaigns

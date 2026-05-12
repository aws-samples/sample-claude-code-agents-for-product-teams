# integration test results

_Produced by: Integration testing_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** QA/Tester

**Stakeholders:** Developer

**Accelerated MVP:** required — the integration points the MVP uses have to work

## What this is

The running record of integration-test outcomes — cross-service, cross-system, and contract tests — per build, per environment, with pass rates, flakiness, and top failure clusters. Owned by QA with heavy developer participation.

## Why it matters for the QA/Tester

Integration is where most real defects hide — the unit tests say green but the whole doesn't work. Keeping an accurate, trended record of integration results tells you which seams are brittle, which owners to engage, and whether the build is trustworthy enough to promote.

## Definition of Done

- [ ] Run history shows pass/fail counts per suite
- [ ] Failure clusters are grouped by root cause
- [ ] Every run is tagged with environment and build
- [ ] Flaky tests are identified and their quarantine state is recorded
- [ ] Evidence links (logs, traces) are attached for failed runs

## What it contains

- Run history with pass/fail counts per suite
- Failure clusters grouped by root cause
- Environment and build tagged per run
- Flaky-test identification and quarantine state
- Evidence links (logs, traces) for analyst follow-up
- Trend metrics: pass rate, MTTR for integration regressions

## Inputs you rely on

- Automated test suite and test plan
- Provisioned environments and integration map
- Feature code and API specifications
- Working CI/CD pipeline
- Telemetry for diagnosing intermittent failures

## Who consumes it

- Developers — fix regressions and triage flake
- Release Manager — gates promotion on integration stability
- QA/Tester leads — monitor coverage of integration points
- SRE — sees integration signals that correlate with production risk

## Common pitfalls

- Failures explained away as "environment issue" repeatedly without root-cause fix
- Flaky quarantine that never gets cleared so coverage silently erodes
- Integration test data drifts from production shapes
- Running only on merge — regressions caught after the problematic commit is buried

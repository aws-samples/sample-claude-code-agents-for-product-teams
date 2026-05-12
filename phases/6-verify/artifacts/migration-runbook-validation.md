# migration runbook validation

_Produced by: Data migration dress rehearsal_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Developer

**Stakeholders:** Site Reliability Engineer

**Accelerated MVP:** required when the MVP migrates data; otherwise skip

## What this is

Evidence from a full dress-rehearsal of the data migration — executed end-to-end against production-scale data in a prod-like environment, timed, measured, and validated against acceptance criteria. The migration runbook annotated with real observations.

## Why it matters for the Developer

Data migrations are among the highest-risk launch activities — they can't always be reversed and they block rollout if they slip their window. Rehearsing cold against real-shaped data is how you find the timing, correctness, and operability issues before they become a customer-visible incident.

## Definition of Done

- [ ] Rehearsal scope and data-set characterization are recorded
- [ ] Step-by-step execution log with timings is captured
- [ ] Correctness verification queries and their results are attached
- [ ] Rollback rehearsal outcome and observed performance/resource usage are documented
- [ ] Required runbook updates prior to production execution are listed

## What it contains

- Rehearsal scope and data-set characterization
- Step-by-step execution log with timings
- Correctness verification queries and results
- Rollback rehearsal outcome
- Performance and resource usage observed
- Runbook updates required before production execution

## Inputs you rely on

- Deployment runbook and data-migration plan
- Data model and integration map
- Validated staging environment with representative data
- Telemetry and monitoring per the telemetry plan
- Change-control coverage for data changes

## Who consumes it

- SRE — operates the production migration window
- Release Manager — gates launch on successful rehearsal
- Architect — validates assumptions about data shape and volume
- QA/Tester — runs post-migration functional checks against expected shape

## Common pitfalls

- Rehearsal against sanitized data that misses production-scale edge cases
- Rollback path not actually rehearsed, only described
- Window assumed linear when real migration hits lock contention
- Runbook not updated with the actual timings and observations

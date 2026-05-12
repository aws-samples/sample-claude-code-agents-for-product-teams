# architectural launch signals

_Produced by: Architectural launch signals monitoring_

**Business outcome supported:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — the KPI and telemetry dashboard covers this

## What this is

The focused set of architectural telemetry watched during launch — the signals that tell you whether the system is behaving the way the design assumed under real traffic. Not every dashboard, just the ones that would trigger a rollback or redesign if they broke.

## Why it matters for the Architect

NFRs get promises at design time and evidence at launch time. Launch is the first moment real users hit the architecture; if integration fan-out, queue depth, saturation, or partner dependencies behave differently than the threat/capacity model predicted, you need to see it in minutes, not days.

## Definition of Done

- [ ] Watchlist names each architectural SLI tracked (latency percentiles, queue lag, DB contention, cache hit rates, partner API error rates).
- [ ] Every signal has a threshold tied to a specific NFR or capacity model assumption.
- [ ] Dashboard link and alert route are recorded for each signal on the watchlist.
- [ ] Escalation path identifies the named owner and next step when a signal trips.
- [ ] Known-unknowns being watched for the first time in production are explicitly listed.

## What it contains

- Watchlist of architectural SLIs (latency percentiles, queue lag, DB contention, cache hit rates, partner API error rates)
- Thresholds tied to NFRs and capacity model assumptions
- Links to dashboards and alert routes during hypercare
- Known-unknowns you are explicitly watching for the first time in production
- Escalation path when a signal trips
- Post-launch observations to feed into architectural health report

## Inputs you rely on

- Architecture document and NFR targets
- Performance test report and resilience test results from Verify
- Monitoring dashboards & alerts from SRE
- Capacity & scale predictions and assumptions
- Threat model coverage for launch-day abuse vectors

## Who consumes it

- Release Manager and SRE — use signals as inputs to continue/rollback calls
- Product Sponsor — referenced in rollback safety sign-off
- Post-launch Architect — feeds architectural health report in Operate
- Developer — targets for hotfix if a signal degrades

## Common pitfalls

- Watching too many signals and missing the critical few
- Thresholds copied from staging without accounting for production scale
- No rollback action tied to a tripped signal — alerts without decisions
- Letting the watchlist atrophy after hypercare instead of promoting it to steady-state

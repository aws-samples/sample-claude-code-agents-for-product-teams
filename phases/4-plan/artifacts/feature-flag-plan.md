# feature flag plan

_Produced by: Feature flag strategy_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Architect

**Stakeholders:** Developer

## What this is

The strategy for how the team will use feature flags — which flagging platform, flag taxonomy (release, experiment, ops, permission), lifecycle, rollout patterns, and cleanup discipline. It's the operating contract for trunk-based delivery and progressive rollout.

## Why it matters for the Architect

Flags are the switch between "merge is risky" and "merge is safe, rollout is the lever." Without a shared plan, teams reinvent flagging per service, accumulate zombie flags, and expose control logic to users. You set the pattern once so Build-phase engineering stays uniform and SRE gets real kill-switches at launch.

## Definition of Done

- [ ] Flag types and naming conventions are defined
- [ ] Targeting-rule dimensions (cohort, percentage, geography, tenant) are specified
- [ ] Lifecycle rules cover creation, ownership, and cleanup SLAs
- [ ] Platform choice and integration pattern are documented
- [ ] Default behavior on flag-service outage is specified
- [ ] Audit and change-logging requirements are stated

## What it contains

- Flag types and naming conventions (release, experiment, operational, permission)
- Targeting rules — user cohort, percentage, geography, tenant
- Lifecycle: who creates, who owns, cleanup SLAs
- Platform choice (build vs. buy) and integration pattern
- Default behavior on flag-service outage
- Audit and change-logging requirements

## Inputs you rely on

- Deployment runbook — flags are a rollback lever
- Telemetry plan — flag state is a key dimension on events
- Security control requirements — permission flags need extra rigor
- Existing enterprise flagging tooling (if any)
- Product plans for experimentation and beta cohorts

## Who consumes it

- Developers — build to the pattern when adding flags
- Release Manager — uses flags as a rollout and rollback tool
- SRE — configures the flag service, alerts on flag-service health
- QA/Tester — tests both flag states and edge transitions

## Common pitfalls

- No cleanup SLA — flag count grows unbounded and becomes config-graph chaos
- Using release flags for permission logic — authz bugs waiting to happen
- Fail-open defaults on critical flags that leak half-built features during an outage
- No audit trail when marketing or PM toggles production flags directly

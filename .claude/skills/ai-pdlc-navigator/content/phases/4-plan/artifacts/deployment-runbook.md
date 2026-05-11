# deployment runbook

_Produced by: Rollout & rollback plan_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Release Manager

**Stakeholders:** Site Reliability Engineer

## What this is

The operational playbook for rolling out the release — pre-deploy checks, deploy steps, progressive rollout controls (flags, canaries, rings), health signals to watch, and explicit rollback procedures. Executable under pressure by whoever is on-call.

## Why it matters for the Release Manager

Launches fail on missing detail, not missing bravery. A runbook with rehearsed steps, clear halt criteria, and a tested rollback is how you ship confidently and reverse cleanly — protecting the SLO, the customer, and the team's reputation for predictable releases.

## Definition of Done

- [ ] Pre-deploy checklist and readiness gates are documented
- [ ] Deploy sequence lists timing, owner, and expected duration per step
- [ ] Progressive rollout plan specifies canary thresholds and promotion criteria
- [ ] Health signals and stop/rollback triggers are defined
- [ ] Rollback procedure has been tested in staging
- [ ] Comms plan covers internal and customer-facing notifications

## What it contains

- Pre-deploy checklist and readiness gates
- Deploy sequence with timing, owner, and expected duration per step
- Progressive rollout plan (canary thresholds, promotion criteria)
- Health signals and stop/rollback triggers
- Rollback procedure tested in staging
- Comms plan for internal and customer-facing notifications

## Inputs you rely on

- Working CI/CD pipeline and provisioned environments
- Service-level objectives and monitoring dashboards
- Feature flag plan
- Database migration strategy and integration map
- Change advisory or approval process

## Who consumes it

- SRE on-call — executes deploy and monitors health
- Developers — participate in rollout windows and halt conditions
- Release Manager — runs the release using the runbook
- Product Owner and Sponsor — consulted on no-go/stop calls during high-risk rollouts

## Common pitfalls

- Rollback path untested until it's needed
- Migration steps that are one-way, with no reverse path
- Health signals defined loosely — "looks okay" is not a halt criterion
- Runbook last updated three releases ago and no longer matches the stack

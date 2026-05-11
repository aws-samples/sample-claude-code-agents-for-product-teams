# released product in production

_Produced by: Deploy / release execution_

**Business outcome supported:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

**Primary owner:** Release Manager

**Stakeholders:** _(none listed)_

## What this is

The signed-off record that the release bill-of-materials has been successfully deployed to production — what exact artifacts, which environments, at what time, under which feature-flag posture — and that the deploy is considered complete.

## Why it matters for the Release Manager

This is the moment your phase of responsibility transitions from "getting it there" to "keeping it stable." A clean release record lets you prove release integrity, gives SRE and Support a known state to reason against, and anchors rollback if signals go bad.

## Definition of Done

- [ ] Release version and full bill-of-materials (services, images, migrations) are recorded.
- [ ] Deployment timestamps are captured per environment and per wave.
- [ ] Feature flag state at launch is documented.
- [ ] Database migrations applied are listed with reversible or irreversible status.
- [ ] Sign-off from Release Manager, SRE, and on-call engineer is captured.

## What it contains

- Release version and full bill-of-materials (services, images, migrations)
- Deployment timestamps per environment and per wave
- Feature flag state at launch
- Database migrations applied (reversible/irreversible)
- Smoke test and health check results immediately post-deploy
- Sign-off from Release Manager, SRE, and on-call engineer

## Inputs you rely on

- Deployment runbook and rollback plan
- Stable build/deploy pipeline from Verify
- Go/no-go decision and rollback safety sign-off
- CI/CD release bill-of-materials
- Change-review approvals from governance process

## Who consumes it

- SRE and on-call — authoritative "what is running" for incident response
- QA/Tester — baseline for production validation smoke tests
- Security & Compliance — audit evidence that release went through controls
- Operate phase Architect — starting state for architectural health monitoring

## Common pitfalls

- Partial rollouts recorded as "done" when only a fraction of traffic was migrated
- Feature flag state omitted; rollback ambiguity when a flag is the real switch
- Unrecorded hotfixes during hypercare drift the BOM from reality
- Skipping post-deploy smoke tests because monitoring "looks fine"

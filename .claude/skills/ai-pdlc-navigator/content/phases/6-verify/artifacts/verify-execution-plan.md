# verify execution plan

_Produced by: Verify-phase coordination_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Project Manager

**Stakeholders:** _(none listed)_

## What this is

The PM's sequenced plan for the Verify phase — which test campaigns run when, environment contention, defect-fix windows, readiness checkpoint dates, and the path to launch-date commitment. Coordinates many roles whose work overlaps tightly.

## Why it matters for the Project Manager

Verify looks simple ("run the tests, get the sign-offs") but is where most launch dates slip because activities contend for the same environments and people. Planning Verify as its own coordinated mini-schedule is how you keep the campaigns out of each other's way and preserve the launch-date confidence interval.

## Definition of Done

- [ ] Campaign calendar covers functional, perf, security, UAT, a11y, and resilience
- [ ] Environment allocation and contention plan are documented
- [ ] Defect-fix windows and retest cycles are scheduled
- [ ] Readiness checkpoint dates (readiness assessment, PRR, compliance go/no-go) and go/no-go and launch-date decision checkpoints are calendared
- [ ] Owners per activity and escalation paths are named

## What it contains

- Campaign calendar (functional, perf, security, UAT, a11y, resilience)
- Environment allocation and contention plan
- Defect-fix windows and retest cycles
- Readiness checkpoint dates (readiness assessment, PRR, compliance go/no-go)
- Go/no-go and launch-date decision checkpoints
- Owners per activity and escalation paths

## Inputs you rely on

- Test plan, security test plan, and NFR document
- Baselined schedule and iteration plan
- Validated staging environment availability
- Provisioned environments
- Dependencies on external teams or vendors

## Who consumes it

- All Verify-phase role owners — execute to it
- Release Manager — coordinates release-window from its output
- Product Sponsor — sees path-to-launch clarity
- Business Analyst — plans UAT coordination in context

## Common pitfalls

- Treating Verify as "extra time to finish Build" — campaigns compress badly
- Environment contention not modeled — two teams find the same env at 3am
- No defect-fix windows — late fixes destabilize late tests
- Sign-off checkpoints not calendared, so readiness is never formally declared

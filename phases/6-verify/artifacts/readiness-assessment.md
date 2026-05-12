# readiness assessment

_Produced by: Assess feature readiness_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** QA/Tester

**Stakeholders:** Security & Compliance

**Accelerated MVP:** slim — a DoD checklist plus a go-ahead from QA is enough

## What this is

QA's aggregated view of feature-level readiness across the Verify campaign — functional coverage, regression state, defect posture, and outstanding risk. The QA input that rolls up into the launch-readiness assessment.

## Why it matters for the QA/Tester

You own the evidence behind "it works." Assembling a clear readiness view — not just test results, but the interpretation of those results against risk — is how you give the Sponsor and Release Manager a trustworthy signal and keep your veto rights credible.

## Definition of Done

- [ ] Feature-by-feature coverage and pass rate are reported
- [ ] Open defects are listed by severity with status and owner
- [ ] Test-to-requirement coverage completion is shown
- [ ] Known gaps, residual risks, and retest completion after remediation are recorded
- [ ] Each feature has an explicit recommendation: ready / ready with caveats / not ready

## What it contains

- Feature-by-feature coverage and pass rate
- Open defects by severity with status and owner
- Test-to-requirement coverage completion
- Known gaps and residual risks
- Retest completion after remediation
- Recommendation per feature: ready / ready with caveats / not ready

## Inputs you rely on

- Test plan and test-to-requirement coverage map
- Regression, performance, accessibility, security test results
- Triaged UAT defects
- Automated test suite state
- Control-to-test coverage map

## Who consumes it

- Launch-readiness assessment consumes this directly
- UAT/beta sign-off uses it as a gate input
- Product Owner — scope decisions on features not ready
- Release Manager — uses per-feature readiness for release composition

## Common pitfalls

- Pass rate reported without severity context
- "Tested" reported without coverage detail
- Residual risks hidden in long appendix, not summarized
- Recommendation absent — stakeholders must infer QA's view

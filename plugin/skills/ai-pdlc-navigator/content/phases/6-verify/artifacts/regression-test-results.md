# regression test results

_Produced by: Regression testing_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** QA/Tester

**Stakeholders:** _(none listed)_

## What this is

Full-regression-suite execution against the release candidate in a production-like environment — pass/fail, trend, flakiness, and any regressions introduced by late-Build or Verify-phase fixes.

## Why it matters for the QA/Tester

Release candidates regress constantly without a trustworthy regression signal. Running the full suite against the candidate build — not just delta tests — is how you prove nothing old broke while you were fixing something new.

## Definition of Done

- [ ] Suite was executed against the exact release candidate and the build ID is recorded
- [ ] Pass/fail is reported by test area with trend
- [ ] Regressions introduced during the Verify window list owner and state
- [ ] Flake isolation and quarantine decisions are documented
- [ ] Coverage verification confirms every acceptance criterion was reached, with evidence artifacts (logs, screenshots, traces) attached

## What it contains

- Suite execution against the exact release candidate
- Pass/fail by test area with trend
- Regressions introduced in the Verify window, owner, and state
- Flake isolation and quarantine decisions
- Coverage verification (every acceptance criterion reached)
- Evidence artifacts (logs, screenshots, traces)

## Inputs you rely on

- Automated test suite and test plan
- Validated staging environment
- Merged release candidate
- Triaged UAT defects that spawned late fixes
- Test-to-requirement coverage map

## Who consumes it

- Readiness assessment aggregates these results
- Release Manager — gates on regression stability
- Developers — work regressions introduced during Verify
- Product Owner — sees per-feature regression posture

## Common pitfalls

- Only running on main, not on the exact release candidate artifact
- Quarantining too many flakes until the suite no longer covers the surface
- Pass rate ignored when the passing tests are the easy ones
- No feedback loop from escapes to added regression tests

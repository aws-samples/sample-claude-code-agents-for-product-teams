# conformance findings

_Produced by: Architecture conformance review_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

Findings from periodic architecture conformance reviews — where implementation has drifted from approved patterns, NFRs, data model, or integration contracts. Per finding: severity, what's deviating, why, and the remediation plan.

## Why it matters for the Architect

Unchecked drift turns the approved architecture into a paper artifact and bakes in future support cost, NFR misses, and reliability risk. Regular conformance review with tracked findings is how you keep the real system close enough to intent that the ADRs still describe it.

## Definition of Done

- [ ] Every finding names the component or location affected
- [ ] Severity is classified as blocker, major, or minor with the NFR or pattern in question
- [ ] Root-cause notes accompany each finding
- [ ] Remediation plan lists an owner and target date
- [ ] Risk-accepted items carry an expiry and rationale

## What it contains

- Finding description and component/location affected
- Severity (blocker, major, minor) and NFR or pattern in question
- Root-cause notes (shortcut, missing enabler, divergent context)
- Remediation plan with owner and target date
- Risk-accepted items with expiry and rationale
- Trend metrics by area or team

## Inputs you rely on

- Architecture document and ADRs
- Reviewed code, PR history, and dependency graphs
- Integration test results and performance data
- Design guidance session notes
- Updated ADRs from Build

## Who consumes it

- Developers — remediate findings assigned to them
- Architect — uses findings to update ADRs or enabler backlog
- Product Owner — sees cost of conformance debt and prioritizes remediation
- Release Manager — gates high-risk deviations from release

## Common pitfalls

- Findings logged but never remediated — list becomes wallpaper
- Severity inflation or deflation — signal becomes untrustworthy
- Reviews done by one person who misses their own areas of authorship
- No connection to enabler backlog — patterns stay broken because no one owns fixing them

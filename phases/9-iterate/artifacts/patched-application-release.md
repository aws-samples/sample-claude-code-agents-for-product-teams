# patched application release

_Produced by: Bugfix application updates_

**Business outcome supported:** close the loop — measure actual performance against the business case, decide continue/pivot/sunset, and feed validated learning back into Discover for the next cycle.

**Primary owner:** Developer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required when patches are being shipped

## What this is

A shipped release that bundles bug fixes, minor enhancements, and dependency updates — the steady-state production cadence rather than a major feature launch. Versioned, released notes included, tested to the same bar as any other release.

## Why it matters for the Developer

These releases are how customer-facing quality actually improves between bigger bets. Your discipline in shipping them regularly and cleanly determines whether the team is trusted to run production; sloppy patch releases create the incidents that force freezes and slow everything down.

## Definition of Done

- [ ] Fix list references specific issue IDs
- [ ] Dependency upgrades included in the release are listed
- [ ] Test coverage evidence is attached
- [ ] Release notes and changelog entry are published
- [ ] Rollback plan and deployment record are included

## What it contains

- Fix list with issue IDs
- Dependency upgrades included
- Test coverage evidence
- Release notes and changelog entry
- Rollback plan
- Deployment record

## Inputs you rely on

- Prioritized bug list and known-issues list
- Prioritized tech-debt list
- Patched dependencies from security
- Regression and integration test results
- Release notes from Release Manager

## Who consumes it

- Customers — receive the fixes
- Customer Support — update known-issues and close tickets
- Security & Compliance — record dependency patches as evidence
- SRE — confirm operational impact

## Common pitfalls

- Patches quietly shipped with no release notes — customers confused
- Mixing risky refactors into a "patch" release
- Skipping regression because "it's only a small fix"
- Rollback plan absent; small patch causes big incident

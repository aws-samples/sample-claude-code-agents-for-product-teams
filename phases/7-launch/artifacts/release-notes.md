# release notes

_Produced by: Write release notes_

**Business outcome supported:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

**Primary owner:** Release Manager

**Stakeholders:** _(none listed)_

## What this is

The canonical, customer-facing statement of what changed in this release: new capabilities, fixes, breaking changes, deprecations, and known issues. Short, scannable, and precise enough to be the single source of truth for "what shipped."

## Why it matters for the Release Manager

Release notes are the artifact support, sales, and customers all point to when something looks different. Clean notes protect launch integrity: they prevent surprise breakage conversations, anchor rollback decisions, and become the audit record of what hit production on this date.

## Definition of Done

- [ ] Version, release date, and deployment scope are stated at the top.
- [ ] New features and enhancements link to corresponding documentation.
- [ ] Bug fixes are mapped to issue IDs.
- [ ] Breaking changes are called out with migration guidance.
- [ ] Known issues are listed with workarounds and ETA.

## What it contains

- Version, release date, and deployment scope
- New features and enhancements with links to docs
- Bug fixes mapped to issue IDs
- Breaking changes with migration guidance
- Deprecations and sunset timelines
- Known issues with workarounds and ETA
- Compliance-relevant notes (security patches, regulatory flags)

## Inputs you rely on

- Feature documentation and user guides from Technical Writer
- Triaged UAT defects and resolved/unresolved list from Verify
- Release bill-of-materials from the CI/CD pipeline
- Breaking-change decisions and deprecation plans
- Legal approval for any compliance language

## Who consumes it

- Customers and channel partners — decide whether and how to upgrade
- Customer Support — anchors troubleshooting and reduces ticket volume
- Sales & Marketing — sourcing for launch announcement and battlecards
- Auditors — trace what was in production when

## Common pitfalls

- Feature dumps without user-framed value; customers skim and miss the point
- Omitting known issues to look cleaner — support pays the cost
- Breaking changes buried in a bullet instead of called out with migration path
- Versioning drift with release notes published under the wrong version

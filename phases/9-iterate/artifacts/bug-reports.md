# bug reports

_Produced by: Document bugs with reproduction details_

**Business outcome supported:** close the loop — measure actual performance against the business case, decide continue/pivot/sunset, and feed validated learning back into Discover for the next cycle.

**Primary owner:** QA/Tester

**Stakeholders:** _(none listed)_

## What this is

Structured bug reports — reproducible, scoped, and severity-assigned — from exploratory testing, failed automation, regression runs, and field reports. The raw material Product Owner uses to build the prioritized bug list.

## Why it matters for the QA/Tester

A bug without reproduction is an opinion, not a defect. Your discipline in filing clean, reproducible reports is what makes engineering take them seriously and fix them quickly — and what keeps the bug backlog a trustworthy signal of product quality.

## Definition of Done

- [ ] Each report has a title, summary, and observed behavior
- [ ] Expected behavior is documented alongside observed
- [ ] Reproduction steps include environment and test data
- [ ] Severity and suggested priority are assigned
- [ ] Affected version, device/config, and related tickets/logs/recordings are linked

## What it contains

- Title, summary, and observed behavior
- Expected behavior
- Steps to reproduce with environment and data
- Severity and suggested priority
- Affected version and device/config
- Related tickets, logs, or recordings

## Inputs you rely on

- Exploratory and regression test sessions
- Failed automation runs
- Customer resolutions and escalated tickets
- Release notes (context for changes)
- Known-issues list (to avoid duplicates)

## Who consumes it

- Product Owner — feeds prioritized bug list
- Developer — reproduces and fixes
- Customer Support — references when customer reports match
- Iterate phase — pattern analysis on bug sources

## Common pitfalls

- "Sometimes fails" reports without reproduction — engineering can't act
- Missing environment/version context; fixes target wrong code
- Severity inflated by individual reporter preference
- Duplicate reports that fragment engineering attention

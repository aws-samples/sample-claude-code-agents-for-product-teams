# feature code

_Produced by: New feature development_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — the MVP is code

## What this is

The actual application code that implements a feature — source, tests, migrations, config, and documentation as-code. The primary output of the Build phase and the medium in which most decisions ultimately live.

## Why it matters for the Developer

Code is the commitment — everything upstream has been leading to this, and everything downstream inherits whatever you encode here. Treating feature code as a first-class artifact (reviewed, tested, instrumented, documented) is the difference between work that compounds and work that generates incident pages later.

## Definition of Done

- [ ] Production source implements the stated acceptance criteria
- [ ] Unit and integration tests accompany the change
- [ ] Schema migrations and risky config changes sit behind flags
- [ ] Telemetry and structured logging match the telemetry plan
- [ ] The commit or PR links to the originating work item

## What it contains

- Production source implementing the acceptance criteria
- Accompanying unit and integration tests
- Schema migrations and config changes behind flags where needed
- Inline docs, ADR updates, and interface docs as appropriate
- Telemetry and structured logging per the telemetry plan
- Links in the commit/PR to the originating work item

## Inputs you rely on

- Design specification and API specification
- Architecture document, ADRs, and enabler backlog
- Telemetry plan and feature flag plan
- Testable acceptance criteria and test plan
- Reviewed code and prior related patterns in the repo

## Who consumes it

- Reviewers — evaluate for correctness, maintainability, and NFR fit
- QA/Tester — tests the running behavior
- SRE — operates the service this code becomes
- Future developers — extend, debug, and maintain

## Common pitfalls

- Treating tests as optional — bar moves only when they're part of the PR
- Skipping telemetry or feature flags and retrofitting later under pressure
- Wide PRs that resist meaningful review
- Changes that silently drift from the approved architecture or data model

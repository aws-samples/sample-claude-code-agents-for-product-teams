# merged code in main branch

_Produced by: Merge code_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — trunk is where the MVP lives

## What this is

Reviewed code integrated into the main branch through the merge process — all gates passed, pipeline green, changelog entry captured. The state of main is the canonical build-ready snapshot at any moment.

## Why it matters for the Developer

Main must remain shippable. Your disciplined integration — small PRs, clean history, passing gates, flagged incomplete work — is what lets the team release on demand rather than stabilize on deadline.

## Definition of Done

- [ ] Merged commits use conventional messages that survive tooling
- [ ] Pipeline record shows green tests, scans, and artifact signing
- [ ] Changelog entry references the originating work item
- [ ] Branch protection evidence (required reviewers, checks) is present
- [ ] A tag or build artifact is produced by the merge

## What it contains

- Merged commits with conventional messages that survive tooling
- Green pipeline record (tests, scans, artifact signing)
- Changelog entry referencing the work item
- Branch protection evidence (required reviewers, checks)
- Tag or artifact produced by the merge
- Revert procedure ready if the merge later proves harmful

## Inputs you rely on

- Reviewed code
- Working CI/CD pipeline
- Changelog review process
- Feature flag plan (for gating incomplete features behind flags)
- Lint/static-analysis and vulnerability scan outcomes

## Who consumes it

- SRE and Release Manager — promote from main to environments
- QA/Tester — tests against main-built artifacts
- Developers — rebase and build on top of current main
- Audit tooling — uses merge history for change traceability

## Common pitfalls

- Feature branches merged with incomplete work behind weak flags — landmines in main
- Merge commits that erase review history or authorship
- Green pipeline achieved by disabled tests rather than fixed tests
- Main goes red and stays red — rolling integration breaks the contract

# triaged UAT defects

_Produced by: UAT defect triage_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** QA/Tester

**Stakeholders:** Developer

## What this is

The defect queue from UAT and beta sessions — each finding triaged for severity, reproducibility, scope disposition (fix now, fix post-launch, won't fix), and owner. The operational artifact of running UAT.

## Why it matters for the QA/Tester

Verify windows are short; not every UAT defect gets fixed. A disciplined triage is how you concentrate scarce fix capacity on the items that actually alter launch risk and document the rest so they don't vanish into the void after GA.

## Definition of Done

- [ ] Each finding includes description, steps, environment, and severity
- [ ] Reproducibility state and attached evidence are recorded
- [ ] Disposition (fix, defer, accept, won't-fix) is stated with rationale
- [ ] Owner and target fix date are listed for in-scope items
- [ ] Retest status after fix and links to backlog items for deferred defects are captured

## What it contains

- Finding description, steps, environment, and severity
- Reproducibility state and attached evidence
- Disposition: fix, defer, accept, won't-fix — with rationale
- Owner and target fix date if in scope
- Retest status after fix
- Links to created backlog items for deferred defects

## Inputs you rely on

- UAT coordination & results
- Test plan severity rubric
- Triaged vulnerabilities (for security-flavored findings)
- Integration test results for duplicates
- Product Owner priority input on scope calls

## Who consumes it

- Developers — fix assigned defects
- Release Manager — uses severity distribution as a gate input
- Product Owner — weighs scope trade-offs
- Business Analyst — updates benefits/assumption log where defects change value

## Common pitfalls

- Defects dumped into the backlog with no disposition — lost until post-launch chaos
- Severity inflation from stakeholders protecting pet concerns
- Deferred defects never get a created ticket — unfindable later
- Retest step skipped under time pressure — reopens in prod

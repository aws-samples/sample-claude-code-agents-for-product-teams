# change impact report

_Produced by: Scope-change impact analysis_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the MVP is contained to its own codebase

## What this is

The BA's analysis of a proposed scope change — what it affects across requirements, tests, data, processes, and downstream consumers, plus the benefits and risks of doing or not doing it. Feeds the change-control package.

## Why it matters for the Business Analyst

Scope change is where discipline either holds or dissolves. A rigorous impact report is how you stop the drift-through-ambiguity pattern — changes get accepted or rejected based on evidence, not enthusiasm, and everyone who inherits consequences is named.

## Definition of Done

- [ ] Change statement identifies the requester
- [ ] Affected requirements are classified as new, modified, or retired with traceability impact
- [ ] Downstream systems, processes, and teams affected are named
- [ ] Benefits and risks of approving vs. deferring are both stated
- [ ] Recommendation includes written rationale

## What it contains

- Change statement and requested-by
- Requirements affected (new, modified, retired) with traceability impact
- Systems, processes, and downstream teams affected
- Test-coverage deltas implied
- Benefits/risks of approving vs. deferring
- Recommendation with rationale

## Inputs you rely on

- Traceability matrix and approved requirements
- Technical impact analysis (architecture-side)
- Security control requirements and privacy impact assessment
- Stakeholder comms plan (who must be notified)
- Benefits plan (benefit implications of the change)

## Who consumes it

- Product Owner and Sponsor — approve/reject through change control
- Project Manager — folds into the change control package
- Architect and Security — respond to technical and control impacts
- QA/Tester — updates test plan and coverage

## Common pitfalls

- Analysis skipped because "it's small" — small changes accumulate to large drift
- Impact limited to the team's surface, ignoring support, docs, and partners
- Recommendation absent — leaves stakeholders to guess the BA's view
- Benefits claimed without evidence, making trade-offs impossible to judge

# skills requirement input

_Produced by: Technical skills & roles requirement_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the existing squad covers the MVP

## What this is

A role-by-role breakdown of the technical skills the approved architecture needs — languages, frameworks, platforms, specialist disciplines — mapped against when in the plan each skill must be on-seat. It's the Architect's input to staffing decisions, not a generic job-requisition doc.

## Why it matters for the Architect

You own NFR fit and solution-viability; if the team can't operate the stack you approved, the architecture fails in execution regardless of its design. This artifact turns architecture decisions into concrete hiring, training, or vendor calls before the schedule bakes in assumptions you can't meet.

## Definition of Done

- [ ] Skill taxonomy is tied to the architectural components that need it
- [ ] Quantity and proficiency level (lead vs. contributor) are specified per skill
- [ ] Timing is captured for when each skill must be on-seat
- [ ] Current-bench gaps are listed with a proposed remedy (hire, contract, upskill, partner)
- [ ] Cross-team dependencies on scarce skills are called out
- [ ] Risks where single-threaded skills threaten the critical path are flagged

## What it contains

- Skill taxonomy tied to architectural components (e.g., Kafka, Terraform, specific cloud services, accessibility, performance engineering)
- Quantity needed per skill and proficiency level (lead vs. contributor)
- Timing — which skills are needed at kickoff vs. later milestones
- Current-bench gaps and proposed remedies (hire, contract, upskill, partner)
- Cross-team dependencies where scarce skills are shared
- Risk call-outs where a single-threaded skill threatens the critical path

## Inputs you rely on

- Approved architecture document and ADRs from Design
- Technical milestone plan sequencing
- Current headcount and skills inventory from Engineering Management
- Vendor/partner commitments from Design phase
- NFR document (perf, security, reliability targets drive specialist needs)

## Who consumes it

- Product Sponsor — uses it to approve resource commitment and unlock budget
- Project Manager — folds it into the resource schedule and iteration plan
- Engineering Manager / Director — executes hiring, contracting, or reassignment
- HR / Talent Acquisition — sources candidates against concrete requirements

## Common pitfalls

- Listing titles instead of skills — "Senior Engineer" tells no one what to hire for
- Ignoring timing — everything shows as "needed day 1" which is rarely true and inflates cost
- Skipping operate-phase skills (SRE, on-call coverage) and discovering the gap at launch
- Treating the document as one-and-done when architecture evolves during Build

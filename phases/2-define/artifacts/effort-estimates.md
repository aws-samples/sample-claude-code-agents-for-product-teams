# effort estimates

_Produced by: Estimation / sizing_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Developer

**Stakeholders:** Project Manager

**Accelerated MVP:** slim — t-shirt sizing on the MVP scope items is enough

## What this is

Engineering sizing of the requirements and enabler work, expressed in whatever currency the team uses (points, T-shirt sizes, days, cost), with confidence bands. It is what turns the requirements document into a plannable body of work.

## Why it matters for the Developer

You produce these because estimates drive schedules, staffing, and the business case. Underestimates destroy credibility and lead to a death march; overestimates cede the initiative to someone else. Honest ranges with explicit assumptions are how you protect both the team and the schedule.

## Definition of Done

- [ ] Each requirement or epic has an estimate with a confidence band, not a single point
- [ ] Assumptions behind each estimate are documented
- [ ] Explicit exclusions (integration, migration, enablement, hardening) are listed
- [ ] Spike candidates are named where uncertainty is too high to size
- [ ] Total envelope rolls up with a stated contingency rationale

## What it contains

- Per-requirement or per-epic estimate with confidence band
- Assumptions behind each estimate
- Explicit exclusions (integration, migration, enablement, hardening)
- Dependencies that could change the estimate
- Spike candidates where uncertainty is too high to size
- Total envelope rolled up with a contingency rationale

## Inputs you rely on

- [Requirements document](requirements-document.md) and [NFR document](nfr-document.md)
- [Technical feasibility findings](technical-feasibility-findings.md) and [capability gap report](capability-gap-report.md)
- Historical throughput data from comparable work
- Team composition and realistic availability

## Who consumes it

- Project Manager — baselines schedule and budget from it
- Product Sponsor — ratifies the envelope in Define exit and the Plan-phase commitment
- Business Analyst — uses precision to prune or resequence requirements
- Architect — sees where spike investment is required

## Common pitfalls

- Single-point estimates with no confidence band
- Estimating only happy path coding; missing testing, reviews, rework, docs
- Assumptions in heads, not on paper; they cannot be revisited
- No re-estimate cadence as design detail lands and assumptions resolve

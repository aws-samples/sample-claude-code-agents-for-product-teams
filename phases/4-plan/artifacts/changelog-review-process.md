# changelog review process

_Produced by: Change-review process setup_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — "every PR gets a reviewer" is the review process

## What this is

The defined process for reviewing changes flowing toward production — how PRs, infra changes, and dependency updates are classified, who reviews, what SLAs apply, and how changelogs are curated for release notes and audit.

## Why it matters for the SRE

Reliability is won or lost in the change stream. A consistent review process catches risky changes early, keeps the changelog trustworthy for release notes and rollback, and provides the evidence trail that auditors and incident responders need.

## Definition of Done

- [ ] Change classifications and routing rules are defined
- [ ] Review SLAs and minimum-reviewer requirements are specified per class
- [ ] Merge-gate criteria and pipeline enforcement mechanisms are documented
- [ ] Changelog format and capture automation are specified
- [ ] Emergency-change procedure and post-hoc review steps are captured
- [ ] Process-health metrics (review time, escape rate) are named

## What it contains

- Change classification (standard, normal, emergency) and routing rules
- Review SLA and minimum-reviewer requirements per class
- Merge-gate criteria and how the pipeline enforces them
- Changelog format and capture automation
- Emergency-change procedure and post-hoc review
- Metrics to monitor process health (review time, escape rate)

## Inputs you rely on

- Working CI/CD pipeline and pipeline security controls
- Deployment runbook
- Release Manager's cadence and release-window constraints
- Enterprise change-management policy (if applicable)
- Feature flag plan (flags change release-risk profile)

## Who consumes it

- Developers — operate within the process on every PR
- Release Manager — consumes curated changelog for release notes
- Security & Compliance — audits change controls and emergency changes
- SRE on-call — references changelog during incidents for recent-change correlation

## Common pitfalls

- Emergency channel abused for routine changes — process erodes
- Changelog generated but not curated — release notes become noise
- Review SLA ignored, PRs sit for days, or approved without review under pressure
- No metrics, so drift is invisible until an incident

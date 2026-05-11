# Architect in Plan

You are here to make sure the technical runway exists before feature work starts — that the skills, enablers, telemetry, and flag strategy the approved architecture assumes are actually in place. Plan is where architecture stops being a document and starts being infrastructure, instrumentation, and sequencing decisions the team can execute against.

## What you do

- Translate the architecture into skills & roles requirements so staffing matches what the design needs.
- Sequence technical milestones so enablers land in time for the features that depend on them.
- Define the enabler backlog with Developers so runway work is visible alongside feature work.
- Plan analytics & telemetry instrumentation so KPIs, SLOs, and experiments have data from day one.
- Set feature flag strategy with Developers so progressive delivery and rollback are options, not afterthoughts.
- Partner with the Sponsor to resolve cross-portfolio priority conflicts when your capacity fights another initiative's.

## Artifacts you own

- [skills requirement input](artifacts/skills-requirement-input.md) — what the design requires of the team.
- [technical milestone plan](artifacts/technical-milestone-plan.md) — sequencing of enablers and features.
- [enabler backlog](artifacts/enabler-backlog.md) — co-owned with Developer.
- [telemetry plan](artifacts/telemetry-plan.md) — what's instrumented, where, and why.
- [feature flag plan](artifacts/feature-flag-plan.md) — co-owned with Developer.

## Artifacts you contribute to

You don't contribute to other-owned artifacts this phase — your outputs are the enabler and instrumentation substrate others rely on.

## Outcomes you drive

- [portfolio priority decision](outcomes/portfolio-priority-decision.md) — co-owned with Product Sponsor; you frame the technical trade-offs.

## Who you work with

- **Developer** — co-owns the enabler backlog and feature flag plan; you set patterns, they build against them.
- **Product Sponsor** — arbitrates portfolio conflicts you surface; you bring the technical impact framing.
- **Site Reliability Engineer** — consumes your telemetry plan and milestone sequencing into environments and pipeline.
- **Product Owner** — negotiates enabler-vs-feature sequence with you.

## Handoff into [Build](../5-build/README.md)

In Build you stop planning runway and start guarding conformance. You know Plan is done when the enabler backlog is in flight, telemetry and flag plans are wired into the pipeline, and engineers know what patterns to reach for. In Build you shift to design guidance, conformance reviews, and unblocking technical impediments.

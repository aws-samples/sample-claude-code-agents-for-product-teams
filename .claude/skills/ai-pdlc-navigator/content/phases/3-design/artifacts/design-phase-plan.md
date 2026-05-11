# design-phase plan

_Produced by: Design-phase schedule & resource coordination_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Project Manager

**Stakeholders:** _(none listed)_

## What this is

The PM's working plan for running the Design phase — milestones, reviews, owners, dependencies, and risks — parallel to the Define-phase [initial project brief](../../1-discover/artifacts/initial-project-brief.md) but tuned for the Design-specific cadence.

## Why it matters for the Project Manager

You produce this to coordinate the many concurrent Design streams (UX, architecture, security, vendor selection, BA validation) without dropping hand-offs. Design is where parallelism is high and dependencies are dense; a plan keeps the phase from stretching into the calendar allocated for Build.

## Definition of Done

- [ ] Every design track (UX, architecture, data, API, security, vendor) has a named lead.
- [ ] Milestones have target dates and cross-stream dependencies mapped.
- [ ] Review cadence (design, architecture, gate) is scheduled.
- [ ] Design-specific risks are enumerated with owners.
- [ ] Exit criteria for the Design gate are stated unambiguously.

## What it contains

- Design-phase milestones and target dates
- Each design track (UX, architecture, data, API, security, vendor) with lead and dependencies
- Review cadence (design reviews, architecture reviews, gate review)
- Risks specific to Design (late feasibility finding, vendor slip, usability findings)
- Resource calendar across contributors
- Decision-making cadence and escalation path
- Exit criteria for the Design gate

## Inputs you rely on

- [Draft project schedule](../../2-define/artifacts/draft-project-schedule.md) and [dependency list](../../2-define/artifacts/dependency-list.md)
- Contributor availability and portfolio calendar
- [Stakeholder map](../../1-discover/artifacts/stakeholder-map.md) for review attendance

## Who consumes it

- Design-phase contributors — use it to plan their weeks
- Product Sponsor — sees the phase shape and gate date
- Architect, UI/UX Designer, Security & Compliance — align their streams to it
- Project Manager (future you) — feeds it into the Plan-phase baseline

## Common pitfalls

- Plan drawn once, never re-baselined as streams slip
- Missing cross-stream dependencies (e.g., API spec blocks test design)
- Single-point-of-failure reviews with no backup reviewer
- Exit criteria defined loosely, so "done" is a negotiation at gate time

# technical impact analysis

_Produced by: Technical impact of scope changes_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

The Architect's analysis of the technical consequences of a proposed scope change — what components, NFRs, integrations, and ADRs it touches, plus risk, effort, and sequence implications. Parallel to the BA's change impact report but on the engineering side.

## Why it matters for the Architect

Scope changes that look small to the PO can blow a hole in the architecture — cache assumptions, consistency models, throughput budgets. Your analysis keeps those consequences visible so the change is either sized honestly or deferred until it fits.

## Definition of Done

- [ ] Affected components and services are listed
- [ ] NFR exposure across perf, scale, availability, and security is stated with magnitude
- [ ] Integration or contract impact on other teams is named
- [ ] ADRs to revisit are identified
- [ ] Engineering effort estimate includes sequence disruption and mitigation options

## What it contains

- Components and services affected
- NFR exposure (perf, scale, availability, security) with magnitude
- Integration or contract impact on other teams
- ADR revisit list
- Engineering effort estimate and sequence disruption
- Technical risk rating and mitigation options

## Inputs you rely on

- Change impact report from the BA
- Architecture document, ADRs, and integration map
- Technical milestone plan
- Dependency list and vendor commitments
- Conformance findings (for areas already strained)

## Who consumes it

- Project Manager — includes it in the change control package
- Product Sponsor and PO — decide change under full information
- Developer leads — plan the work if approved
- Security — reviews for compensating control needs

## Common pitfalls

- Effort-only view that ignores NFR and long-tail architectural debt
- "We can make it work" optimism without naming what breaks
- Skipping the analysis on "obvious" changes that carry non-obvious cost
- Analysis done but not fed into the change-control forum

# QA / Tester in Design

Design is where you update your Define-era test designs against the now-approved design. The requirements haven't changed much, but how they're realized has — and the difference matters for test design. Your job is to make sure every piece of design (UX flow, API, data model, security control) has planned test coverage before Build starts.

## What you do

- Update test designs against approved design — produce the [design-aligned test designs](artifacts/design-aligned-test-designs.md)
- Read the [design specification](artifacts/design-specification.md), [API specification](artifacts/api-specification.md), [data model](artifacts/data-model.md), and [threat model](artifacts/threat-model.md) — update tests accordingly
- Keep the test-to-requirement traceability current against the BA's updated traceability matrix

## Artifacts you own

- [design-aligned test designs](artifacts/design-aligned-test-designs.md) — the test designs refreshed against the approved design

## Outcomes you drive

You don't drive outcomes this phase — you input into the [approved design package](outcomes/approved-design-package.md) by making sure testability has been checked against the design.

## Who you work with

- **UI/UX Designer** — their design specs, prototypes, and usability findings shape your UI test coverage
- **Architect** — their API spec and data model are your API and data-test substrate
- **Security & Compliance** — their threat model and approved patterns drive your security test design
- **Business Analyst** — consumes your coverage back into the updated traceability matrix
- **Developer** — partner on what's automatable vs. what needs exploratory coverage

## Handoff into Plan

Your design-aligned test designs are the starting point for the [Plan](../4-plan/README.md)-phase test plan you'll own there, and for the security test plan you'll co-author with Security. The quality bar is that when Build starts, the team can write tests directly from your designs. You're done when every element of the approved design has planned coverage and the BA's traceability matrix lights up end-to-end.

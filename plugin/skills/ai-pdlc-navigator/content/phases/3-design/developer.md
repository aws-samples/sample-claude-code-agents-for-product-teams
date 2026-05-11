# Developer in Design

Your involvement steps up this phase. You co-own the API specification with the Architect and the build-ready package with the Architect and UI/UX Designer — because the people who write the code need to shape the contract and the handoff. Push hard for clarity; an API spec or build-ready package you don't believe is buildable is a disaster waiting for Build.

## What you do

- Co-own the [API specification](artifacts/api-specification.md) with the Architect — the contracts you'll implement
- Co-own the [build-ready package](artifacts/build-ready-package.md) with the Architect and UI/UX Designer — the handoff you'll pick up in Build
- Review the [architecture document](artifacts/architecture-document.md), [data model](artifacts/data-model.md), and [integration map](artifacts/integration-map.md) — flag anything unbuildable
- Challenge the design specs and prototypes on buildability, performance, and maintainability

## Artifacts you own

You don't own any artifacts this phase — you contribute to others' (see below).

## Artifacts you contribute to

- [API specification](artifacts/api-specification.md) — owned by the Architect; you co-author the contract you'll implement
- [build-ready package](artifacts/build-ready-package.md) — owned by the UI/UX Designer with the Architect; you sign that the package is actually buildable

## Outcomes you drive

You don't drive outcomes this phase — you input into the approved design package and build-vs-buy decisions through buildability signal.

## Who you work with

- **Architect** — your primary partner on API spec and build-ready package
- **UI/UX Designer** — their design specs and prototype have to be translatable into code
- **QA/Tester** — their design-aligned test designs are what you'll be testing against

## Handoff into Plan

[Plan](../4-plan/README.md) is where you co-own the feature flag plan, enabler backlog, and CI/CD pipeline — and then Build is where you deliver. The quality bar in Design is that when you see the build-ready package, you can estimate it and start implementation without re-opening design questions. You're done when you've signed the build-ready package knowing it's buildable and when Plan can decompose it into work items cleanly.

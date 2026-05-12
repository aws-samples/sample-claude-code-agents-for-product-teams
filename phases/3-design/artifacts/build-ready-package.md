# build-ready package

_Produced by: Design → engineering handoff review_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** UI/UX Designer

**Stakeholders:** Architect, Developer

**Accelerated MVP:** slim — a shared folder with the screens, API spec, and ADRs is enough

## What this is

The curated set of design artifacts engineering needs to start building confidently — specs, mockups, tokens, acceptance criteria, and open-question log — packaged for handoff. It is the handoff moment between Design and the Plan / Build phases.

## Why it matters for the UI/UX Designer

You produce this because a great design that is hard to hand off becomes a worse product. A clean build-ready package keeps the team from re-asking questions you have already answered and limits the "developer interpretation" surface where quality quietly erodes.

## Definition of Done

- [ ] Links point to the canonical, current versions of the design spec, mockups, and IA spec.
- [ ] Component list references the design-system entries engineers will consume.
- [ ] Design tokens, assets, and icons are present and ready to use.
- [ ] Each screen / flow has acceptance criteria attached.
- [ ] Open questions list names a change-management contact for each entry.

## What it contains

- Pointers to latest [design specification](design-specification.md), [visual design mockups](visual-design-mockups.md), [IA spec](ia-spec.md)
- Component list with design-system references
- Design tokens, assets, and icons ready to consume
- Acceptance criteria per screen / flow
- Accessibility annotations and test cases
- Open questions and change-management contact
- Known deviations from the design system with rationale

## Inputs you rely on

- All Design-phase UX artifacts
- [Testable acceptance criteria](../../2-define/artifacts/testable-acceptance-criteria.md) from Define
- [Accessibility design report](accessibility-design-report.md)
- Architect's sign-off on feasibility

## Who consumes it

- Developer — implements from it
- Architect — validates design fits the architecture
- QA/Tester — maps test coverage to it
- Product Owner — signs off on the [approved design package](../outcomes/approved-design-package.md)

## Common pitfalls

- Dumping every draft file rather than curating the canonical set
- Outdated components still linked because the package was assembled once and not refreshed
- No "what's out of scope" note, so engineers invent behavior for unspecified areas
- Missing acceptance criteria per screen, collapsing back into requirements-only handoff

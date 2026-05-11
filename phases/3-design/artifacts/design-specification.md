# design specification

_Produced by: Create design specifications_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** UI/UX Designer

**Stakeholders:** _(none listed)_

## What this is

The detailed, screen-by-screen (or flow-by-flow) specification of UX behavior — component usage, states, validation, empty/error/loading behavior, microcopy, motion, and accessibility requirements. It is the engineering-grade UX contract.

## Why it matters for the UI/UX Designer

You produce this so the product that ships matches the product you designed. Mockups plus a specification is how you keep the fifty small decisions that separate a good product from a mediocre one from being made by whoever reaches that component first.

## Definition of Done

- [ ] Component inventory references the design-system source for each item.
- [ ] Every flow documents default, hover/focus, disabled, loading, empty, error, and success states.
- [ ] Validation rules and every microcopy string are specified (no "TBD").
- [ ] Responsive behavior and breakpoints are defined.
- [ ] Accessibility annotations (roles, labels, keyboard, contrast, focus order) are present per flow.

## What it contains

- Component inventory with design-system references
- Each flow with states: default, hover/focus, disabled, loading, empty, error, success
- Validation rules and microcopy (all strings)
- Responsive behavior and breakpoints
- Motion / animation specs and when they apply
- Accessibility: roles, labels, keyboard, contrast, focus order
- Tokens: colors, type, spacing, radii, elevation

## Inputs you rely on

- [IA spec](ia-spec.md) and [visual design mockups](visual-design-mockups.md)
- [Requirements document](../../2-define/artifacts/requirements-document.md) and [testable acceptance criteria](../../2-define/artifacts/testable-acceptance-criteria.md)
- Design system / component library
- Accessibility standards (WCAG level committed to)

## Who consumes it

- Developer — implements against it
- QA/Tester — builds visual and interaction test cases
- Technical Writer — aligns microcopy ownership
- UI/UX Designer (future you) — packages it into the [build-ready package](build-ready-package.md)

## Common pitfalls

- Happy-path only — missing empty, error, and loading states
- Microcopy "TBD" that becomes developer-written by default
- Ambiguous responsive behavior that each engineer resolves differently
- Accessibility annotations bolted on after design rather than designed in

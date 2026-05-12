# IA spec

_Produced by: Information architecture_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** UI/UX Designer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the MVP has minimal navigation surface

## What this is

The information architecture of the product — navigation model, content hierarchy, taxonomy, labels, and search behavior. It is the skeleton on top of which visual design, content, and code all hang.

## Why it matters for the UI/UX Designer

You own IA because findability, not prettiness, is what separates usable products from unusable ones. Getting IA right up front prevents navigation-rewrite projects a year in and gives Technical Writing and Support a stable content map to plan against.

## Definition of Done

- [ ] Top-level navigation model is chosen with explicit rationale.
- [ ] Taxonomy uses a controlled vocabulary with rationale per label.
- [ ] Sitemap / screen hierarchy is complete for the MVP scope.
- [ ] Search model (scope, facets, ranking) is specified.
- [ ] URL / route structure is defined and accessibility landmarks / skip-links are covered.

## What it contains

- Top-level navigation model (flat / hierarchical / hybrid) and rationale
- Content inventory and taxonomy with controlled vocabulary
- Labeling system with rationale for each term
- Page / screen hierarchy and sitemap
- Search model: scope, facets, ranking behavior
- URL / route structure
- Accessibility considerations in navigation (landmarks, skip links, focus order)

## Inputs you rely on

- [Journey map / service blueprint](journey-map-service-blueprint.md)
- Card sorts and tree tests with target users
- [User personas](../../1-discover/artifacts/user-personas.md) for mental models
- Existing product IA if applicable and brand terminology standards

## Who consumes it

- UI/UX Designer (future you) — builds [design specification](design-specification.md) and [visual design mockups](visual-design-mockups.md) on it
- Technical Writer — aligns docs IA to product IA
- Developer — implements routing and navigation
- Customer Support — aligns knowledge-base taxonomy to product IA

## Common pitfalls

- Internal jargon in user-facing labels
- Navigation that mirrors the org chart rather than user tasks
- Untested taxonomy — assumed-obvious terms users don't use
- No URL plan, so SEO and deep-linking are hostages to fortune

# updated traceability matrix

_Produced by: Update traceability (requirements → design)_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the traceability matrix itself is optional

## What this is

The Define-era [traceability matrix](../../2-define/artifacts/traceability-matrix.md) extended with design-artifact links — each requirement now traces to the specific design doc, component, or API that realizes it. It is the backbone of "can we prove design covers requirements."

## Why it matters for the Business Analyst

You maintain it because traceability without design linkage is half the story. The updated matrix is what you hand auditors, what you use for change impact analysis, and what lets you spot "orphan design" (screens with no requirement) and "orphan requirements" (no design) in one pass.

## Definition of Done

- [ ] Every requirement links to the specific design artifact / section that realizes it.
- [ ] Each requirement names the component, API, or screen that implements it.
- [ ] Security-relevant requirements link to their threat-model entry.
- [ ] Each requirement points to its Build-ready test design.
- [ ] Coverage gaps are flagged with severity.

## What it contains

- All Define-era columns plus:
- Design artifact / section reference per requirement
- Component, API, or screen realizing each requirement
- Threat-model entry where applicable
- Test design pointer ready for Build
- Coverage gap flags by severity

## Inputs you rely on

- [Traceability matrix](../../2-define/artifacts/traceability-matrix.md) as the starting point
- [Architecture document](architecture-document.md), [design specification](design-specification.md), [API specification](api-specification.md)
- [Design-requirements validation](design-requirements-validation.md)
- [Design-aligned test designs](design-aligned-test-designs.md) in progress

## Who consumes it

- Security & Compliance — audit evidence and DPIA support
- Architect — validates design completeness
- Project Manager — uses for change impact in Build
- QA/Tester — uses to align tests to requirements and design

## Common pitfalls

- Matrix maintenance deferred until phase gates — drifts and becomes unreliable
- Links to high-level documents without section anchors, making traceability lookup slow
- No flags for gaps; the matrix becomes decorative
- Treating it as write-only; it should be actively read during change impact analysis

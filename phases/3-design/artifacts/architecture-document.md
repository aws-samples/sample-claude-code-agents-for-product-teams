# architecture document

_Produced by: Document solution architecture_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — a one-page overview plus ADRs is enough

## What this is

The authoritative description of the solution architecture — components, responsibilities, interactions, data flows, deployment topology, and the NFRs each decision honors. It is the diagram-and-narrative pack an engineer can build from.

## Why it matters for the Architect

You own this because it is the single artifact that aligns every engineer's mental model with the shape they are supposed to build. Without a shared architecture document, implementations drift into divergent interpretations and the conformance review in Build becomes a brawl.

## Definition of Done

- [ ] Context, container, and component views are all present with responsibilities named.
- [ ] Each NFR has a named location where the design delivers it.
- [ ] Deployment topology and environment strategy are documented.
- [ ] Cross-cutting concerns (auth, observability, config, error handling) are addressed explicitly.
- [ ] Every material decision links out to a decision-log / ADR entry with alternatives and trade-offs.

## What it contains

- Context (system-of-systems) and container views
- Component view with responsibilities and tech choices
- Data flows including sensitive-data paths
- Deployment topology and environment strategy
- NFR response: where the design delivers each NFR
- Cross-cutting concerns (auth, observability, config, error handling)
- Known constraints, trade-offs, and alternatives rejected
- Link out to [decision log](../outcomes/decision-log.md) for every material decision

## Inputs you rely on

- [Technical options assessment](technical-options-assessment.md) and [integration map](integration-map.md)
- [NFR document](../../2-define/artifacts/nfr-document.md) and [security control requirements](../../2-define/artifacts/security-control-requirements.md)
- [Data model](data-model.md) and [API specification](api-specification.md)
- Platform standards and reference architectures

## Who consumes it

- Developer — builds from it and references it at code review
- Security & Compliance — drives [threat model](threat-model.md) from it
- SRE — derives capacity, observability, and deployment plans
- Architect (future you) — maintains it through Build via [updated ADRs](../../5-build/artifacts/updated-adrs.md) and conformance findings

## Common pitfalls

- Box-and-line diagrams without behavior — pretty but unbuildable
- Missing NFR response per decision, so "why this way" is lost
- No deployment view, so operational cost and failure modes are invisible
- Treated as a Design-phase artifact rather than a living document

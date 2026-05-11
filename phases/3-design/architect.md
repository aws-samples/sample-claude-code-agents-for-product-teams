# Architect in Design

This is your phase. You turn the approved requirements and NFRs into a build-ready technical design — architecture, data model, APIs, integrations, ADRs — and you co-sign the executive approval and build-vs-buy with the Sponsor. You also co-own the threat model, security patterns, and security/compliance approval with Security & Compliance and SRE. If the architecture is wrong here, every downstream phase pays for it.

## What you do

- Research technical options — publish the [technical options assessment](artifacts/technical-options-assessment.md)
- Document solution architecture — own the [architecture document](artifacts/architecture-document.md)
- Architecture decision records — maintain the [decision log](outcomes/decision-log.md)
- Integration / system context map — publish the [integration map](artifacts/integration-map.md)
- Data model / schema design — own the [data model](artifacts/data-model.md)
- API / interface contract design — co-own the [API specification](artifacts/api-specification.md) with the Developer
- Co-own threat model, security patterns, and security/compliance approval with Security & Compliance
- Co-own build-vs-buy, executive approval, and the build-ready package at the technical level

## Artifacts you own

- [technical options assessment](artifacts/technical-options-assessment.md) — weighed options with trade-offs and a recommendation
- [architecture document](artifacts/architecture-document.md) — the canonical architecture view
- [integration map](artifacts/integration-map.md) — all integrations with protocols, owners, and SLAs
- [data model](artifacts/data-model.md) — logical and physical model with classification
- [API specification](artifacts/api-specification.md) — interface contracts (co-owned with Developer)

## Artifacts you contribute to

- [threat model](artifacts/threat-model.md) — owned by Security & Compliance; you bring system context and trust boundaries
- [build-ready package](artifacts/build-ready-package.md) — owned by UI/UX Designer; you attach architecture, APIs, data model
- [vendor evaluation scorecard](artifacts/vendor-evaluation-scorecard.md) — owned by the BA; you bring technical fit scoring

## Outcomes you drive

- [decision log](outcomes/decision-log.md) — the ADR trail for every architectural commitment
- [build-vs-buy decision](outcomes/build-vs-buy-decision.md) — co-owned with the Sponsor
- [architecture executive approval](outcomes/architecture-executive-approval.md) — co-owned with the Sponsor
- [approved security patterns](outcomes/approved-security-patterns.md) — co-owned with Security & Compliance
- [security/compliance approval](outcomes/security-compliance-approval.md) — co-owned with Security & Compliance and SRE

## Who you work with

- **Security & Compliance** — co-owns threat model, security patterns, and compliance approval with you
- **Site Reliability Engineer** — co-owns security/compliance approval with you; their reliability posture shapes your architecture
- **Developer** — co-owns API spec and build-ready package with you; they're your build partner
- **UI/UX Designer** — co-owns the build-ready package with you; their design has to fit your architecture
- **Product Sponsor** — co-owns build-vs-buy and executive approval with you
- **Business Analyst** — co-owns vendor evaluation with you; their requirements anchor your architecture

## Handoff into Plan

Your Design artifacts are the architectural foundation for [Plan](../4-plan/README.md) — technical milestone sequencing, enabler backlog, telemetry plan, feature-flag plan, skills requirement input. The quality bar is that every architecture decision is documented as an ADR, every NFR has a design answer, and every integration has a named owner. You're done when Plan can stand up pipelines and environments, and Build can begin without architectural ambiguity.

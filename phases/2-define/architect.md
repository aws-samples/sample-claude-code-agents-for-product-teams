# Architect in Define

You are here to make sure the requirements being approved are actually buildable at the cost, speed, and quality the business case assumes. Define is where NFRs get real, where system context gets drawn, and where the solution recommendation sets the direction Design will execute. You also co-sign the Define exit decision — your name is on the gate.

## What you do

- System context overlay on processes — produce the [system-to-process map](artifacts/system-to-process-map.md)
- Requirements technical feasibility review — publish [technical feasibility findings](artifacts/technical-feasibility-findings.md)
- Non-functional requirements definition — own the [NFR document](artifacts/nfr-document.md) with the BA
- Dependency mapping — produce the [dependency list](artifacts/dependency-list.md) with the PM
- Co-own solution evaluation, change impact, gap analysis, and data requirements with the BA
- Co-sign the Define exit decision and the commercial/delivery model decision

## Artifacts you own

- [system-to-process map](artifacts/system-to-process-map.md) — where each to-be process lands on the system landscape
- [technical feasibility findings](artifacts/technical-feasibility-findings.md) — which requirements are risky or costly, with options
- [NFR document](artifacts/nfr-document.md) — performance, availability, security, scale, cost, observability (co-owned with BA)
- [dependency list](artifacts/dependency-list.md) — cross-team, cross-system, vendor (co-owned with PM)

## Artifacts you contribute to

- [commercial model decision](outcomes/commercial-model-decision.md) — owned by the Sponsor, you bring the technical implications of delivery-model choices
- [data inventory & classification](artifacts/data-inventory-classification.md) — owned by the BA, you co-author the technical/data classification side
- [solution recommendation](artifacts/solution-recommendation.md) — owned by the BA, you bring the technical options and trade-offs
- [change impact assessment](artifacts/change-impact-assessment.md) — owned by the BA, you scope the technical/integration impact
- [capability gap report](artifacts/capability-gap-report.md) — owned by the BA, you name the technical gaps

## Outcomes you drive

- [Define exit decision](outcomes/define-exit-decision.md) — co-owned with the Sponsor; your signature says the requirements and NFRs are buildable

## Who you work with

- **Business Analyst** — your primary partner; requirements only hold together when they're technically coherent
- **Product Sponsor** — co-owner of the exit decision; you bring technical fit and risk
- **Project Manager** — co-owns dependency mapping with you; your dependencies feed their schedule
- **Security & Compliance** — their control requirements become your NFR and design input
- **Developer** — their estimation in Define tells you whether your NFRs are affordable

## Handoff into Design

Your Define artifacts are the brief for your own Design work. [Design](../3-design/README.md) is where you produce the architecture document, data model, APIs, integration map, and decision log — and they all have to satisfy the NFRs you wrote here. The quality bar is that the exit decision is based on evidence, not vibes: every must-have NFR has a measurement method and a rough cost. You're done when Design can begin without needing to renegotiate scope or NFRs.

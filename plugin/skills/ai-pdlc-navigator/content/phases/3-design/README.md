# Phase 3: Design

**Goal:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

## Where this fits

Design picks up where [Define](../2-define/README.md) exits and prepares the conditions for [Plan](../4-plan/README.md). Every artifact and outcome in this phase is produced because a later phase depends on it.

## What happens in this phase

Design turns approved requirements into a build-ready package — UX, solution architecture, data model, API contracts, threat model, and a vendor decision if applicable. It's the last cheap phase to change direction. Discovering at Plan or Build that the design can't scale, can't meet NFRs, or can't be audited is an expensive mistake.

Design is carried jointly by the **Architect** (solution architecture, ADRs, data model, APIs, integration map, feasibility), **UI/UX Designer** (journey map, IA, specs, visual design, prototype, usability findings, accessibility review), and **Security & Compliance** (threat modeling, secure patterns, vendor security review). The **Business Analyst** validates design against requirements and maintains traceability. The **Product Sponsor** ratifies architecture, build-vs-buy, risk appetite, budget, and any vendor partnership. **QA/Tester** updates test designs against the approved design. **Project Manager** coordinates design reviews, vendor selection, and the decision log.

Design ends with an [approved design package](outcomes/approved-design-package.md) and [architecture executive approval](outcomes/architecture-executive-approval.md). Engineering must be signed off to build.

## Deliverables

- **[`artifacts/`](artifacts/)** — 24 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 11 decisions or state changes.

See the [Design activities list in the master flow](../../AI-PDLC-linear-flow.md#3-design) for the full activity-by-activity view.

## Role-specific briefs

| Role | Brief |
|------|-------|
| Product Sponsor | [product-sponsor.md](product-sponsor.md) |
| Product Owner | [product-owner.md](product-owner.md) |
| Business Analyst | [business-analyst.md](business-analyst.md) |
| UI/UX Designer | [ui-ux-designer.md](ui-ux-designer.md) |
| Architect | [architect.md](architect.md) |
| Security & Compliance | [security-compliance.md](security-compliance.md) |
| Site Reliability Engineer | [site-reliability-engineer.md](site-reliability-engineer.md) |
| Project Manager | [project-manager.md](project-manager.md) |
| Developer | [developer.md](developer.md) |
| QA / Tester | [qa-tester.md](qa-tester.md) |
| Release Manager | [release-manager.md](release-manager.md) |
| Technical Writer | [technical-writer.md](technical-writer.md) |
| Sales & Marketing | [sales-marketing.md](sales-marketing.md) |
| Customer Support | [customer-support.md](customer-support.md) |

## Exit checklist

Ready to enter [Plan](../4-plan/README.md) when all of the following are true:

- [ ] [accessibility design report](artifacts/accessibility-design-report.md) — Every finding cites the specific WCAG success criterion it relates to.
- [ ] [API specification](artifacts/api-specification.md) — Spec is captured in a machine-readable source (OpenAPI / AsyncAPI), not narrative only.
- [ ] [architecture document](artifacts/architecture-document.md) — Every material decision links out to a decision-log / ADR entry with alternatives and trade-offs.
- [ ] [build-ready package](artifacts/build-ready-package.md) — Each screen / flow has acceptance criteria attached.
- [ ] [business-rules catalog](artifacts/business-rules-catalog.md) — Each rule has a unique ID, plain-language statement, and precise formulation.
- [ ] [data model](artifacts/data-model.md) — Every entity has keys, cardinality, and constraints defined.
- [ ] [design-aligned test designs](artifacts/design-aligned-test-designs.md) — Test designs cover every flow, API, and NFR in the design package.
- [ ] [design-phase plan](artifacts/design-phase-plan.md) — Exit criteria for the Design gate are stated unambiguously.
- [ ] [design-requirements validation](artifacts/design-requirements-validation.md) — Every committed requirement has a coverage status in the design.
- [ ] [design specification](artifacts/design-specification.md) — Every flow documents default, hover/focus, disabled, loading, empty, error, and success states.
- [ ] [IA spec](artifacts/ia-spec.md) — Sitemap / screen hierarchy is complete for the MVP scope.
- [ ] [integration map](artifacts/integration-map.md) — Failure modes and fallback / degradation strategy are documented per integration.
- [ ] [interactive prototype](artifacts/interactive-prototype.md) — Core happy-path flows are clickable end-to-end.
- [ ] [journey map / service blueprint](artifacts/journey-map-service-blueprint.md) — Front-stage and back-stage actions are both represented.
- [ ] [technical options assessment](artifacts/technical-options-assessment.md) — At least three credible options are evaluated, not just preferred vs. straw-man.
- [ ] [threat model](artifacts/threat-model.md) — Every threat has a mitigation or an explicit acceptance decision.
- [ ] [updated ROI model](artifacts/updated-roi-model.md) — Delta vs. the approved business case is stated with rationale.
- [ ] [updated traceability matrix](artifacts/updated-traceability-matrix.md) — Every requirement links to the specific design artifact / section that realizes it.
- [ ] [usability findings](artifacts/usability-findings.md) — Each issue has a severity rating with recommended design change.
- [ ] [validated business-value alignment](artifacts/validated-business-value-alignment.md) — A decision (continue / resize / re-baseline / kill) is recorded.
- [ ] [vendor evaluation scorecard](artifacts/vendor-evaluation-scorecard.md) — TCO is computed over a 3-5 year horizon including exit cost.
- [ ] [vendor risk assessment](artifacts/vendor-risk-assessment.md) — Residual risk and acceptance recommendation are stated.
- [ ] [vendor selection process outputs](artifacts/vendor-selection-process-outputs.md) — Final decision captures rationale and any dissents.
- [ ] [visual design mockups](artifacts/visual-design-mockups.md) — Mockups apply design-system tokens rather than one-off values.
- [ ] [approved design package](outcomes/approved-design-package.md) — Design leadership and the Product Owner have signed off in writing.
- [ ] [approved security patterns](outcomes/approved-security-patterns.md) — Every deviation or custom pattern has a written justification.
- [ ] [architecture executive approval](outcomes/architecture-executive-approval.md) — Architecture document and ADRs are approved and version-locked.
- [ ] [build-vs-buy decision](outcomes/build-vs-buy-decision.md) — A build / buy / partner / reuse decision is recorded for every material capability.
- [ ] [confirmed scope/budget or change request](outcomes/confirmed-scope-budget-or-change-request.md) — The document states clearly whether scope/budget are confirmed or changed.
- [ ] [decision log from design reviews](outcomes/decision-log-from-design-reviews.md) — Log is kept as a single canonical source, not scattered across minutes.
- [ ] [decision log](outcomes/decision-log.md) — Every significant architecture decision has its own ADR entry.
- [ ] [ratified risk decisions](outcomes/ratified-risk-decisions.md) — Every risk has a classification and chosen response (accept / mitigate / transfer / avoid).
- [ ] [security/compliance approval](outcomes/security-compliance-approval.md) — Conditions and required mitigations before launch are listed.
- [ ] [steering checkpoint](outcomes/steering-checkpoint.md) — Continuation (or redirection) of the initiative is stated explicitly.
- [ ] [vendor partnership agreement](outcomes/vendor-partnership-agreement.md) — The agreement is signed or formally committed, not verbal.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

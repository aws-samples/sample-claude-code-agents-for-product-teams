# approved security patterns

_Produced by: Secure design pattern selection_

**Primary owner:** Security & Compliance

**Stakeholders:** Architect

**Accelerated MVP:** slim — "we're using the platform's defaults" is a valid approved pattern

## What this is

Security & Compliance and Architecture have agreed which of the enterprise's paved-road security patterns apply to this product (auth, secrets, encryption, network, logging).

## Why it matters

Pattern selection up front avoids reinventing security per feature, makes audits repeatable, and keeps the build on the paved road where tooling and automation already exist.

## What it contains

- Named patterns to use, with references to enterprise catalog
- Deviations or custom patterns with justification
- Expected controls and evidence per pattern

## Definition of Done

- [ ] Selected patterns are named and linked to the enterprise catalog.
- [ ] Every deviation or custom pattern has a written justification.
- [ ] Expected controls and the evidence shape are listed per pattern.
- [ ] Security & Compliance and Architecture have both signed off.

## Entry criteria

- Threat model drafted
- Data classification confirmed
- Applicable regulations identified

## Exit signal

Developers and SREs know which templates and libraries to use and what the pipeline will enforce.

## Supporting artifacts (this phase)

- [validated business-value alignment](../artifacts/validated-business-value-alignment.md)
- [technical options assessment](../artifacts/technical-options-assessment.md)
- [architecture document](../artifacts/architecture-document.md)
- [integration map](../artifacts/integration-map.md)
- [data model](../artifacts/data-model.md)
- [API specification](../artifacts/api-specification.md)
- [threat model](../artifacts/threat-model.md)
- [journey map / service blueprint](../artifacts/journey-map-service-blueprint.md)
- [IA spec](../artifacts/ia-spec.md)
- [design specification](../artifacts/design-specification.md)
- [visual design mockups](../artifacts/visual-design-mockups.md)
- [interactive prototype](../artifacts/interactive-prototype.md)
- [usability findings](../artifacts/usability-findings.md)
- [accessibility design report](../artifacts/accessibility-design-report.md)
- [build-ready package](../artifacts/build-ready-package.md)
- [design-requirements validation](../artifacts/design-requirements-validation.md)
- [updated traceability matrix](../artifacts/updated-traceability-matrix.md)
- [vendor evaluation scorecard](../artifacts/vendor-evaluation-scorecard.md)
- [business-rules catalog](../artifacts/business-rules-catalog.md)
- [updated ROI model](../artifacts/updated-roi-model.md)
- [design-aligned test designs](../artifacts/design-aligned-test-designs.md)
- [vendor risk assessment](../artifacts/vendor-risk-assessment.md)
- [design-phase plan](../artifacts/design-phase-plan.md)
- [vendor selection process outputs](../artifacts/vendor-selection-process-outputs.md)

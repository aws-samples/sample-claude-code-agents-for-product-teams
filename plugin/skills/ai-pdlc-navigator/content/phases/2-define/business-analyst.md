# Business Analyst in Define

This is your heaviest-lift phase. You turn a validated opportunity into approved, testable, traceable requirements — the spine of everything that follows. If the requirements are fuzzy, the tests are fuzzy, the estimates are fuzzy, and the deliverables miss. Your job is to make the requirements so sharp that "are we done?" has one answer per item.

## What you do

- Draft requirements — produce the [requirements document](artifacts/requirements-document.md)
- Review & iterate on requirements — drive them to [approved requirements](outcomes/approved-requirements.md)
- Acceptance criteria authoring — pair with QA on [testable acceptance criteria](artifacts/testable-acceptance-criteria.md)
- Data requirements & classification — work with the Architect on [data inventory & classification](artifacts/data-inventory-classification.md)
- Requirements traceability matrix — own the [traceability matrix](artifacts/traceability-matrix.md)
- Solution options evaluation — partner with the Architect on the [solution recommendation](artifacts/solution-recommendation.md)
- Business process modeling (as-is / to-be) — publish [process models](artifacts/process-models.md)
- Change impact analysis — produce the [change impact assessment](artifacts/change-impact-assessment.md) with the Architect
- Gap analysis — produce the [capability gap report](artifacts/capability-gap-report.md) with the Architect
- Contribute to NFRs and applicable regulations

## Artifacts you own

- [requirements document](artifacts/requirements-document.md) — the canonical requirements set
- [testable acceptance criteria](artifacts/testable-acceptance-criteria.md) — Gherkin-style or equivalent, each trivially testable (co-owned with QA)
- [data inventory & classification](artifacts/data-inventory-classification.md) — what data, from where, under what classification (co-owned with Architect)
- [traceability matrix](artifacts/traceability-matrix.md) — requirement → test → control linkage
- [solution recommendation](artifacts/solution-recommendation.md) — options weighed, choice justified (co-owned with Architect)
- [process models](artifacts/process-models.md) — as-is/to-be flows
- [change impact assessment](artifacts/change-impact-assessment.md) — who and what changes because of this (co-owned with Architect)
- [capability gap report](artifacts/capability-gap-report.md) — what we have vs. what we need (co-owned with Architect)

## Artifacts you contribute to

- [NFR document](artifacts/nfr-document.md) — owned by the Architect, you bring business-derived non-functional expectations
- [applicable-regulations list](artifacts/applicable-regulations-list.md) — owned by Security & Compliance, you help translate business scope into regulatory scope

## Outcomes you drive

- [approved requirements](outcomes/approved-requirements.md) — the cross-functionally reviewed and approved set that Design will build against

## Who you work with

- **Architect** — primary partner on data, solution options, change impact, gap analysis, and NFRs
- **QA/Tester** — pairs on acceptance criteria and the test-to-requirement coverage map
- **Security & Compliance** — you help scope regulations and data classification; they derive control requirements
- **Product Owner** — consumes your approved requirements into MVP scope and the roadmap
- **Project Manager** — runs workshops where your requirements get stress-tested

## Handoff into Design

Approved requirements, acceptance criteria, and the traceability matrix are what [Design](../3-design/README.md) builds against and what you'll update when design choices land. The quality bar is that every requirement is unambiguous, sized, owned, testable, and traceable — no "the system shall be fast" language. You're done when Design can quote any requirement number and know exactly what success looks like, and when the all-roles sign-off happens without rework.

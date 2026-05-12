# applicable-regulations list

_Produced by: Regulatory / compliance scope assessment_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Security & Compliance

**Stakeholders:** Business Analyst

**Accelerated MVP:** required — compliance scope doesn't get to be accelerated

## What this is

The definitive list of laws, regulations, standards, and contractual obligations the product must comply with, promoted from the Discover [regulatory risk flag](../../1-discover/artifacts/regulatory-risk-flag.md). For each, it names the specific controls, evidence, and audit cadence implied.

## Why it matters for the Security & Compliance owner

You produce this so the compliance surface is decided before the architecture is locked in. A regulation discovered after Design is a re-design; made explicit in Define, it becomes a constraint the team can build to.

## Definition of Done

- [ ] Each entry names the regulation or standard, its jurisdiction, and the applicability trigger
- [ ] Specific clauses or controls that apply are distinguished from those that do not
- [ ] Attestation or audit requirements include a cadence
- [ ] Third-party and vendor flow-down obligations are captured
- [ ] Open questions and pending legal determinations are listed with the required decision

## What it contains

- Each regulation / standard with jurisdiction, scope, and applicability trigger
- Specific clauses / controls that apply and those that do not
- Attestation or audit requirements and cadence
- Data subject rights and response timelines
- Third-party / flow-down obligations on vendors
- Open questions and pending legal determinations

## Inputs you rely on

- [Regulatory risk flag](../../1-discover/artifacts/regulatory-risk-flag.md) and [data-sensitivity flag](../../1-discover/artifacts/data-sensitivity-flag.md)
- [Data inventory & classification](data-inventory-classification.md)
- Legal counsel for ambiguous scope
- Corporate control framework or compliance register

## Who consumes it

- Security & Compliance (future you) — derives [security control requirements](security-control-requirements.md) and the [privacy impact assessment](privacy-impact-assessment.md)
- Architect — factors residency, encryption, and logging into design
- Business Analyst — adds compliance-derived rows to the [traceability matrix](traceability-matrix.md)
- Product Sponsor — sees the regulatory cost on the bet

## Common pitfalls

- Listing the regulation without identifying which clauses apply — treats everything as in-scope
- Missing sub-regimes (state privacy laws, sector-specific data rules)
- Ignoring flow-down to vendors, making vendor selection later a compliance scramble
- No owner per regulation; nobody watches for regulatory changes

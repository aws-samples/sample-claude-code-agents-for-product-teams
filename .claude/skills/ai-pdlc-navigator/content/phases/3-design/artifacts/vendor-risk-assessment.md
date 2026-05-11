# vendor risk assessment

_Produced by: Vendor security & compliance assessment_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

A security, privacy, and compliance assessment of each candidate (and selected) vendor — certifications, data handling, sub-processors, incident history, and contractual posture. It is the diligence record that makes "we did our due diligence" a defensible claim.

## Why it matters for the Security & Compliance owner

You produce this because vendor incidents become your incidents. Catching a weak SOC2 or a dubious sub-processor in Design is a conversation; catching it after go-live is an incident, a breach notification, and possibly a fine.

## Definition of Done

- [ ] Certifications and last-audit dates are recorded per vendor.
- [ ] Data categories handled and residency are documented.
- [ ] Sub-processor chain is enumerated with each party's attestations.
- [ ] Required contract clauses (DPA, flow-down, audit rights, SLA, exit) are listed.
- [ ] Residual risk and acceptance recommendation are stated.

## What it contains

- Vendor's certifications and last audit dates
- Data categories the vendor will handle and residency
- Sub-processor chain and its own attestations
- Security controls the vendor claims and evidence provided
- Incident history and breach-notification posture
- Contract clauses required (DPA, flow-down, audit rights, SLA, exit)
- Residual risk and acceptance recommendation

## Inputs you rely on

- [Vendor evaluation scorecard](vendor-evaluation-scorecard.md)
- [Data inventory & classification](../../2-define/artifacts/data-inventory-classification.md) and [applicable-regulations list](../../2-define/artifacts/applicable-regulations-list.md)
- Vendor's questionnaire responses and evidence
- [Security control requirements](../../2-define/artifacts/security-control-requirements.md)

## Who consumes it

- Procurement / Legal — negotiates DPA and contract clauses
- Architect — understands trust-boundary implications for [threat model](threat-model.md)
- Product Sponsor — ratifies at the [vendor partnership agreement](../outcomes/vendor-partnership-agreement.md)
- Security & Compliance (future you) — monitors vendor posture in Operate

## Common pitfalls

- Accepting the vendor's SOC2 cover page without reading the report
- Ignoring the sub-processor chain; that is where breaches start
- No exit-plan assessment — vendor lock-in becomes a risk you cannot retire
- One-time assessment, no recurring review cadence

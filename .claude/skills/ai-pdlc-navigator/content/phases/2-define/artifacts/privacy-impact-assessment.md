# privacy impact assessment

_Produced by: Privacy / DPIA assessment_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

A structured assessment of how the product collects, uses, shares, retains, and safeguards personal data, and the residual risks to data subjects. Under GDPR and similar regimes, a DPIA (data protection impact assessment) is a legal requirement for higher-risk processing.

## Why it matters for the Security & Compliance owner

You produce this so privacy is designed in, not bolted on. A completed PIA / DPIA is also the record you show regulators — without one, the regulator assumes the worst; with one, you have evidence of diligence even when an incident occurs.

## Definition of Done

- [ ] Processing description covers data categories, subjects, purposes, and lawful basis
- [ ] Data flow diagram highlights cross-border transfers
- [ ] Necessity and proportionality are assessed, not just asserted
- [ ] Risks to data subjects are listed with severity and mitigations mapped to controls
- [ ] Residual risk statement is signed off by a named risk owner

## What it contains

- Processing description: data categories, subjects, purposes, lawful basis
- Data flow diagrams with cross-border transfers highlighted
- Necessity and proportionality assessment
- Risks to data subjects (re-identification, access loss, profiling harm) with severity
- Mitigations mapped to controls
- Consultation record (DPO, legal, users where applicable)
- Residual risk and sign-off

## Inputs you rely on

- [Data inventory & classification](data-inventory-classification.md) and [applicable-regulations list](applicable-regulations-list.md)
- [Process models](process-models.md) and [system-to-process map](system-to-process-map.md)
- [Security control requirements](security-control-requirements.md)
- DPO or Privacy Counsel for jurisdictional specifics

## Who consumes it

- Security & Compliance (future you) — drives the [threat model](../../3-design/artifacts/threat-model.md) and carries DPIA into audit evidence
- Architect — translates mitigations into design choices
- Product Owner — sees where data minimization decisions are needed
- Regulator / auditor — examines on request

## Common pitfalls

- Treating DPIA as a checkbox; the analysis of necessity and proportionality is the point
- Missing cross-border flows hidden in vendor sub-processing
- No residual-risk statement with a named risk owner
- Written once and not refreshed when processing purposes change

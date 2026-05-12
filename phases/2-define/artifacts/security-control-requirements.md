# security control requirements

_Produced by: Security & compliance requirements derivation_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required when the data-sensitivity flag fires; otherwise slim to "standard platform controls"

## What this is

The specific security controls the product must implement, derived from regulations, data classification, threat exposure, and the org's control framework. Each control is expressed as a testable requirement the rest of the team can design and verify against.

## Why it matters for the Security & Compliance owner

You produce this because generic "be secure" instructions don't survive contact with an engineering team. Translating regulation and risk into discrete, assigned, testable controls is how security becomes a built-in attribute instead of a last-mile negotiation.

## Definition of Done

- [ ] Each control has an ID, title, and a testable statement
- [ ] Each control identifies its source (regulation / standard / internal policy / threat)
- [ ] Implementation guidance (pattern, library, or standard) is named per control
- [ ] Evidence required to prove the control and its verification method are specified
- [ ] Each control names an owner role and a residual-risk statement if weakened

## What it contains

- Control ID, title, and testable statement
- Source (regulation, standard, internal policy, threat-derived)
- Implementation guidance (pattern, library, or standard to use)
- Evidence required to prove the control is in place
- Owner role and verification method
- Residual risk if the control is weakened

## Inputs you rely on

- [Applicable-regulations list](applicable-regulations-list.md) and [data inventory & classification](data-inventory-classification.md)
- [NFR document](nfr-document.md) and draft [privacy impact assessment](privacy-impact-assessment.md)
- Org's control framework (ISO 27001, SOC2, NIST, internal) and secure pattern library
- Early threat sketches (pre-formal threat model)

## Who consumes it

- Architect — selects patterns and stack choices to meet controls
- Developer — implements and attests to controls in code
- QA/Tester — builds security test cases via the [control-to-test coverage map](control-to-test-coverage-map.md)
- Security & Compliance (future you) — carries controls into [threat model](../../3-design/artifacts/threat-model.md) and [approved security patterns](../../3-design/outcomes/approved-security-patterns.md)

## Common pitfalls

- Lifted control text verbatim from frameworks — not actionable by engineers
- No evidence column, so audit time becomes a scavenger hunt
- Mixing preventive, detective, and compensating controls without labeling
- Over-specifying vendor-specific tooling; controls should be tool-agnostic where possible

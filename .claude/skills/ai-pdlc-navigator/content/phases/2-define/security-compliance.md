# Security & Compliance in Define

This is where your Discover flags turn into actual scope. You name the regulations, derive the controls, run the privacy assessment, and confirm data classification — the regulatory posture of the entire initiative is decided here. Get this right and Design/Build can move fast within clear guardrails; get it wrong and you're refactoring controls into the product after launch.

## What you do

- Regulatory / compliance scope assessment — produce the [applicable-regulations list](artifacts/applicable-regulations-list.md) with the BA
- Security & compliance requirements derivation — publish [security control requirements](artifacts/security-control-requirements.md)
- Map security controls to test cases — pair with QA on the [control-to-test coverage map](artifacts/control-to-test-coverage-map.md)
- Privacy / DPIA assessment — produce the [privacy impact assessment](artifacts/privacy-impact-assessment.md)
- Data classification confirmation — produce the [confirmed data classification](outcomes/confirmed-data-classification.md)

## Artifacts you own

- [applicable-regulations list](artifacts/applicable-regulations-list.md) — regimes in scope with rationale (co-owned with BA)
- [security control requirements](artifacts/security-control-requirements.md) — the controls the product must implement, derived from regs and risk
- [control-to-test coverage map](artifacts/control-to-test-coverage-map.md) — every control mapped to one or more tests (co-owned with QA)
- [privacy impact assessment](artifacts/privacy-impact-assessment.md) — DPIA where applicable, with mitigations

## Outcomes you drive

- [confirmed data classification](outcomes/confirmed-data-classification.md) — the ratified classification of the data the product will handle

## Who you work with

- **Business Analyst** — they anchor regulatory scope in business reality; you translate it into controls
- **QA/Tester** — they operationalize your controls as tests
- **Architect** — consumes your control requirements into the NFR document and Design-phase architecture
- **Product Sponsor** — needs to know the compliance posture to ratify the business case

## Handoff into Design

Your Define outputs drive the [Design](../3-design/README.md) threat model, security patterns, and security/compliance review you'll co-own with the Architect and SRE. The quality bar is that every control has an owner, a design path, and a test. You're done when the Architect can start architecture with clear guardrails, QA can plan control-validation coverage, and no regulatory ambiguity remains for the Sponsor's exit decision.

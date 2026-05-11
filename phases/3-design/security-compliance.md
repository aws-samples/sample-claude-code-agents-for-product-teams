# Security & Compliance in Design

This is where your control requirements become designed-in controls. You co-own the threat model, security patterns, and security/compliance approval with the Architect, and the vendor risk assessment is yours. The difference between "secure by design" and "bolt it on later" is decided in this phase — every pattern approved here is one you don't have to fight for in Build.

## What you do

- Threat modeling — produce the [threat model](artifacts/threat-model.md) with the Architect
- Secure design pattern selection — issue the [approved security patterns](outcomes/approved-security-patterns.md) with the Architect
- Security & compliance review — issue the [security/compliance approval](outcomes/security-compliance-approval.md) with the Architect and SRE
- Vendor security & compliance assessment — own the [vendor risk assessment](artifacts/vendor-risk-assessment.md)
- Co-own the [ratified risk decisions](outcomes/ratified-risk-decisions.md) with the Sponsor
- Contribute to the [design-requirements validation](artifacts/design-requirements-validation.md) with the BA

## Artifacts you own

- [threat model](artifacts/threat-model.md) — attacker-centric analysis with mitigations (co-owned with Architect)
- [vendor risk assessment](artifacts/vendor-risk-assessment.md) — per-vendor security and compliance due diligence

## Artifacts you contribute to

- [design-requirements validation](artifacts/design-requirements-validation.md) — owned by the BA; you cover control coverage vs. design

## Outcomes you drive

- [approved security patterns](outcomes/approved-security-patterns.md) — the agreed building blocks (co-owned with Architect)
- [security/compliance approval](outcomes/security-compliance-approval.md) — formal sign-off on the design from a controls perspective (co-owned with Architect and SRE)
- [ratified risk decisions](outcomes/ratified-risk-decisions.md) — owned by the Sponsor; you co-sign the residual risk acceptance

## Who you work with

- **Architect** — your primary partner this phase; threat model, patterns, and approval are joint
- **Site Reliability Engineer** — co-owns security/compliance approval with you; their posture shapes detection and response
- **Product Sponsor** — co-owns risk ratification with you
- **Business Analyst** — partners on design-requirements validation

## Handoff into Plan

Your Design outputs drive the [Plan](../4-plan/README.md)-phase security test plan, pipeline security controls, evidence collection plan, and IR runbook you'll own there. The quality bar is that every control has a design owner, a pattern, and a test path. You're done when Plan can wire security into the pipeline and Build can pick up secure-by-default patterns without re-litigating the controls.

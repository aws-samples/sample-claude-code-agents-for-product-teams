# pipeline security controls

_Produced by: Define security & compliance controls in pipeline_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — SAST and SCA in CI are cheap insurance

## What this is

The concrete set of security controls embedded in the CI/CD pipeline — scan types, thresholds, signing, attestations, secret detection, branch protection — and the automation that enforces them without human effort per PR.

## Why it matters for the Security & Compliance owner

Manual security reviews don't scale and get bypassed under deadline pressure. Codifying controls into the pipeline is how you get consistent enforcement, machine-readable evidence, and fewer "we skipped it this once" conversations — while keeping engineering velocity up.

## Definition of Done

- [ ] Control catalog maps each control back to its source requirement
- [ ] Tool configuration (rules, severity thresholds, allowlists) is specified per control
- [ ] Pipeline enforcement points (pre-merge, post-merge, pre-deploy) are named
- [ ] Artifact signing and provenance attestation requirements are stated
- [ ] Exception/waiver process and review cadence are defined
- [ ] Evidence-capture path for audit is documented

## What it contains

- Control catalog mapped to source (e.g., OWASP, SOC2, internal policy)
- Tool configuration for each control (rules, severity thresholds, allowlists)
- Pipeline enforcement points (pre-merge, post-merge, pre-deploy)
- Artifact signing and provenance attestation requirements
- Exception/waiver process and review cadence
- Evidence-capture path for audit

## Inputs you rely on

- Working CI/CD pipeline from SRE
- Security control requirements and applicable regulations
- Threat model
- Existing enterprise security tooling and policy
- Evidence collection plan

## Who consumes it

- SRE and Developers — operate in the pipeline these controls govern
- Release Manager — gates on the controls at promotion points
- Internal/external auditors — use captured evidence for attestation
- Security team members — operate waivers and investigate exceptions

## Common pitfalls

- Gates set so tight they break legitimate work, so engineering learns to waive them routinely
- No evidence capture — the control runs but the audit trail doesn't
- Running scans after merge only — bad code in main before anyone notices
- Overlapping tools producing duplicate findings and remediation fatigue

# Site Reliability Engineer in Design

You become an actual signatory this phase. You co-own the security/compliance approval with the Architect and Security because a secure design that can't be operated is still a bad design. Your job is to make sure the architecture being approved is observable, recoverable, and affordable at the NFR targets — because in Plan you'll be provisioning the environments and writing the SLOs against exactly this design.

## What you do

- Co-own the [security/compliance approval](outcomes/security-compliance-approval.md) with the Architect and Security & Compliance — your signature says the design is operable within the security posture
- Pressure-test the [architecture document](artifacts/architecture-document.md) and [integration map](artifacts/integration-map.md) for observability, capacity, and failure-domain clarity
- Input into the [technical options assessment](artifacts/technical-options-assessment.md) on run-cost and operability trade-offs
- Start sketching environments, pipeline shape, and SLO targets for Plan

## Artifacts you own

You don't own any artifacts this phase — you contribute to others' (see below).

## Artifacts you contribute to

- [architecture document](artifacts/architecture-document.md) — owned by the Architect; you bring observability, capacity, and failure-handling input
- [integration map](artifacts/integration-map.md) — owned by the Architect; you verify SLAs and failure modes with upstream/downstream owners
- [technical options assessment](artifacts/technical-options-assessment.md) — owned by the Architect; you sharpen run-cost and on-call implications

## Outcomes you drive

- [security/compliance approval](outcomes/security-compliance-approval.md) — co-owned with Architect and Security; your signature is the operability-and-security check

## Who you work with

- **Architect** — your primary partner; their architecture has to be operable
- **Security & Compliance** — co-signers on the security/compliance approval with you
- **Release Manager** — the release shape implied by this design will land on you both in Plan

## Handoff into Plan

[Plan](../4-plan/README.md) is your heavy phase — you'll own provisioned environments, CI/CD, SLOs, deployment runbook, and the changelog review process. Everything you sign off here in Design is what you'll operate against. The quality bar is that you can commit to SLOs against the approved architecture without asking for re-design. You're done when the security/compliance approval is signed with confidence and you have a clear shape for Plan.

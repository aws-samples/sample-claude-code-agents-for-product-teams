# resilience test results

_Produced by: Chaos / resilience testing_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** QA/Tester

**Accelerated MVP:** slim — one chaos or load scenario representing the MVP's worst case is enough

## What this is

The evidence that the system behaves correctly under failure — node loss, dependency outage, network partition, slow-dep, resource exhaustion. Captures scenarios run, observed behavior, and the gaps between design expectations and tested reality.

## Why it matters for the SRE

SLOs and DR commitments are promises about failure behavior. Only actual fault injection proves they hold, and Verify is the last cheap opportunity to find the false assumptions before customers do it for you.

## Definition of Done

- [ ] Scenario list maps directly to architecture failure modes
- [ ] Before/during/after signals are captured as execution evidence
- [ ] Automated fallback and alert verification outcomes are recorded
- [ ] Recovery-time observations are compared to targets
- [ ] Defects found have remediation state, and residual risks list owner and mitigation

## What it contains

- Scenario list mapped to architecture failure modes
- Execution evidence: before/during/after signals
- Automated fallback and alert verification
- Recovery-time observations vs. targets
- Defects found and their remediation state
- Residual risks with owner and mitigation

## Inputs you rely on

- Architecture document and integration map
- Service-level objectives and DR commitments
- Validated staging environment (prod-like)
- Threat model (for adversarial failure modes)
- Runbook and deployment runbook

## Who consumes it

- PRR sign-off artifact consumes this as a key input
- Release Manager — gates launch on resolution of blocking gaps
- Architect — updates ADRs where resilience assumptions failed
- Product Sponsor — sees residual risk for launch-risk acceptance

## Common pitfalls

- Running scenarios only in isolated test environments that lack real coupling
- Declaring recovery "successful" on human intervention rather than automation
- Skipping data-path resilience because "we never lose the DB" — until you do
- No retest after remediation so claimed fixes aren't proven

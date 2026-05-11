# Security & Compliance in Plan

You are here to make controls a property of the pipeline, not a gate at the end. Plan is where you bake scanning, evidence collection, IR readiness, and security test coverage into the delivery machinery — so Build produces secure, auditable increments by default.

## What you do

- Contribute to the security test plan so QA coverage includes threat-model-derived cases, not just functional ones.
- Define security & compliance controls in the pipeline — SAST, SCA, secrets, IaC scanning, gating thresholds.
- Author the compliance evidence collection plan so audit artifacts accumulate automatically, not retroactively.
- Write the incident response plan & runbook so on-call knows what to do when (not if) something fires.

## Artifacts you own

- [pipeline security controls](artifacts/pipeline-security-controls.md) — controls wired into CI/CD.
- [evidence collection plan](artifacts/evidence-collection-plan.md) — how compliance evidence is gathered continuously.
- [IR plan & runbook](artifacts/ir-plan-runbook.md) — who does what when an incident fires.
- [security test plan](artifacts/security-test-plan.md) — co-owned with QA/Tester.

## Artifacts you contribute to

You don't contribute to other-owned artifacts this phase — your outputs are the security substrate others build on.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **QA/Tester** — co-owns the security test plan; you provide threat-model-derived cases, they integrate into the overall test strategy.
- **Site Reliability Engineer** — wires your pipeline controls into the CI/CD pipeline they're setting up.
- **Developer** — will be the one whose commits hit your controls in Build; you make sure failure modes are clear.
- **Architect** — aligns your controls with the approved security patterns.

## Handoff into [Build](../5-build/README.md)

In Build you shift from planning controls to operating them — scanning every build, triaging vulnerabilities against SLA, and reviewing code for security issues. You know Plan is done when pipeline controls are running green on sample commits, IR runbooks are rehearsed at least once, and the evidence collection plan is generating data.

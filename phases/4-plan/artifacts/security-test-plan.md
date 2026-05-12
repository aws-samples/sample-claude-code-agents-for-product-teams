# security test plan

_Produced by: Security test plan contribution_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Security & Compliance

**Stakeholders:** QA/Tester

**Accelerated MVP:** required when applicable regulations or a threat model exist; otherwise slim

## What this is

The slice of the test plan focused on security: threat-model-driven test cases, SAST/DAST/SCA/IAST tooling, pen-test scope and timing, abuse-case testing, and the controls that must be verified before launch. Owned by Security, executed jointly with QA.

## Why it matters for the Security & Compliance owner

Controls written on paper aren't controls — only tested controls are. This plan ties threat-model findings and compliance requirements to concrete tests so you can evidence that high-risk vulnerability classes are demonstrably mitigated at launch.

## Definition of Done

- [ ] Security test scope and out-of-scope items are explicit
- [ ] Tool inventory (SAST, SCA, secrets, container, DAST, IAST) names run points
- [ ] Abuse-case and negative-path catalogs exist per threat
- [ ] Pen-test engagement scope, timing, and retest plan are defined
- [ ] Compliance controls are mapped to verification tests
- [ ] Vulnerability severity rubric and remediation SLAs are stated

## What it contains

- Security test scope and explicit out-of-scope items
- Tool inventory (SAST, SCA, secrets, container, DAST, IAST) with run points
- Abuse-case and negative-path test catalogs per threat
- Pen-test engagement scope, timing, and retest plan
- Compliance control verification mapping
- Vulnerability severity rubric and remediation SLAs

## Inputs you rely on

- Threat model and approved security patterns from Design
- Security control requirements and applicable regulations
- Test plan for integration points
- Architecture document and data classification
- Pipeline security controls for automated gating

## Who consumes it

- QA/Tester — executes joint campaigns and integrates with main test reporting
- Developers — consume scan findings and remediate
- Release Manager — uses exit criteria to gate launch on security
- Internal auditors — evidence of test-based control verification

## Common pitfalls

- Pen-test scheduled so late there's no time to remediate findings before launch
- SAST/SCA gate severity set so permissively it's theater
- Abuse cases exist on paper but no automation or exploratory time is budgeted
- Third-party/vendor surfaces excluded from scope and discovered in production

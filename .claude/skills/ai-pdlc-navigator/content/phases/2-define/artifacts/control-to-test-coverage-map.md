# control-to-test coverage map

_Produced by: Map security controls to test cases_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Security & Compliance

**Stakeholders:** QA/Tester

## What this is

A matrix mapping each security control to the test case(s) that verify it — automated, manual, or attestation-based. Rows are controls, columns are the tests that prove them, and gaps are things the audit will find if you don't fix them first.

## Why it matters for the Security & Compliance owner

You co-own this with QA so every control has an observable proof, not just a promise. It is also the fastest way to spot controls with no verification strategy while they can still be reshaped — before Build makes them expensive to change.

## Definition of Done

- [ ] Every control ID traces to a control in the security control requirements
- [ ] Each control row names at least one test case with its type (unit / integration / SAST / DAST / manual / attestation)
- [ ] Each test row has an execution cadence stated
- [ ] Evidence artifact location is specified per control
- [ ] Coverage gaps are flagged with a named remediation plan

## What it contains

- Control ID linked to the [security control requirements](security-control-requirements.md)
- Test case ID and type (unit, integration, SAST, DAST, manual, attestation)
- Execution cadence (per commit, per release, quarterly audit)
- Evidence artifact location
- Coverage gap flags and remediation plan
- Tested-environment scope (preprod, prod, both)

## Inputs you rely on

- [Security control requirements](security-control-requirements.md)
- [Test-to-requirement coverage map](test-to-requirement-coverage-map.md) for deduplication
- QA's test strategy and automation capability
- CI/CD pipeline capability for automated evidence

## Who consumes it

- QA/Tester — authors or automates the tests and maintains the coverage view
- Security & Compliance — uses it for audit and for the [evidence collection plan](../../4-plan/artifacts/evidence-collection-plan.md)
- Release Manager — validates controls are green before release
- Auditor — follows it to evidence-of-control

## Common pitfalls

- Documentation-as-evidence for things that could be automated
- Gaps that are known but not tracked as remediation items
- Cadence mismatches — a control verified quarterly for a daily-release product
- No environment scope, so a preprod pass is treated as a prod assurance

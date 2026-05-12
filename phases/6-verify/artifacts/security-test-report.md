# security test report

_Produced by: Security testing / pen test_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Security & Compliance

**Stakeholders:** QA/Tester

**Accelerated MVP:** required when the MVP is external-facing or data-sensitive; otherwise platform scans suffice

## What this is

The consolidated outcome of security testing — pen test, DAST, abuse-case exercises, control verification — against the production-like environment. Every finding has severity, owner, reproducibility, and remediation state.

## Why it matters for the Security & Compliance owner

Launch-window remediation time is your scarcest resource. A clear report with prioritized findings is how you direct that window efficiently and provide the Sponsor honest risk information for the compliance go/no-go and launch-risk acceptance.

## Definition of Done

- [ ] Scope, methodology, and dates of testing are stated
- [ ] Findings list severity, CVSS/custom scoring, and exploitability evidence
- [ ] Threat-model coverage check and control-verification outcomes tied to requirements are recorded
- [ ] Remediation state per finding (fixed, accepted, deferred) is documented
- [ ] Retest results after fixes are attached

## What it contains

- Scope, methodology, and dates of testing
- Findings with severity, CVSS/custom scoring, exploitability evidence
- Threat-model coverage check
- Control-verification outcomes tied to requirements
- Remediation state per finding (fixed, accepted, deferred)
- Retest results after fixes

## Inputs you rely on

- Security test plan
- Threat model and security control requirements
- Validated staging environment
- Vulnerability scan outcomes from Build
- Applicable regulations

## Who consumes it

- Product Sponsor — uses it in launch-risk acceptance
- Release Manager — gates on severity-based exit criteria
- Developers — remediate findings
- Auditors — evidence of pre-launch security verification

## Common pitfalls

- Tested against staging that diverges from production — misses exist in prod
- Findings rated by tool default without context calibration
- Pen test performed too late for remediation — findings become "accepted"
- No retest after fix — closed findings weren't actually closed

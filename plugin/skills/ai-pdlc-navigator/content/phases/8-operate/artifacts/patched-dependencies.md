# patched dependencies

_Produced by: Security patching_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Security & Compliance

**Stakeholders:** Developer, Site Reliability Engineer

## What this is

The ongoing record that vulnerable dependencies, OS packages, base images, and libraries are being patched on cadence against the agreed remediation SLAs — what got patched, when, in response to which CVE, and what still needs work.

## Why it matters for the Security & Compliance team

Dependency vulnerabilities are now the most common exploit path; your ability to measure and enforce patch SLAs is audit-table-stakes. A clean patched-dependencies record is both evidence for compliance and the operational artifact that keeps the attack surface shrinking instead of growing.

## Definition of Done

- [ ] Each CVE is recorded with severity and the affected components.
- [ ] Patch status, production version, and deploy date are captured per item.
- [ ] Remediation-SLA compliance is measured, not just set.
- [ ] Exceptions include rationale and compensating controls.
- [ ] Pending items have named owners and due dates.

## What it contains

- CVE IDs with severity and affected components
- Patch status, version in production, and deploy date
- Remediation SLA and compliance with it
- Exceptions with rationale and compensating controls
- Pending items with owners and due dates
- Dependency SBOM snapshots

## Inputs you rely on

- Vulnerability scan reports (SCA, SAST, container)
- SBOM and dependency inventory
- Security monitoring alerts
- Triaged vulnerabilities from Build phase process
- CVE feeds and threat intelligence

## Who consumes it

- Security & Compliance — audit evidence
- Developer and SRE — work queue
- Architect — feeds modernization plan
- Customer security questionnaires — enterprise sales

## Common pitfalls

- Patches applied in one environment but not all
- Exceptions granted without compensating controls documented
- SLA set but not measured — no idea if it's being met
- Focus on "critical" only, letting highs pile up until they become critical

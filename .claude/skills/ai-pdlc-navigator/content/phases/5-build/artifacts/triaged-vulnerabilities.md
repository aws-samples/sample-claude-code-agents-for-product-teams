# triaged vulnerabilities

_Produced by: Vulnerability triage & remediation SLA tracking_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

The actively-managed subset of scan findings — decided, owned, and on a remediation clock. Each entry has a call (fix, suppress, accept), an owner, an SLA by severity, and a visible aging indicator.

## Why it matters for the Security & Compliance owner

Scan reports only matter if they drive action. This artifact is the operational commitment to meet the remediation SLAs the org has set — and the data you rely on to gate release, negotiate with engineering, and evidence posture to auditors.

## Definition of Done

- [ ] Every finding has a decision of fix, suppress, or accept and a decision-maker
- [ ] Severity, owner, and remediation-by date are captured per entry
- [ ] Aging against SLA is shown and overdues are flagged
- [ ] Each entry links to a remediation PR or waiver record
- [ ] Summary metrics cover counts by severity and SLA compliance

## What it contains

- Findings with decision (fix / suppress / accept) and decision-maker
- Severity, owner, and remediation-by date
- Aging against SLA, with flagged overdues
- Link to remediation PR or waiver record
- Re-open history if previously resolved
- Summary metrics (count by severity, SLA compliance %)

## Inputs you rely on

- Vulnerability scan report
- Threat model and exploit-context for severity calibration
- Developer and architect input on feasibility/cost of fix
- Applicable regulations for mandatory patching SLAs
- Reviewed code status (what's already been addressed)

## Who consumes it

- Developers — work remediation against the queue
- Release Manager — gates promotion on SLA-compliant posture
- Product Sponsor — sees summary when risk-acceptance needs approval
- Auditors — evidence of active vulnerability management

## Common pitfalls

- Triage debt — new findings not picked up within days, distorting metrics
- Over-broad suppressions that hide later variants of the same flaw
- Fixes marked closed without verification or regression check
- Acceptance rubber-stamped without expiry or re-review trigger

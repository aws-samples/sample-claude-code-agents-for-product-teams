# Security & Compliance in Operate

Operate is where controls earn their keep. You run the evidence collection, security monitoring, patching cadence, and audit cycles that keep the company shippable and regulated. Your job is to stop vulnerabilities before they matter and deliver clean attestations on demand.

## What you do

- Collect compliance audit evidence so audits are routine, not fire drills.
- Drive security patching with Developer and Site Reliability Engineer on SLA-defined cadence.
- Run security monitoring and SIEM operations with Site Reliability Engineer.
- Respond to security incidents — triage, contain, post-mortem, improve.
- Execute periodic compliance audits and deliver the attestations.
- Run access reviews so least-privilege actually holds up.

## Artifacts you own

- [audit evidence](artifacts/audit-evidence.md) — the ongoing evidence collection that underwrites audits.
- [patched dependencies](artifacts/patched-dependencies.md) — the patch cadence output, produced with Developer and SRE.
- [security monitoring alerts](artifacts/security-monitoring-alerts.md) — the monitoring output, produced with SRE.
- [security incident postmortems](artifacts/security-incident-postmortems.md) — the post-mortems you own end-to-end.
- [audit report / attestation](artifacts/audit-report-attestation.md) — the periodic audit output.
- [access review results](artifacts/access-review-results.md) — the access-review cadence output.

## Artifacts you contribute to

You don't contribute to others' artifacts this phase.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Developer** — bi-directional on patching, secure code, and security incident fixes.
- **Site Reliability Engineer** — bi-directional on monitoring, patching, and access control.
- **Product Sponsor** — bi-directional on Sev-1 security incidents and comms approval.
- **Architect** — bi-directional on architectural security evolution.

## Handoff into [Iterate](../9-iterate/README.md)

You exit Operate with a live controls posture and audit-ready evidence. Carry that into Iterate's security posture review and regulatory change monitoring — the posture you report is the baseline for next-cycle investment, and regulatory change is the highest-signal input into Discover for new controls work.

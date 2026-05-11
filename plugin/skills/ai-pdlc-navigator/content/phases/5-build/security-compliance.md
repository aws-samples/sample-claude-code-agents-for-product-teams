# Security & Compliance in Build

You are here to operate the controls you set up in Plan — every commit, every PR, every build. Build is where vulnerabilities appear as real findings and where remediation SLAs either mean something or don't. Your job is to keep scanning loud, triage fast, and make sure code review catches what scanners miss.

## What you do

- Run security scanning (SAST/SCA) with Developers so every build produces a current vulnerability picture.
- Triage vulnerabilities against remediation SLAs so "known risk" is a decision, not a backlog.
- Participate in code review on security-sensitive changes so authz, crypto, secrets, and input handling stay correct.
- Keep the evidence collection plan running so audit prep isn't a separate project at Launch.

## Artifacts you own

- [vulnerability scan report](artifacts/vulnerability-scan-report.md) — co-owned with Developer.
- [triaged vulnerabilities](artifacts/triaged-vulnerabilities.md) — prioritized, SLA-tracked.

## Artifacts you contribute to

- [reviewed code](artifacts/reviewed-code.md) — Developer owns; you review on security-sensitive changes.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Developer** — co-owns scanning; they triage alongside you and fix against SLA.
- **Architect** — pairs with you when a finding suggests an architectural pattern miss.
- **Site Reliability Engineer** — keeps pipeline controls running and reports failures.
- **QA/Tester** — aligns on which security tests run in Build vs. wait for Verify.

## Handoff into [Verify](../6-verify/README.md)

In Verify you co-own security testing / pen test with QA and drive the compliance go/no-go. You know Build is done when open vulnerabilities are within policy, the evidence log is current, and no critical/high is heading into Verify without a decision.

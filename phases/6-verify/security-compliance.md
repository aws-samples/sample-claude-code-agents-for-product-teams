# Security & Compliance in Verify

You are here to produce launch-grade security and compliance evidence. Verify is where you run the tests that can't be automated into every build — pen test, compliance readiness — and where your go/no-go determines whether the product is legally and operationally shippable.

## What you do

- Run security testing / pen test jointly with QA/Tester so the application is tested the way attackers test it.
- Conduct the compliance readiness review and issue the go/no-go so the Sponsor can commit to launch.
- Co-own launch risk posture with Sponsor and Product Owner so known issues are accepted with eyes open.
- Validate the evidence collection plan actually produced the audit artifacts you said it would.

## Artifacts you own

- [security test report](artifacts/security-test-report.md) — co-owned with QA/Tester.

## Artifacts you contribute to

- [readiness assessment](artifacts/readiness-assessment.md) — QA/Tester owns; you contribute the security read.
- [approved known-issues & risk acceptance](outcomes/approved-known-issues-risk-acceptance.md) — Product Sponsor owns; you bring the security/compliance risks.

## Outcomes you drive

- [compliance go/no-go](outcomes/compliance-go-no-go.md) — launch-grade compliance decision.

## Who you work with

- **QA/Tester** — co-owns security testing; they run the harness, you interpret and direct.
- **Product Sponsor / Product Owner** — co-own risk posture with you; you bring the risks, they accept or defer.
- **Architect** — pairs with you when a finding suggests design-level remediation.
- **Release Manager** — confirms evidence is attached to the release package.

## Handoff into [Launch](../7-launch/README.md)

In Launch you co-own the legal approval with the Product Owner. You know Verify is done when the security test report is triaged and accepted or closed, the compliance go/no-go is issued, and known security/compliance issues have formal risk acceptance.

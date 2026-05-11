# Release Manager in Launch

Launch is your phase. You own the release mechanics end-to-end — release notes, deploy execution, the hypercare war room — and you co-own the continue/rollback authority with the Sponsor. Your standard is zero Sev-1 escapes and a launch window that stabilizes on schedule.

## What you do

- Write release notes that serve customers, support, sales, and auditors as the single source of truth for what shipped.
- Execute the deploy/release into production per the runbook.
- Run the post-deploy smoke tests with QA to validate release health.
- Co-own the launch war room and hypercare with the Site Reliability Engineer through stabilization.
- Participate in the go/no-go call and the continue/rollback authority call.

## Artifacts you own

- [release notes](artifacts/release-notes.md) — the canonical "what shipped" for customers, support, and auditors.
- [released product in production](artifacts/released-product-in-production.md) — the actual release, on record, in prod.

## Artifacts you contribute to

- [production validation](artifacts/production-validation.md) — QA owns; you execute the deploy side and sign release health.

## Outcomes you drive

- [stabilized launch window](outcomes/stabilized-launch-window.md) — your hypercare call, co-owned with SRE.
- [continue/rollback decision](outcomes/continue-rollback-decision.md) — Product Sponsor owns; you deliver the release-integrity view.
- [go/no-go decision](outcomes/go-no-go-decision.md) — Product Owner owns; you deliver release readiness.

## Who you work with

- **Product Owner** — bi-directional on go/no-go and release sequencing.
- **Product Sponsor** — bi-directional on rollback authority and launch-day posture.
- **Site Reliability Engineer** — bi-directional on hypercare, observability, and stabilization.
- **QA/Tester** — bi-directional on production validation and smoke tests.
- **Project Manager** — bi-directional on command-center coordination and comms cadence.

## Handoff into [Operate](../8-operate/README.md)

You exit Launch with a stabilized release, clean notes on record, and rollback capability preserved. Hand operational ownership to SRE and Support for steady-state — your focus shifts to the next release's cadence, readiness, and rollback posture, carrying forward what this launch taught you about release integrity.

# Release Manager in Verify

This is where your Plan-phase runbook gets rehearsed. You are here to prove the deployment path works, stabilize the build/deploy pipeline under real release-shaped activity, and co-sign the Production Readiness Review alongside SRE and the Architect. Your co-ownership of the launch-date commitment means you carry credibility for whether the system can actually ship when the Sponsor says it will.

## What you do

- Execute staging deployment with smoke tests jointly with QA/Tester to prove the release path.
- Troubleshoot build & deploy activities so pipeline issues are cleared before Launch, not during.
- Co-own Production Readiness Review sign-off with SRE and Architect.
- Co-own the launch-date commitment with the Sponsor based on Verify evidence.

## Artifacts you own

- [validated staging environment](artifacts/validated-staging-environment.md) — co-owned with QA/Tester.
- [stable build/deploy pipeline](artifacts/stable-build-deploy-pipeline.md) — issues troubleshot and cleared.

## Artifacts you contribute to

You don't formally contribute to other Verify-phase artifacts beyond your outcomes.

## Outcomes you drive

- [committed launch date](outcomes/committed-launch-date.md) — co-owned with Product Sponsor.
- [PRR sign-off](outcomes/prr-sign-off.md) — co-owned with Site Reliability Engineer and Architect.

## Who you work with

- **QA/Tester** — co-owns staging smoke tests; primary counterpart for rehearsal.
- **Site Reliability Engineer** — co-owns PRR; shared runbook ownership.
- **Architect** — co-owns PRR; validates rollout pattern.
- **Product Sponsor** — co-owns launch-date commitment.
- **Project Manager** — gives you the launch-readiness status pack to plug into the commitment.

## Handoff into [Launch](../7-launch/README.md)

In Launch you own release notes, deploy/release execution, and hypercare co-ownership. You know Verify is done when staging deploys are repeatable, the pipeline is stable, PRR is signed, and the launch date is committed with confidence.

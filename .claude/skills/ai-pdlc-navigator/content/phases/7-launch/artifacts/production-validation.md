# production validation

_Produced by: Post-deploy production smoke tests_

**Business outcome supported:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

**Primary owner:** QA/Tester

**Stakeholders:** Release Manager

## What this is

The post-deploy smoke-test result proving that critical paths work for real users on production configuration — login, core transactions, integrations, payment, telemetry emission. Short, targeted, non-destructive.

## Why it matters for the QA/Tester

Staging is not production. Config, secrets, data shape, and partner availability diverge in ways that only appear post-deploy. Your validation is the fast feedback that tells the war room whether to announce launch, delay comms, or roll back.

## Definition of Done

- [ ] Smoke suite coverage is mapped to every critical user journey.
- [ ] Integration health checks executed against each upstream and downstream partner.
- [ ] KPI telemetry emission was spot-checked and the result recorded.
- [ ] Pass/fail result per scenario is recorded with timestamp.
- [ ] QA lead sign-off is captured.

## What it contains

- Smoke suite coverage of critical user journeys
- Integration health checks against each upstream/downstream partner
- KPI telemetry emission spot-checks
- Pass/fail per scenario with timestamps
- Any defects found, severity, and action (fix-forward or rollback)
- Sign-off from QA lead

## Inputs you rely on

- Released product in production (BOM and deploy confirmation)
- Regression test results and validated staging environment
- Verified KPI telemetry from Verify
- Launch run-of-show for timing
- Access to production test accounts and synthetic data

## Who consumes it

- Release Manager — input to stabilized launch window decision
- Product Sponsor and Product Owner — informs continue/rollback
- Customer Support — early warning of user-visible issues
- SRE — confirms observability is actually working

## Common pitfalls

- Smoke suite too broad; takes too long and blocks go-live comms
- Using staging test data instead of production-safe accounts
- Missing partner/integration checks — the failures that hurt most
- No codified pass/fail thresholds, so interpretation varies by tester

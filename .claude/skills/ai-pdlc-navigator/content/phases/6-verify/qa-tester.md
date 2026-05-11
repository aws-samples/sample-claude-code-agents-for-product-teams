# QA/Tester in Verify

This is your heaviest phase. You are here to produce evidence — performance, accessibility, regression, UAT, security — that says whether this product is safe to ship. You drive the UAT/beta sign-off, run the tests others rely on, and triage the defects that come out. If Verify is rescue, it's usually because Build testing wasn't trusted; your job is to not have that problem.

## What you do

- Assess feature readiness with Security & Compliance so the readiness picture is complete.
- Run pre-launch UAT / beta validation with the Product Owner — the user-facing gate.
- Run performance / load testing with SRE and Architect against SLOs.
- Run accessibility testing with UI/UX Designer against WCAG targets.
- Run regression testing so nothing that used to work has silently broken.
- Co-own security testing / pen test execution with Security & Compliance.
- Co-own chaos / resilience testing with SRE.
- Co-own staging smoke tests with Release Manager.
- Co-own documentation review with Technical Writer — walking the product with the docs.
- Triage UAT defects with Developer — fix, defer, or accept.

## Artifacts you own

- [readiness assessment](artifacts/readiness-assessment.md) — co-owned with Security & Compliance.
- [performance test report](artifacts/performance-test-report.md) — co-owned with SRE and Architect.
- [accessibility audit report](artifacts/accessibility-audit-report.md) — co-owned with UI/UX Designer.
- [regression test results](artifacts/regression-test-results.md)
- [triaged UAT defects](artifacts/triaged-uat-defects.md) — co-owned with Developer.

## Artifacts you contribute to

- [security test report](artifacts/security-test-report.md) — Security & Compliance owns.
- [resilience test results](artifacts/resilience-test-results.md) — Site Reliability Engineer owns.
- [validated staging environment](artifacts/validated-staging-environment.md) — Release Manager owns.
- [verified docs](artifacts/verified-docs.md) — Technical Writer owns.

## Outcomes you drive

- [UAT/beta sign-off](outcomes/uat-beta-sign-off.md) — co-owned with Product Owner.

## Who you work with

- **Product Owner** — co-signs UAT/beta with you.
- **Developer** — co-triages UAT defects with you; fixes what you find.
- **Security & Compliance** — co-owns security testing and readiness.
- **Site Reliability Engineer** — co-owns chaos and performance.
- **UI/UX Designer** — co-owns accessibility.
- **Release Manager** — co-owns staging smoke tests.
- **Technical Writer** — co-owns documentation review.

## Handoff into [Launch](../7-launch/README.md)

In Launch you own post-deploy production smoke tests. You know Verify is done when UAT/beta is signed, every test stream has issued its result, and the remaining defects are either fixed or on the approved known-issues list.

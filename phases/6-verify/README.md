# Phase 6: Verify

**Goal:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

## Where this fits

Verify picks up where [Build](../5-build/README.md) exits and prepares the conditions for [Launch](../7-launch/README.md). Every artifact and outcome in this phase is produced because a later phase depends on it.

## What happens in this phase

Verify gathers the evidence that the product is safe to launch and that the business is ready to measure it. Code-complete is not done — launch readiness is functional, non-functional, operational, regulatory, and informational. Findings here cost 10x less to fix than findings after launch.

Verify is led by **QA/Tester** (feature readiness, UAT/beta, performance, accessibility, regression, defect triage). The **SRE** runs chaos/resilience tests, operational readiness review, KPI telemetry verification, and performance testing. The **Release Manager** executes staging deployments, smoke tests, build/deploy stabilization, and the launch-readiness status pack. **Security & Compliance** leads security testing, pen testing, and the compliance readiness review. The **UI/UX Designer** validates visual fidelity and runs accessibility testing. The **Technical Writer** reviews documentation. The **Architect** validates architecture in the verify environment and assesses architectural risk. The **Business Analyst** coordinates UAT with business users and assesses benefits readiness. **Customer Support** and **Sales & Marketing** recruit and onboard UAT/beta cohorts. The **Developer** runs data migration dress rehearsals. The **Product Sponsor** reviews launch-readiness metrics, approves the beta cohort, launch window, risk posture, and analyst briefings. The **Project Manager** coordinates the verify phase, reports readiness status, and runs defect governance.

Verify ends with multiple sign-offs in hand: [PRR sign-off](outcomes/prr-sign-off.md), [UAT/beta sign-off](outcomes/uat-beta-sign-off.md), [compliance go/no-go](outcomes/compliance-go-no-go.md), [approved known-issues & risk acceptance](outcomes/approved-known-issues-risk-acceptance.md), and a [committed launch date](outcomes/committed-launch-date.md).

## Deliverables

- **[`artifacts/`](artifacts/)** — 22 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 7 decisions or state changes.

See the [Verify activities list in the master flow](../../AI-PDLC-linear-flow.md#6-verify) for the full activity-by-activity view.

## Role-specific briefs

| Role | Brief |
|------|-------|
| Product Sponsor | [product-sponsor.md](product-sponsor.md) |
| Product Owner | [product-owner.md](product-owner.md) |
| Business Analyst | [business-analyst.md](business-analyst.md) |
| UI/UX Designer | [ui-ux-designer.md](ui-ux-designer.md) |
| Architect | [architect.md](architect.md) |
| Security & Compliance | [security-compliance.md](security-compliance.md) |
| Site Reliability Engineer | [site-reliability-engineer.md](site-reliability-engineer.md) |
| Project Manager | [project-manager.md](project-manager.md) |
| Developer | [developer.md](developer.md) |
| QA / Tester | [qa-tester.md](qa-tester.md) |
| Release Manager | [release-manager.md](release-manager.md) |
| Technical Writer | [technical-writer.md](technical-writer.md) |
| Sales & Marketing | [sales-marketing.md](sales-marketing.md) |
| Customer Support | [customer-support.md](customer-support.md) |

## Exit checklist

Ready to enter [Launch](../7-launch/README.md) when all of the following are true:

- [ ] [accessibility audit report](artifacts/accessibility-audit-report.md) — Every finding lists severity and the specific WCAG criterion.
- [ ] [architectural risk report](artifacts/architectural-risk-report.md) — Each risk has a blast-radius and probability score.
- [ ] [architecture validation report](artifacts/architecture-validation-report.md) — NFR attainment is supported by measured evidence (perf, scale, availability, security).
- [ ] [benefits-readiness report](artifacts/benefits-readiness-report.md) — Pre-launch baseline values are captured.
- [ ] [defect status & triage cadence](artifacts/defect-status-triage-cadence.md) — Decision rights (fix-now, defer, accept) are assigned by role.
- [ ] [launch-readiness assessment](artifacts/launch-readiness-assessment.md) — An explicit recommendation (proceed, adjust, or delay) is recorded.
- [ ] [launch-readiness status pack](artifacts/launch-readiness-status-pack.md) — Sign-off tracker shows owners and dates for each gate.
- [ ] [migration runbook validation](artifacts/migration-runbook-validation.md) — Rollback rehearsal outcome is documented.
- [ ] [performance test report](artifacts/performance-test-report.md) — Latency percentiles are reported per critical journey, with comparison to NFR/SLO targets.
- [ ] [readiness assessment](artifacts/readiness-assessment.md) — Each feature has an explicit recommendation: ready / ready with caveats / not ready.
- [ ] [recruited UAT cohort](artifacts/recruited-uat-cohort.md) — Legal agreements (beta terms, NDA, data handling) are signed.
- [ ] [regression test results](artifacts/regression-test-results.md) — Coverage verification confirms every acceptance criterion was reached.
- [ ] [resilience test results](artifacts/resilience-test-results.md) — Recovery-time observations are compared to targets.
- [ ] [security test report](artifacts/security-test-report.md) — Retest results after fixes are attached.
- [ ] [stable build/deploy pipeline](artifacts/stable-build-deploy-pipeline.md) — Rollback path has been rehearsed end-to-end with timings recorded.
- [ ] [triaged UAT defects](artifacts/triaged-uat-defects.md) — Disposition (fix, defer, accept, won't-fix) is stated with rationale.
- [ ] [UAT coordination & results](artifacts/uat-coordination-results.md) — Sign-off status is recorded by participant segment.
- [ ] [validated staging environment](artifacts/validated-staging-environment.md) — Monitoring and alerting are active and wired to the correct channels.
- [ ] [verified docs](artifacts/verified-docs.md) — Defects found (incorrect UI text, broken flows, stale references) are listed.
- [ ] [verified KPI telemetry](artifacts/verified-kpi-telemetry.md) — Every KPI has an emission check comparing expected vs. observed event shape.
- [ ] [verify execution plan](artifacts/verify-execution-plan.md) — Go/no-go and launch-date decision checkpoints are calendared.
- [ ] [visual QA report](artifacts/visual-qa-report.md) — Findings include expected vs. actual, severity, and evidence per screen/component.
- [ ] [approved known-issues & risk acceptance](outcomes/approved-known-issues-risk-acceptance.md) — Sponsor, PO, and Security & Compliance acceptance is recorded.
- [ ] [approved launch cohort](outcomes/approved-launch-cohort.md) — Criteria for expansion to the next wave are defined.
- [ ] [committed launch date](outcomes/committed-launch-date.md) — Date is stated with time zone and go-live window.
- [ ] [compliance go/no-go](outcomes/compliance-go-no-go.md) — Compliance decision is stated with referenced controls and evidence.
- [ ] [PRR sign-off](outcomes/prr-sign-off.md) — SLOs, runbooks, on-call, and observability are attested.
- [ ] [UAT/beta sign-off](outcomes/uat-beta-sign-off.md) — Defects found are classified as fixed, deferred, or accepted as known issues.
- [ ] [warmed market & analyst briefings](outcomes/warmed-market-analyst-briefings.md) — Feedback from briefings and resulting narrative adjustments are documented.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

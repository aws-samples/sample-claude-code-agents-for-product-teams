# Phase 8: Operate

**Goal:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

## Where this fits

Operate picks up where [Launch](../7-launch/README.md) exits and prepares the conditions for [Iterate](../9-iterate/README.md). Every artifact and outcome in this phase is produced because a later phase depends on it.

## What happens in this phase

Operate runs the product as a commercial service. Reliability, security, compliance, and unit economics run alongside customer onboarding, renewals, and expansion. This is where the business case actually gets earned — the service has to stay up, customers have to adopt, and the P&L has to work.

Operations is owned day-to-day by the **SRE** (monitoring, incident investigation, RCA, on-call, DR testing, cost & capacity, production issue triage), **Customer Support** (onboarding/activation, health scoring, QBRs, triage, troubleshooting, known issues, user escalations, ticket tagging, renewals), and **Security & Compliance** (audit evidence, security patching, SIEM operations, security incident response, periodic audits, access reviews). The **Architect** monitors architectural health, reviews capacity/scale, and evolves architecture from production learnings. **Sales & Marketing** runs win/loss analysis and manages renewals with CS. The **Technical Writer** curates customer documentation. The **Product Owner** leads business reviews with the Sponsor. The **Product Sponsor** reviews operational KPIs & SLO performance, approves Sev-1 external comms, tracks revenue/ARR, and reviews unit economics and margin. The **Business Analyst** runs the business-metric reporting cadence, tracks value realization, and analyzes support data. The **Developer** participates in RCA and security patching. The **Project Manager** transitions from project mode to steady-state and coordinates the operating cadence.

Operate is the longest phase — it runs until Iterate decides what's next. Healthy Operate = SLOs met, compliance current, customers retained/expanding, and unit economics on plan.

## Deliverables

- **[`artifacts/`](artifacts/)** — 34 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 3 decisions or state changes.

See the [Operate activities list in the master flow](../../AI-PDLC-linear-flow.md#8-operate) for the full activity-by-activity view.

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

Ready to enter [Iterate](../9-iterate/README.md) when all of the following are true:

- [ ] [access review results](artifacts/access-review-results.md) — Each account has a manager attestation recorded as kept, modified, or revoked.
- [ ] [activated customers](artifacts/activated-customers.md) — Time-to-value is reported per cohort, not as a single aggregate.
- [ ] [architectural health report](artifacts/architectural-health-report.md) — NFR attainment is reported with specific numbers for latency, availability, throughput, and cost.
- [ ] [architecture updates](artifacts/architecture-updates.md) — Every architectural change lands as a new or superseding ADR.
- [ ] [audit evidence](artifacts/audit-evidence.md) — Each evidence item is mapped to at least one control and framework.
- [ ] [audit report / attestation](artifacts/audit-report-attestation.md) — Every exception has a management response and a dated remediation commitment.
- [ ] [business performance report](artifacts/business-performance-report.md) — Every KPI on the scorecard has an actual vs. target value.
- [ ] [cost & capacity report](artifacts/cost-capacity-report.md) — Unit-cost trend is reported against at least one KPI.
- [ ] [customer-facing knowledge base](artifacts/customer-facing-knowledge-base.md) — Per-article analytics (views, helpful-rating, deflection) are recorded.
- [ ] [customer resolution](artifacts/customer-resolution.md) — Time to first response and total resolution are captured.
- [ ] [DR test results](artifacts/dr-test-results.md) — Measured RTO and RPO are reported against target.
- [ ] [escalated issue ticket](artifacts/escalated-issue-ticket.md) — Support steps already tried are listed so engineering does not repeat them.
- [ ] [health scores & at-risk list](artifacts/health-scores-at-risk-list.md) — Each at-risk account has a save-play status and next step.
- [ ] [incident investigation report](artifacts/incident-investigation-report.md) — Customer impact is measured: who, what, and for how long.
- [ ] [incident postmortem](artifacts/incident-postmortem.md) — Action items carry owners, due dates, and status.
- [ ] [known-issues list](artifacts/known-issues-list.md) — Workaround (with any limits) and fix ETA are captured.
- [ ] [margin & CAC/LTV report](artifacts/margin-cac-ltv-report.md) — Variance is measured against the original business-case assumptions.
- [ ] [monitoring dashboards & alerts](artifacts/monitoring-dashboards-alerts.md) — Each alert rule has severity, routing, and a linked runbook.
- [ ] [ongoing benefits tracking](artifacts/ongoing-benefits-tracking.md) — Every committed benefit has a baseline, target, and current actual.
- [ ] [operating review meetings](artifacts/operating-review-meetings.md) — A decision-log template and archive are in place.
- [ ] [operational performance review](artifacts/operational-performance-review.md) — SLO attainment is reported by service with error-budget status.
- [ ] [patched dependencies](artifacts/patched-dependencies.md) — Remediation-SLA compliance is measured, not just set.
- [ ] [prioritized prod issue log](artifacts/prioritized-prod-issue-log.md) — A proposed owner and target release are assigned.
- [ ] [renewal & expansion bookings](artifacts/renewal-expansion-bookings.md) — Churn (non-renewals) has a reason code captured.
- [ ] [renewal & expansion pipeline](artifacts/renewal-expansion-pipeline.md) — Expansion opportunities have estimated ARR and a confidence weighting.
- [ ] [revenue report](artifacts/revenue-report.md) — Variance is measured vs. both the business case and the current plan.
- [ ] [root cause analysis report](artifacts/root-cause-analysis-report.md) — Contributing causes are enumerated across technical, process, and organisational dimensions.
- [ ] [scale-readiness report](artifacts/scale-readiness-report.md) — Each identified bottleneck has a ceiling and timing estimate.
- [ ] [security incident postmortems](artifacts/security-incident-postmortems.md) — Notification obligations and their current status are documented.
- [ ] [security monitoring alerts](artifacts/security-monitoring-alerts.md) — Detection coverage is mapped against the threat model.
- [ ] [support/VoC trend analysis](artifacts/support-voc-trend-analysis.md) — Thematic analysis of verbatims ends in recommendations with named owners.
- [ ] [tagged support-ticket dataset](artifacts/tagged-support-ticket-dataset.md) — A canonical tag taxonomy with definitions is documented.
- [ ] [triaged ticket queue](artifacts/triaged-ticket-queue.md) — Aging and escalation flags surface breaches before they age out.
- [ ] [win-loss insights](artifacts/win-loss-insights.md) — Top reasons to win and to lose are ranked with supporting evidence.
- [ ] [approved incident comms](outcomes/approved-incident-comms.md) — A delivery record confirms the comm reached customers within the stated SLA.
- [ ] [business review decisions](outcomes/business-review-decisions.md) — Each decision has a named owner and a follow-up action.
- [ ] [steady-state operating handoff](outcomes/steady-state-operating-handoff.md) — Steady-state owners are named for each operational area.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

# Phase 9: Iterate

**Goal:** close the loop — measure actual performance against the business case, decide iterate / pivot / double-down (or sunset when warranted), and feed validated learning back into the next-cycle [Discover](../1-discover/README.md).

## Where this fits

Iterate picks up where [Operate](../8-operate/README.md) has earned real production evidence and closes the loop by feeding validated learning into the next-cycle [Discover](../1-discover/README.md).

## What happens in this phase

Iterate closes the loop. Actual performance gets measured against the business case, learning gets synthesized, and leadership decides whether to iterate, pivot, double-down — or sunset when warranted. The validated learning feeds the next Discover cycle so every cycle compounds what came before.

Iterate is led by the **Product Sponsor** making the portfolio investment decision, running the commercial performance review and benefits realization review, and approving any business-case reforecast. The **Product Owner** refreshes the roadmap, tracks KPIs, runs experiments, prioritizes bug fixes, hands insights to the next Discover cycle, and owns any sunset/deprecation. The **Business Analyst** aggregates feedback, analyzes feature adoption, runs continuous discovery, produces the benefits-shortfall report, and reforecasts the business case. The **Architect** refreshes the architecture roadmap and plans technology modernization. **Security & Compliance** reviews security posture and monitors regulatory change. The **Developer** ships bug fixes. The **QA/Tester** documents bugs with reproduction details. **Customer Support** and **Sales & Marketing** document user feedback and run NPS/health check-ins. The **Project Manager** facilitates lessons learned, closes the project, and coordinates benefits realization reviews.

Iterate ends when the Sponsor makes a [portfolio investment decision](outcomes/portfolio-investment-decision.md) — iterate, pivot, double-down, or sunset — and the accumulated insights become the next cycle's opportunity backlog.

## Deliverables

- **[`artifacts/`](artifacts/)** — 26 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 2 decisions or state changes.

See the [Iterate activities list in the master flow](../../AI-PDLC-linear-flow.md#9-iterate) for the full activity-by-activity view.

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

Ready to feed back into [Discover](../1-discover/README.md) for the next cycle when all of the following are true:

- [ ] [adoption metrics](artifacts/adoption-metrics.md) — Actuals are compared to the adoption targets set in Define.
- [ ] [benefits-realization report](artifacts/benefits-realization-report.md) — Every committed benefit has a realized/partial/shortfall verdict with cited evidence.
- [ ] [benefits-shortfall report](artifacts/benefits-shortfall-report.md) — A clear recommended posture (continue, pivot, sunset) is stated.
- [ ] [bug reports](artifacts/bug-reports.md) — Reproduction steps include environment and test data.
- [ ] [closed project & archive](artifacts/closed-project-archive.md) — Closure sign-off from Sponsor and PMO is captured.
- [ ] [deprecation plan](artifacts/deprecation-plan.md) — Timeline specifies announce, soft sunset, and end-of-life dates.
- [ ] [experiment results](artifacts/experiment-results.md) — Decision (ship, kill, iterate) and rationale are stated.
- [ ] [feedback insights report](artifacts/feedback-insights-report.md) — Recommendations are tied to specific roadmap themes.
- [ ] [KPI performance report](artifacts/kpi-performance-report.md) — KPI actuals are reported against the targets set in Define.
- [ ] [lessons-learned repository](artifacts/lessons-learned-repository.md) — Status (adopted into standards, still open) is tracked per lesson.
- [ ] [modernization plan](artifacts/modernization-plan.md) — Cost, risk, and business impact per item are quantified.
- [ ] [next-cycle opportunity backlog](artifacts/next-cycle-opportunity-backlog.md) — A recommended Discover posture (investigate, fast-track, defer) is assigned per opportunity.
- [ ] [NPS & health scores](artifacts/nps-health-scores.md) — Save-play and advocacy candidate lists are produced.
- [ ] [ongoing insights feed](artifacts/ongoing-insights-feed.md) — Surprises (expectation-vs-reality gaps) are called out.
- [ ] [patched application release](artifacts/patched-application-release.md) — Release notes and changelog entry are published.
- [ ] [prioritized bug list](artifacts/prioritized-bug-list.md) — Customer impact is scored (severity x reach).
- [ ] [prioritized tech-debt list](artifacts/prioritized-tech-debt-list.md) — A cost signal (velocity drag, incident correlation, security risk, cost) is cited with evidence.
- [ ] [profitability assessment vs. business case](artifacts/profitability-assessment-vs-business-case.md) — CAC, LTV, and payback are compared to business-case assumptions.
- [ ] [regulatory change impact](artifacts/regulatory-change-impact.md) — Options and a recommended posture are stated, with tracking until compliant.
- [ ] [retrospective report](artifacts/retrospective-report.md) — Specific actions carry owners and delivery dates.
- [ ] [scheduled benefits reviews](artifacts/scheduled-benefits-reviews.md) — Escalation path when targets are missed is documented.
- [ ] [security posture report](artifacts/security-posture-report.md) — Control maturity is scored against the chosen framework.
- [ ] [updated architecture roadmap](artifacts/updated-architecture-roadmap.md) — Cost and risk of inaction are quantified.
- [ ] [updated business case](artifacts/updated-business-case.md) — A change log captures what moved since the prior business case and why.
- [ ] [updated roadmap](artifacts/updated-roadmap.md) — Items reference the benefits-realization and feedback-insights evidence that drove changes.
- [ ] [user feedback log](artifacts/user-feedback-log.md) — Entry is classified as ask, complaint, or observation and tagged by theme/feature area.
- [ ] [portfolio investment decision](outcomes/portfolio-investment-decision.md) — A kill, pivot, or double-down decision is stated with rationale.
- [ ] [reforecast decision](outcomes/reforecast-decision.md) — The new baseline is defined if the reforecast is accepted.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

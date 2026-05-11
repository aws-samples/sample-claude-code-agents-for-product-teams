# Phase 7: Launch

**Goal:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

## Where this fits

Launch picks up where [Verify](../6-verify/README.md) exits and prepares the conditions for [Operate](../8-operate/README.md). Every artifact and outcome in this phase is produced because a later phase depends on it.

## What happens in this phase

Launch goes live. The product ships to its first real customers, teams get enabled, markets get notified, and the team stays in command of the launch window until the service stabilizes. Baseline metrics are captured so Iterate can measure lift against the business case.

Launch is executed by the **Release Manager** (deploy, release notes, post-deploy smoke tests, launch war room / hypercare) alongside the **SRE** (live ops, monitoring, launch signals). The **Product Sponsor** runs the board and internal launch briefings, watches real-time metrics, holds rollback authority, engages analysts/press, and recognizes the team. The **Product Owner** owns the go/no-go decision with the Release Manager. **Security & Compliance** signs off on legal and compliance. The **Technical Writer** publishes feature documentation and user guides. **Sales & Marketing** executes the marketing push, launch event, pricing & packaging decision, enablement, customer communications, and the sales process cutover. **Customer Support** executes the support process cutover. The **Business Analyst** sets up the live launch KPI dashboard and rolls out process changes to impacted teams. The **Architect** reviews rollback safety and monitors architectural launch signals. The **Project Manager** runs the launch day command center, executes launch comms, and coordinates the stage gate. The **Developer** publishes sample data, demos, and wires KPI events.

Launch ends when the product is live, the [go/no-go decision](outcomes/go-no-go-decision.md) has executed, hypercare stabilizes the service, and baseline metrics are captured. The team shifts into Operate.

## Deliverables

- **[`artifacts/`](artifacts/)** — 22 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 9 decisions or state changes.

See the [Launch activities list in the master flow](../../AI-PDLC-linear-flow.md#7-launch) for the full activity-by-activity view.

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

Ready to enter [Operate](../8-operate/README.md) when all of the following are true:

- [ ] [analyst/press coverage](artifacts/analyst-press-coverage.md) — Every quote carries explicit clearance status for reuse in sales and marketing assets.
- [ ] [architectural launch signals](artifacts/architectural-launch-signals.md) — Every signal has a threshold tied to a specific NFR or capacity model assumption.
- [ ] [board/investor launch narrative](artifacts/board-investor-launch-narrative.md) — Top risks and mitigations — including rollback posture — are documented.
- [ ] [connected KPI data pipeline](artifacts/connected-kpi-data-pipeline.md) — Freshness, completeness, and latency SLIs are stated with target values.
- [ ] [demo assets](artifacts/demo-assets.md) — Reset and re-seed scripts return the environment to a named, known state.
- [ ] [executed launch comms](artifacts/executed-launch-comms.md) — Actual send timestamps are captured and any delta from plan is noted.
- [ ] [feature documentation](artifacts/feature-documentation.md) — Every launching feature has its own page covering purpose, prerequisites, and outcomes.
- [ ] [internal launch announcement](artifacts/internal-launch-announcement.md) — Each affected function has a stated action to take starting today.
- [ ] [launch announcement emails/notices](artifacts/launch-announcement-emails-notices.md) — Send schedule and suppression rules are specified per audience.
- [ ] [launch announcement](artifacts/launch-announcement.md) — Every claim carries Legal and Security & Compliance review status.
- [ ] [launch run-of-show](artifacts/launch-run-of-show.md) — Rollback procedure is documented and the authorizing role is identified.
- [ ] [live sales processes](artifacts/live-sales-processes.md) — Product, SKU, and pricing catalog entries exist and are live in CRM/CPQ.
- [ ] [live support processes](artifacts/live-support-processes.md) — Knowledge base articles and macros are published and linked from day one.
- [ ] [marketing collateral](artifacts/marketing-collateral.md) — Battlecards cover each named key competitor.
- [ ] [pre-launch metrics baseline](artifacts/pre-launch-metrics-baseline.md) — Baseline value, measurement window, and sample size are recorded per KPI.
- [ ] [pricing & packaging plan](artifacts/pricing-packaging-plan.md) — List price, floor price, and discount matrix by segment are documented.
- [ ] [production validation](artifacts/production-validation.md) — QA lead sign-off is captured.
- [ ] [release notes](artifacts/release-notes.md) — Breaking changes are called out with migration guidance.
- [ ] [released product in production](artifacts/released-product-in-production.md) — Sign-off from Release Manager, SRE, and on-call engineer is captured.
- [ ] [rolled-out process changes](artifacts/rolled-out-process-changes.md) — Steady-state owner is named for every rolled-out process.
- [ ] [trained sales & support teams](artifacts/trained-sales-support-teams.md) — Demo certification pass-offs are captured for every seller required to demo.
- [ ] [user guides](artifacts/user-guides.md) — Getting started / quickstart path is published and linked from the product entry point.
- [ ] [continue/rollback decision](outcomes/continue-rollback-decision.md) — Decision is recorded with timestamp and the trigger signals that drove it.
- [ ] [go/no-go decision package](outcomes/go-no-go-decision-package.md) — Support, ops, and comms readiness attestations are captured from each function.
- [ ] [go/no-go decision](outcomes/go-no-go-decision.md) — Decision is recorded with its rationale.
- [ ] [legal approval](outcomes/legal-approval.md) — Every launch-blocking item is listed with its resolution status.
- [ ] [live launch-day status](outcomes/live-launch-day-status.md) — Connected KPI dashboard is live and visible to the Sponsor and launch team.
- [ ] [live launch KPI dashboard](outcomes/live-launch-kpi-dashboard.md) — Every KPI from the approved KPI definitions is rendered live on the dashboard.
- [ ] [recognized team & captured wins](outcomes/recognized-team-captured-wins.md) — Recognition artifact is produced and delivered, with contributors named.
- [ ] [rollback safety sign-off](outcomes/rollback-safety-sign-off.md) — Data-migration reversibility is attested by the Architect in writing.
- [ ] [stabilized launch window](outcomes/stabilized-launch-window.md) — Transition-to-steady-state criteria are documented and confirmed met.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

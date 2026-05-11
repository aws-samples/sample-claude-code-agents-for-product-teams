# Phase 4: Plan

**Goal:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

## Where this fits

Plan picks up where [Design](../3-design/README.md) exits and prepares the conditions for [Build](../5-build/README.md). Every artifact and outcome in this phase is produced because a later phase depends on it.

## What happens in this phase

Plan stands up everything engineering needs to begin productively on day one: the team, environments, pipeline, test strategy, SLOs, governance, a decomposed work-ready backlog, and a baselined schedule. A strong Plan turns 'we have a design' into 'we're shipping by Friday.' A weak Plan means engineering spends its first sprint building scaffolding instead of product.

Plan is coordinated primarily by the **Project Manager** (iteration planning, workitem management, feature/epic tracking, resource scheduling, risk register, governance cadence, RAID log). The **Site Reliability Engineer** provisions environments, sets up CI/CD, defines SLOs, and establishes the change-review process. The **Architect** plans analytics/telemetry, feature flags, technical enablers, and skills requirements. The **QA/Tester** drafts the test strategy. The **Product Owner** manages and decomposes the backlog. The **Business Analyst** authors the benefits realization and stakeholder communication plans. The **Release Manager** drafts the rollout & rollback plan. **Security & Compliance** defines pipeline security controls, compliance evidence plan, security test plan, and incident response plan. The **Product Sponsor** approves staffing, delivery baseline, escalation policy, benefits plan, and announces the kickoff.

Plan ends when the team has a [baselined schedule & budget commitment](outcomes/baselined-schedule-budget-commitment.md) and [approved resource commitment](outcomes/approved-resource-commitment.md). Build can begin.

## Deliverables

- **[`artifacts/`](artifacts/)** — 28 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 6 decisions or state changes.

See the [Plan activities list in the master flow](../../AI-PDLC-linear-flow.md#4-plan) for the full activity-by-activity view.

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

Ready to enter [Build](../5-build/README.md) when all of the following are true:

- [ ] [assigned workitems & daily status](artifacts/assigned-workitems-daily-status.md) — Every in-flight item lists exactly one owner.
- [ ] [benefits plan](artifacts/benefits-plan.md) — Each benefit has a measurement definition with baseline and target values.
- [ ] [changelog review process](artifacts/changelog-review-process.md) — Merge-gate criteria and pipeline enforcement mechanisms are documented.
- [ ] [delivery-ready work items](artifacts/delivery-ready-work-items.md) — Every item has testable acceptance criteria and an engineering size estimate.
- [ ] [deployment runbook](artifacts/deployment-runbook.md) — Rollback procedure has been tested in staging.
- [ ] [enabler backlog](artifacts/enabler-backlog.md) — Sequencing rationale names the feature work each enabler unblocks.
- [ ] [evidence collection plan](artifacts/evidence-collection-plan.md) — Automation status is marked per control, with a gap plan where manual.
- [ ] [executed comms per cadence](artifacts/executed-comms-per-cadence.md) — Log entries record date, audience, channel, topic, and artifact link.
- [ ] [feature/epic status report](artifacts/feature-epic-status-report.md) — RAG status is accompanied by reasoning, not just a color.
- [ ] [feature flag plan](artifacts/feature-flag-plan.md) — Lifecycle rules cover creation, ownership, and cleanup SLAs.
- [ ] [governance calendar](artifacts/governance-calendar.md) — Gates and approval checkpoints are called out explicitly.
- [ ] [IR plan & runbook](artifacts/ir-plan-runbook.md) — Runbooks cover each incident class with step-by-step procedures.
- [ ] [iteration plan](artifacts/iteration-plan.md) — Target scope per iteration names features, enablers, and milestones.
- [ ] [onboarded team](artifacts/onboarded-team.md) — Each member's local dev environment is verified by a first green PR.
- [ ] [pipeline security controls](artifacts/pipeline-security-controls.md) — Pipeline enforcement points (pre-merge, post-merge, pre-deploy) are named.
- [ ] [prioritized backlog](artifacts/prioritized-backlog.md) — Items are ordered with value rationale captured for the top slice.
- [ ] [provisioned environments](artifacts/provisioned-environments.md) — Environment inventory lists every tier (dev, CI, staging, prod, sandbox/demo).
- [ ] [RAID log](artifacts/raid-log.md) — Each entry has a change history and links to decisions or artifacts.
- [ ] [resource schedule](artifacts/resource-schedule.md) — Gaps vs. skills requirement list a planned remedy.
- [ ] [risk register](artifacts/risk-register.md) — Mitigation plan and escalation trigger are specified per risk.
- [ ] [security test plan](artifacts/security-test-plan.md) — Vulnerability severity rubric and remediation SLAs are stated.
- [ ] [service-level objectives](artifacts/service-level-objectives.md) — Error budget and burn policy are specified.
- [ ] [skills requirement input](artifacts/skills-requirement-input.md) — Current-bench gaps are listed with a proposed remedy.
- [ ] [stakeholder comms plan](artifacts/stakeholder-comms-plan.md) — Escalation triggers that change cadence or audience are defined.
- [ ] [technical milestone plan](artifacts/technical-milestone-plan.md) — Risk-reduction spikes are timed before commitments lock.
- [ ] [telemetry plan](artifacts/telemetry-plan.md) — Sampling rates, retention, and PII handling are specified per stream.
- [ ] [test plan](artifacts/test-plan.md) — Entry/exit criteria are defined per test type and for the overall verify stage.
- [ ] [working CI/CD pipeline](artifacts/working-ci-cd-pipeline.md) — Quality gates (coverage thresholds, vuln severity, test results) are defined.
- [ ] [approved benefits plan](outcomes/approved-benefits-plan.md) — Sponsor approval is recorded against the plan.
- [ ] [approved resource commitment](outcomes/approved-resource-commitment.md) — Every staffed role lists a named person and start date.
- [ ] [baselined schedule & budget commitment](outcomes/baselined-schedule-budget-commitment.md) — Critical-path schedule is baselined and recorded.
- [ ] [escalation policy](outcomes/escalation-policy.md) — Severity levels are defined with response SLAs.
- [ ] [internal kickoff announcement](outcomes/internal-kickoff-announcement.md) — Team, Sponsor, PO, and core roles are named.
- [ ] [portfolio priority decision](outcomes/portfolio-priority-decision.md) — Each conflict is named with the chosen resolution.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

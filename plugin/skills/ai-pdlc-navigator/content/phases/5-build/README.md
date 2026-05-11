# Phase 5: Build

**Goal:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

## Where this fits

Build picks up where [Plan](../4-plan/README.md) exits and prepares the conditions for [Verify](../6-verify/README.md). Every artifact and outcome in this phase is produced because a later phase depends on it.

## What happens in this phase

Build is where the product materializes: code, tests, instrumentation, security scanning, peer review, and incremental acceptance. Quality is designed into the delivery cadence — not inspected in at the end. Leadership stays active to hold scope, re-validate the business case as reality emerges, and unblock cross-org dependencies.

Build is centered on **Developers** (feature code, review, merge, static analysis, telemetry, API docs) and **QA/Testers** (automated tests, integration testing, raising requirements questions). The **Architect** provides design guidance, conformance review, ADR updates, and resolves technical blockers. **Security & Compliance** runs security scanning and vulnerability triage; code reviews include security. The **SRE** reviews incoming changes before they hit production. The **Product Owner** accepts increments and makes scope-change decisions. The **Project Manager** runs process improvement reviews, status reports, change control, cross-team sync, budget tracking, and the RAID log. The **Product Sponsor** checkpoints progress, unblocks cross-org dependencies, re-validates the business case, engages design partners, and briefs steering. The **Business Analyst** clarifies requirements, tracks in-flight benefits, and analyzes scope changes.

Build ends when increments meet the Definition of Done with stakeholder acceptance, automated test coverage, and instrumented telemetry — ready for rigorous verification.

## Deliverables

- **[`artifacts/`](artifacts/)** — 30 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 6 decisions or state changes.

See the [Build activities list in the master flow](../../AI-PDLC-linear-flow.md#5-build) for the full activity-by-activity view.

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

Ready to enter [Verify](../6-verify/README.md) when all of the following are true:

- [ ] [architecture status report](artifacts/architecture-status-report.md) — NFR trajectory covers perf, scale, and availability with measured values.
- [ ] [assumptions & benefits-tracking log](artifacts/assumptions-benefits-tracking-log.md) — Every assumption shows a current status of holds, weakened, or broken.
- [ ] [automated test suite](artifacts/automated-test-suite.md) — Acceptance criteria coverage is traceable via a test-to-requirement map.
- [ ] [budget burn report](artifacts/budget-burn-report.md) — Forecast to completion includes a stated confidence level.
- [ ] [change control package](artifacts/change-control-package.md) — Decision record slot is populated with outcome, decider, and date.
- [ ] [change impact report](artifacts/change-impact-report.md) — Benefits and risks of approving vs. deferring are both stated.
- [ ] [clarified requirements](artifacts/clarified-requirements.md) — Rationale names the approver for each decision.
- [ ] [conformance findings](artifacts/conformance-findings.md) — Remediation plan lists an owner and target date per finding.
- [ ] [cross-team sync notes](artifacts/cross-team-sync-notes.md) — Each commitment names the party, date, and confidence.
- [ ] [design guidance sessions](artifacts/design-guidance-sessions.md) — Each session records topic, participants, decision, and rationale.
- [ ] [executive status update](artifacts/executive-status-update.md) — Headline sentence states on track / at risk / off track with the why.
- [ ] [feature code](artifacts/feature-code.md) — Unit and integration tests accompany the change.
- [ ] [generated API docs](artifacts/generated-api-docs.md) — Every published endpoint or operation has a generated reference entry.
- [ ] [governance briefing](artifacts/governance-briefing.md) — Explicit recommendations and decisions sought are stated.
- [ ] [implemented workitems](artifacts/implemented-workitems.md) — DoD checklist is completed per item.
- [ ] [instrumented code](artifacts/instrumented-code.md) — Structured log statements cover the meaningful events in the telemetry plan.
- [ ] [integration test results](artifacts/integration-test-results.md) — Every run is tagged with environment and build.
- [ ] [lint/static-analysis report](artifacts/lint-static-analysis-report.md) — Delta from previous run distinguishes new from pre-existing.
- [ ] [managed vendor deliverables](artifacts/managed-vendor-deliverables.md) — Acceptance status and sign-off evidence are recorded per milestone.
- [ ] [merged code in main branch](artifacts/merged-code-in-main-branch.md) — Pipeline record shows green tests, scans, and artifact signing.
- [ ] [process improvement actions](artifacts/process-improvement-actions.md) — Every action item carries an owner, target date, and success signal.
- [ ] [requirements questions log](artifacts/requirements-questions-log.md) — Resolved entries point to the clarified-requirements entry.
- [ ] [reviewed change log](artifacts/reviewed-change-log.md) — Every change has a risk classification of routine, elevated, or emergency.
- [ ] [reviewed code](artifacts/reviewed-code.md) — Every review comment is resolved or carries a deferral rationale.
- [ ] [technical impact analysis](artifacts/technical-impact-analysis.md) — NFR exposure across perf, scale, availability, and security is stated with magnitude.
- [ ] [triaged vulnerabilities](artifacts/triaged-vulnerabilities.md) — Every finding has a decision of fix, suppress, or accept and a decision-maker.
- [ ] [updated ADRs](artifacts/updated-adrs.md) — Chosen option states both positive and negative consequences.
- [ ] [updated RAID log](artifacts/updated-raid-log.md) — Items updated this cycle show state changes with evidence.
- [ ] [vulnerability scan report](artifacts/vulnerability-scan-report.md) — SLA status identifies which findings are past the remediation window.
- [ ] [weekly/biweekly status report](artifacts/weekly-biweekly-status-report.md) — Every help-needed ask names a decision owner.
- [ ] [accepted increments](outcomes/accepted-increments.md) — Accepted items list the date and reviewer.
- [ ] [business-case reconfirmation or reset](outcomes/business-case-reconfirmation-or-reset.md) — The decision explicitly states continue, adjust scope, or escalate.
- [ ] [committed design partners](outcomes/committed-design-partners.md) — Scope of participation is stated as beta, reference, or co-development.
- [ ] [resolved technical blockers](outcomes/resolved-technical-blockers.md) — Every blocker entry identifies the team impacted and the resolution.
- [ ] [scope-change decisions](outcomes/scope-change-decisions.md) — Every change request links to its impact analysis and decision.
- [ ] [unblocked dependencies](outcomes/unblocked-dependencies.md) — Each entry names the dependency, the blocker, and who unblocked it.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

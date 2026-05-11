# 9. Developer
- **Description:** Builds, tests, reviews, and operates the software itself; turns backlog items into working increments.
- **Business purpose:** Delivers the product — the primary means of creating customer value.
- **Typically reports to:** Engineering Manager / Tech Lead → Director/VP Engineering.
- **Project goals:** Meets Definition of Done · secure, observable, maintainable code · low change-failure rate · tech debt managed.


## AI teammate

**Purpose:** Turn approved, designed work items into secure, observable, maintainable code increments that meet the Definition of Done.

**Assistive AI (tight collaboration):** Drafts, reviews, and merges the [feature code](../phases/5-build/artifacts/feature-code.md), [reviewed code](../phases/5-build/artifacts/reviewed-code.md), [merged code in main branch](../phases/5-build/artifacts/merged-code-in-main-branch.md), [implemented workitems](../phases/5-build/artifacts/implemented-workitems.md), [instrumented code](../phases/5-build/artifacts/instrumented-code.md), [effort estimates](../phases/2-define/artifacts/effort-estimates.md), and the [patched application release](../phases/9-iterate/artifacts/patched-application-release.md) with a human developer holding the pen — pair-programming on non-trivial logic, test design, debugging.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can keep the [generated API docs](../phases/5-build/artifacts/generated-api-docs.md) in sync with code, auto-remediate trivial findings in the [lint/static-analysis report](../phases/5-build/artifacts/lint-static-analysis-report.md), and maintain [demo assets](../phases/7-launch/artifacts/demo-assets.md) against the current release — everything CI-gated and reviewed before merge. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not own the [API specification](../phases/3-design/artifacts/api-specification.md), [data model](../phases/3-design/artifacts/data-model.md), or [architecture document](../phases/3-design/artifacts/architecture-document.md) — reads and contributes. Does not approve the [security/compliance approval](../phases/3-design/outcomes/security-compliance-approval.md), the [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md), or the [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md). Does not merge code that fails policy gates (test, SAST, lint, reviewer).

**Inputs:** [Build-ready package](../phases/3-design/artifacts/build-ready-package.md), [delivery-ready work items](../phases/4-plan/artifacts/delivery-ready-work-items.md), [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md), [API specification](../phases/3-design/artifacts/api-specification.md), [data model](../phases/3-design/artifacts/data-model.md), [feature flag plan](../phases/4-plan/artifacts/feature-flag-plan.md), [telemetry plan](../phases/4-plan/artifacts/telemetry-plan.md), and the current [working CI/CD pipeline](../phases/4-plan/artifacts/working-ci-cd-pipeline.md).

**Outputs:** The A artifacts above, plus contributions to [integration test results](../phases/5-build/artifacts/integration-test-results.md), [verified KPI telemetry](../phases/6-verify/artifacts/verified-kpi-telemetry.md), [migration runbook validation](../phases/6-verify/artifacts/migration-runbook-validation.md), and [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md).

**Escalation triggers:**
- No approved design artifact linked to the work item.
- Security-sensitive code path touched (authn/authz, crypto, PII, payment, regulated data).
- Breaking change to a published [API specification](../phases/3-design/artifacts/api-specification.md) or [data model](../phases/3-design/artifacts/data-model.md).
- Production database migration proposed.
- Acceptance-criteria ambiguity detected during implementation.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Build exit checklist](../phases/5-build/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your source control and IDE**, pair-programming on the [feature code](../phases/5-build/artifacts/feature-code.md): design, generation, and critique of non-trivial logic; review of peer changes before they become [reviewed code](../phases/5-build/artifacts/reviewed-code.md) and [merged code in main branch](../phases/5-build/artifacts/merged-code-in-main-branch.md).
- **In your source control and test framework**, shape test design for the [automated test suite](../phases/5-build/artifacts/automated-test-suite.md) — edge cases, coverage gaps against acceptance criteria, tricky integration scenarios.
- **In your observability / telemetry SDKs**, decide what to emit and how to structure it as [instrumented code](../phases/5-build/artifacts/instrumented-code.md); reason about the [verified KPI telemetry](../phases/6-verify/artifacts/verified-kpi-telemetry.md) story end-to-end.
- **In your issue tracker**, debug reproduced issues: hypothesis generation, log and trace reading, diff analysis; draft fixes feeding [bug reports](../phases/9-iterate/artifacts/bug-reports.md) and the [patched application release](../phases/9-iterate/artifacts/patched-application-release.md).
- **In your feature-flag platform**, reason about rollout/rollback strategy for the [feature flag plan](../phases/4-plan/artifacts/feature-flag-plan.md) and the blast radius of staged changes.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your dependency / supply-chain tooling and CI/CD pipeline**, apply routine dependency updates and security patches through CI-gated PRs; produce the [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md) flow and keep the [vulnerability scan report](../phases/5-build/artifacts/vulnerability-scan-report.md) current.
- **In your source control and CI/CD pipeline**, scaffold modules and boilerplate from specs, generate unit tests for well-specified functions, and feed the [automated test suite](../phases/5-build/artifacts/automated-test-suite.md) — everything CI-gated and human-reviewed before merge.
- **In your CI/CD pipeline**, auto-remediate trivial lint / static-analysis findings and keep the [lint/static-analysis report](../phases/5-build/artifacts/lint-static-analysis-report.md) clean.
- **In your generated documentation site**, keep [generated API docs](../phases/5-build/artifacts/generated-api-docs.md) in sync with code and flag stale or unexplained exports for your attention.
- **In your package / artifact registry**, maintain [demo assets](../phases/7-launch/artifacts/demo-assets.md) and sample data against the current [released product in production](../phases/7-launch/artifacts/released-product-in-production.md).

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **12** artifacts/outcomes as primary (A) and co-own **14** (R)._

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [effort estimates](../phases/2-define/artifacts/effort-estimates.md) | Estimation / sizing |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [API specification](../phases/3-design/artifacts/api-specification.md) | API / interface contract design |
| **R** | [build-ready package](../phases/3-design/artifacts/build-ready-package.md) | Design → engineering handoff review |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [enabler backlog](../phases/4-plan/artifacts/enabler-backlog.md) | Architecture runway / technical enablers |
| **R** | [feature flag plan](../phases/4-plan/artifacts/feature-flag-plan.md) | Feature flag strategy |
| **R** | [working CI/CD pipeline](../phases/4-plan/artifacts/working-ci-cd-pipeline.md) | CI/CD pipeline setup |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [vulnerability scan report](../phases/5-build/artifacts/vulnerability-scan-report.md) | Security scanning (SAST/SCA) |
| **A** | [implemented workitems](../phases/5-build/artifacts/implemented-workitems.md) | Review & code workitems |
| **A** | [feature code](../phases/5-build/artifacts/feature-code.md) | New feature development |
| **A** | [reviewed code](../phases/5-build/artifacts/reviewed-code.md) | Code review |
| **A** | [merged code in main branch](../phases/5-build/artifacts/merged-code-in-main-branch.md) | Merge code |
| **A** | [lint/static-analysis report](../phases/5-build/artifacts/lint-static-analysis-report.md) | Static analysis / linting |
| **A** | [instrumented code](../phases/5-build/artifacts/instrumented-code.md) | Telemetry implementation |
| **A** | [generated API docs](../phases/5-build/artifacts/generated-api-docs.md) | Inline / API code documentation |
| **R** | [integration test results](../phases/5-build/artifacts/integration-test-results.md) | Integration testing |
| **A** | [requirements questions log](../phases/5-build/artifacts/requirements-questions-log.md) | Raise requirements questions & impediments |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [migration runbook validation](../phases/6-verify/artifacts/migration-runbook-validation.md) | Data migration dress rehearsal |
| **R** | [triaged UAT defects](../phases/6-verify/artifacts/triaged-uat-defects.md) | UAT defect triage |
| **R** | [verified KPI telemetry](../phases/6-verify/artifacts/verified-kpi-telemetry.md) | Verify KPI telemetry emission |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [demo assets](../phases/7-launch/artifacts/demo-assets.md) | Create sample data & demos |
| **R** | [connected KPI data pipeline](../phases/7-launch/artifacts/connected-kpi-data-pipeline.md) | Wire KPI events into dashboard |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [root cause analysis report](../phases/8-operate/artifacts/root-cause-analysis-report.md) | Root cause analysis |
| **R** | [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md) | Security patching |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [experiment results](../phases/9-iterate/artifacts/experiment-results.md) | A/B testing / experimentation |
| **R** | [prioritized tech-debt list](../phases/9-iterate/artifacts/prioritized-tech-debt-list.md) | Technical debt backlog grooming |
| **A** | [patched application release](../phases/9-iterate/artifacts/patched-application-release.md) | Bugfix application updates |

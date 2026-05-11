# 7. Site Reliability Engineer (SRE)
- **Description:** Applies software engineering to operations; owns SLIs/SLOs, on-call, capacity, observability, and release engineering.
- **Business purpose:** Keeps services reliable, performant, and cost-efficient while preserving feature velocity.
- **Typically reports to:** VP/Director of Infrastructure, Platform, or Engineering.
- **Project goals:** SLOs met within error budget · automated progressive rollout · manageable on-call load · capacity headroom.


## AI teammate

**Purpose:** Keep services reliable, performant, and cost-efficient — own SLIs/SLOs, observability, capacity, and release engineering while preserving feature velocity.

**Assistive AI (tight collaboration):** Drafts and iterates on the [service-level objectives](../phases/4-plan/artifacts/service-level-objectives.md), [changelog review process](../phases/4-plan/artifacts/changelog-review-process.md), [reviewed change log](../phases/5-build/artifacts/reviewed-change-log.md), [resilience test results](../phases/6-verify/artifacts/resilience-test-results.md), [incident investigation report](../phases/8-operate/artifacts/incident-investigation-report.md), [root cause analysis report](../phases/8-operate/artifacts/root-cause-analysis-report.md), [incident postmortem](../phases/8-operate/artifacts/incident-postmortem.md), and [DR test results](../phases/8-operate/artifacts/dr-test-results.md) with a human SRE holding the pen — error-budget judgment, game-day design, incident hypothesis generation.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can maintain the [provisioned environments](../phases/4-plan/artifacts/provisioned-environments.md), [working CI/CD pipeline](../phases/4-plan/artifacts/working-ci-cd-pipeline.md), [verified KPI telemetry](../phases/6-verify/artifacts/verified-kpi-telemetry.md), [connected KPI data pipeline](../phases/7-launch/artifacts/connected-kpi-data-pipeline.md), [monitoring dashboards & alerts](../phases/8-operate/artifacts/monitoring-dashboards-alerts.md), [cost & capacity report](../phases/8-operate/artifacts/cost-capacity-report.md), and the [prioritized prod issue log](../phases/8-operate/artifacts/prioritized-prod-issue-log.md) — routine toil, alert-noise reduction, triage — within pre-approved runbook steps. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not sign off on the [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md) automatically — AI prepares, human signs. Does not approve the [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md) or [continue/rollback decision](../phases/7-launch/outcomes/continue-rollback-decision.md). Does not take action on production systems during a live incident without human authorization beyond pre-approved runbook steps.

**Inputs:** [Architecture document](../phases/3-design/artifacts/architecture-document.md), [NFR document](../phases/2-define/artifacts/nfr-document.md), [deployment runbook](../phases/4-plan/artifacts/deployment-runbook.md), [feature flag plan](../phases/4-plan/artifacts/feature-flag-plan.md), [telemetry plan](../phases/4-plan/artifacts/telemetry-plan.md), live telemetry, incident signals, cost and usage metrics.

**Outputs:** The A artifacts above, plus contributions to [migration runbook validation](../phases/6-verify/artifacts/migration-runbook-validation.md), [performance test report](../phases/6-verify/artifacts/performance-test-report.md), [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md), and on-call triage output.

**Escalation triggers:**
- SLO breach or error-budget burn exceeds policy threshold.
- Sev-2 or higher incident, or suspected data loss/corruption.
- Production DB migration, schema change, or destructive data operation proposed.
- Capacity headroom drops below threshold or cost anomaly exceeds policy.
- Chaos/DR test exposes unmitigated single-point-of-failure.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Operate exit checklist](../phases/8-operate/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your alerting / on-call platform and incident management tool**, hypothesis generation and log/trace correlation during an active incident; draft the [incident investigation report](../phases/8-operate/artifacts/incident-investigation-report.md), [root cause analysis report](../phases/8-operate/artifacts/root-cause-analysis-report.md), and blame-free [incident postmortem](../phases/8-operate/artifacts/incident-postmortem.md) from the timeline.
- **In your observability stack**, design and iterate on [service-level objectives](../phases/4-plan/artifacts/service-level-objectives.md) and the SLIs that feed them; stress-test error-budget assumptions before you commit.
- **In your chaos / load-testing tools**, design game-day scenarios and interpret results into [resilience test results](../phases/6-verify/artifacts/resilience-test-results.md) and [DR test results](../phases/8-operate/artifacts/dr-test-results.md) — where the system's weakest, what compensations work.
- **In your runbook repository and CI/CD platform**, draft the [deployment runbook](../phases/4-plan/artifacts/deployment-runbook.md), [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md) package, and the [changelog review process](../phases/4-plan/artifacts/changelog-review-process.md); review the [reviewed change log](../phases/5-build/artifacts/reviewed-change-log.md) with production risk in mind.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your infrastructure-as-code and CI/CD platform**, routine toil: certificate rotation, scheduled scaling, log-retention enforcement, cleanup of stale resources across [provisioned environments](../phases/4-plan/artifacts/provisioned-environments.md) and the [working CI/CD pipeline](../phases/4-plan/artifacts/working-ci-cd-pipeline.md).
- **In your observability stack and alerting platform**, alert-noise reduction and alert-to-runbook mapping; keep [monitoring dashboards & alerts](../phases/8-operate/artifacts/monitoring-dashboards-alerts.md) and [verified KPI telemetry](../phases/6-verify/artifacts/verified-kpi-telemetry.md) consistent as services change.
- **In your incident management tool**, triage new production signals into the [prioritized prod issue log](../phases/8-operate/artifacts/prioritized-prod-issue-log.md) with severity, owner, and duplicates identified.
- **In your CI/CD platform**, analyze the [reviewed change log](../phases/5-build/artifacts/reviewed-change-log.md) before release for blast-radius heuristics, flag high-risk changes, and auto-propose deployment windows.
- **In your chaos / load-testing tools**, scheduled resilience drills and capacity-headroom verification against current load; produce refreshed [DR test results](../phases/8-operate/artifacts/dr-test-results.md).

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **16** artifacts/outcomes as primary (A) and co-own **7** (R)._

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [security/compliance approval](../phases/3-design/outcomes/security-compliance-approval.md) | Security & compliance review |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [provisioned environments](../phases/4-plan/artifacts/provisioned-environments.md) | Infrastructure / environment provisioning |
| **A** | [working CI/CD pipeline](../phases/4-plan/artifacts/working-ci-cd-pipeline.md) | CI/CD pipeline setup |
| **A** | [service-level objectives](../phases/4-plan/artifacts/service-level-objectives.md) | SLA / SLO definition |
| **R** | [deployment runbook](../phases/4-plan/artifacts/deployment-runbook.md) | Rollout & rollback plan |
| **A** | [changelog review process](../phases/4-plan/artifacts/changelog-review-process.md) | Change-review process setup |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [reviewed change log](../phases/5-build/artifacts/reviewed-change-log.md) | Review incoming changes (changelog) |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [resilience test results](../phases/6-verify/artifacts/resilience-test-results.md) | Chaos / resilience testing |
| **R** | [migration runbook validation](../phases/6-verify/artifacts/migration-runbook-validation.md) | Data migration dress rehearsal |
| **A** | [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md) | Operational readiness review |
| **R** | [performance test report](../phases/6-verify/artifacts/performance-test-report.md) | Performance / load testing |
| **A** | [verified KPI telemetry](../phases/6-verify/artifacts/verified-kpi-telemetry.md) | Verify KPI telemetry emission |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [stabilized launch window](../phases/7-launch/outcomes/stabilized-launch-window.md) | Launch war room / hypercare |
| **A** | [connected KPI data pipeline](../phases/7-launch/artifacts/connected-kpi-data-pipeline.md) | Wire KPI events into dashboard |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [monitoring dashboards & alerts](../phases/8-operate/artifacts/monitoring-dashboards-alerts.md) | Application monitoring |
| **A** | [incident investigation report](../phases/8-operate/artifacts/incident-investigation-report.md) | Investigate production errors |
| **A** | [root cause analysis report](../phases/8-operate/artifacts/root-cause-analysis-report.md) | Root cause analysis |
| **A** | [incident postmortem](../phases/8-operate/artifacts/incident-postmortem.md) | Incident response / on-call |
| **A** | [DR test results](../phases/8-operate/artifacts/dr-test-results.md) | Backup & disaster-recovery testing |
| **A** | [cost & capacity report](../phases/8-operate/artifacts/cost-capacity-report.md) | Cost / capacity monitoring |
| **A** | [prioritized prod issue log](../phases/8-operate/artifacts/prioritized-prod-issue-log.md) | Triage & log production issues for developer fixes |
| **R** | [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md) | Security patching |
| **R** | [security monitoring alerts](../phases/8-operate/artifacts/security-monitoring-alerts.md) | Security monitoring & SIEM operations |

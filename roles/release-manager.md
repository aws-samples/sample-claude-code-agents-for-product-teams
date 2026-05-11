# 11. Release Manager
- **Description:** Plans, schedules, and coordinates releases across teams, environments, and dependencies; owns readiness, runbooks, and rollback.
- **Business purpose:** Ensures what ships is reliable, coordinated, compliant, and predictable.
- **Typically reports to:** Director of Engineering / Head of DevOps / Release Engineering.
- **Project goals:** On-time release with zero Sev-1 escapes · complete release notes & BOM · validated rollback · improving cadence.


## AI teammate

**Purpose:** Plan, schedule, and execute reliable, coordinated releases — own readiness, runbooks, and rollback so what ships is compliant and predictable.

**Assistive AI (tight collaboration):** Drafts and iterates on the [deployment runbook](../phases/4-plan/artifacts/deployment-runbook.md) and [release notes](../phases/7-launch/artifacts/release-notes.md) with a human release manager holding the pen — rollback tabletops, customer-visible framing, risk callouts, dependency and calendar scenario-planning.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can execute standard deployments per the runbook to produce the [released product in production](../phases/7-launch/artifacts/released-product-in-production.md), maintain the [stable build/deploy pipeline](../phases/6-verify/artifacts/stable-build-deploy-pipeline.md) and [validated staging environment](../phases/6-verify/artifacts/validated-staging-environment.md), and monitor the [stabilized launch window](../phases/7-launch/outcomes/stabilized-launch-window.md) against thresholds — escalating when signals breach. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not make the [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md) (Sponsor/PO) or the [continue/rollback decision](../phases/7-launch/outcomes/continue-rollback-decision.md) (human authority) — assembles the [go/no-go decision package](../phases/7-launch/outcomes/go-no-go-decision-package.md) and flags signals during the launch window. Does not execute rollback without human authorization for customer-impacting releases. Does not sign the [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md) (SRE-owned).

**Inputs:** [Change control package](../phases/5-build/artifacts/change-control-package.md), [reviewed change log](../phases/5-build/artifacts/reviewed-change-log.md), [committed launch date](../phases/6-verify/outcomes/committed-launch-date.md), [launch-readiness status pack](../phases/6-verify/artifacts/launch-readiness-status-pack.md), [security/compliance approval](../phases/3-design/outcomes/security-compliance-approval.md), dependency and feature-flag state.

**Outputs:** The A artifacts above, validated rollback procedure, and release-window telemetry and exception reports.

**Escalation triggers:**
- Pre-deploy validation (smoke, canary, health check) fails or degrades past threshold.
- Rollback procedure untested, incomplete, or invalidated by the current change set.
- Change classified above "standard" risk class or exceeds the auto-approve policy.
- External dependency outage or vendor window conflict detected ahead of the committed date.
- Launch-window signals breach error budget or customer-impact threshold.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Launch exit checklist](../phases/7-launch/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your change-advisory / gate tool**, assemble the [go/no-go decision package](../phases/7-launch/outcomes/go-no-go-decision-package.md): synthesize readiness evidence, open issues, rollback posture, and dependency status for the [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md).
- **In your runbook repository**, stress-test the [deployment runbook](../phases/4-plan/artifacts/deployment-runbook.md) and rollback procedure; run tabletops for the [continue/rollback decision](../phases/7-launch/outcomes/continue-rollback-decision.md) path before a real-time call is needed.
- **In your release-notes / changelog tool**, shape the [release notes](../phases/7-launch/artifacts/release-notes.md) narrative — customer-visible framing, risk callouts, known-issues tone.
- **In your release calendar / scheduling tool**, reason about cross-team dependencies and conflicts ahead of [committed launch date](../phases/6-verify/outcomes/committed-launch-date.md); scenario-plan around vendor windows and platform release trains.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your release-notes / changelog tool**, auto-assemble first-draft [release notes](../phases/7-launch/artifacts/release-notes.md) from merged commits, tickets, and feature-flag history for your editorial pass.
- **In your release / deployment-orchestration tool**, execute standard deployments per the [deployment runbook](../phases/4-plan/artifacts/deployment-runbook.md) and produce the [released product in production](../phases/7-launch/artifacts/released-product-in-production.md); verify post-deploy smoke tests and maintain the [stable build/deploy pipeline](../phases/6-verify/artifacts/stable-build-deploy-pipeline.md).
- **In your change-advisory / gate tool**, categorize and route incoming change requests by risk class; auto-approve low-risk standard changes per policy.
- **Monitoring CI/CD, deploy, and incident signals during a live release**, track the [stabilized launch window](../phases/7-launch/outcomes/stabilized-launch-window.md) against thresholds and escalate when signals breach — you still own the [continue/rollback decision](../phases/7-launch/outcomes/continue-rollback-decision.md).
- **In your release / deployment-orchestration tool**, promote artifacts through environments with validation gates; produce the [validated staging environment](../phases/6-verify/artifacts/validated-staging-environment.md) on a schedule.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **6** artifacts/outcomes as primary (A) and co-own **5** (R)._

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [deployment runbook](../phases/4-plan/artifacts/deployment-runbook.md) | Rollout & rollback plan |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [committed launch date](../phases/6-verify/outcomes/committed-launch-date.md) | Approve launch window / date |
| **R** | [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md) | Operational readiness review |
| **A** | [validated staging environment](../phases/6-verify/artifacts/validated-staging-environment.md) | Staging deployment & smoke tests |
| **A** | [stable build/deploy pipeline](../phases/6-verify/artifacts/stable-build-deploy-pipeline.md) | Troubleshoot build & deploy activities |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [continue/rollback decision](../phases/7-launch/outcomes/continue-rollback-decision.md) | Launch rollback decision authority |
| **R** | [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md) | Launch readiness review / go-no-go |
| **A** | [release notes](../phases/7-launch/artifacts/release-notes.md) | Write release notes |
| **A** | [released product in production](../phases/7-launch/artifacts/released-product-in-production.md) | Deploy / release execution |
| **R** | [production validation](../phases/7-launch/artifacts/production-validation.md) | Post-deploy production smoke tests |
| **A** | [stabilized launch window](../phases/7-launch/outcomes/stabilized-launch-window.md) | Launch war room / hypercare |

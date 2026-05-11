# 2. Product Owner
- **Description:** Owns the backlog and maximizes value delivered each iteration; single empowered decision-maker for "what to build next."
- **Business purpose:** Keeps the delivery team always working on the highest-value items.
- **Typically reports to:** Head of Product / Director of Product Management.
- **Project goals:** Clear, ordered, refined backlog · validated increments · stakeholder alignment on sequence & trade-offs.


## AI teammate

**Purpose:** Keep the backlog clear, ordered, and refined so the delivery team is always working on the highest-value items against a coherent roadmap.

**Assistive AI (tight collaboration):** Drafts and iterates on the [opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md), [vision statement](../phases/1-discover/artifacts/vision-statement.md), [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md), [product roadmap](../phases/2-define/artifacts/product-roadmap.md), [KPI definitions](../phases/2-define/artifacts/kpi-definitions.md), [MVP scope statement](../phases/2-define/artifacts/mvp-scope-statement.md), [delivery-ready work items](../phases/4-plan/artifacts/delivery-ready-work-items.md), [updated roadmap](../phases/9-iterate/artifacts/updated-roadmap.md), [KPI performance report](../phases/9-iterate/artifacts/kpi-performance-report.md), [experiment results](../phases/9-iterate/artifacts/experiment-results.md), and [deprecation plan](../phases/9-iterate/artifacts/deprecation-plan.md) with a human PO holding the pen — problem framing, sequencing trade-offs, first-pass acceptance criteria.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can groom the [prioritized backlog](../phases/4-plan/artifacts/prioritized-backlog.md) (dedupe, staleness flags, field consistency), cluster raw feedback into the [next-cycle opportunity backlog](../phases/9-iterate/artifacts/next-cycle-opportunity-backlog.md), and convert triaged bug signals into a [prioritized bug list](../phases/9-iterate/artifacts/prioritized-bug-list.md) ready for your prioritization pass. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not make the [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md) alone — it's A for PO but is a committed organizational decision with Sponsor and Security/Legal gates. Does not own [business case](../phases/1-discover/artifacts/business-case.md) approval, [pricing & packaging plan](../phases/7-launch/artifacts/pricing-packaging-plan.md), or [legal approval](../phases/7-launch/outcomes/legal-approval.md). Does not accept increments ([accepted increments](../phases/5-build/outcomes/accepted-increments.md)) without the evidence that the acceptance criteria were met.

**Inputs:** [Market analysis report](../phases/1-discover/artifacts/market-analysis-report.md), [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), [user personas](../phases/1-discover/artifacts/user-personas.md), [feedback insights report](../phases/9-iterate/artifacts/feedback-insights-report.md), [adoption metrics](../phases/9-iterate/artifacts/adoption-metrics.md), experiment telemetry, and stakeholder inputs.

**Outputs:** The A artifacts above; authoritative ordering of the [prioritized backlog](../phases/4-plan/artifacts/prioritized-backlog.md) and [prioritized bug list](../phases/9-iterate/artifacts/prioritized-bug-list.md).

**Escalation triggers:**
- Scope change large enough to alter the [MVP scope statement](../phases/2-define/artifacts/mvp-scope-statement.md) or baseline commitments.
- Experiment result that invalidates the [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md).
- KPI trending past a threshold the business case depends on.
- Conflicting stakeholder priorities that require a cross-portfolio decision.
- Customer-facing copy or launch-visible content drafted for an external audience.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Plan exit checklist](../phases/4-plan/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your knowledge base / wiki**, draft and iterate on the [vision statement](../phases/1-discover/artifacts/vision-statement.md), [opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md), [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md), and [MVP scope statement](../phases/2-define/artifacts/mvp-scope-statement.md) — sharpen problem framing and surface assumptions worth testing.
- **In your roadmapping tool**, explore sequencing trade-offs for the [product roadmap](../phases/2-define/artifacts/product-roadmap.md) and [updated roadmap](../phases/9-iterate/artifacts/updated-roadmap.md) — what-if simulations, impact on KPIs, dependency conflicts.
- **In your backlog / work-tracking tool**, decompose epics into [delivery-ready work items](../phases/4-plan/artifacts/delivery-ready-work-items.md) and propose first-pass [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md) for your review.
- **In your analytics / experimentation platform**, design experiments and interpret [experiment results](../phases/9-iterate/artifacts/experiment-results.md) and the [KPI performance report](../phases/9-iterate/artifacts/kpi-performance-report.md) against the [KPI definitions](../phases/2-define/artifacts/kpi-definitions.md) you committed to.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your backlog / work-tracking tool**, grooming the [prioritized backlog](../phases/4-plan/artifacts/prioritized-backlog.md): dedupe, flag staleness, keep labels and fields consistent, surface candidates for prioritization review.
- **In your customer feedback system**, cluster and tag raw signals into a [feedback insights report](../phases/9-iterate/artifacts/feedback-insights-report.md) and propose additions to the [next-cycle opportunity backlog](../phases/9-iterate/artifacts/next-cycle-opportunity-backlog.md).
- **In your analytics / experimentation platform**, maintain the [live launch KPI dashboard](../phases/7-launch/outcomes/live-launch-kpi-dashboard.md) and [adoption metrics](../phases/9-iterate/artifacts/adoption-metrics.md); alert you when a metric crosses your threshold.
- **In your backlog tool**, convert triaged bug signals into a [prioritized bug list](../phases/9-iterate/artifacts/prioritized-bug-list.md) ready for your prioritization pass.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **19** artifacts/outcomes as primary (A) and co-own **16** (R)._

### [1. Discover](../phases/1-discover/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md) | Ideation / opportunity framing |
| **A** | [vision statement](../phases/1-discover/artifacts/vision-statement.md) | Document product vision |
| **A** | [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md) | Problem-solution fit hypothesis |
| **A** | [business case](../phases/1-discover/artifacts/business-case.md) | Business planning |
| **A** | [stakeholder map](../phases/1-discover/artifacts/stakeholder-map.md) | Stakeholder identification & alignment |
| **A** | [feasibility memo](../phases/1-discover/artifacts/feasibility-memo.md) | Early feasibility / risk assessment |

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [signed product charter](../phases/2-define/artifacts/signed-product-charter.md) | Approve product charter |
| **R** | [commercial model decision](../phases/2-define/outcomes/commercial-model-decision.md) | Commercial / delivery model decision |
| **A** | [product roadmap](../phases/2-define/artifacts/product-roadmap.md) | Create & manage product roadmap |
| **A** | [KPI definitions](../phases/2-define/artifacts/kpi-definitions.md) | Success metrics / KPI definition |
| **A** | [MVP scope statement](../phases/2-define/artifacts/mvp-scope-statement.md) | MVP / scope decision |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [validated business-value alignment](../phases/3-design/artifacts/validated-business-value-alignment.md) | Design-to-business-case alignment review |
| **R** | [confirmed scope/budget or change request](../phases/3-design/outcomes/confirmed-scope-budget-or-change-request.md) | Budget & scope reality check |
| **R** | [approved design package](../phases/3-design/outcomes/approved-design-package.md) | Design review & sign-off |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [prioritized backlog](../phases/4-plan/artifacts/prioritized-backlog.md) | Manage product backlog |
| **A** | [delivery-ready work items](../phases/4-plan/artifacts/delivery-ready-work-items.md) | Backlog decomposition (features → work items) |
| **R** | [service-level objectives](../phases/4-plan/artifacts/service-level-objectives.md) | SLA / SLO definition |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [scope-change decisions](../phases/5-build/outcomes/scope-change-decisions.md) | Scope discipline / change control |
| **A** | [accepted increments](../phases/5-build/outcomes/accepted-increments.md) | Progress review & increment acceptance |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [approved launch cohort](../phases/6-verify/outcomes/approved-launch-cohort.md) | Approve beta / early-access cohort |
| **R** | [approved known-issues & risk acceptance](../phases/6-verify/outcomes/approved-known-issues-risk-acceptance.md) | Approve launch risk posture |
| **R** | [UAT/beta sign-off](../phases/6-verify/outcomes/uat-beta-sign-off.md) | Pre-launch validation — UAT / beta |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md) | Launch readiness review / go-no-go |
| **R** | [legal approval](../phases/7-launch/outcomes/legal-approval.md) | Legal & compliance final sign-off |
| **R** | [pre-launch metrics baseline](../phases/7-launch/artifacts/pre-launch-metrics-baseline.md) | Launch baseline snapshot |
| **R** | [pricing & packaging plan](../phases/7-launch/artifacts/pricing-packaging-plan.md) | Pricing & packaging decision |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [business review decisions](../phases/8-operate/outcomes/business-review-decisions.md) | Business review meeting |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [updated roadmap](../phases/9-iterate/artifacts/updated-roadmap.md) | Roadmap refresh |
| **A** | [KPI performance report](../phases/9-iterate/artifacts/kpi-performance-report.md) | KPI / success-metric tracking |
| **R** | [adoption metrics](../phases/9-iterate/artifacts/adoption-metrics.md) | Feature adoption analysis |
| **A** | [experiment results](../phases/9-iterate/artifacts/experiment-results.md) | A/B testing / experimentation |
| **R** | [feedback insights report](../phases/9-iterate/artifacts/feedback-insights-report.md) | Aggregate & analyze feedback |
| **A** | [next-cycle opportunity backlog](../phases/9-iterate/artifacts/next-cycle-opportunity-backlog.md) | Hand off insights to Discover |
| **A** | [prioritized bug list](../phases/9-iterate/artifacts/prioritized-bug-list.md) | Prioritize bug fixes |
| **A** | [deprecation plan](../phases/9-iterate/artifacts/deprecation-plan.md) | Sunset / deprecation |

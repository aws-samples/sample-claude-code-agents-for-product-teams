# 3. Business Analyst
- **Description:** Elicits, analyzes, and documents needs; models as-is/to-be processes; validates that solutions deliver benefits.
- **Business purpose:** Bridges business strategy and technical delivery so teams solve the right problem.
- **Typically reports to:** BA Practice Lead, PMO, or Head of Product.
- **Project goals:** Traceable, validated requirements · scope discipline · benefits realization post-launch.


## AI teammate

**Purpose:** Elicit, analyze, and document requirements — and track benefits realization — so the delivery team solves the right problem and the business can see whether it paid off.

**Assistive AI (tight collaboration):** Drafts and iterates on the [requirements document](../phases/2-define/artifacts/requirements-document.md), [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md), [process models](../phases/2-define/artifacts/process-models.md), [change impact assessment](../phases/2-define/artifacts/change-impact-assessment.md), [capability gap report](../phases/2-define/artifacts/capability-gap-report.md), [ROI model](../phases/1-discover/artifacts/roi-model.md), and [benefits plan](../phases/4-plan/artifacts/benefits-plan.md) with a human BA holding the pen — hypothesis framing, assumption challenge, stakeholder conflict surfacing.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can maintain the [traceability matrix](../phases/2-define/artifacts/traceability-matrix.md) as requirements and tests change, and produce the recurring [business performance report](../phases/8-operate/artifacts/business-performance-report.md) and [ongoing benefits tracking](../phases/8-operate/artifacts/ongoing-benefits-tracking.md) against the benefits plan. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not approve requirements — the [approved requirements](../phases/2-define/outcomes/approved-requirements.md) outcome requires stakeholder sign-off. Does not commit the business case; the Product Sponsor owns that approval. Reads but does not modify the [NFR document](../phases/2-define/artifacts/nfr-document.md) (Architect-owned) or the [applicable-regulations list](../phases/2-define/artifacts/applicable-regulations-list.md) (Security-owned).

**Inputs:** [Opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md), [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), [vision statement](../phases/1-discover/artifacts/vision-statement.md), [user personas](../phases/1-discover/artifacts/user-personas.md), interview / workshop transcripts, [stakeholder map](../phases/1-discover/artifacts/stakeholder-map.md), and live analytics and VoC feeds for benefits tracking.

**Outputs:** The A artifacts above, plus [design-requirements validation](../phases/3-design/artifacts/design-requirements-validation.md), [updated traceability matrix](../phases/3-design/artifacts/updated-traceability-matrix.md), [updated ROI model](../phases/3-design/artifacts/updated-roi-model.md), [benefits-readiness report](../phases/6-verify/artifacts/benefits-readiness-report.md), [benefits-shortfall report](../phases/9-iterate/artifacts/benefits-shortfall-report.md), and [updated business case](../phases/9-iterate/artifacts/updated-business-case.md).

**Escalation triggers:**
- Requirements ambiguity that would affect acceptance criteria or test coverage.
- Conflicting requirements between two named stakeholders or segments.
- Change impact crosses a regulated workflow, business unit, or SLA boundary.
- Benefits tracking indicates the business case is off by more than the sponsor's threshold.
- Scope change large enough to require a [change control package](../phases/5-build/artifacts/change-control-package.md).

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Define exit checklist](../phases/2-define/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your requirements / ALM tool**, draft the [requirements document](../phases/2-define/artifacts/requirements-document.md) and [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md) from notes and interview transcripts; stress-test for ambiguity, conflicts, and missing edge cases before stakeholder review.
- **In your process modeling tool**, synthesize interview / workshop notes into first-pass [process models](../phases/2-define/artifacts/process-models.md) and [capability gap report](../phases/2-define/artifacts/capability-gap-report.md); surface impacts for the [change impact assessment](../phases/2-define/artifacts/change-impact-assessment.md).
- **In your spreadsheet / financial modeling tool**, work through the [ROI model](../phases/1-discover/artifacts/roi-model.md), [updated ROI model](../phases/3-design/artifacts/updated-roi-model.md), and [benefits plan](../phases/4-plan/artifacts/benefits-plan.md) — sensitivity analysis, assumption challenge, scenario comparison ahead of the [updated business case](../phases/9-iterate/artifacts/updated-business-case.md).
- **In your collaboration / whiteboarding tool**, shape the [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), [journey map / service blueprint](../phases/3-design/artifacts/journey-map-service-blueprint.md), and [stakeholder workshop outcomes](../phases/2-define/artifacts/stakeholder-workshop-outcomes.md) — hypothesis generation, synthesis, and gap-spotting.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your requirements / ALM tool**, maintain the [traceability matrix](../phases/2-define/artifacts/traceability-matrix.md): link requirements to acceptance criteria, tests, and design elements as they're authored or changed; flag orphans and coverage gaps.
- **Reading requirements and test inventories**, continuously detect coverage gaps against the [test-to-requirement coverage map](../phases/2-define/artifacts/test-to-requirement-coverage-map.md) and [design-requirements validation](../phases/3-design/artifacts/design-requirements-validation.md).
- **In your BI / reporting platform**, produce the recurring [business performance report](../phases/8-operate/artifacts/business-performance-report.md) and [ongoing benefits tracking](../phases/8-operate/artifacts/ongoing-benefits-tracking.md) against the benefits plan; feed the [benefits-realization report](../phases/9-iterate/artifacts/benefits-realization-report.md) and [benefits-shortfall report](../phases/9-iterate/artifacts/benefits-shortfall-report.md).
- **Pulling from support, feedback, and analytics sources**, first-pass synthesis of [support/VoC trend analysis](../phases/8-operate/artifacts/support-voc-trend-analysis.md) and candidate inputs to the [updated business case](../phases/9-iterate/artifacts/updated-business-case.md) reforecast.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **36** artifacts/outcomes as primary (A) and co-own **11** (R)._

### [1. Discover](../phases/1-discover/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [market analysis report](../phases/1-discover/artifacts/market-analysis-report.md) | Market & customer research |
| **A** | [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md) | User / problem validation |
| **A** | [opportunity sizing](../phases/1-discover/artifacts/opportunity-sizing.md) | Problem-opportunity analysis |
| **A** | [ROI model](../phases/1-discover/artifacts/roi-model.md) | Cost-benefit / ROI analysis |
| **R** | [user personas](../phases/1-discover/artifacts/user-personas.md) | Persona / target user definition |

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [requirements document](../phases/2-define/artifacts/requirements-document.md) | Draft requirements |
| **A** | [approved requirements](../phases/2-define/outcomes/approved-requirements.md) | Review & iterate on requirements |
| **A** | [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md) | Acceptance criteria authoring |
| **A** | [data inventory & classification](../phases/2-define/artifacts/data-inventory-classification.md) | Data requirements & classification |
| **A** | [traceability matrix](../phases/2-define/artifacts/traceability-matrix.md) | Requirements traceability matrix |
| **A** | [solution recommendation](../phases/2-define/artifacts/solution-recommendation.md) | Solution options evaluation |
| **A** | [process models](../phases/2-define/artifacts/process-models.md) | Business process modeling (as-is / to-be) |
| **A** | [change impact assessment](../phases/2-define/artifacts/change-impact-assessment.md) | Change impact analysis |
| **A** | [capability gap report](../phases/2-define/artifacts/capability-gap-report.md) | Gap analysis |
| **R** | [NFR document](../phases/2-define/artifacts/nfr-document.md) | Non-functional requirements definition |
| **R** | [applicable-regulations list](../phases/2-define/artifacts/applicable-regulations-list.md) | Regulatory / compliance scope assessment |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [validated business-value alignment](../phases/3-design/artifacts/validated-business-value-alignment.md) | Design-to-business-case alignment review |
| **A** | [design-requirements validation](../phases/3-design/artifacts/design-requirements-validation.md) | Validate design against requirements |
| **A** | [updated traceability matrix](../phases/3-design/artifacts/updated-traceability-matrix.md) | Update traceability (requirements → design) |
| **A** | [vendor evaluation scorecard](../phases/3-design/artifacts/vendor-evaluation-scorecard.md) | Vendor / buy option evaluation |
| **A** | [business-rules catalog](../phases/3-design/artifacts/business-rules-catalog.md) | Business rules documentation |
| **A** | [updated ROI model](../phases/3-design/artifacts/updated-roi-model.md) | Refine cost-benefit model with design-era data |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [delivery-ready work items](../phases/4-plan/artifacts/delivery-ready-work-items.md) | Backlog decomposition (features → work items) |
| **A** | [benefits plan](../phases/4-plan/artifacts/benefits-plan.md) | Benefits realization plan |
| **A** | [stakeholder comms plan](../phases/4-plan/artifacts/stakeholder-comms-plan.md) | Stakeholder communication plan |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [business-case reconfirmation or reset](../phases/5-build/outcomes/business-case-reconfirmation-or-reset.md) | Re-validate business case vs. emerging reality |
| **A** | [clarified requirements](../phases/5-build/artifacts/clarified-requirements.md) | Requirements clarification support |
| **A** | [change impact report](../phases/5-build/artifacts/change-impact-report.md) | Scope-change impact analysis |
| **A** | [assumptions & benefits-tracking log](../phases/5-build/artifacts/assumptions-benefits-tracking-log.md) | In-flight benefits & assumptions tracking |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [UAT coordination & results](../phases/6-verify/artifacts/uat-coordination-results.md) | UAT coordination with business users |
| **A** | [benefits-readiness report](../phases/6-verify/artifacts/benefits-readiness-report.md) | Benefits-readiness assessment |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [pre-launch metrics baseline](../phases/7-launch/artifacts/pre-launch-metrics-baseline.md) | Launch baseline snapshot |
| **A** | [live launch KPI dashboard](../phases/7-launch/outcomes/live-launch-kpi-dashboard.md) | Launch KPI dashboard setup |
| **A** | [rolled-out process changes](../phases/7-launch/artifacts/rolled-out-process-changes.md) | Process change rollout to impacted business teams |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [margin & CAC/LTV report](../phases/8-operate/artifacts/margin-cac-ltv-report.md) | Unit-economics / margin review |
| **A** | [business performance report](../phases/8-operate/artifacts/business-performance-report.md) | Business-metric reporting cadence |
| **A** | [ongoing benefits tracking](../phases/8-operate/artifacts/ongoing-benefits-tracking.md) | Value-realization tracking |
| **A** | [support/VoC trend analysis](../phases/8-operate/artifacts/support-voc-trend-analysis.md) | Support data analysis |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [profitability assessment vs. business case](../phases/9-iterate/artifacts/profitability-assessment-vs-business-case.md) | Commercial performance review |
| **R** | [benefits-realization report](../phases/9-iterate/artifacts/benefits-realization-report.md) | Benefits realization review |
| **R** | [KPI performance report](../phases/9-iterate/artifacts/kpi-performance-report.md) | KPI / success-metric tracking |
| **A** | [adoption metrics](../phases/9-iterate/artifacts/adoption-metrics.md) | Feature adoption analysis |
| **A** | [feedback insights report](../phases/9-iterate/artifacts/feedback-insights-report.md) | Aggregate & analyze feedback |
| **A** | [ongoing insights feed](../phases/9-iterate/artifacts/ongoing-insights-feed.md) | Continuous discovery |
| **R** | [next-cycle opportunity backlog](../phases/9-iterate/artifacts/next-cycle-opportunity-backlog.md) | Hand off insights to Discover |
| **A** | [benefits-shortfall report](../phases/9-iterate/artifacts/benefits-shortfall-report.md) | Benefits shortfall root-cause analysis |
| **A** | [updated business case](../phases/9-iterate/artifacts/updated-business-case.md) | Business-case reforecast |

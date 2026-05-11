# 5. Architect
- **Description:** Designs and governs the technical solution; sets patterns, makes build-vs-buy calls, ensures non-functional requirements are met.
- **Business purpose:** De-risks delivery and keeps the solution fit-for-enterprise (cost, compliance, scale, evolvability).
- **Typically reports to:** Chief Architect / VP Engineering / CTO.
- **Project goals:** Approved architecture meeting NFRs · fit with enterprise standards · clear guardrails for engineers.


## AI teammate

**Purpose:** Draft, critique, and maintain the technical solution design so it meets NFRs, fits enterprise standards, and gives engineers clear guardrails to build against.

**Assistive AI (tight collaboration):** Drafts and iterates on the [architecture document](../phases/3-design/artifacts/architecture-document.md), [decision log](../phases/3-design/outcomes/decision-log.md), [integration map](../phases/3-design/artifacts/integration-map.md), [data model](../phases/3-design/artifacts/data-model.md), [API specification](../phases/3-design/artifacts/api-specification.md), [NFR document](../phases/2-define/artifacts/nfr-document.md), and [technical options assessment](../phases/3-design/artifacts/technical-options-assessment.md) with a human architect holding the pen — trade-off analysis, ADR alternatives, NFR stress-testing.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can run continuous architecture-conformance scans that feed the [updated ADRs](../phases/5-build/artifacts/updated-adrs.md) queue and keep related A-owned artifacts across Plan–Iterate (e.g., the [updated architecture roadmap](../phases/9-iterate/artifacts/updated-architecture-roadmap.md)) current from the live system. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not approve the [build-vs-buy decision](../phases/3-design/outcomes/build-vs-buy-decision.md), [architecture executive approval](../phases/3-design/outcomes/architecture-executive-approval.md), [security/compliance approval](../phases/3-design/outcomes/security-compliance-approval.md), or [ratified risk decisions](../phases/3-design/outcomes/ratified-risk-decisions.md). Does not sign off on the [PRR](../phases/6-verify/outcomes/prr-sign-off.md) or own the [threat model](../phases/3-design/artifacts/threat-model.md) (reads, contributes to).

**Inputs:** [Validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), [requirements document](../phases/2-define/artifacts/requirements-document.md), [NFR document](../phases/2-define/artifacts/nfr-document.md), [data inventory & classification](../phases/2-define/artifacts/data-inventory-classification.md), [applicable-regulations list](../phases/2-define/artifacts/applicable-regulations-list.md), prior [decision log](../phases/3-design/outcomes/decision-log.md) entries, and enterprise patterns / reference architectures.

**Outputs:** The A artifacts above, plus the [technical feasibility findings](../phases/2-define/artifacts/technical-feasibility-findings.md), [dependency list](../phases/2-define/artifacts/dependency-list.md), [telemetry plan](../phases/4-plan/artifacts/telemetry-plan.md), [feature flag plan](../phases/4-plan/artifacts/feature-flag-plan.md), and [updated architecture roadmap](../phases/9-iterate/artifacts/updated-architecture-roadmap.md).

**Escalation triggers:**
- NFR violation proposed or detected (availability, latency, throughput, cost ceiling).
- Regulated data crosses a new system, boundary, or jurisdiction.
- New external dependency or vendor lock-in introduced.
- Breaking change to a published [API specification](../phases/3-design/artifacts/api-specification.md) or [data model](../phases/3-design/artifacts/data-model.md).
- Architecture drift detected that requires a new ADR rather than an update.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Design exit checklist](../phases/3-design/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your docs-as-code / knowledge base**, draft and critique the [architecture document](../phases/3-design/artifacts/architecture-document.md) and individual entries in the [decision log](../phases/3-design/outcomes/decision-log.md) — surface trade-offs, challenge assumptions, propose ADR alternatives before you commit.
- **In your threat-modeling tool**, explore attack surfaces against the [threat model](../phases/3-design/artifacts/threat-model.md) and the [approved security patterns](../phases/3-design/outcomes/approved-security-patterns.md); stress-test NFRs captured in the [NFR document](../phases/2-define/artifacts/nfr-document.md).
- **In your diagramming, data modeling, and API specification tools**, iterate on the [integration map](../phases/3-design/artifacts/integration-map.md), [data model](../phases/3-design/artifacts/data-model.md), and [API specification](../phases/3-design/artifacts/api-specification.md) — propose alternatives, detect coupling, check against NFRs and data classification.
- **In your cost / FinOps dashboard**, work through cost and scale scenarios for the [ROI technical inputs](../phases/1-discover/artifacts/roi-technical-inputs.md), [cost & capacity report](../phases/8-operate/artifacts/cost-capacity-report.md), [scale-readiness report](../phases/8-operate/artifacts/scale-readiness-report.md), and the [modernization plan](../phases/9-iterate/artifacts/modernization-plan.md).

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your enterprise architecture repository and source control**, continuously scan for architecture conformance against ADRs and patterns; flag drift and feed the [updated ADRs](../phases/5-build/artifacts/updated-adrs.md) queue.
- **In your API specification / registry**, lint contracts against style and backward-compatibility rules; block or flag changes that violate them.
- **In your data modeling tool / schema catalog**, keep the [data model](../phases/3-design/artifacts/data-model.md) and [data inventory & classification](../phases/2-define/artifacts/data-inventory-classification.md) in sync with the live schema; detect classification drift.
- **Across code and the [dependency list](../phases/2-define/artifacts/dependency-list.md)**, monitor dependency and integration drift; auto-generate refreshed [integration map](../phases/3-design/artifacts/integration-map.md) diagrams from the running system.
- **In your cost / FinOps dashboard**, continuous cost-anomaly detection against thresholds; route material changes into the [updated architecture roadmap](../phases/9-iterate/artifacts/updated-architecture-roadmap.md) review.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **32** artifacts/outcomes as primary (A) and co-own **23** (R)._

### [1. Discover](../phases/1-discover/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [feasibility memo](../phases/1-discover/artifacts/feasibility-memo.md) | Early feasibility / risk assessment |
| **A** | [ROI technical inputs](../phases/1-discover/artifacts/roi-technical-inputs.md) | Technical cost & feasibility inputs |
| **R** | [strategic alignment statement](../phases/1-discover/artifacts/strategic-alignment-statement.md) | Align to portfolio strategy |

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [commercial model decision](../phases/2-define/outcomes/commercial-model-decision.md) | Commercial / delivery model decision |
| **R** | [data inventory & classification](../phases/2-define/artifacts/data-inventory-classification.md) | Data requirements & classification |
| **R** | [solution recommendation](../phases/2-define/artifacts/solution-recommendation.md) | Solution options evaluation |
| **A** | [system-to-process map](../phases/2-define/artifacts/system-to-process-map.md) | System context overlay on processes |
| **R** | [change impact assessment](../phases/2-define/artifacts/change-impact-assessment.md) | Change impact analysis |
| **R** | [capability gap report](../phases/2-define/artifacts/capability-gap-report.md) | Gap analysis |
| **A** | [technical feasibility findings](../phases/2-define/artifacts/technical-feasibility-findings.md) | Requirements technical feasibility review |
| **A** | [NFR document](../phases/2-define/artifacts/nfr-document.md) | Non-functional requirements definition |
| **A** | [dependency list](../phases/2-define/artifacts/dependency-list.md) | Dependency mapping |
| **R** | [Define exit decision](../phases/2-define/outcomes/define-exit-decision.md) | Define stage-gate review |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [build-vs-buy decision](../phases/3-design/outcomes/build-vs-buy-decision.md) | Approve build-vs-buy & vendor decisions |
| **R** | [architecture executive approval](../phases/3-design/outcomes/architecture-executive-approval.md) | Architecture strategic review |
| **A** | [technical options assessment](../phases/3-design/artifacts/technical-options-assessment.md) | Research technical options |
| **A** | [architecture document](../phases/3-design/artifacts/architecture-document.md) | Document solution architecture |
| **A** | [decision log](../phases/3-design/outcomes/decision-log.md) | Architecture decision records |
| **A** | [integration map](../phases/3-design/artifacts/integration-map.md) | Integration / system context map |
| **A** | [data model](../phases/3-design/artifacts/data-model.md) | Data model / schema design |
| **A** | [API specification](../phases/3-design/artifacts/api-specification.md) | API / interface contract design |
| **R** | [threat model](../phases/3-design/artifacts/threat-model.md) | Threat modeling |
| **R** | [approved security patterns](../phases/3-design/outcomes/approved-security-patterns.md) | Secure design pattern selection |
| **R** | [security/compliance approval](../phases/3-design/outcomes/security-compliance-approval.md) | Security & compliance review |
| **R** | [build-ready package](../phases/3-design/artifacts/build-ready-package.md) | Design → engineering handoff review |
| **R** | [vendor evaluation scorecard](../phases/3-design/artifacts/vendor-evaluation-scorecard.md) | Vendor / buy option evaluation |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [skills requirement input](../phases/4-plan/artifacts/skills-requirement-input.md) | Technical skills & roles requirement |
| **R** | [portfolio priority decision](../phases/4-plan/outcomes/portfolio-priority-decision.md) | Resolve cross-portfolio priority conflicts |
| **A** | [technical milestone plan](../phases/4-plan/artifacts/technical-milestone-plan.md) | Technical milestone sequencing |
| **A** | [enabler backlog](../phases/4-plan/artifacts/enabler-backlog.md) | Architecture runway / technical enablers |
| **A** | [telemetry plan](../phases/4-plan/artifacts/telemetry-plan.md) | Analytics & telemetry instrumentation planning |
| **A** | [feature flag plan](../phases/4-plan/artifacts/feature-flag-plan.md) | Feature flag strategy |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [architecture status report](../phases/5-build/artifacts/architecture-status-report.md) | Architecture status input |
| **A** | [resolved technical blockers](../phases/5-build/outcomes/resolved-technical-blockers.md) | Resolve technical blockers |
| **A** | [technical impact analysis](../phases/5-build/artifacts/technical-impact-analysis.md) | Technical impact of scope changes |
| **A** | [design guidance sessions](../phases/5-build/artifacts/design-guidance-sessions.md) | Technical design guidance & pairing |
| **A** | [conformance findings](../phases/5-build/artifacts/conformance-findings.md) | Architecture conformance review |
| **A** | [updated ADRs](../phases/5-build/artifacts/updated-adrs.md) | Update architecture decision records |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md) | Operational readiness review |
| **R** | [performance test report](../phases/6-verify/artifacts/performance-test-report.md) | Performance / load testing |
| **A** | [architecture validation report](../phases/6-verify/artifacts/architecture-validation-report.md) | Architecture validation in verify env |
| **A** | [architectural risk report](../phases/6-verify/artifacts/architectural-risk-report.md) | Architectural risk assessment |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [rollback safety sign-off](../phases/7-launch/outcomes/rollback-safety-sign-off.md) | Architectural rollback safety review |
| **A** | [architectural launch signals](../phases/7-launch/artifacts/architectural-launch-signals.md) | Architectural launch signals monitoring |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [margin & CAC/LTV report](../phases/8-operate/artifacts/margin-cac-ltv-report.md) | Unit-economics / margin review |
| **R** | [root cause analysis report](../phases/8-operate/artifacts/root-cause-analysis-report.md) | Root cause analysis |
| **R** | [cost & capacity report](../phases/8-operate/artifacts/cost-capacity-report.md) | Cost / capacity monitoring |
| **A** | [architectural health report](../phases/8-operate/artifacts/architectural-health-report.md) | Architectural health monitoring |
| **A** | [scale-readiness report](../phases/8-operate/artifacts/scale-readiness-report.md) | Capacity & scale architecture review |
| **A** | [architecture updates](../phases/8-operate/artifacts/architecture-updates.md) | Evolve architecture from production learnings |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [profitability assessment vs. business case](../phases/9-iterate/artifacts/profitability-assessment-vs-business-case.md) | Commercial performance review |
| **A** | [updated architecture roadmap](../phases/9-iterate/artifacts/updated-architecture-roadmap.md) | Architecture roadmap refresh |
| **A** | [modernization plan](../phases/9-iterate/artifacts/modernization-plan.md) | Technology refresh / modernization planning |
| **A** | [prioritized tech-debt list](../phases/9-iterate/artifacts/prioritized-tech-debt-list.md) | Technical debt backlog grooming |
| **R** | [benefits-shortfall report](../phases/9-iterate/artifacts/benefits-shortfall-report.md) | Benefits shortfall root-cause analysis |

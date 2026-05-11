# Formats — Bridging Named Docs and Shareable Bundles

Teams arrive at this handbook with their own document formats and leave wanting to share their work with others. This doc answers both:

1. **Inbound** — if you already have a PRFAQ, PRD, or other named format, which handbook artifacts does it cover?
2. **Outbound** — what's the recipe for a zip-and-share bundle at common handoff moments?
3. **Bundle conventions** — what a shareable bundle contains beyond the artifacts themselves.

> **v1, opinionated.** These mappings are a starting point. If a format you use isn't here or you disagree with a mapping, file a PR.

---

## 1. Inbound — named format → handbook artifact mapping

Each row shows what the named format typically covers *fully*, what it covers *partially*, and what a team would still need to generate to reach a complete handbook artifact set for [Discover](../phases/1-discover/README.md) and [Define](../phases/2-define/README.md).

### PRFAQ (press release + FAQ)

- **Fully covers:** [opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md), [vision statement](../phases/1-discover/artifacts/vision-statement.md), [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md).
- **Partially covers:** [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), [business case](../phases/1-discover/artifacts/business-case.md), [user personas](../phases/1-discover/artifacts/user-personas.md) (implicit in the customer voice).
- **Typically missing:** [ROI model](../phases/1-discover/artifacts/roi-model.md), [market analysis report](../phases/1-discover/artifacts/market-analysis-report.md), [feasibility memo](../phases/1-discover/artifacts/feasibility-memo.md), [stakeholder map](../phases/1-discover/artifacts/stakeholder-map.md).

### PRD (product requirements document)

- **Fully covers:** [requirements document](../phases/2-define/artifacts/requirements-document.md).
- **Partially covers:** [MVP scope statement](../phases/2-define/artifacts/mvp-scope-statement.md), [NFR document](../phases/2-define/artifacts/nfr-document.md), [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md), [KPI definitions](../phases/2-define/artifacts/kpi-definitions.md).
- **Typically missing:** [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md), [product roadmap](../phases/2-define/artifacts/product-roadmap.md), [effort estimates](../phases/2-define/artifacts/effort-estimates.md), [dependency list](../phases/2-define/artifacts/dependency-list.md).

### 6-pager / executive memo

- **Fully covers:** [opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md), [strategic alignment statement](../phases/1-discover/artifacts/strategic-alignment-statement.md).
- **Partially covers:** [business case](../phases/1-discover/artifacts/business-case.md), [ROI model](../phases/1-discover/artifacts/roi-model.md), [competitive landscape report](../phases/1-discover/artifacts/competitive-landscape-report.md).
- **Typically missing:** [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), [user personas](../phases/1-discover/artifacts/user-personas.md), [feasibility memo](../phases/1-discover/artifacts/feasibility-memo.md).

### Lean canvas / business model canvas

- **Fully covers:** [opportunity sizing](../phases/1-discover/artifacts/opportunity-sizing.md).
- **Partially covers:** [business case](../phases/1-discover/artifacts/business-case.md), [user personas](../phases/1-discover/artifacts/user-personas.md), [pricing benchmark report](../phases/1-discover/artifacts/pricing-benchmark-report.md).
- **Typically missing:** [vision statement](../phases/1-discover/artifacts/vision-statement.md), [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md), [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), [ROI model](../phases/1-discover/artifacts/roi-model.md).

### Opportunity canvas / Jobs-to-be-Done statement

- **Fully covers:** [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md), [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md) (hypothesized form).
- **Partially covers:** [opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md), [user personas](../phases/1-discover/artifacts/user-personas.md).
- **Typically missing:** [business case](../phases/1-discover/artifacts/business-case.md), [vision statement](../phases/1-discover/artifacts/vision-statement.md), [ROI model](../phases/1-discover/artifacts/roi-model.md).

### Wireframes / design mocks

- **Fully covers:** [visual design mockups](../phases/3-design/artifacts/visual-design-mockups.md).
- **Partially covers:** [IA spec](../phases/3-design/artifacts/ia-spec.md), [interactive prototype](../phases/3-design/artifacts/interactive-prototype.md), [design specification](../phases/3-design/artifacts/design-specification.md).
- **Typically missing:** [journey map / service blueprint](../phases/3-design/artifacts/journey-map-service-blueprint.md), [usability findings](../phases/3-design/artifacts/usability-findings.md), [accessibility design report](../phases/3-design/artifacts/accessibility-design-report.md).

### User story map

- **Fully covers:** [product roadmap](../phases/2-define/artifacts/product-roadmap.md).
- **Partially covers:** [MVP scope statement](../phases/2-define/artifacts/mvp-scope-statement.md), the backlog entries consumed in Plan.
- **Typically missing:** [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md), [NFR document](../phases/2-define/artifacts/nfr-document.md), [effort estimates](../phases/2-define/artifacts/effort-estimates.md).

### ADR / RFC

- **Fully covers:** An entry in [architecture decision records](../phases/3-design/artifacts/architecture-document.md), [decision log from design reviews](../phases/3-design/outcomes/decision-log-from-design-reviews.md).
- **Partially covers:** [architecture document](../phases/3-design/artifacts/architecture-document.md) (one decision's worth), [build-vs-buy decision](../phases/3-design/outcomes/build-vs-buy-decision.md).
- **Typically missing:** The broader design package (API spec, data model, threat model).

### OKRs / objectives document

- **Fully covers:** [KPI definitions](../phases/2-define/artifacts/kpi-definitions.md) (lagging measures), approximations of the [outcome hypothesis](../phases/1-discover/artifacts/outcome-hypothesis.md) (leading).
- **Partially covers:** [business case](../phases/1-discover/artifacts/business-case.md) success framing, [strategic alignment statement](../phases/1-discover/artifacts/strategic-alignment-statement.md).
- **Typically missing:** Everything about *how* — requirements, scope, roadmap, plan, and the per-phase handoffs.

---

## 2. Outbound — bundle recipes (zip-and-share)

Named bundles for common handoff moments. Each recipe lists the artifacts to include, the intended reader, and a "ready to share" check. Bundles are generated by path 6 of the [navigator skill](../.claude/skills/ai-pdlc-navigator/SKILL.md) or assembled manually.

### Vision bundle

**Intended reader:** Executive sponsors deciding whether to fund further Discover.

- [opportunity brief](../phases/1-discover/artifacts/opportunity-brief.md)
- [business case](../phases/1-discover/artifacts/business-case.md)
- [ROI model](../phases/1-discover/artifacts/roi-model.md)
- [strategic alignment statement](../phases/1-discover/artifacts/strategic-alignment-statement.md)
- [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md)

**Ready to share when:** every artifact's Definition of Done is green and the business case references the ROI model by version.

### Kickoff bundle

**Intended reader:** An incoming delivery team at Plan start.

- [signed product charter](../phases/2-define/artifacts/signed-product-charter.md)
- [product roadmap](../phases/2-define/artifacts/product-roadmap.md)
- [MVP scope statement](../phases/2-define/artifacts/mvp-scope-statement.md)
- [KPI definitions](../phases/2-define/artifacts/kpi-definitions.md)
- [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md)
- [risk register](../phases/4-plan/artifacts/risk-register.md)
- [dependency list](../phases/2-define/artifacts/dependency-list.md)

**Ready to share when:** the charter is signed, the MVP scope is stable, and KPIs are instrumented (or explicitly planned for instrumentation in Build).

### Build-start bundle

**Intended reader:** Engineering, QA, and design partners starting Build.

- [approved design package](../phases/3-design/outcomes/approved-design-package.md)
- [build-ready package](../phases/3-design/artifacts/build-ready-package.md)
- [API specification](../phases/3-design/artifacts/api-specification.md)
- [data model](../phases/3-design/artifacts/data-model.md)
- [NFR document](../phases/2-define/artifacts/nfr-document.md)
- [test plan](../phases/4-plan/artifacts/test-plan.md)
- [feature flag plan](../phases/4-plan/artifacts/feature-flag-plan.md)
- [telemetry plan](../phases/4-plan/artifacts/telemetry-plan.md)

**Ready to share when:** the [Design exit checklist](../phases/3-design/README.md#exit-checklist) passes.

### Design-partner bundle

**Intended reader:** Early customers invited to co-create or validate.

- [vision statement](../phases/1-discover/artifacts/vision-statement.md)
- [user personas](../phases/1-discover/artifacts/user-personas.md)
- [interactive prototype](../phases/3-design/artifacts/interactive-prototype.md)
- [journey map / service blueprint](../phases/3-design/artifacts/journey-map-service-blueprint.md)

**Ready to share when:** the prototype is shareable in the target environment and the vision is stable enough to survive customer feedback.

### Launch-readiness bundle

**Intended reader:** Go/no-go reviewers at the Launch gate.

- [launch-readiness assessment](../phases/6-verify/artifacts/launch-readiness-assessment.md)
- [verified KPI telemetry](../phases/6-verify/artifacts/verified-kpi-telemetry.md)
- [approved known-issues & risk acceptance](../phases/6-verify/outcomes/approved-known-issues-risk-acceptance.md)
- [rollback safety sign-off](../phases/7-launch/outcomes/rollback-safety-sign-off.md)
- [go/no-go decision package](../phases/7-launch/outcomes/go-no-go-decision-package.md)

**Ready to share when:** the [Verify exit checklist](../phases/6-verify/README.md#exit-checklist) passes.

### Board / investor bundle

**Intended reader:** Board or investor update. Use sparingly — high-stakes, high-visibility.

- [board/investor launch narrative](../phases/7-launch/artifacts/board-investor-launch-narrative.md)
- [revenue report](../phases/8-operate/artifacts/revenue-report.md)
- [operational performance review](../phases/8-operate/artifacts/operational-performance-review.md)
- [updated roadmap](../phases/9-iterate/artifacts/updated-roadmap.md)

**Ready to share when:** metrics are current within the board's reporting window and the narrative references them by date.

---

## 3. Bundle conventions

Every shareable bundle — whether generated by the skill or hand-assembled — should include the artifacts plus:

- **`README.md` manifest** at the top level. One-line description per included file, grouped by phase. Name the bundle recipe used (e.g., "Vision bundle v1"). Name the source handbook (link to the repo) and the version or date.
- **`traceability.md`** linking each generated artifact back to the source document(s) it draws from. Makes review fast and surfaces gaps.
- **Top-of-file pointer** in every artifact back to the handbook, so a recipient can go deeper if they want the canonical definition.
- **No deep-links into `phases/` paths** from inside the bundle. Links inside the bundle are relative to the bundle root. External links go to the handbook.
- **`_TBD: <note>_` placeholders** wherever an artifact was generated from a seed doc that didn't cover that field — never silently invent. The manifest calls out which artifacts have material TBDs.

These rules let the bundle render standalone when zipped, so the recipient doesn't need access to the handbook to read the work.

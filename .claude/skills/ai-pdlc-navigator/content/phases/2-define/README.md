# Phase 2: Define

**Goal:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

## Where this fits

Define picks up where [Discover](../1-discover/README.md) exits — a funded, validated opportunity — and produces the formal contract the rest of the lifecycle will execute against. [Design](../3-design/README.md) cannot start safely without the decisions made here.

## What happens in this phase

Define is where a validated opportunity becomes a signed contract: what the product must do, for whom, within what budget, against what KPIs, under which regulations, and sold through which commercial model. Every later phase will reference the documents produced here. Ambiguity that survives Define becomes a defect at launch.

Define is led by the **Business Analyst** (drafting and iterating requirements, traceability, process models, and change-impact analysis), the **Product Owner** (ratifying roadmap, success metrics, and MVP scope), and the **Architect** (NFRs, dependency mapping, technical feasibility, system context). The **Product Sponsor** formally ratifies the business case, approves the charter, and commits to the commercial model. **Security & Compliance** derives regulatory scope into testable controls and confirms data classification. **QA/Tester** maps test cases to requirements. **Sales & Marketing** drafts the initial GTM plan. **Customer Support** defines the support process model. **Project Manager** facilitates the charter, runs stakeholder workshops, drafts the schedule, and identifies affected audiences. **Developer** provides effort estimates.

The phase ends at the [Define stage-gate review](outcomes/define-exit-decision.md). Only initiatives with approved requirements, ratified business case, decided commercial model, and cross-role sign-off move to Design.

## Deliverables

- **[`artifacts/`](artifacts/)** — 28 tangible outputs for this phase.
- **[`outcomes/`](outcomes/)** — 6 decisions or state changes.

See the [Define activities list in the master flow](../../AI-PDLC-linear-flow.md#2-define) for the full activity-by-activity view.

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

Ready to enter [Design](../3-design/README.md) when all of the following are true:

- [ ] [affected-audiences list](artifacts/affected-audiences-list.md) — Each audience names a specific liaison or sponsor, not a team placeholder.
- [ ] [applicable-regulations list](artifacts/applicable-regulations-list.md) — Each entry names the regulation, jurisdiction, and applicability trigger.
- [ ] [capability gap report](artifacts/capability-gap-report.md) — Each gap has a disposition (build / buy / partner / defer / reuse-with-extension).
- [ ] [change impact assessment](artifacts/change-impact-assessment.md) — Process changes show an explicit as-is to to-be delta.
- [ ] [charter draft](artifacts/charter-draft.md) — Scope statement includes explicit non-goals.
- [ ] [control-to-test coverage map](artifacts/control-to-test-coverage-map.md) — Coverage gaps are flagged with a named remediation plan.
- [ ] [data inventory & classification](artifacts/data-inventory-classification.md) — Every element carries a classification tier per org policy.
- [ ] [dependency list](artifacts/dependency-list.md) — Each dependency carries a fallback or contingency statement.
- [ ] [draft GTM plan](artifacts/draft-gtm-plan.md) — Assumptions and items to validate before final GTM are listed.
- [ ] [draft project schedule](artifacts/draft-project-schedule.md) — Critical path through the work is identified.
- [ ] [effort estimates](artifacts/effort-estimates.md) — Each estimate has a confidence band, not a single point.
- [ ] [KPI definitions](artifacts/kpi-definitions.md) — Each KPI has an exact formula with numerator, denominator, and filters.
- [ ] [MVP scope statement](artifacts/mvp-scope-statement.md) — Success criteria define the keep-building / pivot / kill decision.
- [ ] [NFR document](artifacts/nfr-document.md) — Each NFR has a unique ID, category, and quantified target with tolerance.
- [ ] [privacy impact assessment](artifacts/privacy-impact-assessment.md) — Residual risk statement is signed off by a named risk owner.
- [ ] [process models](artifacts/process-models.md) — Both as-is and to-be diagrams exist for each in-scope process.
- [ ] [product roadmap](artifacts/product-roadmap.md) — Each theme states a problem, a hypothesis, and a target KPI movement.
- [ ] [requirements document](artifacts/requirements-document.md) — Every requirement has a unique ID and outcome-language statement.
- [ ] [security control requirements](artifacts/security-control-requirements.md) — Each control has an ID, title, and a testable statement.
- [ ] [signed product charter](artifacts/signed-product-charter.md) — Decision rights for scope, budget, and trade-offs are assigned to named roles.
- [ ] [solution recommendation](artifacts/solution-recommendation.md) — At least three options (including "do nothing") are evaluated with elimination rationale.
- [ ] [stakeholder workshop outcomes](artifacts/stakeholder-workshop-outcomes.md) — Decisions are listed with owner and effective date.
- [ ] [support process model](artifacts/support-process-model.md) — SLA targets are listed by severity and contract tier.
- [ ] [system-to-process map](artifacts/system-to-process-map.md) — Every process step is mapped to the system(s) that enact it.
- [ ] [technical feasibility findings](artifacts/technical-feasibility-findings.md) — Each requirement or NFR carries a feasibility rating with rationale.
- [ ] [test-to-requirement coverage map](artifacts/test-to-requirement-coverage-map.md) — Each row carries a coverage status (covered / partial / uncovered / exempt).
- [ ] [testable acceptance criteria](artifacts/testable-acceptance-criteria.md) — Each criterion is phrased in Given / When / Then (or equivalent) observable form.
- [ ] [traceability matrix](artifacts/traceability-matrix.md) — Links are navigable in both directions (requirement to test and back).
- [ ] [approved business case](outcomes/approved-business-case.md) — Continue / pivot / kill thresholds are stated with numeric values.
- [ ] [approved requirements](outcomes/approved-requirements.md) — Every functional requirement has at least one linked acceptance criterion.
- [ ] [commercial model decision](outcomes/commercial-model-decision.md) — Deployment model, pricing family, and channel strategy are all selected.
- [ ] [confirmed data classification](outcomes/confirmed-data-classification.md) — Handling, retention, and residency requirements are specified per tier.
- [ ] [cross-role requirements sign-off](outcomes/cross-role-requirements-sign-off.md) — Each executing role has a named sign-off with date.
- [ ] [Define exit decision](outcomes/define-exit-decision.md) — Decision is recorded as go / no-go / defer with rationale.
- [ ] All role-owned artifacts for this phase meet their artifact-doc DoD

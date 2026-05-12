# AI-PDLC Linear Flow — Tool-Agnostic

Tasks from the circle diagram mapped into a linear, phase-based flow for creating a new product. Personas responsible appear in parentheses after each task.

Each line uses the format `<ACTIVITY> produces <OUTCOME>` for easy extraction.

> **New to this?** Start at [`adoption/README.md`](adoption/README.md) to self-locate on the [maturity model](adoption/maturity-model.md), read the [anti-patterns](adoption/anti-patterns.md), and set your [autonomy policy](adoption/hitl-framework.md) before diving into the flow below.

## Diagram

Source: [`AI-PDLC-linear.drawio`](AI-PDLC-linear.drawio) — swim lanes (roles) × columns (phases), with tasks placed in their (role, phase) cell.

Rendered output: `build/AI-PDLC-linear.svg` and `build/AI-PDLC-linear.png` (after running `make`).

### Build

```
make          # build both PNG and SVG for every .drawio in the repo
make svg      # SVG only
make png      # PNG only
make clean    # remove build/
```

Requires the `drawio` CLI (Homebrew: `brew install --cask drawio`).

---

## Roles

### 1. Product Sponsor (VP Product / CPO / GM / Executive Sponsor)
- **Description:** Sets strategic direction, owns the P&L, secures funding and air-cover, and arbitrates cross-functional trade-offs across a portfolio of initiatives.
- **Business purpose:** Ensures the initiative ladders up to corporate strategy and delivers portfolio-level business outcomes.
- **Typically reports to:** CEO (CPO/GM) or CPO/COO (VP Product).
- **Project goals:** Executive/board alignment on the bet · funding & staffing secured · portfolio KPIs hit · roadmap coherence preserved.

### 2. Product Owner
- **Description:** Owns the backlog and maximizes value delivered each iteration; single empowered decision-maker for "what to build next."
- **Business purpose:** Keeps the delivery team always working on the highest-value items.
- **Typically reports to:** Head of Product / Director of Product Management.
- **Project goals:** Clear, ordered, refined backlog · validated increments · stakeholder alignment on sequence & trade-offs.

### 3. Business Analyst
- **Description:** Elicits, analyzes, and documents needs; models as-is/to-be processes; validates that solutions deliver benefits.
- **Business purpose:** Bridges business strategy and technical delivery so teams solve the right problem.
- **Typically reports to:** BA Practice Lead, PMO, or Head of Product.
- **Project goals:** Traceable, validated requirements · scope discipline · benefits realization post-launch.

### 4. UI/UX Designer
- **Description:** Conducts user research and designs usable, accessible, desirable product experiences; maintains design-system contributions.
- **Business purpose:** Reduces the risk of building the wrong thing, or the right thing in an unusable way.
- **Typically reports to:** Head of Design / Director of UX.
- **Project goals:** Validated user needs · accessible, consistent UI · measurable usability improvements.

### 5. Architect
- **Description:** Designs and governs the technical solution; sets patterns, makes build-vs-buy calls, ensures non-functional requirements are met.
- **Business purpose:** De-risks delivery and keeps the solution fit-for-enterprise (cost, compliance, scale, evolvability).
- **Typically reports to:** Chief Architect / VP Engineering / CTO.
- **Project goals:** Approved architecture meeting NFRs · fit with enterprise standards · clear guardrails for engineers.

### 6. Security & Compliance
- **Description:** Embeds security and regulatory controls across the PDLC; runs threat modeling, AppSec tooling, audits, and incident response.
- **Business purpose:** Protects the org, customers, and regulated data; keeps the company shippable under its legal obligations.
- **Typically reports to:** CISO / VP Security (in Engineering, Risk, or Legal/Compliance org).
- **Project goals:** No critical/high vulns shipped · audit evidence without blocking delivery · measurable reduction in recurring vuln classes.

### 7. Site Reliability Engineer (SRE)
- **Description:** Applies software engineering to operations; owns SLIs/SLOs, on-call, capacity, observability, and release engineering.
- **Business purpose:** Keeps services reliable, performant, and cost-efficient while preserving feature velocity.
- **Typically reports to:** VP/Director of Infrastructure, Platform, or Engineering.
- **Project goals:** SLOs met within error budget · automated progressive rollout · manageable on-call load · capacity headroom.

### 8. Project Manager (Delivery)
- **Description:** Owns the "how and when" of delivery; plans scope/schedule/budget, manages cross-team dependencies, tracks risks and changes.
- **Business purpose:** Predictable delivery of cross-functional initiatives against a baselined plan.
- **Typically reports to:** Head of PMO / Director of Program Management.
- **Project goals:** On-time/on-budget delivery · early dependency resolution · transparent risk management · clean closure.

### 9. Developer
- **Description:** Builds, tests, reviews, and operates the software itself; turns backlog items into working increments.
- **Business purpose:** Delivers the product — the primary means of creating customer value.
- **Typically reports to:** Engineering Manager / Tech Lead → Director/VP Engineering.
- **Project goals:** Meets Definition of Done · secure, observable, maintainable code · low change-failure rate · tech debt managed.

### 10. QA / Tester
- **Description:** Provides evidence-based confidence in quality; plans testing, designs/automates tests, runs exploratory sessions, manages risks.
- **Business purpose:** Reduces the risk of defects reaching customers.
- **Typically reports to:** Head of Quality Engineering, or Engineering Manager (embedded model).
- **Project goals:** Risk-based coverage · trusted regression suite · defects caught pre-release · traceability requirements → tests → results.

### 11. Release Manager
- **Description:** Plans, schedules, and coordinates releases across teams, environments, and dependencies; owns readiness, runbooks, and rollback.
- **Business purpose:** Ensures what ships is reliable, coordinated, compliant, and predictable.
- **Typically reports to:** Director of Engineering / Head of DevOps / Release Engineering.
- **Project goals:** On-time release with zero Sev-1 escapes · complete release notes & BOM · validated rollback · improving cadence.

### 12. Technical Writer
- **Description:** Produces and maintains user guides, API reference, tutorials, UI copy, and changelogs; often owns the docs-as-code toolchain.
- **Business purpose:** Reduces time-to-value and deflects support load through discoverable, accurate documentation.
- **Typically reports to:** Head of Product, DevRel, or Engineering.
- **Project goals:** Docs ready at GA · lower support load on documented topics · healthy doc infra · cross-team contribution.

### 13. Sales & Marketing (Product Marketing + Sales Enablement)
- **Description:** Owns positioning, messaging, pricing, launch strategy, competitive intel, and sales readiness (battlecards, demos, certification).
- **Business purpose:** Converts product capability into pipeline and revenue.
- **Typically reports to:** VP Marketing/CMO (PMM); VP Sales/CRO (Enablement).
- **Project goals:** Validated positioning & pricing · certified sales team at GA · pipeline/win-rate lift · field feedback loop.

### 14. Customer Support / Success
- **Description:** Reactive ticket resolution (Support) plus proactive onboarding, health scoring, QBRs, renewals, and advocacy (CS).
- **Business purpose:** Protects and grows recurring revenue; contains cost-to-serve.
- **Typically reports to:** VP/Chief Customer Officer, CRO, or CEO.
- **Project goals:** Support/CS launch-ready · users hit activation milestones · GRR/NRR targets · closed-loop VoC to Product.

---

## [1. Discover](phases/1-discover/README.md)
Goal: frame the opportunity, validate the problem, understand the market, and exit with a funded, strategically-aligned bet.

- Ideation / opportunity framing produces [opportunity brief](phases/1-discover/artifacts/opportunity-brief.md) *([Product Owner](#2-product-owner))*
- Document product vision produces [vision statement](phases/1-discover/artifacts/vision-statement.md) *([Product Owner](#2-product-owner))*
- Problem-solution fit hypothesis produces [outcome hypothesis](phases/1-discover/artifacts/outcome-hypothesis.md) *([Product Owner](#2-product-owner))*
- Business planning produces [business case](phases/1-discover/artifacts/business-case.md) *([Product Owner](#2-product-owner), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Stakeholder identification & alignment produces [stakeholder map](phases/1-discover/artifacts/stakeholder-map.md) *([Product Owner](#2-product-owner), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Early feasibility / risk assessment produces [feasibility memo](phases/1-discover/artifacts/feasibility-memo.md) *([Product Owner](#2-product-owner), [Architect](#5-architect), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Market & customer research produces [market analysis report](phases/1-discover/artifacts/market-analysis-report.md) *([Business Analyst](#3-business-analyst))*
- User / problem validation produces [validated problem statement](phases/1-discover/artifacts/validated-problem-statement.md) *([Business Analyst](#3-business-analyst), [UI/UX Designer](#4-uiux-designer))*
- Problem-opportunity analysis produces [opportunity sizing](phases/1-discover/artifacts/opportunity-sizing.md) *([Business Analyst](#3-business-analyst))*
- Cost-benefit / ROI analysis produces [ROI model](phases/1-discover/artifacts/roi-model.md) *([Business Analyst](#3-business-analyst))*
- Persona / target user definition produces [user personas](phases/1-discover/artifacts/user-personas.md) *([UI/UX Designer](#4-uiux-designer), [Business Analyst](#3-business-analyst))*
- Competitor analysis produces [competitive landscape report](phases/1-discover/artifacts/competitive-landscape-report.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Pricing research produces [pricing benchmark report](phases/1-discover/artifacts/pricing-benchmark-report.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Technical cost & feasibility inputs produces [ROI technical inputs](phases/1-discover/artifacts/roi-technical-inputs.md) *([Architect](#5-architect))*
- Initial regulatory landscape scan produces [regulatory risk flag](phases/1-discover/artifacts/regulatory-risk-flag.md) *([Security & Compliance](#6-security-compliance))*
- Data sensitivity early read produces [data-sensitivity flag](phases/1-discover/artifacts/data-sensitivity-flag.md) *([Security & Compliance](#6-security-compliance))*
- Project initiation / pre-kickoff coordination produces [initial project brief](phases/1-discover/artifacts/initial-project-brief.md) *([Project Manager](#8-project-manager-delivery))*
- Sponsor/PO alignment facilitation produces [aligned leadership team](phases/1-discover/outcomes/aligned-leadership-team.md) *([Project Manager](#8-project-manager-delivery))*
- Align to portfolio strategy produces [strategic alignment statement](phases/1-discover/artifacts/strategic-alignment-statement.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Architect](#5-architect))*
- Secure initiative funding produces [approved budget & investment commitment](phases/1-discover/outcomes/approved-budget-investment-commitment.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- [Discover](phases/1-discover/README.md) stage-gate review produces [Discover exit decision](phases/1-discover/outcomes/discover-exit-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*

### Artifacts
- [Opportunity brief](phases/1-discover/artifacts/opportunity-brief.md)
- [vision statement](phases/1-discover/artifacts/vision-statement.md)
- [outcome hypothesis](phases/1-discover/artifacts/outcome-hypothesis.md)
- [business case](phases/1-discover/artifacts/business-case.md)
- [stakeholder map](phases/1-discover/artifacts/stakeholder-map.md)
- [feasibility memo](phases/1-discover/artifacts/feasibility-memo.md)
- [market analysis report](phases/1-discover/artifacts/market-analysis-report.md)
- [validated problem statement](phases/1-discover/artifacts/validated-problem-statement.md)
- [opportunity sizing](phases/1-discover/artifacts/opportunity-sizing.md)
- [ROI model](phases/1-discover/artifacts/roi-model.md)
- [user personas](phases/1-discover/artifacts/user-personas.md)
- [competitive landscape report](phases/1-discover/artifacts/competitive-landscape-report.md)
- [pricing benchmark report](phases/1-discover/artifacts/pricing-benchmark-report.md)
- [ROI technical inputs](phases/1-discover/artifacts/roi-technical-inputs.md)
- [regulatory risk flag](phases/1-discover/artifacts/regulatory-risk-flag.md)
- [data-sensitivity flag](phases/1-discover/artifacts/data-sensitivity-flag.md)
- [initial project brief](phases/1-discover/artifacts/initial-project-brief.md)
- [aligned leadership team](phases/1-discover/outcomes/aligned-leadership-team.md)
- [strategic alignment statement](phases/1-discover/artifacts/strategic-alignment-statement.md)
- [approved budget & investment commitment](phases/1-discover/outcomes/approved-budget-investment-commitment.md)
- [Discover exit decision](phases/1-discover/outcomes/discover-exit-decision.md)

## [2. Define](phases/2-define/README.md)
Goal: turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

- Ratify business case produces [approved business case](phases/2-define/outcomes/approved-business-case.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Approve product charter produces [signed product charter](phases/2-define/artifacts/signed-product-charter.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner))*
- Commercial / delivery model decision produces [commercial model decision](phases/2-define/outcomes/commercial-model-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner), [Architect](#5-architect))*
- Create & manage product roadmap produces [product roadmap](phases/2-define/artifacts/product-roadmap.md) *([Product Owner](#2-product-owner))*
- Success metrics / KPI definition produces [KPI definitions](phases/2-define/artifacts/kpi-definitions.md) *([Product Owner](#2-product-owner), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- MVP / scope decision produces [MVP scope statement](phases/2-define/artifacts/mvp-scope-statement.md) *([Product Owner](#2-product-owner), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Draft requirements produces [requirements document](phases/2-define/artifacts/requirements-document.md) *([Business Analyst](#3-business-analyst))*
- Review & iterate on requirements produces [approved requirements](phases/2-define/outcomes/approved-requirements.md) *([Business Analyst](#3-business-analyst))*
- Acceptance criteria authoring produces [testable acceptance criteria](phases/2-define/artifacts/testable-acceptance-criteria.md) *([Business Analyst](#3-business-analyst), [QA/Tester](#10-qa-tester))*
- Data requirements & classification produces [data inventory & classification](phases/2-define/artifacts/data-inventory-classification.md) *([Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Requirements traceability matrix produces [traceability matrix](phases/2-define/artifacts/traceability-matrix.md) *([Business Analyst](#3-business-analyst))*
- Solution options evaluation produces [solution recommendation](phases/2-define/artifacts/solution-recommendation.md) *([Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Business process modeling (as-is / to-be) produces [process models](phases/2-define/artifacts/process-models.md) *([Business Analyst](#3-business-analyst))*
- System context overlay on processes produces [system-to-process map](phases/2-define/artifacts/system-to-process-map.md) *([Architect](#5-architect))*
- Change impact analysis produces [change impact assessment](phases/2-define/artifacts/change-impact-assessment.md) *([Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Gap analysis produces [capability gap report](phases/2-define/artifacts/capability-gap-report.md) *([Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Requirements technical feasibility review produces [technical feasibility findings](phases/2-define/artifacts/technical-feasibility-findings.md) *([Architect](#5-architect))*
- Non-functional requirements definition produces [NFR document](phases/2-define/artifacts/nfr-document.md) *([Architect](#5-architect), [Business Analyst](#3-business-analyst))*
- Dependency mapping produces [dependency list](phases/2-define/artifacts/dependency-list.md) *([Architect](#5-architect), [Project Manager](#8-project-manager-delivery))*
- Regulatory / compliance scope assessment produces [applicable-regulations list](phases/2-define/artifacts/applicable-regulations-list.md) *([Security & Compliance](#6-security-compliance), [Business Analyst](#3-business-analyst))*
- Security & compliance requirements derivation produces [security control requirements](phases/2-define/artifacts/security-control-requirements.md) *([Security & Compliance](#6-security-compliance))*
- Map security controls to test cases produces [control-to-test coverage map](phases/2-define/artifacts/control-to-test-coverage-map.md) *([Security & Compliance](#6-security-compliance), [QA/Tester](#10-qa-tester))*
- Privacy / DPIA assessment produces [privacy impact assessment](phases/2-define/artifacts/privacy-impact-assessment.md) *([Security & Compliance](#6-security-compliance))*
- Data classification confirmation produces [confirmed data classification](phases/2-define/outcomes/confirmed-data-classification.md) *([Security & Compliance](#6-security-compliance))*
- Estimation / sizing produces [effort estimates](phases/2-define/artifacts/effort-estimates.md) *([Developer](#9-developer), [Project Manager](#8-project-manager-delivery))*
- Map test cases to requirements produces [test-to-requirement coverage map](phases/2-define/artifacts/test-to-requirement-coverage-map.md) *([QA/Tester](#10-qa-tester))*
- Support process definition produces [support process model](phases/2-define/artifacts/support-process-model.md) *([Customer Support](#14-customer-support-success))*
- Identify affected internal audiences produces [affected-audiences list](phases/2-define/artifacts/affected-audiences-list.md) *([Project Manager](#8-project-manager-delivery))*
- Charter development facilitation produces [charter draft](phases/2-define/artifacts/charter-draft.md) *([Project Manager](#8-project-manager-delivery))*
- [Define](phases/2-define/README.md)-phase stakeholder workshops produces [stakeholder workshop outcomes](phases/2-define/artifacts/stakeholder-workshop-outcomes.md) *([Project Manager](#8-project-manager-delivery))*
- Baseline schedule draft produces [draft project schedule](phases/2-define/artifacts/draft-project-schedule.md) *([Project Manager](#8-project-manager-delivery))*
- GTM planning — initial produces [draft GTM plan](phases/2-define/artifacts/draft-gtm-plan.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Review requirements produces [cross-role requirements sign-off](phases/2-define/outcomes/cross-role-requirements-sign-off.md) *(All roles)*
- [Define](phases/2-define/README.md) stage-gate review produces [Define exit decision](phases/2-define/outcomes/define-exit-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Architect](#5-architect))*

### Artifacts
- [Approved business case](phases/2-define/outcomes/approved-business-case.md)
- [signed product charter](phases/2-define/artifacts/signed-product-charter.md)
- [commercial model decision](phases/2-define/outcomes/commercial-model-decision.md)
- [product roadmap](phases/2-define/artifacts/product-roadmap.md)
- [KPI definitions](phases/2-define/artifacts/kpi-definitions.md)
- [
- scope statement](phases/2-define/artifacts/mvp-scope-statement.md)
- [requirements document](phases/2-define/artifacts/requirements-document.md)
- [approved requirements](phases/2-define/outcomes/approved-requirements.md)
- [testable acceptance criteria](phases/2-define/artifacts/testable-acceptance-criteria.md)
- [data inventory & classification](phases/2-define/artifacts/data-inventory-classification.md)
- [traceability matrix](phases/2-define/artifacts/traceability-matrix.md)
- [solution recommendation](phases/2-define/artifacts/solution-recommendation.md)
- [process models](phases/2-define/artifacts/process-models.md)
- [system-to-process map](phases/2-define/artifacts/system-to-process-map.md)
- [change impact assessment](phases/2-define/artifacts/change-impact-assessment.md)
- [capability gap report](phases/2-define/artifacts/capability-gap-report.md)
- [technical feasibility findings](phases/2-define/artifacts/technical-feasibility-findings.md)
- [NFR document](phases/2-define/artifacts/nfr-document.md)
- [dependency list](phases/2-define/artifacts/dependency-list.md)
- [applicable-regulations list](phases/2-define/artifacts/applicable-regulations-list.md)
- [security control requirements](phases/2-define/artifacts/security-control-requirements.md)
- [control-to-test coverage map](phases/2-define/artifacts/control-to-test-coverage-map.md)
- [privacy impact assessment](phases/2-define/artifacts/privacy-impact-assessment.md)
- [confirmed data classification](phases/2-define/outcomes/confirmed-data-classification.md)
- [effort estimates](phases/2-define/artifacts/effort-estimates.md)
- [test-to-requirement coverage map](phases/2-define/artifacts/test-to-requirement-coverage-map.md)
- [support process model](phases/2-define/artifacts/support-process-model.md)
- [affected-audiences list](phases/2-define/artifacts/affected-audiences-list.md)
- [charter draft](phases/2-define/artifacts/charter-draft.md)
- [stakeholder workshop outcomes](phases/2-define/artifacts/stakeholder-workshop-outcomes.md)
- [draft project schedule](phases/2-define/artifacts/draft-project-schedule.md)
- [draft GTM plan](phases/2-define/artifacts/draft-gtm-plan.md)
- [cross-role requirements sign-off](phases/2-define/outcomes/cross-role-requirements-sign-off.md)
- [Define exit decision](phases/2-define/outcomes/define-exit-decision.md)

## [3. Design](phases/3-design/README.md)
Goal: produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

- Approve build-vs-buy & vendor decisions produces [build-vs-buy decision](phases/3-design/outcomes/build-vs-buy-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Architect](#5-architect))*
- [Design](phases/3-design/README.md)-to-business-case alignment review produces [validated business-value alignment](phases/3-design/artifacts/validated-business-value-alignment.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner), [Business Analyst](#3-business-analyst))*
- Architecture strategic review produces [architecture executive approval](phases/3-design/outcomes/architecture-executive-approval.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Architect](#5-architect))*
- Budget & scope reality check produces [confirmed scope/budget or change request](phases/3-design/outcomes/confirmed-scope-budget-or-change-request.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner), [Project Manager](#8-project-manager-delivery))*
- Risk appetite ratification produces [ratified risk decisions](phases/3-design/outcomes/ratified-risk-decisions.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Security & Compliance](#6-security-compliance))*
- Vendor / partner executive alignment produces [vendor partnership agreement](phases/3-design/outcomes/vendor-partnership-agreement.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Steering committee review produces [steering checkpoint](phases/3-design/outcomes/steering-checkpoint.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Research technical options produces [technical options assessment](phases/3-design/artifacts/technical-options-assessment.md) *([Architect](#5-architect))*
- Document solution architecture produces [architecture document](phases/3-design/artifacts/architecture-document.md) *([Architect](#5-architect))*
- Architecture decision records produces [decision log](phases/3-design/outcomes/decision-log.md) *([Architect](#5-architect))*
- Integration / system context map produces [integration map](phases/3-design/artifacts/integration-map.md) *([Architect](#5-architect))*
- Data model / schema design produces [data model](phases/3-design/artifacts/data-model.md) *([Architect](#5-architect))*
- API / interface contract design produces [API specification](phases/3-design/artifacts/api-specification.md) *([Architect](#5-architect), [Developer](#9-developer))*
- Threat modeling produces [threat model](phases/3-design/artifacts/threat-model.md) *([Security & Compliance](#6-security-compliance), [Architect](#5-architect))*
- Secure design pattern selection produces [approved security patterns](phases/3-design/outcomes/approved-security-patterns.md) *([Security & Compliance](#6-security-compliance), [Architect](#5-architect))*
- Security & compliance review produces [security/compliance approval](phases/3-design/outcomes/security-compliance-approval.md) *([Security & Compliance](#6-security-compliance), [Architect](#5-architect), [Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Customer journey mapping produces [journey map / service blueprint](phases/3-design/artifacts/journey-map-service-blueprint.md) *([UI/UX Designer](#4-uiux-designer))*
- Information architecture produces [IA spec](phases/3-design/artifacts/ia-spec.md) *([UI/UX Designer](#4-uiux-designer))*
- Create design specifications produces [design specification](phases/3-design/artifacts/design-specification.md) *([UI/UX Designer](#4-uiux-designer))*
- Create visual design produces [visual design mockups](phases/3-design/artifacts/visual-design-mockups.md) *([UI/UX Designer](#4-uiux-designer))*
- Prototyping produces [interactive prototype](phases/3-design/artifacts/interactive-prototype.md) *([UI/UX Designer](#4-uiux-designer))*
- Usability testing (pre-build) produces [usability findings](phases/3-design/artifacts/usability-findings.md) *([UI/UX Designer](#4-uiux-designer))*
- Accessibility design review produces [accessibility design report](phases/3-design/artifacts/accessibility-design-report.md) *([UI/UX Designer](#4-uiux-designer))*
- [Design](phases/3-design/README.md) review & sign-off produces [approved design package](phases/3-design/outcomes/approved-design-package.md) *([UI/UX Designer](#4-uiux-designer), [Product Owner](#2-product-owner))*
- [Design](phases/3-design/README.md) → engineering handoff review produces [build-ready package](phases/3-design/artifacts/build-ready-package.md) *([UI/UX Designer](#4-uiux-designer), [Architect](#5-architect), [Developer](#9-developer))*
- Validate design against requirements produces [design-requirements validation](phases/3-design/artifacts/design-requirements-validation.md) *([Business Analyst](#3-business-analyst), [Security & Compliance](#6-security-compliance))*
- Update traceability (requirements → design) produces [updated traceability matrix](phases/3-design/artifacts/updated-traceability-matrix.md) *([Business Analyst](#3-business-analyst))*
- Vendor / buy option evaluation produces [vendor evaluation scorecard](phases/3-design/artifacts/vendor-evaluation-scorecard.md) *([Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Business rules documentation produces [business-rules catalog](phases/3-design/artifacts/business-rules-catalog.md) *([Business Analyst](#3-business-analyst))*
- Refine cost-benefit model with design-era data produces [updated ROI model](phases/3-design/artifacts/updated-roi-model.md) *([Business Analyst](#3-business-analyst))*
- Update test designs against approved design produces [design-aligned test designs](phases/3-design/artifacts/design-aligned-test-designs.md) *([QA/Tester](#10-qa-tester))*
- Vendor security & compliance assessment produces [vendor risk assessment](phases/3-design/artifacts/vendor-risk-assessment.md) *([Security & Compliance](#6-security-compliance))*
- [Design](phases/3-design/README.md)-phase schedule & resource coordination produces [design-phase plan](phases/3-design/artifacts/design-phase-plan.md) *([Project Manager](#8-project-manager-delivery))*
- Vendor selection process coordination produces [vendor selection process outputs](phases/3-design/artifacts/vendor-selection-process-outputs.md) *([Project Manager](#8-project-manager-delivery))*
- [Design](phases/3-design/README.md) review scheduling & minutes produces [decision log from design reviews](phases/3-design/outcomes/decision-log-from-design-reviews.md) *([Project Manager](#8-project-manager-delivery))*

### Artifacts
- [Build-vs-buy decision](phases/3-design/outcomes/build-vs-buy-decision.md)
- [validated business-value alignment](phases/3-design/artifacts/validated-business-value-alignment.md)
- [architecture executive approval](phases/3-design/outcomes/architecture-executive-approval.md)
- [confirmed scope/budget or change request](phases/3-design/outcomes/confirmed-scope-budget-or-change-request.md)
- [ratified risk decisions](phases/3-design/outcomes/ratified-risk-decisions.md)
- [vendor partnership agreement](phases/3-design/outcomes/vendor-partnership-agreement.md)
- [steering checkpoint](phases/3-design/outcomes/steering-checkpoint.md)
- [technical options assessment](phases/3-design/artifacts/technical-options-assessment.md)
- [architecture document](phases/3-design/artifacts/architecture-document.md)
- [decision log](phases/3-design/outcomes/decision-log.md)
- [integration map](phases/3-design/artifacts/integration-map.md)
- [data model](phases/3-design/artifacts/data-model.md)
- [API specification](phases/3-design/artifacts/api-specification.md)
- [threat model](phases/3-design/artifacts/threat-model.md)
- [approved security patterns](phases/3-design/outcomes/approved-security-patterns.md)
- [security/compliance approval](phases/3-design/outcomes/security-compliance-approval.md)
- [journey map / service blueprint](phases/3-design/artifacts/journey-map-service-blueprint.md)
- [IA spec](phases/3-design/artifacts/ia-spec.md)
- [design specification](phases/3-design/artifacts/design-specification.md)
- [visual design mockups](phases/3-design/artifacts/visual-design-mockups.md)
- [interactive prototype](phases/3-design/artifacts/interactive-prototype.md)
- [usability findings](phases/3-design/artifacts/usability-findings.md)
- [accessibility design report](phases/3-design/artifacts/accessibility-design-report.md)
- [approved design package](phases/3-design/outcomes/approved-design-package.md)
- [build-ready package](phases/3-design/artifacts/build-ready-package.md)
- [design-requirements validation](phases/3-design/artifacts/design-requirements-validation.md)
- [updated traceability matrix](phases/3-design/artifacts/updated-traceability-matrix.md)
- [vendor evaluation scorecard](phases/3-design/artifacts/vendor-evaluation-scorecard.md)
- [business-rules catalog](phases/3-design/artifacts/business-rules-catalog.md)
- [updated ROI model](phases/3-design/artifacts/updated-roi-model.md)
- [design-aligned test designs](phases/3-design/artifacts/design-aligned-test-designs.md)
- [vendor risk assessment](phases/3-design/artifacts/vendor-risk-assessment.md)
- [design-phase plan](phases/3-design/artifacts/design-phase-plan.md)
- [vendor selection process outputs](phases/3-design/artifacts/vendor-selection-process-outputs.md)
- [decision log from design reviews](phases/3-design/outcomes/decision-log-from-design-reviews.md)

## [4. Plan](phases/4-plan/README.md)
Goal: stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

- Approve staffing & resourcing plan produces [approved resource commitment](phases/4-plan/outcomes/approved-resource-commitment.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Technical skills & roles requirement produces [skills requirement input](phases/4-plan/artifacts/skills-requirement-input.md) *([Architect](#5-architect))*
- Resolve cross-portfolio priority conflicts produces [portfolio priority decision](phases/4-plan/outcomes/portfolio-priority-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Architect](#5-architect))*
- Approve delivery baseline produces [baselined schedule & budget commitment](phases/4-plan/outcomes/baselined-schedule-budget-commitment.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Project Manager](#8-project-manager-delivery))*
- Technical milestone sequencing produces [technical milestone plan](phases/4-plan/artifacts/technical-milestone-plan.md) *([Architect](#5-architect))*
- Set risk appetite & escalation thresholds produces [escalation policy](phases/4-plan/outcomes/escalation-policy.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Initiative kickoff & internal announcement produces [internal kickoff announcement](phases/4-plan/outcomes/internal-kickoff-announcement.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Manage product backlog produces [prioritized backlog](phases/4-plan/artifacts/prioritized-backlog.md) *([Product Owner](#2-product-owner))*
- Backlog decomposition (features → work items) produces [delivery-ready work items](phases/4-plan/artifacts/delivery-ready-work-items.md) *([Product Owner](#2-product-owner), [Business Analyst](#3-business-analyst))*
- Architecture runway / technical enablers produces [enabler backlog](phases/4-plan/artifacts/enabler-backlog.md) *([Architect](#5-architect), [Developer](#9-developer))*
- Analytics & telemetry instrumentation planning produces [telemetry plan](phases/4-plan/artifacts/telemetry-plan.md) *([Architect](#5-architect))*
- Feature flag strategy produces [feature flag plan](phases/4-plan/artifacts/feature-flag-plan.md) *([Architect](#5-architect), [Developer](#9-developer))*
- Infrastructure / environment provisioning produces [provisioned environments](phases/4-plan/artifacts/provisioned-environments.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- CI/CD pipeline setup produces [working CI/CD pipeline](phases/4-plan/artifacts/working-ci-cd-pipeline.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [Developer](#9-developer))*
- SLA / SLO definition produces [service-level objectives](phases/4-plan/artifacts/service-level-objectives.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [Product Owner](#2-product-owner))*
- Team onboarding & ramp-up produces [onboarded team](phases/4-plan/artifacts/onboarded-team.md) *([Project Manager](#8-project-manager-delivery))*
- Iteration / milestone planning produces [iteration plan](phases/4-plan/artifacts/iteration-plan.md) *([Project Manager](#8-project-manager-delivery))*
- Assign & manage workitems produces [assigned workitems & daily status](phases/4-plan/artifacts/assigned-workitems-daily-status.md) *([Project Manager](#8-project-manager-delivery))*
- Track features & epics produces [feature/epic status report](phases/4-plan/artifacts/feature-epic-status-report.md) *([Project Manager](#8-project-manager-delivery))*
- Resource tracking & scheduling produces [resource schedule](phases/4-plan/artifacts/resource-schedule.md) *([Project Manager](#8-project-manager-delivery))*
- Risk identification & escalation produces [risk register](phases/4-plan/artifacts/risk-register.md) *([Project Manager](#8-project-manager-delivery), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Test strategy produces [test plan](phases/4-plan/artifacts/test-plan.md) *([QA/Tester](#10-qa-tester))*
- Security test plan contribution produces [security test plan](phases/4-plan/artifacts/security-test-plan.md) *([Security & Compliance](#6-security-compliance), [QA/Tester](#10-qa-tester))*
- [Define](phases/2-define/README.md) security & compliance controls in pipeline produces [pipeline security controls](phases/4-plan/artifacts/pipeline-security-controls.md) *([Security & Compliance](#6-security-compliance))*
- Compliance evidence plan produces [evidence collection plan](phases/4-plan/artifacts/evidence-collection-plan.md) *([Security & Compliance](#6-security-compliance))*
- Incident response plan produces [IR plan & runbook](phases/4-plan/artifacts/ir-plan-runbook.md) *([Security & Compliance](#6-security-compliance))*
- Rollout & rollback plan produces [deployment runbook](phases/4-plan/artifacts/deployment-runbook.md) *([Release Manager](#11-release-manager), [Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Benefits realization plan produces [benefits plan](phases/4-plan/artifacts/benefits-plan.md) *([Business Analyst](#3-business-analyst))*
- Approve benefits realization plan produces [approved benefits plan](phases/4-plan/outcomes/approved-benefits-plan.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Stakeholder communication plan produces [stakeholder comms plan](phases/4-plan/artifacts/stakeholder-comms-plan.md) *([Business Analyst](#3-business-analyst))*
- Execute stakeholder communication cadence produces [executed comms per cadence](phases/4-plan/artifacts/executed-comms-per-cadence.md) *([Project Manager](#8-project-manager-delivery))*
- Dependency / RAID management setup produces [RAID log](phases/4-plan/artifacts/raid-log.md) *([Project Manager](#8-project-manager-delivery))*
- Governance cadence setup produces [governance calendar](phases/4-plan/artifacts/governance-calendar.md) *([Project Manager](#8-project-manager-delivery))*
- Change-review process setup produces [changelog review process](phases/4-plan/artifacts/changelog-review-process.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*

### Artifacts
- [Approved resource commitment](phases/4-plan/outcomes/approved-resource-commitment.md)
- [skills requirement input](phases/4-plan/artifacts/skills-requirement-input.md)
- [portfolio priority decision](phases/4-plan/outcomes/portfolio-priority-decision.md)
- [baselined schedule & budget commitment](phases/4-plan/outcomes/baselined-schedule-budget-commitment.md)
- [technical milestone plan](phases/4-plan/artifacts/technical-milestone-plan.md)
- [escalation policy](phases/4-plan/outcomes/escalation-policy.md)
- [internal kickoff announcement](phases/4-plan/outcomes/internal-kickoff-announcement.md)
- [prioritized backlog](phases/4-plan/artifacts/prioritized-backlog.md)
- [delivery-ready work items](phases/4-plan/artifacts/delivery-ready-work-items.md)
- [enabler backlog](phases/4-plan/artifacts/enabler-backlog.md)
- [telemetry plan](phases/4-plan/artifacts/telemetry-plan.md)
- [feature flag plan](phases/4-plan/artifacts/feature-flag-plan.md)
- [provisioned environments](phases/4-plan/artifacts/provisioned-environments.md)
- [working CI/CD pipeline](phases/4-plan/artifacts/working-ci-cd-pipeline.md)
- [service-level objectives](phases/4-plan/artifacts/service-level-objectives.md)
- [onboarded team](phases/4-plan/artifacts/onboarded-team.md)
- [iteration plan](phases/4-plan/artifacts/iteration-plan.md)
- [assigned workitems & daily status](phases/4-plan/artifacts/assigned-workitems-daily-status.md)
- [feature/epic status report](phases/4-plan/artifacts/feature-epic-status-report.md)
- [resource schedule](phases/4-plan/artifacts/resource-schedule.md)
- [risk register](phases/4-plan/artifacts/risk-register.md)
- [test plan](phases/4-plan/artifacts/test-plan.md)
- [security test plan](phases/4-plan/artifacts/security-test-plan.md)
- [pipeline security controls](phases/4-plan/artifacts/pipeline-security-controls.md)
- [evidence collection plan](phases/4-plan/artifacts/evidence-collection-plan.md)
- [IR plan & runbook](phases/4-plan/artifacts/ir-plan-runbook.md)
- [deployment runbook](phases/4-plan/artifacts/deployment-runbook.md)
- [benefits plan](phases/4-plan/artifacts/benefits-plan.md)
- [approved benefits plan](phases/4-plan/outcomes/approved-benefits-plan.md)
- [stakeholder comms plan](phases/4-plan/artifacts/stakeholder-comms-plan.md)
- [executed comms per cadence](phases/4-plan/artifacts/executed-comms-per-cadence.md)
- [RAID log](phases/4-plan/artifacts/raid-log.md)
- [governance calendar](phases/4-plan/artifacts/governance-calendar.md)
- [changelog review process](phases/4-plan/artifacts/changelog-review-process.md)

## [5. Build](phases/5-build/README.md)
Goal: produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

- Executive checkpoint review produces [executive status update](phases/5-build/artifacts/executive-status-update.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Unblock cross-org dependencies produces [unblocked dependencies](phases/5-build/outcomes/unblocked-dependencies.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Project Manager](#8-project-manager-delivery))*
- Scope discipline / change control produces [scope-change decisions](phases/5-build/outcomes/scope-change-decisions.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner))*
- Re-validate business case vs. emerging reality produces [business-case reconfirmation or reset](phases/5-build/outcomes/business-case-reconfirmation-or-reset.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Business Analyst](#3-business-analyst))*
- [Design](phases/3-design/README.md)-partner / early-customer engagement produces [committed design partners](phases/5-build/outcomes/committed-design-partners.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Steering / board progress briefing produces [governance briefing](phases/5-build/artifacts/governance-briefing.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Progress review & increment acceptance produces [accepted increments](phases/5-build/outcomes/accepted-increments.md) *([Product Owner](#2-product-owner), [Project Manager](#8-project-manager-delivery))*
- Process improvement review produces [process improvement actions](phases/5-build/artifacts/process-improvement-actions.md) *([Project Manager](#8-project-manager-delivery))*
- Security scanning (SAST/SCA) produces [vulnerability scan report](phases/5-build/artifacts/vulnerability-scan-report.md) *([Security & Compliance](#6-security-compliance), [Developer](#9-developer))*
- Vulnerability triage & remediation SLA tracking produces [triaged vulnerabilities](phases/5-build/artifacts/triaged-vulnerabilities.md) *([Security & Compliance](#6-security-compliance))*
- MVP delivery produces [MVP](phases/5-build/artifacts/mvp.md) *([Developer](#9-developer), [Product Owner](#2-product-owner))*
- Review & code workitems produces [implemented workitems](phases/5-build/artifacts/implemented-workitems.md) *([Developer](#9-developer))*
- New feature development produces [feature code](phases/5-build/artifacts/feature-code.md) *([Developer](#9-developer))*
- Code review produces [reviewed code](phases/5-build/artifacts/reviewed-code.md) *([Developer](#9-developer), [Security & Compliance](#6-security-compliance))*
- Merge code produces [merged code in main branch](phases/5-build/artifacts/merged-code-in-main-branch.md) *([Developer](#9-developer))*
- Static analysis / linting produces [lint/static-analysis report](phases/5-build/artifacts/lint-static-analysis-report.md) *([Developer](#9-developer))*
- Telemetry implementation produces [instrumented code](phases/5-build/artifacts/instrumented-code.md) *([Developer](#9-developer))*
- Inline / API code documentation produces [generated API docs](phases/5-build/artifacts/generated-api-docs.md) *([Developer](#9-developer))*
- Develop tests produces [automated test suite](phases/5-build/artifacts/automated-test-suite.md) *([QA/Tester](#10-qa-tester))*
- Integration testing produces [integration test results](phases/5-build/artifacts/integration-test-results.md) *([QA/Tester](#10-qa-tester), [Developer](#9-developer))*
- Requirements clarification support produces [clarified requirements](phases/5-build/artifacts/clarified-requirements.md) *([Business Analyst](#3-business-analyst))*
- Scope-change impact analysis produces [change impact report](phases/5-build/artifacts/change-impact-report.md) *([Business Analyst](#3-business-analyst))*
- In-flight benefits & assumptions tracking produces [assumptions & benefits-tracking log](phases/5-build/artifacts/assumptions-benefits-tracking-log.md) *([Business Analyst](#3-business-analyst))*
- Raise requirements questions & impediments produces [requirements questions log](phases/5-build/artifacts/requirements-questions-log.md) *([Developer](#9-developer), [QA/Tester](#10-qa-tester))*
- Architecture status input produces [architecture status report](phases/5-build/artifacts/architecture-status-report.md) *([Architect](#5-architect))*
- Resolve technical blockers produces [resolved technical blockers](phases/5-build/outcomes/resolved-technical-blockers.md) *([Architect](#5-architect))*
- Technical impact of scope changes produces [technical impact analysis](phases/5-build/artifacts/technical-impact-analysis.md) *([Architect](#5-architect))*
- Technical design guidance & pairing produces [design guidance sessions](phases/5-build/artifacts/design-guidance-sessions.md) *([Architect](#5-architect))*
- Architecture conformance review produces [conformance findings](phases/5-build/artifacts/conformance-findings.md) *([Architect](#5-architect))*
- Update architecture decision records produces [updated ADRs](phases/5-build/artifacts/updated-adrs.md) *([Architect](#5-architect))*
- Sponsor/PO status report preparation produces [weekly/biweekly status report](phases/5-build/artifacts/weekly-biweekly-status-report.md) *([Project Manager](#8-project-manager-delivery))*
- Scope-change impact coordination produces [change control package](phases/5-build/artifacts/change-control-package.md) *([Project Manager](#8-project-manager-delivery))*
- RAID log maintenance produces [updated RAID log](phases/5-build/artifacts/updated-raid-log.md) *([Project Manager](#8-project-manager-delivery))*
- Cross-team sync facilitation produces [cross-team sync notes](phases/5-build/artifacts/cross-team-sync-notes.md) *([Project Manager](#8-project-manager-delivery))*
- Budget & burn tracking produces [budget burn report](phases/5-build/artifacts/budget-burn-report.md) *([Project Manager](#8-project-manager-delivery))*
- Vendor & contract management produces [managed vendor deliverables](phases/5-build/artifacts/managed-vendor-deliverables.md) *([Project Manager](#8-project-manager-delivery))*
- Review incoming changes (changelog) produces [reviewed change log](phases/5-build/artifacts/reviewed-change-log.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*

### Artifacts
- [Executive status update](phases/5-build/artifacts/executive-status-update.md)
- [unblocked dependencies](phases/5-build/outcomes/unblocked-dependencies.md)
- [scope-change decisions](phases/5-build/outcomes/scope-change-decisions.md)
- [business-case reconfirmation or reset](phases/5-build/outcomes/business-case-reconfirmation-or-reset.md)
- [committed design partners](phases/5-build/outcomes/committed-design-partners.md)
- [governance briefing](phases/5-build/artifacts/governance-briefing.md)
- [accepted increments](phases/5-build/outcomes/accepted-increments.md)
- [process improvement actions](phases/5-build/artifacts/process-improvement-actions.md)
- [vulnerability scan report](phases/5-build/artifacts/vulnerability-scan-report.md)
- [triaged vulnerabilities](phases/5-build/artifacts/triaged-vulnerabilities.md)
- [MVP](phases/5-build/artifacts/mvp.md)
- [implemented workitems](phases/5-build/artifacts/implemented-workitems.md)
- [feature code](phases/5-build/artifacts/feature-code.md)
- [reviewed code](phases/5-build/artifacts/reviewed-code.md)
- [merged code in main branch](phases/5-build/artifacts/merged-code-in-main-branch.md)
- [lint/static-analysis report](phases/5-build/artifacts/lint-static-analysis-report.md)
- [instrumented code](phases/5-build/artifacts/instrumented-code.md)
- [generated API docs](phases/5-build/artifacts/generated-api-docs.md)
- [automated test suite](phases/5-build/artifacts/automated-test-suite.md)
- [integration test results](phases/5-build/artifacts/integration-test-results.md)
- [clarified requirements](phases/5-build/artifacts/clarified-requirements.md)
- [change impact report](phases/5-build/artifacts/change-impact-report.md)
- [assumptions & benefits-tracking log](phases/5-build/artifacts/assumptions-benefits-tracking-log.md)
- [requirements questions log](phases/5-build/artifacts/requirements-questions-log.md)
- [architecture status report](phases/5-build/artifacts/architecture-status-report.md)
- [resolved technical blockers](phases/5-build/outcomes/resolved-technical-blockers.md)
- [technical impact analysis](phases/5-build/artifacts/technical-impact-analysis.md)
- [design guidance sessions](phases/5-build/artifacts/design-guidance-sessions.md)
- [conformance findings](phases/5-build/artifacts/conformance-findings.md)
- [updated ADRs](phases/5-build/artifacts/updated-adrs.md)
- [weekly/biweekly status report](phases/5-build/artifacts/weekly-biweekly-status-report.md)
- [change control package](phases/5-build/artifacts/change-control-package.md)
- [updated RAID log](phases/5-build/artifacts/updated-raid-log.md)
- [cross-team sync notes](phases/5-build/artifacts/cross-team-sync-notes.md)
- [budget burn report](phases/5-build/artifacts/budget-burn-report.md)
- [managed vendor deliverables](phases/5-build/artifacts/managed-vendor-deliverables.md)
- [reviewed change log](phases/5-build/artifacts/reviewed-change-log.md)

## [6. Verify](phases/6-verify/README.md)
Goal: evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

- Review launch-readiness metrics produces [launch-readiness assessment](phases/6-verify/artifacts/launch-readiness-assessment.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Approve beta / early-access cohort produces [approved launch cohort](phases/6-verify/outcomes/approved-launch-cohort.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner))*
- Approve launch window / date produces [committed launch date](phases/6-verify/outcomes/committed-launch-date.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Release Manager](#11-release-manager))*
- Approve launch risk posture produces [approved known-issues & risk acceptance](phases/6-verify/outcomes/approved-known-issues-risk-acceptance.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner), [Security & Compliance](#6-security-compliance))*
- Analyst / press / reference pre-briefing produces [warmed market & analyst briefings](phases/6-verify/outcomes/warmed-market-analyst-briefings.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Validate visual fidelity to design produces [visual QA report](phases/6-verify/artifacts/visual-qa-report.md) *([UI/UX Designer](#4-uiux-designer))*
- Security testing / pen test produces [security test report](phases/6-verify/artifacts/security-test-report.md) *([Security & Compliance](#6-security-compliance), [QA/Tester](#10-qa-tester))*
- Chaos / resilience testing produces [resilience test results](phases/6-verify/artifacts/resilience-test-results.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [QA/Tester](#10-qa-tester))*
- Data migration dress rehearsal produces [migration runbook validation](phases/6-verify/artifacts/migration-runbook-validation.md) *([Developer](#9-developer), [Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Operational readiness review produces [PRR sign-off](phases/6-verify/outcomes/prr-sign-off.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [Release Manager](#11-release-manager), [Architect](#5-architect))*
- Assess feature readiness produces [readiness assessment](phases/6-verify/artifacts/readiness-assessment.md) *([QA/Tester](#10-qa-tester), [Security & Compliance](#6-security-compliance))*
- Compliance readiness review produces [compliance go/no-go](phases/6-verify/outcomes/compliance-go-no-go.md) *([Security & Compliance](#6-security-compliance))*
- Pre-launch validation — UAT / beta produces [UAT/beta sign-off](phases/6-verify/outcomes/uat-beta-sign-off.md) *([QA/Tester](#10-qa-tester), [Product Owner](#2-product-owner))*
- Performance / load testing produces [performance test report](phases/6-verify/artifacts/performance-test-report.md) *([QA/Tester](#10-qa-tester), [Site Reliability Engineer](#7-site-reliability-engineer-sre), [Architect](#5-architect))*
- Accessibility testing produces [accessibility audit report](phases/6-verify/artifacts/accessibility-audit-report.md) *([QA/Tester](#10-qa-tester), [UI/UX Designer](#4-uiux-designer))*
- Regression testing produces [regression test results](phases/6-verify/artifacts/regression-test-results.md) *([QA/Tester](#10-qa-tester))*
- Staging deployment & smoke tests produces [validated staging environment](phases/6-verify/artifacts/validated-staging-environment.md) *([Release Manager](#11-release-manager), [QA/Tester](#10-qa-tester))*
- Troubleshoot build & deploy activities produces [stable build/deploy pipeline](phases/6-verify/artifacts/stable-build-deploy-pipeline.md) *([Release Manager](#11-release-manager))*
- Documentation review produces [verified docs](phases/6-verify/artifacts/verified-docs.md) *([Technical Writer](#12-technical-writer), [QA/Tester](#10-qa-tester))*
- UAT coordination with business users produces [UAT coordination & results](phases/6-verify/artifacts/uat-coordination-results.md) *([Business Analyst](#3-business-analyst))*
- Recruit & onboard UAT / beta users produces [recruited UAT cohort](phases/6-verify/artifacts/recruited-uat-cohort.md) *([Customer Support](#14-customer-support-success), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- UAT defect triage produces [triaged UAT defects](phases/6-verify/artifacts/triaged-uat-defects.md) *([QA/Tester](#10-qa-tester), [Developer](#9-developer))*
- Benefits-readiness assessment produces [benefits-readiness report](phases/6-verify/artifacts/benefits-readiness-report.md) *([Business Analyst](#3-business-analyst))*
- [Verify](phases/6-verify/README.md) KPI telemetry emission produces [verified KPI telemetry](phases/6-verify/artifacts/verified-kpi-telemetry.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [Developer](#9-developer))*
- Architecture validation in verify env produces [architecture validation report](phases/6-verify/artifacts/architecture-validation-report.md) *([Architect](#5-architect))*
- Architectural risk assessment produces [architectural risk report](phases/6-verify/artifacts/architectural-risk-report.md) *([Architect](#5-architect))*
- [Verify](phases/6-verify/README.md)-phase coordination produces [verify execution plan](phases/6-verify/artifacts/verify-execution-plan.md) *([Project Manager](#8-project-manager-delivery))*
- [Launch](phases/7-launch/README.md)-readiness status reporting produces [launch-readiness status pack](phases/6-verify/artifacts/launch-readiness-status-pack.md) *([Project Manager](#8-project-manager-delivery))*
- Issue / defect governance produces [defect status & triage cadence](phases/6-verify/artifacts/defect-status-triage-cadence.md) *([Project Manager](#8-project-manager-delivery))*

### Artifacts
- [Launch-readiness assessment](phases/6-verify/artifacts/launch-readiness-assessment.md)
- [approved launch cohort](phases/6-verify/outcomes/approved-launch-cohort.md)
- [committed launch date](phases/6-verify/outcomes/committed-launch-date.md)
- [approved known-issues & risk acceptance](phases/6-verify/outcomes/approved-known-issues-risk-acceptance.md)
- [warmed market & analyst briefings](phases/6-verify/outcomes/warmed-market-analyst-briefings.md)
- [visual QA report](phases/6-verify/artifacts/visual-qa-report.md)
- [security test report](phases/6-verify/artifacts/security-test-report.md)
- [resilience test results](phases/6-verify/artifacts/resilience-test-results.md)
- [migration runbook validation](phases/6-verify/artifacts/migration-runbook-validation.md)
- [PRR sign-off](phases/6-verify/outcomes/prr-sign-off.md)
- [readiness assessment](phases/6-verify/artifacts/readiness-assessment.md)
- [compliance go/no-go](phases/6-verify/outcomes/compliance-go-no-go.md)
- [UAT/beta sign-off](phases/6-verify/outcomes/uat-beta-sign-off.md)
- [performance test report](phases/6-verify/artifacts/performance-test-report.md)
- [accessibility audit report](phases/6-verify/artifacts/accessibility-audit-report.md)
- [regression test results](phases/6-verify/artifacts/regression-test-results.md)
- [validated staging environment](phases/6-verify/artifacts/validated-staging-environment.md)
- [stable build/deploy pipeline](phases/6-verify/artifacts/stable-build-deploy-pipeline.md)
- [verified docs](phases/6-verify/artifacts/verified-docs.md)
- [UAT coordination & results](phases/6-verify/artifacts/uat-coordination-results.md)
- [recruited UAT cohort](phases/6-verify/artifacts/recruited-uat-cohort.md)
- [triaged UAT defects](phases/6-verify/artifacts/triaged-uat-defects.md)
- [benefits-readiness report](phases/6-verify/artifacts/benefits-readiness-report.md)
- [verified KPI telemetry](phases/6-verify/artifacts/verified-kpi-telemetry.md)
- [architecture validation report](phases/6-verify/artifacts/architecture-validation-report.md)
- [architectural risk report](phases/6-verify/artifacts/architectural-risk-report.md)
- [verify execution plan](phases/6-verify/artifacts/verify-execution-plan.md)
- [launch-readiness status pack](phases/6-verify/artifacts/launch-readiness-status-pack.md)
- [defect status & triage cadence](phases/6-verify/artifacts/defect-status-triage-cadence.md)

## [7. Launch](phases/7-launch/README.md)
Goal: product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

- Board / investor launch briefing produces [board/investor launch narrative](phases/7-launch/artifacts/board-investor-launch-narrative.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Internal all-hands launch communication produces [internal launch announcement](phases/7-launch/artifacts/internal-launch-announcement.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Real-time launch metrics monitoring produces [live launch-day status](phases/7-launch/outcomes/live-launch-day-status.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- [Launch](phases/7-launch/README.md) rollback decision authority produces [continue/rollback decision](phases/7-launch/outcomes/continue-rollback-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Release Manager](#11-release-manager))*
- External analyst & press engagement produces [analyst/press coverage](phases/7-launch/artifacts/analyst-press-coverage.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Team recognition & celebration produces [recognized team & captured wins](phases/7-launch/outcomes/recognized-team-captured-wins.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Architectural rollback safety review produces [rollback safety sign-off](phases/7-launch/outcomes/rollback-safety-sign-off.md) *([Architect](#5-architect))*
- Architectural launch signals monitoring produces [architectural launch signals](phases/7-launch/artifacts/architectural-launch-signals.md) *([Architect](#5-architect))*
- [Launch](phases/7-launch/README.md) day coordination / command center produces [launch run-of-show](phases/7-launch/artifacts/launch-run-of-show.md) *([Project Manager](#8-project-manager-delivery))*
- [Launch](phases/7-launch/README.md) comms execution produces [executed launch comms](phases/7-launch/artifacts/executed-launch-comms.md) *([Project Manager](#8-project-manager-delivery))*
- [Launch](phases/7-launch/README.md) stage-gate coordination produces [go/no-go decision package](phases/7-launch/outcomes/go-no-go-decision-package.md) *([Project Manager](#8-project-manager-delivery))*
- [Launch](phases/7-launch/README.md) readiness review / go-no-go produces [go/no-go decision](phases/7-launch/outcomes/go-no-go-decision.md) *([Product Owner](#2-product-owner), [Release Manager](#11-release-manager), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Legal & compliance final sign-off produces [legal approval](phases/7-launch/outcomes/legal-approval.md) *([Security & Compliance](#6-security-compliance), [Product Owner](#2-product-owner))*
- [Launch](phases/7-launch/README.md) baseline snapshot produces [pre-launch metrics baseline](phases/7-launch/artifacts/pre-launch-metrics-baseline.md) *([Business Analyst](#3-business-analyst), [Product Owner](#2-product-owner))*
- Write release notes produces [release notes](phases/7-launch/artifacts/release-notes.md) *([Release Manager](#11-release-manager))*
- Deploy / release execution produces [released product in production](phases/7-launch/artifacts/released-product-in-production.md) *([Release Manager](#11-release-manager))*
- Post-deploy production smoke tests produces [production validation](phases/7-launch/artifacts/production-validation.md) *([QA/Tester](#10-qa-tester), [Release Manager](#11-release-manager))*
- [Launch](phases/7-launch/README.md) war room / hypercare produces [stabilized launch window](phases/7-launch/outcomes/stabilized-launch-window.md) *([Release Manager](#11-release-manager), [Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Create feature documentation produces [feature documentation](phases/7-launch/artifacts/feature-documentation.md) *([Technical Writer](#12-technical-writer))*
- Draft user guides produces [user guides](phases/7-launch/artifacts/user-guides.md) *([Technical Writer](#12-technical-writer))*
- Create marketing resources & battlecards produces [marketing collateral](phases/7-launch/artifacts/marketing-collateral.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- [Launch](phases/7-launch/README.md) event produces [launch announcement](phases/7-launch/artifacts/launch-announcement.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Pricing & packaging decision produces [pricing & packaging plan](phases/7-launch/artifacts/pricing-packaging-plan.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement), [Product Owner](#2-product-owner), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Internal enablement / training produces [trained sales & support teams](phases/7-launch/artifacts/trained-sales-support-teams.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement), [Customer Support](#14-customer-support-success))*
- Customer communications produces [launch announcement emails/notices](phases/7-launch/artifacts/launch-announcement-emails-notices.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Create sample data & demos produces [demo assets](phases/7-launch/artifacts/demo-assets.md) *([Developer](#9-developer))*
- [Launch](phases/7-launch/README.md) KPI dashboard setup produces [live launch KPI dashboard](phases/7-launch/outcomes/live-launch-kpi-dashboard.md) *([Business Analyst](#3-business-analyst))*
- Wire KPI events into dashboard produces [connected KPI data pipeline](phases/7-launch/artifacts/connected-kpi-data-pipeline.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [Developer](#9-developer))*
- Process change rollout to impacted business teams produces [rolled-out process changes](phases/7-launch/artifacts/rolled-out-process-changes.md) *([Business Analyst](#3-business-analyst))*
- Execute support process cutover produces [live support processes](phases/7-launch/artifacts/live-support-processes.md) *([Customer Support](#14-customer-support-success))*
- Execute sales process cutover produces [live sales processes](phases/7-launch/artifacts/live-sales-processes.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*

### Artifacts
- [Board/investor launch narrative](phases/7-launch/artifacts/board-investor-launch-narrative.md)
- [internal launch announcement](phases/7-launch/artifacts/internal-launch-announcement.md)
- [live launch-day status](phases/7-launch/outcomes/live-launch-day-status.md)
- [continue/rollback decision](phases/7-launch/outcomes/continue-rollback-decision.md)
- [analyst/press coverage](phases/7-launch/artifacts/analyst-press-coverage.md)
- [recognized team & captured wins](phases/7-launch/outcomes/recognized-team-captured-wins.md)
- [rollback safety sign-off](phases/7-launch/outcomes/rollback-safety-sign-off.md)
- [architectural launch signals](phases/7-launch/artifacts/architectural-launch-signals.md)
- [launch run-of-show](phases/7-launch/artifacts/launch-run-of-show.md)
- [executed launch comms](phases/7-launch/artifacts/executed-launch-comms.md)
- [go/no-go decision package](phases/7-launch/outcomes/go-no-go-decision-package.md)
- [go/no-go decision](phases/7-launch/outcomes/go-no-go-decision.md)
- [legal approval](phases/7-launch/outcomes/legal-approval.md)
- [pre-launch metrics baseline](phases/7-launch/artifacts/pre-launch-metrics-baseline.md)
- [release notes](phases/7-launch/artifacts/release-notes.md)
- [released product in production](phases/7-launch/artifacts/released-product-in-production.md)
- [production validation](phases/7-launch/artifacts/production-validation.md)
- [stabilized launch window](phases/7-launch/outcomes/stabilized-launch-window.md)
- [feature documentation](phases/7-launch/artifacts/feature-documentation.md)
- [user guides](phases/7-launch/artifacts/user-guides.md)
- [marketing collateral](phases/7-launch/artifacts/marketing-collateral.md)
- [launch announcement](phases/7-launch/artifacts/launch-announcement.md)
- [pricing & packaging plan](phases/7-launch/artifacts/pricing-packaging-plan.md)
- [trained sales & support teams](phases/7-launch/artifacts/trained-sales-support-teams.md)
- [launch announcement emails/notices](phases/7-launch/artifacts/launch-announcement-emails-notices.md)
- [demo assets](phases/7-launch/artifacts/demo-assets.md)
- [live launch KPI dashboard](phases/7-launch/outcomes/live-launch-kpi-dashboard.md)
- [connected KPI data pipeline](phases/7-launch/artifacts/connected-kpi-data-pipeline.md)
- [rolled-out process changes](phases/7-launch/artifacts/rolled-out-process-changes.md)
- [live support processes](phases/7-launch/artifacts/live-support-processes.md)
- [live sales processes](phases/7-launch/artifacts/live-sales-processes.md)

## [8. Operate](phases/8-operate/README.md)
Goal: run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

- Review operational KPIs & SLO performance produces [operational performance review](phases/8-operate/artifacts/operational-performance-review.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Approve Sev-1 external comms produces [approved incident comms](phases/8-operate/outcomes/approved-incident-comms.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Revenue / ARR tracking produces [revenue report](phases/8-operate/artifacts/revenue-report.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Unit-economics / margin review produces [margin & CAC/LTV report](phases/8-operate/artifacts/margin-cac-ltv-report.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Application monitoring produces [monitoring dashboards & alerts](phases/8-operate/artifacts/monitoring-dashboards-alerts.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Investigate production errors produces [incident investigation report](phases/8-operate/artifacts/incident-investigation-report.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Root cause analysis produces [root cause analysis report](phases/8-operate/artifacts/root-cause-analysis-report.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [Developer](#9-developer), [Architect](#5-architect))*
- Incident response / on-call produces [incident postmortem](phases/8-operate/artifacts/incident-postmortem.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Backup & disaster-recovery testing produces [DR test results](phases/8-operate/artifacts/dr-test-results.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Cost / capacity monitoring produces [cost & capacity report](phases/8-operate/artifacts/cost-capacity-report.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre), [Architect](#5-architect))*
- Triage & log production issues for developer fixes produces [prioritized prod issue log](phases/8-operate/artifacts/prioritized-prod-issue-log.md) *([Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Compliance audit evidence collection produces [audit evidence](phases/8-operate/artifacts/audit-evidence.md) *([Security & Compliance](#6-security-compliance))*
- Security patching produces [patched dependencies](phases/8-operate/artifacts/patched-dependencies.md) *([Security & Compliance](#6-security-compliance), [Developer](#9-developer), [Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Security monitoring & SIEM operations produces [security monitoring alerts](phases/8-operate/artifacts/security-monitoring-alerts.md) *([Security & Compliance](#6-security-compliance), [Site Reliability Engineer](#7-site-reliability-engineer-sre))*
- Security incident response produces [security incident postmortems](phases/8-operate/artifacts/security-incident-postmortems.md) *([Security & Compliance](#6-security-compliance))*
- Periodic compliance audit produces [audit report / attestation](phases/8-operate/artifacts/audit-report-attestation.md) *([Security & Compliance](#6-security-compliance))*
- Access reviews produces [access review results](phases/8-operate/artifacts/access-review-results.md) *([Security & Compliance](#6-security-compliance))*
- Customer onboarding / activation produces [activated customers](phases/8-operate/artifacts/activated-customers.md) *([Customer Support](#14-customer-support-success))*
- Customer health scoring produces [health scores & at-risk list](phases/8-operate/artifacts/health-scores-at-risk-list.md) *([Customer Support](#14-customer-support-success))*
- QBRs / customer check-ins produces [renewal & expansion pipeline](phases/8-operate/artifacts/renewal-expansion-pipeline.md) *([Customer Support](#14-customer-support-success))*
- Renewal & expansion management produces [renewal & expansion bookings](phases/8-operate/artifacts/renewal-expansion-bookings.md) *([Customer Support](#14-customer-support-success), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Win/loss analysis produces [win-loss insights](phases/8-operate/artifacts/win-loss-insights.md) *([Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Triage customer support issues produces [triaged ticket queue](phases/8-operate/artifacts/triaged-ticket-queue.md) *([Customer Support](#14-customer-support-success))*
- Troubleshoot customer issues produces [customer resolution](phases/8-operate/artifacts/customer-resolution.md) *([Customer Support](#14-customer-support-success))*
- Identify known issues produces [known-issues list](phases/8-operate/artifacts/known-issues-list.md) *([Customer Support](#14-customer-support-success))*
- Escalate user issues produces [escalated issue ticket](phases/8-operate/artifacts/escalated-issue-ticket.md) *([Customer Support](#14-customer-support-success))*
- Curate documentation for customers produces [customer-facing knowledge base](phases/8-operate/artifacts/customer-facing-knowledge-base.md) *([Technical Writer](#12-technical-writer))*
- Business-metric reporting cadence produces [business performance report](phases/8-operate/artifacts/business-performance-report.md) *([Business Analyst](#3-business-analyst))*
- Business review meeting produces [business review decisions](phases/8-operate/outcomes/business-review-decisions.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Product Owner](#2-product-owner))*
- Value-realization tracking produces [ongoing benefits tracking](phases/8-operate/artifacts/ongoing-benefits-tracking.md) *([Business Analyst](#3-business-analyst))*
- Support data analysis produces [support/VoC trend analysis](phases/8-operate/artifacts/support-voc-trend-analysis.md) *([Business Analyst](#3-business-analyst))*
- Tag / categorize support tickets produces [tagged support-ticket dataset](phases/8-operate/artifacts/tagged-support-ticket-dataset.md) *([Customer Support](#14-customer-support-success))*
- Architectural health monitoring produces [architectural health report](phases/8-operate/artifacts/architectural-health-report.md) *([Architect](#5-architect))*
- Capacity & scale architecture review produces [scale-readiness report](phases/8-operate/artifacts/scale-readiness-report.md) *([Architect](#5-architect))*
- Evolve architecture from production learnings produces [architecture updates](phases/8-operate/artifacts/architecture-updates.md) *([Architect](#5-architect))*
- Hypercare transition to steady-state produces [steady-state operating handoff](phases/8-operate/outcomes/steady-state-operating-handoff.md) *([Project Manager](#8-project-manager-delivery))*
- Operating cadence coordination produces [operating review meetings](phases/8-operate/artifacts/operating-review-meetings.md) *([Project Manager](#8-project-manager-delivery))*

### Artifacts
- [Operational performance review](phases/8-operate/artifacts/operational-performance-review.md)
- [approved incident comms](phases/8-operate/outcomes/approved-incident-comms.md)
- [revenue report](phases/8-operate/artifacts/revenue-report.md)
- [margin & CAC/LTV report](phases/8-operate/artifacts/margin-cac-ltv-report.md)
- [monitoring dashboards & alerts](phases/8-operate/artifacts/monitoring-dashboards-alerts.md)
- [incident investigation report](phases/8-operate/artifacts/incident-investigation-report.md)
- [root cause analysis report](phases/8-operate/artifacts/root-cause-analysis-report.md)
- [incident postmortem](phases/8-operate/artifacts/incident-postmortem.md)
- [DR test results](phases/8-operate/artifacts/dr-test-results.md)
- [cost & capacity report](phases/8-operate/artifacts/cost-capacity-report.md)
- [prioritized prod issue log](phases/8-operate/artifacts/prioritized-prod-issue-log.md)
- [audit evidence](phases/8-operate/artifacts/audit-evidence.md)
- [patched dependencies](phases/8-operate/artifacts/patched-dependencies.md)
- [security monitoring alerts](phases/8-operate/artifacts/security-monitoring-alerts.md)
- [security incident postmortems](phases/8-operate/artifacts/security-incident-postmortems.md)
- [audit report / attestation](phases/8-operate/artifacts/audit-report-attestation.md)
- [access review results](phases/8-operate/artifacts/access-review-results.md)
- [activated customers](phases/8-operate/artifacts/activated-customers.md)
- [health scores & at-risk list](phases/8-operate/artifacts/health-scores-at-risk-list.md)
- [renewal & expansion pipeline](phases/8-operate/artifacts/renewal-expansion-pipeline.md)
- [renewal & expansion bookings](phases/8-operate/artifacts/renewal-expansion-bookings.md)
- [win-loss insights](phases/8-operate/artifacts/win-loss-insights.md)
- [triaged ticket queue](phases/8-operate/artifacts/triaged-ticket-queue.md)
- [customer resolution](phases/8-operate/artifacts/customer-resolution.md)
- [known-issues list](phases/8-operate/artifacts/known-issues-list.md)
- [escalated issue ticket](phases/8-operate/artifacts/escalated-issue-ticket.md)
- [customer-facing knowledge base](phases/8-operate/artifacts/customer-facing-knowledge-base.md)
- [business performance report](phases/8-operate/artifacts/business-performance-report.md)
- [business review decisions](phases/8-operate/outcomes/business-review-decisions.md)
- [ongoing benefits tracking](phases/8-operate/artifacts/ongoing-benefits-tracking.md)
- [support/VoC trend analysis](phases/8-operate/artifacts/support-voc-trend-analysis.md)
- [tagged support-ticket dataset](phases/8-operate/artifacts/tagged-support-ticket-dataset.md)
- [architectural health report](phases/8-operate/artifacts/architectural-health-report.md)
- [scale-readiness report](phases/8-operate/artifacts/scale-readiness-report.md)
- [architecture updates](phases/8-operate/artifacts/architecture-updates.md)
- [steady-state operating handoff](phases/8-operate/outcomes/steady-state-operating-handoff.md)
- [operating review meetings](phases/8-operate/artifacts/operating-review-meetings.md)

## [9. Iterate](phases/9-iterate/README.md)
Goal: close the loop — measure actual performance against the business case, decide iterate / pivot / double-down (or sunset when warranted), and feed validated learning back into the next-cycle [Discover](phases/1-discover/README.md).

- Kill / pivot / double-down decision produces [portfolio investment decision](phases/9-iterate/outcomes/portfolio-investment-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Commercial performance review produces [profitability assessment vs. business case](phases/9-iterate/artifacts/profitability-assessment-vs-business-case.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Benefits realization review produces [benefits-realization report](phases/9-iterate/artifacts/benefits-realization-report.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor), [Business Analyst](#3-business-analyst))*
- Roadmap refresh produces [updated roadmap](phases/9-iterate/artifacts/updated-roadmap.md) *([Product Owner](#2-product-owner), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Architecture roadmap refresh produces [updated architecture roadmap](phases/9-iterate/artifacts/updated-architecture-roadmap.md) *([Architect](#5-architect))*
- Technology refresh / modernization planning produces [modernization plan](phases/9-iterate/artifacts/modernization-plan.md) *([Architect](#5-architect))*
- Security posture review produces [security posture report](phases/9-iterate/artifacts/security-posture-report.md) *([Security & Compliance](#6-security-compliance))*
- Regulatory change monitoring produces [regulatory change impact](phases/9-iterate/artifacts/regulatory-change-impact.md) *([Security & Compliance](#6-security-compliance))*
- Lessons-learned facilitation produces [lessons-learned repository](phases/9-iterate/artifacts/lessons-learned-repository.md) *([Project Manager](#8-project-manager-delivery))*
- Project closure produces [closed project & archive](phases/9-iterate/artifacts/closed-project-archive.md) *([Project Manager](#8-project-manager-delivery))*
- Benefits realization coordination produces [scheduled benefits reviews](phases/9-iterate/artifacts/scheduled-benefits-reviews.md) *([Project Manager](#8-project-manager-delivery))*
- KPI / success-metric tracking produces [KPI performance report](phases/9-iterate/artifacts/kpi-performance-report.md) *([Product Owner](#2-product-owner), [Business Analyst](#3-business-analyst))*
- Feature adoption analysis produces [adoption metrics](phases/9-iterate/artifacts/adoption-metrics.md) *([Business Analyst](#3-business-analyst), [Product Owner](#2-product-owner))*
- A/B testing / experimentation produces [experiment results](phases/9-iterate/artifacts/experiment-results.md) *([Product Owner](#2-product-owner), [Developer](#9-developer))*
- Aggregate & analyze feedback produces [feedback insights report](phases/9-iterate/artifacts/feedback-insights-report.md) *([Business Analyst](#3-business-analyst), [Product Owner](#2-product-owner))*
- Continuous discovery produces [ongoing insights feed](phases/9-iterate/artifacts/ongoing-insights-feed.md) *([Business Analyst](#3-business-analyst), [UI/UX Designer](#4-uiux-designer))*
- Hand off insights to [Discover](phases/1-discover/README.md) produces [next-cycle opportunity backlog](phases/9-iterate/artifacts/next-cycle-opportunity-backlog.md) *([Product Owner](#2-product-owner), [Business Analyst](#3-business-analyst))*
- Prioritize bug fixes produces [prioritized bug list](phases/9-iterate/artifacts/prioritized-bug-list.md) *([Product Owner](#2-product-owner))*
- Technical debt backlog grooming produces [prioritized tech-debt list](phases/9-iterate/artifacts/prioritized-tech-debt-list.md) *([Architect](#5-architect), [Developer](#9-developer))*
- Sunset / deprecation produces [deprecation plan](phases/9-iterate/artifacts/deprecation-plan.md) *([Product Owner](#2-product-owner), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Bugfix application updates produces [patched application release](phases/9-iterate/artifacts/patched-application-release.md) *([Developer](#9-developer))*
- Document bugs with reproduction details produces [bug reports](phases/9-iterate/artifacts/bug-reports.md) *([QA/Tester](#10-qa-tester))*
- Document user feedback produces [user feedback log](phases/9-iterate/artifacts/user-feedback-log.md) *([Customer Support](#14-customer-support-success), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Customer success check-ins / NPS produces [NPS & health scores](phases/9-iterate/artifacts/nps-health-scores.md) *([Customer Support](#14-customer-support-success), [Sales & Marketing](#13-sales-marketing-product-marketing-sales-enablement))*
- Post-launch review / retrospective produces [retrospective report](phases/9-iterate/artifacts/retrospective-report.md) *([Project Manager](#8-project-manager-delivery), [Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*
- Benefits shortfall root-cause analysis produces [benefits-shortfall report](phases/9-iterate/artifacts/benefits-shortfall-report.md) *([Business Analyst](#3-business-analyst), [Architect](#5-architect))*
- Business-case reforecast produces [updated business case](phases/9-iterate/artifacts/updated-business-case.md) *([Business Analyst](#3-business-analyst))*
- Approve reforecast decision produces [reforecast decision](phases/9-iterate/outcomes/reforecast-decision.md) *([Product Sponsor](#1-product-sponsor-vp-product-cpo-gm-executive-sponsor))*

### Artifacts
- [Portfolio investment decision](phases/9-iterate/outcomes/portfolio-investment-decision.md)
- [profitability assessment vs. business case](phases/9-iterate/artifacts/profitability-assessment-vs-business-case.md)
- [benefits-realization report](phases/9-iterate/artifacts/benefits-realization-report.md)
- [updated roadmap](phases/9-iterate/artifacts/updated-roadmap.md)
- [updated architecture roadmap](phases/9-iterate/artifacts/updated-architecture-roadmap.md)
- [modernization plan](phases/9-iterate/artifacts/modernization-plan.md)
- [security posture report](phases/9-iterate/artifacts/security-posture-report.md)
- [regulatory change impact](phases/9-iterate/artifacts/regulatory-change-impact.md)
- [lessons-learned repository](phases/9-iterate/artifacts/lessons-learned-repository.md)
- [closed project & archive](phases/9-iterate/artifacts/closed-project-archive.md)
- [scheduled benefits reviews](phases/9-iterate/artifacts/scheduled-benefits-reviews.md)
- [KPI performance report](phases/9-iterate/artifacts/kpi-performance-report.md)
- [adoption metrics](phases/9-iterate/artifacts/adoption-metrics.md)
- [experiment results](phases/9-iterate/artifacts/experiment-results.md)
- [feedback insights report](phases/9-iterate/artifacts/feedback-insights-report.md)
- [ongoing insights feed](phases/9-iterate/artifacts/ongoing-insights-feed.md)
- [next-cycle opportunity backlog](phases/9-iterate/artifacts/next-cycle-opportunity-backlog.md)
- [prioritized bug list](phases/9-iterate/artifacts/prioritized-bug-list.md)
- [prioritized tech-debt list](phases/9-iterate/artifacts/prioritized-tech-debt-list.md)
- [deprecation plan](phases/9-iterate/artifacts/deprecation-plan.md)
- [patched application release](phases/9-iterate/artifacts/patched-application-release.md)
- [bug reports](phases/9-iterate/artifacts/bug-reports.md)
- [user feedback log](phases/9-iterate/artifacts/user-feedback-log.md)
- [NPS & health scores](phases/9-iterate/artifacts/nps-health-scores.md)
- [retrospective report](phases/9-iterate/artifacts/retrospective-report.md)
- [benefits-shortfall report](phases/9-iterate/artifacts/benefits-shortfall-report.md)
- [updated business case](phases/9-iterate/artifacts/updated-business-case.md)
- [reforecast decision](phases/9-iterate/outcomes/reforecast-decision.md)

---

## Swim Lane Order (top → bottom)

1. Product Sponsor
2. Product Owner
3. Business Analyst
4. UI/UX Designer
5. Architect
6. Security & Compliance
7. Site Reliability Engineer
8. Project Manager
9. Developer
10. QA/Tester
11. Release Manager
12. Technical Writer
13. Sales & Marketing
14. Customer Support

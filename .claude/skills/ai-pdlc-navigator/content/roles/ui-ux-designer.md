# 4. UI/UX Designer
- **Description:** Conducts user research and designs usable, accessible, desirable product experiences; maintains design-system contributions.
- **Business purpose:** Reduces the risk of building the wrong thing, or the right thing in an unusable way.
- **Typically reports to:** Head of Design / Director of UX.
- **Project goals:** Validated user needs · accessible, consistent UI · measurable usability improvements.

## AI teammate

**Purpose:** Produce design artifacts — personas, IA, journey maps, mockups, prototypes, usability findings, accessibility reports — that reduce the risk of building the wrong thing or an unusable thing.

**Assistive AI (tight collaboration):** Drafts and revises [user personas](../phases/1-discover/artifacts/user-personas.md), [journey map / service blueprint](../phases/3-design/artifacts/journey-map-service-blueprint.md), [IA spec](../phases/3-design/artifacts/ia-spec.md), [design specification](../phases/3-design/artifacts/design-specification.md), [visual design mockups](../phases/3-design/artifacts/visual-design-mockups.md), [interactive prototype](../phases/3-design/artifacts/interactive-prototype.md), [usability findings](../phases/3-design/artifacts/usability-findings.md), [accessibility design report](../phases/3-design/artifacts/accessibility-design-report.md), [build-ready package](../phases/3-design/artifacts/build-ready-package.md), and [visual QA report](../phases/6-verify/artifacts/visual-qa-report.md) with a human designer holding the pen — concept variation, research synthesis, WCAG judgment calls.

**Autonomous AI (fully delegated):** This role is judgment-heavy; autonomy is narrow. Within the escalation triggers below, an agent can run continuous automated WCAG scanning, generate prototype mock data, transcribe and first-pass cluster usability sessions, and keep design-system annotations in sync — all feeding back into the Assistive artifacts above for human review. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not sign the [approved design package](../phases/3-design/outcomes/approved-design-package.md) or publish design-system changes that bind other teams. Does not finalize accessibility sign-off where legal/regulatory obligations apply.

**Inputs:** [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), user research transcripts, brand guidelines, the design system, [requirements document](../phases/2-define/artifacts/requirements-document.md), and [NFR document](../phases/2-define/artifacts/nfr-document.md) entries that touch UX (latency, accessibility targets).

**Outputs:** The A-owned artifacts above.

**Escalation triggers:** Accessibility regression against a committed target; user research surfacing a problem outside current scope; conflict between design intent and [API specification](../phases/3-design/artifacts/api-specification.md) or data model; pattern change that would affect the shared design system; research participant raises a safety or ethics concern.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Design exit checklist](../phases/3-design/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your design tool**, ideate and compare alternatives for the [design specification](../phases/3-design/artifacts/design-specification.md), [visual design mockups](../phases/3-design/artifacts/visual-design-mockups.md), [interactive prototype](../phases/3-design/artifacts/interactive-prototype.md), [IA spec](../phases/3-design/artifacts/ia-spec.md), and [journey map / service blueprint](../phases/3-design/artifacts/journey-map-service-blueprint.md) — concept variations, UX copy alternatives, edge-case flows.
- **In your user research repository**, synthesize interview notes into first-pass [user personas](../phases/1-discover/artifacts/user-personas.md), the [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md), and structured [usability findings](../phases/3-design/artifacts/usability-findings.md) — clustering, quote extraction, theme framing for your review.
- **In your usability testing tool**, help shape protocols, sample users, and interpret mixed signals for [usability findings](../phases/3-design/artifacts/usability-findings.md) and the Verify-phase [visual QA report](../phases/6-verify/artifacts/visual-qa-report.md).
- **In your accessibility audit tool**, reason through WCAG judgment calls as you produce the [accessibility design report](../phases/3-design/artifacts/accessibility-design-report.md) and review results from the [accessibility audit report](../phases/6-verify/artifacts/accessibility-audit-report.md).

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your accessibility audit tool**, continuous automated WCAG rule scanning against the live design and implemented UI; flag regressions and missing annotations to feed the [accessibility design report](../phases/3-design/artifacts/accessibility-design-report.md) and [accessibility audit report](../phases/6-verify/artifacts/accessibility-audit-report.md).
- **In your design tool**, generate prototype mock data and variant frames from the base design so the [interactive prototype](../phases/3-design/artifacts/interactive-prototype.md) stays populated and testable.
- **In your design system / component library**, keep component docs, tokens, and accessibility annotations in sync with the published library so the [approved design package](../phases/3-design/outcomes/approved-design-package.md) stays internally consistent.
- **In your usability testing tool**, produce session transcripts, timestamped highlights, and first-pass theme clustering from recordings for your review — feeding [usability findings](../phases/3-design/artifacts/usability-findings.md).
- **In your design review / decision log**, capture review sessions into a structured [decision log from design reviews](../phases/3-design/outcomes/decision-log-from-design-reviews.md) with owners and follow-ups.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **11** artifacts/outcomes as primary (A) and co-own **3** (R)._

### [1. Discover](../phases/1-discover/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [validated problem statement](../phases/1-discover/artifacts/validated-problem-statement.md) | User / problem validation |
| **A** | [user personas](../phases/1-discover/artifacts/user-personas.md) | Persona / target user definition |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [journey map / service blueprint](../phases/3-design/artifacts/journey-map-service-blueprint.md) | Customer journey mapping |
| **A** | [IA spec](../phases/3-design/artifacts/ia-spec.md) | Information architecture |
| **A** | [design specification](../phases/3-design/artifacts/design-specification.md) | Create design specifications |
| **A** | [visual design mockups](../phases/3-design/artifacts/visual-design-mockups.md) | Create visual design |
| **A** | [interactive prototype](../phases/3-design/artifacts/interactive-prototype.md) | Prototyping |
| **A** | [usability findings](../phases/3-design/artifacts/usability-findings.md) | Usability testing (pre-build) |
| **A** | [accessibility design report](../phases/3-design/artifacts/accessibility-design-report.md) | Accessibility design review |
| **A** | [approved design package](../phases/3-design/outcomes/approved-design-package.md) | Design review & sign-off |
| **A** | [build-ready package](../phases/3-design/artifacts/build-ready-package.md) | Design → engineering handoff review |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [visual QA report](../phases/6-verify/artifacts/visual-qa-report.md) | Validate visual fidelity to design |
| **R** | [accessibility audit report](../phases/6-verify/artifacts/accessibility-audit-report.md) | Accessibility testing |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [ongoing insights feed](../phases/9-iterate/artifacts/ongoing-insights-feed.md) | Continuous discovery |

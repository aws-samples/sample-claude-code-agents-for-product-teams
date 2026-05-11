# 12. Technical Writer
- **Description:** Produces and maintains user guides, API reference, tutorials, UI copy, and changelogs; often owns the docs-as-code toolchain.
- **Business purpose:** Reduces time-to-value and deflects support load through discoverable, accurate documentation.
- **Typically reports to:** Head of Product, DevRel, or Engineering.
- **Project goals:** Docs ready at GA · lower support load on documented topics · healthy doc infra · cross-team contribution.


## AI teammate

**Purpose:** Produce and maintain discoverable, accurate documentation — user guides, API reference, tutorials, UI copy, release notes — that reduces time-to-value and deflects support load.

**Assistive AI (tight collaboration):** Drafts and iterates on the [feature documentation](../phases/7-launch/artifacts/feature-documentation.md), [user guides](../phases/7-launch/artifacts/user-guides.md), [customer-facing knowledge base](../phases/8-operate/artifacts/customer-facing-knowledge-base.md), [verified docs](../phases/6-verify/artifacts/verified-docs.md), and [release notes](../phases/7-launch/artifacts/release-notes.md) narrative with a human writer holding the pen — information architecture, voice calibration, quality passes before sign-off.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can keep the [generated API docs](../phases/5-build/artifacts/generated-api-docs.md) current from inline annotations, enforce style/lint against the style guide, scan for broken links and stale content, and flag undocumented public surface for your attention. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not approve customer-facing launch messaging — that belongs to PMM ([launch announcement](../phases/7-launch/artifacts/launch-announcement.md), [marketing collateral](../phases/7-launch/artifacts/marketing-collateral.md)) or Sponsor ([board/investor launch narrative](../phases/7-launch/artifacts/board-investor-launch-narrative.md)). Does not change product behavior or UI strings in code without developer review. Does not publish docs that describe unreleased features without explicit ship-date coordination.

**Inputs:** [API specification](../phases/3-design/artifacts/api-specification.md), [feature code](../phases/5-build/artifacts/feature-code.md), [release notes](../phases/7-launch/artifacts/release-notes.md), work-tracking/commit history, search analytics, support-deflection signals, and style-guide rules.

**Outputs:** The A artifacts above, lint/style reports, broken-link and stale-content reports, and content-gap candidates surfaced from search and support signals.

**Escalation triggers:**
- Undocumented public API surface or breaking change detected ahead of release.
- Security-sensitive or compliance-relevant documentation change (auth flows, data handling, retention).
- Customer-facing copy changes that affect pricing, legal terms, or commitments.
- Doc-site outage, broken-link spike, or sample-code drift above threshold.
- Conflicting information between PMM copy and engineering documentation.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Launch exit checklist](../phases/7-launch/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your docs-as-code platform**, draft and iterate on the [feature documentation](../phases/7-launch/artifacts/feature-documentation.md) and [user guides](../phases/7-launch/artifacts/user-guides.md): explain complex concepts, decide information architecture, calibrate voice to the audience.
- **In your published documentation site**, shape the structure and navigation of the [customer-facing knowledge base](../phases/8-operate/artifacts/customer-facing-knowledge-base.md) — information architecture choices, page-to-journey mapping, search-relevance tuning.
- **In your docs-as-code platform and engineering's source**, review UI microcopy and error messages against guidelines; critique tone before they ship.
- **In your changelog repository**, shape [release notes](../phases/7-launch/artifacts/release-notes.md) narrative — what the customer cares about vs. what engineering changed, migration guidance tone.
- **In your docs-as-code platform**, run a quality pass before [verified docs](../phases/6-verify/artifacts/verified-docs.md) sign-off — catch ambiguity, missing steps, outdated screenshots.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your API-reference generator**, keep the [generated API docs](../phases/5-build/artifacts/generated-api-docs.md) current from inline code annotations; flag undocumented public surface area for your attention.
- **In your changelog repository and work-tracking tool**, assemble first-draft [release notes](../phases/7-launch/artifacts/release-notes.md) and migration guides from commits and tickets for your editorial pass.
- **In your docs-as-code platform**, style/lint enforcement against the style guide; broken-link scanning; stale-content detection against source-control activity.
- **In your published documentation site**, monitor search queries and deflection signals; cluster unsolved queries into content-gap candidates for the [customer-facing knowledge base](../phases/8-operate/artifacts/customer-facing-knowledge-base.md).
- **In your docs-as-code platform**, keep code samples in documentation continuously tested against the live API; flag samples that drift.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **4** artifacts/outcomes as primary (A) and co-own **0** (R)._

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [verified docs](../phases/6-verify/artifacts/verified-docs.md) | Documentation review |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [feature documentation](../phases/7-launch/artifacts/feature-documentation.md) | Create feature documentation |
| **A** | [user guides](../phases/7-launch/artifacts/user-guides.md) | Draft user guides |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [customer-facing knowledge base](../phases/8-operate/artifacts/customer-facing-knowledge-base.md) | Curate documentation for customers |

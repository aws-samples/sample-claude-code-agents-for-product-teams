# accessibility design report

_Produced by: Accessibility design review_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** UI/UX Designer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required when the MVP is publicly accessible; otherwise address during Verify

## What this is

A review of the design against the committed accessibility standard (typically WCAG 2.1 or 2.2 at AA) — findings, required changes, and the accessibility posture for build. It is accessibility-by-design, before the expensive audit in Verify.

## Why it matters for the UI/UX Designer

You produce this because accessibility found late is accessibility that costs 10x to fix. Building the audit trail in Design also satisfies procurement and regulatory reviewers who increasingly ask for it pre-launch.

## Definition of Done

- [ ] Committed accessibility standard and conformance level are named up front.
- [ ] Every finding cites the specific WCAG success criterion it relates to.
- [ ] Assistive-technology walk-through results are captured, not just automated checks.
- [ ] Each required change has a named owner.
- [ ] Residual gaps include a mitigation plan and re-test date.

## What it contains

- Committed standard and conformance level
- Per-screen / per-component findings with WCAG success criteria referenced
- Color contrast and typography checks
- Keyboard and focus-order coverage
- Assistive-technology walk-through results (screen readers, voice)
- Motion and cognitive-load considerations
- Required changes and who owns each
- Known residual gaps and mitigation plan

## Inputs you rely on

- [Design specification](design-specification.md) and [visual design mockups](visual-design-mockups.md)
- [Usability findings](usability-findings.md) including assistive-tech sessions
- Org accessibility standard and legal obligations (ADA, EAA, Section 508)
- Design-system accessibility annotations

## Who consumes it

- Developer — implements to the annotations
- QA/Tester — designs accessibility tests for the Verify-phase [accessibility audit report](../../6-verify/artifacts/accessibility-audit-report.md)
- Product Owner — accepts residual-gap decisions
- Security & Compliance — includes accessibility obligations in regulatory scope

## Common pitfalls

- Running an automated check and calling the job done — automation catches ~30% of issues
- Testing with assistive tech only at launch when findings force re-design
- Listing findings without WCAG references, so engineers can't self-check
- Deferring residual gaps without a plan or re-test date

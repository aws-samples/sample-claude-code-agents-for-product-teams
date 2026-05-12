# visual QA report

_Produced by: Validate visual fidelity to design_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** UI/UX Designer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the MVP is utility, API, or internal-only

## What this is

The systematic comparison of the built product against the approved visual design — spacing, typography, color, motion, states, responsive behavior — flagging drift for remediation before launch. Not pixel-perfect dogma; an evidence-based fidelity check.

## Why it matters for the UI/UX Designer

Product quality is felt before it's understood. Small visual drifts compound into a product that looks cheaper than it is and undermines the brand, usability, and trust the design promised. This report is your leverage to get those fixes made while there's still time.

## Definition of Done

- [ ] Findings per screen/component include expected vs. actual, severity, and evidence
- [ ] States and breakpoints covered (loading, error, empty, responsive) are documented
- [ ] Design-system deviation notes (off-palette colors, off-token spacing) are captured
- [ ] Motion and interaction fidelity checks are recorded
- [ ] Localization/copy-length checks (where applicable) and a remediation list with owners are included

## What it contains

- Findings per screen/component: expected vs. actual, severity, evidence
- States and breakpoints covered (loading, error, empty, responsive)
- Design-system deviation notes (off-palette colors, off-token spacing)
- Motion and interaction fidelity check
- Localization and copy-length checks where applicable
- Remediation list with owners

## Inputs you rely on

- Visual design mockups and design specification
- Interactive prototype and design system tokens
- Implemented feature code in staging
- Accessibility audit report (often overlaps)
- Validated staging environment

## Who consumes it

- Developers — fix flagged items
- Release Manager — gates launch on resolution of blocking items
- Product Owner — accepts or defers non-blocking drift
- Future designers — learn where drift tends to happen

## Common pitfalls

- Pixel-perfect nitpicks drowning substantive usability drift
- Single-viewport testing missing responsive or state issues
- No severity rubric — everything is "medium"
- Findings logged with no photo/screenshot evidence, creating dispute cycles

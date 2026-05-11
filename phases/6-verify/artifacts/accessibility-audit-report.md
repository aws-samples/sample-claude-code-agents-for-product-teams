# accessibility audit report

_Produced by: Accessibility testing_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** QA/Tester

**Stakeholders:** UI/UX Designer

## What this is

The formal accessibility audit of the built product — WCAG (or equivalent) conformance, screen-reader flows, keyboard nav, contrast, motion, and assistive-tech compatibility — with findings, severity, and remediation state.

## Why it matters for the QA/Tester

A11y failures are both a product defect class and, in many markets, a legal exposure. Auditing in Verify — with designer collaboration — produces the evidence the Sponsor and legal need for launch risk decisions and gives the team time to fix what matters most.

## Definition of Done

- [ ] Audit scope and conformance target (e.g., WCAG 2.2 AA) are stated
- [ ] Every finding lists severity and the specific WCAG criterion
- [ ] Assistive-tech coverage names screen readers and devices tested
- [ ] Keyboard-only and zoom-path results are documented
- [ ] Remediation state and owner are recorded per finding, with residual gaps and accessibility-statement draft captured

## What it contains

- Audit scope and conformance target (e.g., WCAG 2.2 AA)
- Findings per page/flow with severity and WCAG criterion
- Assistive-tech coverage (which screen readers, devices)
- Keyboard-only and zoom-path results
- Remediation state and owner
- Residual gaps and accessibility statement draft

## Inputs you rely on

- Accessibility design report from Design
- Validated staging environment
- Design specification and visual design
- Implemented feature code
- Applicable regulations (ADA, EN 301 549, etc.)

## Who consumes it

- UI/UX Designer — fixes design-level defects
- Developers — fix code-level defects
- Release Manager — gates on severity-based exit criteria
- Legal/Compliance — confirms accessibility statement posture

## Common pitfalls

- Automated scan only — misses 50–70% of real issues
- One screen reader tested — doesn't generalize
- Severity rubric that treats "hard-blocked" and "awkward" the same
- Statement written without the audit evidence to back it

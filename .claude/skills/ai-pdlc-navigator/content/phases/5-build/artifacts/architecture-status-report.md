# architecture status report

_Produced by: Architecture status input_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

The Architect's periodic status input to the PM's status report — progress against the technical milestone plan, NFR posture, emerging technical risks, and architecture-level decisions needed. The engineering view the PM can't generate alone.

## Why it matters for the Architect

Delivery status that's feature-count-heavy and engineering-light hides the problems that actually sink initiatives — integration brittleness, NFR slippage, accumulating conformance drift. Your status input is how those concerns stay visible at the altitude where resourcing and scope decisions get made.

## Definition of Done

- [ ] Technical milestone progress is recorded with forecast dates
- [ ] NFR trajectory covers perf, scale, and availability with measured values
- [ ] Conformance posture names each material deviation from approved architecture
- [ ] Technical risks list mitigation state for each entry
- [ ] Every decision requested names the specific Sponsor, PO, or steering owner

## What it contains

- Technical milestone progress with forecast dates
- NFR trajectory (perf, scale, availability as measured in staging)
- Conformance posture and notable deviations from approved architecture
- Vendor/platform dependency health
- Technical risks with mitigation state
- Decisions requested from Sponsor, PO, or steering

## Inputs you rely on

- Technical milestone plan and integration map
- Conformance findings and updated ADRs
- Integration test results and performance trends
- Resolved technical blockers artifact
- Design guidance sessions

## Who consumes it

- Project Manager — rolls into weekly status report
- Product Sponsor — sees technical state in executive updates
- Architect peers and chief architect — portfolio technical view
- Steering or architecture review board — governance evidence

## Common pitfalls

- Technical happy-talk that mirrors the PM report's green without adding depth
- Omitting NFR posture because it hasn't been measured yet
- Decisions implied but not explicitly requested — action stalls
- Format so dense nobody reads past the first paragraph

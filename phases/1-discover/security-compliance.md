# Security & Compliance in Discover

You are here to make sure nobody funds an initiative that turns out to be illegal, uninsurable, or built on data the company can't hold. Discover isn't the time for deep control design — it's the time for two fast, directional reads: is this in scope for a regulated regime, and does it touch sensitive data? Loud early flags prevent expensive late pivots.

## What you do

- Initial regulatory landscape scan — publish the [regulatory risk flag](artifacts/regulatory-risk-flag.md)
- Data sensitivity early read — publish the [data-sensitivity flag](artifacts/data-sensitivity-flag.md)

## Artifacts you own

- [regulatory risk flag](artifacts/regulatory-risk-flag.md) — the regimes likely in scope (GDPR, HIPAA, PCI, SOX, sector-specific) with a confidence read
- [data-sensitivity flag](artifacts/data-sensitivity-flag.md) — whether the initiative will touch PII, PHI, regulated financial data, or secrets

## Outcomes you drive

You don't drive outcomes this phase — you input into the Sponsor's [Discover exit decision](outcomes/discover-exit-decision.md) by making sure regulatory and data risks are visible at the gate.

## Who you work with

- **Product Owner** — consumes your flags into the business case and feasibility memo
- **Architect** — your flags change their cost and NFR read materially
- **Product Sponsor** — needs your honest read on regulatory risk appetite
- **Business Analyst** — their market analysis may surface regulated segments you need to flag

## Handoff into Define

Your two flags become the triggers for real work in [Define](../2-define/README.md) — regulatory scope assessment, control requirements derivation, DPIA, and data classification confirmation. The quality bar is that nothing material surfaces in Define that you didn't flag in Discover. You're done when the Sponsor knows whether this initiative carries regulatory or data risk that changes the funding posture, and the Architect has enough signal to cost the controls correctly.

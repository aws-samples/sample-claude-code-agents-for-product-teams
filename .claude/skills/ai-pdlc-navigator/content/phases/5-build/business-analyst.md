# Business Analyst in Build

You are here to keep the traceability thread intact while the team codes, and to detect when the business case quietly stops being true. Build is when assumptions meet reality — your clarifications, impact analyses, and benefits tracking are the evidence the Sponsor and PO need to make good scope and reforecast decisions.

## What you do

- Clarify requirements in-flight as Developers and QA raise questions, keeping acceptance criteria unambiguous.
- Run scope-change impact analysis on every inbound ask so the Sponsor/PO decide with eyes open.
- Track benefits assumptions against emerging build reality — flag early when a KPI is quietly becoming unachievable.
- Keep the traceability matrix current so "what's built" still maps back to "why we built it."

## Artifacts you own

- [clarified requirements](artifacts/clarified-requirements.md) — mid-flight requirement resolutions.
- [change impact report](artifacts/change-impact-report.md) — scope-change analysis.
- [assumptions & benefits-tracking log](artifacts/assumptions-benefits-tracking-log.md) — how the case is holding up.

## Artifacts you contribute to

- [business-case reconfirmation or reset](outcomes/business-case-reconfirmation-or-reset.md) — Product Sponsor owns the decision; you provide the evidence.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'. Your evidence drives the Sponsor's reconfirm/reset call.

## Who you work with

- **Product Sponsor** — consumes your benefits tracking to re-validate the business case.
- **Product Owner** — consumes your clarifications and impact reports to accept increments and decide scope.
- **Developer / QA/Tester** — raise requirements questions that you resolve.
- **Architect** — pairs with you on change impact when a scope change has architectural implications.

## Handoff into [Verify](../6-verify/README.md)

In Verify you coordinate UAT with business users and produce the benefits-readiness assessment that tells the Sponsor whether the KPIs you promised are actually measurable at launch. You know Build is done when the traceability matrix is current, no requirements question is open, and the benefits log either confirms the plan or has triggered a formal reset.

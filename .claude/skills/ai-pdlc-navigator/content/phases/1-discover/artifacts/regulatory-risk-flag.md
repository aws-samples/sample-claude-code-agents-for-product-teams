# regulatory risk flag

_Produced by: Initial regulatory landscape scan_

**Business outcome supported:** frame the opportunity, validate the problem, understand the market, and exit with a funded, strategically-aligned bet.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

A first-pass scan of the regulatory and legal landscape the opportunity will touch — data protection, industry-specific rules, export controls, accessibility mandates, and anything else that could block or reshape the work. It is a flag, not a full assessment; the goal is to surface known unknowns early.

## Why it matters for the Security & Compliance owner

You produce this so the Sponsor does not fund an initiative that will collide with a regulator mid-Build. Flagging GDPR, HIPAA, PCI, SOX, or sector-specific regimes in Discover is cheap; discovering them in Verify is expensive and embarrassing.

## Definition of Done

- [ ] Jurisdictions the product will reach are listed.
- [ ] Applicable regimes each carry a confidence rating (definitely, likely, possible).
- [ ] Data categories and triggers (PII, PHI, financial, children's data) are named.
- [ ] Industry-specific rules and certifications are recorded where relevant.
- [ ] Open questions requiring Define-phase legal review are logged.

## What it contains

- Jurisdictions in scope (geographies the product will reach)
- Applicable regimes with initial confidence rating (definitely / likely / possible)
- Data categories and triggers (PII, PHI, financial, children's data)
- Industry-specific rules and certification requirements
- Known regulatory-change monitoring needs
- Open questions that need formal legal review in Define

## Inputs you rely on

- [Opportunity brief](opportunity-brief.md) and [market analysis report](market-analysis-report.md) for geography and segment
- [Data-sensitivity flag](data-sensitivity-flag.md) sibling scan
- Internal compliance register and prior initiatives in the same space
- Legal counsel for anything non-obvious

## Who consumes it

- Product Sponsor — factors regulatory risk into go / no-go / defer
- Architect — shapes early feasibility conclusions and NFR candidates
- Security & Compliance (future you) — promotes flags into the [applicable-regulations list](../../2-define/artifacts/applicable-regulations-list.md) in Define

## Common pitfalls

- Treating "we don't process PII" as settled without checking the actual data flow
- Missing sub-regimes (state privacy laws, sector-specific data rules)
- Ignoring regulatory-change velocity in high-velocity regimes
- Confident greens with no basis — flag ambers liberally and resolve in Define

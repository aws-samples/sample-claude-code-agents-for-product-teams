# data-sensitivity flag

_Produced by: Data sensitivity early read_

**Business outcome supported:** frame the opportunity, validate the problem, understand the market, and exit with a funded, strategically-aligned bet.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

An early, coarse read on the sensitivity of data the product will collect, process, store, or share. It flags the "this touches PHI" or "this handles payment data" reality before Architecture picks a stack that cannot support it.

## Why it matters for the Security & Compliance owner

You produce this because data classification drives almost everything downstream — architecture, residency, retention, encryption, access, logging, and vendor choice. Missing a sensitivity tier in Discover silently constrains every subsequent decision in the wrong direction.

## Definition of Done

- [ ] Expected data categories are enumerated (e.g., PII, PHI, PCI, credentials).
- [ ] Data subjects and their jurisdictions are named.
- [ ] Sources and sinks across the product boundary are listed.
- [ ] A preliminary classification tier is assigned against the org's scheme.
- [ ] At least one red-line category is stated.

## What it contains

- Expected data categories (PII, PHI, PCI, financial, credentials, trade secrets)
- Data subjects and their jurisdictions
- Expected volume and velocity signals if known
- Sources and sinks (where data enters and exits the product boundary)
- Preliminary classification tier against the org's scheme
- Red lines (data categories the org has decided not to handle)

## Inputs you rely on

- [Opportunity brief](opportunity-brief.md) and draft user journeys
- [Regulatory risk flag](regulatory-risk-flag.md) for jurisdictional triggers
- Org data classification policy and tiering scheme
- Architect's early system-context sketch

## Who consumes it

- Architect — uses it to rule candidate stacks and deployment models in or out
- Product Sponsor — sees the true regulatory gravity of the initiative
- Security & Compliance (future you) — promotes this into [data inventory & classification](../../2-define/artifacts/data-inventory-classification.md) and the [privacy impact assessment](../../2-define/artifacts/privacy-impact-assessment.md) in Define

## Common pitfalls

- Assuming anonymized data is out-of-scope — re-identification risk is often underestimated
- Missing secondary data (logs, telemetry, support tickets) that may contain sensitive fields
- Inheriting stale classifications from a similar product without re-checking
- No red-line decisions, so the initiative drifts into regulated territory by accident

# system-to-process map

_Produced by: System context overlay on processes_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

The overlay that shows which systems (current and planned) enact which steps of the business processes — and where the product under development fits in. It is the bridge from BA-owned process models to Architect-owned integration design.

## Why it matters for the Architect

You produce this because processes and systems are modeled separately for good reasons but must reconcile to build anything real. The overlay exposes which process steps have no system support, which have too many, and which integration seams the product will have to cross.

## Definition of Done

- [ ] Every process step is mapped to the system(s) that enact it
- [ ] Data entering and leaving each system at each step is shown
- [ ] Each step is classified manual or automated
- [ ] System ownership (our org / partner / vendor) and SLA reality are captured
- [ ] Systems are labelled in-scope for change versus out-of-scope

## What it contains

- Each process step mapped to the system(s) that enact it
- Data entering and leaving each system at each step
- Manual / automated classification per step
- System ownership (our org, partner, vendor) and SLA reality
- Integration gaps and candidate integration approaches
- Systems in scope for change vs. out of scope

## Inputs you rely on

- [Process models](process-models.md) as-is and to-be
- Enterprise application catalog and existing integration map
- [Capability gap report](capability-gap-report.md) and [dependency list](dependency-list.md)
- [Data inventory & classification](data-inventory-classification.md)

## Who consumes it

- Architect (future you) — evolves this into the Design-phase [integration map](../../3-design/artifacts/integration-map.md)
- Business Analyst — validates that to-be processes are actually enactable
- Security & Compliance — identifies systems-of-record for compliance data
- Developer — uses it to scope integration work early

## Common pitfalls

- Drawing the systems as boxes with no data flows — hides the actual work
- Missing shadow systems (spreadsheets, scripts, manual workflows)
- Treating partner / vendor systems as opaque when their SLAs determine product NFRs
- Not versioning alongside process model changes, so the two drift

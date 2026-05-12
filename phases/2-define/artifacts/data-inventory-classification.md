# data inventory & classification

_Produced by: Data requirements & classification_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Business Analyst

**Stakeholders:** Architect

**Accelerated MVP:** slim — list the personal/sensitive data the MVP touches; full inventory comes with scale

## What this is

The catalogue of every data element the product will create, ingest, process, store, or share, each mapped to a classification tier and a lawful basis. This is the authoritative data register the architecture, security, and privacy work will anchor to.

## Why it matters for the Business Analyst

You own this — with Architect — because data is where legal risk lives, and classification silently drives NFRs (encryption, residency, retention, access). An incomplete inventory at Define turns into unplanned work in Design and a compliance finding in Verify.

## Definition of Done

- [ ] Each data element has a name, source, purpose, and named owner
- [ ] Every element carries a classification tier per org policy
- [ ] Personal-data flags (PII / PHI / PCI / children's data / biometrics) are set where applicable
- [ ] Lawful basis and retention period are stated per element
- [ ] Residency and cross-border transfer constraints are captured

## What it contains

- Data element name, source, purpose, and owner
- Classification tier (public / internal / confidential / restricted, per org policy)
- Personal-data flags (PII, PHI, PCI, children's data, biometrics)
- Lawful basis / purpose limitation and retention period
- Residency and cross-border transfer constraints
- Upstream and downstream systems (producers and consumers)
- Sensitivity rationale and open questions

## Inputs you rely on

- [Data-sensitivity flag](../../1-discover/artifacts/data-sensitivity-flag.md) from Discover
- [Regulatory risk flag](../../1-discover/artifacts/regulatory-risk-flag.md) and [applicable-regulations list](applicable-regulations-list.md)
- [Process models](process-models.md) and [system-to-process map](system-to-process-map.md)
- Org data classification policy and existing data catalog

## Who consumes it

- Architect — drives [data model](../../3-design/artifacts/data-model.md) and residency decisions
- Security & Compliance — drives [privacy impact assessment](privacy-impact-assessment.md) and [security control requirements](security-control-requirements.md)
- Developer — uses it to honor classification-aware logging, masking, and retention

## Common pitfalls

- Missing secondary data (logs, traces, analytics events) that contain personal fields
- Classifying by system rather than by element — one system, many tiers
- Copy-paste retention periods that do not match actual regulatory obligations
- No owner per element — when it drifts, nobody notices

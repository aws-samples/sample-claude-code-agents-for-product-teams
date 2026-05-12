# data model

_Produced by: Data model / schema design_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — the schemas the MVP actually creates and reads; formalize as scale grows

## What this is

The logical and physical data model — entities, attributes, relationships, keys, cardinality, constraints, retention, and the choice of store(s). It is the structural contract behind the product's behavior, and the thing that is most expensive to change after Build.

## Why it matters for the Architect

You own this because data model decisions have the longest half-life of any design choice. Fix a service boundary in a sprint; fix a data model and you are migrating for quarters. Getting ownership, residency, and privacy right here is non-negotiable.

## Definition of Done

- [ ] Every entity has keys, cardinality, and constraints defined.
- [ ] PII/PHI classification markers are set at the attribute level.
- [ ] Each entity has a named system-of-record and ownership.
- [ ] Retention, archival, and purge policy is documented per entity.
- [ ] Schema-evolution approach (migrations, versioning) is described.

## What it contains

- Entity and relationship model with cardinality and keys
- Attribute-level definitions with types and constraints
- Classification tier and PII/PHI markers at attribute level
- Persistence choice per entity with rationale
- Ownership and system-of-record designation
- Retention, archival, and purge policy per entity
- Indexing, partitioning, and residency posture
- Change-management approach (schema evolution, migrations)

## Inputs you rely on

- [Data inventory & classification](../../2-define/artifacts/data-inventory-classification.md) and [privacy impact assessment](../../2-define/artifacts/privacy-impact-assessment.md)
- [Requirements document](../../2-define/artifacts/requirements-document.md) and [process models](../../2-define/artifacts/process-models.md)
- [NFR document](../../2-define/artifacts/nfr-document.md) — especially scale, latency, residency
- Existing enterprise data standards and master-data decisions

## Who consumes it

- Developer — implements schemas, migrations, and access patterns
- Security & Compliance — validates classification-aware storage and access
- Architect (future you) — updates through Build in ADRs
- SRE — sizes storage, backup, and DR from it

## Common pitfalls

- Physical-first modeling that locks in a specific store before requirements stabilize
- Missing retention and purge per entity — a privacy landmine
- No system-of-record designation, so multiple copies drift
- Schema-evolution strategy deferred until the first breaking migration

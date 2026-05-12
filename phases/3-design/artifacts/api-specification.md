# API specification

_Produced by: API / interface contract design_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Architect

**Stakeholders:** Developer

**Accelerated MVP:** slim — OpenAPI or equivalent for the MVP's endpoints; full registry later

## What this is

The formal contract for every API the product exposes — endpoints, operations, request/response shapes, error model, auth, versioning, and non-functional commitments. Typically an OpenAPI or AsyncAPI spec plus the narrative that humans read.

## Why it matters for the Architect

You co-own this with Developer because API contracts are the public surface the product is judged by. A well-specified API buys forward compatibility, third-party trust, and clean test generation; a loose one makes the product its own integration problem.

## Definition of Done

- [ ] Spec is captured in a machine-readable source (OpenAPI / AsyncAPI), not narrative only.
- [ ] Every operation has request, response, and error-envelope schemas defined.
- [ ] Auth, tenancy, rate-limit, idempotency, and pagination rules are explicit.
- [ ] Versioning and deprecation policy is stated, not deferred.
- [ ] Every operation has at least one happy-path and one unhappy-path example that round-trips through the schema.

## What it contains

- Resource / operation catalog with semantics
- Request/response schemas, including error envelopes
- Authentication, authorization, and tenancy model
- Rate limits, idempotency, and pagination
- Versioning and deprecation policy
- SLOs for latency, availability, and throughput
- Examples for every operation, happy and unhappy
- Compliance / PII handling notes per field

## Inputs you rely on

- [Data model](data-model.md) and [integration map](integration-map.md)
- [NFR document](../../2-define/artifacts/nfr-document.md) and [security control requirements](../../2-define/artifacts/security-control-requirements.md)
- Platform API standards and reference specs
- Prospective consumer requirements (internal and partner)

## Who consumes it

- Developer — codes to it and mocks it for client work
- QA/Tester — generates contract and integration tests
- Security & Compliance — assesses via [threat model](threat-model.md)
- Technical Writer (later phases) — derives [generated API docs](../../5-build/artifacts/generated-api-docs.md) from it

## Common pitfalls

- Narrative-only spec with no machine-readable source of truth
- Undefined error model, so every client codes defensively in a different way
- Versioning policy deferred — the first breaking change becomes political
- Examples that don't round-trip through the schema

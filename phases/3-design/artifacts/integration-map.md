# integration map

_Produced by: Integration / system context map_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — a sketch of the systems the MVP talks to is enough

## What this is

The detailed view of integrations in and out of the product — protocols, data, directionality, ownership, SLAs, and failure modes. It is the Design-era evolution of the [system-to-process map](../../2-define/artifacts/system-to-process-map.md) with enough specificity to build against.

## Why it matters for the Architect

You own this because integrations are where products most often break in production. Making every edge explicit — including partner SLA reality and failure-mode ownership — prevents the launch-week discovery that an upstream system returns 500s for valid requests.

## Definition of Done

- [ ] Every integration lists endpoint, protocol, payload, and directionality.
- [ ] Each edge names an owning team and escalation contact on both sides.
- [ ] SLA (contractual, not marketed) is recorded per integration.
- [ ] Auth, rate-limit, and idempotency posture are stated per edge.
- [ ] Failure modes and fallback / degradation strategy are documented per integration.

## What it contains

- Each integration with endpoint, protocol, payload shape, and directionality
- Owning team on each side and escalation contact
- SLA (real, not marketed) and error-budget impact
- Auth, rate-limit, and idempotency posture
- Failure modes and fallback / degradation strategy
- Data classification flowing across each edge
- Change / deprecation schedule of upstream dependencies

## Inputs you rely on

- [System-to-process map](../../2-define/artifacts/system-to-process-map.md) and [dependency list](../../2-define/artifacts/dependency-list.md)
- [Data inventory & classification](../../2-define/artifacts/data-inventory-classification.md)
- Counter-parties' API contracts and SLA commitments
- Platform / API gateway standards

## Who consumes it

- Developer — builds to it and handles the failure modes
- SRE — factors SLAs into overall service SLO math
- Security & Compliance — uses it for [threat model](threat-model.md) trust boundaries
- QA/Tester — designs integration and resilience tests from it

## Common pitfalls

- Listing APIs without SLAs or with marketed SLAs that contracts don't back
- Ignoring the out-bound integrations (telemetry, logs, analytics) that carry sensitive data
- No failure-mode ownership, so production incidents become finger-pointing
- Static map — dependencies evolve and the map becomes misleading

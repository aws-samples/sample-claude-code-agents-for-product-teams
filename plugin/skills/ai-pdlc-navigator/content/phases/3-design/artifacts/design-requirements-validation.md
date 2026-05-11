# design-requirements validation

_Produced by: Validate design against requirements_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Business Analyst

**Stakeholders:** Security & Compliance

## What this is

A cross-check that every committed requirement (functional, non-functional, regulatory) is actually addressed by the design — and that the design has not quietly added scope that isn't in requirements. It is the reconciliation step before build commitment.

## Why it matters for the Business Analyst

You own this because Design is where scope silently shifts — a new screen for an unplanned job, a dropped requirement "we'll add later." Catching drift here is cheap; catching it in Build or Verify means expensive rework or a broken business case.

## Definition of Done

- [ ] Every committed requirement has a coverage status in the design.
- [ ] Every NFR is traced to the architecture or design artifact that delivers it.
- [ ] Every regulatory control has a coverage status recorded.
- [ ] Added scope (design beyond requirements) has rationale or a remove-it decision.
- [ ] Removed scope (requirement not covered) has an explicit disposition.

## What it contains

- Per-requirement coverage status in the design
- Per-NFR coverage location in architecture / design artifacts
- Per-regulatory-control coverage status
- Added scope (design introduces behavior not in requirements) with rationale or remove-it decision
- Removed scope (requirement not covered) with disposition
- Open issues to resolve before build commitment

## Inputs you rely on

- [Requirements document](../../2-define/artifacts/requirements-document.md) and [NFR document](../../2-define/artifacts/nfr-document.md)
- [Applicable-regulations list](../../2-define/artifacts/applicable-regulations-list.md) and [security control requirements](../../2-define/artifacts/security-control-requirements.md)
- [Architecture document](architecture-document.md), [design specification](design-specification.md), [API specification](api-specification.md)
- [Threat model](threat-model.md) for security-coverage check

## Who consumes it

- Product Owner — signs off on scope at the approved design package
- Business Analyst (future you) — updates the [updated traceability matrix](updated-traceability-matrix.md)
- Security & Compliance — confirms all controls covered before approval
- Project Manager — turns unresolved issues into pre-build commitments

## Common pitfalls

- Superficial tick-box review without opening each artifact
- Missing NFRs — they are often buried in design and hard to locate
- No disposition for removed scope, so it floats unowned
- Running the check once; design drifts through the rest of Design without re-check

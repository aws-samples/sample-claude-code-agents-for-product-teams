# traceability matrix

_Produced by: Requirements traceability matrix_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the squad keeps traceability in the backlog tool itself

## What this is

A table linking each requirement to its sources (persona, business rule, regulation), its design artifacts, its tests, and — in later phases — its release and benefits. Rows are requirement IDs; columns trace upstream and downstream relationships.

## Why it matters for the Business Analyst

You own this because it is the single artifact that answers "why are we building this?" and "where is the evidence it works?" at audit time. Without traceability, change impact is guesswork and regulatory evidence is a scramble; with it, both become table lookups.

## Definition of Done

- [ ] Matrix includes columns for source, requirement ID, NFR links, design artifact, acceptance criteria, test case, release, and benefit
- [ ] Every requirement ID appears as a row with upstream source populated
- [ ] Links are navigable in both directions (requirement to test and test to requirement)
- [ ] Compliance-critical rows are flagged for coverage
- [ ] An exceptions register captures deferred, rejected, or out-of-scope requirements with rationale

## What it contains

- Columns for: source (persona / rule / regulation), requirement ID, NFR links, design artifact, acceptance criteria, test case, release, and benefit
- Bidirectional navigability (requirement → test and test → requirement)
- Coverage flags for compliance-critical items
- Last-updated stamp and owner per row
- Exceptions register (requirements deferred, rejected, or out of scope with rationale)

## Inputs you rely on

- [Requirements document](requirements-document.md) and [testable acceptance criteria](testable-acceptance-criteria.md)
- [NFR document](nfr-document.md) and [applicable-regulations list](applicable-regulations-list.md)
- [Test-to-requirement coverage map](test-to-requirement-coverage-map.md) and [control-to-test coverage map](control-to-test-coverage-map.md)

## Who consumes it

- Security & Compliance — uses it for audit evidence and PIA support
- Architect — uses it to validate design covers every committed requirement; feeds the [updated traceability matrix](../../3-design/artifacts/updated-traceability-matrix.md) in Design
- Project Manager — uses it during change impact coordination in Build
- QA/Tester — uses it to justify regression scope

## Common pitfalls

- Maintained manually in a spreadsheet and going stale within a sprint
- Missing one-to-many relationships — one requirement often has several tests and rules
- No link to benefit — requirements trace up to source but not down to outcome
- Treating it as a Define-only artifact instead of a living register

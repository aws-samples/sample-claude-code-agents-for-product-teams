# architecture updates

_Produced by: Evolve architecture from production learnings_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

Concrete architectural changes introduced as a result of production learning — refined patterns, replaced components, new ADRs, updated NFR targets. Not a greenfield redesign; targeted evolutions to the system of record.

## Why it matters for the Architect

The design that made sense in Design almost never survives contact with production unchanged. Continuous architectural evolution — captured in ADRs and reflected in the living architecture document — prevents the system from silently becoming unmaintainable.

## Definition of Done

- [ ] Every architectural change lands as a new or superseding ADR.
- [ ] Architecture document sections are updated to reflect the changes.
- [ ] Revised NFR targets are stated with measurable thresholds.
- [ ] Deprecated patterns have a migration plan with sequencing.
- [ ] Each change cross-references the RCA, incident, or report that prompted it.

## What it contains

- New or superseded ADRs
- Updated architecture document sections
- Revised NFR targets
- Pattern changes and deprecations
- Migration plans where components are replaced
- Cross-reference to RCAs that prompted the change

## Inputs you rely on

- Architectural health report
- RCAs and incident postmortems
- Scale-readiness report
- Cost & capacity report
- Conformance findings

## Who consumes it

- Developer — new guardrails and patterns to follow
- SRE — updated operating expectations
- Iterate phase — feeds updated architecture roadmap and modernization plan
- Future engineers — onboarding context

## Common pitfalls

- Informal decisions that never make it into ADRs
- ADRs written but not reflected in the architecture document
- No migration path for deprecated patterns — old and new coexist indefinitely
- Updates chosen by taste instead of grounded in production data

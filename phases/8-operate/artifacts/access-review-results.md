# access review results

_Produced by: Access reviews_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — quarterly access review is enough

## What this is

The periodic (usually quarterly) review of who has access to what — production systems, data stores, admin consoles, privileged roles — with manager sign-off on continued need and removal of stale access.

## Why it matters for the Security & Compliance team

Excess access is the single largest internal risk surface. A disciplined review program is an auditor favorite, a breach-blast-radius shrinker, and the process that catches orphaned accounts and role creep before they appear in an incident postmortem.

## Definition of Done

- [ ] Every in-scope system lists current access roster and review frequency.
- [ ] Each account has a manager attestation recorded as kept, modified, or revoked.
- [ ] Orphaned or anomalous access findings are identified with disposition.
- [ ] Privileged access usage is summarised for the review period.
- [ ] Completion rate and any exceptions (with rationale) are captured.

## What it contains

- Systems in scope and review frequency
- Current access rosters per system
- Manager attestations (kept, modified, revoked)
- Orphaned or anomalous access found
- Privileged access usage summary
- Completion rate and exception handling

## Inputs you rely on

- Identity provider and access management system exports
- HR roster (joiners, movers, leavers)
- Applicable-regulations list (SOX, SOC 2, HIPAA drive scope)
- Threat model (which privileges matter most)
- Previous review results

## Who consumes it

- Security & Compliance — feeds audit evidence
- System owners — remove stale access
- Audit and legal — evidence of least-privilege operation
- Incident response — lookup during investigations

## Common pitfalls

- Rubber-stamp attestations that don't actually review access
- Scope excludes shadow systems where real risk sits
- Revocations decided but never executed
- No closure loop — orphaned accounts flagged again next quarter

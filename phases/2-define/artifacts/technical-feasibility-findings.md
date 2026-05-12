# technical feasibility findings

_Produced by: Requirements technical feasibility review_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — name the riskiest assumption and how the MVP tests it

## What this is

The Architect's deeper read on whether each requirement and NFR can be met with the available platform, patterns, and time budget. It promotes ambers from the Discover [feasibility memo](../../1-discover/artifacts/feasibility-memo.md) into explicit findings, and surfaces new ones discovered in Define.

## Why it matters for the Architect

You produce this to give the team and Sponsor a clear-eyed view of what is and is not achievable with current constraints, before design lock-in. Unflagged feasibility issues become Build-phase surprises that blow schedules.

## Definition of Done

- [ ] Each requirement or NFR carries a feasibility rating with rationale
- [ ] Findings name the specific platform, integration, or data constraints that drive them
- [ ] Spike results or prototypes are cited for items that were de-risked
- [ ] Where a requirement is infeasible as written, a recommended edit is proposed
- [ ] Remaining amber or red risks list their mitigation posture

## What it contains

- Per-requirement or per-NFR feasibility rating with rationale
- Platform, integration, and data constraints that bite
- Spike results or prototypes that de-risked specific items
- Open questions that require Design-phase investigation
- Recommended requirement edits where something is infeasible as written
- Risks that remain amber or red and the mitigation posture

## Inputs you rely on

- [Requirements document](requirements-document.md) and [NFR document](nfr-document.md)
- [System-to-process map](system-to-process-map.md) and current architecture
- [Capability gap report](capability-gap-report.md)
- Platform team input on capacity, roadmap, and known constraints

## Who consumes it

- Business Analyst — edits requirements and acceptance criteria where needed
- Project Manager — updates risk register and sequence
- Product Owner — sees which scope items carry real delivery risk
- Architect (future you) — carries open questions into [technical options assessment](../../3-design/artifacts/technical-options-assessment.md)

## Common pitfalls

- Optimism bias — rating things "feasible" without a spike
- Reviewing requirements in isolation from NFRs, missing the compound infeasibility
- No link back to the requirement ID, so findings cannot be traced
- Stopping at "it's hard" instead of proposing alternatives

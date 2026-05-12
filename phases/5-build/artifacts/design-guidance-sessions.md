# design guidance sessions

_Produced by: Technical design guidance & pairing_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — recorded decisions in ADRs or the work item

## What this is

The record of working sessions where the Architect engages directly with developers on implementation-level design — pairing, whiteboarding, pattern selection, reviewing non-trivial changes before they're written. Lightweight notes, not formal documents.

## Why it matters for the Architect

The approved architecture is a starting point; dozens of local design decisions shape whether it actually gets built. Investing time in guidance keeps the team on pattern, unblocks hard calls fast, and prevents drift that's expensive to correct later.

## Definition of Done

- [ ] Each session records topic, participants, decision, and rationale
- [ ] Sketches, prototypes, or RFC drafts produced are linked
- [ ] Follow-up items list ADR updates, enabler items, or pattern write-ups needed
- [ ] Open questions parked for broader discussion are captured
- [ ] Related work items affected are cross-linked

## What it contains

- Session notes: topic, participants, decision, rationale
- Links to sketches, prototypes, or RFC drafts produced
- Follow-up items (ADR updates, enabler items, pattern write-ups)
- Open questions parked for broader discussion
- Related work items impacted
- Trends across sessions that indicate systemic pain

## Inputs you rely on

- Architecture document and ADRs
- Feature code in progress and recent PRs
- Technical impact analyses
- Developer questions and impediment log
- Enabler backlog

## Who consumes it

- Developers in the session — implement to the agreed direction
- Broader team — learns patterns through notes and follow-up ADRs
- Architect — spots systemic patterns that need ADRs or training
- Architect peers — reuse decisions across teams

## Common pitfalls

- Verbal decisions never written down — repeated debates across teams
- Guidance dominated by senior voices, no capture of junior questions
- No follow-through — ADRs and pattern docs promised but never produced
- Sessions scheduled late after code is already written in a different direction

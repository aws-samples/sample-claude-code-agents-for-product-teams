# enabler backlog

_Produced by: Architecture runway / technical enablers_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Architect

**Stakeholders:** Developer

## What this is

The backlog of technical work that has no direct user-facing value but must exist before feature work can land cleanly — auth scaffolding, shared libraries, schema migrations, platform upgrades, observability plumbing, security primitives. It's architecture runway, tracked like stories.

## Why it matters for the Architect

Feature backlogs starve architectural investment unless you explicitly budget for it; the result is a stack that ships fast for three iterations and grinds to a halt by month four. This artifact gives the runway a name, an owner, and a place in iteration planning so the Product Owner can trade it against features with eyes open.

## Definition of Done

- [ ] Each enabler has a problem statement and target capability
- [ ] Acceptance criteria are stated (via developer-velocity or NFR signals where applicable)
- [ ] Dependencies on vendors, platform teams, or other enablers are listed
- [ ] Each enabler carries an engineering size estimate
- [ ] Sequencing rationale names the feature work each enabler unblocks
- [ ] Risk flags mark enablers with compounding cost if deferred

## What it contains

- Enabler items with clear problem statement and target capability
- Acceptance criteria (often observable through developer velocity or NFR metrics, not UI)
- Dependencies on vendor work, platform teams, or other enablers
- Sizing from engineering
- Sequencing rationale — which feature work each enabler unblocks
- Risk flags where deferring an enabler has compounding cost

## Inputs you rely on

- Approved architecture document and ADRs
- Integration map and data model
- NFR document — many enablers exist to meet NFRs
- Current technical state / debt inventory
- Developer input on friction and slow-downs

## Who consumes it

- Product Owner — interleaves enablers with feature stories in the prioritized backlog
- Developers — implement the enablers
- SRE — takes platform-side enablers into their own queue
- Project Manager — reflects runway work in schedule and capacity

## Common pitfalls

- Framing enablers as "tech tasks" with no value story — PO deprioritizes them
- Omitting enablers that span teams (assume "someone else will do it")
- Batching enablers into a single "platform sprint" that gets cut when schedule slips
- Letting the list grow unbounded without pruning items that became moot

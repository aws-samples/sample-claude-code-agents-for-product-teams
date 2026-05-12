# technical milestone plan

_Produced by: Technical milestone sequencing_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — the MVP milestones are the iterations themselves

## What this is

A sequenced view of the technical milestones that have to land — in order — for the architecture to come together: platform foundations, integration points, data pipeline cutover, security controls, scale rehearsals. It's the engineering "build order" behind the PM's schedule.

## Why it matters for the Architect

You're accountable for the solution coming together on a path that respects NFRs and hard dependencies. Without a Architect-blessed sequence, iteration planning will optimize for user-visible stories and starve the runway — leading to rework, NFR misses, or late-breaking integration surprises.

## Definition of Done

- [ ] Milestones are ordered with clear technical acceptance criteria
- [ ] Dependencies between milestones show what blocks what
- [ ] Integration/handshake dates with external teams or vendors are captured
- [ ] Infrastructure-readiness gates (environments, networking, data) are listed
- [ ] NFR verification milestones (perf baseline, load, failover drill) are included
- [ ] Risk-reduction spikes are timed before commitments lock

## What it contains

- Ordered milestones with clear technical acceptance criteria
- Dependencies between milestones (what blocks what)
- Integration/handshake dates with external teams or vendors
- Infrastructure-readiness gates (environments, networking, data)
- NFR verification milestones (perf baseline, load, failover drill)
- Risk-reduction spikes timed before commitments lock

## Inputs you rely on

- Approved architecture document and integration map
- Dependency list and vendor commitments
- Enabler backlog (many milestones are enablers)
- Estimation from engineering on component-level effort
- External team roadmaps where handshakes exist

## Who consumes it

- Project Manager — lays it into the iteration plan and critical path
- Developer leads — use it to plan technical work per iteration
- SRE — aligns environment provisioning and pipeline readiness to the sequence
- Product Sponsor — sees it as the spine of the baselined schedule

## Common pitfalls

- Writing milestones as outputs ("component X built") instead of verifiable capabilities ("end-to-end happy path in staging with traces")
- Burying integration dates in prose so external partners miss them
- Omitting NFR verification until late — perf/load surprises force replan
- No slack around vendor- or platform-dependent milestones

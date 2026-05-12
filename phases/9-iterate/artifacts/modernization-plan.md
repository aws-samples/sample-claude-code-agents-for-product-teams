# modernization plan

_Produced by: Technology refresh / modernization planning_

**Business outcome supported:** close the loop — measure actual performance against the business case, decide continue/pivot/sunset, and feed validated learning back into Discover for the next cycle.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the MVP is new code in a new space

## What this is

The specific plan to migrate off end-of-life dependencies, replace underperforming components, and move to newer platforms or patterns where the ROI justifies the effort. The tactical counterpart to the architecture roadmap.

## Why it matters for the Architect

Languages, frameworks, cloud services, and vendor products have finite life. A disciplined modernization plan turns "we'll deal with it later" into funded, sequenced work; without one, the team is eventually blocked by deprecation schedules and hiring difficulty on stale tech.

## Definition of Done

- [ ] Items nearing end-of-life or support sunset are listed
- [ ] Replacement target and migration approach are specified for each
- [ ] Sequencing and dependencies across items are documented
- [ ] Cost, risk, and business impact per item are quantified
- [ ] Success criteria and cutover plan are defined

## What it contains

- Items nearing end-of-life or support sunset
- Replacement target and migration approach
- Sequencing and dependencies
- Cost, risk, and business impact per item
- Required product-roadmap accommodation
- Success criteria and cutover plan

## Inputs you rely on

- Updated architecture roadmap
- Scale-readiness and architectural health reports
- Vendor lifecycle announcements
- Patched dependencies and SBOM
- Cost & capacity report

## Who consumes it

- Sponsor — funds the work
- Developer — executes migrations
- SRE — validates operational impact of cutovers
- Iterate and next Discover cycles — slots modernization into the roadmap

## Common pitfalls

- "Big bang" rewrites with no incremental business value
- No cutover plan — old and new coexist indefinitely, adding ops cost
- Modernization chosen by tech taste, not customer or cost impact
- Missing dependency on product roadmap; features freeze or clash

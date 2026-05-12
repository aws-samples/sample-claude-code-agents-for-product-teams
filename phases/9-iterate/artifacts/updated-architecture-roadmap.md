# updated architecture roadmap

_Produced by: Architecture roadmap refresh_

**Business outcome supported:** close the loop — measure actual performance against the business case, decide continue/pivot/sunset, and feed validated learning back into Discover for the next cycle.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — ADRs covering the next moves are enough

## What this is

The forward-looking architectural plan, refreshed from production learnings and the updated product roadmap. What needs to evolve, consolidate, or retire over the next cycles to keep the system fit-for-enterprise on cost, scale, evolvability, and compliance.

## Why it matters for the Architect

A product roadmap without an architecture roadmap sneaks in bets the system can't afford to keep. Refreshing the architecture roadmap is how you trade off between new capability and the NFRs you promised — and how you justify the architecture-focused items on the overall roadmap.

## Definition of Done

- [ ] Themes for architectural evolution (scale, modernization, consolidation) are defined
- [ ] Initiatives are sequenced with stated business value
- [ ] Cost and risk of inaction are quantified
- [ ] A retirement list for deprecated patterns, platforms, or services is included
- [ ] Dependencies on the product roadmap are explicit

## What it contains

- Themes for architectural evolution (scale, modernization, consolidation)
- Sequenced initiatives with business value
- Cost and risk of inaction
- Retirement list (deprecated patterns, platforms, services)
- Dependencies on product roadmap
- Decision framework for future ADRs

## Inputs you rely on

- Architectural health report and scale-readiness report
- Architecture updates from Operate
- Cost & capacity report
- Updated product roadmap
- Modernization plan (if separate)

## Who consumes it

- Sponsor — input to investment decisions on architecture work
- Developer — anticipates future patterns
- SRE — platform and tooling planning
- Next Discover cycle — seeds architecture feasibility conversations

## Common pitfalls

- Architecture roadmap divorced from product roadmap; nothing aligns
- All themes labeled critical; no sequencing that fits the bet budget
- No retirements; platform accretes complexity forever
- Inaction risk not quantified; Sponsor under-funds the work

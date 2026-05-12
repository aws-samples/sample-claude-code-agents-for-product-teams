# capability gap report

_Produced by: Gap analysis_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Business Analyst

**Stakeholders:** Architect

**Accelerated MVP:** optional when the MVP lives within existing capability

## What this is

A gap analysis of required capabilities vs. what the organization, platform, and product already provide — categorized by build, buy, partner, or defer. It names the real work, not just the feature list.

## Why it matters for the Business Analyst

You produce this — with Architect — so the organization distinguishes "new to the product" from "new to the company." Unseen gaps in platform, process, or people are the reason build schedules slip; this artifact makes them visible before commitment.

## Definition of Done

- [ ] Required capabilities are derived from specific requirements or to-be process steps
- [ ] Each capability carries a gap classification (missing / partial / duplicative / undersized)
- [ ] Each gap has a disposition (build / buy / partner / defer / reuse-with-extension)
- [ ] Each gap carries an effort and time-to-capability estimate
- [ ] Dependencies on other initiatives' capability work are named

## What it contains

- Required capabilities derived from requirements and to-be processes
- Current-state inventory of related capabilities in the org
- Gap classification (missing, partial, duplicative, undersized)
- Disposition: build, buy, partner, defer, or reuse-with-extension
- Effort and time-to-capability estimate per gap
- Dependencies on other initiatives' capability builds

## Inputs you rely on

- [Requirements document](requirements-document.md) and [NFR document](nfr-document.md)
- [System-to-process map](system-to-process-map.md)
- Enterprise capability model if one exists
- [Technical feasibility findings](technical-feasibility-findings.md)

## Who consumes it

- Architect — drives [solution recommendation](solution-recommendation.md) and build-vs-buy
- Product Owner — uses it to sequence the roadmap realistically
- Project Manager — derives [dependency list](dependency-list.md) and risks
- Product Sponsor — sees the true scope of the initiative beyond the product itself

## Common pitfalls

- Mixing product features and enterprise capabilities in one list
- Treating partial capabilities as full, and inheriting hidden gaps
- No effort estimate per gap, so the scope looks smaller than it is
- Ignoring capabilities needed in non-engineering functions (Legal, Support, Finance)

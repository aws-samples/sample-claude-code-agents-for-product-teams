# KPI definitions

_Produced by: Success metrics / KPI definition_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Product Owner

**Stakeholders:** Product Sponsor

**Accelerated MVP:** required — the MVP cannot be evaluated without named metrics

## What this is

The precise, implementable definitions of the metrics the product will be judged by — formula, data source, cadence, owner, and target. Definitions at this level let engineers instrument, analysts compute, and everyone argue about the right thing.

## Why it matters for the Product Owner

You produce this so success is defined before the build starts, not relitigated after it ships. Each KPI definition also becomes a contract with SRE and Developer on what telemetry must be emitted — fuzzy definitions produce fuzzy dashboards that no one trusts.

## Definition of Done

- [ ] Each KPI has a name, plain-language description, and exact formula with numerator, denominator, and filters
- [ ] Data source and required events are named per KPI
- [ ] Cadence and refresh-latency tolerance are specified
- [ ] Targets and green/yellow/red thresholds are stated
- [ ] Each KPI names an owner and a sign-off authority for definition changes

## What it contains

- KPI name and plain-language description
- Exact formula with numerator, denominator, and filters
- Data source and event definitions required to compute it
- Cadence (real-time, daily, weekly) and refresh latency tolerance
- Segmentation dimensions (persona, plan, geography)
- Target and threshold for "green / yellow / red"
- Owner for the number and who signs off on definition changes

## Inputs you rely on

- [Outcome hypothesis](../../1-discover/artifacts/outcome-hypothesis.md) and [business case](../../1-discover/artifacts/business-case.md)
- [User personas](../../1-discover/artifacts/user-personas.md) for segmentation dimensions
- Existing analytics stack and data-model constraints
- Finance and Sponsor agreement on North-Star candidate

## Who consumes it

- Architect and Developer — drive telemetry planning (in Plan) and instrumentation (in Build)
- Business Analyst — owns the traceability from KPI to requirement to test
- Product Sponsor — governs against these numbers at every gate and in Operate
- Sales & Marketing — aligns commercial KPIs (ARR, pipeline) with product KPIs

## Common pitfalls

- Vanity metrics (pageviews, signups) that do not tie to outcomes
- Definitions that depend on data the platform cannot emit
- Too many KPIs — more than 5–7 and the team can't steer against them
- No change-control — KPI definitions quietly drift and historical comparisons break

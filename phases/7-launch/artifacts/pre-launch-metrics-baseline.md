# pre-launch metrics baseline

_Produced by: Launch baseline snapshot_

**Business outcome supported:** product live, teams enabled, customers notified, baseline metrics captured, and launch stabilized through hypercare.

**Primary owner:** Business Analyst

**Stakeholders:** Product Owner

**Accelerated MVP:** required — MVP impact can't be measured without a baseline

## What this is

A frozen snapshot of KPI values as of the moment before launch — the numbers that define "before" so Iterate can legitimately claim "after." Includes the baseline definition of each metric, source system, and measurement window.

## Why it matters for the Business Analyst

Benefits realization and ROI assertions made in the business case are only credible if there is a clean baseline to measure against. Without it, Iterate becomes a debate about what counts; with it, every claim is evidence-traceable back to the business case.

## Definition of Done

- [ ] Each KPI is captured with its precise definition, formula, and source system.
- [ ] Baseline value, measurement window, and sample size are recorded per KPI.
- [ ] Segmentation baselines exist for every cohort, geo, or plan the business case cares about.
- [ ] Known data caveats and exclusions are documented alongside the baseline.
- [ ] Target trajectory from the approved business case is stated and linked.

## What it contains

- Each KPI with its precise definition, formula, and source
- Baseline value, measurement window, and sample size
- Segmentation baselines (by cohort, geo, plan) where relevant
- Known data caveats and exclusions
- Target trajectory pulled from the approved business case
- Link to the live launch KPI dashboard that will track the lift

## Inputs you rely on

- KPI definitions from Define phase
- Verified KPI telemetry from Verify phase
- Approved business case and benefits plan
- Pre-launch production data for the last stable period
- Data inventory & classification (to cite authoritative sources)

## Who consumes it

- Product Owner and Sponsor — anchor the board narrative and reforecast in Iterate
- Business Analyst — inputs to benefits-realization report and benefits-shortfall analysis
- Finance — reconciles commercial KPIs against forecast
- Product Marketing — fact-checks "X% improvement" claims in collateral

## Common pitfalls

- Capturing the baseline after launch has already perturbed the system
- Redefining a KPI mid-flight, invalidating the before/after comparison
- Missing segments the business case cared about (e.g. enterprise vs. SMB)
- No provenance on source data — baseline can't survive audit

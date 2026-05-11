# ROI model

_Produced by: Cost-benefit / ROI analysis_

**Business outcome supported:** frame the opportunity, validate the problem, understand the market, and exit with a funded, strategically-aligned bet.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

## What this is

The working spreadsheet (or equivalent) that computes NPV, IRR, and payback from the benefit and cost inputs. It is the engine behind the [business case](business-case.md) — the business case is the narrative; this is the math.

## Why it matters for the Business Analyst

You own this model because every later phase will tug at its inputs as reality changes. A well-structured model — explicit assumptions, clean sensitivity levers, versioned snapshots — lets you update honestly; a spaghetti model quietly hides the fact that the business case no longer holds.

## Definition of Done

- [ ] Cost inputs cover build, run, opportunity, and change-management lines.
- [ ] Benefit inputs separate incremental revenue, cost avoidance, and productivity gain.
- [ ] Adoption curve, discount rate, and time horizon assumptions are explicit.
- [ ] NPV, IRR, and payback are computed under expected, best, and worst cases.
- [ ] Sensitivity tornado covers the top 3-5 drivers.

## What it contains

- Cost inputs: build (one-time), run (recurring), opportunity, and change-management
- Benefit inputs: incremental revenue, cost avoidance, productivity gain
- Adoption curve with explicit ramp assumptions
- Time horizon, discount rate, and terminal value policy
- Sensitivity tornado for top 3–5 drivers
- NPV, IRR, payback, and break-even under expected/best/worst cases

## Inputs you rely on

- [Opportunity sizing](opportunity-sizing.md) for benefit lines
- [ROI technical inputs](roi-technical-inputs.md) for build and run cost
- [Pricing benchmark report](pricing-benchmark-report.md) for unit economics
- Finance-sanctioned discount rate and treatment of internal costs

## Who consumes it

- Product Sponsor — uses it to defend funding in governance forums
- Product Owner — uses sensitivities to see which decisions actually move the needle
- Business Analyst (future you) — refines it in Design as [updated ROI model](../../3-design/artifacts/updated-roi-model.md) and tracks actuals in Operate/Iterate

## Common pitfalls

- Hard-coded numbers instead of input cells, so updates require archaeology
- Optimistic ramp curves with no basis in comparable launches
- Missing run-cost escalation (support, compliance, platform fees)
- No version control — "which version did the Sponsor approve?" becomes unanswerable

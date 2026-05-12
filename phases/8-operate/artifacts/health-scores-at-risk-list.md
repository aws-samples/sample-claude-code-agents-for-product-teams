# health scores & at-risk list

_Produced by: Customer health scoring_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Customer Support

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the cohort is small enough to track in-head

## What this is

A composite score per customer account — usage, support sentiment, NPS, billing health, executive engagement — that predicts renewal probability. Paired with an at-risk list triaged into save-plays.

## Why it matters for the Customer Support / Success team

Net retention is the compounding growth engine for any subscription business. Health scoring turns gut-feel CSM judgment into a pipeline of save-opportunities; the at-risk list is the proactive work that protects the number you've already booked.

## Definition of Done

- [ ] Score components and their weights are documented.
- [ ] Every account in scope has a current health score and trend direction.
- [ ] At-risk accounts have a named CSM and action owner.
- [ ] Each at-risk account has a save-play status and next step.
- [ ] Renewals within the next two quarters are flagged on the list.

## What it contains

- Score components and weights, documented
- Current health score per account
- Trend (improving, stable, declining)
- At-risk accounts with CSM and action owner
- Save-play status and next step
- Renewals within the next two quarters

## Inputs you rely on

- Product usage telemetry and activation events
- Support ticket volume and sentiment
- NPS and customer feedback
- Renewal dates from CRM
- Executive sponsor engagement logs

## Who consumes it

- CSM team — prioritize outreach and save-plays
- Sales — coordinate on expansion plays with healthy accounts
- Business Analyst — input to churn and retention analysis
- Product Owner — segments that churn at higher rates feed Iterate

## Common pitfalls

- Score opaque — CSMs don't trust it, fall back on intuition
- All components weighted equally; dominant signals ignored
- At-risk list without action — no save-play doctrine
- Score not reviewed when renewals come in; model stays stale

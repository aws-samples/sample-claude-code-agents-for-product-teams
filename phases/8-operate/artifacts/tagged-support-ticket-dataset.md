# tagged support-ticket dataset

_Produced by: Tag / categorize support tickets_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Customer Support

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when ticket volume is low

## What this is

The support ticket corpus enriched with consistent tags — product area, feature, persona, severity, root-cause class, sentiment — so that analysis can slice the data reliably. The dataset behind the VoC trend analysis.

## Why it matters for the Customer Support team

Your tickets are one of the richest data sources the product has. If tagging is inconsistent, every downstream analysis is fuzzy; if tagging is disciplined, Support becomes a revenue-adjacent function by telling Product and Marketing where the friction actually is.

## Definition of Done

- [ ] A canonical tag taxonomy with definitions is documented.
- [ ] Tickets carry version, plan, and segment fields.
- [ ] Tagging QA and inter-agent consistency are measured.
- [ ] Sentiment or CSAT is recorded per ticket.
- [ ] Root-cause classification and a link to customer account for revenue weighting are present.

## What it contains

- Canonical tag taxonomy with definitions
- Tagged tickets with version, plan, segment
- Tagging QA and inter-agent consistency
- Sentiment or CSAT per ticket
- Root-cause classification
- Link to customer account for revenue weighting

## Inputs you rely on

- Triaged ticket queue and customer resolutions
- Support process model
- Taxonomy decisions and annotation guidelines
- NPS and customer feedback data
- Product feature map

## Who consumes it

- Business Analyst — support/VoC trend analysis
- Product Owner — backlog and Iterate priorities
- Technical Writer — KB article gap identification
- Customer Success — account-level issue history

## Common pitfalls

- Taxonomy grows without pruning; duplicates and near-synonyms dilute signal
- No calibration sessions; agents tag inconsistently
- Tagging happens at ticket close, so live-queue analysis is impossible
- Sensitive content (PII, customer verbatims) not access-controlled

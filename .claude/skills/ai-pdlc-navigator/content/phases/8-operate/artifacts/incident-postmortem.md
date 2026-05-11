# incident postmortem

_Produced by: Incident response / on-call_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

## What this is

The shareable, blameless narrative of an incident — what happened, impact, causes, response effectiveness, and follow-up actions — written for the broader engineering org to read and learn from. One per incident above severity threshold.

## Why it matters for the SRE

Postmortems build organizational memory. They turn a painful incident into a teaching artifact that new engineers read during onboarding, Architects cite in design reviews, and Sponsors reference during reliability investments. Without them, reliability stays tribal.

## Definition of Done

- [ ] Summary is written for a wide engineering audience (blameless, shareable).
- [ ] Customer impact and incident duration are stated.
- [ ] Contributing causes and detection/response analysis are documented.
- [ ] "What went well" is called out alongside what didn't.
- [ ] Action items carry owners, due dates, and status; the investigation report and RCA are linked.

## What it contains

- Summary suitable for wide distribution
- Customer impact and duration
- Contributing causes and detection/response analysis
- What went well
- Action items with owners, due dates, and status tracking
- Links to incident investigation report and RCA

## Inputs you rely on

- Incident investigation report and RCA
- Customer communications sent during incident
- Any Sev-1 approved incident comms
- Postmortem review session notes
- Related past postmortems

## Who consumes it

- Engineering org — learning and onboarding material
- Sponsor — input to operational performance review
- Security & Compliance — evidence of incident handling discipline
- Customer Success — conversations with affected customers

## Common pitfalls

- Naming individuals instead of system behaviors
- Action items that quietly age out with no tracking
- Limited circulation — other teams never learn the lesson
- Writing the postmortem too long after the fact — detail lost

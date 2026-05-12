# known-issues list

_Produced by: Identify known issues_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Customer Support

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — a short shared doc of "what doesn't work yet" is enough

## What this is

The living register of recurring customer-facing issues with status, workaround, and fix ETA. Both an internal support tool and the public-facing "known issues" customers can check before filing a ticket.

## Why it matters for the Customer Support team

Deflection depends on customers finding answers before they escalate to humans. A clean, discoverable known-issues list reduces ticket volume, shortens resolution times (agents get to the workaround faster), and makes the product feel more transparent to customers.

## Definition of Done

- [ ] Each issue has a customer-facing description with symptoms.
- [ ] Affected versions, plans, or regions are scoped.
- [ ] Workaround (with any limits) and fix ETA are captured.
- [ ] Status reflects current investigation state and links to the ticket or PR.
- [ ] First-seen and last-updated dates are recorded; fixed items are retired.

## What it contains

- Issue description with symptoms
- Affected versions, plans, or regions
- Workaround and its limits
- Fix ETA and ticket/PR link
- Status (under investigation, fix in progress, fixed)
- Date first seen and last updated

## Inputs you rely on

- Customer resolutions and tagged support-ticket dataset
- Incident investigation reports
- Prioritized prod issue log
- Release notes and prioritized bug list
- Escalated issue tickets

## Who consumes it

- Customers — self-serve before filing tickets
- Support agents — resolution shortcut
- Sales engineers — pre-empt objections in deals
- Product Owner — frequent issues shape Iterate priorities

## Common pitfalls

- Internal-only list; customers keep filing duplicates
- Workarounds with side-effects not documented
- Status never updated; "under investigation" for months
- Fixed items never retired — noise drowns active issues

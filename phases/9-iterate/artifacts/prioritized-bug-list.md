# prioritized bug list

_Produced by: Prioritize bug fixes_

**Business outcome supported:** close the loop — measure actual performance against the business case, decide continue/pivot/sunset, and feed validated learning back into Discover for the next cycle.

**Primary owner:** Product Owner

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — bugs are the first iteration's debt

## What this is

The PO-ordered backlog of customer-reported and internally-found bugs, ranked by impact, reach, and severity. The list engineering pulls from when capacity is allocated to fixes rather than new features.

## Why it matters for the Product Owner

Bug backlog management is where value and reliability trade off. Without prioritization discipline, either customers churn over unfixed issues or engineering burns velocity on low-impact fixes. Your ranked list makes the trade-offs explicit and defensible.

## Definition of Done

- [ ] Each entry has a bug description and reproduction reference
- [ ] Customer impact is scored (severity x reach)
- [ ] Suggested priority and target release are assigned
- [ ] Workaround status is noted
- [ ] Age and SLA compliance are tracked against each item

## What it contains

- Bug description and reproduction reference
- Customer impact (severity × reach)
- Suggested priority and target release
- Workaround status
- Link to bug report and support tickets
- Age and SLA compliance

## Inputs you rely on

- Bug reports from QA/Tester
- Known-issues list and customer resolutions
- Prioritized prod issue log
- Customer health scores (weight toward at-risk accounts)
- Escalated issue tickets

## Who consumes it

- Developer — work queue
- Release Manager — release planning
- Customer Support — response to affected customers
- Iterate and Plan phases — capacity allocation

## Common pitfalls

- Severity without reach; one-customer Sev-1s beat multi-customer Sev-2s
- Aged bugs buried; no SLA enforcement
- Duplicates survive; wastes engineering triage
- No linkage to revenue impact; prioritization feels arbitrary

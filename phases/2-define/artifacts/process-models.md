# process models

_Produced by: Business process modeling (as-is / to-be)_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Business Analyst

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the MVP doesn't change existing business processes

## What this is

As-is and to-be diagrams of the business processes the product participates in — who does what, in what order, with what inputs and outputs, and where the product fits. Typically BPMN or an equivalent lightweight swim-lane notation.

## Why it matters for the Business Analyst

You produce these because requirements without process context are fragments. Modeling the before and after makes hand-offs, wait states, and exception paths visible — which is exactly where scope gaps and change-management cost hide.

## Definition of Done

- [ ] Both as-is and to-be diagrams exist for each in-scope process
- [ ] As-is includes current pain points, cycle times, and error paths
- [ ] To-be shows measurable improvements against the as-is
- [ ] Swim lanes are drawn for each actor (user, system, integration partner)
- [ ] Happy path, alternate paths, and exception handling are each depicted

## What it contains

- As-is process with current pain points, cycle times, and error paths
- To-be process with the product in place, with measurable improvements
- Swim lanes for each actor (user, system, integration partner)
- Happy path, alternate paths, and exception handling
- Hand-off points and the data that flows at each
- Business rules that fire at specific steps

## Inputs you rely on

- Process interviews and observation sessions with operators
- [Validated problem statement](../../1-discover/artifacts/validated-problem-statement.md) and [user personas](../../1-discover/artifacts/user-personas.md)
- Existing SOPs, runbooks, and support playbooks
- Metrics on current cycle times and error rates if available

## Who consumes it

- Architect — derives the [system-to-process map](system-to-process-map.md) from these
- Product Owner — uses to-be to validate scope and sequence
- Customer Support — uses to-be to shape the [support process model](support-process-model.md)
- Change management (if separate) — uses delta to plan [affected-audiences](affected-audiences-list.md) communications

## Common pitfalls

- Only happy paths — real work lives in the exceptions
- To-be processes drawn without talking to the people who will run them
- No cycle-time or volume data, so improvement claims are unfalsifiable
- Notation salad — mix of conventions that no downstream reader can parse

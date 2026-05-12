# change impact assessment

_Produced by: Change impact analysis_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Business Analyst

**Stakeholders:** Architect

**Accelerated MVP:** optional when the MVP has no downstream-system impact

## What this is

A structured analysis of who and what is affected by introducing the product — people, processes, systems, policies, partners — and what work is needed for each to absorb the change. This is distinct from the in-flight "change control" mechanism; it is pre-build impact scoping.

## Why it matters for the Business Analyst

You produce this so the cost of change is visible alongside the cost of build. Initiatives that ignore change-management cost ship "complete" products that nobody adopts because training, policy, and process didn't happen.

## Definition of Done

- [ ] Assessment names affected groups with the nature of impact for each
- [ ] Process changes show an explicit as-is to to-be delta
- [ ] System changes are classified as new / changed / retired
- [ ] Training and enablement needs are identified per affected group
- [ ] Residual risks of un-absorbed change are listed with owners

## What it contains

- Affected groups (teams, roles, customer segments) and nature of impact
- Process changes with delta from as-is to to-be
- System changes (new, changed, retired)
- Policy, contract, and procedure updates
- Training and enablement needs
- Communication and sequencing plan candidates
- Residual risks if change is not absorbed

## Inputs you rely on

- [Process models](process-models.md) and [system-to-process map](system-to-process-map.md)
- [Stakeholder map](../../1-discover/artifacts/stakeholder-map.md)
- [Affected-audiences list](affected-audiences-list.md)
- [Support process model](support-process-model.md) for support-side impact

## Who consumes it

- Project Manager — uses it to shape the change / comms plan in Plan
- Business Analyst (future you) — maintains it through Build as scope evolves
- Customer Support and Sales & Marketing — scope enablement from it
- Product Sponsor — tests "is the org ready to absorb this?" before committing budget

## Common pitfalls

- Only assessing technical systems; missing people and process impact
- One-shot assessment — change scope evolves with design decisions
- Underestimating training cost, especially for internal operations teams
- No residual-risk column, so unabsorbed impact silently becomes launch risk

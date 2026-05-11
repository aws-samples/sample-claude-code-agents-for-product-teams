# support process model

_Produced by: Support process definition_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Customer Support

**Stakeholders:** _(none listed)_

## What this is

The end-to-end model of how customers will get help with the product — tiers, channels, SLAs, triage paths, escalation routes, knowledge-base structure, and staffing implications. It is the support equivalent of an architecture diagram.

## Why it matters for the Customer Support owner

You produce this so support is designed alongside the product, not reverse-engineered the week before launch. Cost-to-serve and retention are shaped here — a good model prevents the launch-day surge from becoming launch-month churn.

## Definition of Done

- [ ] Support tiers (T1/T2/T3) are defined with responsibility boundaries
- [ ] Intake channels and triage rules are specified
- [ ] SLA targets are listed by severity and contract tier
- [ ] Escalation path includes named hand-offs to Engineering and SRE
- [ ] Staffing model and training implications are stated

## What it contains

- Support tiers and responsibility boundaries (T1/T2/T3)
- Intake channels (chat, email, phone, in-product) and triage rules
- SLA targets by severity and contract tier
- Escalation path including Engineering and SRE hand-offs
- Knowledge base taxonomy and content-ownership model
- Tooling requirements (ticketing, knowledge, telemetry access)
- Staffing model and training implications

## Inputs you rely on

- [User personas](../../1-discover/artifacts/user-personas.md) and expected support volume
- [Process models](process-models.md) and to-be customer journey
- [KPI definitions](kpi-definitions.md) for support-side metrics
- Existing support stack and team capacity

## Who consumes it

- Project Manager — includes support readiness in Plan and launch readiness
- Technical Writer — aligns documentation plan with support's KB taxonomy
- Product Owner — sees where product gaps will drive avoidable tickets
- Customer Support (future you) — operates it in [live support processes](../../../7-launch/artifacts/live-support-processes.md) and evolves it in Operate

## Common pitfalls

- Designing for expected volume instead of peak volume at launch
- SLA targets divorced from staffing reality
- No feedback loop from support into product backlog — Voice of Customer dies in tickets
- Missing cross-team handoffs (SRE for incidents, Engineering for bugs) and their SLAs

# journey map / service blueprint

_Produced by: Customer journey mapping_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** UI/UX Designer

**Stakeholders:** _(none listed)_

## What this is

Two paired artifacts: the user journey map (the experience from the user's point of view, including pre- and post-product touchpoints) and the service blueprint (the front-stage, back-stage, and support processes that make the journey work). Together they show what the user experiences and what the org must do to deliver it.

## Why it matters for the UI/UX Designer

You produce these so the team designs for the whole job-to-be-done rather than the UI in isolation. A great screen inside a broken journey is still a broken product, and the service blueprint is how you get Support, Ops, and Engineering aligned before build.

## Definition of Done

- [ ] Primary persona and scenario are named up front.
- [ ] Every journey stage shows user goals and emotions.
- [ ] Touchpoints are mapped across channels at each stage.
- [ ] Front-stage and back-stage actions are both represented.
- [ ] A success metric is named for each stage.

## What it contains

- Persona and scenario context
- Stages of the journey with user goals and emotions per stage
- Touchpoints across channels and the content/action at each
- Pain points and moments of truth
- Front-stage UI interactions and back-stage system/people actions
- Support processes underpinning each stage
- Metrics that signal success per stage

## Inputs you rely on

- [User personas](../../1-discover/artifacts/user-personas.md) and [validated problem statement](../../1-discover/artifacts/validated-problem-statement.md)
- [Process models](../../2-define/artifacts/process-models.md) and [support process model](../../2-define/artifacts/support-process-model.md)
- Analytics and support data if an adjacent product exists
- Usability research from Discover

## Who consumes it

- Product Owner — uses it to sequence MVP and identify gaps
- Business Analyst — validates that requirements cover every stage
- Customer Support — aligns the support blueprint with design intent
- UI/UX Designer (future you) — decomposes it into [IA spec](ia-spec.md) and [design specification](design-specification.md)

## Common pitfalls

- Front-stage only — misses the back-stage work that makes or breaks the journey
- Too many personas in one map; pick the primary and show the journey for them
- Emotions drawn but never acted on — capture only what you will design to
- No metric per stage, so "improvement" is unmeasured

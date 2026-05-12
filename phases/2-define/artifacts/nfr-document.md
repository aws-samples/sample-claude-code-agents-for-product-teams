# NFR document

_Produced by: Non-functional requirements definition_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Architect

**Stakeholders:** Business Analyst

**Accelerated MVP:** slim — define only the NFRs the MVP's traffic and data sensitivity actually stress

## What this is

The catalog of non-functional requirements — performance, availability, scalability, security, privacy, maintainability, observability, portability, usability, accessibility — each quantified with a target, a measurement method, and a rationale. NFRs are requirements too, just the kind that usually determine build cost.

## Why it matters for the Architect

You own NFRs because they drive architecture more than functional features do. A "three nines" commitment and a "five nines" commitment are different products; authoring NFRs concretely is how you force the org to pay for what it has committed to, or walk back the commitment.

## Definition of Done

- [ ] Each NFR has a unique ID, category, and quantified target with tolerance
- [ ] Each NFR specifies a measurement method and data source
- [ ] Each NFR ties its target to a business need or regulatory obligation
- [ ] Applicability scope (services / tiers / personas / geographies) is stated per NFR
- [ ] Trade-offs between competing NFRs are captured

## What it contains

- Each NFR with ID, category, quantified target, and tolerance
- Measurement method and data source (how you will prove it)
- Rationale tying target to a business need or regulatory obligation
- Applicability scope (which services, tiers, personas, geographies)
- Cost implications and dependencies
- Trade-off notes where two NFRs pull against each other

## Inputs you rely on

- [Requirements document](requirements-document.md) for functional context
- [Applicable-regulations list](applicable-regulations-list.md) and [data inventory & classification](data-inventory-classification.md)
- [KPI definitions](kpi-definitions.md) and Sponsor's appetite for cost
- Platform team's current SLIs / SLOs and cost baselines

## Who consumes it

- Architect (future you) — derives architecture, API, and data-model decisions
- Developer — uses as Definition-of-Done input for code and instrumentation
- QA/Tester — designs performance, resilience, and security tests
- Security & Compliance — traces [security control requirements](security-control-requirements.md) and derives DPIA input

## Common pitfalls

- Unquantified NFRs ("fast", "secure", "scalable") — no way to pass or fail
- Inherited NFRs from a prior product without re-checking fit
- Over-spec ("five nines" when nobody is paying for it)
- No trade-off statements — availability vs. cost, latency vs. consistency — makes later choices look like regressions

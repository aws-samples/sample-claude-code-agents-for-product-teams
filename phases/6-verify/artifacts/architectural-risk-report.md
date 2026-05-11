# architectural risk report

_Produced by: Architectural risk assessment_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

## What this is

The Architect's honest inventory of residual architectural risk at the cusp of launch — areas where the architecture is working but strained, known technical debt that amplifies incidents, and the "we got lucky" patterns that should be watched.

## Why it matters for the Architect

Not every risk can be bought down before launch; some must go to production consciously. Documenting those with blast-radius, probability, and mitigation plan is how you keep them visible post-launch and convert the end of Verify into the start of an informed Operate posture rather than hidden liabilities.

## Definition of Done

- [ ] Residual risks are inventoried with description and context
- [ ] Each risk has a blast-radius and probability score
- [ ] Mitigation, contingency plans, and watch conditions (with alert tie-ins) are recorded per risk
- [ ] Remediation backlog for Iterate/post-launch is listed
- [ ] Dependencies on external teams or vendors are identified

## What it contains

- Residual risk inventory with description and context
- Blast-radius and probability scoring
- Mitigation and contingency plans
- Watch conditions and alert tie-ins
- Remediation backlog for Iterate/post-launch
- Dependencies on external teams or vendors

## Inputs you rely on

- Architecture validation report
- Performance and resilience test results
- Conformance findings from Build
- Incident-response plan
- Enabler backlog and tech-debt signals

## Who consumes it

- Approved known-issues & risk acceptance outcome consumes this
- Product Sponsor — weighs residuals in launch-risk acceptance
- SRE — feeds into monitoring and runbooks
- Product Owner — prioritizes follow-on remediation in Iterate

## Common pitfalls

- Residuals framed as "unlikely" without probability reasoning
- No watch conditions — the risk is on paper but invisible in production
- Remediation backlog never scheduled after launch
- Understated risks to protect launch optimism — surfaced at the first incident

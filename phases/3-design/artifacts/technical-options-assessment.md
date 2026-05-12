# technical options assessment

_Produced by: Research technical options_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — an ADR comparing the shortlist suffices

## What this is

A structured evaluation of the viable technical approaches for the solution — stacks, patterns, deployment models, build-vs-buy options — scored against NFRs, cost, time-to-value, and strategic fit. It is the decision artifact that precedes the architecture document.

## Why it matters for the Architect

You own this so architectural commitments are made with evidence rather than preference. A clear options record also protects you when reality proves one of the constraints different than assumed — it shows the reasoning at the time the call was made.

## Definition of Done

- [ ] At least three credible options are evaluated, not just preferred vs. straw-man.
- [ ] Evaluation criteria and weights are set before scoring.
- [ ] Each score cites the evidence behind it.
- [ ] Spike or POC results are recorded for the riskiest option(s).
- [ ] Recommendation states its conditions and attached risks.

## What it contains

- The set of credible options with one-paragraph descriptions
- Evaluation criteria and weights (NFR fit, cost, risk, time, strategic control)
- Scored comparison with evidence behind each score
- Spike or POC results where they moved scores
- Recommended option and the next-best with reasoning
- Conditions and risks attached to the recommendation

## Inputs you rely on

- [Solution recommendation](../../2-define/artifacts/solution-recommendation.md) and [NFR document](../../2-define/artifacts/nfr-document.md)
- [Technical feasibility findings](../../2-define/artifacts/technical-feasibility-findings.md)
- Platform and security pattern libraries
- Vendor pricing and reference customer input for buy candidates

## Who consumes it

- Product Sponsor — ratifies via [build-vs-buy decision](../outcomes/build-vs-buy-decision.md)
- Architect (future you) — carries the chosen approach into [architecture document](architecture-document.md) and [decision log](../outcomes/decision-log.md)
- Business Analyst — updates [vendor evaluation scorecard](vendor-evaluation-scorecard.md) for buy options
- Security & Compliance — pressure-tests against [security control requirements](../../2-define/artifacts/security-control-requirements.md)

## Common pitfalls

- Two-option assessment (preferred vs. straw-man) — not a real evaluation
- Weights adjusted after scoring to produce the desired answer
- No spike evidence for the riskiest option
- Recommendation without conditions, so risks silently ride along

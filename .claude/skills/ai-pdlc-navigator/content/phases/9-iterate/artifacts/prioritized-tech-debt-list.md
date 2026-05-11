# prioritized tech-debt list

_Produced by: Technical debt backlog grooming_

**Business outcome supported:** close the loop — measure actual performance against the business case, decide continue/pivot/sunset, and feed validated learning back into Discover for the next cycle.

**Primary owner:** Architect

**Stakeholders:** Developer

## What this is

The ranked list of technical-debt items — latent architectural issues, shortcut workarounds, outdated patterns, flaky tests — with evidence of cost to velocity, reliability, or security. The non-feature work engineering argues for in planning.

## Why it matters for the Architect

Tech debt without prioritization is either ignored or treated as equally urgent, both of which are wrong. A ranked, evidence-backed list lets you make the case for specific debt work with a quantifiable case that Sponsor and Product Owner can buy into.

## Definition of Done

- [ ] Each debt item describes where it lives in the system
- [ ] A cost signal (velocity drag, incident correlation, security risk, cost) is cited with evidence
- [ ] Rough effort and fix risk are estimated
- [ ] Dependencies on other roadmap items are listed
- [ ] Proposed sequencing and an owner are assigned per item

## What it contains

- Debt item and where it lives
- Cost signal (velocity drag, incident correlation, security risk, cost)
- Rough effort and risk of the fix
- Dependency on other roadmap items
- Proposed sequencing
- Owner

## Inputs you rely on

- Architectural health report and conformance findings
- RCAs and postmortems correlating debt to incidents
- Cost & capacity report
- Scale-readiness and modernization plans
- Engineer-reported debt (bottom-up signals)

## Who consumes it

- Developer — picks up during debt sprints
- Product Owner — negotiates capacity split
- Sponsor — approves larger debt initiatives
- Iterate phase — slots debt into updated roadmap

## Common pitfalls

- Debt framed by vibes, not evidence — prioritization arbitrary
- Infinite backlog; same items sit for years
- No quantification of cost; Product Owner always wins the feature argument
- Debt work completed but the list not pruned

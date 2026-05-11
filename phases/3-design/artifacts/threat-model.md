# threat model

_Produced by: Threat modeling_

**Business outcome supported:** produce a build-ready design package — UX, architecture, data model, APIs, threat model, and integration map — with engineering signed off to build.

**Primary owner:** Security & Compliance

**Stakeholders:** Architect

## What this is

A structured analysis of how the architecture could be attacked — assets, trust boundaries, entry points, threats (typically via STRIDE or similar), mitigations, and residual risk. It is how abstract security controls become concrete, in-context design decisions.

## Why it matters for the Security & Compliance owner

You co-own this with the Architect so threats are considered while design is still malleable. A threat model done in Design is cheap mitigation; a threat model after Build means either re-architecture or accepted risk — and regulators treat the absence of one as negligence.

## Definition of Done

- [ ] Assets and their protection goals are listed explicitly.
- [ ] Data flow diagram shows trust boundaries.
- [ ] Threats are enumerated by category with likelihood and impact scores.
- [ ] Every threat has a mitigation or an explicit acceptance decision.
- [ ] Residual risks each have a named owner.

## What it contains

- Assets and their protection goals (CIA, privacy, integrity of audit)
- Data flow diagram with trust boundaries
- Entry points, actors (including insiders), and attack surfaces
- Threats enumerated by category with likelihood and impact
- Existing and proposed mitigations mapped to threats
- Residual risks and owners
- Assumptions and out-of-scope items

## Inputs you rely on

- [Architecture document](architecture-document.md), [data model](data-model.md), [integration map](integration-map.md), [API specification](api-specification.md)
- [Security control requirements](../../2-define/artifacts/security-control-requirements.md) and [privacy impact assessment](../../2-define/artifacts/privacy-impact-assessment.md)
- Org threat intelligence and prior incident patterns
- Secure design pattern library

## Who consumes it

- Architect — updates design to resolve mitigations
- Developer — implements mitigations and attests to them
- Security & Compliance (future you) — drives [approved security patterns](../outcomes/approved-security-patterns.md) and [security/compliance approval](../outcomes/security-compliance-approval.md)
- QA/Tester — designs security tests for the threats identified

## Common pitfalls

- External-actor focus only — misses insider, supply-chain, and abuse-of-feature threats
- Threats without mitigations or acceptance decisions
- No residual-risk owner, so risks drift into ambient anxiety
- One-shot exercise — threat model must be refreshed when architecture changes

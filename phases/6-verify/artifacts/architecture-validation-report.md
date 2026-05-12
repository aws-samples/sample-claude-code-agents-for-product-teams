# architecture validation report

_Produced by: Architecture validation in verify env_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** Architect

**Stakeholders:** _(none listed)_

**Accelerated MVP:** optional when the squad is its own architecture reviewer

## What this is

The Architect's confirmation that the as-built, as-deployed system matches the approved architecture — components, integrations, NFR posture, data model — as validated in the Verify environment under realistic load and failure scenarios.

## Why it matters for the Architect

The most expensive architectural problems land at launch because they were never actually validated end-to-end before. Running this check as a gate — using perf, resilience, and integration evidence — is how you catch the gaps between intent and reality while remediation is still possible.

## Definition of Done

- [ ] Component-by-component conformance is documented against the architecture document
- [ ] Integration-point verification references the integration map
- [ ] NFR attainment is supported by measured evidence (perf, scale, availability, security)
- [ ] Data model and schema confirmation is captured
- [ ] Deviations from ADRs list accepted-risk status, and required pre-launch remediation items are identified

## What it contains

- Component-by-component conformance against architecture document
- Integration-point verification against the integration map
- NFR attainment evidence (perf, scale, availability, security)
- Data model and schema confirmation
- Deviations from ADRs with accepted-risk status
- Remediation items required before launch

## Inputs you rely on

- Architecture document, integration map, and ADRs
- Performance, resilience, and security test reports
- Conformance findings from Build
- Validated staging environment
- Verified KPI telemetry

## Who consumes it

- PRR sign-off — architectural fitness is a key input
- Launch-readiness assessment — Sponsor-facing summary
- Architect peers and chief architect — portfolio posture
- Developers — own remediation items

## Common pitfalls

- Validation limited to the happy path — integration seams and failure modes untested
- NFR claims without measured evidence
- Deviations found but accepted without real risk analysis
- Report produced too late for the gaps to be fixed before launch

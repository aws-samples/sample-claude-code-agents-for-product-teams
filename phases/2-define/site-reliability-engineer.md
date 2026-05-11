# Site Reliability Engineer in Define

You are still mostly in a watching posture in Define, but the NFR document the Architect is writing is going to become your SLO target in Plan — so your job is to make sure the NFRs being written are reliability- and cost-realistic. Speak up now on availability, latency, capacity, and run-cost; it's cheap to change an NFR, expensive to miss an SLO.

## What you do

- Input on the [NFR document](artifacts/nfr-document.md) — bring operational reality to availability, latency, throughput, and cost targets
- Contribute to the [technical feasibility findings](artifacts/technical-feasibility-findings.md) — flag anything that's reliability- or on-call-hostile
- Begin scoping the environments, pipeline, and SLOs you'll build in Plan

## Artifacts you own

You don't own any artifacts this phase — you contribute to others' (see below).

## Artifacts you contribute to

- [NFR document](artifacts/nfr-document.md) — owned by the Architect with the BA; you bring the reliability and run-cost side of the NFRs
- [technical feasibility findings](artifacts/technical-feasibility-findings.md) — owned by the Architect, you flag operational risks

## Outcomes you drive

You don't drive outcomes this phase — you input into the Sponsor's [Define exit decision](outcomes/define-exit-decision.md) through reliability-grounded NFRs.

## Who you work with

- **Architect** — your primary touchpoint; their NFR document becomes your SLO target
- **Security & Compliance** — their control requirements may drive your observability and pipeline design later

## Handoff into Design

In [Design](../3-design/README.md) you'll co-own the security/compliance approval with Architect and Security, so your posture here sets you up to weigh in credibly on architecture fit for operations. The quality bar is that the NFRs leaving Define are ones you can plausibly deliver SLOs against without heroic effort. You're done when you believe the NFRs are honest and you have a clear picture of what Plan-phase work will be needed.

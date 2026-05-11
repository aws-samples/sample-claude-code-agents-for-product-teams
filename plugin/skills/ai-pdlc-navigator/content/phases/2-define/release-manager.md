# Release Manager in Define

You are still off-stage but increasingly aware. In Define, the commercial/delivery model decision and the NFRs being written will shape the release strategy you eventually own. Your job is to pay close attention to those two things and make sure nothing gets approved that implies a release shape you can't support — continuous delivery, air-gapped on-prem, regulated waterfalls all have very different implications.

## What you do

- Watch the [commercial model decision](outcomes/commercial-model-decision.md) — note how it shapes cadence, channels, and environments
- Read the [NFR document](artifacts/nfr-document.md) — availability and deployment-frequency targets are release-engineering decisions in disguise
- Stay aware of the [signed product charter](artifacts/signed-product-charter.md) and [applicable-regulations list](artifacts/applicable-regulations-list.md) — change-control posture comes from here

## Artifacts you own

You don't own any artifacts this phase — you contribute to others' (see below).

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Architect** — their NFRs and solution recommendation shape your release posture
- **Product Sponsor** — their commercial model decision may force a cadence or packaging shift
- **Security & Compliance** — their control requirements may land release gates in your pipeline

## Handoff into Design

Nothing you produce is a hard handoff into [Design](../3-design/README.md); you become materially active in Plan with the deployment runbook and in Verify when staging and smoke tests start. The quality bar is awareness — the release shape being implicitly chosen in Define shouldn't be a surprise to you in Plan. You're done when you can describe the release shape this initiative will have without needing to re-read anything.

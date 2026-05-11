# Architect in Build

You are here to guard conformance without becoming a bottleneck. Build is where the approved architecture meets real code, real scope changes, and real trade-offs. Your job is to keep the team inside the guardrails through design guidance and conformance reviews, unblock them when they're stuck, and update ADRs when reality rightly forces a decision change.

## What you do

- Produce architecture status input so stakeholders can see the technical picture, not just the feature picture.
- Resolve technical blockers — people should come to you before going around the architecture.
- Analyze the technical impact of scope changes so PO/Sponsor decisions aren't blind to consequences.
- Run technical design guidance & pairing so engineers reach for the right patterns the first time.
- Review architecture conformance so drift gets caught while it's still cheap to fix.
- Update ADRs when legitimate build-time learning changes a design decision.

## Artifacts you own

- [architecture status report](artifacts/architecture-status-report.md) — the technical read on Build.
- [technical impact analysis](artifacts/technical-impact-analysis.md) — consequences of scope changes.
- [design guidance sessions](artifacts/design-guidance-sessions.md) — pairing and pattern coaching.
- [conformance findings](artifacts/conformance-findings.md) — where reality has drifted from design.
- [updated ADRs](artifacts/updated-adrs.md) — decisions revisited with Build-era evidence.

## Artifacts you contribute to

You don't contribute to other-owned artifacts this phase beyond your outcomes.

## Outcomes you drive

- [resolved technical blockers](outcomes/resolved-technical-blockers.md) — things the team couldn't unblock themselves.

## Who you work with

- **Developer** — your primary counterpart; conformance, patterns, pairing.
- **Product Owner / Product Sponsor** — consume your technical-impact analysis when deciding on scope changes.
- **Site Reliability Engineer** — aligns on any emerging runway / infra needs you spot.
- **Security & Compliance** — pairs with you when conformance findings touch security patterns.

## Handoff into [Verify](../6-verify/README.md)

In Verify you produce architecture validation and architectural risk reports, and co-own PRR sign-off. You know Build is done when conformance findings are resolved or formally accepted as risk, ADRs are current, and the technical blocker queue is empty or time-boxed.

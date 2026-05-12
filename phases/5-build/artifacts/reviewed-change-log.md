# reviewed change log

_Produced by: Review incoming changes (changelog)_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim — PR reviews cover this for the MVP

## What this is

The SRE-reviewed, curated changelog from upstream merges — classified by risk, tagged for operational impact, and readied for inclusion in release notes and deployment runbooks. The operational cut of what engineering produced.

## Why it matters for the SRE

Release notes and incident correlation both depend on a trustworthy changelog. Reviewing the change stream with an ops lens is how you catch reliability-relevant changes early, flag risky rollouts for extra scrutiny, and keep the running record that powers incident forensics.

## Definition of Done

- [ ] Changes since previous review are grouped by service or component
- [ ] Every change has a risk classification of routine, elevated, or emergency
- [ ] Operational notes cover new alerts, migrations, flag toggles, or new dependencies
- [ ] Items needing deployment-runbook updates are flagged
- [ ] Items requiring stakeholder or customer-visible notice are identified

## What it contains

- Changes since previous review, grouped by service/component
- Risk classification per change (routine, elevated, emergency)
- Operational notes (new alerts, migrations, flag toggles, new dependencies)
- Flags for deployment-runbook updates needed
- Items requiring stakeholder or customer-visible notice
- Backport or cherry-pick tracking where relevant

## Inputs you rely on

- Merged code in main and its commit/PR metadata
- Changelog review process from Plan
- Working CI/CD pipeline outputs (build/test signals)
- Feature flag plan state
- Architecture status and conformance findings

## Who consumes it

- Release Manager — drafts release notes from the curated log
- SRE on-call — uses it during incident correlation
- Security & Compliance — audits for controls impact
- Support and Docs — prepare user-facing change information

## Common pitfalls

- Auto-generated log with zero curation — noise dominates signal
- Risky changes not flagged for extra rollout care
- Emergency changes never back-reviewed — policy erodes
- Log exists but isn't the source the release notes and runbooks consume

# Project Manager in Verify

You are here to orchestrate Verify so nothing falls through the cracks between testers, owners, and approvers. Multiple verification streams run in parallel — UAT, security, performance, accessibility, chaos, compliance — each with different owners and defect queues. Your job is to make the whole picture legible to the Sponsor and the go/no-go signers.

## What you do

- Coordinate Verify-phase execution across all testing streams so nothing blocks in silence.
- Produce the launch-readiness status pack so Sponsor and go/no-go signers have a single clear read.
- Run issue / defect governance — triage cadence, severity standards, owner assignment — so defects don't pile up anonymously.
- Maintain the RAID log and governance cadence through Verify.

## Artifacts you own

- [verify execution plan](artifacts/verify-execution-plan.md) — how Verify runs end-to-end.
- [launch-readiness status pack](artifacts/launch-readiness-status-pack.md) — the single read for decision-makers.
- [defect status & triage cadence](artifacts/defect-status-triage-cadence.md) — governance of the defect stream.

## Artifacts you contribute to

You don't formally contribute to other Verify-phase artifacts beyond your coordination outputs.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'. Your status pack is what the Sponsor's launch-readiness assessment stands on.

## Who you work with

- **All testing stream owners** (QA/Tester, SRE, Security & Compliance, Architect, UI/UX, Tech Writer, BA) — you coordinate the cadence.
- **Product Sponsor** — consumes your status pack to make launch decisions.
- **Product Owner** — co-governs defect triage priority with you.
- **Release Manager** — aligns Verify execution with deployment rehearsals.

## Handoff into [Launch](../7-launch/README.md)

In Launch you own the run-of-show, launch comms execution, and stage-gate (go/no-go) coordination. You know Verify is done when all streams are green or formally accepted, the status pack tells one coherent story, and defect governance has settled into the known-issues list the Sponsor has approved.

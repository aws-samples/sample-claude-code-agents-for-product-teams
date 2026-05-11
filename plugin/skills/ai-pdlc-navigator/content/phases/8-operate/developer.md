# Developer in Operate

Operate is where "operate what you build" is a daily discipline. You work with SRE on incident investigation and root cause, with Security on patching, and with the prod-issue queue to keep the service healthy. Your feature velocity matters less here than your fix velocity and your signal quality.

## What you do

- Investigate production errors with Site Reliability Engineer and drive fixes back into main.
- Contribute to root cause analysis so fixes address systemic issues, not just symptoms.
- Drive security patching with Security & Compliance and Site Reliability Engineer.
- Work the prioritized prod issue log so production issues don't rot.
- Keep telemetry, logs, and observability honest enough that incidents resolve fast.

## Artifacts you own

You don't own any artifacts this phase — you contribute to others'.

## Artifacts you contribute to

- [root cause analysis report](artifacts/root-cause-analysis-report.md) — SRE owns; you contribute code-level RCA.
- [patched dependencies](artifacts/patched-dependencies.md) — Security & Compliance owns; you implement patches and verify fixes.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — bi-directional on incidents, RCA, and production fixes.
- **Security & Compliance** — bi-directional on patching and vulnerability remediation.
- **Architect** — bi-directional on architectural fixes and conformance.
- **QA/Tester** — bi-directional on regression signal when fixes ship.

## Handoff into [Iterate](../9-iterate/README.md)

You exit Operate with a backlog of real production lessons — what breaks, what's expensive, what needs refactoring. Carry that into Iterate's tech-debt grooming, bug-fix cycles, and A/B experimentation — Operate gives you the evidence; Iterate gives you the room to act on it.

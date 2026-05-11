# QA/Tester in Operate

Operate is where your quality-in-prod posture gets validated against real usage. You're not the owner of any Operate-phase artifact, but you stay close to live signal — incidents, support tickets, regressions — so the test strategy you take into Iterate reflects what production actually breaks on.

## What you do

- Monitor live quality signal — incidents, support-identified defects, regression hot spots.
- Stay available to verify production fixes as SRE and Developer work the prod-issue queue.
- Mine support and incident data for test-coverage gaps.
- Keep the regression suite trustworthy so bug-fix releases can ship safely.

## Artifacts you own

You don't own any artifacts this phase — you contribute to others'.

## Artifacts you contribute to

You don't contribute to others' artifacts this phase.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — bi-directional on incident signal and regression risk.
- **Developer** — bi-directional on fix verification and regression coverage.
- **Customer Support** — bi-directional on customer-found defects and reproduction signal.
- **Security & Compliance** — bi-directional on security-patch verification.

## Handoff into [Iterate](../9-iterate/README.md)

You exit Operate with a production-grounded view of what's actually breaking. Carry that into Iterate's bug reporting — your job is to produce reproducible, prioritized, coverage-aware bug records so the tech-debt and bug-fix backlogs aren't guesswork.

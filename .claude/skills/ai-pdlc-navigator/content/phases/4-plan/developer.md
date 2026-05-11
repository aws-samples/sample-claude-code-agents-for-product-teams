# Developer in Plan

Plan is about sharpening your tools before you swing them. You're co-owning the CI/CD pipeline and feature flag strategy, refining your chunk of the enabler backlog, and making sure the approved design is something you can actually commit against. If Plan is done right, day one of Build is "pull a card and go," not "figure out how to build anything."

## What you do

- Co-own the CI/CD pipeline with SRE — you'll be living in it, so build it for fast feedback and loud failures.
- Co-own the enabler backlog with the Architect so technical runway work is visible and sequenced.
- Co-own the feature flag strategy with the Architect so progressive delivery is the default pattern.
- Review decomposed work items for buildability and flag ambiguity back to PO/BA before Build starts.
- Dry-run the pipeline on a throwaway change to validate scanning, lint, test, and deploy stages.

## Artifacts you own

You don't own artifacts outright this phase — you co-own foundational ones.

## Artifacts you contribute to

- [working CI/CD pipeline](artifacts/working-ci-cd-pipeline.md) — SRE owns; you're the primary user and co-builder.
- [enabler backlog](artifacts/enabler-backlog.md) — Architect owns; you scope and size the enablers.
- [feature flag plan](artifacts/feature-flag-plan.md) — Architect owns; you implement and operate it.

## Outcomes you drive

You don't drive outcomes this phase — you input into others'.

## Who you work with

- **Site Reliability Engineer** — builds the pipeline with you.
- **Architect** — hands you patterns, enabler sequencing, and flag strategy; you feedback what's buildable.
- **Product Owner / Business Analyst** — you flag work-item ambiguity back to them before Build.
- **QA/Tester** — you align on how tests run in the pipeline so integration testing works from sprint one.
- **Security & Compliance** — you confirm scanning gates are failing loud enough and fast enough.

## Handoff into [Build](../5-build/README.md)

In Build you become the primary producer — feature code, code review, merges, static analysis, telemetry, inline docs, all flowing through the pipeline you helped stand up. You know Plan is done when you can push a test commit through the full pipeline green, enablers are in flight, and you understand the patterns and flags you're expected to use.

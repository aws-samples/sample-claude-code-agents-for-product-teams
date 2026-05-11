# lint/static-analysis report

_Produced by: Static analysis / linting_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** _(none listed)_

## What this is

The output of lint, formatter, type-checker, and non-security static-analysis tooling across the codebase — surfacing code-quality and maintainability issues, style violations, and known-bug patterns. Typically produced automatically in CI and consumed per PR.

## Why it matters for the Developer

Static analysis catches the boring defects cheaply and keeps the codebase consistent enough that reviewers can focus on substance. Keeping the report clean is how you preserve reviewability and prevent the "broken windows" effect where small violations normalize into larger ones.

## Definition of Done

- [ ] Findings list file, severity, and rule-id
- [ ] Delta from previous run distinguishes new from pre-existing
- [ ] Every suppression carries a rationale
- [ ] Rule-set version and any project-local tuning are recorded
- [ ] Metrics cover warning density and trend

## What it contains

- Findings per file with severity and rule-id
- Delta from previous run (new vs. pre-existing)
- Suppression index with rationale
- Metrics: warning density, warnings per file, trend
- Rule-set version and any project-local tuning
- Auto-fix availability per rule

## Inputs you rely on

- Working CI/CD pipeline
- Rule-set decisions made during Plan (style, formatter, type-check strictness)
- Reviewed code rules (what blocks merge)
- Architecture and API specifications (for architectural linters)
- Developer tooling (IDE integration)

## Who consumes it

- Developers — fix findings before merge
- Architect — reviews new architectural-rule violations
- Engineering leads — watch trend and tighten rules over time
- Reviewers — use clean reports as a baseline expectation

## Common pitfalls

- Legacy baseline with 10k warnings making every new one invisible
- Disabling rules rather than addressing findings
- Run only on modified files so whole-file issues drift undetected
- No metric dashboarding so regressions are invisible until a clean-up push

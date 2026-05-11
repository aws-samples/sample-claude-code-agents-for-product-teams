# QA / Tester in Define

You are here to turn requirements into tests — not to execute anything yet, but to make sure every approved requirement has a test hook and every regulated control has a test owner. Define is where your testability bar gets set. If the requirements leaving this phase aren't testable, the whole downstream test pyramid inherits the fuzziness.

## What you do

- Map test cases to requirements — own the [test-to-requirement coverage map](artifacts/test-to-requirement-coverage-map.md)
- Pair with the BA on [testable acceptance criteria](artifacts/testable-acceptance-criteria.md) — push back on untestable language
- Pair with Security & Compliance on the [control-to-test coverage map](artifacts/control-to-test-coverage-map.md) — every control becomes a test

## Artifacts you own

- [test-to-requirement coverage map](artifacts/test-to-requirement-coverage-map.md) — requirement → planned test linkage

## Artifacts you contribute to

- [testable acceptance criteria](artifacts/testable-acceptance-criteria.md) — owned by the BA, you co-author to ensure each criterion is a test
- [control-to-test coverage map](artifacts/control-to-test-coverage-map.md) — owned by Security & Compliance, you co-author the test side

## Outcomes you drive

You don't drive outcomes this phase — you input into the BA's [approved requirements](outcomes/approved-requirements.md) through testability gates.

## Who you work with

- **Business Analyst** — primary partner; requirements without testable acceptance criteria get kicked back
- **Security & Compliance** — partners on mapping controls to tests
- **Developer** — their sizing picks up testing effort; you want them in the loop on how big test automation will be
- **Product Owner** — consumes your coverage view into MVP scope confidence

## Handoff into Design

In [Design](../3-design/README.md) you'll update test designs against the approved design, and by the time you get there the traceability you're setting up now becomes what you update. The quality bar is that every approved requirement has at least one planned test and no control is orphaned. You're done when a risk-based test strategy is sketch-able from your coverage maps, and when the BA's approved requirements don't include untestable "shoulds".

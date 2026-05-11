# testable acceptance criteria

_Produced by: Acceptance criteria authoring_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Business Analyst

**Stakeholders:** QA/Tester

## What this is

The unambiguous, observable conditions under which a requirement is considered done — typically written in Given / When / Then form, tied to requirement IDs, and pre-agreed with QA. "Testable" is the load-bearing word: if a criterion cannot be observed by a human or a test, it is not an acceptance criterion.

## Why it matters for the Business Analyst

You co-author these with QA so "done" means the same thing to PO, Dev, and Tester. Acceptance criteria are the device that turns requirements into executable tests — they are how you buy back weeks of Build-phase "that's not what I meant" arguments.

## Definition of Done

- [ ] Every acceptance criterion links to a requirement ID and has its own ID
- [ ] Each criterion is phrased in Given / When / Then (or equivalent) observable form
- [ ] Positive, negative, and edge cases are covered per requirement
- [ ] Data conditions, personas, and pre-state are specified
- [ ] Expected outcome includes a tolerance or threshold where performance is involved

## What it contains

- Requirement ID and linked acceptance criterion IDs
- Given / When / Then (or equivalent) phrasing
- Positive, negative, and edge cases
- Data conditions, personas, and pre-state
- Expected observable outcome with tolerance
- Coverage tags (functional, NFR, regulatory)

## Inputs you rely on

- [Requirements document](requirements-document.md) and [process models](process-models.md)
- [NFR document](nfr-document.md) for non-functional criteria
- [Business rules](../../3-design/artifacts/business-rules-catalog.md) drafts
- QA input on test feasibility and coverage strategy

## Who consumes it

- QA/Tester — builds test designs and automation against these
- Developer — uses as Definition-of-Done input
- Product Owner — uses for increment acceptance in Build
- Security & Compliance — traces [control-to-test coverage map](control-to-test-coverage-map.md) back to these

## Common pitfalls

- Soft language ("the system should feel fast") — unobservable, untestable
- Only happy-path criteria — misses the majority of defect surface
- Criteria written in isolation from QA, so they cannot be automated cost-effectively
- No tolerance or thresholds on performance criteria

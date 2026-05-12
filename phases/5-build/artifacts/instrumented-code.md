# instrumented code

_Produced by: Telemetry implementation_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** required — the MVP without telemetry is a prototype

## What this is

Feature code that emits the events, metrics, logs, and traces called for by the telemetry plan — correctly named, correctly tagged, and verified at test time. Not "we'll add logging later" — first-class output alongside functional code.

## Why it matters for the Developer

You are the author of the signal that SRE, QA, product analytics, and business reporting will rely on. Instrumenting up front is cheaper than retrofitting under incident pressure and is what makes your code observable — and therefore operable — from day one.

## Definition of Done

- [ ] Structured log statements cover the meaningful events in the telemetry plan
- [ ] Metrics are registered and emitted with correct labels and dimensions
- [ ] Trace spans wrap cross-service calls and critical units
- [ ] PII and classification handling matches policy
- [ ] Tests assert emission shape for the key signals

## What it contains

- Structured log statements at meaningful events
- Metrics registered and emitted with correct labels/dimensions
- Trace spans around cross-service calls and critical units
- PII/classification handling consistent with policy
- Sampling configuration where applicable
- Tests that assert emission shape (where practical)

## Inputs you rely on

- Telemetry plan and event catalog
- SLO and KPI definitions
- Data model and classification
- Logging and tracing libraries from the platform
- Correlation-ID conventions

## Who consumes it

- SRE — builds dashboards and alerts from emitted signals
- Business Analyst — maps events to KPI dashboards
- Customer Support — diagnoses issues with logs and traces
- Verified KPI telemetry artifact in Verify confirms emission against this output

## Common pitfalls

- Unstructured log lines that can't be queried reliably
- High-cardinality labels that explode metric costs
- Missing correlation IDs so traces don't join across services
- Logging secrets or PII in violation of data classification

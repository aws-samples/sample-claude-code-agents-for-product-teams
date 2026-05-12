# experiment results

_Produced by: A/B testing / experimentation_

**Business outcome supported:** close the loop — measure actual performance against the business case, decide continue/pivot/sunset, and feed validated learning back into Discover for the next cycle.

**Primary owner:** Product Owner

**Stakeholders:** Developer

**Accelerated MVP:** slim — a short writeup of what shipped and what moved is enough

## What this is

The results of A/B and multivariate experiments run on the live product — hypothesis, design, sample size, stat significance, and decision (ship, kill, iterate). A living record of what the team learned empirically.

## Why it matters for the Product Owner

Experimentation is how opinion loses to evidence. A disciplined results log converts experimentation from demo theater into a real decision-making machine — and the accumulated corpus teaches the team what generally works for this product and its customers.

## Definition of Done

- [ ] Each experiment records hypothesis and success metric
- [ ] Design, sample size, and duration are captured
- [ ] Results report effect size and confidence, including segment-level outcomes
- [ ] Decision (ship, kill, iterate) and rationale are stated
- [ ] Linked feature flags and release changes are referenced

## What it contains

- Hypothesis and success metric per experiment
- Experiment design, sample size, duration
- Results with effect size and confidence
- Segment-level outcomes
- Decision made and rationale
- Links to feature flags and release changes

## Inputs you rely on

- Telemetry plan and instrumented code
- Feature flag infrastructure from Plan
- Adoption metrics and KPI definitions
- User research and feedback insights (hypothesis seed)
- Analytics platform

## Who consumes it

- Product Owner — prioritization and roadmap
- UI/UX Designer — iterates on findings
- Business Analyst — feeds benefits analysis
- Next Discover cycle — validated patterns inform new bets

## Common pitfalls

- Peeking at data and stopping experiments early
- Running with under-powered samples; false positives dominate
- No kill criteria; indecisive experiments drag
- Results not generalized; every experiment starts from scratch

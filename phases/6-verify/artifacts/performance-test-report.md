# performance test report

_Produced by: Performance / load testing_

**Business outcome supported:** evidence-based readiness to launch — functional, non-functional, operational, and documentation — validated in production-like conditions.

**Primary owner:** QA/Tester

**Stakeholders:** Site Reliability Engineer, Architect

**Accelerated MVP:** slim — "can it handle the MVP cohort" is the test

## What this is

The outcome of load, stress, soak, and spike tests against the production-like environment — latency distributions, throughput, resource saturation, and failure-mode behavior versus the NFR and SLO targets.

## Why it matters for the QA/Tester

Perf is the NFR most likely to be defeated by launch-day traffic if not proven ahead. You own the credibility of the test design, the realism of the workload, and the clear read-out that the Architect and SRE can act on before the window closes.

## Definition of Done

- [ ] Workload model is described with its derivation from expected production traffic
- [ ] Latency percentiles are reported per critical journey
- [ ] Throughput and saturation curves are included
- [ ] Observed failure modes at breaking point and comparison to NFR/SLO targets are documented
- [ ] Bottlenecks identified have remediation state recorded

## What it contains

- Workload model and derivation from expected production traffic
- Latency percentiles per critical journey
- Throughput and saturation curves
- Observed failure modes at breaking point
- Comparison to NFR targets and SLOs
- Bottlenecks identified and remediation state

## Inputs you rely on

- NFR document and service-level objectives
- Validated staging environment sized close to prod
- Telemetry and monitoring per telemetry plan
- Expected traffic forecast from PO/Sales & Marketing
- Test plan and perf-test scripts

## Who consumes it

- Architect — validates architectural assumptions and sizing
- SRE — calibrates capacity, autoscaling, and alerting
- Release Manager — gates on NFR pass
- Product Sponsor — includes in launch-risk acceptance

## Common pitfalls

- Synthetic workload that doesn't resemble real traffic
- Staging smaller than prod — results read as a lower bound only
- Reporting averages instead of tail latencies where user pain lives
- Testing happy path only — no headroom or failure-mode signal

# provisioned environments

_Produced by: Infrastructure / environment provisioning_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

## What this is

Working dev, test, staging, and prod environments — provisioned as code, with network, IAM, data, observability, and secrets wiring in place. The record captures what exists, how it was built, and how to rebuild it.

## Why it matters for the SRE

"Works in dev, broken in staging" kills velocity and hides NFR defects until the worst possible moment. Production-parity environments under IaC are how you give engineering fast, reproducible feedback while keeping cost, security, and drift under control from day one.

## Definition of Done

- [ ] Environment inventory lists every tier (dev, CI, staging, prod, sandbox/demo)
- [ ] IaC repo links and module versions are captured per environment
- [ ] Network, DNS, and IAM posture are documented per environment
- [ ] Secrets and config management approach is specified
- [ ] Observability agents, log routing, and alert endpoints are installed
- [ ] Cost guardrails and auto-teardown policies are defined for ephemeral environments

## What it contains

- Environment inventory (dev, CI, staging, prod, any sandbox/demo tier)
- IaC repo links and module versions that produced each environment
- Network, DNS, and IAM posture per environment
- Secrets and config management approach
- Observability agents, log routing, and alert endpoints installed
- Cost guardrails and auto-teardown policies for ephemeral environments

## Inputs you rely on

- Architecture document and integration map
- Security control requirements and data classification
- NFR document — drives staging sizing and data shape
- Enterprise platform standards (landing zones, approved regions)
- Cost estimates from the budget baseline

## Who consumes it

- Developers — deploy to dev/CI and debug against staging
- QA/Tester — runs test campaigns in staging and verify environments
- Release Manager — promotes through the environment chain
- Security & Compliance — audits posture against control requirements

## Common pitfalls

- Staging that "looks like prod" but differs in scale, data, or network so load tests lie
- Click-ops fixes that drift from IaC — changes can't be reproduced or rolled forward
- Forgotten dev environments racking up cloud spend
- Missing observability in lower environments so problems are only visible in prod

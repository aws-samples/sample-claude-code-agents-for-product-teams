# working CI/CD pipeline

_Produced by: CI/CD pipeline setup_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** Developer

## What this is

A functional, trusted pipeline that takes a commit from main through build, test, security scanning, artifact signing, and promotion to each environment — with the stages, gates, and triggers documented.

## Why it matters for the SRE

Pipeline quality is velocity. A flaky or slow pipeline turns every PR into a guessing game and drives engineers to merge around the process. You set up a reliable, secure pipeline in Plan so Build-phase engineering gets minutes-not-hours feedback and Release Manager inherits a trustworthy promotion path.

## Definition of Done

- [ ] Stage definitions (build, unit, integration, SAST/SCA, artifact publish, deploy) are documented
- [ ] Trigger model per branch/environment (PR, merge, tag, scheduled) is specified
- [ ] Quality gates (coverage thresholds, vuln severity, test results) are defined
- [ ] Artifact signing and provenance (SBOM, attestations) are configured
- [ ] Promotion strategy across environments is described
- [ ] Pipeline observability and MTTR for pipeline failures are captured

## What it contains

- Stage definitions (build, unit, integration, SAST/SCA, artifact publish, deploy)
- Trigger model (PR, merge, tag, scheduled) per branch/environment
- Quality gates (coverage thresholds, vuln severity, test results)
- Artifact signing and provenance (SBOM, attestations)
- Promotion strategy across environments
- Pipeline observability and MTTR for pipeline failures

## Inputs you rely on

- Provisioned environments and deployment targets
- Pipeline security controls from Security & Compliance
- Test plan — stages align to test strategy
- Changelog review process for merge gating
- Developer feedback on acceptable cycle time

## Who consumes it

- Developers — push code and consume pipeline feedback hundreds of times a week
- Release Manager — uses the pipeline to execute releases
- Security & Compliance — audits scan gates and evidence capture
- QA/Tester — hooks automated suites into stages

## Common pitfalls

- Slow or flaky pipelines that teams work around by merging without signal
- Security gates bolted on late and bypassed under deadline pressure
- No supply-chain controls — unsigned artifacts, unverified dependencies
- Pipeline-as-code that isn't itself reviewed, versioned, or tested

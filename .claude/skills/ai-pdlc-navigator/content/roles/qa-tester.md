# 10. QA / Tester
- **Description:** Provides evidence-based confidence in quality; plans testing, designs/automates tests, runs exploratory sessions, manages risks.
- **Business purpose:** Reduces the risk of defects reaching customers.
- **Typically reports to:** Head of Quality Engineering, or Engineering Manager (embedded model).
- **Project goals:** Risk-based coverage · trusted regression suite · defects caught pre-release · traceability requirements → tests → results.


## AI teammate

**Purpose:** Provide evidence-based confidence in quality — design and automate risk-based tests, keep traceability current, and surface where coverage or stability is weak before release.

**Assistive AI (tight collaboration):** Drafts and iterates on the [test-to-requirement coverage map](../phases/2-define/artifacts/test-to-requirement-coverage-map.md), [design-aligned test designs](../phases/3-design/artifacts/design-aligned-test-designs.md), [test plan](../phases/4-plan/artifacts/test-plan.md), [performance test report](../phases/6-verify/artifacts/performance-test-report.md), [accessibility audit report](../phases/6-verify/artifacts/accessibility-audit-report.md), [readiness assessment](../phases/6-verify/artifacts/readiness-assessment.md), [triaged UAT defects](../phases/6-verify/artifacts/triaged-uat-defects.md), [production validation](../phases/7-launch/artifacts/production-validation.md), and [bug reports](../phases/9-iterate/artifacts/bug-reports.md) with a human QA engineer holding the pen — risk-based planning, exploratory charters, defect root-cause hypothesis.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can generate and maintain the [automated test suite](../phases/5-build/artifacts/automated-test-suite.md) from spec and requirement changes and keep the [integration test results](../phases/5-build/artifacts/integration-test-results.md) and [regression test results](../phases/6-verify/artifacts/regression-test-results.md) flowing through CI, with flakiness detection and quarantine. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not own the [UAT/beta sign-off](../phases/6-verify/outcomes/uat-beta-sign-off.md) outside of aggregating evidence — the human tester signs. Does not set SLOs or approve the [PRR sign-off](../phases/6-verify/outcomes/prr-sign-off.md). Does not approve the [security test report](../phases/6-verify/artifacts/security-test-report.md) (Security-owned) or [resilience test results](../phases/6-verify/artifacts/resilience-test-results.md) (SRE-owned) — contributes evidence.

**Inputs:** [Requirements document](../phases/2-define/artifacts/requirements-document.md), [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md), [approved design package](../phases/3-design/outcomes/approved-design-package.md), [API specification](../phases/3-design/artifacts/api-specification.md), [NFR document](../phases/2-define/artifacts/nfr-document.md), [control-to-test coverage map](../phases/2-define/artifacts/control-to-test-coverage-map.md), CI/CD signals, and incoming defect streams.

**Outputs:** The A artifacts above, live CI-integrated test suites, coverage/gap reports, flakiness analysis, and first-pass root-cause hypotheses for the defect queue.

**Escalation triggers:**
- Test reveals production data corruption risk, PII leak, or security regression.
- Coverage gap detected in a regulated or safety-critical path.
- Regression suite unstable (flake rate) above the team's trust threshold.
- Acceptance-criteria ambiguity detected during test design.
- Performance or accessibility threshold breached in an SLA-bound workflow.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Verify exit checklist](../phases/6-verify/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your test-management tool**, shape a risk-based [test plan](../phases/4-plan/artifacts/test-plan.md): propose risks, map coverage against the [test-to-requirement coverage map](../phases/2-define/artifacts/test-to-requirement-coverage-map.md), and iterate on [design-aligned test designs](../phases/3-design/artifacts/design-aligned-test-designs.md) before review.
- **In your exploratory / session tooling**, design exploratory charters and interpret session results for the [readiness assessment](../phases/6-verify/artifacts/readiness-assessment.md) — where to focus next, what was under-covered.
- **In your performance and accessibility tools**, reason about realistic load scenarios, thresholds, and user-impact severity for the [performance test report](../phases/6-verify/artifacts/performance-test-report.md) and [accessibility audit report](../phases/6-verify/artifacts/accessibility-audit-report.md).
- **In your defect tracker**, triage and root-cause complex defects: pattern-match across the [triaged UAT defects](../phases/6-verify/artifacts/triaged-uat-defects.md) queue and prior [bug reports](../phases/9-iterate/artifacts/bug-reports.md) to spot related clusters.
- **In your test-management tool**, synthesize UAT session notes into structured evidence for [UAT/beta sign-off](../phases/6-verify/outcomes/uat-beta-sign-off.md).

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your test-automation framework**, generate unit, integration, and regression tests from spec and requirement changes; feed the [automated test suite](../phases/5-build/artifacts/automated-test-suite.md) and keep the [integration test results](../phases/5-build/artifacts/integration-test-results.md) and [regression test results](../phases/6-verify/artifacts/regression-test-results.md) flowing through CI.
- **In your test-automation framework**, flakiness detection, test quarantine, and root-cause suggestions for unstable tests.
- **In your test-management tool**, keep the [test-to-requirement coverage map](../phases/2-define/artifacts/test-to-requirement-coverage-map.md) live as requirements and tests change; surface gaps and orphaned tests.
- **In your defect tracker**, cluster and de-duplicate incoming defects, enrich with reproduction context, and route to the right owner; keep the [bug reports](../phases/9-iterate/artifacts/bug-reports.md) queue tidy.
- **In your performance and accessibility tools**, run nightly performance and accessibility suites on an automated schedule and report trend deltas.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **13** artifacts/outcomes as primary (A) and co-own **8** (R)._

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [testable acceptance criteria](../phases/2-define/artifacts/testable-acceptance-criteria.md) | Acceptance criteria authoring |
| **R** | [control-to-test coverage map](../phases/2-define/artifacts/control-to-test-coverage-map.md) | Map security controls to test cases |
| **A** | [test-to-requirement coverage map](../phases/2-define/artifacts/test-to-requirement-coverage-map.md) | Map test cases to requirements |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [design-aligned test designs](../phases/3-design/artifacts/design-aligned-test-designs.md) | Update test designs against approved design |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [test plan](../phases/4-plan/artifacts/test-plan.md) | Test strategy |
| **R** | [security test plan](../phases/4-plan/artifacts/security-test-plan.md) | Security test plan contribution |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [automated test suite](../phases/5-build/artifacts/automated-test-suite.md) | Develop tests |
| **A** | [integration test results](../phases/5-build/artifacts/integration-test-results.md) | Integration testing |
| **R** | [requirements questions log](../phases/5-build/artifacts/requirements-questions-log.md) | Raise requirements questions & impediments |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [security test report](../phases/6-verify/artifacts/security-test-report.md) | Security testing / pen test |
| **R** | [resilience test results](../phases/6-verify/artifacts/resilience-test-results.md) | Chaos / resilience testing |
| **A** | [readiness assessment](../phases/6-verify/artifacts/readiness-assessment.md) | Assess feature readiness |
| **A** | [UAT/beta sign-off](../phases/6-verify/outcomes/uat-beta-sign-off.md) | Pre-launch validation — UAT / beta |
| **A** | [performance test report](../phases/6-verify/artifacts/performance-test-report.md) | Performance / load testing |
| **A** | [accessibility audit report](../phases/6-verify/artifacts/accessibility-audit-report.md) | Accessibility testing |
| **A** | [regression test results](../phases/6-verify/artifacts/regression-test-results.md) | Regression testing |
| **R** | [validated staging environment](../phases/6-verify/artifacts/validated-staging-environment.md) | Staging deployment & smoke tests |
| **R** | [verified docs](../phases/6-verify/artifacts/verified-docs.md) | Documentation review |
| **A** | [triaged UAT defects](../phases/6-verify/artifacts/triaged-uat-defects.md) | UAT defect triage |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [production validation](../phases/7-launch/artifacts/production-validation.md) | Post-deploy production smoke tests |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [bug reports](../phases/9-iterate/artifacts/bug-reports.md) | Document bugs with reproduction details |

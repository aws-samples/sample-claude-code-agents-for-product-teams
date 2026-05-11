# 6. Security & Compliance
- **Description:** Embeds security and regulatory controls across the PDLC; runs threat modeling, AppSec tooling, audits, and incident response.
- **Business purpose:** Protects the org, customers, and regulated data; keeps the company shippable under its legal obligations.
- **Typically reports to:** CISO / VP Security (in Engineering, Risk, or Legal/Compliance org).
- **Project goals:** No critical/high vulns shipped · audit evidence without blocking delivery · measurable reduction in recurring vuln classes.


## AI teammate

**Purpose:** Embed security and regulatory controls across the PDLC so the org stays shippable under its legal obligations while producing audit evidence without blocking delivery.

**Assistive AI (tight collaboration):** Drafts and iterates on the [regulatory risk flag](../phases/1-discover/artifacts/regulatory-risk-flag.md), [data-sensitivity flag](../phases/1-discover/artifacts/data-sensitivity-flag.md), [applicable-regulations list](../phases/2-define/artifacts/applicable-regulations-list.md), [security control requirements](../phases/2-define/artifacts/security-control-requirements.md), [control-to-test coverage map](../phases/2-define/artifacts/control-to-test-coverage-map.md), [privacy impact assessment](../phases/2-define/artifacts/privacy-impact-assessment.md), [threat model](../phases/3-design/artifacts/threat-model.md), [vendor risk assessment](../phases/3-design/artifacts/vendor-risk-assessment.md), [security test plan](../phases/4-plan/artifacts/security-test-plan.md), [pipeline security controls](../phases/4-plan/artifacts/pipeline-security-controls.md), [evidence collection plan](../phases/4-plan/artifacts/evidence-collection-plan.md), [IR plan & runbook](../phases/4-plan/artifacts/ir-plan-runbook.md), [security incident postmortems](../phases/8-operate/artifacts/security-incident-postmortems.md), [security posture report](../phases/9-iterate/artifacts/security-posture-report.md), and [regulatory change impact](../phases/9-iterate/artifacts/regulatory-change-impact.md) with a human security engineer holding the pen — attack-surface exploration, jurisdiction-specific reasoning, edge-case surfacing.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can produce the [vulnerability scan report](../phases/5-build/artifacts/vulnerability-scan-report.md) and [triaged vulnerabilities](../phases/5-build/artifacts/triaged-vulnerabilities.md) queue from continuous scanning, feed the [security test report](../phases/6-verify/artifacts/security-test-report.md), enrich and correlate [security monitoring alerts](../phases/8-operate/artifacts/security-monitoring-alerts.md), run recurring [access review results](../phases/8-operate/artifacts/access-review-results.md), patch routine CVEs into the [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md) flow, and gather [audit evidence](../phases/8-operate/artifacts/audit-evidence.md) and first-draft [audit report / attestation](../phases/8-operate/artifacts/audit-report-attestation.md) from source systems. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not give [security/compliance approval](../phases/3-design/outcomes/security-compliance-approval.md), [compliance go/no-go](../phases/6-verify/outcomes/compliance-go-no-go.md), [legal approval](../phases/7-launch/outcomes/legal-approval.md), [ratified risk decisions](../phases/3-design/outcomes/ratified-risk-decisions.md), or [confirmed data classification](../phases/2-define/outcomes/confirmed-data-classification.md) — these are human sign-off outcomes for which AI prepares the package. Does not accept security risk, decide jurisdiction-specific legal interpretation, or approve [approved incident comms](../phases/8-operate/outcomes/approved-incident-comms.md).

**Inputs:** [Data inventory & classification](../phases/2-define/artifacts/data-inventory-classification.md), [NFR document](../phases/2-define/artifacts/nfr-document.md), [architecture document](../phases/3-design/artifacts/architecture-document.md), [integration map](../phases/3-design/artifacts/integration-map.md), [API specification](../phases/3-design/artifacts/api-specification.md), source-code and dependency scans, SIEM signals, regulator feeds.

**Outputs:** The A artifacts above, audit-evidence flow, scan-and-triage outputs, and the [regulatory change impact](../phases/9-iterate/artifacts/regulatory-change-impact.md) watch.

**Escalation triggers:**
- Critical/High CVE in a production-path component or supply-chain compromise indicator.
- Regulated data (PII, PHI, financial, regulated telemetry) crosses a new boundary or jurisdiction.
- Control gap or failed evidence on a control required for a live attestation scope.
- Active security incident at Sev-2 or above, or suspected data exfiltration.
- Regulatory change that alters the obligations in the [applicable-regulations list](../phases/2-define/artifacts/applicable-regulations-list.md).

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Verify exit checklist](../phases/6-verify/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your threat-modeling tool**, explore attack surfaces for the [threat model](../phases/3-design/artifacts/threat-model.md); propose candidates for the [approved security patterns](../phases/3-design/outcomes/approved-security-patterns.md) and counter-examples you may have missed.
- **In your GRC platform**, map regulations to controls and derive the [security control requirements](../phases/2-define/artifacts/security-control-requirements.md) and [control-to-test coverage map](../phases/2-define/artifacts/control-to-test-coverage-map.md) from the [applicable-regulations list](../phases/2-define/artifacts/applicable-regulations-list.md); stress-test the [evidence collection plan](../phases/4-plan/artifacts/evidence-collection-plan.md).
- **In your AppSec / policy repository**, draft and revise the [IR plan & runbook](../phases/4-plan/artifacts/ir-plan-runbook.md) and synthesize [security incident postmortems](../phases/8-operate/artifacts/security-incident-postmortems.md); frame analysis for the [regulatory change impact](../phases/9-iterate/artifacts/regulatory-change-impact.md).
- **In your privacy / DPIA tooling**, work through the [privacy impact assessment](../phases/2-define/artifacts/privacy-impact-assessment.md) and [confirmed data classification](../phases/2-define/outcomes/confirmed-data-classification.md) — jurisdiction-specific reasoning and edge-case surfacing.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your SAST / SCA / DAST scanners**, continuous scanning of code and dependencies with risk-scored triage producing the [vulnerability scan report](../phases/5-build/artifacts/vulnerability-scan-report.md), [triaged vulnerabilities](../phases/5-build/artifacts/triaged-vulnerabilities.md) queue, and inputs to the [security test report](../phases/6-verify/artifacts/security-test-report.md); alert on SLA breaches.
- **In your SIEM / security monitoring**, enrich and correlate [security monitoring alerts](../phases/8-operate/artifacts/security-monitoring-alerts.md) into actionable cases; suppress known-benign noise; escalate what matters.
- **In your GRC platform**, continuously gather [audit evidence](../phases/8-operate/artifacts/audit-evidence.md) from source systems against the [evidence collection plan](../phases/4-plan/artifacts/evidence-collection-plan.md); draft the [audit report / attestation](../phases/8-operate/artifacts/audit-report-attestation.md) for your review.
- **In your secrets-management / PAM**, run recurring access reviews and produce [access review results](../phases/8-operate/artifacts/access-review-results.md) with flagged anomalies.
- **Across dependency registries and your AppSec / policy repository**, patch routine CVEs in the [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md) flow behind CI gates; monitor regulatory feeds for changes worth routing into [regulatory change impact](../phases/9-iterate/artifacts/regulatory-change-impact.md).

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **28** artifacts/outcomes as primary (A) and co-own **5** (R)._

### [1. Discover](../phases/1-discover/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [regulatory risk flag](../phases/1-discover/artifacts/regulatory-risk-flag.md) | Initial regulatory landscape scan |
| **A** | [data-sensitivity flag](../phases/1-discover/artifacts/data-sensitivity-flag.md) | Data sensitivity early read |

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [applicable-regulations list](../phases/2-define/artifacts/applicable-regulations-list.md) | Regulatory / compliance scope assessment |
| **A** | [security control requirements](../phases/2-define/artifacts/security-control-requirements.md) | Security & compliance requirements derivation |
| **A** | [control-to-test coverage map](../phases/2-define/artifacts/control-to-test-coverage-map.md) | Map security controls to test cases |
| **A** | [privacy impact assessment](../phases/2-define/artifacts/privacy-impact-assessment.md) | Privacy / DPIA assessment |
| **A** | [confirmed data classification](../phases/2-define/outcomes/confirmed-data-classification.md) | Data classification confirmation |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [ratified risk decisions](../phases/3-design/outcomes/ratified-risk-decisions.md) | Risk appetite ratification |
| **A** | [threat model](../phases/3-design/artifacts/threat-model.md) | Threat modeling |
| **A** | [approved security patterns](../phases/3-design/outcomes/approved-security-patterns.md) | Secure design pattern selection |
| **A** | [security/compliance approval](../phases/3-design/outcomes/security-compliance-approval.md) | Security & compliance review |
| **R** | [design-requirements validation](../phases/3-design/artifacts/design-requirements-validation.md) | Validate design against requirements |
| **A** | [vendor risk assessment](../phases/3-design/artifacts/vendor-risk-assessment.md) | Vendor security & compliance assessment |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [security test plan](../phases/4-plan/artifacts/security-test-plan.md) | Security test plan contribution |
| **A** | [pipeline security controls](../phases/4-plan/artifacts/pipeline-security-controls.md) | Define security & compliance controls in pipeline |
| **A** | [evidence collection plan](../phases/4-plan/artifacts/evidence-collection-plan.md) | Compliance evidence plan |
| **A** | [IR plan & runbook](../phases/4-plan/artifacts/ir-plan-runbook.md) | Incident response plan |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [vulnerability scan report](../phases/5-build/artifacts/vulnerability-scan-report.md) | Security scanning (SAST/SCA) |
| **A** | [triaged vulnerabilities](../phases/5-build/artifacts/triaged-vulnerabilities.md) | Vulnerability triage & remediation SLA tracking |
| **R** | [reviewed code](../phases/5-build/artifacts/reviewed-code.md) | Code review |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [approved known-issues & risk acceptance](../phases/6-verify/outcomes/approved-known-issues-risk-acceptance.md) | Approve launch risk posture |
| **A** | [security test report](../phases/6-verify/artifacts/security-test-report.md) | Security testing / pen test |
| **R** | [readiness assessment](../phases/6-verify/artifacts/readiness-assessment.md) | Assess feature readiness |
| **A** | [compliance go/no-go](../phases/6-verify/outcomes/compliance-go-no-go.md) | Compliance readiness review |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [legal approval](../phases/7-launch/outcomes/legal-approval.md) | Legal & compliance final sign-off |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [audit evidence](../phases/8-operate/artifacts/audit-evidence.md) | Compliance audit evidence collection |
| **A** | [patched dependencies](../phases/8-operate/artifacts/patched-dependencies.md) | Security patching |
| **A** | [security monitoring alerts](../phases/8-operate/artifacts/security-monitoring-alerts.md) | Security monitoring & SIEM operations |
| **A** | [security incident postmortems](../phases/8-operate/artifacts/security-incident-postmortems.md) | Security incident response |
| **A** | [audit report / attestation](../phases/8-operate/artifacts/audit-report-attestation.md) | Periodic compliance audit |
| **A** | [access review results](../phases/8-operate/artifacts/access-review-results.md) | Access reviews |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [security posture report](../phases/9-iterate/artifacts/security-posture-report.md) | Security posture review |
| **A** | [regulatory change impact](../phases/9-iterate/artifacts/regulatory-change-impact.md) | Regulatory change monitoring |

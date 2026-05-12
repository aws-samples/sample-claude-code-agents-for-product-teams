# security monitoring alerts

_Produced by: Security monitoring & SIEM operations_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Security & Compliance

**Stakeholders:** Site Reliability Engineer

**Accelerated MVP:** required when data-sensitive; otherwise slim to platform defaults

## What this is

The detection rules and alert stream from SIEM, EDR, CSPM, WAF, and identity platforms — tuned to catch abuse, intrusion, misconfiguration, and data-exfiltration patterns relevant to this product. Paged to the security on-call, not broadcast.

## Why it matters for the Security & Compliance team

Detection is the difference between a contained event and a breach. Well-tuned alerts keep the signal-to-noise ratio high enough for the team to actually respond; noisy ones lead to ignored pages and delayed containment — exactly how disasters happen.

## Definition of Done

- [ ] Every alert rule has severity and routing defined.
- [ ] Active alerts carry a current triage state.
- [ ] False-positive rate and tuning history are tracked per rule.
- [ ] Detection coverage is mapped against the threat model.
- [ ] Each alert class has a playbook and integration status is recorded for SIEM/EDR/identity/WAF.

## What it contains

- Alert rules, severities, and routing
- Triage state for active alerts
- False-positive rate per rule and tuning history
- Detection coverage mapped to threat model
- Playbooks per alert class
- Integration status with SIEM, EDR, identity, WAF

## Inputs you rely on

- Threat model and applicable-regulations list
- Telemetry plan and instrumented code
- Vendor detection rules and threat intel feeds
- Previous security incident postmortems
- Access review results (abnormal-access detection)

## Who consumes it

- Security on-call — investigates alerts
- SRE — coordinates when alerts overlap with reliability events
- Security incident postmortems — evaluates detection effectiveness
- Audit — coverage evidence

## Common pitfalls

- Rules copied from vendor defaults without tuning to the product
- No playbook per alert — responder re-derives every time
- False-positive rate never reviewed; alert fatigue dulls response
- Detection gaps vs. threat model never measured

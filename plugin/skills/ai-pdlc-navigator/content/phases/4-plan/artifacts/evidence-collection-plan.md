# evidence collection plan

_Produced by: Compliance evidence plan_

**Business outcome supported:** stand up the team, environments, pipeline, test strategy, SLOs, and work-ready backlog so engineering can begin productively on day one.

**Primary owner:** Security & Compliance

**Stakeholders:** _(none listed)_

## What this is

The plan for which compliance controls need evidenced, what evidence satisfies each, where it's produced, and how it's captured and retained — so audits (internal or external) don't turn into archaeology.

## Why it matters for the Security & Compliance owner

You're measured on audit evidence without blocking delivery. Planning evidence collection now — while the pipeline and controls are being built — means the evidence flows automatically as a by-product of normal work rather than becoming a last-minute manual scramble that stalls releases.

## Definition of Done

- [ ] Each control lists evidence requirements (what, how often, who produces)
- [ ] Source system is named per evidence stream
- [ ] Retention period and storage location are specified per evidence type
- [ ] Automation status is marked per control, with a gap plan where manual
- [ ] Evidence review cadence and sign-off are defined
- [ ] Audit-export format and responsible party are captured

## What it contains

- Control-by-control evidence requirements (what, how often, who produces)
- Source system for each evidence stream (pipeline, identity, cloud, ticket data)
- Retention period and storage location per evidence type
- Automation status — which is automatic, which is manual, gap plan
- Evidence review cadence and sign-off
- Audit-export format and responsible party

## Inputs you rely on

- Applicable regulations list and security control requirements
- Pipeline security controls
- Working CI/CD pipeline and provisioned environments
- Existing GRC or evidence-management tooling
- Audit-scheme requirements (SOC2, ISO, PCI, HIPAA)

## Who consumes it

- Internal auditors — map evidence to controls during audits
- External auditors and customers — receive compiled evidence packages
- Developers and SRE — know which artifacts must be preserved
- Release Manager — gates releases on required evidence

## Common pitfalls

- Evidence spread across 20 tools with no index — audit becomes a hunt
- Collecting everything but mapped to nothing — no auditor can use it
- Manual evidence gathering that decays as staff turns over
- Retention policies that violate privacy or data-classification constraints

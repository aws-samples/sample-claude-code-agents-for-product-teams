# DR test results

_Produced by: Backup & disaster-recovery testing_

**Business outcome supported:** run a stable, SLO-meeting service while growing a profitable, retained customer base — the commercial engine of the product.

**Primary owner:** Site Reliability Engineer

**Stakeholders:** _(none listed)_

## What this is

The evidence from periodic disaster-recovery and backup-restoration exercises — actual RTO/RPO measured against target, procedural gaps found, and remediation taken. Not a theoretical review; a live drill.

## Why it matters for the SRE

Backups and DR plans are Schrödinger's artifacts until tested. A documented, rehearsed, measured DR capability is a prerequisite for most enterprise contracts, many compliance regimes, and any serious claim about business continuity.

## Definition of Done

- [ ] Test scope (service, region, dataset) is explicitly stated.
- [ ] Measured RTO and RPO are reported against target.
- [ ] Step-by-step observations and any deviations from the runbook are logged.
- [ ] Data integrity is verified after restore.
- [ ] Defects found have a remediation plan and the next test is scheduled.

## What it contains

- Scope of the test (service, region, dataset)
- Measured RTO and RPO vs. target
- Step-by-step observations and deviations
- Data integrity verification after restore
- Defects found and remediation plan
- Next test schedule

## Inputs you rely on

- IR plan & runbook
- Backup configuration and inventory
- Architecture document (especially cross-region design)
- Previous DR test results (trend)
- Compliance requirements that mandate testing frequency

## Who consumes it

- Security & Compliance — audit evidence
- Architect — feeds scale-readiness report and architecture updates
- Sponsor — operational performance review
- Enterprise sales and deal teams — customer due diligence answers

## Common pitfalls

- Tabletop only — no real restore exercised
- Restoring to a fresh environment that isn't representative of production
- Passing RTO but failing data-integrity checks silently
- Tests performed but results never documented for audit

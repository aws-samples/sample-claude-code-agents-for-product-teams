# dependency list

_Produced by: Dependency mapping_

**Business outcome supported:** turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model, with sized estimates ready to plan.

**Primary owner:** Architect

**Stakeholders:** Project Manager

## What this is

The register of everything the initiative depends on being true, delivered, or available — other teams' outputs, vendor commitments, platform capabilities, regulatory approvals, contract signatures — with owners, dates, and contingency posture.

## Why it matters for the Architect

You produce this — with the PM — because unmanaged dependencies are the top reason delivery dates slip. Making them explicit and owner-assigned moves them from "surprise" to "managed risk" and gives the PM something concrete to chase.

## Definition of Done

- [ ] Each dependency has an ID, title, and type
- [ ] Every dependency names a specific internal owner and counterpart, not a team
- [ ] Each entry states a need-by date with current confidence
- [ ] Each dependency specifies what the initiative cannot progress past without it
- [ ] Each dependency carries a fallback or contingency statement

## What it contains

- Dependency ID, title, type (team, vendor, platform, legal, data)
- Internal or external owner and their named counterpart
- Need-by date and current confidence
- What the initiative cannot progress past without it
- Fallback or contingency if the dependency slips
- Link to the requirement(s) that need it

## Inputs you rely on

- [System-to-process map](system-to-process-map.md) and [capability gap report](capability-gap-report.md)
- Portfolio and platform roadmaps for upstream commitments
- Vendor contracts and SLAs
- [Applicable-regulations list](applicable-regulations-list.md) for regulatory dependencies

## Who consumes it

- Project Manager — drives it into the RAID log and escalation in Plan and Build
- Product Sponsor — uses it for air-cover and cross-portfolio unblocks
- Architect (future you) — refines dependencies as design detail lands
- Release Manager — sequences integration testing around critical dependencies

## Common pitfalls

- Vague owners — "Platform team" rather than a named person
- Missing external legal / procurement dependencies until they bite
- No contingency column, so a slip becomes a stop
- Static register — confidence and dates must be re-scored weekly in Build

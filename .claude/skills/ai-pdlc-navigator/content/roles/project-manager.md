# 8. Project Manager (Delivery)
- **Description:** Owns the "how and when" of delivery; plans scope/schedule/budget, manages cross-team dependencies, tracks risks and changes.
- **Business purpose:** Predictable delivery of cross-functional initiatives against a baselined plan.
- **Typically reports to:** Head of PMO / Director of Program Management.
- **Project goals:** On-time/on-budget delivery · early dependency resolution · transparent risk management · clean closure.


## AI teammate

**Purpose:** Own the "how and when" of delivery — keep plan, risks, dependencies, and comms current so cross-functional initiatives deliver predictably against a baselined plan.

**Assistive AI (tight collaboration):** Drafts and iterates on the [initial project brief](../phases/1-discover/artifacts/initial-project-brief.md), [charter draft](../phases/2-define/artifacts/charter-draft.md), [draft project schedule](../phases/2-define/artifacts/draft-project-schedule.md), [iteration plan](../phases/4-plan/artifacts/iteration-plan.md), [resource schedule](../phases/4-plan/artifacts/resource-schedule.md), [risk register](../phases/4-plan/artifacts/risk-register.md), [RAID log](../phases/4-plan/artifacts/raid-log.md) and [updated RAID log](../phases/5-build/artifacts/updated-raid-log.md), [change control package](../phases/5-build/artifacts/change-control-package.md), [retrospective report](../phases/9-iterate/artifacts/retrospective-report.md), and [lessons-learned repository](../phases/9-iterate/artifacts/lessons-learned-repository.md) with a human PM holding the pen — replanning scenarios, risk workshops, change trade-off analysis.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can produce the recurring [weekly/biweekly status report](../phases/5-build/artifacts/weekly-biweekly-status-report.md), [budget burn report](../phases/5-build/artifacts/budget-burn-report.md), and [launch-readiness status pack](../phases/6-verify/artifacts/launch-readiness-status-pack.md) from source data, keep the [governance calendar](../phases/4-plan/artifacts/governance-calendar.md) current, and assemble the [closed project & archive](../phases/9-iterate/artifacts/closed-project-archive.md) at project close for your sign-off. Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not approve the [baselined schedule & budget commitment](../phases/4-plan/outcomes/baselined-schedule-budget-commitment.md), [scope-change decisions](../phases/5-build/outcomes/scope-change-decisions.md), [go/no-go decision](../phases/7-launch/outcomes/go-no-go-decision.md), or [escalation policy](../phases/4-plan/outcomes/escalation-policy.md) — Sponsor-owned. Does not accept increments or arbitrate product priority.

**Inputs:** [Aligned leadership team](../phases/1-discover/outcomes/aligned-leadership-team.md), [dependency list](../phases/2-define/artifacts/dependency-list.md), [effort estimates](../phases/2-define/artifacts/effort-estimates.md), [stakeholder map](../phases/1-discover/artifacts/stakeholder-map.md), source signals from work-tracking, source control, PPM, and RAID tools; meeting transcripts.

**Outputs:** The A artifacts above, plus [design-phase plan](../phases/3-design/artifacts/design-phase-plan.md), [stakeholder workshop outcomes](../phases/2-define/artifacts/stakeholder-workshop-outcomes.md), [decision log from design reviews](../phases/3-design/outcomes/decision-log-from-design-reviews.md), [cross-team sync notes](../phases/5-build/artifacts/cross-team-sync-notes.md), [executed launch comms](../phases/7-launch/artifacts/executed-launch-comms.md), [launch run-of-show](../phases/7-launch/artifacts/launch-run-of-show.md), and [steady-state operating handoff](../phases/8-operate/outcomes/steady-state-operating-handoff.md).

**Escalation triggers:**
- Schedule slip or budget burn crosses the Sponsor-defined threshold.
- Cross-team dependency blocked and at risk of missing a named milestone.
- Risk promoted to Red, or realized issue with customer or regulatory impact.
- Scope change that requires a formal [change control package](../phases/5-build/artifacts/change-control-package.md).
- Vendor deliverable fails acceptance or triggers a contract issue.

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Plan exit checklist](../phases/4-plan/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your work-tracking / PPM tool**, explore replanning scenarios against the [draft project schedule](../phases/2-define/artifacts/draft-project-schedule.md) and [iteration plan](../phases/4-plan/artifacts/iteration-plan.md) — what shifts if a dependency slips, what the critical path becomes, how the [resource schedule](../phases/4-plan/artifacts/resource-schedule.md) must flex.
- **In your RAID / risk tool**, facilitate risk workshops and stress-test mitigations; draft entries for the [risk register](../phases/4-plan/artifacts/risk-register.md), [RAID log](../phases/4-plan/artifacts/raid-log.md), and [updated RAID log](../phases/5-build/artifacts/updated-raid-log.md).
- **In your change-request tool**, think through cost/schedule/scope trade-offs for a [change control package](../phases/5-build/artifacts/change-control-package.md) before proposing [scope-change decisions](../phases/5-build/outcomes/scope-change-decisions.md).
- **In your shared drive / wiki**, draft the [charter draft](../phases/2-define/artifacts/charter-draft.md), [governance briefing](../phases/5-build/artifacts/governance-briefing.md), and synthesize the [retrospective report](../phases/9-iterate/artifacts/retrospective-report.md) and [lessons-learned repository](../phases/9-iterate/artifacts/lessons-learned-repository.md).

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your work-tracking / PPM tool and reporting tool**, produce the recurring [weekly/biweekly status report](../phases/5-build/artifacts/weekly-biweekly-status-report.md), [feature/epic status report](../phases/4-plan/artifacts/feature-epic-status-report.md), [budget burn report](../phases/5-build/artifacts/budget-burn-report.md), and [launch-readiness status pack](../phases/6-verify/artifacts/launch-readiness-status-pack.md) from source data.
- **Across work-tracking, source control, and PPM tools**, detect dependency drift and schedule-health signals; escalate exceptions per your policy.
- **In your collaboration / meeting tool**, transcribe and summarize sessions into structured [cross-team sync notes](../phases/5-build/artifacts/cross-team-sync-notes.md), [stakeholder workshop outcomes](../phases/2-define/artifacts/stakeholder-workshop-outcomes.md), and [decision log from design reviews](../phases/3-design/outcomes/decision-log-from-design-reviews.md) — action items with owners and due dates.
- **In your RAID / risk tool**, flag stale items, auto-assign owners for routine risk categories, and keep the [governance calendar](../phases/4-plan/artifacts/governance-calendar.md) current.
- **In your shared drive / wiki**, on project close, assemble the [closed project & archive](../phases/9-iterate/artifacts/closed-project-archive.md) from the project's artifact set for your sign-off.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **37** artifacts/outcomes as primary (A) and co-own **6** (R)._

### [1. Discover](../phases/1-discover/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [initial project brief](../phases/1-discover/artifacts/initial-project-brief.md) | Project initiation / pre-kickoff coordination |
| **A** | [aligned leadership team](../phases/1-discover/outcomes/aligned-leadership-team.md) | Sponsor/PO alignment facilitation |

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [dependency list](../phases/2-define/artifacts/dependency-list.md) | Dependency mapping |
| **R** | [effort estimates](../phases/2-define/artifacts/effort-estimates.md) | Estimation / sizing |
| **A** | [affected-audiences list](../phases/2-define/artifacts/affected-audiences-list.md) | Identify affected internal audiences |
| **A** | [charter draft](../phases/2-define/artifacts/charter-draft.md) | Charter development facilitation |
| **A** | [stakeholder workshop outcomes](../phases/2-define/artifacts/stakeholder-workshop-outcomes.md) | Define-phase stakeholder workshops |
| **A** | [draft project schedule](../phases/2-define/artifacts/draft-project-schedule.md) | Baseline schedule draft |

### [3. Design](../phases/3-design/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [confirmed scope/budget or change request](../phases/3-design/outcomes/confirmed-scope-budget-or-change-request.md) | Budget & scope reality check |
| **A** | [design-phase plan](../phases/3-design/artifacts/design-phase-plan.md) | Design-phase schedule & resource coordination |
| **A** | [vendor selection process outputs](../phases/3-design/artifacts/vendor-selection-process-outputs.md) | Vendor selection process coordination |
| **A** | [decision log from design reviews](../phases/3-design/outcomes/decision-log-from-design-reviews.md) | Design review scheduling & minutes |

### [4. Plan](../phases/4-plan/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [baselined schedule & budget commitment](../phases/4-plan/outcomes/baselined-schedule-budget-commitment.md) | Approve delivery baseline |
| **A** | [onboarded team](../phases/4-plan/artifacts/onboarded-team.md) | Team onboarding & ramp-up |
| **A** | [iteration plan](../phases/4-plan/artifacts/iteration-plan.md) | Iteration / milestone planning |
| **A** | [assigned workitems & daily status](../phases/4-plan/artifacts/assigned-workitems-daily-status.md) | Assign & manage workitems |
| **A** | [feature/epic status report](../phases/4-plan/artifacts/feature-epic-status-report.md) | Track features & epics |
| **A** | [resource schedule](../phases/4-plan/artifacts/resource-schedule.md) | Resource tracking & scheduling |
| **A** | [risk register](../phases/4-plan/artifacts/risk-register.md) | Risk identification & escalation |
| **A** | [executed comms per cadence](../phases/4-plan/artifacts/executed-comms-per-cadence.md) | Execute stakeholder communication cadence |
| **A** | [RAID log](../phases/4-plan/artifacts/raid-log.md) | Dependency / RAID management setup |
| **A** | [governance calendar](../phases/4-plan/artifacts/governance-calendar.md) | Governance cadence setup |

### [5. Build](../phases/5-build/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [unblocked dependencies](../phases/5-build/outcomes/unblocked-dependencies.md) | Unblock cross-org dependencies |
| **R** | [accepted increments](../phases/5-build/outcomes/accepted-increments.md) | Progress review & increment acceptance |
| **A** | [process improvement actions](../phases/5-build/artifacts/process-improvement-actions.md) | Process improvement review |
| **A** | [weekly/biweekly status report](../phases/5-build/artifacts/weekly-biweekly-status-report.md) | Sponsor/PO status report preparation |
| **A** | [change control package](../phases/5-build/artifacts/change-control-package.md) | Scope-change impact coordination |
| **A** | [updated RAID log](../phases/5-build/artifacts/updated-raid-log.md) | RAID log maintenance |
| **A** | [cross-team sync notes](../phases/5-build/artifacts/cross-team-sync-notes.md) | Cross-team sync facilitation |
| **A** | [budget burn report](../phases/5-build/artifacts/budget-burn-report.md) | Budget & burn tracking |
| **A** | [managed vendor deliverables](../phases/5-build/artifacts/managed-vendor-deliverables.md) | Vendor & contract management |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [verify execution plan](../phases/6-verify/artifacts/verify-execution-plan.md) | Verify-phase coordination |
| **A** | [launch-readiness status pack](../phases/6-verify/artifacts/launch-readiness-status-pack.md) | Launch-readiness status reporting |
| **A** | [defect status & triage cadence](../phases/6-verify/artifacts/defect-status-triage-cadence.md) | Issue / defect governance |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [launch run-of-show](../phases/7-launch/artifacts/launch-run-of-show.md) | Launch day coordination / command center |
| **A** | [executed launch comms](../phases/7-launch/artifacts/executed-launch-comms.md) | Launch comms execution |
| **A** | [go/no-go decision package](../phases/7-launch/outcomes/go-no-go-decision-package.md) | Launch stage-gate coordination |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [steady-state operating handoff](../phases/8-operate/outcomes/steady-state-operating-handoff.md) | Hypercare transition to steady-state |
| **A** | [operating review meetings](../phases/8-operate/artifacts/operating-review-meetings.md) | Operating cadence coordination |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [lessons-learned repository](../phases/9-iterate/artifacts/lessons-learned-repository.md) | Lessons-learned facilitation |
| **A** | [closed project & archive](../phases/9-iterate/artifacts/closed-project-archive.md) | Project closure |
| **A** | [scheduled benefits reviews](../phases/9-iterate/artifacts/scheduled-benefits-reviews.md) | Benefits realization coordination |
| **A** | [retrospective report](../phases/9-iterate/artifacts/retrospective-report.md) | Post-launch review / retrospective |

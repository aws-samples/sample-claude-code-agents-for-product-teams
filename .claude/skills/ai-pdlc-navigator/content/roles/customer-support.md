# 14. Customer Support / Success
- **Description:** Reactive ticket resolution (Support) plus proactive onboarding, health scoring, QBRs, renewals, and advocacy (CS).
- **Business purpose:** Protects and grows recurring revenue; contains cost-to-serve.
- **Typically reports to:** VP/Chief Customer Officer, CRO, or CEO.
- **Project goals:** Support/CS launch-ready · users hit activation milestones · GRR/NRR targets · closed-loop VoC to Product.

---


## AI teammate

**Purpose:** Run the ticket-to-resolution and customer-health loops — deflect, triage, escalate, and feed VoC back to Product — so users hit activation milestones and recurring revenue is protected.

**Assistive AI (tight collaboration):** Drafts and iterates on the [support process model](../phases/2-define/artifacts/support-process-model.md), [live support processes](../phases/7-launch/artifacts/live-support-processes.md), [health scores & at-risk list](../phases/8-operate/artifacts/health-scores-at-risk-list.md), [user feedback log](../phases/9-iterate/artifacts/user-feedback-log.md), and [NPS & health scores](../phases/9-iterate/artifacts/nps-health-scores.md) with a human in the loop; drafts [customer resolution](../phases/8-operate/artifacts/customer-resolution.md) content for human approval where policy requires.

**Autonomous AI (fully delegated):** Within the escalation triggers below, an agent can maintain [activated customers](../phases/8-operate/artifacts/activated-customers.md) status, run tier-1 ticket deflection and triage that feeds the [triaged ticket queue](../phases/8-operate/artifacts/triaged-ticket-queue.md), [tagged support-ticket dataset](../phases/8-operate/artifacts/tagged-support-ticket-dataset.md), and [escalated issue ticket](../phases/8-operate/artifacts/escalated-issue-ticket.md) stream, and cluster recurring issues into a refreshed [known-issues list](../phases/8-operate/artifacts/known-issues-list.md). Illustrative, not prescriptive — customer policy decides what lands here.

**Scope boundaries:** Does not negotiate, commit, or close renewals or expansions — contributes to the [renewal & expansion pipeline](../phases/8-operate/artifacts/renewal-expansion-pipeline.md) but not the [renewal & expansion bookings](../phases/8-operate/artifacts/renewal-expansion-bookings.md) (Sales-owned). Does not promise product changes, issue goodwill credits, or extend SLAs to customers. Does not send customer-facing responses above the team's confidence/risk threshold without human review.

**Inputs:** Incoming tickets and cases, product-usage telemetry, [customer-facing knowledge base](../phases/8-operate/artifacts/customer-facing-knowledge-base.md), [user guides](../phases/7-launch/artifacts/user-guides.md), [feature documentation](../phases/7-launch/artifacts/feature-documentation.md), [release notes](../phases/7-launch/artifacts/release-notes.md), account metadata, and VoC capture feeds.

**Outputs:** The A artifacts above, structured escalations to Product and Engineering, and VoC synthesis into the [feedback insights report](../phases/9-iterate/artifacts/feedback-insights-report.md).

**Escalation triggers:**
- Sev-1/Sev-2 customer issue, suspected data breach, or customer-impacting outage.
- At-risk account crossing a churn-probability threshold or a named strategic account flagged.
- Ticket involves pricing, contract, legal, or regulatory commitment.
- Response would commit the company to a product change, SLA exception, or refund.
- VoC theme reaches the threshold defined in the feedback policy (escalate to Product).

**Autonomy:** Customer policy decision — see [adoption/maturity-model.md](../adoption/maturity-model.md) and [adoption/hitl-framework.md](../adoption/hitl-framework.md).

Output is verified at handoff — see the exit checklist in each phase README (e.g., [Operate exit checklist](../phases/8-operate/README.md#exit-checklist)).

## AI acceleration

These are examples of how AI can accelerate your work — not an exhaustive list. Calibrate them to your org's tooling and risk posture.

**Assistive AI (tight collaboration)** — you hold the pen, AI accelerates your judgment. Examples:

- **In your ticketing / case-management tool**, work through complex escalations: pull related tickets, surface likely root causes, draft customer-facing responses before you approve them for the [customer resolution](../phases/8-operate/artifacts/customer-resolution.md) record.
- **In your customer-success platform**, prepare for QBRs and at-risk-account reviews against the [health scores & at-risk list](../phases/8-operate/artifacts/health-scores-at-risk-list.md); synthesize account narratives into the [renewal & expansion pipeline](../phases/8-operate/artifacts/renewal-expansion-pipeline.md).
- **In your feedback-capture tool**, shape voice-of-customer synthesis that feeds the [user feedback log](../phases/9-iterate/artifacts/user-feedback-log.md) and [NPS & health scores](../phases/9-iterate/artifacts/nps-health-scores.md) narrative — what the signals actually mean.
- **In your support-process playbooks**, review the [support process model](../phases/2-define/artifacts/support-process-model.md) and iterate on the [live support processes](../phases/7-launch/artifacts/live-support-processes.md) as the product evolves; spot friction before customers do.
- **In your knowledge base / community**, draft and critique hard-to-explain articles for the [customer-facing knowledge base](../phases/8-operate/artifacts/customer-facing-knowledge-base.md); calibrate tone and depth to the segment.

**Autonomous AI (fully delegated)** — AI runs without you in the loop; you set policy and review on cadence. Examples:

- **In your ticketing / case-management tool**, tier-1 deflection: match incoming tickets to knowledge-base articles and suggest resolutions to customers, with human handoff on confidence threshold breach; feed the [triaged ticket queue](../phases/8-operate/artifacts/triaged-ticket-queue.md).
- **In your ticketing / case-management tool**, tag, route, and prioritize incoming tickets; maintain the [tagged support-ticket dataset](../phases/8-operate/artifacts/tagged-support-ticket-dataset.md) and auto-populate the [escalated issue ticket](../phases/8-operate/artifacts/escalated-issue-ticket.md) stream per policy.
- **In your customer-success platform**, continuously update [activated customers](../phases/8-operate/artifacts/activated-customers.md) status and the [health scores & at-risk list](../phases/8-operate/artifacts/health-scores-at-risk-list.md) from product usage, ticket, and engagement signals.
- **In your knowledge base / community**, cluster recurring issues into a refreshed [known-issues list](../phases/8-operate/artifacts/known-issues-list.md); spot articles that are out-of-date with product changes.
- **In your feedback-capture tool**, run continuous sentiment and topic analysis; route emerging themes into the [user feedback log](../phases/9-iterate/artifacts/user-feedback-log.md) with severity and audience.

## Primary artifacts you interact with

**RACI key:** **A** = Accountable (primary owner) · **R** = Responsible (co-owner). Consulted and Informed positions aren't auto-computed — add them as your org's RACI takes shape.

_Across the lifecycle you own **14** artifacts/outcomes as primary (A) and co-own **1** (R)._

### [2. Define](../phases/2-define/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [support process model](../phases/2-define/artifacts/support-process-model.md) | Support process definition |

### [6. Verify](../phases/6-verify/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [recruited UAT cohort](../phases/6-verify/artifacts/recruited-uat-cohort.md) | Recruit & onboard UAT / beta users |

### [7. Launch](../phases/7-launch/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **R** | [trained sales & support teams](../phases/7-launch/artifacts/trained-sales-support-teams.md) | Internal enablement / training |
| **A** | [live support processes](../phases/7-launch/artifacts/live-support-processes.md) | Execute support process cutover |

### [8. Operate](../phases/8-operate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [activated customers](../phases/8-operate/artifacts/activated-customers.md) | Customer onboarding / activation |
| **A** | [health scores & at-risk list](../phases/8-operate/artifacts/health-scores-at-risk-list.md) | Customer health scoring |
| **A** | [renewal & expansion pipeline](../phases/8-operate/artifacts/renewal-expansion-pipeline.md) | QBRs / customer check-ins |
| **A** | [renewal & expansion bookings](../phases/8-operate/artifacts/renewal-expansion-bookings.md) | Renewal & expansion management |
| **A** | [triaged ticket queue](../phases/8-operate/artifacts/triaged-ticket-queue.md) | Triage customer support issues |
| **A** | [customer resolution](../phases/8-operate/artifacts/customer-resolution.md) | Troubleshoot customer issues |
| **A** | [known-issues list](../phases/8-operate/artifacts/known-issues-list.md) | Identify known issues |
| **A** | [escalated issue ticket](../phases/8-operate/artifacts/escalated-issue-ticket.md) | Escalate user issues |
| **A** | [tagged support-ticket dataset](../phases/8-operate/artifacts/tagged-support-ticket-dataset.md) | Tag / categorize support tickets |

### [9. Iterate](../phases/9-iterate/README.md)

| RACI | Artifact / Outcome | Activity |
|------|--------------------|----------|
| **A** | [user feedback log](../phases/9-iterate/artifacts/user-feedback-log.md) | Document user feedback |
| **A** | [NPS & health scores](../phases/9-iterate/artifacts/nps-health-scores.md) | Customer success check-ins / NPS |

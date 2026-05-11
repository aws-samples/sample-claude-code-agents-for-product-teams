# AI Maturity Assessment

A structured way to answer "how AI-mature are we?" The assessment uses two lenses:

1. **Automation lens** — per-phase automation coverage, labeled Sporadic / Isolated / Struggling / Scaling / Mature. Can be run org-wide (14 roles × 9 phases) or role-level (1 role × 9 phases).
2. **Readiness lens** — five organizational dimensions (Strategy & Governance, Data, Tech Infrastructure & Tools, Workforce & Skills, Culture), labeled on the same 5-tier scale. Org-level only.

Together they answer two different questions. Automation asks "how much of the work is AI-assisted today?" Readiness asks "is the org positioned for that automation to stick and scale?" A team can have high automation and low readiness (built it, but won't scale) or low automation and high readiness (ready to go, haven't shipped).

> **Label source.** The 5-tier vocabulary (Sporadic, Isolated, Struggling, Scaling, Mature) and the five readiness dimensions come from an internal AWS maturity model developed by a partner team. This doc adopts them directly so customers see one consistent vocabulary across AWS materials.

This complements the [maturity model](maturity-model.md). The maturity model is the **tactical picker** — for one workflow, it helps a team decide "what autonomy level × coverage should we aim for next?" This assessment is the **strategic scorecard** — it tells you where you are today across automation and readiness, so you can decide where to invest.

## Why this matters

A mature AI-PDLC org has high automation across all roles and phases, backed by strategy, data, infrastructure, workforce, and culture that support it sticking. Not every role is necessarily performed by a person — some roles or role-tasks can be fully autonomous within named escalation triggers (see [HITL framework](hitl-framework.md)). The observable results: **cycle times drop** (handoffs compress, reviews shorten) and **ship velocity rises** (more features through the pipeline per unit time, at the same or better quality).

This assessment doesn't measure cycle time or velocity directly — those are outcomes. It measures the drivers so you can diagnose why cycle times or velocity aren't improving.

## Scope options

### Org-level assessment

Walks all 14 roles across all 9 phases (automation lens) and all 5 readiness dimensions. Use this when:

- You're planning a program-level AI adoption push.
- You're reporting maturity to leadership.
- You want to spot cross-role gaps (e.g., "Build is Scaling but Verify is Sporadic, so fast code still waits at the gate") or automation/readiness mismatches.

### Role-level assessment

Walks one role across all 9 phases (automation lens only; the readiness lens is org-wide and doesn't apply to a single role). Use this when:

- You're planning AI adoption for a specific role's team.
- You want to know where the biggest leverage is within one role's lifecycle.
- You're a role owner (Developer team lead, QA manager, etc.) preparing a pitch.

---

## Lens 1 — Automation

### Methodology — interview

Assessment runs as an **interview**, not a self-score questionnaire. For each activity, ask the user to describe *how they currently do the work* in their own words. State the score back for confirmation before moving on.

For each **phase × role** cell in scope, enumerate the **activities, artifacts, and outcomes** that role owns (A) or co-owns (R) in that phase. Source from:

- The role's RACI table in `roles/<role>.md` (primary and co-owned).
- The phase's exit checklist in `phases/<N>-<slug>/README.md`.
- The activity lines in `AI-PDLC-linear-flow.md` under that phase.

Example interview questions:

| Activity | Interview question |
|---|---|
| Design review for operational/resilience risk | "How does your team currently review a design for operational and resilience risk before signing off?" |
| Postmortem authoring | "Walk me through how a postmortem gets written today — who drafts it, what tools, how long?" |
| Alert triage | "When an alert fires off-hours, what happens between the page and a human acknowledging?" |

**Capture the tools they name** as they describe each activity — product names, not categories. Keep a running list; use it to build the Tools Used section of the report.

From the interview answer, derive two columns:

- **Maturity** — one of the 5-tier labels: Sporadic, Isolated, Struggling, Scaling, Mature.
- **Approach** — Assistive or Autonomous. Blank when Maturity is Sporadic.

Activity-level scoring:

| Maturity | When it applies | Approach |
|---|---|---|
| **Sporadic** | Activity isn't performed, or is performed with zero AI involvement. | — |
| **Isolated** | One-off or experimental AI use; not consistent; hasn't produced a repeatable pattern yet. | Assistive |
| **Struggling** | AI is used sometimes on this activity but not reliably; the team knows it could be working but it hasn't landed. | Assistive |
| **Scaling** | AI is the norm for this activity; used routinely in production; a human still owns the output. | Assistive |
| **Mature** | AI runs the activity end-to-end within escalation triggers; humans review on cadence or exception. | Autonomous |

**Confirm the maturity before moving on:** "Sounds like that's currently Scaling with Assistive approach — AI drafts the first pass, you edit, it's part of your routine. Correct?" Fix on disagreement. For ambiguity, prefer the more conservative label and note the uncertainty.

**Batch only after the user demonstrates fluency.** The skill can offer "if the next three are the same, say 'same,'" but only after the user has seen the pattern a few times.

### Phase label rubric

Roll each phase up using the 5-tier scale based on the % of activities with any AI assistance (Assistive + Autonomous):

| Label | Rule | What it looks like |
|-------|------|--------------------|
| **Sporadic** | 0% of activities have AI assistance. | The phase runs exactly as it did before AI. All activities are human-only. |
| **Isolated** | 1-20% assisted. A handful of activities, mostly Assistive. | One or two pilots inside the phase. Cycle-time impact is hard to detect at the phase level. |
| **Struggling** | 21-50% assisted. Mostly Assistive, little or no Autonomous. | Many POCs and assistive uses, but little has reached production or autonomous operation. The "valley of despair" between pilots and scale. |
| **Scaling** | 51-75% assisted. Mix of Assistive and Autonomous across the phase. | AI-accelerated work is the norm across most of the phase. Autonomous work exists for narrow, well-bounded activities. Cycle time is measurably shorter. |
| **Mature** | 76%+ assisted. Many Autonomous activities. | AI-accelerated or autonomous is the default. A human gates the phase exit but doesn't touch most activities. Cycle time is dramatically shorter; some phases run continuously rather than in sprints. |

Ties break up: if a phase is on a boundary (e.g., 20% vs. 21%), weight Autonomous activities more heavily — they indicate deeper adoption.

### Potential automation targets per phase

For each phase scored, after the activity table, add a **Potential automation targets** subsection. List 3-5 activities where AI could advance the maturity (Sporadic → Isolated/Scaling; Scaling Assistive → Mature Autonomous). For each target:

- Name the activity and its current Maturity/Approach.
- Describe how the automation would work in 1-2 sentences — the concrete mechanic, not the abstraction. "Claude Code watches Datadog against a 7-day baseline and posts an anomaly summary to the launch bridge every 5 minutes" beats "AI-assisted launch monitoring."
- Name what would move on the Maturity/Approach columns ("Scaling / Assistive → Mature / Autonomous").

Skip this subsection for phases where all activities are already Mature / Autonomous or where the role has zero activities in that phase.

### Automation rollup — role-level

One table, nine rows:

| Phase | Activities scored | None | Assistive | Autonomous | % assisted | Label |
|-------|------------------:|-----:|----------:|-----------:|-----------:|-------|
| 1. Discover | _N_ | _n0_ | _n1_ | _n2_ | _x%_ | _label_ |
| … | | | | | | |

Plus a short summary: strongest phase, weakest phase, cross-phase patterns (e.g., "Discover through Design is Scaling; Build through Operate is Isolated" — a common shape that tells you where to invest next).

### Automation rollup — org-level

A matrix: 14 roles × 9 phases, cells = label. Plus:

- Per-phase label (weighted by activity count across roles) — the **phase maturity**.
- Per-role label (weighted by activity count across phases) — the **role maturity**.
- A summary with the top 3 leverage opportunities.

---

## Lens 2 — Readiness (org-level only)

The readiness lens answers whether the org is positioned for its automation to stick and scale. Each dimension is scored on the same 5-tier scale. Score from the team's observed state — don't grade aspirationally.

### Dimension 1 — Strategy & Governance

| Level | Signals |
|-------|---------|
| **Sporadic** | Uncoordinated experimentation. No formal AI strategy or budget. |
| **Isolated** | Siloed proofs of concept. No business cases. Some innovation budget. Leadership recognition exists but ownership is fragmented. |
| **Struggling** | No clear definition of success. Release frustration — teams building but not shipping. Competing priorities across business units. |
| **Scaling** | Formal AI strategy. Clear business and product success metrics. At least one successful AI launch in production. |
| **Mature** | C-level AI strategy. AI KPIs tracked at the top of the company. AI is threaded throughout the product roadmap. Successful AI adoption is the pattern, not the exception. |

### Dimension 2 — Data

| Level | Signals |
|-------|---------|
| **Sporadic** | Fragmented data. No data strategy. |
| **Isolated** | Some cataloging exists but data access takes time. No data strategy. |
| **Struggling** | Data is available for AI POCs but acquiring it for production paths is ad-hoc. Common pipeline patterns are emerging but not standardized. |
| **Scaling** | Documented data strategy. Data automation and workflows exist. Data is curated and maintained to support production AI features. |
| **Mature** | Enterprise-wide data strategy. Quality metrics are tracked. The org actively gathers new data to support AI features. |

### Dimension 3 — Tech Infrastructure & Tools

| Level | Signals |
|-------|---------|
| **Sporadic** | Consumer-grade AI tools. More personal AI use than corporate use. |
| **Isolated** | Experimentation with enterprise AI services. No clear paths to production for AI ideas. |
| **Struggling** | Fluency with enterprise-grade AI tools is rising. Teams are ready to release a first AI workload but operational support is thin. |
| **Scaling** | Investment in AI infrastructure. Established MLOps / AIOps. |
| **Mature** | Scalable and secure AI infrastructure. Continuous learning and adaptation are built in. |

### Dimension 4 — Workforce & Skills

| Level | Signals |
|-------|---------|
| **Sporadic** | Basic AI literacy. Individual efforts. No systematic upskilling. |
| **Isolated** | AI power users emerge. Peer-to-peer sharing. AI-assisted tools in some teams. No systematic upskilling. |
| **Struggling** | Technical teams can build AI POCs. AI software-development tools are in regular use. Productivity gains are hard to measure. |
| **Scaling** | Structured talent development and training. Productivity and velocity are measured. Hiring includes new roles based on the AI-PDLC pattern. |
| **Mature** | Talent is fully upskilled with continuous training. AI-PDLC *is* PDLC. AI skills and usage are default-on. |

### Dimension 5 — Culture

| Level | Signals |
|-------|---------|
| **Sporadic** | Grassroots. Isolated individuals. No leadership support. |
| **Isolated** | Increase in AI chatter. Some sharing. AI usage is task-oriented. |
| **Struggling** | Using AI in beneficial ways. Individual productivity gains are felt but not measured. Uncoordinated processes, duplicate efforts. |
| **Scaling** | Processes work in harmony. Productivity is measured in business outcomes, not tool usage. |
| **Mature** | Hive mind of shared best practices. Continuously accelerating improvement. |

### Readiness rollup

A single table:

| Dimension | Level | Top signal observed | Top gap to next level |
|---|---|---|---|
| Strategy & Governance | _label_ | | |
| Data | _label_ | | |
| Tech Infrastructure & Tools | _label_ | | |
| Workforce & Skills | _label_ | | |
| Culture | _label_ | | |

Plus a short summary: the lowest-scoring dimension is usually the one that will drag the others back if left alone. Name it explicitly.

---

## Cross-lens diagnosis

After scoring both lenses, look for mismatches:

| Pattern | Diagnosis |
|---------|-----------|
| Automation > Readiness | Built ahead of scale. Expect brittle wins; investments won't compound until Strategy/Data/Infra/Workforce/Culture catch up. |
| Automation < Readiness | Ready but haven't shipped. Identify the blocker — usually appetite, not capability. |
| Both low | Start with one high-leverage workflow (role-level lens 1) and one foundational dimension (usually Strategy or Data on lens 2). Don't boil the ocean. |
| Both high | Cross-phase coverage is likely the next frontier — see the [maturity model](maturity-model.md)'s coverage axis. |

Record the diagnosis in the report.

---

## How this relates to the maturity model

The [maturity model](maturity-model.md) is a **tactical picker** — for one workflow, it helps a team decide "what autonomy level × coverage should we aim for next?" The 2D grid is about a workflow's current and target state.

The **assessment is a strategic scorecard** — it tells you where you are today across automation and readiness, so you can decide where to invest.

Loose mapping from an automation label to the [maturity model](maturity-model.md) grid:

- **Sporadic** → L0 regardless of coverage.
- **Isolated** → usually L1 × single-role.
- **Struggling** → L1-L2 × single-role or single-phase; rarely cross-phase.
- **Scaling** → L1-L2 × single-phase or cross-phase.
- **Mature** → L2-L3 × cross-phase or full lifecycle.

Use them together: the assessment tells you where you are; the maturity model helps you pick a reasonable next step for one workflow; [anti-patterns](anti-patterns.md) tells you what to watch out for when you move.

---

## What a Mature org looks like

- **Most activities across most phases are AI-accelerated.** Human attention concentrates at phase boundaries ([exit checklists](../phases/README.md)) and escalation triggers.
- **Some roles or role-tasks are fully autonomous.** Dependency patching, test generation, documentation sync, KPI monitoring, release-notes drafting, incident summarization — these lean autonomous in mature orgs.
- **Strategy, data, infra, workforce, and culture all support it.** No single dimension is dragging.
- **Cycle times are compressed.** Handoffs that took days now take minutes; reviews that took hours now take seconds. The [exit checklists](../phases/README.md) still gate quality, but the work to meet them is mostly automated.
- **Feature ship velocity is maximized relative to the team's quality bar.** More features through the pipeline at the same or better defect rate. Velocity is a *symptom* of maturity, not a score input — but a Mature org sees it reliably.

---

## Running the assessment

The [navigator skill](../.claude/skills/ai-pdlc-navigator/SKILL.md) path 7 orchestrates this interactively: collects scope, walks the activities, computes the labels, writes a report. You can also run it manually by following this doc.

## Recording the assessment

Save the report(s) to `./artifacts/` in the user's project root (not this handbook repo).

### Role-level scope

Write a per-role markdown artifact at `./artifacts/YYYY-MM-DD-<role-slug>-maturity.md` — one file per role assessed. Using the handbook's role slug (`developer`, `site-reliability-engineer`, `product-owner`, etc.) keeps the filename stable across re-runs and makes diffs meaningful.

Each role artifact contains:

- **Scope** — role name and slug, date run.
- **Lens 1 (Automation)** — for each phase the role owns activities in:
  - An activity table with columns: **Activity | Artifact/Outcome | Maturity | Approach | Notes**. Maturity is the 5-tier label (Sporadic/Isolated/Struggling/Scaling/Mature); Approach is Assistive or Autonomous (blank when Maturity is Sporadic). Notes cites the user's phrasing from the interview.
  - A **Potential automation targets** subsection (see "Potential automation targets per phase" above).
  - The phase label and a 1-2 sentence rationale.
- **Rollup table** — one row per phase. Columns: Phase / Activities / Sporadic / Isolated / Struggling / Scaling / Mature / Assistive (count) / Autonomous (count) / Label.
- **Cross-phase pattern** — strongest phase, weakest phase, observed pattern (e.g., "Discover through Design is Scaling; Build through Operate is Isolated").
- **Top 3 leverage opportunities** for this role, each grounded in a named activity or artifact.
- **A concrete "next tier" picture** for this role — what moving one label up would look like in practice.
- **Tools used** — a table of every product the user named during the interview, grouped by handbook capability category. Columns: Capability / Tool / Used for (list of activities in this assessment where the tool came up). This doubles as a mini tools inventory for this role; link to the full inventory if path 3 has been run.

If multiple roles are assessed in the same session, write one file per role. Do not combine them.

### Org-level scope

Write:
- One **per-role artifact** at `./artifacts/YYYY-MM-DD-<role-slug>-maturity.md` for each of the 14 roles — same shape as the role-level output above.
- A **rollup artifact** at `./artifacts/YYYY-MM-DD-org-maturity.md` containing the 14×9 automation matrix, the 5-dimension readiness table, the cross-lens diagnosis, org-wide top 3 leverage opportunities, and the concrete Mature picture for the org. The rollup links to each per-role artifact.

This way a customer can share the Developer artifact with engineering leadership without also handing over the Product Sponsor assessment, while the rollup stays the single source of truth for the org view.

### Re-running

Re-run quarterly or after a significant AI adoption push. Because filenames are role-slug-keyed, the newest run overwrites or sits alongside the previous one — diff against the previous file to track progress per role.

---
name: ai-pdlc-navigator
description: Use this skill whenever the user asks about this AI-PDLC repo — the tool-agnostic product development lifecycle with 9 phases (Discover → Iterate), 14 role swim lanes, ~130 activities, ~260 artifacts/outcomes, and AI acceleration guidance per role. Trigger on any mention of phases (Discover/Define/Design/Plan/Build/Verify/Launch/Operate/Iterate), roles (Product Sponsor, BA, Architect, SRE, PM, etc.), artifacts, outcomes, RACI, the swim-lane diagram, the drawio source, "assistive vs autonomous AI" for a role, or requests to extend/regenerate/commit changes to this lifecycle. Also trigger when the user says things like "update our flow", "what does X role do in Y phase", "where does artifact Z live", "how do I regenerate the diagram", or "stay source-of-truth aligned".
---

# AI-PDLC Handbook Navigator

This skill orients you (Claude) to the AI-PDLC handbook so you can help the user extend, maintain, or explain the lifecycle framework without re-learning it every session.

## What this handbook is

A tool-agnostic, end-to-end product-development lifecycle captured as:

- **9 phases** — Discover · Define · Design · Plan · Build · Verify · Launch · Operate · Iterate
- **14 role swim lanes** — Product Sponsor, Product Owner, Business Analyst, UI/UX Designer, Architect, Security & Compliance, SRE, Project Manager, Developer, QA/Tester, Release Manager, Technical Writer, Sales & Marketing, Customer Support
- **~130 activities** mapped to phase × role, each producing an **artifact** (tangible deliverable) or **outcome** (decision / state change)
- **A swim-lane diagram** (`content/AI-PDLC-linear.drawio` when editing the source handbook repo; rendered to PNG/SVG)

## Bundled content — paths to use

All handbook content is bundled inside this skill under `content/`. When you need to read a file, use these paths (relative to this SKILL.md):

- **Master index:** `content/AI-PDLC-linear-flow.md`
- **Role pages:** `content/roles/<role-slug>.md`
- **Phase overview:** `content/phases/<N-phase>/README.md`
- **Role in a specific phase:** `content/phases/<N-phase>/<role-slug>.md`
- **Artifact stubs:** `content/phases/<N-phase>/artifacts/<slug>.md`
- **Outcome stubs:** `content/phases/<N-phase>/outcomes/<slug>.md`
- **Adoption guides:** `content/adoption/maturity-model.md` · `content/adoption/maturity-assessment.md` · `content/adoption/hitl-framework.md` · `content/adoption/anti-patterns.md` · `content/adoption/formats.md` · `content/adoption/objection-handling.md`
- **Rendered diagram:** `content/docs/AI-PDLC-linear.png`

In human-facing replies, you can use bare handbook paths (e.g., `roles/developer.md`) — they're recognizable to users reading the handbook repo on GitHub. But when *you* open a file with Read, always prefix with `content/` so the plugin install resolves it.

Activity links inside `content/AI-PDLC-linear-flow.md` are written as `phases/<N>/…` without the `content/` prefix — they're relative-from-master-index. To resolve one, join it onto `content/`: a link `phases/3-design/artifacts/api-specification.md` lives at `content/phases/3-design/artifacts/api-specification.md`.

## Two invocation modes

This skill serves two audiences:

1. **Humans working interactively** (the default). Run the teach-as-you-go onboarding and the seven-path menu below.
2. **A role agent delegating** (Developer, Architect, SRE, etc.). Skip the onboarding. The agent already knows its role and its question. Just orient to the handbook paths and hand control back. See **Agent mode** section below.

Decide which mode you're in on first activation: if the message comes from a role agent (prompt mentions "you are acting as the X teammate" or similar), use Agent mode; otherwise use interactive.

## Agent mode — serving a role teammate

When invoked by one of the 14 role agents defined in `plugin/agents/`:

1. **Skip the onboarding paragraph, the concept definitions, and the seven-path menu.** The agent already has role context.
2. **Confirm the role slug.** It should be one of: `product-sponsor` · `product-owner` · `business-analyst` · `ui-ux-designer` · `architect` · `security-compliance` · `site-reliability-engineer` · `project-manager` · `developer` · `qa-tester` · `release-manager` · `technical-writer` · `sales-marketing` · `customer-support`.
3. **Point the agent at the canonical doc for whatever it's about to do:**
   - For role-wide questions (remit, RACI, escalation triggers): `content/roles/<slug>.md`.
   - For an artifact or outcome the agent is producing: the stub file at `content/phases/<N>/artifacts/<slug>.md` or `content/phases/<N>/outcomes/<slug>.md`.
   - For cross-role handoffs or gates: the phase README at `content/phases/<N>/README.md` (look for Exit checklist).
4. **Return control.** A short acknowledgement — "Oriented. Canonical role file: `content/roles/developer.md`. For the feature-code artifact, see `content/phases/5-build/artifacts/feature-code.md`." — and let the agent get on with the task. Don't run a path unless the agent explicitly asks for one.

## Interactive mode — teach as you go

Assume the user has never seen this framework before. Default to onboarding behavior until the user signals otherwise (e.g., they use the vocabulary fluently, name specific files, or explicitly say "skip the intro").

**On first contact**, before showing the menu:

1. **Orient in one paragraph.** Briefly explain what this repo is — a **tool-agnostic product development handbook** with 9 phases, 14 roles, and per-role AI acceleration guidance — designed for customer teams adopting AI teammates. Use the word "handbook" explicitly so the user knows this is a reference they work *with*, not a tool they install. Two to three sentences.
2. **Offer the menu below.** Present the five starter paths. Tell them they can also just describe their situation and you'll pick the right path.

**As the conversation unfolds, introduce concepts before using them.** The first time each of these appears in a reply, define it briefly in plain language (one short sentence is enough):

- **Phase** — a stage of the lifecycle (Discover, Define, Design, Plan, Build, Verify, Launch, Operate, Iterate).
- **Role** — one of 14 named jobs in a product org (Developer, PO, SRE, etc.), each with its own lane across every phase.
- **Artifact** — a tangible deliverable (spec, report, plan, code). Lives at `phases/<N>/artifacts/<slug>.md`.
- **Outcome** — a decision or state change (approval, sign-off, gate). Lives at `phases/<N>/outcomes/<slug>.md`.
- **Activity** — a task a role does, producing an artifact or outcome.
- **RACI** — Responsible / Accountable / Consulted / Informed. Every artifact has a named owner (A).
- **Agent card** — the contract for an AI teammate on a given role: purpose, inputs, outputs, escalation triggers. Lives in `roles/<role>.md`.
- **Assistive AI** — AI accelerates the human's judgment; human holds the pen.
- **Autonomous AI** — AI runs the work within defined escalation triggers; human reviews on cadence.
- **Definition of Done** — a 3-5 item checklist per artifact/outcome making "is this ready?" verifiable.
- **Exit checklist** — the per-phase gate listing every artifact + outcome needed before the next phase begins.
- **Maturity model** — the *tactical picker*: a 2D grid (autonomy × coverage) for choosing where to aim for one workflow. `adoption/maturity-model.md`.
- **Maturity assessment** — the *strategic scorecard*: two lenses (automation per phase, readiness across 5 dimensions) labeled on a shared 5-tier scale (Sporadic / Isolated / Struggling / Scaling / Mature). `adoption/maturity-assessment.md`.
- **HITL framework** — how a team decides how much autonomy to grant (blast radius, reversibility, etc.). `adoption/hitl-framework.md`. Explicitly a framework, not a prescription.

**Keep the teaching lightweight.** Define on first use, not every use. Don't lecture — a clause in a sentence is often enough ("the Developer role — one of 14 named jobs in the framework — owns…"). If the user demonstrates familiarity, drop the definitions.

**Favor links over paraphrase.** When a concept has its own doc (maturity model, HITL framework, anti-patterns, a specific artifact), link to it so the user can go deeper without you reciting the whole thing.

**Ask, don't assume.** Before running a path, confirm the basics: "Which role is yours?" (path 1), "Which phase or phases?" (path 2), "Which tool category first?" (path 3). A first-time user won't know to volunteer this.

## How I can help

When the user arrives with an open-ended ask — or explicitly asks "what can you help with?" — offer these seven starter paths. Most first-time users want one of them.

1. **Plan AI acceleration for my role.** Walk a confirm-and-extend flow before ideating:
   1. **Identify the role.** Ask which of the 14 roles is theirs. Read `content/roles/<role-slug>.md`.
   2. **Confirm outcomes they own.** Pull every outcome (from the RACI table and from the activity lines in `content/AI-PDLC-linear-flow.md`) where this role is A or R. List them back: "Here are the outcomes the handbook says this role owns. Which apply to your situation? Any the handbook doesn't list but you actually drive?" Record confirmed, unconfirmed, and additional outcomes.
   3. **Confirm artifacts they own.** Same pattern for artifacts: list the A and R artifacts from the role's RACI table. Ask which apply, which don't, and what additional artifacts they produce that aren't in the handbook. Record the same three buckets.
   4. **Ideate AI acceleration.** Now use the agent card (AI teammate or AI assistance for this role) plus the Assistive AI / Autonomous AI buckets in the AI acceleration section as the palette. Brainstorm 3-5 concrete accelerations — grounded specifically in the *confirmed + additional* outcomes and artifacts from steps 2-3, not the full handbook list.
   5. **Point at maturity.** Reference `content/adoption/maturity-model.md` so the user can self-locate on autonomy × coverage.
   6. **Hand off.** Offer to deepen any candidate via path 4 (create a new automation spec).

   The confirmation step matters because the handbook is a reference, not a prescription — teams often don't match it 1:1, and the accelerations should reflect what *this team* actually owns.

2. **Plan AI acceleration for my whole project.** Ask where the team is on the lifecycle (all phases? specific phase? just Build?) and which roles are active. Walk `content/phases/<N>/README.md` for each in-scope phase and the relevant `content/roles/<role-slug>.md` files. Produce a per-phase acceleration map (assistive + autonomous candidates per role), flag cross-phase handoffs where automation compounds, and call out where the team sits on the `content/adoption/maturity-model.md` grid. Use `content/adoption/anti-patterns.md` to flag risks in the plan early.

3. **Discover the tools we use for PDLC processes.** The handbook describes tools in *categories* (work-tracking / PPM tool, source control, observability stack, docs-as-code platform, etc.). This workflow walks those categories **one at a time, prescriptively**, using the handbook's canonical category names — and captures the specific product this team uses for each. Output is a reusable tools inventory artifact that downstream workflows (paths 2, 4, 7) consume.
   1. **Assemble the canonical category list.** Extract every distinct tool-category phrase from the "In your \<category\>…" bullets in `content/roles/*.md` (the AI acceleration sections). De-dup. Use the phrases **verbatim** — do not shorten, paraphrase, or rename them, because the inventory must map back 1:1 to the handbook. Representative categories include (non-exhaustive): work-tracking / PPM tool · backlog / work-tracking tool · source control · CI/CD platform · feature-flag platform · observability / telemetry SDKs · observability stack and alerting platform · incident management tool · dependency / supply-chain tooling · package / artifact registry · docs-as-code platform · runbook repository · requirements / ALM tool · process modeling tool · roadmapping tool · analytics / experimentation platform · customer feedback system · customer-success platform · ticketing / case-management tool · knowledge base / wiki · design tool · design system · user research repository · usability testing tool · accessibility audit tool · performance and accessibility tool · threat-modeling tool · GRC platform · AppSec / policy repository · privacy / DPIA tool · change-advisory / gate tool · change-request tool · release / deployment-orchestration tool · release calendar / scheduling tool · release-notes / changelog tool · changelog repository · test-automation framework · test-management tool · chaos / load-testing tool · exploratory / session tool · collaboration / meeting tool · collaboration / whiteboarding tool · shared drive / wiki · presentation / narrative tool · executive dashboard / BI tool · BI / reporting platform · strategic planning / portfolio tool · RAID / risk tool · spreadsheet / financial modeling tool · cost / FinOps dashboard · enterprise architecture repository · API specification / registry · data modeling tool / schema catalog · diagramming, data modeling, and API specification tool · infrastructure-as-code and CI/CD platform · feedback-capture tool · marketing-content platform · sales-enablement platform · pricing / CPQ tool · analyst / press relations tool · internal announcement channel.
   2. **Scope the walk to roles in play.** Before starting, ask which roles/lanes are active (e.g., "backend-only", "full product org", "single squad without sales"). Drop categories whose parent roles are out of scope — don't force a product for irrelevant capabilities.
   3. **Walk the list one category at a time.** Do **not** show the full list and ask the user to filter it. Don't batch. One turn per category. For each, ask a single question using the handbook's exact category name:
      - Template: "For your **\<canonical category name\>** — what product do you use?"
      - Examples: "For your **work-tracking / PPM tool** — what product do you use?" · "For your **observability stack and alerting platform** — what do you use?" · "For your **feature-flag platform** — what product do you use?" · "For your **threat-modeling tool** — what do you use?"
      - Capture the product name exactly as the user says it.
      - If multiple products fill the same category: capture all, then ask which is the system of record.
      - If they don't use anything for that category: mark `none` and capture one short note on whether the capability is unmet, handled manually, or intentionally skipped. Move on.
      - If they don't know: park as `unknown — confirm with <owner>` and move on. Don't block.
      - If the category is not applicable to their team (say they tell you): mark `N/A` with a one-line reason and move on.
      - Only batch categories after the user explicitly signals they want to speed up ("just give me the rest in one shot"). Even then, keep the handbook names verbatim.
   4. **Write the tools inventory artifact.** Default path `./artifacts/tools-inventory-YYYY-MM-DD.md` in the user's project root (not this handbook repo). One table, using the handbook category name verbatim in the first column:

      | Capability (handbook category) | Tool in use | System of record? | Owner | Notes |
      |---|---|---|---|---|

      Plus a short preamble noting the date, the scope walked, and a link back to the handbook so a reader understands what "capability" means.

   5. **Hand off.** The inventory becomes the input to:
      - **Path 2** (project-wide AI acceleration plan) — so accelerations reference the team's actual tools, not the category.
      - **Path 4** (create a new automation spec) — so the spec names the real integration surface.
      - **Path 7** (maturity assessment) — so the "how do you do X today?" questions can reference the tool by name.

   Keep the handbook's tool-agnostic voice intact: the inventory artifact is the *only* place product names live. Everywhere else in generated outputs, refer to the category and link the inventory for the product mapping.

4. **Create new AI automations.** Confirm role + task + tool. Invoke the `superpowers:brainstorming` skill if the scope is ambiguous. Draft a spec with: purpose, inputs (artifact + tool context), outputs (updated artifact), scope boundaries, escalation triggers, success criteria. Link to the role's agent card as the contract and to `content/adoption/hitl-framework.md` for autonomy policy. If the automation crosses roles, call that out — cross-role automations need handoff checkpoints, not a single prompt.

5. **Talk about an outcome or artifact.** Name it. Read the canonical doc — don't paraphrase from memory. Prefer the most specific file: artifact stub (`content/phases/<N>/artifacts/<slug>.md`) or outcome stub (`content/phases/<N>/outcomes/<slug>.md`). Explain what it is, why it matters, inputs, consumers, Definition of Done, and where it sits in the phase's Exit checklist. If they ask about stakeholders, cross-reference every `content/roles/<role>.md` whose RACI table lists this artifact — primary owner (A), co-owners (R) — and note that Consulted/Informed slots are intentionally blank for the customer org to fill in.

6. **Bootstrap a product.** Take the user's seed vision document(s) and generate a starter set of handbook artifacts so the team can move forward with traceability back to the vision.
   1. **Collect inputs.** Ask the user to name or point at the seed doc(s). Read them. If multiple, ask which is authoritative when they conflict.
   2. **Map inbound format to handbook artifacts.** If the user names a format (PRFAQ, PRD, 6-pager, lean canvas, opportunity canvas, wireframes, user story map, ADR/RFC, OKRs), consult `content/adoption/formats.md` §1 for what that format typically covers fully vs. partially vs. not at all. Use that mapping as the starting proposed artifact set.
   3. **Ask what bundle they want.** Present the named bundle recipes from `content/adoption/formats.md` §2 — Vision, Kickoff, Build-start, Design-partner, Launch-readiness, Board/investor — and ask which matches their handoff moment. Or let them mix-and-match. If none fits, propose a custom set.
   4. **Confirm the artifact set.** Show the combined list (inbound-covered + bundle-recipe + anything else they name). Flag which are fully covered by the seed docs, which are partially covered (will have `_TBD_` placeholders), and which would need fresh content.
   5. **Generate into `./artifacts/`.** Create a top-level `./artifacts/` dir (relative to the user's project root, not this handbook repo). One markdown file per artifact, using the same metadata header + section structure as the handbook's artifact stubs (`_Produced by:_`, `**Primary owner:**`, `**Stakeholders:**`, `## Definition of Done`, `## What it contains`, `## Inputs you rely on`, `## Who consumes it`). Fill in content grounded in the seed docs — don't invent content the vision doesn't support; use `_TBD: <what to clarify>_` placeholders where the seed is silent.
   6. **Add a manifest.** Write `./artifacts/README.md` following the conventions in `content/adoption/formats.md` §3: one-line description per file grouped by phase, named bundle recipe used, link back to the handbook, version or date. Call out any artifacts with material `_TBD_` placeholders.
   7. **Add a traceability map.** Write `./artifacts/traceability.md` mapping each generated artifact back to the section(s) of the seed doc(s) it draws from.
   8. **Report and hand off.** Tell the user the bundle is ready to zip and share. Offer to walk the team through reviewing the DoDs, or to move to path 2 (project-wide AI acceleration plan) once the artifact set is validated.

   Keep the generated artifacts tool-agnostic and self-contained — they should render correctly outside this repo. Do not deep-link into the handbook's `phases/` paths from inside a generated artifact; use name references and a single top-of-file pointer to the handbook per `content/adoption/formats.md` §3.

7. **Run an AI Maturity Assessment.** Score the team using two lenses (Automation per-phase + Readiness across 5 dimensions) and label each on the shared 5-tier scale: **Sporadic / Isolated / Struggling / Scaling / Mature**. Use `content/adoption/maturity-assessment.md` as the methodology reference — don't invent a different scoring rubric or different labels.
   1. **Pick the scope.** Ask: **org-level** (both lenses — 14 roles × 9 phases automation plus 5 readiness dimensions) or **role-level** (automation lens only, one role × 9 phases). If this is a first-time use with no context, recommend role-level first — it's faster and the findings are actionable sooner. Note: readiness is org-wide by definition and is only scored at org-level scope.
   2. **Lens 1 — Automation (interview).** Run this as an interview, not a self-score questionnaire. For each phase × role cell in scope:
      - Enumerate the activities, artifacts, and outcomes the role owns (A or R). Source from `content/roles/<role>.md` RACI table, the phase's exit checklist, and `content/AI-PDLC-linear-flow.md`.
      - For each activity, ask the user to describe **how they currently do the work**: "How does your team review a design for operational and resilience risk before signing off?" or "Walk me through how a postmortem gets written today." Capture their answer as notes (quote their phrasing).
      - **Capture every tool they name** as they describe the work. Product names, not categories. Keep a running list — it becomes the Tools Used section of the report.
      - From the interview answer, derive two values: **Maturity** (one of Sporadic / Isolated / Struggling / Scaling / Mature — the 5-tier label) and **Approach** (Assistive or Autonomous; blank when Maturity is Sporadic). See `content/adoption/maturity-assessment.md` for the activity-level scoring table.
      - State the maturity and approach back for confirmation: "Sounds like that's currently Scaling with Assistive approach — AI drafts, you edit, it's routine. Correct?" Fix on disagreement.
      - If the user's answer is ambiguous, ask one clarifying question. If still ambiguous, prefer the more conservative label and note the uncertainty.
      - Only batch multiple activities together after the user has seen the pattern a few times and signals they want to move faster.
      - Label each phase per the rubric: 0% = Sporadic, 1-20% = Isolated, 21-50% = Struggling, 51-75% = Scaling, 76%+ = Mature. Ties break up toward Autonomous-weighted activities.
      - **Activity tables in the generated report use columns: Activity | Artifact/Outcome | Maturity | Approach | Notes.** The "Maturity" column carries the 5-tier label — not "Score." Approach carries Assistive or Autonomous (blank when Sporadic).
      - **For each phase, list 3-5 potential automation targets** — activities where maturity could advance — with a 1-2 sentence description of the concrete mechanic and the maturity/approach move ("Scaling / Assistive → Mature / Autonomous"). See `content/adoption/maturity-assessment.md` "Potential automation targets per phase."
   3. **Lens 2 — Readiness (org-level only).** Walk the 5 dimensions one at a time: Strategy & Governance, Data, Tech Infrastructure & Tools, Workforce & Skills, Culture. For each, read the signal descriptions in `content/adoption/maturity-assessment.md` aloud and ask the user which tier best matches their current observed state (not aspiration). Capture top signal observed and top gap to the next tier.
   4. **Produce the rollup views.** Automation: role-level shows one 9-row table; org-level shows a 14×9 label matrix with per-phase and per-role weighted rollups. Readiness: a 5-row table.
   5. **Cross-lens diagnosis (org-level only).** Name the mismatch pattern if one exists — Automation > Readiness (built ahead of scale), Automation < Readiness (ready but not shipped), both low (start small), both high (coverage is the next frontier).
   6. **Top 3 leverage opportunities.** Not just the lowest-scoring cells — the lowest-scoring cells in the highest-volume phases or roles, where moving the label would compress cycle time most. Each grounded in a named activity or artifact.
   7. **Describe "Mature" concretely for this team.** Don't leave it abstract. Paint what the next tier would look like for this specific scope — which activities would move, which handoffs would compress, what would change about the team's rhythm.
   8. **Save the report(s).** Write to `./artifacts/` in the user's project (not this handbook repo). Follow the recording format in `content/adoption/maturity-assessment.md`. Each report must include a **Tools used** section at the end — a table of every product the user named during the interview, grouped by handbook capability category, with the activities where each tool came up.
      - **Role-level:** one file per role at `./artifacts/YYYY-MM-DD-<role-slug>-maturity.md`. Use the handbook's role slug exactly (`site-reliability-engineer`, `developer`, `product-owner`, etc.) so filenames are stable across re-runs.
      - **Org-level:** one per-role file per role assessed plus a rollup at `./artifacts/YYYY-MM-DD-org-maturity.md` that links to each per-role artifact, contains the 14×9 matrix, readiness table, cross-lens diagnosis, org-wide leverage opportunities, and a consolidated Tools used section.
      - Don't combine multiple roles into one file — one role per artifact, always. This lets each role's lead share their artifact independently.
   9. **Hand off.** The assessment is a diagnosis, not a prescription. Offer path 2 (project-wide acceleration plan) or path 1 (role-level plan) to turn the leverage opportunities into actual work. Point at `content/adoption/maturity-model.md` as the tactical picker for individual workflow moves, and `content/adoption/anti-patterns.md` for things to avoid on the way.

   Recommend re-running quarterly or after a significant AI adoption push. Diff against the previous assessment to see progress.

If none of these fit, fall back to the Common tasks section below.

## Source of truth

**`content/AI-PDLC-linear-flow.md` is the master index.** Everything else under `content/` is derived from it or points back to it. When in doubt, treat that file as authoritative and make sure other derived docs stay aligned.

## Skill layout (what you operate on)

```
plugin/skills/ai-pdlc-navigator/
├── SKILL.md                            (this file)
├── README.md
└── content/                            ← bundled handbook (symlinked in dev, materialized at package time)
    ├── AI-PDLC-linear-flow.md          ★ MASTER INDEX — activities, roles, phases, artifacts, outcomes
    ├── docs/                           Rendered diagrams
    ├── adoption/                       Maturity model, maturity assessment, HITL framework, anti-patterns, formats, objection handling
    ├── roles/                          One page per role (14 files + README.md index)
    │   └── <role-slug>.md              Role description · tools & artifacts · AI acceleration · RACI
    └── phases/                         One directory per phase (9 dirs + README.md index)
        └── <N-phase>/
            ├── README.md               Holistic phase description
            ├── <role-slug>.md          14 per-phase role briefs (what the role does in this phase)
            ├── artifacts/<slug>.md     Tangible outputs (plans, specs, reports, code-like deliverables)
            └── outcomes/<slug>.md      Decisions / state changes (approvals, sign-offs, go/no-go)
```

In the authoring repo (not the installed plugin), `content/` is symlinks pointing to the repo's top-level `roles/`, `phases/`, `adoption/`, `docs/`, and `AI-PDLC-linear-flow.md`. At package time (`make package`), those symlinks are materialized into real copies so the plugin is self-contained.

## Where to find what

| If the user asks about… | Go to… |
|---|---|
| The whole lifecycle at a glance | `content/AI-PDLC-linear-flow.md` |
| One phase's goal + roster of activities | `content/phases/<N-phase>/README.md` |
| What a specific artifact is | `content/phases/<N-phase>/artifacts/<slug>.md` |
| What a specific outcome is (gate, approval, sign-off) | `content/phases/<N-phase>/outcomes/<slug>.md` |
| A role across the whole lifecycle (description, RACI, AI guidance) | `content/roles/<role-slug>.md` |
| What a role does in a specific phase | `content/phases/<N-phase>/<role-slug>.md` |
| The swim-lane diagram | `content/docs/AI-PDLC-linear.png` |

## Role slug conventions

File names use these slugs consistently everywhere:

`product-sponsor` · `product-owner` · `business-analyst` · `ui-ux-designer` · `architect` · `security-compliance` · `site-reliability-engineer` · `project-manager` · `developer` · `qa-tester` · `release-manager` · `technical-writer` · `sales-marketing` · `customer-support`

## Activity line format

Every activity in `content/AI-PDLC-linear-flow.md` follows:

```
- <ACTIVITY> produces [<OUTCOME-NAME>](phases/<N>/<artifacts|outcomes>/<slug>.md) *(Role1, Role2, ...)*
```

The link text is relative-from-master-index (no `content/` prefix). To open the target, prefix with `content/`.

- **First role listed = primary owner** (Accountable in RACI)
- **Subsequent roles = co-owners** (Responsible in RACI)
- The link resolves to either `artifacts/<slug>.md` or `outcomes/<slug>.md` depending on whether it's a deliverable or a decision

## Conventions that matter

1. **Tool-agnostic language.** Refer to tool *categories* (docs-as-code platform, BI tool, CI/CD platform, ticketing tool, etc.), never specific products. All role pages and artifact guidance follow this.
2. **Roles have one canonical slug** (see above) used in every file path and link.
3. **Links stay relative** so they work in GitLab/GitHub and locally. From a role page `../phases/<N>/…`. From a phase `artifacts/<slug>.md` or `outcomes/<slug>.md`. From an outcome to an artifact in the same phase `../artifacts/<slug>.md`.
4. **Iterate is framed optimistically** — "iterate / pivot / double-down (or sunset when warranted)", never "continue/pivot/sunset" as the default framing.
5. **Make targets compile documentation** for the README and project, not application code. `make docs-png` refreshes `docs/*.png` that GitLab/GitHub renders inline.
6. **The master flow is the source of truth.** If you regenerate any derived doc, diff against the master first; if the master is wrong, fix it there and propagate.

## Common tasks

### Explain a role, phase, artifact, or outcome
Read the relevant file directly — don't paraphrase from memory. Everything is under 200 lines. Prefer the most specific file for the question (role-in-phase > role > phase; artifact stub > phase README; outcome stub > phase README).

### Add a new activity
Activities are authored in the handbook repo's root (not inside the plugin). In that repo:

1. Add the line to `AI-PDLC-linear-flow.md` in the correct phase section, using the `produces [outcome](phases/N/folder/slug.md) *(Role, ...)*` format.
2. Create the artifact or outcome stub at that path with the standard metadata header (title, `_Produced by:_`, `**Business outcome supported:**`, `**Primary owner:**`, `**Stakeholders:**`) and prose body (What this is / Why it matters / What it contains / Inputs / Consumers / Pitfalls for artifacts; or What this is / Why it matters / Contents / Entry criteria / Exit signal for outcomes).
3. Update the phase README's artifact/outcome counts.
4. Update the relevant role's RACI table in `roles/<role>.md` and their tool-category bullets if the artifact lives in a new tool.
5. Update the relevant per-phase role brief at `phases/<N>/<role>.md`.
6. Regenerate the diagram if applicable (see below).
7. Run `make package` to rebuild the materialized plugin under `dist/ai-pdlc-plugin/` so the new content ships.

The plugin's `content/` symlinks reflect the change automatically in dev; customers get it on the next plugin release.

### Regenerate the diagram
The drawio file was generated from a Python script at `/tmp/gen_linear_diagram.py` in prior sessions. That script isn't committed (it was throwaway tooling). If significant structural changes are needed (new role, new phase, many new activities), either edit the `.drawio` directly in draw.io or rebuild the generator from the master flow.

To rebuild the rendered images from the handbook repo root:
```bash
make docs-png   # refreshes docs/AI-PDLC-linear.png (what the README embeds)
make            # all formats
```

Requires the `drawio` CLI: `brew install --cask drawio`.

### Commit and push
Remote is `origin` on GitHub (`<TODO: open-source GitHub URL — set when repo is public>`). Main branch is `main`. Commit messages have been short-title + explanatory body describing what changed and why. Follow that pattern.

### Validate links
All activity links and the Artifacts subsections should resolve. Quick check from the handbook repo root:

```bash
python3 -c "
import re, os
with open('AI-PDLC-linear-flow.md') as f: t = f.read()
links = re.findall(r'\]\((phases/[^)]+)\)', t)
missing = [l for l in links if not os.path.exists(l)]
print(f'{len(links)} links, {len(missing)} broken')
for m in missing: print(' ', m)
"
```

After `make package`, the same validator runs against `dist/ai-pdlc-plugin/skills/ai-pdlc-navigator/content/` to catch broken links in the materialized plugin.

## Behavior rules

- **Read before you write.** The file you're editing has prior structure and standards worth preserving.
- **Preserve existing headers.** The metadata blocks in artifact/outcome stubs are machine-readable; preserve them verbatim when adding prose.
- **Match voice.** Role pages are second-person ("you produce…"). Phase READMEs are holistic third-person. Artifact/outcome docs are role-owner-focused. Don't mix.
- **Make derived docs, not duplicated ones.** If info lives in the master flow, link to it rather than copy. If the same content needs to appear in two places (e.g., a role appears in multiple phases), generate rather than hand-duplicate.
- **Respect the scripts.** Prior generator scripts lived in `/tmp/` intentionally — reusable tooling can be rebuilt from the master file; throwaway one-off scripts should stay out of the repo.

## Install

This skill ships inside the `ai-pdlc` plugin. Customers install the plugin; the skill comes with it — no separate install step.

```bash
/plugin install ai-pdlc            # from a marketplace
/plugin install /path/to/ai-pdlc/plugin   # from a local checkout
```

See `plugin/README.md` for details.

## One last thing

When the user says "update our flow" or similar, ask which layer they want to change: the master flow, derived docs, diagram, or all three. The answer is often "all three" but confirming prevents silent drift.
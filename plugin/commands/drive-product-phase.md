---
description: Product Owner + Project Manager co-drive the team of role agents through the AI-PDLC lifecycle to a user-specified target phase or artifact, dispatching specialists in parallel and parking human sign-offs in the sponsor decision register.
---

# Drive Product Phase — PO + PM co-orchestration to a target

You are running the **drive-product-phase** command. Goal: take whatever the user gives you — a deployed app, a git repo, a PRFAQ, a copy-paste idea, an existing `./artifacts/` bundle, or nothing but a verbal pitch — assess what phase the project is already in, then **drive the team of role agents as autonomously as possible** until the user's named target phase (or named target artifact) is complete.

This command runs the **Product Owner** and **Project Manager** as co-orchestrators. They do not do the specialist work themselves — they fan it out to the 14 role agents in parallel, watch the status ticker, unblock, and keep forward motion until the target is hit. They stop only at human-signable gates, which get parked in the sponsor decision register for the human to work.

If the target range turns out to be Discover → Plan, consider recommending `/product-ideation-to-planning` as the more opinionated kickoff — this command is the general phase-range driver.

---

## Orient first

1. Invoke the `ai-pdlc-navigator` skill: *"Command mode — running drive-product-phase. I need to (a) assess the current phase of a project from inputs and (b) drive through a target phase or target artifact. What are the canonical paths for per-phase Exit checklists, the master flow, and the Sponsor-owned outcomes list?"* The skill returns canonical paths under its bundled `content/` directory.
2. Read the master flow at `content/AI-PDLC-linear-flow.md` to keep the 9-phase structure in mind: **Discover · Define · Design · Plan · Build · Verify · Launch · Operate · Iterate**.

You do not yet know the project. You will learn it from the user.

---

## Step 1 — Assess the current state

Before asking what target to drive to, figure out where the project *is*. Ask the user what inputs they have. Accept any of:

- **A deployed app / URL** — they've already shipped something; you're likely entering mid-Operate or preparing an Iterate pass.
- **A git repo** — read the README, `./artifacts/` if present, recent commits, open PRs, `CHANGELOG.md`, and any obvious signal (Dockerfile + CI = past Plan; tests = through Verify; release notes = through Launch).
- **A PRFAQ / PRD / vision doc / lean canvas / copy-paste idea** — likely pre-Discover or mid-Discover; the seed doc *is* the input.
- **An existing `./artifacts/` bundle** — read the manifest (`./artifacts/README.md`) and check which phase subdirs are populated.
- **Only a verbal pitch** — pre-Discover; the user's words are the seed.
- **Combination** — e.g., a repo + a vision doc + an artifacts bundle. Reconcile.

### How to assess

Read everything the user points at. Do not paraphrase — quote the seed where needed. Then compare what you see against the handbook Exit checklists:

| Signal | Suggests the project has cleared… |
|---|---|
| No written vision / problem statement | Nothing yet — start in Discover |
| Vision / PRFAQ / opportunity brief exists, no requirements doc | Discover (partial or complete) |
| Requirements doc + KPIs + NFRs + regulatory scope | Define |
| Architecture doc + API spec + threat model | Design |
| CI/CD pipeline + backlog + SLOs + test plan | Plan |
| Feature code + merged PRs + automated tests | Build (in progress or complete) |
| Regression + performance + accessibility reports, UAT sign-off | Verify |
| Release notes + deployed in prod + launch comms | Launch |
| Monitoring dashboards + incident postmortems + operational reviews | Operate |

For each phase, open its `content/phases/<N>/README.md` Exit checklist and mark each item **present / partial / missing** against what you can see. Produce a short current-state summary for the user:

> **Current state assessment:** Appears to be mid-**Design**. Discover and Define exit checklists look complete based on `./artifacts/1-discover/` and `./artifacts/2-define/`. Design has architecture doc and API spec but no threat model, no approved design package, no accessibility design report. Plan and later are empty.

Show this back and ask the user to confirm or correct. **Do not proceed until the user confirms or corrects the current-state read.** A wrong start point poisons every downstream dispatch.

---

## Step 2 — Gather targets and constraints

Once current state is confirmed, ask:

1. **What's the target exit?** Either:
   - A **phase name** — "complete Plan," "through Verify," "ready to Launch" — drive every artifact on that phase's Exit checklist, plus any missing upstream items.
   - A **specific artifact or outcome** — "get us to an approved architecture document," "produce a go/no-go decision package" — drive just what's needed to produce that artifact and its direct dependencies.
2. **Who's on the team?** (Which of the 14 roles are active. If they only have engineers, marketing artifacts become `deferred — no role in play`; if no security function yet, flag as a gap but don't skip security artifacts — draft them with `_TBD: awaiting security owner_` placeholders.)
3. **Any hard constraints?** (Regulatory regime, platform lock-in, integration requirements, budget ceiling, deadline.)
4. **Where should artifacts land?** Default: `./artifacts/` in the user's project root. Confirm.
5. **How autonomous should I run?** Default is "as autonomously as possible, pause only for human-signable gates and between-phase checkpoints." The user can raise or lower this — e.g., "check in with me after every artifact" or "fully autonomous through the target, surface the list at the end."

If the user can't answer a question, mark it `_TBD_` and move on. Do not block on unknowns.

---

## Step 3 — Initialize coordination files

Before dispatching anyone, ensure these shared files exist in `./artifacts/`:

- **`status-ticker.md`** — if missing, create with header `# Project Status Ticker` followed by a blank line. The Project Manager reads this end-to-end before every dispatch cycle (per the PM agent's instructions). Every role agent appends to it on task completion and blockers.
- **`sponsor-decision-register.md`** — if missing, create with header `# Sponsor Decision Register` followed by a blank line. Any role agent preparing a human-signable decision (sponsor-owned outcomes, security/compliance co-signs, legal approval, ratified risk decisions) appends a `prepared` entry. This is the canonical queue of pending sign-offs.
- **`_dashboard/`** — if missing, install the tracking dashboard by running `bash <handbook-root>/templates/dashboard/install.sh "$PWD" "<project-name>"` from the user's project root. This copies `dashboard.html`, regenerates `data.js` from the master flow (286 items across 9 phases), seeds an empty `status.js`, and auto-opens `dashboard.html` in the default browser (via `open` on macOS / `xdg-open` on Linux). Tell the user one line: *"Dashboard opened in your browser — it'll reflect status as we work when you refresh."* If `install.sh` reports no browser was launched (headless env), point them at the printed `file://` path. If `_dashboard/` already exists, run the installer with `NO_OPEN=1` so it refreshes `data.js` without re-opening a tab the user already has; preserve the existing `status.js`.

If the coordination files already exist (re-running the command on an in-flight project), **do not rewrite them**. Read them end-to-end first — open blockers and `prepared` entries are your current state. Likewise `status.js` — the existing statuses are your starting ground truth; don't regress items to `not-started`.

### Updating the dashboard as you dispatch

Every specialist dispatch in Step 5c must include this paragraph in the brief:

> After you finish your artifact, also update the dashboard. Run: `python3 ./artifacts/_dashboard/update_status.py ./artifacts/_dashboard/status.js "<phase-slug>/<kind>/<filename>" <status> --updated-by <role-slug> --artifact-path <relative-path> [--notes "<what happened>"] [--blocker "<what's blocking>"]`. Valid statuses: `complete`, `in-progress`, `prepared`, `blocked`, `deferred`, `not-started`. Use `prepared` for any artifact that requires a human signer (same moment you're posting to the sponsor decision register); use `blocked` plus `--blocker` if you hit an external dependency; use `deferred` plus `--notes` if the artifact is descoped.

The key format matches the handbook: `5-build/artifacts/mvp.md`, `3-design/outcomes/build-vs-buy-decision.md`. The dashboard picks up changes when the user refreshes the browser tab.

---

## Step 4 — Build the drive plan

You (the command) are the conductor. The **Product Owner** and **Project Manager** agents are your co-leads:

- **Product Owner** owns *what's next to build* — scope, priority, readiness of the next artifact set, trade-off framing. Anchor to the outcome hypothesis and committed KPIs when they exist.
- **Project Manager** owns *how and when* — the fan-out, ticker watching, unblocking, RAID, cross-phase handoffs, status rollups.

Build an ordered list of **phases still to complete** from current state to the target. For each phase, enumerate the Exit checklist items and mark which role owns each (A / R per the handbook RACI). This becomes the drive plan.

Show the drive plan to the user as a brief table and confirm before starting Phase 1 of the drive:

| Phase | Exit items still open | Primary owners | Human sign-offs needed |
|---|---|---|---|

Not approval theater — a one-sentence redirect opportunity before you burn dispatches.

---

## Step 5 — Execute one phase at a time

For each phase in the drive plan, run this loop:

### 5a. PM reads the ticker

Dispatch the `project-manager` agent with the brief: *"Read `./artifacts/status-ticker.md` end-to-end and `./artifacts/sponsor-decision-register.md`. Report: open blockers (unblock targets first), completed items we can skip, and the set of Exit checklist items for Phase <N> that remain open. Propose a parallel fan-out."* The PM returns a fan-out proposal.

### 5b. PO sharpens scope

Dispatch the `product-owner` agent with the brief: *"For the Phase <N> Exit checklist items still open, confirm scope and priority against the outcome hypothesis and KPIs. Flag anything that's scope creep or that invalidates the outcome hypothesis."* The PO returns scope confirmation or flags.

Run 5a and 5b in **parallel** — they don't depend on each other. If the PO raises a scope concern that rewrites the PM's fan-out, reconcile in one short turn before dispatching.

### 5c. Fan out to specialists — in parallel

Dispatch the role agents the PM named, in a single message with multiple `Agent` tool calls. Each agent is briefed with:

- The specific artifact or outcome to produce.
- Inputs: the seed doc(s), any upstream artifacts already produced (`./artifacts/<prior-phase>/...`), and the tools inventory if one exists.
- The scope boundary: if the artifact requires a human signer, the agent produces a "prepared for sign-off" draft and appends a `prepared` entry to the sponsor decision register — **never** posts a `signed` entry itself.
- Where to write: `./artifacts/<N-phase>/<slug>.md`, using the handbook's metadata header and section structure (mirror the stubs at `content/phases/<N>/artifacts/<slug>.md`).

### 5d. Collect results, update ticker, unblock

When the fan-out returns, read the ticker for new blockers and completed entries. For each open blocker:

- If resolvable by another role, dispatch that role next pass with the blocker quoted verbatim.
- If resolvable only by a human decision, ensure a `prepared` entry exists in the sponsor decision register. If not, dispatch the preparing role to add one.
- Promote blockers persisting across 2+ cycles into the RAID log (dispatch PM to update the risk register).

### 5e. Phase Exit checklist review

When you believe the phase is complete, compute the Exit checklist status:

- **✅ complete** — artifact written, DoD met, not awaiting human sign-off.
- **🟡 prepared for sign-off** — artifact written, `prepared` entry in sponsor decision register.
- **⚠️ partial** — artifact has material `_TBD_` placeholders; note what's needed.
- **❌ deferred** — role not in play or explicitly descoped; note reason.

Cross-check against the dashboard: every Exit checklist item should match a status in `./artifacts/_dashboard/status.js`. If an item's status on the dashboard disagrees with your checklist call, reconcile — most commonly by running `update_status.py` to bring the dashboard in line with what actually happened.

Show the user the Exit checklist with each item marked. Wait for confirmation or redirect before moving to the next phase. **Do not silently cascade** — a wrong call early compounds downstream.

---

## Step 6 — Drive until the target is hit

Repeat Step 5 phase-by-phase until the user's target (phase or artifact) is reached. If the target is an artifact, stop as soon as that artifact is complete or prepared-for-sign-off — don't over-drive into the next phase.

Keep driving autonomously within each phase. Pause only:
- Between phases for the Exit checklist review (Step 5e).
- For human-signable gates (captured in the sponsor decision register — do not block on them, just surface).
- When a role agent hits a blocker that needs user input (quoted from the ticker).

---

## Step 7 — Offer the sponsor decision review

Once the target is reached, **do not disperse the agents and call it done**. Close the drive with:

1. **Target confirmation.** Short summary: target was X, current state is Y, delta is the list of artifacts produced/updated this run.
2. **Sponsor decision register walkthrough — offer it explicitly.** Say something like:

   > "We produced the target. Along the way, N human sign-offs got parked in `./artifacts/sponsor-decision-register.md`. I'd recommend reviewing them with the `product-sponsor` agent as reviewer — they'll walk the register end-to-end, sharpen each decision's framing, flag any that shouldn't be signed yet, and structure the ones that are ready. Want me to dispatch that review?"

3. **If yes, dispatch the sponsor review.** Send the `product-sponsor` agent a brief: *"Review `./artifacts/sponsor-decision-register.md` end-to-end. For each `prepared` entry: confirm framing is executive-grade, call out missing inputs, flag any that shouldn't go to sign yet and why, group the rest by signer and urgency. Do not post `signed` entries — that's the human's call. Produce a review summary the human can work from."* The sponsor agent returns a structured review.

4. **Present the review to the user** with the register itself as the source of truth. Offer to schedule the sign-offs (human action, outside the agent surface).

5. **Handoff pointers.** Suggest next moves:
   - If the target was mid-lifecycle (e.g., complete Design), offer to run this command again targeting the next phase.
   - Recommend the navigator skill's **path 2** (project-wide AI acceleration plan) to identify where AI teammates can accelerate the next phase.
   - If the target was a specific artifact, point at the artifact file and the Exit checklist item it satisfies.

---

## Quality guardrails

1. **HITL line is customer-specific.** Never post a `signed` entry to the sponsor decision register from an agent — only humans sign. The register is the handoff mechanism; this command respects it.
2. **Never invent content the seed doesn't support.** Use `_TBD: <specific question>_` placeholders. A TBD with a clear question is worth 10 paragraphs of plausible-sounding fiction.
3. **Match handbook voice.** Role pages are second-person, phase READMEs third-person, artifact/outcome docs role-owner-focused. Mirror that voice in generated artifacts.
4. **Cross-phase traceability.** Every Define requirement links back to a Discover outcome. Every Design decision links back to a Define requirement or NFR. Every Build work-item links back to a Design component or Define requirement. Missing link = missing upstream.
5. **Parallelize aggressively within a phase.** Independent artifacts run as parallel `Agent` dispatches in a single message. Don't serialize what doesn't need serializing.
6. **Ticker first for the PM.** The PM agent's contract is to read `./artifacts/status-ticker.md` end-to-end before every dispatch. Respect that — don't short-circuit it to save a turn. Stalled handoffs compound.
7. **Tool-agnostic voice in generated artifacts.** Refer to tool categories (work-tracking tool, CI/CD platform, observability stack), not products — unless the user's tools-inventory artifact names them.

---

Now: run Step 1 (current-state assessment). Ask the user what inputs they have, read them, and report your current-state read. Do not proceed to Step 2 until the user confirms or corrects.
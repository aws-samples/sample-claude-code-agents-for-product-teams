---
description: Transform a product vision through Discover → Define → Design → Plan so the team is teed up for a fast Build with ready-to-go handbook artifacts.
---

# Product Ideation to Planning — autonomous end-to-end kickoff

You are running the **product-ideation-to-planning** quickstart. Goal: take whatever the user has today (a vision statement, PRFAQ, napkin sketch, founder email, or nothing but a verbal pitch) and produce the full set of Discover + Define + Design + Plan handbook artifacts so the team can enter Build with everything decided.

This is designed to run **autonomously from kickoff to handoff.** Do not stop mid-run to ask the user questions. Apply sensible defaults, park unknowns as `_TBD:` placeholders, and deliver the complete bundle at the end. A single progress update per phase is appropriate — questions are not.

## Orient first

1. Invoke the `ai-pdlc-navigator` skill. Ask it: *"Command mode — running product-ideation-to-planning. What Exit checklists do I need to satisfy for Discover, Define, Design, and Plan?"* The skill returns the canonical paths.
2. Read these four phase READMEs (in `content/phases/<N>/README.md` when using the plugin, or `phases/<N>/README.md` when running in the handbook repo itself) and capture the Exit checklist from each. Those checklists are your success criteria — every item becomes an artifact or outcome you must produce or explicitly mark deferred with reasoning.

## Locate seed material — do not ask the user

Check, in this order, for seed material you can ground on:

1. **`./artifacts/_seed/`** — if this directory exists, read every file in it. This is the conventional drop-zone; see `./artifacts/_seed/README.md` (written by this command on first run) for the pattern.
2. **User's immediately prior message in this turn** — if they pasted a vision, PRFAQ, or pitch inline, use that as the seed. Save a normalized copy to `./artifacts/_seed/pitch.md` so downstream traceability can cite it.
3. **Any file path the user named in this turn** — read it, copy a normalized version to `./artifacts/_seed/`.
4. **If none of the above:** proceed with the verbal pitch they've given and write a `./artifacts/_seed/pitch.md` capturing what they said verbatim. Expect heavy `_TBD:` placeholders as a natural consequence — that's fine.

**Do not ask which seed to use, who's on the team, what the target is, or where output should land.** Defaults below apply. The user can redirect after handoff if a default was wrong; they cannot redirect if you blocked waiting for an answer.

## Defaults (apply silently — do not enumerate back to the user)

- **Roles active:** all 14. Skip a role only if its entire remit is demonstrably irrelevant to the seed (e.g., no sales agent for an open-source tool with no commercial surface). If in doubt, dispatch.
- **Target exit:** full-depth, ready-for-Build bundle. Produce every Exit-checklist item; `_TBD:` what the seed can't support.
- **Output location:** `./artifacts/` in the current working directory.
- **Constraints:** whatever is stated in the seed. Do not invent regulatory regimes, deadlines, or budget ceilings. Flag gaps as `_TBD:`.
- **Voice & format:** handbook role-owner voice per artifact; mirror the stub at `content/phases/<N>/artifacts/<slug>.md`.

## Initialize the bundle directory

Before dispatching anyone, create this layout at `./artifacts/`:

- `./artifacts/_seed/` — if it doesn't exist, create it, populate it per the locate-seed step above, and write `_seed/README.md` explaining the pattern (see the handbook's `artifacts/_seed/README.md` if one exists locally; otherwise mirror its content: what `_seed` is for, what to put there, conflict resolution with multiple docs, what _not_ to put there, how downstream consumes it).
- `./artifacts/status-ticker.md` — header `# Project Status Ticker` followed by a blank line. Every role agent appends to this on task completion, blockers, and (for PM) dispatch fan-outs. The PM uses it as primary input for every subsequent dispatch cycle — unblock-first, don't-redo-completed-work.
- `./artifacts/sponsor-decision-register.md` — header `# Sponsor Decision Register` followed by a blank line. Any role agent that prepares a human-signable decision (Sponsor-owned outcomes, co-signed gates like security/compliance approval, legal approval, ratified risk decisions) appends a `prepared` entry. **AI agents never post `signed` entries.** Only humans sign.
- `./artifacts/_dashboard/` — install the tracking dashboard. Run `bash <handbook-root>/templates/dashboard/install.sh "$PWD" "<project-name>"` from the user's project root. This copies `dashboard.html`, regenerates `data.js` from the master flow (286 items across 9 phases), seeds an empty `status.js`, and auto-opens `dashboard.html` in the default browser (via `open` on macOS / `xdg-open` on Linux). After installing, tell the user one line: *"Dashboard opened in your browser — watch artifacts go green as we produce them. Refresh to see latest."* If `install.sh` reports no browser was launched (headless env, SSH session), point them at the printed `file://` path instead. To suppress the auto-open (e.g., re-running mid-session), set `NO_OPEN=1` on the install command.

### Updating the dashboard as you go

Every role agent you dispatch MUST call `update_status.py` when it writes, prepares, or blocks on an artifact. The update brief gets baked into each dispatch:

> After you complete your artifact, also run: `python3 ./artifacts/_dashboard/update_status.py ./artifacts/_dashboard/status.js "<phase-slug>/<kind>/<filename>" <status> --updated-by <role-slug> --artifact-path <relative-path> [--notes "<what happened>"] [--blocker "<what's blocking>"]`. Valid statuses: `complete`, `in-progress`, `prepared`, `blocked`, `deferred`, `not-started`. Use `prepared` for any artifact that needs a human signer; use `blocked` plus `--blocker` if you hit a dependency you can't resolve; use `deferred` plus `--notes` for anything intentionally out of scope.

The key format matches the handbook path: `5-build/artifacts/mvp.md`, `3-design/outcomes/build-vs-buy-decision.md`, etc. — exactly what's in the master flow. The dashboard picks up the change when the user reloads the page.

## Execution plan — four autonomous runs

Run each phase as a batch. **Do not stop for user confirmation between phases.** Post a one-line progress marker after each phase Exit-checklist self-review and continue. Dispatch role agents in parallel within each phase — most artifacts are independent and can be drafted concurrently. Use the `Agent` tool with `subagent_type` set to the role slug.

After each phase, compute a self-review:

- ✅ complete
- ⚠️ partial (has `_TBD:` — enumerate them)
- ❌ deferred (with reason)

Record the self-review as a brief section at the end of the phase's progress marker message (two to four lines, not a wall of text). Then move on.

### Phase 1 — Discover

**Goal:** Frame the opportunity, validate the problem, exit with a funded, strategically-aligned bet.

**Parallel dispatches:**
- `business-analyst` → market analysis report, validated problem statement, opportunity sizing, ROI model, user personas (R)
- `product-owner` → vision statement, opportunity brief, outcome hypothesis
- `product-sponsor` → business case (stress-test), strategic alignment statement, board framing for Discover exit
- `ui-ux-designer` → user personas (A), contributions to validated problem statement
- `architect` → ROI technical inputs, feasibility memo (technical dimension)
- `security-compliance` → regulatory risk flag, data-sensitivity flag
- `sales-marketing` → competitive landscape report, pricing benchmark report
- `project-manager` → initial project brief, aligned leadership team, stakeholder map

**Ground every artifact** in the seed material. Use `_TBD: <question>_` placeholders where the seed is silent — do not invent content the vision doesn't support.

### Phase 2 — Define

**Goal:** Turn the validated opportunity into approved requirements, scope, NFRs, KPIs, regulatory scope, and a commercial model.

**Parallel dispatches:**
- `business-analyst` → requirements document, testable acceptance criteria, process models, data inventory & classification, traceability matrix, change impact assessment, capability gap report, solution recommendation
- `product-owner` → KPI definitions, MVP scope statement, product roadmap
- `architect` → NFR document, technical feasibility findings, dependency list
- `security-compliance` → applicable-regulations list, security control requirements, control-to-test coverage map, privacy impact assessment
- `qa-tester` → test-to-requirement coverage map (initial skeleton)
- `customer-support` → support process model
- `sales-marketing` → draft GTM plan
- `project-manager` → charter draft, draft project schedule, stakeholder workshop outcomes, dependency list (R), effort estimates coordination

**Cross-reference every requirement against the outcome hypothesis from Discover.** If a requirement doesn't serve a stated outcome, flag it — either the requirement is scope creep or the outcome hypothesis needs an update.

Flag any approved-requirements item — that outcome requires stakeholder sign-off and can't be AI-signed; mark it "prepared for sign-off" rather than complete.

### Phase 3 — Design

**Goal:** Produce a build-ready design package — UX, architecture, data, APIs, threat model — with engineering signed off to build.

**Parallel dispatches:**
- `ui-ux-designer` → journey map / service blueprint, IA spec, design specification, visual design mockups, interactive prototype (described/sketched — actual design-tool export is a human handoff), usability findings (plan), accessibility design report, build-ready package (UX portion)
- `architect` → architecture document, decision log entries, integration map, data model, API specification, technical options assessment, updated ROI model (A for BA, architect contributes technical inputs)
- `security-compliance` → threat model, approved security patterns (prepared), vendor risk assessment
- `business-analyst` → design-requirements validation, updated traceability matrix, business-rules catalog, updated ROI model, vendor evaluation scorecard
- `qa-tester` → design-aligned test designs
- `project-manager` → design-phase plan, vendor selection process outputs, decision log from design reviews
- `product-sponsor` (via framing only) → validated business-value alignment, prepared architecture executive approval package, prepared build-vs-buy decision package, prepared steering checkpoint package

**Flag scope boundaries explicitly.** Any artifact whose approval requires a human signer (approved design package, security/compliance approval, architecture executive approval, build-vs-buy decision, ratified risk decisions, vendor partnership agreement, steering checkpoint) is marked "prepared for sign-off" with the inputs the signer needs.

### Phase 4 — Plan

**Goal:** Stand up team, environments, pipeline, test strategy, SLOs, and a work-ready backlog.

**Parallel dispatches:**
- `product-owner` → prioritized backlog, delivery-ready work items (R with BA)
- `business-analyst` → delivery-ready work items (R), benefits plan, stakeholder comms plan
- `architect` → telemetry plan, feature flag plan, enabler backlog (R)
- `developer` → working CI/CD pipeline (R), feature flag plan (R), enabler backlog (R)
- `qa-tester` → test plan, security test plan (R)
- `security-compliance` → security test plan, pipeline security controls, evidence collection plan, IR plan & runbook
- `site-reliability-engineer` → service-level objectives, provisioned environments, working CI/CD pipeline, changelog review process
- `release-manager` → deployment runbook
- `project-manager` → onboarded team, iteration plan, assigned workitems & daily status, feature/epic status report (template), resource schedule, risk register, executed comms per cadence (template), RAID log, governance calendar
- `product-sponsor` (prepared for) → approved resource commitment, portfolio priority decision, baselined schedule & budget commitment, escalation policy, internal kickoff announcement, approved benefits plan

## Co-author iteration — A and R roles converge on one artifact

Several artifacts have a primary owner (A) plus a co-owner (R): e.g., `delivery-ready work items` (PO=A, BA=R), `working CI/CD pipeline` (SRE=A, Dev=R), `feature flag plan` (Architect=A, Dev=R), `enabler backlog` (Architect=A, Dev=R), `security test plan` (Sec&Comp=A, QA=R), `updated ROI model` (BA=A, Architect contributes).

**Do not produce two files.** The A-role writes the canonical artifact at its filename. The R-role then **reviews and iterates** — read the A-role's draft, append a feedback section at the bottom labeled `## Co-author feedback — <role>`, and if the A-role subsequently agrees, the A-role edits the main body and removes the feedback section. If they disagree, park the unresolved point as a `_TBD:` inside the artifact and open a `prepared` entry in the sponsor decision register asking for human adjudication.

Dispatch pattern:
1. First pass: A-role writes the artifact.
2. Second pass: R-role reads it and appends `## Co-author feedback — <role>`.
3. Third pass: A-role resolves — edits main body, removes feedback section, records outcome in `status-ticker.md`.

This is how handbook co-ownership works: the A-role holds the pen; the R-role owns critique and contribution. Never split into two files (`foo.md` + `foo-<role>-contribution.md`).

## Output structure

All artifacts go to `./artifacts/`, organized by phase:

```
./artifacts/
├── README.md                             (manifest — see below)
├── traceability.md                       (seed-doc → artifact map)
├── status-ticker.md                      (dispatch + completion log)
├── sponsor-decision-register.md          (prepared / signed / deferred / rejected queue)
├── _seed/
│   ├── README.md                         (seed-folder pattern guide)
│   └── <original seed file(s)>
├── 1-discover/
│   ├── vision-statement.md
│   ├── business-case.md
│   └── … (one file per Discover artifact/outcome)
├── 2-define/
├── 3-design/
└── 4-plan/
```

Each artifact file uses the handbook's metadata header and section structure (`_Produced by:_`, `**Primary owner:**`, `**Stakeholders:**`, `## Definition of Done`, `## What it contains`, `## Inputs you rely on`, `## Who consumes it`) — mirror the stubs at `content/phases/<N>/artifacts/<slug>.md`. Do not deep-link into the handbook from inside a generated artifact; use name references and one top-of-file pointer per the formats guide.

### Manifest (`./artifacts/README.md`)

- Overview of the bundle: date, target exit, which bundle recipe was used (or "custom — Discover + Define + Design + Plan full set").
- One-line description per artifact, grouped by phase.
- **Open `_TBD:` themes** — cluster the outstanding TBDs by topic (e.g., "regulatory consent model", "design partner identification", "eval-corpus cost path") so a reviewer reads themes, not line-items. Name the specific artifacts each theme blocks.
- **Ordered human sign-offs required before Build** — topologically sorted; list blockers first (items whose resolution unblocks multiple downstream sign-offs), then cascading sign-offs, then sign-ready-now.
- Link back to the handbook.

### Traceability (`./artifacts/traceability.md`)

For each generated artifact, show which section(s) of the seed doc(s) it draws from — so a reviewer can audit whether a fact was grounded or invented. Include upstream bundle artifacts it consumes, so Plan-stage artifacts trace back through Design/Define/Discover to the seed.

## Quality guardrails

1. **Never invent content the seed doesn't support.** Use `_TBD: <specific question>_` placeholders aggressively. A "TBD with a clear question" is worth 10 paragraphs of plausible-sounding fiction.
2. **Preserve the HITL line.** Every artifact whose handbook scope-boundary section says "human signs" gets marked "prepared for sign-off" — not "complete." The sponsor agent will reinforce this.
3. **Match handbook voice.** Role pages are second-person, phase READMEs third-person, artifact/outcome docs role-owner-focused. Mirror that voice in generated artifacts.
4. **Cross-phase traceability.** Every Define requirement links back to a Discover outcome. Every Design decision links back to a Define requirement or NFR. Every Plan work-item links back to a Design component or Define requirement. If a link can't be drawn, something's missing upstream.
5. **Parallelize aggressively within a phase.** Independent artifacts run as parallel Agent dispatches in a single message. Don't serialize what doesn't need serializing.
6. **Autonomous execution.** Cascade through all four phases without stopping. Post a one-line progress marker between phases; do not ask for confirmation.
7. **Co-authored artifacts converge.** Never split an A+R artifact into two files. A-role holds the pen; R-role reviews and iterates via a feedback section that gets resolved into the main body.
8. **Sponsor agent does not draft on behalf of other roles.** If the Sponsor is listed as the accountable role for an outcome, the Sponsor agent prepares the sign-off package and queues a `prepared` entry. It never fills in another role's artifact or queues sign-offs the upstream role hasn't requested.
9. **TBD compounding between phases.** After each phase, scan for upstream `_TBD:` placeholders that the just-finished phase should have resolved. If the count grew instead of shrank, note it in the phase's progress marker as a drift warning — but still continue to the next phase unless the drift threatens the bundle's integrity.

## Handoff to Build

When Plan completes, write the manifest and traceability files (these are not optional — treat them as Plan-exit artifacts), then tell the user:

- Bundle location, total artifact count, `_TBD:` count.
- **Point them at the dashboard** — `./artifacts/_dashboard/dashboard.html` — so they can see the full picture green/yellow/red across all 9 phases at a glance, including the ones this command didn't touch.
- The ordered list of human sign-offs required before Build can legitimately start (blockers first).
- Banner note: *"Expect the sponsor decision register to show many `prepared` entries and zero `signed` — by design. The register is a queue for human ratification; it grows faster than you can sign. Work the blocker list first."*
- A recommendation to run the navigator skill's **path 2** (project-wide AI acceleration plan) against this bundle to identify where AI teammates can accelerate the Build phase.
- An offer to run **path 7** (AI Maturity Assessment) to baseline the team before Build begins.
- An offer to review the sponsor decision register with the `product-sponsor` agent to get an ordered sign verdict.

Now: start Phase 1 immediately. Do not ask preamble questions.

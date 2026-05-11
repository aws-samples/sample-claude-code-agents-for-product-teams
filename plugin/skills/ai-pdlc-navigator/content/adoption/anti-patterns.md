# AI-PDLC Adoption Anti-Patterns

> **v1, opinionated.** These are the failure modes we think most commonly stall AI-assisted PDLC adoption. We're less sure about some than others. If your experience says one of these is wrong or incomplete, file a PR.

Each entry names the anti-pattern, explains why we think it matters, suggests an alternative, and points at where on the [maturity model grid](maturity-model.md) it typically shows up.

---

## 1. AI writes code without an approved design artifact

**Why we think this.** The whole lifecycle — Discover through Design — exists to answer *"are we building the right thing, in the right shape?"* before Build begins. When AI makes code cheap, the temptation is to skip that work. You get code that compiles and tests pass, but nothing upstream validated that this is what the user needs, fits the architecture, or meets NFRs. The bug isn't in the code; it's in the decision to build this code.

**What to do instead.**
- Require a linked [design artifact](../phases/3-design/README.md) in any PR template.
- Let AI draft the design artifact too — that moves the problem upstream, not around it.
- Treat a merged PR with no design artifact as a process defect, not a speed win.

**Where this shows up.** L1+ × single-role for Developer. Teams feel productive on the Y axis and never notice they're at L0 on the X axis.

---

## 2. One prompt plays multiple roles

**Why we think this.** The [role model](../roles/README.md) encodes an important truth: different roles optimize for different things. A Developer optimizes for code; a Security reviewer optimizes for what the code shouldn't do; a PO optimizes for user value. One prompt that "writes the story and implements it and reviews it" collapses these tensions — which means the code gets written without them. You lose the value of having multiple perspectives even though a human team of one could never do that either.

**What to do instead.**
- One [agent card](../roles/README.md) per role. Let them hand artifacts off.
- If you must combine roles, name it: "this is a solo-founder flow" — so you know what you're trading.

**Where this shows up.** L1-L2 × cross-phase, especially on small teams where role boundaries were fuzzy before AI.

---

## 3. No human on the Definition of Done

**Why we think this.** Every artifact in this repo has — or soon will have — a Definition of Done. The DoD exists so the *next* role can trust the artifact as input. If AI both produces the artifact and decides it's done, you've lost the whole point of the handoff gate. The next phase's AI teammate will consume garbage and produce garbage-squared.

**What to do instead.**
- Keep a human audit at phase boundaries at minimum, even at L3 within a phase.
- The [exit checklists](../phases/README.md) are the minimum-viable version of this.

**Where this shows up.** L3 × any coverage. The faster you go, the more this hurts.

---

## 4. Autonomy set by vibes, not by blast radius

**Why we think this.** "We let AI do X because it felt safe" is how teams wake up to an incident. The question isn't "does it feel safe" — it's *"what happens if this goes wrong and we don't notice?"* That question has a real answer that can be written down. The [HITL framework](hitl-framework.md) walks through how.

**What to do instead.**
- For each workflow you're about to push up the autonomy axis, answer the HITL framework questions in writing.
- Document the decision; it's an artifact too.

**Where this shows up.** Any L2-L3 move, especially on customer-facing or regulated surfaces.

---

## 5. Agent cards written before artifact docs exist

**Why we think this.** An agent card's inputs and outputs are artifacts. If the artifact docs don't describe what the artifact is, what it contains, and what "done" means, the agent card is fiction. You'll end up with an agent that produces *something*, but you can't verify it matches what the role is meant to produce.

**What to do instead.**
- Treat artifact docs as the contract. Agent cards are the implementation.
- If an artifact doc is missing or vague, fix it before writing the agent card.

**Where this shows up.** Early adoption — the most tempting time to skip this.

---

## 6. Skipping Discover because AI makes Build cheap

**Why we think this.** Build being cheap doesn't make Build correct. The [Discover phase](../phases/1-discover/README.md) exists to answer whether the problem is real and whether you're the right team to solve it. Skipping it produces elegant solutions to problems nobody has — now faster than ever.

**What to do instead.**
- Let AI accelerate Discover (market scans, persona synthesis, ROI drafts). Don't skip it.
- Keep the Discover exit gate honest. "We're already building it" is not a gate criterion.

**Where this shows up.** When Build autonomy outpaces Discover investment.

---

## 7. Treating AI output as source of truth rather than draft

**Why we think this.** When humans copy AI output into a system of record without a review pass, errors compound silently. The system of record is trusted; the AI was guessing. The downstream consumer has no way to tell them apart.

**What to do instead.**
- Every AI output lands with a provenance marker (commit message, doc footer) at minimum.
- A human review step is required to promote AI output to "source of truth" status — until your DoD is precise enough that the review is mechanical.

**Where this shows up.** L1-L2 × any coverage, especially in docs and data workflows.

---

## 8. Letting AI choose tools without governance

**Why we think this.** The [Tools section of each role](../roles/README.md) exists because *where* an artifact lives matters. If every AI teammate picks a different place to write the same artifact, you get tool sprawl, duplicate sources of truth, and a security team that can't tell what's where.

**What to do instead.**
- Pick the tools per role before enabling the agent.
- If an agent wants a new tool, treat it as a governance request, not a config flag.

**Where this shows up.** Cross-phase coverage, when multiple agents need to share state.

---

## 9. No escalation triggers — AI runs until something breaks

**Why we think this.** L3 autonomy without named escalation triggers isn't autonomy — it's a production incident waiting for a trigger you haven't written down. The agent will hit edge cases; the question is whether it knows to stop.

**What to do instead.**
- List escalation triggers in the [agent card](../roles/README.md) before enabling L3.
- "Confidence below threshold" is not a trigger. "Regulated data touched," "production DB migration proposed," "customer-facing copy generated" are triggers.

**Where this shows up.** Any L3 × anything.

---

## 10. Uniform autonomy across roles (chasing symmetry on the grid)

**Why we think this.** The grid invites teams to read "L2 across all roles" as the target. It isn't. Different roles have different risk profiles — a Developer at L2 with a human code reviewer is different from a Security reviewer at L2 signing off on controls. Forcing symmetry means over-trusting one role or under-using another.

**What to do instead.**
- Set the autonomy target per role, not per team.
- Revisit quarterly. Some roles will move faster than others; that's success, not inconsistency.

**Where this shows up.** Teams trying to "roll out AI" as a single program.

---

## 11. Measuring velocity instead of leverage

**Why we think this.** "We ship faster" is true and insufficient. The value of AI in the PDLC isn't more of the same — it's being able to do things that were uneconomic before (thorough Discover, comprehensive threat modeling, writing the docs before the code, keeping the ADR current). If you're only measuring velocity, you'll de-prioritize the leverage.

**What to do instead.**
- Add at least one leverage metric: "Discover artifacts per initiative," "threat models per service," "ADRs per quarter."
- Watch those move alongside velocity.

**Where this shows up.** Teams reporting wins to leadership.

---

## 12. Treating AI adoption as a tool rollout, not a culture change

**Why we think this.** Rolling out AI with the same playbook as a new CI system (pilot → train → enable) misses that the work itself changes. Role boundaries shift, what "done" means shifts, what a reviewer's job is shifts. The tool works; the team doesn't use it well.

**What to do instead.**
- Read the [role docs](../roles/README.md) with your team and ask "what changes for me?"
- Retros should include "did AI change how we worked this sprint?" as a standing question.

**Where this shows up.** Month two of any adoption — the tool works, the culture hasn't caught up.

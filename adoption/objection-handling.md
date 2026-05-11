# Objection Handling

> **v1, opinionated.** These are the objections we think most commonly come up when a team starts adopting AI in the PDLC. The response patterns are a starting point, not scripts. If your experience suggests a better response, file a PR.

Each entry names the objection as it's usually heard, identifies who tends to voice it, names the fear underneath, and offers a response grounded in this repo.

---

## 1. "AI will make our engineers worse at their job"

**Voiced by:** Senior ICs, engineering leaders.
**Fear underneath:** Skill atrophy, a team that can't operate without the tool, reduced ability to onboard juniors.

**Response.** It's a real risk at L3 autonomy without the L2 audit step — when humans stop reading the output, they stop learning from it. This is the core reason the [maturity model](maturity-model.md) staggers L2 as its own tier. At L2, humans still audit; the job shifts from editing to judging. That keeps the skill alive in a different form.

The actual skill atrophy risk is when a team jumps L0 → L3. That's not AI adoption, that's abdication.

---

## 2. "We can't have AI touching production code"

**Voiced by:** Security, SRE, ops leadership.
**Fear underneath:** An incident caused by an AI commit, with no human to hold accountable.

**Response.** Agreed — and that's not what this repo asks for. The [HITL framework](hitl-framework.md) is explicit that blast radius and reversibility drive the autonomy decision. Production code changes are high blast radius and usually low reversibility. Those workflows stay at L0 or L1, and the [agent cards](../roles/README.md) list the scope boundaries.

The mistake would be reading L3 as "AI merges to main." It isn't. L3 is "AI runs the workflow within its defined scope and escalates on named triggers."

---

## 3. "Our regulator won't allow this"

**Voiced by:** Compliance, legal, heads of regulated business units.
**Fear underneath:** Audit findings, fines, loss of operating license.

**Response.** Which parts won't they allow? This is usually a question about data flow, provenance, and human accountability — all of which the [HITL framework](hitl-framework.md) treats as decision axes. Most regulators don't prohibit AI assistance; they require documented controls, human accountability, and auditability. Those are features of this approach, not obstacles to it.

Start with the regulator's specific constraints. Map them to the axes. Usually the answer isn't "no AI" — it's "AI at L1, with audit logs, in these named workflows."

---

## 4. "We tried an AI pilot; it didn't stick"

**Voiced by:** Leaders who've been through a failed pilot.
**Fear underneath:** Wasted time, embarrassment, another pilot going the same way.

**Response.** Pilots usually fail for one of three reasons: (1) no clear role or artifact to own, (2) the team jumped to L3 on day one, (3) no measurement of whether the work improved. This repo addresses all three — the [role cards](../roles/README.md) give ownership, the [maturity model](maturity-model.md) enforces a staged path, and the [exit checklists](../phases/README.md) make "improved" concrete.

What matters: start at L1 in one role, pick something with a DoD, measure substantive edits over 4-6 weeks. That's a meaningful pilot.

---

## 5. "This just speeds up the wrong thing"

**Voiced by:** Product leaders, senior PMs.
**Fear underneath:** Faster delivery of features nobody asked for, more tech debt, louder backlog without more value.

**Response.** Agreed — and that's why we don't start at Build. The [Discover](../phases/1-discover/README.md) and [Define](../phases/2-define/README.md) phases are where AI can have the biggest leverage precisely because they were under-invested when humans did all the work. The leverage anti-pattern is [#11](anti-patterns.md) — don't just measure velocity.

If your team is only speeding up Build, you have a prioritization problem, not an AI problem. AI makes it more visible.

---

## 6. "Our team won't trust AI output"

**Voiced by:** Team leads, delivery managers.
**Fear underneath:** Low adoption, duplicated work ("I'll check everything anyway"), silent abandonment.

**Response.** Trust is earned over cases, not declared. The [maturity model](maturity-model.md) is explicitly staged around this: at L1, nobody is asked to trust output; humans edit and own it. Trust builds when humans notice their edits are trivial. That's the L1 → L2 signal.

Trying to force trust through a policy doesn't work. Let people stay at L1 as long as they need to.

---

## 7. "We'd have to rewrite our PDLC"

**Voiced by:** Process owners, PMO, senior delivery leaders.
**Fear underneath:** Massive change-management cost, consultants, a year of disruption.

**Response.** You don't. This repo is intentionally laid out as additions to what most teams already do — roles, phases, artifacts, DoDs. The [agent cards](../roles/README.md) bind to existing roles; the [exit checklists](../phases/README.md) add precision to handoffs that were already happening. If your current PDLC is close to what this repo describes, the delta is small.

Where it's larger, start with one phase. Don't rewrite. Instrument.

---

## 8. "We can't measure whether this is working"

**Voiced by:** Executives, finance, anyone asked to fund the effort.
**Fear underneath:** Can't justify continued investment, can't course-correct, can't tell success from noise.

**Response.** Use the axes. Velocity is the obvious metric and usually the wrong one alone. Better:

- **Substantive-edit rate** on AI-drafted artifacts (falling = earned L2).
- **Artifact coverage** per phase (are all DoDs met at gate?).
- **Escalation rate** at L3 (falling over time = triggers are tight enough).
- **Leverage metrics** from [anti-pattern #11](anti-patterns.md).

None require new tooling — they derive from your existing artifact inventory.

---

## 9. "We're too small / too big for this"

**Voiced by:** Both small and large orgs, for opposite reasons.
**Fear underneath:** (Small) this is over-engineered for us. (Large) this will never survive our complexity.

**Response.** The [role and phase model](../README.md) is a description, not a prescription. Small teams collapse roles onto fewer people and skip phases that don't apply. Large teams add roles, split phases, and layer governance — the [HITL framework](hitl-framework.md) accommodates more complex autonomy decisions.

The pattern is the same at both scales: named roles, artifacts with DoDs, staged autonomy. Implementation varies wildly.

---

## 10. "Who's accountable when the AI is wrong?"

**Voiced by:** Executives, legal, risk.
**Fear underneath:** Diffused accountability, nobody to fire, inability to explain what happened to a regulator or a board.

**Response.** Accountability stays with the human who signs the artifact. At L1, that's the editor. At L2, that's the auditor. At L3, that's whoever defined the escalation triggers and the agent's scope. The [agent cards](../roles/README.md) and [HITL framework](hitl-framework.md) are explicit that autonomy is a customer policy decision — meaning there is always a policy-owner, and that's your accountable human.

"The AI did it" is not a defensible answer. "A human approved scope X with triggers Y; the system operated within that scope and escalated when expected" is.

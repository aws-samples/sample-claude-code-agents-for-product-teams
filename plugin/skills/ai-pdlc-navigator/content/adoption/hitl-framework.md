# HITL Framework — Drawing Your Own Line

There is no universally right answer to "how much autonomy should we give an AI teammate." The answer depends on your risk posture, your regulatory context, your blast radius, and your organization's maturity. This doc is a **framework for making that decision consistently**, not a recommendation of where to land.

Every [agent card](../roles/README.md) in this repo points here for its autonomy setting. Agent cards describe *what* an agent does; this doc describes *how much* your organization trusts it to do so.

## The five axes

When deciding autonomy for a given workflow, score it on each axis. Higher scores push you toward lower autonomy (more human involvement).

### 1. Blast radius

Who or what is affected if this goes wrong?

- **Low:** only the AI teammate's own workspace; a draft file, a scratch branch.
- **Medium:** internal artifacts visible to the team; an updated backlog, a generated test.
- **High:** production systems, customer-facing surfaces, regulated data, financial commitments.

### 2. Reversibility

How hard is it to undo?

- **Low (easy to reverse):** git revert, delete a draft, re-run the workflow.
- **Medium:** requires a rollback script, a migration reversal, a comms correction.
- **High (hard or impossible to reverse):** money moved, customer emailed, data deleted, PII disclosed.

### 3. Regulated / audited

Is this work subject to external or internal compliance review?

- **Low:** not regulated, not audited.
- **Medium:** subject to internal audit but not external regulation (e.g., SOC2 controls).
- **High:** subject to external regulation with specific human-in-the-loop requirements (financial services, healthcare, aerospace).

### 4. Customer-facing

Can a customer see the output directly?

- **Low:** internal-only; customers never see this artifact.
- **Medium:** visible indirectly (e.g., influences a product decision).
- **High:** directly customer-facing — emails, generated content, pricing, UI copy.

### 5. Cost of a false positive / false negative

What does a mistake cost?

- **Low:** re-run the workflow, trivial cost.
- **Medium:** engineering time to diagnose and correct; possible minor customer impact.
- **High:** significant financial cost, customer loss, reputational damage, regulatory exposure.

## The eight questions to ask

For each new AI-teammate deployment or autonomy change:

1. **Blast radius:** If this agent is wrong 5% of the time, what's the cumulative damage over a month?
2. **Reversibility:** What would the rollback procedure look like? Has anyone tested it?
3. **Auditability:** If a regulator asks "what did the AI do and why," can we answer in full?
4. **Customer surface:** Does this touch a customer-facing artifact? Under what circumstances?
5. **Escalation:** What conditions should end the agent's turn and require a human? Are those conditions precise enough to be tested?
6. **Owner:** Who is the named human accountable for this agent's scope and policy? (If the answer is "the team," it's no one.)
7. **Review cadence:** How often do we inspect a sample of the agent's output? What change in output triggers an unplanned review?
8. **Exit ramp:** If this doesn't work out, how fast can we revert to L0 or L1? What's the operational cost?

If you can answer all eight in writing, you have the basis for an informed autonomy decision. If you can't, you're not ready to make the move.

## Worked archetypes

These are **examples of how different organizations might land**, not recommendations. Your team will land somewhere similar or different based on your specific context.

### Archetype A: Regulated enterprise

**Context:** Financial services, healthcare, or similar. SOC2 + external regulator. Change management is a formal process. Auditability is non-negotiable.

- Most workflows stay at L1: AI drafts, human owns and signs.
- A narrow set of internal-only, low-blast-radius workflows may reach L2 (e.g., generating test data for non-prod environments).
- L3 is rare and reserved for workflows where the escalation triggers can be defined mechanically and tested. Autonomous dependency patching in non-prod might qualify.
- Customer-facing AI output is L0 or L1 with mandatory legal review.

### Archetype B: Growth-stage startup

**Context:** Series B-C, shipping fast, limited internal audit function, competitive pressure on velocity.

- Most internal workflows reach L2 quickly: AI drafts and revises, humans audit at artifact-done time.
- Cross-phase handoffs reach L2 within a year — the exit checklists are the audit.
- L3 applies to narrow, well-instrumented workflows (dependency updates, documentation sync, test generation).
- Customer-facing AI output goes through L1 with human review before publish — not as a policy matter, as a brand-quality matter.

### Archetype C: Internal-only tooling team

**Context:** Platform or developer-tools team building for internal consumers. No external regulator. Blast radius is usually bounded to engineering.

- L2 is the default after a short L1 warmup.
- L3 applies widely because blast radius is low and reversibility is high.
- The main risk is coverage — if AI teammates span too many workflows without coordination, tool sprawl and conflicting outputs emerge. Governance of tool choice (see [anti-pattern #8](anti-patterns.md)) matters more than governance of autonomy.
- Customer-facing axis is mostly N/A.

## What this framework deliberately doesn't say

- **What autonomy you should pick.** Not our call.
- **Which artifacts are always L0.** Varies by your context.
- **How to enforce the policy.** Your org's existing governance tools — change management, PR review, audit — are the enforcement layer. This framework is the decision layer.

## Where this plugs in

- The [maturity model](maturity-model.md) describes the axes you move along.
- The [anti-patterns](anti-patterns.md) describe failure modes at specific cells.
- The [objection-handling](objection-handling.md) doc shows how this framework answers common pushback.
- [Agent cards](../roles/README.md) reference this doc for their autonomy setting.

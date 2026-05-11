# AI-PDLC Maturity Model — the tactical picker

A tool for **self-locating one workflow** on an AI-adoption curve. Two axes, sixteen cells. Your team can legitimately sit in different cells for different workflows — uniformity is not the goal, deliberate progress is.

**Pair with the [Maturity Assessment](maturity-assessment.md) — the strategic scorecard.** The assessment tells you where you *are* across the org (automation + readiness, 5-tier Sporadic → Mature). This model helps you decide where to aim *next* for a specific workflow. Use them together: the assessment diagnoses; this model picks the next move.

This is one of the adoption docs. Read it alongside [anti-patterns](anti-patterns.md), [objection-handling](objection-handling.md), and the [HITL framework](hitl-framework.md).

## Axis 1 — Autonomy (Y)

How much of the work AI does versus a human:

| Level | Name | Meaning |
|-------|------|---------|
| L0 | Human-only | No AI in this workflow. Baseline. |
| L1 | AI drafts, human owns | AI produces a first draft; a human edits and signs their name to it. |
| L2 | AI owns, human audits | AI produces the finished artifact; a human reviews before it lands, but rarely changes it. |
| L3 | Autonomous with escalation | AI runs the workflow end-to-end against named escalation triggers. Humans are pulled in by exception, not by schedule. |

Moving up this axis is about **trust and evidence**, not about the model being smarter. You earn L2 from L1 by accumulating cases where the human's edits were trivial. You earn L3 from L2 by defining what "exception" means precisely enough that you're comfortable not reading every output.

## Axis 2 — Coverage (X)

How much of the lifecycle your AI teammate covers:

| Level | Name | Meaning |
|-------|------|---------|
| Single-role | One role in the [role list](../roles/README.md) has an AI teammate. |
| Single-phase | Most roles active in a single [phase](../phases/README.md) have AI assistance. |
| Cross-phase | AI teammates hand artifacts off to each other across two or more phases. |
| Full lifecycle | AI teammates span Discover through Iterate, with the [exit checklists](../phases/README.md) as the handoff contract. |

Moving right is about **workflow integration**, not about replacing more people. The hardest step is usually single-role → single-phase: that's where you discover whether your artifact DoDs are precise enough to serve as inputs to the next role.

## The grid

Each cell is a legitimate place to operate.

|  | Single-role | Single-phase | Cross-phase | Full lifecycle |
|--|-------------|--------------|-------------|----------------|
| **L3 Autonomous** | Niche workflow on autopilot (e.g., dependency patching). | A whole phase runs without a standing human review. | Phases hand off to each other via machine-checkable exit criteria. | Target state — rare today. Most teams don't need this. |
| **L2 AI owns, human audits** | One role produces finished artifacts; a human skims. | A phase's artifacts are mostly AI-owned; humans gate at exit. | Multi-phase automation with human audit at each phase gate. | Full lifecycle with audit at each phase boundary. |
| **L1 AI drafts, human owns** | Drafts in one role; human finishes. | Drafts across a phase; humans finish each. | Drafts across phases; humans own each hand-edited artifact. | Drafts across every phase. Common starting point for mature teams. |
| **L0 Human-only** | Baseline. | Baseline. | Baseline. | Baseline. |

## How to read this

- **Your team is probably not in one cell.** You might be L2 × single-role for code review and L0 × everywhere-else. That's fine. Pick the cell per workflow, not per team.
- **Don't chase uniformity.** Forcing every role to L2 at the same time guarantees some of them are there for the wrong reasons.
- **Progress is cell-by-cell, not a tidal wave.** One role moving from L1 to L2 is a real win. Don't discount it because the broader team is L1.

## How to move up on the autonomy axis

- **L0 → L1:** pick one high-volume, low-blast-radius artifact in one role. Let AI draft it. Measure how often the human's edits are substantive.
- **L1 → L2:** when substantive edits are rare over a meaningful sample, shift the human from editor to auditor. Define what a failed audit looks like.
- **L2 → L3:** define escalation triggers — what conditions must end the agent's turn and pull a human in? Without precise triggers, L3 is irresponsible, not ambitious.

## How to move right on the coverage axis

- **Single-role → single-phase:** make sure every artifact in that phase has a [Definition of Done](../phases/README.md). Without one, downstream AI teammates can't know if their input is ready.
- **Single-phase → cross-phase:** wire up the next phase's [exit checklist](../phases/README.md). The earlier phase's AI output feeds the next phase's AI input — but a human still gates the boundary.
- **Cross-phase → full lifecycle:** usually not necessary. Most teams find diminishing returns past two or three adjacent phases automated end-to-end.

## Where to go next

- If a cell you want is blocked: read [anti-patterns](anti-patterns.md) for the cell you're trying to leave.
- If an exec or IC is pushing back on the next move: [objection-handling](objection-handling.md).
- If you're unsure what autonomy is *allowed* for a given artifact: [hitl-framework](hitl-framework.md).

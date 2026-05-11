# Adoption — Where to Start

You found this repo. Your team is considering (or actively deploying) AI teammates across your PDLC. This dir is for you.

The rest of the repo describes **what** an AI-powered product lifecycle looks like — [9 phases](../phases/README.md), [14 roles](../roles/README.md), their artifacts, and their handoffs. This dir answers **how a customer team adopts it without the common failure modes**.

## The journey

1. **Self-locate.** Read the [maturity model](maturity-model.md) — a 2D grid of autonomy × coverage. Find the cell your team is in today. Pick the cell you want to be in.
2. **Check the anti-patterns.** Read [anti-patterns](anti-patterns.md) for the cell you're leaving. Most adoption failures aren't from the destination being wrong; they're from skipping steps on the way.
3. **Prepare for pushback.** Read [objection-handling](objection-handling.md). Whoever will resist this adoption move is on that list, and you'll want the response pattern ready before the conversation.
4. **Set your autonomy policy.** Read the [HITL framework](hitl-framework.md) — a framework for deciding how much autonomy a given workflow should have, grounded in blast radius, reversibility, regulation, customer surface, and cost of mistakes. This is explicitly a *framework*, not a prescription.
5. **Pick a phase and a role.** Go to the [phase list](../phases/README.md) and [role list](../roles/README.md). Pick one role in one phase as the starting point.

## Measuring where you are today

The [maturity model](maturity-model.md) is the **tactical picker** — it helps you decide the next move for one workflow. The [maturity assessment](maturity-assessment.md) is the **strategic scorecard** — it tells you where you are across the org using two lenses: automation (per-phase AI coverage) and readiness (Strategy, Data, Infra, Workforce, Culture). Both use the shared 5-tier scale: **Sporadic / Isolated / Struggling / Scaling / Mature**. Run the assessment quarterly; use the model continuously as you plan workflow moves.

## Bridging named formats in and out

If your team arrives with a PRFAQ, PRD, 6-pager, canvas, or other named format — or you want to assemble a shareable bundle at a handoff moment — see [formats](formats.md). It maps common inbound formats to handbook artifacts and defines named outbound bundle recipes (Vision, Kickoff, Build-start, Design-partner, Launch-readiness, Board/investor).

## A note on voice

These docs are opinionated and labeled v1. Where we make a claim — especially in anti-patterns and objection-handling — we've tried to name why we think it. If your experience contradicts what's here, file a PR. That's the fastest way this gets better.

## A note on what's *not* here

- **Workshop kits.** Not yet.
- **A prescribed autonomy policy.** Never. The line varies by customer; the [HITL framework](hitl-framework.md) is how you find yours.
- **Task-specific prompts.** Not yet — on the roadmap.
- **AWS-specific tooling.** Intentionally tool-agnostic.

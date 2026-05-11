# ai-pdlc-navigator skill

Orients Claude to the AI-PDLC handbook — 9 phases, 14 roles, ~130 activities, ~260 artifacts/outcomes — so it can extend, maintain, or explain the lifecycle without re-learning the structure every session. See [`SKILL.md`](SKILL.md) for full details.

## Two modes

- **Interactive** — human user arrives with a question. The skill teaches concepts as needed and offers seven starter paths (role acceleration, project-wide acceleration, tool discovery, new automation spec, explain an artifact/outcome, bootstrap a product, run a maturity assessment).
- **Agent-serving** — one of the 14 role teammate agents (Developer, Architect, SRE, etc.) invokes the skill to orient against the canonical handbook. The skill points at the right role/artifact/outcome files and returns control.

## Install

This skill ships inside the `ai-pdlc` plugin. Install the plugin to get the skill.

```bash
/plugin install ai-pdlc                       # from a marketplace
/plugin install /path/to/ai-pdlc/plugin       # from a local checkout
```

## Bundled content

All handbook markdown lives under `content/`:

- `content/AI-PDLC-linear-flow.md` — master index
- `content/roles/<slug>.md` — 14 role pages
- `content/phases/<N-phase>/` — phase README + 14 per-phase role briefs + artifacts + outcomes
- `content/adoption/` — maturity model, maturity assessment, HITL framework, anti-patterns, formats, objection handling
- `content/docs/` — rendered swim-lane diagram

In the authoring repo, `content/` is symlinks into the repo root. At package time (`make package`) they're materialized into real copies so the plugin is self-contained.

## What it triggers on

Any mention of phases, roles, artifacts, outcomes, RACI, the swim-lane diagram, tool discovery, AI acceleration for a role, or requests to run a maturity assessment, bootstrap a product, or explain a handbook concept.

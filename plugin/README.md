# ai-pdlc plugin

The AI-PDLC handbook — 9 phases, 14 roles, ~130 activities, ~260 artifacts/outcomes — packaged as a Claude Code plugin.

## What this installs

- **`ai-pdlc-navigator` skill** — the primary interactive entry point. Seven paths: plan AI acceleration for a role or whole project, discover the tools your team uses, create new automations, explain any artifact/outcome, bootstrap a product from a seed doc, run an AI maturity assessment.
- **14 role teammate agents** — one per swim lane, each grounded in its canonical role definition and wired to collaborate with the others via the Agent tool:
  - `product-sponsor`, `product-owner`, `business-analyst`, `ui-ux-designer`, `architect`, `security-compliance`, `site-reliability-engineer`, `project-manager`, `developer`, `qa-tester`, `release-manager`, `technical-writer`, `sales-marketing`, `customer-support`
- **Slash commands** — quickstart workflows that orchestrate the agents:
  - `/product-ideation-to-planning` — end-to-end kickoff. Takes a vision (or nothing formal) through Discover → Define → Design → Plan and produces the full handbook artifact set, with checkpoints between phases and parallel role-agent dispatches inside each.
- **Bundled handbook content** at `skills/ai-pdlc-navigator/content/` — all role pages, phase docs, artifact/outcome stubs, adoption guides, and the master flow index. This is the single source of truth the skill and agents consult.

## How it works

- When you ask for help on PDLC work, the `ai-pdlc-navigator` skill activates and offers the seven paths, introducing handbook concepts as needed.
- When you invoke a role agent (by name or via delegation), that agent loads the navigator skill first to orient against the handbook, then operates within its role's remit, scope boundaries, and escalation triggers.
- Every answer is grounded in the bundled markdown files — not model recall — so humans and AI teammates work from the same phase definitions, artifact contracts, and Exit checklists.

## Install

Install via Claude Code marketplace (recommended) or load from a local path:

```bash
# From a marketplace:
/plugin install ai-pdlc

# From a local checkout:
/plugin install /path/to/ai-pdlc/plugin
```

Once installed, start a Claude Code session and try:

- *"Help me plan AI acceleration for the Developer role."*
- *"Run an AI maturity assessment for our SRE team."*
- *"What tools do we use for PDLC — walk me through it."*
- *"Explain the architecture-document artifact."*

## Development

This plugin dir is authored in the [AI-PDLC handbook repo](https://github.com/). The bundled content at `skills/ai-pdlc-navigator/content/` is symlinked to the repo root during development, and materialized into real copies at package time via `make package`. The repo root remains a human-readable handbook browseable on GitHub/GitLab without the plugin.

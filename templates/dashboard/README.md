# Dashboard template

A single-file HTML dashboard that tracks artifacts and outcomes by phase and by role. Opens directly in a browser from the local filesystem — no server needed.

## Files

- `dashboard.html` — the dashboard UI. Loads `data.js` and `status.js` via script tags from the same directory.
- `generate_data.py` — parses `AI-PDLC-linear-flow.md` and emits `data.js` containing the 286 artifact/outcome entries with phase, role, and file-path metadata.
- `status.template.js` — initial (empty) status file. Gets copied in as `status.js` when the dashboard is installed.
- `update_status.py` — helper for role agents to update a single item's status. Edits `status.js` in place.
- `install.sh` — copies the dashboard into a target project's `./artifacts/_dashboard/` directory.

## Install into a project

From this repo's root:

```bash
bash templates/dashboard/install.sh /path/to/target/project "Project Name"
```

That creates `/path/to/target/project/artifacts/_dashboard/` with `dashboard.html`, `data.js` (fresh from the master flow), `status.js`, and `update_status.py`. The user opens `dashboard.html` in a browser and it renders.

## Update an item's status

```bash
python3 artifacts/_dashboard/update_status.py \
  artifacts/_dashboard/status.js \
  "5-build/artifacts/mvp.md" \
  in-progress \
  --notes "Core journey working end-to-end; payments flow TBD." \
  --artifact-path "./artifacts/5-build/mvp.md" \
  --updated-by developer
```

Valid statuses: `complete`, `in-progress`, `prepared`, `blocked`, `deferred`, `not-started`.

The key format is `<phase-slug>/<kind>/<filename>` — exactly the `path` field (without the `phases/` prefix) that appears in `data.js` for each item.

## Why it's static HTML

- Works offline, opens with a double-click.
- No build toolchain, no dependencies to keep current.
- `status.js` is plain data — an agent can write it, a human can read it, and a diff tool can show what changed between runs.

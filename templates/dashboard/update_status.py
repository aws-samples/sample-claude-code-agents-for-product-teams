#!/usr/bin/env python3
"""Update a single item's status in the dashboard's status.js.

Usage: python3 update_status.py <status.js> <key> <status> [--notes TEXT]
                                [--blocker TEXT] [--artifact-path PATH]
                                [--updated-by ROLE]

Key is "<phase-slug>/<kind>/<filename>" — e.g. "5-build/artifacts/mvp.md".
Status is one of: complete, in-progress, prepared, blocked, deferred, not-started.

The script edits status.js in place. It expects the file to contain a single
`window.PDLC_STATUS = { ... };` assignment — the format the dashboard bootstraps
from templates/dashboard/status.template.js.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

VALID_STATUSES = {"complete", "in-progress", "prepared", "blocked", "deferred", "not-started"}


def load(path: Path) -> dict:
    raw = path.read_text()
    # Strip JS // comments globally so the stray "//" lines inside the template
    # don't break the regex or the JSON parse.
    stripped = re.sub(r"//[^\n]*", "", raw)
    m = re.search(r"window\.PDLC_STATUS\s*=\s*(\{.*\})\s*;", stripped, re.DOTALL)
    if not m:
        print(f"error: could not locate window.PDLC_STATUS assignment in {path}", file=sys.stderr)
        sys.exit(2)
    payload = m.group(1)
    # Drop trailing commas that JS tolerates but JSON doesn't.
    payload = re.sub(r",(\s*[}\]])", r"\1", payload)
    return json.loads(payload)


def save(path: Path, payload: dict) -> None:
    path.write_text(
        "// Updated by update_status.py. Agents edit this via the script, not by hand.\n"
        "window.PDLC_STATUS = " + json.dumps(payload, indent=2) + ";\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("status_js", type=Path)
    ap.add_argument("key")
    ap.add_argument("status", choices=sorted(VALID_STATUSES))
    ap.add_argument("--notes")
    ap.add_argument("--blocker")
    ap.add_argument("--artifact-path")
    ap.add_argument("--updated-by")
    args = ap.parse_args()

    data = load(args.status_js)
    data.setdefault("items", {})
    entry = data["items"].get(args.key, {})
    entry["status"] = args.status
    entry["updated"] = datetime.now(timezone.utc).isoformat()
    if args.updated_by:
        entry["updated_by"] = args.updated_by
    if args.notes is not None:
        entry["notes"] = args.notes
    if args.blocker is not None:
        entry["blocker"] = args.blocker if args.blocker else None
        if not args.blocker:
            entry.pop("blocker", None)
    if args.artifact_path is not None:
        entry["artifact_path"] = args.artifact_path

    data["items"][args.key] = entry
    data["updated"] = datetime.now(timezone.utc).isoformat()
    save(args.status_js, data)
    print(f"updated {args.key} -> {args.status}")


if __name__ == "__main__":
    main()

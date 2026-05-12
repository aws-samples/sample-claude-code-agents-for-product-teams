#!/usr/bin/env python3
"""Generate the dashboard's data.js from the AI-PDLC master flow.

Usage: python3 generate_data.py <path-to-master-flow.md> <output-path/data.js>

The dashboard is static HTML + vanilla JS. This script parses the master flow,
extracts every activity -> artifact/outcome mapping with roles, and emits a
`data.js` file the dashboard reads via a <script src> tag.
"""

import json
import re
import sys
from pathlib import Path

PHASE_RE = re.compile(r"^## \[(\d+)\. ([^\]]+)\]\(phases/(\d+-[a-z]+)/README\.md\)")
# Activity line: "- <activity> produces [<label>](phases/N-slug/kind/filename) *(roles)*"
# The produces-link captures artifact/outcome location; roles trail in *(..)*.
ACTIVITY_RE = re.compile(
    r"^- (?P<activity>.+?) produces \[(?P<label>[^\]]+)\]"
    r"\(phases/(?P<phase_num>\d+)-(?P<phase_slug>[a-z]+)/(?P<kind>artifacts|outcomes)/(?P<filename>[^)]+)\) "
    r"\*\((?P<roles>.+)\)\*\s*$"
)
ROLE_LINK_RE = re.compile(r"\[([^\]]+)\]\(#[^)]+\)")


def strip_md_links(text: str) -> str:
    """Turn '[label](url)' into 'label' so activity names read cleanly."""
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def parse_flow(master_flow_path: Path):
    phases = {}
    items = []
    current_phase = None

    for raw in master_flow_path.read_text().splitlines():
        line = raw.rstrip()
        m = PHASE_RE.match(line)
        if m:
            num = int(m.group(1))
            name = m.group(2).strip()
            slug = m.group(3).strip()
            current_phase = {"num": num, "name": name, "slug": slug}
            phases[num] = current_phase
            continue

        m = ACTIVITY_RE.match(line)
        if m and current_phase:
            activity = strip_md_links(m.group("activity")).strip()
            label = m.group("label").strip()
            phase_num = int(m.group("phase_num"))
            phase_slug = f"{phase_num}-{m.group('phase_slug')}"
            kind = m.group("kind")
            filename = m.group("filename")
            roles_raw = m.group("roles")

            role_names = ROLE_LINK_RE.findall(roles_raw)
            if not role_names:
                if "all roles" in roles_raw.lower():
                    role_names = ["All roles"]
                else:
                    role_names = [r.strip() for r in roles_raw.split(",") if r.strip()]

            items.append({
                "activity": activity,
                "label": label,
                "kind": kind,
                "phase_num": phase_num,
                "phase_name": current_phase["name"],
                "phase_slug": phase_slug,
                "filename": filename,
                "path": f"phases/{phase_slug}/{kind}/{filename}",
                "owner": role_names[0] if role_names else None,
                "coowners": role_names[1:] if len(role_names) > 1 else [],
                "all_roles": role_names,
            })

    return phases, items


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_data.py <master-flow.md> <output/data.js>", file=sys.stderr)
        sys.exit(2)

    flow_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    phases, items = parse_flow(flow_path)

    role_order = [
        "Product Sponsor", "Product Owner", "Business Analyst", "UI/UX Designer",
        "Architect", "Security & Compliance", "Site Reliability Engineer",
        "Project Manager", "Developer", "QA/Tester", "Release Manager",
        "Technical Writer", "Sales & Marketing", "Customer Support",
    ]

    payload = {
        "phases": [phases[k] for k in sorted(phases)],
        "items": items,
        "roles": role_order,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        "// Auto-generated from AI-PDLC-linear-flow.md. Do not edit by hand.\n"
        "window.PDLC_DATA = " + json.dumps(payload, indent=2) + ";\n"
    )
    print(f"Wrote {len(items)} items across {len(phases)} phases -> {out_path}")


if __name__ == "__main__":
    main()

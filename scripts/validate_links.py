#!/usr/bin/env python3
"""Validate handbook links resolve within a given content root.

Usage:
  scripts/validate_links.py <root>

Where <root> is either:
  - The repo root (contains AI-PDLC-linear-flow.md, roles/, phases/, adoption/)
  - A plugin content dir (contains the same layout under content/)

Checks every `](phases/...)`, `](roles/...)`, `](adoption/...)`, `](docs/...)`,
`](../phases/...)`, and `](../roles/...)` link in every markdown file under the root.
Exits non-zero if any link doesn't resolve.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\]\(([^)#]+?)(?:#[^)]*)?\)")

# Only validate link targets that point into handbook content. External URLs, anchors-only,
# and unrelated local files are skipped.
HANDBOOK_PREFIXES = (
    "phases/",
    "roles/",
    "adoption/",
    "docs/",
    "AI-PDLC-linear-flow.md",
    "../phases/",
    "../roles/",
    "../adoption/",
    "../docs/",
    "../../phases/",
    "../../roles/",
    "../../adoption/",
    "../../docs/",
)


# Directories to skip entirely (planning notes, build output, dist, etc.).
SKIP_DIR_PARTS = {
    ".git",
    "build",
    "dist",
    "docs/superpowers",  # prior spec/plan notes, not handbook content
}


def iter_markdown_files(root: Path) -> list[Path]:
    def keep(p: Path) -> bool:
        rel_parts = p.relative_to(root).parts
        for skip in SKIP_DIR_PARTS:
            skip_parts = tuple(skip.split("/"))
            if len(rel_parts) >= len(skip_parts) and rel_parts[: len(skip_parts)] == skip_parts:
                return False
        return True

    return sorted(p for p in root.rglob("*.md") if keep(p))


def is_placeholder(target: str) -> bool:
    # Skip illustrative placeholder paths used inside prose code examples
    # (e.g., `phases/<N>/artifacts/<slug>.md`, `phases/N/folder/slug.md`).
    if "<" in target and ">" in target:
        return True
    if "phases/N/" in target:
        return True
    return False


def collect_links(root: Path) -> list[tuple[Path, str]]:
    pairs: list[tuple[Path, str]] = []
    for md in iter_markdown_files(root):
        try:
            text = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not target.startswith(HANDBOOK_PREFIXES):
                continue
            if is_placeholder(target):
                continue
            pairs.append((md, target))
    return pairs


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.exists():
        print(f"ERROR: {root} does not exist", file=sys.stderr)
        return 2

    pairs = collect_links(root)
    broken: list[tuple[Path, str, Path]] = []

    for md, target in pairs:
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            broken.append((md, target, resolved))

    total = len(pairs)
    if broken:
        print(f"Broken links: {len(broken)} of {total}")
        for md, target, resolved in broken[:50]:
            rel_src = md.relative_to(root)
            print(f"  {rel_src} -> {target}  (resolves to {resolved})")
        if len(broken) > 50:
            print(f"  ... and {len(broken) - 50} more")
        return 1

    print(f"Validated {total} handbook links against {root} — all resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

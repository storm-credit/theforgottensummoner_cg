from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read a source subtree and export a reference manifest without modifying the source."
    )
    parser.add_argument("--name", required=True, help="Manifest display name.")
    parser.add_argument("--source", required=True, help="Read-only source path.")
    parser.add_argument("--output", required=True, help="Markdown output path inside cg.")
    return parser.parse_args()


def normalize_name(name: str) -> str:
    value = name.lower()
    value = value.replace("&", "and")
    value = re.sub(r"\([^)]*\)", "", value)
    value = re.sub(r"[^0-9a-zA-Z가-힣]+", "", value)
    return value


def render_manifest(name: str, source: Path) -> str:
    directories = [p for p in source.rglob("*") if p.is_dir()]
    files = [p for p in source.rglob("*") if p.is_file()]
    markdown = [p for p in files if p.suffix.lower() == ".md"]
    top_level = sorted(source.iterdir(), key=lambda p: p.name)
    root_files = [p for p in top_level if p.is_file()]

    suspicious = []
    for path in source.rglob("*"):
        if any(token in path.name for token in ("_Legacy_", "Backup", "마립", "Aether", "Allians", "참조")):
            suspicious.append(path.relative_to(source))

    normalized = Counter(normalize_name(p.name) for p in directories if p.name)
    duplicate_keys = sorted(key for key, count in normalized.items() if key and count > 1)

    lines = [
        f"# {name} Reference Manifest",
        "",
        f"- Source: `{source}`",
        f"- Directories: {len(directories)}",
        f"- Files: {len(files)}",
        f"- Markdown files: {len(markdown)}",
        "",
        "## Top-level entries",
    ]
    for path in top_level[:30]:
        kind = "dir" if path.is_dir() else "file"
        lines.append(f"- `{path.name}` ({kind})")

    lines.extend(["", "## Root files"])
    if root_files:
        for path in root_files:
            lines.append(f"- `{path.name}`")
    else:
        lines.append("- None")

    lines.extend(["", "## Suspicious paths"])
    if suspicious:
        for path in sorted(suspicious)[:80]:
            lines.append(f"- `{path}`")
        if len(suspicious) > 80:
            lines.append(f"- `... {len(suspicious) - 80} more omitted ...`")
    else:
        lines.append("- None")

    lines.extend(["", "## Duplicate normalized directory keys"])
    if duplicate_keys:
        for key in duplicate_keys[:80]:
            lines.append(f"- `{key}`")
        if len(duplicate_keys) > 80:
            lines.append(f"- `... {len(duplicate_keys) - 80} more omitted ...`")
    else:
        lines.append("- None")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    source = Path(args.source)
    output = Path(args.output)

    if not source.exists():
        raise SystemExit(f"Source path does not exist: {source}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_manifest(args.name, source), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

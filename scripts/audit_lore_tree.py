from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a lightweight inventory report for lore sections."
    )
    parser.add_argument(
        "--section",
        nargs=2,
        action="append",
        metavar=("NAME", "PATH"),
        required=True,
        help="Named section and source path.",
    )
    parser.add_argument(
        "--output",
        help="Optional markdown output path. Defaults to stdout.",
    )
    return parser.parse_args()


def normalize_name(name: str) -> str:
    value = name.lower()
    value = value.replace("&", "and")
    value = re.sub(r"\([^)]*\)", "", value)
    value = re.sub(r"[^0-9a-zA-Z가-힣]+", "", value)
    return value


def suspicious_entry(path: Path) -> bool:
    markers = ("legacy", "backup", "참조", "마립")
    lowered = path.name.lower()
    return any(marker in lowered for marker in markers)


def gather_section(name: str, source: Path) -> dict:
    directories = [p for p in source.rglob("*") if p.is_dir()]
    files = [p for p in source.rglob("*") if p.is_file()]
    markdown_files = [p for p in files if p.suffix.lower() == ".md"]

    top_level = sorted(p.name for p in source.iterdir())
    suspicious = sorted(
        str(p.relative_to(source))
        for p in source.rglob("*")
        if suspicious_entry(p)
    )

    normalized = Counter(normalize_name(p.name) for p in directories if p.name)
    duplicates = sorted(key for key, count in normalized.items() if key and count > 1)

    return {
        "name": name,
        "source": str(source),
        "directory_count": len(directories),
        "file_count": len(files),
        "markdown_count": len(markdown_files),
        "top_level": top_level,
        "suspicious": suspicious[:50],
        "duplicate_keys": duplicates[:50],
    }


def render_report(sections: list[dict]) -> str:
    lines = ["# Lore Inventory Report", ""]
    for section in sections:
        lines.append(f"## {section['name']}")
        lines.append(f"- Source: `{section['source']}`")
        lines.append(f"- Directories: {section['directory_count']}")
        lines.append(f"- Files: {section['file_count']}")
        lines.append(f"- Markdown files: {section['markdown_count']}")
        lines.append("")

        lines.append("### Top-level entries")
        for entry in section["top_level"][:20]:
            lines.append(f"- `{entry}`")
        lines.append("")

        lines.append("### Suspicious entries")
        if section["suspicious"]:
            for entry in section["suspicious"]:
                lines.append(f"- `{entry}`")
        else:
            lines.append("- None")
        lines.append("")

        lines.append("### Duplicate normalized keys")
        if section["duplicate_keys"]:
            for key in section["duplicate_keys"]:
                lines.append(f"- `{key}`")
        else:
            lines.append("- None")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> int:
    args = parse_args()
    sections = []
    for section_name, section_path in args.section:
        source = Path(section_path)
        if not source.exists():
            raise SystemExit(f"Section path does not exist: {source}")
        sections.append(gather_section(section_name, source))

    report = render_report(sections)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

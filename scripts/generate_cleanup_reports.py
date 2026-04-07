from __future__ import annotations

import argparse
from pathlib import Path


WATCH_TOKENS = ("Aether", "Allians", "마립", "_Legacy_", "Backup")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate concrete execution reports for lore cleanup."
    )
    parser.add_argument("--factions-root", required=True, help="Section 8 root path.")
    parser.add_argument("--heroes-root", required=True, help="Section 14 root path.")
    parser.add_argument("--output-dir", required=True, help="Report output directory.")
    return parser.parse_args()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def collect_factions_report(root: Path) -> str:
    top_level = sorted(root.iterdir(), key=lambda p: p.name)
    suspicious_dirs = []
    for path in root.rglob("*"):
        if path.is_dir() and any(token in path.name for token in WATCH_TOKENS):
            suspicious_dirs.append(path.relative_to(root))

    lines = [
        "# Factions Root Audit",
        "",
        f"- Source: `{root}`",
        f"- Top-level entries: {len(top_level)}",
        "",
        "## Top-level entries",
    ]
    for path in top_level:
        kind = "dir" if path.is_dir() else "file"
        lines.append(f"- `{path.name}` ({kind})")

    lines.extend(
        [
            "",
            "## Immediate P0 targets",
            "- `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)`",
            "- `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))`",
            "- `_Legacy_중립세력 (Backup)`",
            "",
            "## Suspicious directories",
        ]
    )
    if suspicious_dirs:
        for path in sorted(suspicious_dirs):
            lines.append(f"- `{path}`")
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Next action",
            "- Freeze the canonical Section 8 root list before any prose edits.",
            "- Quarantine `_Legacy_` and broken-name roots from canon decisions.",
            "- Build a standard subtree map for factions that mix section-style and place-style folders.",
        ]
    )
    return "\n".join(lines)


def collect_heroes_report(root: Path) -> str:
    current_root = root / "01-14-2. 현존 영웅"
    orphan_files = sorted(
        path.relative_to(root)
        for path in current_root.iterdir()
        if path.is_file() and path.suffix.lower() == ".md"
    )
    suspicious_dirs = []
    for path in root.rglob("*"):
        if path.is_dir() and any(token in path.name for token in WATCH_TOKENS):
            suspicious_dirs.append(path.relative_to(root))

    lines = [
        "# Heroes Root Audit",
        "",
        f"- Source: `{root}`",
        "",
        "## Archive roots",
    ]
    for path in sorted(root.iterdir(), key=lambda p: p.name):
        kind = "dir" if path.is_dir() else "file"
        lines.append(f"- `{path.name}` ({kind})")

    lines.extend(
        [
            "",
            "## Orphan files in current heroes root",
        ]
    )
    if orphan_files:
        for path in orphan_files:
            lines.append(f"- `{path}`")
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Suspicious directories",
        ]
    )
    if suspicious_dirs:
        for path in sorted(suspicious_dirs):
            lines.append(f"- `{path}`")
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Next action",
            "- Define the hero canon schema before biography cleanup.",
            "- Normalize continent and faction labels against Section 8.",
            "- Move orphan files only after a canonical destination is approved.",
        ]
    )
    return "\n".join(lines)


def collect_naming_report(factions_root: Path, heroes_root: Path) -> str:
    matches: dict[str, list[str]] = {token: [] for token in WATCH_TOKENS[:-1]}
    for root in (factions_root, heroes_root):
        for path in root.rglob("*"):
            text = str(path.relative_to(root))
            for token in matches:
                if token in text:
                    matches[token].append(f"{root.name}: {text}")

    lines = [
        "# Naming Crosswalk",
        "",
        f"- Factions root: `{factions_root}`",
        f"- Heroes root: `{heroes_root}`",
        "",
        "## Watched variants",
    ]
    for token, entries in matches.items():
        lines.append(f"### {token}")
        lines.append(f"- Count: {len(entries)}")
        if entries:
            for entry in sorted(entries)[:50]:
                lines.append(f"- `{entry}`")
            if len(entries) > 50:
                lines.append(f"- `... {len(entries) - 50} more entries omitted ...`")
        else:
            lines.append("- None")
        lines.append("")

    lines.extend(
        [
            "## Canon actions",
            "- Treat `Ether Continent` as the current default display form unless a broader canon pass changes it.",
            "- Treat `Allians` as a spelling conflict, not a valid alternate canon form.",
            "- Treat `마립` inside the supranational root as corruption.",
            "- Do not normalize `_Legacy_` or `Backup` paths into canon names.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    factions_root = Path(args.factions_root)
    heroes_root = Path(args.heroes_root)
    output_dir = Path(args.output_dir)

    write_text(output_dir / "factions_root_audit.md", collect_factions_report(factions_root))
    write_text(output_dir / "heroes_root_audit.md", collect_heroes_report(heroes_root))
    write_text(output_dir / "naming_crosswalk.md", collect_naming_report(factions_root, heroes_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

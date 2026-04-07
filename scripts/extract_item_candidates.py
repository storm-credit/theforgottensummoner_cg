from __future__ import annotations

import argparse
from pathlib import Path
import re
from collections import Counter


PATTERNS = [
    re.compile(r"《([^》]+)》"),
    re.compile(r"\[\[([^\]]+)\]\]"),
]

ITEM_HINTS = (
    "검",
    "창",
    "활",
    "지팡이",
    "단검",
    "갑옷",
    "반지",
    "목걸이",
    "유물",
    "아티팩트",
    "보검",
    "창검",
    "주사기",
    "가면",
    "망토",
    "staff",
    "sword",
    "ring",
    "artifact",
    "armor",
)

SECTION_HINTS = (
    "전용 무기",
    "아티팩트",
    "Weapons & Gear",
    "무기 및 장비",
    "장비",
    "성유물",
    "유물",
    "소지품",
    "교역품",
    "무역품",
    "주요 무역",
)

SKIP_KEYWORDS = (
    "마법백과",
    "마법 백과",
    "마도통신백과",
    "마도 통신 백과",
    "마도 교통백과",
    "차원 마법",
    "차원 및 공간 마법백과",
    "몬스터백과",
    "종교백과",
    "주술백과",
    "직업 도감",
    "인물 백과",
    "Character Archive",
    "Classes & Jobs",
)

GENERIC_CATEGORY_NAMES = {
    "한손검",
    "양손검",
    "도검류",
    "활",
    "창",
    "지팡이",
    "스태프",
    "중갑",
    "경갑",
    "판금 갑옷",
    "로브",
    "망토",
    "장갑",
    "투구",
    "장화",
    "반지",
    "목걸이",
    "귀걸이",
    "부적",
    "성물",
    "훈장",
    "영웅 고유 성유물",
    "헌터 특수 장비 및 배지",
    "양손검 및 중무기",
    "기병창 및 폴암",
    "기병창(Lance) 및 폴암",
    "타격 둔기 및 철퇴",
    "완드 및 소형 마도구",
    "방패 일체형 특대검",
    "대방패 및 타워 실드",
    "특수 활 및 석궁",
    "마도서 및 스크롤류",
    "한손검 및 도검류",
}

ORG_LIKE_TOKENS = (
    "기사단",
    "병단",
    "군단",
    "연합",
    "협회",
    "결사단",
    "카르텔",
    "정보단",
    "왕국",
    "성국",
    "연맹",
    "의회",
    "기업",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract rough item candidates from imported working documents."
    )
    parser.add_argument("--source", required=True, help="Source directory inside working/imports.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--register-output",
        help="Optional markdown register output path.",
    )
    return parser.parse_args()


def looks_like_item(value: str) -> bool:
    lower = value.lower()
    return any(hint in lower for hint in ITEM_HINTS)


def heading_text(line: str) -> str | None:
    stripped = line.lstrip()
    if not stripped.startswith("#"):
        return None
    return stripped.lstrip("#").strip()


def classify_type(line: str, candidate: str) -> str:
    if "[무기]" in line:
        return "weapon"
    if "[방어구]" in line:
        return "armor"
    if "[악세서리]" in line:
        return "accessory"
    if "[유물]" in line or "[성유물]" in line:
        return "relic"

    lowered = candidate.lower()
    if any(token in lowered for token in ("sword", "blade", "bow", "lance", "spear", "staff", "mace", "hammer")):
        return "weapon"
    if any(token in candidate for token in ("검", "창", "활", "지팡이", "철퇴", "망치", "대검")):
        return "weapon"
    if any(token in lowered for token in ("armor", "cloak", "mask", "gauntlet", "helm", "boots")):
        return "armor"
    if any(token in candidate for token in ("갑주", "갑옷", "망토", "가면", "장갑", "투구", "장화")):
        return "armor"
    if any(token in lowered for token in ("ring", "necklace", "earring", "amulet", "badge")):
        return "accessory"
    if any(token in candidate for token in ("반지", "목걸이", "귀걸이", "부적", "훈장")):
        return "accessory"
    if "유물" in candidate or "성유물" in candidate:
        return "relic"
    return "unknown"


def owner_from_path(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"^\[[^\]]+\]\s*", "", stem).strip()
    return stem


def faction_from_path(path: Path, source: Path) -> str:
    rel = path.relative_to(source)
    parts = rel.parts
    if len(parts) >= 3 and parts[0].startswith("phase") and parts[1]:
        return parts[1]
    if len(parts) >= 2:
        return parts[-2]
    return "unknown"


def normalize_candidate(raw: str) -> tuple[str, str]:
    canonical_hint = ""
    candidate = raw.strip()
    if candidate.startswith("01-19. 아이템 도감"):
        canonical_hint = candidate
        candidate = candidate.split("/")[-1].strip()
    candidate = re.sub(r"^\d+\.\s*", "", candidate).strip()
    return candidate, canonical_hint


def is_generic_category(candidate: str) -> bool:
    core = re.sub(r"\s*\([^)]*\)\s*$", "", candidate).strip()
    if core.endswith("류"):
        return True
    return core in GENERIC_CATEGORY_NAMES


def should_skip(raw: str, candidate: str) -> bool:
    if any(keyword in raw for keyword in SKIP_KEYWORDS):
        return True
    if "/" in candidate:
        return True
    if not candidate:
        return True
    if is_generic_category(candidate):
        return True
    if any(token in candidate for token in ORG_LIKE_TOKENS):
        return True
    if " 및 " in candidate or " & " in candidate:
        return True
    if re.match(r"^\d{2}-\d{2}\.", candidate):
        return True
    return False


def line_is_item_context(line: str, current_heading: str) -> bool:
    return (
        any(hint in line for hint in SECTION_HINTS)
        or any(hint in current_heading for hint in SECTION_HINTS)
        or any(marker in line for marker in ("[무기]", "[방어구]", "[악세서리]", "[유물]", "[성유물]"))
    )


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


def main() -> int:
    args = parse_args()
    source = Path(args.source)
    output = Path(args.output)
    results: list[dict[str, str]] = []
    duplicates: Counter[str] = Counter()

    for path in source.rglob("*.md"):
        current_heading = ""
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        seen = set()
        for line_no, line in enumerate(lines, start=1):
            maybe_heading = heading_text(line)
            if maybe_heading is not None:
                current_heading = maybe_heading

            if "[[" not in line and "《" not in line:
                continue

            context_ok = line_is_item_context(line, current_heading)
            for pattern in PATTERNS:
                for match in pattern.findall(line):
                    raw = match.strip()
                    candidate, canonical_hint = normalize_candidate(raw)
                    if should_skip(raw, candidate):
                        continue
                    if not context_ok:
                        continue
                    key = (candidate, str(path.relative_to(source)))
                    if key in seen:
                        continue
                    seen.add(key)
                    duplicates[candidate] += 1
                    results.append(
                        {
                            "item": candidate,
                            "type": classify_type(line, candidate),
                            "owner": owner_from_path(path),
                            "faction": faction_from_path(path, source),
                            "source": str(path.relative_to(source)),
                            "canonical_hint": canonical_hint,
                            "line": str(line_no),
                        }
                    )

    output.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Extracted Item Candidates", ""]
    lines.append(f"- Total candidates: {len(results)}")
    lines.append(f"- Unique item names: {len(duplicates)}")
    lines.append(f"- Duplicated item names: {sum(1 for count in duplicates.values() if count > 1)}")
    lines.append("")
    if not results:
        lines.append("- None")
    else:
        lines.append("## Duplicate Hotspots")
        lines.append("")
        duplicate_rows = [(item, count) for item, count in duplicates.most_common() if count > 1][:20]
        if duplicate_rows:
            for item, count in duplicate_rows:
                lines.append(f"- `{item}` x{count}")
        else:
            lines.append("- None")
        lines.append("")
        lines.append("## Candidate Rows")
        lines.append("")
        lines.append("| Item | Type | Owner | Faction | Source | Canonical Hint |")
        lines.append("|---|---|---|---|---|---|")
        for row in results:
            lines.append(
                "| "
                + " | ".join(
                    markdown_escape(row[field])
                    for field in ("item", "type", "owner", "faction", "source", "canonical_hint")
                )
                + " |"
            )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if args.register_output:
        register_path = Path(args.register_output)
        register_path.parent.mkdir(parents=True, exist_ok=True)
        register_lines = [
            "# Item Candidate Register",
            "",
            "| Item | Variant | Type | Owner | Faction | First Source | Status | Note |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for row in results:
            note_parts = []
            if row["canonical_hint"]:
                note_parts.append(f"canon_hint={row['canonical_hint']}")
            if duplicates[row["item"]] > 1:
                note_parts.append(f"duplicate_count={duplicates[row['item']]}")
            register_lines.append(
                "| "
                + " | ".join(
                    [
                        markdown_escape(row["item"]),
                        "",
                        markdown_escape(row["type"]),
                        markdown_escape(row["owner"]),
                        markdown_escape(row["faction"]),
                        markdown_escape(f"{row['source']}#L{row['line']}"),
                        "candidate",
                        markdown_escape("; ".join(note_parts)),
                    ]
                )
                + " |"
            )
        register_path.write_text("\n".join(register_lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

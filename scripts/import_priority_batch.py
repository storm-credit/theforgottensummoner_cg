from __future__ import annotations

from pathlib import Path
import shutil


SOURCE_ROOT = Path(r"X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클")
DEST_ROOT = Path(
    r"C:\Users\Storm Credit\Desktop\Novel\The Forgatten Summoner\theforgottensummoner_cg\working\imports"
)


PRIORITY_ITEMS = [
    (
        SOURCE_ROOT
        / r"01-8. 세력 아카이브 (국가·조직 정리)\6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))",
        DEST_ROOT / "phase1_section8_corrupted_root",
    ),
    (
        SOURCE_ROOT
        / r"01-8. 세력 아카이브 (국가·조직 정리)\6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)\6-1. 국제 길드 연합 (Guilds)\05. 키르케 영약회 (Circe's Elixir Order)",
        DEST_ROOT / "phase1_section8_canonical_kirke",
    ),
    (
        SOURCE_ROOT
        / r"01-14. 영웅 백과 (Hero Archive)\01-14-1. 성장 영웅\1. 에테르 대륙 (Aether Continent)",
        DEST_ROOT / "phase1_section14_growth_aether",
    ),
    (
        SOURCE_ROOT
        / r"01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\[현존] 정보단 여왕 이리나 폰 루즈.md",
        DEST_ROOT / "phase1_orphans" / "[현존] 정보단 여왕 이리나 폰 루즈.md",
    ),
    (
        SOURCE_ROOT
        / r"01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\[현존] 카르텔 수장 칼리크 디트리히.md",
        DEST_ROOT / "phase1_orphans" / "[현존] 카르텔 수장 칼리크 디트리히.md",
    ),
]


def copy_item(source: Path, destination: Path) -> str:
    if not source.exists():
        return f"missing: {source}"
    if destination.exists():
        return f"skip-existing: {destination}"

    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination)
        return f"copied-dir: {destination}"

    shutil.copy2(source, destination)
    return f"copied-file: {destination}"


def main() -> int:
    for source, destination in PRIORITY_ITEMS:
        print(copy_item(source, destination))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

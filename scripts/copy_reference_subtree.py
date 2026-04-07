from __future__ import annotations

import argparse
from pathlib import Path
import shutil


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy a source subtree into cg working space without modifying the source."
    )
    parser.add_argument("--source", required=True, help="Read-only source subtree.")
    parser.add_argument("--destination", required=True, help="Destination path inside cg working space.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.source)
    destination = Path(args.destination)

    if not source.exists():
        raise SystemExit(f"Source path does not exist: {source}")
    if destination.exists():
        raise SystemExit(f"Destination already exists: {destination}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

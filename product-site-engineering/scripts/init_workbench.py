#!/usr/bin/env python3
"""Initialize a product engineering workbench without overwriting by default."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from datetime import date
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "workbench"
DEFAULT_OUTPUT = Path("docs/product-workbench")
TEXT_SUFFIXES = {".md", ".json", ".txt", ".yaml", ".yml"}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the product-site-engineering workbench into a project.",
    )
    parser.add_argument(
        "--target",
        default=".",
        help="Project root. Defaults to the current directory.",
    )
    parser.add_argument(
        "--project",
        help="Product name. Defaults to the project directory name.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Relative directory inside the target project.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite template-owned files. Unknown files are preserved.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the write plan without creating files.",
    )
    return parser.parse_args(argv)


def safe_output_root(target: Path, output: str) -> Path:
    relative = Path(output)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("--output must be a relative path inside --target")

    destination = (target / relative).resolve()
    try:
        destination.relative_to(target)
    except ValueError as exc:
        raise ValueError("--output resolves outside --target") from exc
    return destination


def template_files() -> list[Path]:
    if not TEMPLATE_ROOT.is_dir():
        raise FileNotFoundError(f"Template directory is missing: {TEMPLATE_ROOT}")
    files = [path for path in TEMPLATE_ROOT.rglob("*") if path.is_file()]
    if not files:
        raise FileNotFoundError("No workbench templates were found")
    return sorted(files)


def rendered_bytes(source: Path, project: str, today: str) -> bytes:
    if source.suffix.lower() not in TEXT_SUFFIXES:
        return source.read_bytes()
    text = source.read_text(encoding="utf-8")
    text = text.replace("{{PROJECT_NAME}}", project).replace("{{DATE}}", today)
    return text.encode("utf-8")


def write_atomic(destination: Path, content: bytes) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.tmp.{os.getpid()}")
    try:
        temporary.write_bytes(content)
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    target = Path(args.target).expanduser().resolve()
    if not target.is_dir():
        print(f"error: target directory does not exist: {target}", file=sys.stderr)
        return 2

    try:
        output_root = safe_output_root(target, args.output)
        sources = template_files()
    except (ValueError, FileNotFoundError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    project = (args.project or target.name).strip()
    if not project:
        print("error: project name cannot be empty", file=sys.stderr)
        return 2

    plan: list[tuple[Path, Path]] = []
    conflicts: list[Path] = []
    for source in sources:
        relative = source.relative_to(TEMPLATE_ROOT)
        destination = output_root / relative
        plan.append((source, destination))
        if destination.exists() and not args.force:
            conflicts.append(destination)

    if conflicts:
        print("error: refusing to overwrite existing workbench files:", file=sys.stderr)
        for path in conflicts:
            print(f"  - {path}", file=sys.stderr)
        print("Use --force only after reviewing the existing files.", file=sys.stderr)
        return 3

    verb = "WOULD WRITE" if args.dry_run else "WROTE"
    today = date.today().isoformat()
    for source, destination in plan:
        if not args.dry_run:
            write_atomic(destination, rendered_bytes(source, project, today))
        print(f"{verb} {destination.relative_to(target)}")

    print(
        f"{verb} {len(plan)} workbench files for {project!r} under "
        f"{output_root.relative_to(target)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

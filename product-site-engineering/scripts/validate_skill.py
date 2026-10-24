#!/usr/bin/env python3
"""Self-contained repository validator for the Product Site Engineering Skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SKILL_NAME = "product-site-engineering"
REQUIRED_REFERENCES = {
    "benchmark-first.md",
    "delivery-loop.md",
    "external-skill-integration.md",
    "frontend-quality.md",
    "backend-api-data.md",
    "observability.md",
    "ai-product-safety.md",
    "release-operations.md",
    "prompt-learning-resources.md",
    "website-building-resources.md",
}
REQUIRED_SCRIPTS = {
    "init_workbench.py",
    "audit_workbench.py",
    "validate_skill.py",
}


def locate_skill(argument: str) -> tuple[Path, Path]:
    root = Path(argument).expanduser().resolve()
    direct = root / "SKILL.md"
    nested = root / SKILL_NAME / "SKILL.md"
    if direct.is_file():
        return root.parent, root
    if nested.is_file():
        return root, root / SKILL_NAME
    raise FileNotFoundError(f"Could not locate {SKILL_NAME}/SKILL.md under {root}")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md must begin with YAML front matter")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid front matter line: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def validate(argument: str) -> list[str]:
    errors: list[str] = []
    try:
        repository, skill = locate_skill(argument)
    except FileNotFoundError as exc:
        return [str(exc)]

    skill_text = (skill / "SKILL.md").read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(skill_text)
    except ValueError as exc:
        errors.append(str(exc))
        frontmatter = {}

    if set(frontmatter) != {"name", "description"}:
        errors.append("SKILL.md front matter must contain only name and description")
    if frontmatter.get("name") != SKILL_NAME:
        errors.append(f"Skill name must be {SKILL_NAME!r}")
    description = frontmatter.get("description", "")
    if len(description) < 80 or "when" not in description.lower():
        errors.append("Description must explain both capability and trigger conditions")

    required_paths = {
        skill / "agents" / "openai.yaml",
        skill / "assets" / "examples" / "typescript" / "observability.ts",
        skill / "assets" / "workbench" / "BENCHMARK.md",
        skill / "assets" / "workbench" / "BAD_CASES.md",
        skill / "assets" / "workbench" / "frontend-event.schema.json",
        skill / "assets" / "workbench" / "log-event.schema.json",
    }
    required_paths.update(skill / "references" / name for name in REQUIRED_REFERENCES)
    required_paths.update(skill / "scripts" / name for name in REQUIRED_SCRIPTS)
    for path in sorted(required_paths):
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(repository)}")

    all_files = [path for path in repository.rglob("*") if path.is_file()]
    if len(all_files) > 500:
        errors.append("Repository exceeds the 500-file skill bundle limit")
    total_size = sum(path.stat().st_size for path in all_files)
    if total_size > 50 * 1024 * 1024:
        errors.append("Repository exceeds the 50 MB skill bundle limit")
    for path in all_files:
        if path.stat().st_size > 25 * 1024 * 1024:
            errors.append(f"File exceeds 25 MB: {path.relative_to(repository)}")
        if path.is_symlink():
            errors.append(f"Symlinks are not allowed in the bundle: {path.relative_to(repository)}")

    unresolved_markers = ("TO" + "DO:", "[TO" + "DO")
    for path in all_files:
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".json"}:
            continue
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in unresolved_markers):
            errors.append(f"Unresolved TODO in {path.relative_to(repository)}")

    openai_yaml = skill / "agents" / "openai.yaml"
    if openai_yaml.is_file():
        metadata = openai_yaml.read_text(encoding="utf-8")
        for field in ("display_name:", "short_description:", "default_prompt:"):
            if field not in metadata:
                errors.append(f"agents/openai.yaml missing {field}")
        if f"${SKILL_NAME}" not in metadata:
            errors.append("default_prompt must explicitly mention the skill")

    schema_paths = (
        skill / "assets" / "workbench" / "log-event.schema.json",
        skill / "assets" / "workbench" / "frontend-event.schema.json",
    )
    for schema_path in schema_paths:
        if not schema_path.is_file():
            continue
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid {schema_path.name}: {exc}")
        else:
            if schema.get("additionalProperties") is not False:
                errors.append(f"{schema_path.name} must use an explicit field allowlist")

    for script_name in REQUIRED_SCRIPTS:
        script = skill / "scripts" / script_name
        if script.is_file():
            try:
                compile(script.read_text(encoding="utf-8"), str(script), "exec")
            except SyntaxError as exc:
                errors.append(f"Syntax error in {script_name}: {exc}")

    return errors


def main(argv: list[str] | None = None) -> int:
    arguments = argv if argv is not None else sys.argv[1:]
    root = arguments[0] if arguments else "."
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: skill metadata, resources, scripts, size limits, and log schema")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

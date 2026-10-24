#!/usr/bin/env python3
"""Audit a generated product workbench for minimum delivery controls."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


DEFAULT_OUTPUT = Path("docs/product-workbench")
REQUIRED_FILES = {
    "WORKBENCH.md",
    "PRODUCT_SYSTEM_SPEC.md",
    "ACCEPTANCE_MATRIX.md",
    "ENGINEERING_BOUNDARIES.md",
    "PRODUCT_ASSET_REGISTER.md",
    "DELIVERY_ROADMAP.md",
    "OBSERVABILITY_PLAN.md",
    "RUNBOOK.md",
    "DECISION_LOG.md",
    "USER_FEEDBACK_LOG.md",
    "frontend-event.schema.json",
    "log-event.schema.json",
}
PLACEHOLDER = re.compile(r"\{\{[A-Z0-9_]+\}\}")
ACCEPTANCE_ROW = re.compile(
    r"^\|\s*([A-Z][A-Z0-9]+-\d{2,})\s*\|\s*(P[012])\s*\|",
    re.MULTILINE,
)
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credential assignment": re.compile(
        r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)"
        r"\s*[:=]\s*['\"][A-Za-z0-9_./+=-]{12,}['\"]"
    ),
}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit a product engineering workbench.")
    parser.add_argument("--target", default=".", help="Project root.")
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Relative workbench directory inside the project.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")
    return parser.parse_args(argv)


def workbench_root(target: Path, output: str) -> Path:
    relative = Path(output)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("--output must be a relative path inside --target")
    root = (target / relative).resolve()
    try:
        root.relative_to(target)
    except ValueError as exc:
        raise ValueError("--output resolves outside --target") from exc
    return root


def audit(target: Path, output: str) -> list[Finding]:
    findings: list[Finding] = []
    try:
        root = workbench_root(target, output)
    except ValueError as exc:
        return [Finding("error", "PATH", str(exc))]

    if not root.is_dir():
        return [Finding("error", "MISSING_WORKBENCH", f"Missing directory: {root}")]

    for filename in sorted(REQUIRED_FILES):
        if not (root / filename).is_file():
            findings.append(Finding("error", "MISSING_FILE", filename))

    text_files = sorted(root.glob("*.md")) + sorted(root.glob("*.json"))
    for path in text_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(Finding("error", "ENCODING", f"Not UTF-8: {path.name}"))
            continue
        if PLACEHOLDER.search(text):
            findings.append(
                Finding("error", "PLACEHOLDER", f"Unrendered placeholder in {path.name}")
            )
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                findings.append(
                    Finding("error", "POSSIBLE_SECRET", f"Possible {label} in {path.name}")
                )

    matrix = root / "ACCEPTANCE_MATRIX.md"
    if matrix.is_file():
        matrix_text = matrix.read_text(encoding="utf-8")
        rows = ACCEPTANCE_ROW.findall(matrix_text)
        ids = [row[0] for row in rows]
        duplicates = sorted({item for item in ids if ids.count(item) > 1})
        if not rows:
            findings.append(Finding("error", "NO_ACCEPTANCE_IDS", "No acceptance rows found"))
        if not any(priority == "P0" for _, priority in rows):
            findings.append(Finding("error", "NO_P0", "No P0 acceptance row found"))
        for item in duplicates:
            findings.append(Finding("error", "DUPLICATE_ID", item))

    schema_paths = (
        root / "log-event.schema.json",
        root / "frontend-event.schema.json",
    )
    for schema_path in schema_paths:
        if not schema_path.is_file():
            continue
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            findings.append(
                Finding("error", "INVALID_SCHEMA_JSON", f"{schema_path.name}: {exc}")
            )
        else:
            required = set(schema.get("required", []))
            properties = set(schema.get("properties", {}))
            baseline = {"timestamp", "event_name", "outcome", "release"}
            if schema_path.name == "log-event.schema.json":
                baseline.add("request_id")
            if not baseline.issubset(required) or not baseline.issubset(properties):
                findings.append(
                    Finding(
                        "error",
                        "LOG_SCHEMA_FIELDS",
                        f"Missing required fields in {schema_path.name}",
                    )
                )
            if schema.get("additionalProperties") is not False:
                findings.append(
                    Finding("warning", "LOG_SCHEMA_ALLOWLIST", "Set additionalProperties to false")
                )

    obs = root / "OBSERVABILITY_PLAN.md"
    if obs.is_file():
        content = obs.read_text(encoding="utf-8").lower()
        for phrase in ("request id", "forbidden fields", "retention", "runbook"):
            if phrase not in content:
                findings.append(
                    Finding("warning", "OBSERVABILITY_GAP", f"Missing phrase: {phrase}")
                )

    return findings


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    target = Path(args.target).expanduser().resolve()
    if not target.is_dir():
        print(f"error: target directory does not exist: {target}", file=sys.stderr)
        return 2

    findings = audit(target, args.output)
    errors = [finding for finding in findings if finding.severity == "error"]
    if args.json:
        print(
            json.dumps(
                {
                    "ok": not errors,
                    "findings": [asdict(finding) for finding in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for finding in findings:
            print(f"{finding.severity.upper()} {finding.code}: {finding.message}")
        if not findings:
            print("PASS: workbench structure, acceptance IDs, placeholders, and log schema")
        elif not errors:
            print(f"PASS WITH {len(findings)} WARNING(S)")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

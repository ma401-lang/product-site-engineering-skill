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
    "BENCHMARK.md",
    "ACCEPTANCE_MATRIX.md",
    "BAD_CASES.md",
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
BENCHMARK_STATUS = re.compile(
    r"^Status:\s*`?(draft|frozen)`?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
BENCHMARK_VERSION = re.compile(
    r"^Benchmark version:\s*`?([^`\s]+)`?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
BENCHMARK_OWNER = re.compile(
    r"^Owner:\s*`?([^`\n]+)`?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
BENCHMARK_REFERENCE_ROW = re.compile(
    r"^\|\s*BMK-\d{2,}\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*"
    r"(?:<?https://[^|\s>]+>?|\[[^\]]+\]\(https://[^)]+\))\s*\|",
    re.IGNORECASE | re.MULTILINE,
)
BENCHMARK_BASELINE_ROW = re.compile(
    r"^\|\s*BASE-\d{2,}\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|$",
    re.IGNORECASE | re.MULTILINE,
)
BENCHMARK_RUBRIC_ROW = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*(\d{1,3})\s*\|\s*([^|]*)\|\s*([^|]*)\|"
    r"\s*([^|]*)\|\s*([^|]*)\|$",
    re.MULTILINE,
)
BENCHMARK_IDEA_FIELDS = (
    "Idea in the product owner's own words",
    "Why this matters now",
    "Target user and triggering situation",
    "Most expensive or risky assumption",
    "Questions that could change whether or what we build",
)
BAD_CASE_ID = re.compile(r"^BAD-\d{3,}$", re.IGNORECASE)
REGRESSION_ID = re.compile(r"(?:^|[,\s])(?:[A-Z][A-Z0-9]+|EVAL)-\d{2,}(?:$|[,\s])")
BAD_CASE_STATUSES = {
    "observed",
    "reproduced",
    "prevented",
    "verified",
    "accepted",
    "blocked",
}
EMPTY_VALUES = {"", "—", "-"}
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
    parser.add_argument(
        "--release",
        action="store_true",
        help="Enforce frozen discovery evidence and block unresolved P0 bad cases.",
    )
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


def bad_case_rows(text: str) -> tuple[list[list[str]], list[str]]:
    rows: list[list[str]] = []
    malformed: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or not BAD_CASE_ID.fullmatch(cells[0]):
            continue
        if len(cells) != 14:
            malformed.append(cells[0])
            continue
        rows.append(cells)
    return rows, malformed


def prefixed_table_rows(text: str, prefix: str, expected_cells: int) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and cells[0].upper().startswith(prefix) and len(cells) == expected_cells:
            rows.append(cells)
    return rows


def audit(target: Path, output: str, release: bool = False) -> list[Finding]:
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
        required_benchmark_ids = {
            "BENCH-01",
            "BENCH-02",
            "BENCH-03",
            "BADCASE-01",
            "BADCASE-02",
        }
        missing_benchmark_ids = sorted(required_benchmark_ids.difference(ids))
        for item in missing_benchmark_ids:
            findings.append(
                Finding(
                    "error" if release else "warning",
                    "MISSING_BENCHMARK_ACCEPTANCE",
                    item,
                )
            )

    bad_cases = root / "BAD_CASES.md"
    if bad_cases.is_file():
        rows, malformed = bad_case_rows(bad_cases.read_text(encoding="utf-8"))
        for case_id in malformed:
            findings.append(
                Finding(
                    "error",
                    "BAD_CASE_MALFORMED",
                    f"{case_id} must contain all 14 bad-case fields",
                )
            )

        ids = [row[0].upper() for row in rows]
        for case_id in sorted({item for item in ids if ids.count(item) > 1}):
            findings.append(Finding("error", "BAD_CASE_DUPLICATE", case_id))

        for row in rows:
            (
                case_id,
                date,
                source_ref,
                scenario,
                expected,
                observed,
                severity,
                responsible_layer,
                regression_id,
                prevention_guard,
                owner,
                status,
                resolution_evidence,
                recurrence,
            ) = row
            required_values = {
                "date": date,
                "source ref": source_ref,
                "triggering scenario": scenario,
                "expected": expected,
                "observed": observed,
                "severity": severity,
                "responsible layer": responsible_layer,
                "regression/eval ID": regression_id,
                "prevention guard": prevention_guard,
                "owner": owner,
                "status": status,
                "recurrence": recurrence,
            }
            missing = [name for name, value in required_values.items() if value in EMPTY_VALUES]
            if missing:
                findings.append(
                    Finding(
                        "error",
                        "BAD_CASE_INCOMPLETE",
                        f"{case_id} is missing: {', '.join(missing)}",
                    )
                )

            normalized_status = status.lower()
            normalized_severity = severity.upper()
            if normalized_status not in BAD_CASE_STATUSES:
                findings.append(
                    Finding(
                        "error",
                        "BAD_CASE_STATUS",
                        f"{case_id} has unsupported status: {status}",
                    )
                )
            if normalized_severity not in {"P0", "P1", "P2"}:
                findings.append(
                    Finding(
                        "error",
                        "BAD_CASE_SEVERITY",
                        f"{case_id} severity must be P0, P1, or P2",
                    )
                )
            if regression_id not in EMPTY_VALUES and REGRESSION_ID.search(regression_id) is None:
                findings.append(
                    Finding(
                        "error",
                        "BAD_CASE_REGRESSION_ID",
                        f"{case_id} needs a stable acceptance or eval ID",
                    )
                )
            recurrence_match = re.match(r"^(\d+)", recurrence)
            if recurrence not in EMPTY_VALUES and recurrence_match is None:
                findings.append(
                    Finding(
                        "error",
                        "BAD_CASE_RECURRENCE",
                        f"{case_id} recurrence must begin with a number",
                    )
                )
            elif recurrence_match is not None and int(recurrence_match.group(1)) > 0:
                analysis = recurrence[recurrence_match.end() :].strip(" —:-")
                if len(analysis) < 12:
                    findings.append(
                        Finding(
                            "error",
                            "BAD_CASE_RECURRENCE_ANALYSIS",
                            f"{case_id} recurred; explain why the previous guard failed",
                        )
                    )
            if normalized_status in {"prevented", "verified", "accepted"} and (
                resolution_evidence in EMPTY_VALUES
            ):
                findings.append(
                    Finding(
                        "error",
                        "BAD_CASE_EVIDENCE_MISSING",
                        f"{case_id} status {normalized_status} needs resolution evidence",
                    )
                )
            if release and normalized_severity == "P0" and normalized_status not in {
                "verified",
                "accepted",
            }:
                findings.append(
                    Finding(
                        "error",
                        "BAD_CASE_P0_OPEN",
                        f"{case_id} blocks release until verified or explicitly accepted",
                    )
                )

    benchmark = root / "BENCHMARK.md"
    if benchmark.is_file():
        benchmark_text = benchmark.read_text(encoding="utf-8")
        benchmark_severity = "error" if release else "warning"
        status = BENCHMARK_STATUS.search(benchmark_text)
        if status is None:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_STATUS_MISSING",
                    "BENCHMARK.md must declare Status: draft or frozen",
                )
            )
        elif status.group(1).lower() != "frozen":
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_NOT_FROZEN",
                    "BENCHMARK.md is still draft",
                )
            )

        if BENCHMARK_VERSION.search(benchmark_text) is None:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_VERSION_MISSING",
                    "BENCHMARK.md must declare a version",
                )
            )

        owner = BENCHMARK_OWNER.search(benchmark_text)
        if owner is None or owner.group(1).strip().lower() in {
            "",
            "unassigned",
            "replace me",
            "—",
            "-",
        }:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_OWNER_MISSING",
                    "Assign an accountable benchmark owner before release",
                )
            )

        missing_idea_fields = []
        for field in BENCHMARK_IDEA_FIELDS:
            match = re.search(
                rf"^-\s*{re.escape(field)}:[ \t]*([^\n]*)$",
                benchmark_text,
                re.MULTILINE,
            )
            if match is None or match.group(1).strip() in EMPTY_VALUES:
                missing_idea_fields.append(field)
        if missing_idea_fields:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_IDEA_INCOMPLETE",
                    "Complete idea discovery fields: " + ", ".join(missing_idea_fields),
                )
            )

        research_rows = prefixed_table_rows(benchmark_text, "RSH-", 7)
        complete_research = [
            row for row in research_rows if all(value not in EMPTY_VALUES for value in row[1:])
        ]
        if not complete_research:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_RESEARCH_MISSING",
                    "Add at least one complete research question, method, finding, limitation, and decision impact",
                )
            )

        decision_rows = prefixed_table_rows(benchmark_text, "DEC-", 6)
        complete_decisions = [
            row for row in decision_rows if all(value not in EMPTY_VALUES for value in row[1:])
        ]
        if not complete_decisions:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_DECISION_TRACE_MISSING",
                    "Trace at least one requirement and design hypothesis to idea/research evidence and validation IDs",
                )
            )

        references = BENCHMARK_REFERENCE_ROW.findall(benchmark_text)
        useful_references = [
            (name.strip(), author.strip())
            for name, author in references
            if "replace with" not in name.lower()
            and "replace with" not in author.lower()
            and author.strip() not in {"", "—", "-"}
        ]
        if len(useful_references) < 2:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_REFERENCE_MISSING",
                    "Add at least two direct HTTPS references with authors or publishers",
                )
            )

        baselines = BENCHMARK_BASELINE_ROW.findall(benchmark_text)
        captured_baselines = [
            row for row in baselines if row[2].strip() not in {"", "—", "-"}
        ]
        if not captured_baselines:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_BASELINE_MISSING",
                    "Capture a current-state result or artifact before implementation",
                )
            )

        rubric_rows = BENCHMARK_RUBRIC_ROW.findall(benchmark_text)
        total_weight = sum(int(row[1]) for row in rubric_rows)
        if not rubric_rows or total_weight != 100:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_WEIGHT_TOTAL",
                    f"Benchmark rubric weights must total 100; found {total_weight}",
                )
            )
        incomplete_rubric = [
            row[0].strip()
            for row in rubric_rows
            if any(not value.strip() for value in row[2:])
        ]
        if incomplete_rubric:
            findings.append(
                Finding(
                    benchmark_severity,
                    "BENCHMARK_RUBRIC_INCOMPLETE",
                    "Fill current baseline, target, measurement, and acceptance IDs for: "
                    + ", ".join(incomplete_rubric),
                )
            )

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

    findings = audit(target, args.output, release=args.release)
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
            print(
                "PASS: workbench structure, benchmark, bad cases, acceptance IDs, "
                "placeholders, and log schema"
            )
        elif not errors:
            print(f"PASS WITH {len(findings)} WARNING(S)")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

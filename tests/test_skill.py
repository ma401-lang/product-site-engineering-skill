from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
SKILL = REPOSITORY / "product-site-engineering"
INIT = SKILL / "scripts" / "init_workbench.py"
AUDIT = SKILL / "scripts" / "audit_workbench.py"
VALIDATE = SKILL / "scripts" / "validate_skill.py"


def run(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *arguments],
        cwd=REPOSITORY,
        text=True,
        capture_output=True,
        check=False,
    )


class SkillValidationTests(unittest.TestCase):
    def test_repository_validator_passes(self) -> None:
        result = run(str(VALIDATE), str(REPOSITORY))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_workbench_initializes_and_audits(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "demo-product"
            target.mkdir()

            initialized = run(
                str(INIT),
                "--target",
                str(target),
                "--project",
                "Demo Product",
            )
            self.assertEqual(initialized.returncode, 0, initialized.stderr)

            workbench = target / "docs" / "product-workbench"
            self.assertTrue((workbench / "PRODUCT_SYSTEM_SPEC.md").is_file())
            self.assertTrue((workbench / "BENCHMARK.md").is_file())
            self.assertTrue((workbench / "BAD_CASES.md").is_file())
            self.assertIn(
                "Demo Product",
                (workbench / "PRODUCT_SYSTEM_SPEC.md").read_text(encoding="utf-8"),
            )

            audited = run(str(AUDIT), "--target", str(target))
            self.assertEqual(audited.returncode, 0, audited.stdout + audited.stderr)
            self.assertIn("PASS", audited.stdout)

    def test_release_audit_requires_and_accepts_frozen_benchmark(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "demo-product"
            target.mkdir()
            initialized = run(str(INIT), "--target", str(target))
            self.assertEqual(initialized.returncode, 0, initialized.stderr)

            draft_audit = run(str(AUDIT), "--target", str(target), "--release")
            self.assertEqual(draft_audit.returncode, 1)
            self.assertIn("BENCHMARK_NOT_FROZEN", draft_audit.stdout)
            self.assertIn("BENCHMARK_REFERENCE_MISSING", draft_audit.stdout)
            self.assertIn("BENCHMARK_IDEA_INCOMPLETE", draft_audit.stdout)
            self.assertIn("BENCHMARK_RESEARCH_MISSING", draft_audit.stdout)
            self.assertIn("BENCHMARK_DECISION_TRACE_MISSING", draft_audit.stdout)

            benchmark = target / "docs" / "product-workbench" / "BENCHMARK.md"
            benchmark_text = benchmark.read_text(encoding="utf-8")
            benchmark_text = benchmark_text.replace("Status: `draft`", "Status: `frozen`")
            benchmark_text = benchmark_text.replace(
                "Owner: `unassigned`", "Owner: `Product owner`"
            )
            benchmark_text = benchmark_text.replace(
                "- Idea in the product owner's own words:",
                "- Idea in the product owner's own words: Help users finish one useful task",
            )
            benchmark_text = benchmark_text.replace(
                "- Why this matters now:",
                "- Why this matters now: Existing completion is too slow",
            )
            benchmark_text = benchmark_text.replace(
                "- Target user and triggering situation:",
                "- Target user and triggering situation: First-time mobile user under time pressure",
            )
            benchmark_text = benchmark_text.replace(
                "- Most expensive or risky assumption:",
                "- Most expensive or risky assumption: A shorter flow still produces a useful result",
            )
            benchmark_text = benchmark_text.replace(
                "- Questions that could change whether or what we build:",
                "- Questions that could change whether or what we build: Where users abandon the current flow",
            )
            benchmark_text = benchmark_text.replace(
                "| RSH-01 |  |  |  |  |  |  |",
                "| RSH-01 | Where do users abandon? | Five observed sessions | Consented beta users | Three stopped before confirmation | Small beta sample | Prototype a shorter confirmation step |",
            )
            benchmark_text = benchmark_text.replace(
                "| DEC-01 |  |  |  |  |  |",
                "| DEC-01 | RSH-01 | Reduce first-use steps | One-screen confirmation prototype | Keep multi-step flow only for advanced mode | FLOW-01 |",
            )
            benchmark_text = benchmark_text.replace(
                "| BASE-01 | Primary flow | Browser walkthrough |  |",
                "| BASE-01 | Primary flow | Browser walkthrough | evidence/baseline.png |",
            )
            benchmark_text = benchmark_text.replace(
                "| BMK-01 | Replace with a relevant reference | Replace with author or publisher | — |  |  |",
                "| BMK-01 | Web Content Accessibility Guidelines | W3C WAI | https://www.w3.org/WAI/standards-guidelines/wcag/ | Testable accessibility criteria | Product-specific visual identity |",
            )
            benchmark_text = benchmark_text.replace(
                "| BMK-02 | Replace with a relevant reference | Replace with author or publisher | — |  |  |",
                "| BMK-02 | Playwright Best Practices | Microsoft Playwright team | https://playwright.dev/docs/best-practices | User-visible isolated tests | Product architecture choices |",
            )
            for weight, acceptance_id in (
                ("25", "FLOW-01"),
                ("15", "ASSET-01"),
                ("15", "UI-01"),
                ("10", "A11Y-01"),
                ("10", "REL-01"),
                ("15", "DATA-01"),
                ("10", "OBS-01"),
            ):
                benchmark_text = benchmark_text.replace(
                    f"| {weight} |  |  |  | {acceptance_id} |",
                    f"| {weight} | baseline recorded | target defined | scenario evidence | {acceptance_id} |",
                    1,
                )
            benchmark.write_text(benchmark_text, encoding="utf-8")

            release_audit = run(str(AUDIT), "--target", str(target), "--release")
            self.assertEqual(
                release_audit.returncode,
                0,
                release_audit.stdout + release_audit.stderr,
            )
            self.assertIn("PASS", release_audit.stdout)

    def test_open_p0_bad_case_blocks_release_and_verified_case_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "demo-product"
            target.mkdir()
            initialized = run(str(INIT), "--target", str(target))
            self.assertEqual(initialized.returncode, 0, initialized.stderr)

            bad_cases = target / "docs" / "product-workbench" / "BAD_CASES.md"
            with bad_cases.open("a", encoding="utf-8") as handle:
                handle.write(
                    "\n| BAD-001 | 2026-10-24 | FB-001 | Retry creates a duplicate | "
                    "One durable write | Two writes | P0 | API idempotency | API-01 | "
                    "Integration test for duplicate submission | Product owner | reproduced | "
                    "— | 0 first occurrence |\n"
                )

            release_audit = run(str(AUDIT), "--target", str(target), "--release")
            self.assertEqual(release_audit.returncode, 1)
            self.assertIn("BAD_CASE_P0_OPEN", release_audit.stdout)

            text = bad_cases.read_text(encoding="utf-8").replace(
                "| reproduced | — | 0 first occurrence |",
                "| verified | preview test run 42 | 0 first occurrence |",
            )
            bad_cases.write_text(text, encoding="utf-8")
            non_release_audit = run(str(AUDIT), "--target", str(target))
            self.assertNotIn("BAD_CASE_", non_release_audit.stdout)

            text = bad_cases.read_text(encoding="utf-8").replace(
                "| 0 first occurrence |", "| 1 |"
            )
            bad_cases.write_text(text, encoding="utf-8")
            recurrence_audit = run(str(AUDIT), "--target", str(target))
            self.assertIn("BAD_CASE_RECURRENCE_ANALYSIS", recurrence_audit.stdout)

    def test_initializer_refuses_overwrite_and_preserves_unknown_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "demo-product"
            target.mkdir()
            first = run(str(INIT), "--target", str(target))
            self.assertEqual(first.returncode, 0, first.stderr)

            unknown = target / "docs" / "product-workbench" / "TEAM_NOTES.md"
            unknown.write_text("keep me", encoding="utf-8")

            second = run(str(INIT), "--target", str(target))
            self.assertEqual(second.returncode, 3)
            self.assertIn("refusing to overwrite", second.stderr)

            forced = run(str(INIT), "--target", str(target), "--force")
            self.assertEqual(forced.returncode, 0, forced.stderr)
            self.assertEqual(unknown.read_text(encoding="utf-8"), "keep me")

    def test_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "demo-product"
            target.mkdir()
            result = run(str(INIT), "--target", str(target), "--dry-run")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("WOULD WRITE", result.stdout)
            self.assertFalse((target / "docs").exists())

    def test_output_cannot_escape_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "demo-product"
            target.mkdir()
            result = run(
                str(INIT),
                "--target",
                str(target),
                "--output",
                "../outside",
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("inside --target", result.stderr)


if __name__ == "__main__":
    unittest.main()

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
            self.assertIn(
                "Demo Product",
                (workbench / "PRODUCT_SYSTEM_SPEC.md").read_text(encoding="utf-8"),
            )

            audited = run(str(AUDIT), "--target", str(target))
            self.assertEqual(audited.returncode, 0, audited.stdout + audited.stderr)
            self.assertIn("PASS", audited.stdout)

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

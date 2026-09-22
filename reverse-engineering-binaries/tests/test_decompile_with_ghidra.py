import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "decompile_with_ghidra.py"


class DecompileWithGhidraTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.artifact = self.root / "sample.bin"
        self.artifact.write_bytes(b"\x7fELF\x02\x01" + b"\0" * 64)
        self.ghidra_home = self.root / "ghidra"
        launcher_name = "analyzeHeadless.bat" if sys.platform == "win32" else "analyzeHeadless"
        self.launcher = self.ghidra_home / "support" / launcher_name
        self.launcher.parent.mkdir(parents=True)
        self.launcher.write_text("", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_cli(self, *extra, check=True):
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--artifact",
                str(self.artifact),
                "--output-dir",
                str(self.root / "analysis"),
                *extra,
            ],
            check=check,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def test_dry_run_builds_complete_headless_decompilation_plan_without_writing(self):
        completed = self.run_cli(
            "--ghidra-home",
            str(self.ghidra_home),
            "--dry-run",
        )
        plan = json.loads(completed.stdout)

        self.assertEqual(plan["status"], "ready")
        self.assertEqual(plan["artifact"]["sha256"], "af1be71f2dbbb77794867adb312d2466c88e90a2ee1147fffa2f71a04fc4011a")
        self.assertEqual(Path(plan["launcher"]), self.launcher.resolve())
        self.assertIn("-postScript", plan["command"])
        self.assertIn("ExportDecompilation.java", plan["command"])
        self.assertIn("-analysisTimeoutPerFile", plan["command"])
        self.assertFalse((self.root / "analysis").exists())

    def test_missing_ghidra_reports_a_clear_blocker(self):
        missing_home = self.root / "missing-ghidra"
        completed = self.run_cli(
            "--ghidra-home",
            str(missing_home),
            "--dry-run",
            check=False,
        )

        self.assertEqual(completed.returncode, 2)
        self.assertIn("Ghidra headless launcher not found", completed.stderr)
        self.assertEqual(completed.stdout, "")


if __name__ == "__main__":
    unittest.main()

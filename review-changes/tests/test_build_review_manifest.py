import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_review_manifest.py"


class BuildReviewManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp_dir.name)
        self.git("init", "-b", "main")
        self.git("config", "user.email", "review-skill@example.invalid")
        self.git("config", "user.name", "Review Skill Test")

    def tearDown(self):
        self.temp_dir.cleanup()

    def git(self, *args):
        return subprocess.run(
            ["git", *args],
            cwd=self.repo,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        ).stdout

    def write(self, relative_path, content):
        path = self.repo / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def run_manifest(self, *args):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--repo", str(self.repo), *args],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return json.loads(completed.stdout)

    def commit_baseline(self):
        self.write("src/app.py", "def total():\n    return 1\n")
        self.write("README.md", "# Demo\n")
        self.git("add", ".")
        self.git("commit", "-m", "baseline")

    def test_worktree_manifest_covers_staged_unstaged_and_untracked_files(self):
        self.commit_baseline()
        self.write("src/app.py", "def total():\n    return 2\n")
        self.write("README.md", "# Demo\n\nUpdated.\n")
        self.git("add", "README.md")
        self.write("tests/test_app.py", "def test_total():\n    assert True\n")

        manifest = self.run_manifest("--mode", "worktree")
        files = {item["path"]: item for item in manifest["files"]}

        self.assertEqual(set(files), {"README.md", "src/app.py", "tests/test_app.py"})
        self.assertEqual(files["README.md"]["index_status"], "M")
        self.assertEqual(files["src/app.py"]["worktree_status"], "M")
        self.assertTrue(files["tests/test_app.py"]["untracked"])
        self.assertIn("documentation", files["README.md"]["review_lenses"])
        self.assertIn("tests", files["tests/test_app.py"]["review_lenses"])
        self.assertEqual(manifest["coverage"]["total_files"], 3)
        self.assertEqual(manifest["coverage"]["reviewed_files"], 0)

    def test_range_mode_uses_merge_base_and_reports_changed_line_ranges(self):
        self.commit_baseline()
        self.git("checkout", "-b", "feature")
        self.write("src/app.py", "def total():\n    value = 2\n    return value\n")
        self.write("config/settings.yaml", "feature: true\n")
        self.git("add", ".")
        self.git("commit", "-m", "feature change")

        manifest = self.run_manifest(
            "--mode",
            "range",
            "--base",
            "main",
            "--head",
            "feature",
        )
        files = {item["path"]: item for item in manifest["files"]}

        self.assertEqual(manifest["comparison"]["strategy"], "merge-base")
        self.assertEqual(set(files), {"config/settings.yaml", "src/app.py"})
        self.assertEqual(files["src/app.py"]["changed_new_line_ranges"], [[2, 3]])
        self.assertIn("configuration", files["config/settings.yaml"]["review_lenses"])


if __name__ == "__main__":
    unittest.main()

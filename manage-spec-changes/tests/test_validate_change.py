from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = SKILL_ROOT / "scripts" / "validate_change.py"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_manifest(change_dir: Path, **overrides: object) -> dict[str, object]:
    manifest: dict[str, object] = {
        "schemaVersion": 1,
        "changeId": change_dir.name,
        "status": "PROPOSED",
        "kind": "compact",
        "artifacts": {
            "proposal": "proposal.md",
            "specs": [],
        },
        "touches": {
            "specs": [],
            "contracts": [],
            "data": [],
            "security": [],
        },
        "blockingDecisions": [],
        "acceptedGaps": [],
    }
    manifest.update(overrides)
    if "stateHistory" not in overrides:
        status = str(manifest["status"])
        paths = {
            "PROPOSED": ["PROPOSED"],
            "READY": ["PROPOSED", "READY"],
            "ACTIVE": ["PROPOSED", "READY", "ACTIVE"],
            "VERIFYING": ["PROPOSED", "READY", "ACTIVE", "VERIFYING"],
            "COMPLETED": ["PROPOSED", "READY", "ACTIVE", "VERIFYING", "COMPLETED"],
            "COMPLETED WITH ACCEPTED GAPS": [
                "PROPOSED",
                "READY",
                "ACTIVE",
                "VERIFYING",
                "COMPLETED WITH ACCEPTED GAPS",
            ],
            "SUPERSEDED": ["PROPOSED", "SUPERSEDED"],
            "ABANDONED": ["PROPOSED", "ABANDONED"],
        }
        manifest["stateHistory"] = paths[status]
    write(change_dir / "change.json", json.dumps(manifest, indent=2) + "\n")
    return manifest


def write_proposal(change_dir: Path, requirements: str = "") -> None:
    write(
        change_dir / "proposal.md",
        "# Change proposal\n\n"
        "## Problem and Evidence\n\nObserved problem.\n\n"
        "## Desired Outcome\n\nObservable outcome.\n\n"
        "## Scope\n\nIn scope.\n\n"
        f"{requirements}",
    )


def run_validator(change_dir: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(change_dir), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


class ValidateChangeTests(unittest.TestCase):
    def test_valid_compact_proposal_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "clarify-export-copy"
            change_dir.mkdir(parents=True)
            write_manifest(change_dir)
            write_proposal(change_dir)

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PASS", result.stdout)
            self.assertIn("0 error(s)", result.stdout)

    def test_ready_change_cannot_have_blocking_decisions(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "export-api"
            change_dir.mkdir(parents=True)
            write_manifest(
                change_dir,
                status="READY",
                blockingDecisions=["D-002"],
                artifacts={
                    "proposal": "proposal.md",
                    "specs": [],
                    "tasks": "tasks.md",
                },
            )
            write_proposal(change_dir)
            write(change_dir / "tasks.md", "# Tasks\n")

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_STATUS_BLOCKED", result.stdout)

    def test_duplicate_requirement_declaration_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            write_manifest(
                change_dir,
                kind="full",
                artifacts={
                    "proposal": "proposal.md",
                    "specs": ["specs/export.md", "specs/audit.md"],
                    "tasks": "tasks.md",
                },
            )
            write_proposal(change_dir)
            write(
                change_dir / "specs" / "export.md",
                "# Export\n\n## ADDED\n\n### R-001: Export permission\n\n"
                "The system SHALL check permission.\n\n"
                "#### SC-001-A: Allowed\n\n- Given permission\n- When exporting\n- Then start\n",
            )
            write(
                change_dir / "specs" / "audit.md",
                "# Audit\n\n## ADDED\n\n### R-001: Audit export\n\n"
                "The system SHALL audit.\n\n"
                "#### SC-001-B: Audit\n\n- Given export\n- When accepted\n- Then audit\n",
            )
            write(change_dir / "tasks.md", "# Tasks\n")

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_DUPLICATE_ID", result.stdout)
            self.assertIn("R-001", result.stdout)

    def test_completed_change_requires_traceability_and_canonical_sync(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            change_dir = root / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            write_manifest(
                change_dir,
                status="COMPLETED",
                kind="full",
                artifacts={
                    "proposal": "proposal.md",
                    "specs": ["specs/export.md"],
                    "tasks": "tasks.md",
                    "evidence": "evidence.md",
                },
                verification={"implementationState": "commit:abc123"},
            )
            write_proposal(change_dir)
            write(
                change_dir / "specs" / "export.md",
                "# Export\n\n## MODIFIED\n\n### R-001: Export permission\n\n"
                "The system SHALL check permission.\n\n"
                "#### SC-001-A: Denied\n\n- Given no permission\n- When exporting\n"
                "- Then deny without creating a job\n",
            )
            write(
                change_dir / "tasks.md",
                "# Tasks\n\n- [x] T-001 Enforce permission\n  - Covers: R-001, SC-001-A\n",
            )
            write(
                change_dir / "evidence.md",
                "# Evidence\n\nVerification status: PASS\n\n"
                "## Traceability\n\n| Requirement / scenario | Task | Evidence | Result |\n"
                "|---|---|---|---|\n| R-001 | T-001 | V-001 | Pass |\n\n"
                "## Checks Run\n\n### V-001: Permission test\n",
            )

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_TRACE_MISSING", result.stdout)
            self.assertIn("SC-001-A", result.stdout)
            self.assertIn("E_CANONICAL_SYNC", result.stdout)

    def test_fully_traced_completed_change_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            change_dir = root / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            canonical = root / "specs" / "export.md"
            write(canonical, "# Current export policy\n")
            write_manifest(
                change_dir,
                status="COMPLETED",
                kind="full",
                artifacts={
                    "proposal": "proposal.md",
                    "specs": ["specs/export.md"],
                    "tasks": "tasks.md",
                    "evidence": "evidence.md",
                },
                verification={"implementationState": "commit:abc123"},
                canonicalSync={
                    "status": "applied",
                    "files": ["export.md"],
                },
            )
            write_proposal(change_dir)
            write(
                change_dir / "specs" / "export.md",
                "# Export\n\n## MODIFIED\n\n### R-001: Export permission\n\n"
                "The system SHALL check permission.\n\n"
                "#### SC-001-A: Denied\n\n- Given no permission\n- When exporting\n"
                "- Then deny without creating a job\n",
            )
            write(
                change_dir / "tasks.md",
                "# Tasks\n\n- [x] T-001 Enforce permission\n  - Covers: R-001, SC-001-A\n",
            )
            write(
                change_dir / "evidence.md",
                "# Evidence\n\nVerification status: PASS\n\n"
                "## Traceability\n\n| Requirement / scenario | Task | Evidence | Result |\n"
                "|---|---|---|---|\n"
                "| R-001 / SC-001-A | T-001 | V-001 | Pass |\n\n"
                "## Checks Run\n\n### V-001: Permission test\n\n"
                "- Observed: denied and no job created.\n",
            )

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PASS", result.stdout)

    def test_active_change_overlap_is_reported_and_can_be_strict(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            changes = Path(temp) / "changes"
            first = changes / "export-policy"
            second = changes / "export-api"
            first.mkdir(parents=True)
            second.mkdir(parents=True)
            write_manifest(
                first,
                status="ACTIVE",
                touches={
                    "specs": ["export"],
                    "contracts": ["POST /exports"],
                    "data": [],
                    "security": [],
                },
            )
            write_proposal(first)
            write_manifest(
                second,
                status="READY",
                touches={
                    "specs": ["export"],
                    "contracts": ["POST /exports"],
                    "data": [],
                    "security": [],
                },
            )
            write_proposal(second)

            warning_result = run_validator(first)
            strict_result = run_validator(first, "--strict-conflicts")

            self.assertEqual(warning_result.returncode, 0, warning_result.stdout)
            self.assertIn("W_ACTIVE_CONFLICT", warning_result.stdout)
            self.assertEqual(strict_result.returncode, 1)
            self.assertIn("E_ACTIVE_CONFLICT", strict_result.stdout)

    def test_archived_change_uses_original_id_and_workspace_canonical_specs(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            change_dir = root / "changes" / "archive" / "2026-09-12-export-policy"
            change_dir.mkdir(parents=True)
            write(root / "specs" / "export.md", "# Current export policy\n")
            write_manifest(
                change_dir,
                changeId="export-policy",
                status="COMPLETED",
                kind="full",
                artifacts={
                    "proposal": "proposal.md",
                    "specs": ["specs/export.md"],
                    "tasks": "tasks.md",
                    "evidence": "evidence.md",
                },
                verification={"implementationState": "commit:abc123"},
                canonicalSync={"status": "applied", "files": ["export.md"]},
            )
            write_proposal(change_dir)
            write(
                change_dir / "specs" / "export.md",
                "# Export\n\n## MODIFIED\n\n### R-001: Export permission\n\n"
                "The system SHALL check permission.\n\n"
                "#### SC-001-A: Denied\n\n- Given no permission\n- When exporting\n"
                "- Then deny without creating a job\n",
            )
            write(
                change_dir / "tasks.md",
                "# Tasks\n\n- [x] T-001 Enforce permission\n  - Covers: R-001, SC-001-A\n",
            )
            write(
                change_dir / "evidence.md",
                "# Evidence\n\nVerification status: PASS\n\n"
                "## Traceability\n\n| Requirement / scenario | Task | Evidence | Result |\n"
                "|---|---|---|---|\n"
                "| R-001 / SC-001-A | T-001 | V-001 | Pass |\n\n"
                "## Checks Run\n\n### V-001: Permission test\n\n- Observed: denied.\n",
            )

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_task_mapping_rejects_unknown_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            write_manifest(
                change_dir,
                status="READY",
                artifacts={
                    "proposal": "proposal.md",
                    "specs": [],
                    "tasks": "tasks.md",
                },
            )
            write_proposal(
                change_dir,
                "## Requirements\n\n### R-001: Export permission\n\n"
                "#### SC-001-A: Authorized\n",
            )
            write(
                change_dir / "tasks.md",
                "# Tasks\n\n- [ ] T-001 Implement policy\n"
                "  - Covers: R-001, SC-001-A, R-999\n",
            )

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_TASK_UNKNOWN", result.stdout)
            self.assertIn("R-999", result.stdout)

    def test_completed_change_rejects_failed_traceability_row(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            write_manifest(
                change_dir,
                status="COMPLETED",
                artifacts={
                    "proposal": "proposal.md",
                    "specs": [],
                    "tasks": "tasks.md",
                    "evidence": "evidence.md",
                },
                verification={"implementationState": "commit:abc123"},
                canonicalSync={"status": "not-required", "files": []},
            )
            write_proposal(
                change_dir,
                "## Requirements\n\n### R-001: Export permission\n\n"
                "#### SC-001-A: Authorized\n",
            )
            write(
                change_dir / "tasks.md",
                "# Tasks\n\n- [x] T-001 Implement policy\n"
                "  - Covers: R-001, SC-001-A\n",
            )
            write(
                change_dir / "evidence.md",
                "# Evidence\n\nVerification status: PASS\n\n"
                "## Traceability\n\n| Requirement / scenario | Task | Evidence | Result |\n"
                "|---|---|---|---|\n"
                "| R-001 / SC-001-A | T-001 | V-001 | Fail |\n\n"
                "## Checks Run\n\n### V-001: Permission test\n\n- Observed: failed.\n",
            )

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_TRACE_RESULT", result.stdout)

    def test_illegal_lifecycle_jump_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            write_manifest(
                change_dir,
                status="COMPLETED",
                stateHistory=["PROPOSED", "COMPLETED"],
                artifacts={
                    "proposal": "proposal.md",
                    "specs": [],
                    "tasks": "tasks.md",
                    "evidence": "evidence.md",
                },
                verification={"implementationState": "commit:abc123"},
                canonicalSync={"status": "not-required", "files": []},
            )
            write_proposal(change_dir)
            write(change_dir / "tasks.md", "# Tasks\n")
            write(
                change_dir / "evidence.md",
                "# Evidence\n\nVerification status: PASS\n\n## Traceability\n\n",
            )

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_STATE_TRANSITION", result.stdout)

    def test_manifest_requires_state_history(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            manifest = write_manifest(change_dir)
            manifest.pop("stateHistory")
            write(change_dir / "change.json", json.dumps(manifest, indent=2) + "\n")
            write_proposal(change_dir)

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_STATE_HISTORY", result.stdout)

    def test_artifact_path_cannot_escape_change_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            change_dir = root / "changes" / "export-policy"
            change_dir.mkdir(parents=True)
            write(root / "outside.md", "# Not a proposal\n")
            write_manifest(
                change_dir,
                artifacts={"proposal": "../../outside.md", "specs": []},
            )

            result = run_validator(change_dir)

            self.assertEqual(result.returncode, 1)
            self.assertIn("E_ARTIFACT_PATH", result.stdout)

    def test_json_output_is_machine_readable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            change_dir = Path(temp) / "changes" / "clarify-export-copy"
            change_dir.mkdir(parents=True)
            write_manifest(change_dir)
            write_proposal(change_dir)

            result = run_validator(change_dir, "--json")
            payload = json.loads(result.stdout)

            self.assertEqual(result.returncode, 0)
            self.assertTrue(payload["valid"])
            self.assertEqual(payload["errors"], 0)
            self.assertEqual(payload["issues"], [])


if __name__ == "__main__":
    unittest.main()

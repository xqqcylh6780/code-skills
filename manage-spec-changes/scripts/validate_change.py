#!/usr/bin/env python3
"""Validate a manage-spec-changes change directory using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Optional


SCHEMA_VERSION = 1
MANIFEST_NAME = "change.json"
CHANGE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIREMENT_DECL_RE = re.compile(r"^#{3,6}\s+(R-\d{3}):\s+\S", re.MULTILINE)
SCENARIO_DECL_RE = re.compile(r"^#{4,6}\s+(SC-\d{3}-[A-Z]):\s+\S", re.MULTILINE)
TASK_DECL_RE = re.compile(
    r"^[ \t]*-[ \t]*\[([ xX])\][ \t]+(T-\d{3})\b[^\n]*(?:\n(?![ \t]*-[ \t]*\[[ xX]\][ \t]+T-\d{3}\b)[^\n]*)*",
    re.MULTILINE,
)
EVIDENCE_DECL_RE = re.compile(r"^#{3,6}\s+(V-\d{3}):\s+\S", re.MULTILINE)
ID_RE = re.compile(r"\b(?:R-\d{3}|SC-\d{3}-[A-Z]|T-\d{3}|V-\d{3})\b")
DELTA_HEADING_RE = re.compile(
    r"^##\s+(ADDED|MODIFIED|REMOVED|RENAMED)(?:\s+REQUIREMENTS?)?\s*$",
    re.MULTILINE,
)
EVIDENCE_STATUS_RE = re.compile(
    r"^Verification status:\s*(PASS WITH ACCEPTED GAPS|PASS|FAIL|BLOCKED)\s*$",
    re.MULTILINE | re.IGNORECASE,
)

VALID_STATUSES = {
    "PROPOSED",
    "READY",
    "ACTIVE",
    "VERIFYING",
    "COMPLETED",
    "COMPLETED WITH ACCEPTED GAPS",
    "SUPERSEDED",
    "ABANDONED",
}
ACTIVE_STATUSES = {"PROPOSED", "READY", "ACTIVE", "VERIFYING"}
READY_OR_LATER = {
    "READY",
    "ACTIVE",
    "VERIFYING",
    "COMPLETED",
    "COMPLETED WITH ACCEPTED GAPS",
}
VERIFYING_OR_LATER = {
    "VERIFYING",
    "COMPLETED",
    "COMPLETED WITH ACCEPTED GAPS",
}
SUCCESS_TERMINAL = {"COMPLETED", "COMPLETED WITH ACCEPTED GAPS"}
TOUCH_CATEGORIES = ("specs", "contracts", "data", "security")
STATE_TRANSITIONS = {
    "PROPOSED": {"READY", "ABANDONED", "SUPERSEDED"},
    "READY": {"ACTIVE", "PROPOSED", "ABANDONED", "SUPERSEDED"},
    "ACTIVE": {"VERIFYING", "READY", "PROPOSED", "ABANDONED", "SUPERSEDED"},
    "VERIFYING": {
        "ACTIVE",
        "READY",
        "PROPOSED",
        "COMPLETED",
        "COMPLETED WITH ACCEPTED GAPS",
        "ABANDONED",
        "SUPERSEDED",
    },
    "COMPLETED": set(),
    "COMPLETED WITH ACCEPTED GAPS": {"ACTIVE"},
    "SUPERSEDED": set(),
    "ABANDONED": {"PROPOSED"},
}


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str


class ChangeValidator:
    def __init__(self, change_dir: Path, strict_conflicts: bool = False) -> None:
        self.change_dir = change_dir.resolve()
        self.strict_conflicts = strict_conflicts
        self.issues: list[Issue] = []
        self.manifest: dict[str, Any] = {}
        self.status = ""
        self.kind = ""
        self.artifacts: dict[str, Any] = {}
        self.texts: dict[str, str] = {}
        self.requirements: list[str] = []
        self.scenarios: list[str] = []
        self.tasks: list[tuple[str, bool, str]] = []
        self.evidence_ids: list[str] = []

    def error(self, code: str, message: str) -> None:
        self.issues.append(Issue("ERROR", code, message))

    def warning(self, code: str, message: str) -> None:
        self.issues.append(Issue("WARNING", code, message))

    def _is_archived(self) -> bool:
        return self.change_dir.parent.name.casefold() == "archive"

    def _changes_root(self) -> Path:
        return self.change_dir.parent.parent if self._is_archived() else self.change_dir.parent

    def validate(self) -> list[Issue]:
        if not self.change_dir.is_dir():
            self.error("E_CHANGE_DIR", f"Change directory does not exist: {self.change_dir}")
            return self.issues

        if not self._load_manifest():
            return self.issues

        self._validate_manifest_shape()
        self._load_artifacts()
        self._validate_delta_specs()
        self._collect_ids()
        self._validate_id_integrity()
        self._validate_status_gates()
        self._validate_task_coverage()
        self._validate_evidence()
        self._validate_canonical_sync()
        self._detect_active_conflicts()
        return self.issues

    def _load_manifest(self) -> bool:
        manifest_path = self.change_dir / MANIFEST_NAME
        if not manifest_path.is_file():
            self.error("E_MANIFEST_MISSING", f"Missing {MANIFEST_NAME}")
            return False
        try:
            raw = manifest_path.read_text(encoding="utf-8")
            data = json.loads(raw)
        except UnicodeDecodeError as exc:
            self.error("E_MANIFEST_ENCODING", f"{MANIFEST_NAME} is not valid UTF-8: {exc}")
            return False
        except json.JSONDecodeError as exc:
            self.error(
                "E_MANIFEST_JSON",
                f"{MANIFEST_NAME} is invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}",
            )
            return False
        if not isinstance(data, dict):
            self.error("E_MANIFEST_TYPE", f"{MANIFEST_NAME} root must be an object")
            return False
        self.manifest = data
        return True

    def _validate_manifest_shape(self) -> None:
        version = self.manifest.get("schemaVersion")
        if version != SCHEMA_VERSION:
            self.error(
                "E_SCHEMA_VERSION",
                f"schemaVersion must be {SCHEMA_VERSION}, got {version!r}",
            )

        change_id = self.manifest.get("changeId")
        if not isinstance(change_id, str) or not CHANGE_ID_RE.fullmatch(change_id):
            self.error("E_CHANGE_ID", "changeId must be lowercase hyphen-case")
        elif self._is_archived():
            archive_name = self.change_dir.name
            dated_name = re.fullmatch(r"\d{4}-\d{2}-\d{2}-(.+)", archive_name)
            archived_id = dated_name.group(1) if dated_name else archive_name
            if change_id != archived_id:
                self.error(
                    "E_CHANGE_ID_PATH",
                    f"changeId {change_id!r} does not match archived directory {archive_name!r}",
                )
        elif change_id != self.change_dir.name:
            self.error(
                "E_CHANGE_ID_PATH",
                f"changeId {change_id!r} does not match directory {self.change_dir.name!r}",
            )

        status = self.manifest.get("status")
        if not isinstance(status, str) or status not in VALID_STATUSES:
            self.error(
                "E_STATUS",
                f"status must be one of {', '.join(sorted(VALID_STATUSES))}",
            )
        else:
            self.status = status

        kind = self.manifest.get("kind")
        if kind not in {"compact", "full"}:
            self.error("E_KIND", "kind must be 'compact' or 'full'")
        else:
            self.kind = kind

        artifacts = self.manifest.get("artifacts")
        if not isinstance(artifacts, dict):
            self.error("E_ARTIFACTS", "artifacts must be an object")
        else:
            self.artifacts = artifacts
            proposal = artifacts.get("proposal")
            if not isinstance(proposal, str) or not proposal.strip():
                self.error("E_PROPOSAL_DECL", "artifacts.proposal must name proposal.md")
            specs = artifacts.get("specs", [])
            if not isinstance(specs, list) or not all(
                isinstance(value, str) and value.strip() for value in specs
            ):
                self.error("E_SPECS_DECL", "artifacts.specs must be an array of paths")
            elif self.kind == "full" and not specs:
                self.error("E_FULL_SPECS", "full changes require at least one delta specification")

        for list_field in ("blockingDecisions", "acceptedGaps"):
            value = self.manifest.get(list_field)
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                self.error("E_MANIFEST_FIELD", f"{list_field} must be an array of strings")

        self._validate_state_history()

        touches = self.manifest.get("touches")
        if not isinstance(touches, dict):
            self.error("E_TOUCHES", "touches must be an object")
        else:
            for category in TOUCH_CATEGORIES:
                values = touches.get(category, [])
                if not isinstance(values, list) or not all(
                    isinstance(value, str) and value.strip() for value in values
                ):
                    self.error(
                        "E_TOUCHES",
                        f"touches.{category} must be an array of non-empty strings",
                    )

    def _validate_state_history(self) -> None:
        history = self.manifest.get("stateHistory")
        if not isinstance(history, list) or not history or not all(
            isinstance(item, str) and item in VALID_STATUSES for item in history
        ):
            self.error(
                "E_STATE_HISTORY",
                "stateHistory must be a non-empty array of valid lifecycle states",
            )
            return
        if history[0] != "PROPOSED":
            self.error("E_STATE_HISTORY", "stateHistory must start with PROPOSED")
        if self.status and history[-1] != self.status:
            self.error(
                "E_STATE_CURRENT",
                f"stateHistory ends at {history[-1]} but manifest status is {self.status}",
            )
        for previous, current in zip(history, history[1:]):
            if current not in STATE_TRANSITIONS.get(previous, set()):
                self.error(
                    "E_STATE_TRANSITION",
                    f"Illegal lifecycle transition: {previous} -> {current}",
                )

    def _safe_artifact_path(self, relative: str, field: str) -> Optional[Path]:
        candidate = Path(relative)
        if candidate.is_absolute():
            self.error("E_ARTIFACT_PATH", f"{field} must use a relative path: {relative}")
            return None
        resolved = (self.change_dir / candidate).resolve()
        try:
            resolved.relative_to(self.change_dir)
        except ValueError:
            self.error("E_ARTIFACT_PATH", f"{field} escapes the change directory: {relative}")
            return None
        return resolved

    def _load_one_artifact(self, field: str, relative: Any) -> None:
        if not isinstance(relative, str) or not relative.strip():
            return
        path = self._safe_artifact_path(relative, f"artifacts.{field}")
        if path is None:
            return
        if not path.is_file():
            self.error("E_ARTIFACT_MISSING", f"Declared artifact does not exist: {relative}")
            return
        try:
            self.texts[relative] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            self.error("E_ARTIFACT_ENCODING", f"{relative} is not valid UTF-8: {exc}")

    def _load_artifacts(self) -> None:
        if not self.artifacts:
            return
        self._load_one_artifact("proposal", self.artifacts.get("proposal"))
        for spec in self.artifacts.get("specs", []):
            self._load_one_artifact("specs", spec)
        for field in ("design", "tasks", "evidence"):
            if field in self.artifacts:
                self._load_one_artifact(field, self.artifacts.get(field))

    def _validate_delta_specs(self) -> None:
        for spec in self.artifacts.get("specs", []) if self.artifacts else []:
            text = self.texts.get(spec)
            if text is not None and not DELTA_HEADING_RE.search(text):
                self.error(
                    "E_DELTA_OPERATION",
                    f"Delta specification {spec} must contain ADDED, MODIFIED, REMOVED, or RENAMED",
                )

    def _collect_ids(self) -> None:
        proposal = self.artifacts.get("proposal") if self.artifacts else None
        requirement_sources: list[tuple[str, str]] = []
        if isinstance(proposal, str) and proposal in self.texts:
            requirement_sources.append((proposal, self.texts[proposal]))
        for spec in self.artifacts.get("specs", []) if self.artifacts else []:
            if spec in self.texts:
                requirement_sources.append((spec, self.texts[spec]))

        declarations: list[tuple[str, str]] = []
        scenarios: list[tuple[str, str]] = []
        for source, text in requirement_sources:
            declarations.extend((match.group(1), source) for match in REQUIREMENT_DECL_RE.finditer(text))
            scenarios.extend((match.group(1), source) for match in SCENARIO_DECL_RE.finditer(text))

        self.requirements = [item[0] for item in declarations]
        self.scenarios = [item[0] for item in scenarios]
        self._report_duplicate_ids(declarations + scenarios)

        tasks_path = self.artifacts.get("tasks") if self.artifacts else None
        if isinstance(tasks_path, str) and tasks_path in self.texts:
            for match in TASK_DECL_RE.finditer(self.texts[tasks_path]):
                task_id = match.group(2)
                self.tasks.append((task_id, match.group(1).lower() == "x", match.group(0)))
            self._report_duplicate_ids([(task[0], tasks_path) for task in self.tasks])

        evidence_path = self.artifacts.get("evidence") if self.artifacts else None
        if isinstance(evidence_path, str) and evidence_path in self.texts:
            self.evidence_ids = EVIDENCE_DECL_RE.findall(self.texts[evidence_path])
            self._report_duplicate_ids([(item, evidence_path) for item in self.evidence_ids])

    def _report_duplicate_ids(self, declarations: Iterable[tuple[str, str]]) -> None:
        by_id: dict[str, list[str]] = {}
        for identifier, source in declarations:
            by_id.setdefault(identifier, []).append(source)
        for identifier, sources in sorted(by_id.items()):
            if len(sources) > 1:
                self.error(
                    "E_DUPLICATE_ID",
                    f"{identifier} is declared more than once: {', '.join(sources)}",
                )

    def _validate_id_integrity(self) -> None:
        requirement_set = set(self.requirements)
        for scenario in sorted(set(self.scenarios)):
            requirement = f"R-{scenario[3:6]}"
            if requirement not in requirement_set:
                self.error(
                    "E_SCENARIO_PARENT",
                    f"{scenario} has no declared parent requirement {requirement}",
                )

    def _validate_status_gates(self) -> None:
        if not self.status:
            return
        blockers = self.manifest.get("blockingDecisions", [])
        if self.status in READY_OR_LATER and blockers:
            self.error(
                "E_STATUS_BLOCKED",
                f"status {self.status} is invalid with blocking decisions: {', '.join(blockers)}",
            )

        if self.status in READY_OR_LATER and self.kind == "full" and "tasks" not in self.artifacts:
            self.error("E_TASKS_REQUIRED", f"full change in {self.status} requires artifacts.tasks")

        if self.status in VERIFYING_OR_LATER:
            if "evidence" not in self.artifacts:
                self.error("E_EVIDENCE_REQUIRED", f"status {self.status} requires artifacts.evidence")
            verification = self.manifest.get("verification")
            if not isinstance(verification, dict) or not isinstance(
                verification.get("implementationState"), str
            ) or not verification.get("implementationState", "").strip():
                self.error(
                    "E_IMPLEMENTATION_STATE",
                    f"status {self.status} requires verification.implementationState",
                )

        if self.status == "COMPLETED" and self.manifest.get("acceptedGaps"):
            self.error(
                "E_COMPLETED_GAPS",
                "COMPLETED cannot contain acceptedGaps; use COMPLETED WITH ACCEPTED GAPS",
            )
        if self.status == "COMPLETED WITH ACCEPTED GAPS" and not self.manifest.get("acceptedGaps"):
            self.error(
                "E_ACCEPTED_GAPS",
                "COMPLETED WITH ACCEPTED GAPS requires at least one acceptedGaps entry",
            )
        if self.status == "SUPERSEDED" and not self.manifest.get("supersededBy"):
            self.error("E_SUPERSEDED_BY", "SUPERSEDED requires supersededBy")
        if self.status == "ABANDONED" and not self.manifest.get("terminalReason"):
            self.error("E_TERMINAL_REASON", "ABANDONED requires terminalReason")

    def _validate_task_coverage(self) -> None:
        if self.status not in READY_OR_LATER:
            return
        if self.kind == "full" and not self.tasks:
            self.error("E_TASK_DECLARATION", "full ready/active change has no T-### task declarations")
            return

        covered: set[str] = set()
        for task_id, _checked, block in self.tasks:
            match = re.search(
                r"^[ \t]*-[ \t]+Covers:[ \t]*(.+)$",
                block,
                re.MULTILINE | re.IGNORECASE,
            )
            if not match:
                self.warning("W_TASK_COVERS", f"{task_id} has no Covers mapping")
                continue
            covered.update(ID_RE.findall(match.group(1)))

        declared_behavior = set(self.requirements + self.scenarios)
        for identifier in sorted(
            item for item in covered if item.startswith(("R-", "SC-")) and item not in declared_behavior
        ):
            self.error("E_TASK_UNKNOWN", f"Task coverage references undeclared behavior {identifier}")

        for identifier in sorted(declared_behavior - covered):
            self.error("E_TASK_COVERAGE", f"{identifier} is not covered by any declared task")

        if self.status in SUCCESS_TERMINAL:
            for task_id, checked, _block in self.tasks:
                if not checked:
                    self.error("E_TASK_INCOMPLETE", f"{task_id} is not complete in terminal status")

    def _traceability_text(self, evidence_text: str) -> str:
        match = re.search(
            r"^##\s+Traceability\s*$\n(.*?)(?=^##\s+|\Z)",
            evidence_text,
            re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        return match.group(1) if match else ""

    def _validate_evidence(self) -> None:
        if self.status not in VERIFYING_OR_LATER:
            return
        evidence_path = self.artifacts.get("evidence")
        if not isinstance(evidence_path, str) or evidence_path not in self.texts:
            return
        text = self.texts[evidence_path]
        status_match = EVIDENCE_STATUS_RE.search(text)
        evidence_status = status_match.group(1).upper() if status_match else ""
        if not evidence_status:
            self.error("E_EVIDENCE_STATUS", "evidence must declare Verification status")
        elif self.status == "COMPLETED" and evidence_status != "PASS":
            self.error("E_EVIDENCE_STATUS", "COMPLETED requires evidence status PASS")
        elif (
            self.status == "COMPLETED WITH ACCEPTED GAPS"
            and evidence_status != "PASS WITH ACCEPTED GAPS"
        ):
            self.error(
                "E_EVIDENCE_STATUS",
                "COMPLETED WITH ACCEPTED GAPS requires matching evidence status",
            )

        traceability = self._traceability_text(text)
        if not traceability:
            self.error("E_TRACEABILITY_SECTION", "evidence is missing a Traceability section")
            return
        traced = set(ID_RE.findall(traceability))
        required = set(self.requirements + self.scenarios)
        for identifier in sorted(required - traced):
            self.error("E_TRACE_MISSING", f"{identifier} is missing from evidence traceability")

        declared_tasks = {task[0] for task in self.tasks}
        declared_evidence = set(self.evidence_ids)
        for identifier in sorted(traced):
            if identifier.startswith("T-") and identifier not in declared_tasks:
                self.error("E_TRACE_UNKNOWN", f"Traceability references unknown task {identifier}")
            if identifier.startswith("V-") and identifier not in declared_evidence:
                self.error("E_TRACE_UNKNOWN", f"Traceability references unknown evidence {identifier}")

        if self.status in SUCCESS_TERMINAL:
            for task_id in sorted(declared_tasks - traced):
                self.error("E_TASK_TRACE", f"Completed task {task_id} is missing from traceability")
            for line in traceability.splitlines():
                stripped = line.strip()
                if not (stripped.startswith("|") and stripped.endswith("|")):
                    continue
                cells = [cell.strip() for cell in stripped.strip("|").split("|")]
                row_ids = ID_RE.findall(stripped)
                if not row_ids or not cells:
                    continue
                result = cells[-1].casefold()
                if result != "pass":
                    self.error(
                        "E_TRACE_RESULT",
                        f"Terminal traceability row for {', '.join(row_ids)} has result {cells[-1]!r}",
                    )

    def _canonical_root(self, sync: dict[str, Any]) -> Optional[Path]:
        root_value = sync.get("root", "specs")
        if not isinstance(root_value, str) or not root_value.strip():
            self.error("E_CANONICAL_ROOT", "canonicalSync.root must be a relative path")
            return None
        candidate = Path(root_value)
        if candidate.is_absolute():
            self.error("E_CANONICAL_ROOT", "canonicalSync.root must be relative")
            return None
        workspace_root = self._changes_root().parent.resolve()
        root = (workspace_root / candidate).resolve()
        try:
            root.relative_to(workspace_root)
        except ValueError:
            self.error("E_CANONICAL_ROOT", "canonicalSync.root escapes the change workspace")
            return None
        return root

    def _validate_canonical_sync(self) -> None:
        if self.status not in SUCCESS_TERMINAL:
            return
        specs = self.artifacts.get("specs", [])
        sync = self.manifest.get("canonicalSync")
        if not isinstance(sync, dict):
            if specs:
                self.error(
                    "E_CANONICAL_SYNC",
                    "successful terminal status requires canonicalSync for delta specifications",
                )
            return

        sync_status = sync.get("status")
        if sync_status not in {"applied", "not-required"}:
            self.error(
                "E_CANONICAL_SYNC",
                "canonicalSync.status must be applied or not-required in terminal status",
            )
            return
        if specs and sync_status != "applied":
            self.error(
                "E_CANONICAL_SYNC",
                "delta specifications require canonicalSync.status applied",
            )
            return
        if sync_status == "not-required":
            return

        files = sync.get("files")
        if not isinstance(files, list) or not files or not all(
            isinstance(item, str) and item.strip() for item in files
        ):
            self.error("E_CANONICAL_FILES", "applied canonicalSync requires a non-empty files array")
            return
        root = self._canonical_root(sync)
        if root is None:
            return
        for relative in files:
            path = (root / relative).resolve()
            try:
                path.relative_to(root)
            except ValueError:
                self.error("E_CANONICAL_FILE", f"Canonical file escapes its root: {relative}")
                continue
            if not path.is_file():
                self.error("E_CANONICAL_FILE", f"Canonical file does not exist: {path}")

    def _normalized_touches(self, manifest: dict[str, Any]) -> dict[str, set[str]]:
        touches = manifest.get("touches")
        if not isinstance(touches, dict):
            return {category: set() for category in TOUCH_CATEGORIES}
        result: dict[str, set[str]] = {}
        for category in TOUCH_CATEGORIES:
            values = touches.get(category, [])
            result[category] = {
                item.strip().casefold()
                for item in values
                if isinstance(item, str) and item.strip()
            } if isinstance(values, list) else set()
        return result

    def _detect_active_conflicts(self) -> None:
        if self.status not in ACTIVE_STATUSES:
            return
        own = self._normalized_touches(self.manifest)
        if not any(own.values()):
            return
        changes_root = self._changes_root()
        for sibling in sorted(changes_root.iterdir(), key=lambda path: path.name):
            if sibling == self.change_dir or not sibling.is_dir() or sibling.name == "archive":
                continue
            manifest_path = sibling / MANIFEST_NAME
            if not manifest_path.is_file():
                continue
            try:
                other = json.loads(manifest_path.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError, OSError):
                self.warning(
                    "W_CONFLICT_SCAN",
                    f"Could not read sibling manifest for conflict detection: {manifest_path}",
                )
                continue
            if not isinstance(other, dict) or other.get("status") not in ACTIVE_STATUSES:
                continue
            overlaps: list[str] = []
            other_touches = self._normalized_touches(other)
            for category in TOUCH_CATEGORIES:
                shared = sorted(own[category] & other_touches[category])
                if shared:
                    overlaps.append(f"{category}={','.join(shared)}")
            if overlaps:
                other_id = other.get("changeId", sibling.name)
                message = f"Active change {other_id} overlaps on {'; '.join(overlaps)}"
                if self.strict_conflicts:
                    self.error("E_ACTIVE_CONFLICT", message)
                else:
                    self.warning("W_ACTIVE_CONFLICT", message)


def summary_counts(issues: Iterable[Issue]) -> tuple[int, int]:
    counts = Counter(issue.severity for issue in issues)
    return counts["ERROR"], counts["WARNING"]


def render_text(change_dir: Path, issues: list[Issue]) -> str:
    lines = [f"Change: {change_dir.resolve()}"]
    lines.extend(f"{issue.severity} {issue.code} {issue.message}" for issue in issues)
    errors, warnings = summary_counts(issues)
    result = "PASS" if errors == 0 else "FAIL"
    lines.append(f"{result}: {errors} error(s), {warnings} warning(s)")
    return "\n".join(lines)


def render_json(change_dir: Path, issues: list[Issue]) -> str:
    errors, warnings = summary_counts(issues)
    payload = {
        "change": str(change_dir.resolve()),
        "valid": errors == 0,
        "errors": errors,
        "warnings": warnings,
        "issues": [asdict(issue) for issue in issues],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a manage-spec-changes change directory.",
    )
    parser.add_argument("change_dir", type=Path, help="Path to an active or archived change")
    parser.add_argument(
        "--strict-conflicts",
        action="store_true",
        help="Treat overlaps with other active changes as errors instead of warnings",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    validator = ChangeValidator(args.change_dir, strict_conflicts=args.strict_conflicts)
    issues = validator.validate()
    output = render_json(args.change_dir, issues) if args.json else render_text(args.change_dir, issues)
    print(output)
    errors, _warnings = summary_counts(issues)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Build a deterministic, read-only manifest for a Git code review."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath


HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
CONFIG_NAMES = {
    ".editorconfig",
    ".env",
    ".gitattributes",
    ".gitignore",
    "dockerfile",
    "makefile",
    "package.json",
    "pyproject.toml",
}
CONFIG_EXTENSIONS = {".ini", ".json", ".properties", ".toml", ".xml", ".yaml", ".yml"}
DOC_EXTENSIONS = {".md", ".mdx", ".rst", ".txt"}
GENERATED_PARTS = {"build", "coverage", "dist", "generated", "node_modules", "vendor"}
LOCK_NAMES = {
    "cargo.lock",
    "composer.lock",
    "go.sum",
    "package-lock.json",
    "pnpm-lock.yaml",
    "poetry.lock",
    "uv.lock",
    "yarn.lock",
}


def run_git(repo: Path, *args: str) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        error = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(error or f"git {' '.join(args)} failed")
    return completed.stdout


def decode_path(value: bytes) -> str:
    return value.decode("utf-8", errors="surrogateescape").replace("\\", "/")


def parse_porcelain(data: bytes) -> list[dict]:
    fields = data.split(b"\0")
    files = []
    index = 0
    while index < len(fields) and fields[index]:
        record = fields[index]
        index += 1
        status = record[:2].decode("ascii", errors="replace")
        path = decode_path(record[3:])
        old_path = None
        if status[0] in "RC" or status[1] in "RC":
            old_path = decode_path(fields[index])
            index += 1
        files.append(
            {
                "path": path,
                "old_path": old_path,
                "status_code": status,
                "index_status": None if status[0] in {" ", "?"} else status[0],
                "worktree_status": None if status[1] in {" ", "?"} else status[1],
                "untracked": status == "??",
            }
        )
    return files


def parse_name_status(data: bytes) -> list[dict]:
    fields = data.split(b"\0")
    files = []
    index = 0
    while index < len(fields) and fields[index]:
        status = fields[index].decode("ascii", errors="replace")
        index += 1
        old_path = None
        if status.startswith(("R", "C")):
            old_path = decode_path(fields[index])
            path = decode_path(fields[index + 1])
            index += 2
        else:
            path = decode_path(fields[index])
            index += 1
        files.append(
            {
                "path": path,
                "old_path": old_path,
                "status_code": status,
                "index_status": None,
                "worktree_status": None,
                "untracked": False,
            }
        )
    return files


def parse_hunks(patch: str) -> tuple[list[list[int]], list[list[int]]]:
    changed = []
    deleted = []
    for line in patch.splitlines():
        match = HUNK_RE.match(line)
        if not match:
            continue
        old_start = int(match.group(1))
        old_count = int(match.group(2) or "1")
        new_start = int(match.group(3))
        new_count = int(match.group(4) or "1")
        if new_count:
            changed.append([new_start, new_start + new_count - 1])
        if old_count and not new_count:
            deleted.append([old_start, old_start + old_count - 1])
    return merge_ranges(changed), merge_ranges(deleted)


def merge_ranges(ranges: list[list[int]]) -> list[list[int]]:
    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def lenses_for(path_text: str) -> list[str]:
    path = PurePosixPath(path_text)
    lowered = path_text.lower()
    name = path.name.lower()
    suffix = path.suffix.lower()
    parts = {part.lower() for part in path.parts}
    lenses = []

    if suffix in DOC_EXTENSIONS or name in {"license", "notice"}:
        lenses.append("documentation")
    if (
        "test" in parts
        or "tests" in parts
        or "spec" in parts
        or "specs" in parts
        or re.search(r"(^|[._-])(test|spec)([._-]|$)", name)
    ):
        lenses.append("tests")
    if suffix in CONFIG_EXTENSIONS or name in CONFIG_NAMES:
        lenses.append("configuration")
    if name in LOCK_NAMES:
        lenses.append("dependency-lock")
    if GENERATED_PARTS & parts or name.endswith((".generated.ts", ".g.dart", ".designer.cs")):
        lenses.append("generated-or-vendored")
    if "migration" in parts or "migrations" in parts or re.search(r"(^|[/_-])migrat", lowered):
        lenses.append("data-migration")
    if re.search(r"auth|permission|policy|secret|token|session|crypto|credential", lowered):
        lenses.append("security-boundary")
    if re.search(r"(^|/)(api|routes?|controllers?|handlers?)(/|$)", lowered):
        lenses.append("public-interface")
    if re.search(r"(^|/)(ui|views?|screens?|components?)(/|$)", lowered):
        lenses.append("user-interface")
    return lenses or ["general-code"]


def review_unit_for(path_text: str) -> str:
    parts = PurePosixPath(path_text).parts
    if len(parts) == 1:
        return "repository-root"
    if parts[0] in {"app", "apps", "packages", "services"} and len(parts) > 2:
        return "/".join(parts[:2])
    return parts[0]


def untracked_ranges(repo: Path, path_text: str) -> list[list[int]]:
    path = repo / Path(*PurePosixPath(path_text).parts)
    try:
        content = path.read_bytes()
    except OSError:
        return []
    if b"\0" in content:
        return []
    line_count = len(content.splitlines())
    return [[1, line_count]] if line_count else []


def diff_ranges(repo: Path, prefix: list[str], path_text: str) -> tuple[list[list[int]], list[list[int]]]:
    patch = run_git(repo, *prefix, "--unified=0", "--no-color", "--", path_text)
    return parse_hunks(patch.decode("utf-8", errors="replace"))


def collect_files(repo: Path, args: argparse.Namespace) -> tuple[list[dict], dict]:
    if args.mode == "worktree":
        raw = run_git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all")
        files = parse_porcelain(raw)
        comparison = {"base": "HEAD", "head": "WORKTREE", "strategy": "index-and-worktree"}
        for item in files:
            if item["untracked"]:
                item["changed_new_line_ranges"] = untracked_ranges(repo, item["path"])
                item["deleted_old_line_ranges"] = []
                continue
            changed = []
            deleted = []
            if item["index_status"]:
                new_ranges, old_ranges = diff_ranges(repo, ["diff", "--cached"], item["path"])
                changed.extend(new_ranges)
                deleted.extend(old_ranges)
            if item["worktree_status"]:
                new_ranges, old_ranges = diff_ranges(repo, ["diff"], item["path"])
                changed.extend(new_ranges)
                deleted.extend(old_ranges)
            item["changed_new_line_ranges"] = merge_ranges(changed)
            item["deleted_old_line_ranges"] = merge_ranges(deleted)
        return files, comparison

    if args.mode == "staged":
        raw = run_git(repo, "diff", "--cached", "--name-status", "-z")
        files = parse_name_status(raw)
        comparison = {"base": "HEAD", "head": "INDEX", "strategy": "index-vs-head"}
        diff_prefix = ["diff", "--cached"]
    elif args.mode == "range":
        if not args.base:
            raise ValueError("--base is required for range mode")
        head = args.head or "HEAD"
        raw = run_git(repo, "diff", "--name-status", "-z", f"{args.base}...{head}")
        files = parse_name_status(raw)
        comparison = {"base": args.base, "head": head, "strategy": "merge-base"}
        diff_prefix = ["diff", f"{args.base}...{head}"]
    else:
        if not args.commit:
            raise ValueError("--commit is required for commit mode")
        raw = run_git(
            repo,
            "diff-tree",
            "--root",
            "--no-commit-id",
            "--name-status",
            "-r",
            "-z",
            args.commit,
        )
        files = parse_name_status(raw)
        comparison = {"base": f"{args.commit}^", "head": args.commit, "strategy": "commit-parent"}
        diff_prefix = ["show", "--format=", args.commit]

    for item in files:
        changed, deleted = diff_ranges(repo, diff_prefix, item["path"])
        item["changed_new_line_ranges"] = changed
        item["deleted_old_line_ranges"] = deleted
    return files, comparison


def build_manifest(repo_arg: str, args: argparse.Namespace) -> dict:
    requested_repo = Path(repo_arg).resolve()
    root_text = run_git(requested_repo, "rev-parse", "--show-toplevel").decode("utf-8").strip()
    repo = Path(root_text).resolve()
    files, comparison = collect_files(repo, args)

    units = defaultdict(list)
    for item in files:
        item["review_lenses"] = lenses_for(item["path"])
        item["review_unit"] = review_unit_for(item["path"])
        item["coverage_state"] = "pending"
        units[item["review_unit"]].append(item["path"])

    files.sort(key=lambda item: item["path"])
    review_units = [
        {"name": name, "files": sorted(paths), "coverage_state": "pending"}
        for name, paths in sorted(units.items())
    ]
    return {
        "schema_version": 1,
        "repository_root": repo.as_posix(),
        "mode": args.mode,
        "comparison": comparison,
        "files": files,
        "review_units": review_units,
        "coverage": {
            "total_files": len(files),
            "reviewed_files": 0,
            "skipped_files": 0,
            "pending_files": len(files),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Path inside the Git repository")
    parser.add_argument("--mode", choices=("worktree", "staged", "range", "commit"), default="worktree")
    parser.add_argument("--base", help="Base revision for range mode")
    parser.add_argument("--head", help="Head revision for range mode (default: HEAD)")
    parser.add_argument("--commit", help="Commit revision for commit mode")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = build_manifest(args.repo, args)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    json.dump(manifest, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

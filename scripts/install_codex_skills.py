#!/usr/bin/env python3
"""Install selected skills from this repository into a Codex discovery directory."""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORE = {'.git', '.github', 'scripts'}


def available_skills() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for child in ROOT.iterdir():
        if child.is_dir() and child.name not in IGNORE and (child / 'SKILL.md').is_file():
            result[child.name] = child
    return dict(sorted(result.items()))


def target_dir(scope: str, project: str | None) -> Path:
    if scope == 'user':
        return Path.home() / '.agents' / 'skills'
    if not project:
        raise SystemExit('--project is required with --scope project')
    return Path(project).expanduser().resolve() / '.agents' / 'skills'


def main() -> int:
    parser = argparse.ArgumentParser(description='Install code-skills into Codex .agents/skills discovery paths.')
    parser.add_argument('--scope', choices=('user', 'project'), default='user')
    parser.add_argument('--project', help='Project root when --scope project is used.')
    parser.add_argument('--skills', nargs='*', help='Skill names to install. Omit to install all skills.')
    parser.add_argument('--force', action='store_true', help='Replace an existing installed skill directory.')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be installed without changing files.')
    args = parser.parse_args()

    available = available_skills()
    requested = args.skills or list(available)
    unknown = [name for name in requested if name not in available]
    if unknown:
        print('Unknown skill(s): ' + ', '.join(unknown), file=sys.stderr)
        print('Available: ' + ', '.join(available), file=sys.stderr)
        return 2

    destination = target_dir(args.scope, args.project)
    print(f'Codex skill destination: {destination}')

    changed = 0
    skipped = 0
    for name in requested:
        src = available[name]
        dst = destination / name
        if dst.exists() or dst.is_symlink():
            if not args.force:
                print(f'SKIP {name}: {dst} already exists (use --force to replace)')
                skipped += 1
                continue
            print(f'REPLACE {name}: {dst}')
            if not args.dry_run:
                if dst.is_dir() and not dst.is_symlink():
                    shutil.rmtree(dst)
                else:
                    dst.unlink()
        else:
            print(f'INSTALL {name}: {dst}')

        if not args.dry_run:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst)
        changed += 1

    print(f'Done: {changed} install/replace action(s), {skipped} skipped.')
    print('In Codex CLI/IDE, run /skills or type $ to confirm the skill is visible. Restart Codex if an update does not appear.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

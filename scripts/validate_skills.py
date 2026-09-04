#!/usr/bin/env python3
"""Validate code-skills repository structure without third-party dependencies."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORE_TOP_LEVEL = {'.git', '.github', 'scripts'}
LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
MAX_DESCRIPTION_CHARS = 420
TOTAL_DESCRIPTION_BUDGET = 6000


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding='utf-8-sig')
    if not text.startswith('---\n'):
        fail(errors, f'{path.relative_to(ROOT)}: missing YAML frontmatter')
        return {}
    end = text.find('\n---\n', 4)
    if end < 0:
        fail(errors, f'{path.relative_to(ROOT)}: unterminated YAML frontmatter')
        return {}
    block = text[4:end]
    data: dict[str, str] = {}
    current = None
    for raw in block.splitlines():
        m = re.match(r'^([A-Za-z0-9_-]+):(?:\s*(.*))?$', raw)
        if m:
            current = m.group(1)
            value = (m.group(2) or '').strip()
            data[current] = '' if value in {'>-', '|-', '>', '|'} else value.strip('"\'')
        elif current and raw.startswith((' ', '\t')):
            data[current] = (data[current] + ' ' + raw.strip()).strip()
    return data


def skill_dirs() -> list[Path]:
    result = []
    for p in ROOT.iterdir():
        if not p.is_dir() or p.name in IGNORE_TOP_LEVEL or p.name.startswith('.'):
            continue
        if (p / 'SKILL.md').exists():
            result.append(p)
    return sorted(result, key=lambda p: p.name)


def validate_local_links(md: Path, errors: list[str]) -> None:
    text = md.read_text(encoding='utf-8-sig')
    for target in LINK_RE.findall(text):
        target = target.strip()
        if not target or target.startswith(('#', 'http://', 'https://', 'mailto:')):
            continue
        clean = target.split('#', 1)[0]
        if not clean:
            continue
        resolved = (md.parent / clean).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(errors, f'{md.relative_to(ROOT)}: local link escapes repository: {target}')
            continue
        if not resolved.exists():
            fail(errors, f'{md.relative_to(ROOT)}: missing local link target: {target}')


def validate_agent(skill: Path, errors: list[str]) -> None:
    agent = skill / 'agents' / 'openai.yaml'
    if not agent.exists():
        fail(errors, f'{skill.name}: missing agents/openai.yaml')
        return
    text = agent.read_text(encoding='utf-8-sig')
    for key in ('display_name:', 'short_description:', 'default_prompt:'):
        if key not in text:
            fail(errors, f'{agent.relative_to(ROOT)}: missing {key[:-1]}')
    if f'${skill.name}' not in text:
        fail(errors, f'{agent.relative_to(ROOT)}: default prompt does not reference ${skill.name}')


def main() -> int:
    errors: list[str] = []
    skills = skill_dirs()
    names: set[str] = set()
    description_chars = 0

    if not skills:
        fail(errors, 'no skill directories found')

    for skill in skills:
        skill_md = skill / 'SKILL.md'
        meta = parse_frontmatter(skill_md, errors)
        name = meta.get('name', '')
        description = meta.get('description', '')
        if name != skill.name:
            fail(errors, f'{skill_md.relative_to(ROOT)}: name={name!r} must match directory {skill.name!r}')
        if not description:
            fail(errors, f'{skill_md.relative_to(ROOT)}: description is empty')
        description_chars += len(description)
        if len(description) > MAX_DESCRIPTION_CHARS:
            fail(errors, f'{skill_md.relative_to(ROOT)}: description is {len(description)} chars; keep it <= {MAX_DESCRIPTION_CHARS} for Codex routing budget')
        if name in names:
            fail(errors, f'duplicate skill name: {name}')
        names.add(name)
        validate_agent(skill, errors)
        validate_local_links(skill_md, errors)
        routing_eval = skill / 'evals' / 'routing.md'
        if not routing_eval.exists():
            fail(errors, f'{skill.name}: missing evals/routing.md')
        else:
            eval_text = routing_eval.read_text(encoding='utf-8-sig')
            for heading in ('## Should trigger', '## Should not trigger', '## Conflict cases'):
                if heading not in eval_text:
                    fail(errors, f'{routing_eval.relative_to(ROOT)}: missing {heading}')
            validate_local_links(routing_eval, errors)
        for ref in (skill / 'references').glob('**/*.md') if (skill / 'references').exists() else []:
            validate_local_links(ref, errors)

    if description_chars > TOTAL_DESCRIPTION_BUDGET:
        fail(errors, f'total skill description budget is {description_chars} chars; keep it <= {TOTAL_DESCRIPTION_BUDGET} so names/paths still fit Codex initial metadata budget')

    readme = ROOT / 'README.md'
    if not readme.exists():
        fail(errors, 'README.md is missing')
    else:
        readme_text = readme.read_text(encoding='utf-8-sig')
        for skill in skills:
            if f'`{skill.name}`' not in readme_text and f'({skill.name}/SKILL.md)' not in readme_text:
                fail(errors, f'README.md: skill not registered: {skill.name}')
        validate_local_links(readme, errors)

    for doc in ('SKILL_AUTHORING.md', 'CONTRIBUTING.md', 'SOURCES.md'):
        p = ROOT / doc
        if not p.exists():
            fail(errors, f'{doc} is missing')
        else:
            validate_local_links(p, errors)

    if errors:
        print(f'Validation failed with {len(errors)} error(s):')
        for e in errors:
            print(f'  - {e}')
        return 1

    print(f'Validated {len(skills)} skills successfully.')
    print(f'  description budget: {description_chars}/{TOTAL_DESCRIPTION_BUDGET} chars')
    for s in skills:
        print(f'  - {s.name}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

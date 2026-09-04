# Contributing

Changes should improve routing, engineering quality, or task coverage without turning the repository into a catalog of technologies.

## Before adding a skill

Read [`SKILL_AUTHORING.md`](SKILL_AUTHORING.md). Prefer extending an existing reference when the proposed addition is a framework, library, service, or provider rather than a new work type.

## Change checklist

1. Preserve existing skill names and routing unless a rename has a clear migration reason.
2. Keep the main `SKILL.md` workflow framework-neutral where practical.
3. Add detailed technology guidance under `references/`.
4. Add or update routing examples when activation behavior changes.
5. Record third-party sources, imported data, or adapted code in [`SOURCES.md`](SOURCES.md).
6. Run:

```bash
python scripts/validate_skills.py
```

7. Inspect the diff for accidental vendor lock-in, duplicated guidance, stale references, and unnecessary context growth.

## Review criteria

A proposed change should answer:

- What new job or failure mode becomes easier for the agent?
- Why is this a new skill instead of a reference?
- What nearby skill could be confused with it?
- What evidence will show the work is complete?
- What should the agent deliberately not do?

## Third-party material

Do not copy external skill text or code without confirming the license and preserving required notices. Prefer original summaries of engineering principles and links to authoritative documentation. Imported code or datasets must retain the applicable license and notice files.

# Version-Matched Next.js Guidance

Read when Next.js routing, Server Components, caching, metadata, request APIs, or hydration affects
the change. Do not treat current web examples as the contract for an older installed version.

1. Identify the actual app workspace, installed `next` version, router, and applicable agent rules.
2. Locate the package's `dist/docs/` through its actual installation path; monorepo hoisting means
   it may not be under the repository root. Search only the relevant topic and read that page.
3. If bundled docs are absent, use an existing project documentation copy or official guidance
   for the installed version. Do not install a codemod or upgrade Next.js to obtain documentation.

The current official guide distinguishes bundled docs from automatically managed agent rules.
Detect the files rather than hard-coding their availability by version. Do not start `next dev`
solely to generate `AGENTS.md`, or overwrite user instructions to configure this skill.

For caching, establish whether data is public/private, cache scope, key inputs, and invalidation.
Check supported APIs and project configuration before adding cache directives. For RSC work,
check serializable boundary props and keep browser state in the smallest client subtree.

The retired `vercel-labs/next-skills` entries are not the documentation source. Consult the
framework's current workflow skills only when the task specifically needs adoption/optimization.

Sources: [Next.js AI-agent guide](https://nextjs.org/docs/app/guides/ai-agents),
[retired skills notice](https://github.com/vercel-labs/next-skills).

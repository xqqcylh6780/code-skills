# Repository Query Syntax

Use this reference to translate a search brief into complementary GitHub queries. Confirm the active tool's accepted fields because connected tools may expose only a query string plus pagination or organization scope.

## Useful Qualifiers

GitHub repository search supports terms and qualifiers such as:

- `language:rust` or `language:typescript`
- `topic:agent-skills`
- `stars:>500`, `forks:>=50`, or `size:<10000`
- `pushed:>=2026-01-01` or `created:2025-01-01..2026-01-01`
- `license:mit`
- `org:openai` or `user:octocat`
- `archived:false`
- `fork:false`
- `in:name,description,readme`

Examples:

```text
"vector database" language:rust stars:>500 archived:false fork:false
topic:agent-skills language:python pushed:>=2026-01-01 archived:false
org:openai topic:agents archived:false
"workflow engine" license:mit language:typescript archived:false
```

Avoid encoding every preference as a hard filter. A license, runtime, or platform requirement may be a hard qualifier; popularity and update recency are usually better used for ranking and verification.

## GitHub CLI

GitHub CLI accepts GitHub search syntax and dedicated flags. In PowerShell, single-quote the query so operators and punctuation remain literal.

```powershell
gh search repos 'agent skills language:python stars:>100 archived:false fork:false' --limit 20 --sort stars --order desc
```

Request structured fields when the result will be ranked programmatically or compared systematically:

```powershell
gh search repos 'topic:mcp language:typescript archived:false fork:false' --limit 20 --json fullName,description,url,stargazersCount,forksCount,language,license,isArchived,isFork,updatedAt,pushedAt
```

Use only JSON fields supported by the installed `gh` version. If a field is rejected, inspect `gh search repos --help` and request the nearest available evidence instead of guessing.

## Query Portfolio

For one requirement, use a small portfolio rather than repeating the same wording:

1. capability phrase plus language or runtime;
2. established GitHub topic plus the most important hard constraint;
3. common ecosystem synonym or implementation pattern;
4. organization or known standard only when the brief makes it relevant.

Record the queries or at least summarize the search strategy when reproducibility matters. Do not broaden a connected private search into public web search if doing so would reveal private names or requirements.

# Product Context and Comparable UI Variants

Read when product facts and visual direction need reconciling, or the user requests alternatives
for a named browser surface. Ordinary implementation and small style fixes do not need this flow.

## Reuse the applicable context

Read the existing product brief, PRODUCT.md, or equivalent only where it informs the task.
Product context defines the audience, job, capabilities, constraints, terminology, and supported
claims. DESIGN.md and implemented tokens/components describe visual decisions; use
[design-md.md](design-md.md) to identify their authority and scope.

Keep a parent product's shared facts separate from child-app overrides and the current page's
purpose. A marketing page and an admin screen can serve the same product with different design
priorities. Changing one surface's appearance does not authorize changing the product's claims.

Missing document names do not establish a greenfield project. Inspect the actual UI and available
brief before deciding what to preserve. Do not start an init interview, create PRODUCT.md, or
replace DESIGN.md just to perform a local refinement. Ask only about a material gap the existing
evidence cannot resolve. Write or reconcile those documents when that work is requested; keep
inferences and unresolved decisions distinct from confirmed facts.

## Make requested alternatives comparable

Identify the exact component/route and the design question: hierarchy, density, typography,
color, or interaction treatment. Keep content, capabilities, data, and factual claims constant
unless the request explicitly includes them. Vary a deliberate design dimension, not the product.
Honor the requested count; when unspecified, use the smallest set that resolves the real choice.
Do not generate options for an already precise implementation request.

Render candidates under matching viewport, theme, content length, and interaction state. Include
the relevant narrow layout and recovery state when they could change the choice. Use controlled
local data rather than triggering purchases, invitations, or writes to establish comparability.
Source-only proposals remain unrendered proposals, with their limitations labeled.

Compare task completion, comprehension, hierarchy, accessibility, and fit with the agreed product
and visual contract. An existing font or palette can be correct even when a generic detector
dislikes it; assess the actual rendered consequence. Do not mechanically enforce stylistic bans
or treat a numeric design score as objective quality.

If the user reserves selection, present the candidates and wait before applying a winner. If the
user delegates selection and completion, recommend one and continue within that authority.
Keep each candidate's state isolated, preserve unrelated edits, and retain only the accepted
implementation in production code. Remove only temporary artifacts created by this task.

## Use the available browser path

Use existing browser tooling and the applicable [browser QA](browser-qa.md) path. Reuse a suitable
running server; any server start follows the owning task's execution rules. There is no required
Impeccable engine, launcher, hook, overlay, browser extension, or download for this reference.
Do not claim a live variant picker, injected overlay, or automated acceptance unless it actually
ran. Report how the comparison was rendered and what remains unverified.

Sources informing this original local guidance:
[Impeccable context setup](https://github.com/pbakaus/impeccable/blob/main/.agents/skills/impeccable/reference/init.md),
[variant workflow](https://github.com/pbakaus/impeccable/blob/main/.agents/skills/impeccable/reference/generate.md),
[rendered quality checks](https://github.com/pbakaus/impeccable/blob/main/.agents/skills/impeccable/reference/craft-floor.md).

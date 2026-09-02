# Repository Evaluation

Use this rubric after initial discovery. Evidence quality matters more than mathematical precision; scoring should expose tradeoffs, not create false certainty.

## Hard Exclusions

Exclude a candidate before scoring when a verified condition makes it unusable:

- missing a required capability;
- incompatible runtime, platform, protocol, or integration model;
- absent or incompatible license when licensing is a requirement;
- archived or clearly abandoned when active maintenance is required;
- known unresolved security or governance risk outside the user's tolerance.

Keep an excluded repository in the report only when explaining the exclusion helps the decision.

## Weighted Dimensions

Score each dimension from 0 to 5 and adjust weights to the brief:

| Dimension | Default weight | Evidence to inspect |
|---|---:|---|
| Requirement fit | 35% | Required features, platform, API, integration model |
| Maintenance health | 20% | Releases, relevant commits, issue response, maintainer signals |
| Maturity and reliability | 15% | Version stability, adoption evidence, tests, upgrade history |
| Documentation and ergonomics | 10% | Setup, examples, migration notes, troubleshooting |
| License and governance | 10% | Explicit license, ownership, contribution and security policies |
| Integration and security risk | 10% | Dependencies, permissions, data flow, supply-chain exposure |

Do not score unavailable evidence as if it were negative. Mark it unknown, reduce confidence, and explain what would resolve it. Do not double-count stars, forks, contributors, and downloads as four independent signs of maturity.

## Maintenance Interpretation

Consider the project's lifecycle. A small, stable library can be healthy without weekly commits, while a rapidly changing framework may need frequent releases and active issue handling. Prefer release notes, compatibility updates, maintainer responses, and current documentation over raw commit volume.

Distinguish:

- **fact**: a dated release, explicit license, archived state, supported runtime;
- **inference**: likely maintenance health or migration cost based on those facts;
- **unknown**: evidence unavailable or ambiguous.

## Comparison Format

Use a compact table for the final three to five candidates:

| Repository | Requirement fit | Maintenance evidence | License | Main risk |
|---|---|---|---|---|
| `owner/name` | What matches or fails | Dated, direct evidence | Verified identifier or unknown | Decision-relevant caveat |

Follow the table with:

- **Recommendation:** why the top choice best satisfies the brief.
- **Alternatives:** when another candidate is preferable.
- **Confidence:** high, medium, or low, with missing evidence.
- **Next validation:** the smallest proof of concept or documentation check, without performing it unless authorized.

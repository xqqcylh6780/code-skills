# CI and CD

Authoritative GitHub Actions source: https://docs.github.com/en/actions

Use the project's actual CI/CD provider. This reference describes provider-neutral principles.

## CI

CI should establish reproducible evidence for the change:

- checkout exact revision;
- restore/install dependencies using the repository's lock strategy;
- run targeted static/build/test checks;
- create named/versioned artifacts when downstream deployment depends on them;
- avoid hidden state from developer machines.

## CD

Separate “artifact passed checks” from “artifact is authorized for this environment.” Protect higher-risk environments with the approval, branch, identity, and secret controls supported by the platform.

Prefer deploying a previously built immutable artifact rather than rebuilding different bits during production deployment.

## Workflow security

Treat pull-request input, workflow output, artifacts, caches, third-party actions, and generated scripts as untrusted where appropriate. Pin or control third-party automation according to repository policy. Do not print secrets or write them into artifacts.

# Stack-Specific Upgrade Checks

Use only the section for the project's actual package management. Verify version-sensitive
flags and behavior in official docs at task time; these checks do not authorize installation.

## JavaScript / TypeScript

Identify the workspace owner, `packageManager`, runtime pin, manifest ranges, and corresponding
lockfile. Review effective peer constraints and the installed compiler/framework combination.
Keep framework-linked packages aligned where the official release requires it. Do not replace
the package manager or add a second lockfile to get a resolver to accept the target.

Inspect lifecycle scripts, generators, native builds, and registry access before resolution or
clean-install verification. Run only the requested cohort's permitted path; a fresh install and
an update are different operations with different lockfile expectations. Include affected browser
or server behavior when types/build alone cannot prove compatibility.

## Python

Identify `pyproject.toml`, requirements/constraints, lockfiles, and the manager actually used by
the project. Preserve index URLs and Python/platform support. Consider resolver markers, optional
extras, and native wheel/build requirements before changing constraints.

Do not treat an unconstrained requirements file as a reproducible environment or a successfully
resolved environment as runtime proof. Use the existing lock/compile workflow rather than adding
another manager, and keep global/user Python environments outside the requested project change.

## Java / Android

For Maven, inspect parent POMs, dependency management/BOMs, and effective transitive versions
before adding local version declarations. A version may be controlled centrally rather than by
the nearest declaration. Keep the requested Spring/framework cohort and supported JDK aligned
according to its actual release guidance.

For Gradle, inspect checked-in wrappers, version catalogs, platforms/constraints, dependency locks,
and plugins. Runtime library, build plugin, Gradle, JDK, Android Gradle Plugin, and Kotlin versions
are separate compatibility axes. Do not silently upgrade the toolchain to permit a library bump.
Use the existing lock-update mechanism and inspect why each resolved version changed.

Sources: [npm install workflows](https://docs.npmjs.com/cli/commands/npm-ci),
[pip install](https://pip.pypa.io/en/stable/cli/pip_install/),
[Maven dependency management](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html),
[Gradle locking](https://docs.gradle.org/current/userguide/dependency_locking.html).

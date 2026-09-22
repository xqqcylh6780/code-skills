# Ghidra Workflow

Read only the sections relevant to the artifact and question. This is operational guidance for an
existing trusted Ghidra installation, not authorization to install, launch, or extend it.

## Official references

- Project and capabilities: <https://github.com/NationalSecurityAgency/ghidra>
- Releases and checksums: <https://github.com/NationalSecurityAgency/ghidra/releases>
- Security advisories: <https://github.com/NationalSecurityAgency/ghidra/security/advisories>
- Getting Started and supported runtimes: <https://github.com/NationalSecurityAgency/ghidra/blob/master/GhidraDocs/GettingStarted.md>
- Headless analyzer: <https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/RuntimeScripts/support/analyzeHeadlessREADME.md>
- PyGhidra: <https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/Features/PyGhidra/src/main/py/README.md>
- Importer formats: <https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/Features/Base/src/main/help/help/topics/ImporterPlugin/importer.htm>

Use documentation matching the installed release rather than assuming the `master` branch applies.

## Safe session setup

1. Record the sample path, SHA-256, size, acquisition context, and expected format.
2. Verify the Ghidra build and release checksum when provenance matters; check advisories affecting
   that version.
3. Create a task-scoped project/log directory outside the sample directory. Use a local project;
   do not connect to Ghidra Server for sensitive or untrusted samples unless explicitly authorized.
4. Disable or omit untrusted third-party extensions and scripts. Treat pre/post scripts as code
   execution with the analyst's privileges.
5. Set explicit analysis timeouts and resource limits for large, malformed, or adversarial inputs.
6. Preserve import logs and analyzer failures. A partially analyzed program is not equivalent to a
   successfully analyzed one.

Headless mode can import or process files, run pre/post scripts, recurse over directories, constrain
CPU and per-file time, and operate read-only against existing projects. Inspect the exact installed
launcher and documentation before running it because import normally creates or updates a Ghidra
project even though the input artifact remains unchanged.

## Android APK and DEX

Treat an APK as a container with several distinct evidence surfaces:

- `AndroidManifest.xml`: components, exported surfaces, permissions, SDK assumptions, and app
  identity. Confirm decoded values with a suitable Android-aware parser when binary XML details
  matter.
- `classes*.dex`: Java/Kotlin bytecode, entry components, intents, storage, network endpoints,
  cryptographic use, reflection, and JNI boundaries.
- `lib/<abi>/*.so`: native code analyzed independently with the correct ABI and compiler model.
- resources and assets: configuration, embedded endpoints, certificates, models, scripts, or
  secondary payloads.
- signing metadata: identity and integrity context, not proof that behavior is trustworthy.

Ghidra supports APK and DEX import, but Android behavior crosses resources, manifest data, bytecode,
framework lifecycle, and native code. Do not infer the whole app from one imported DEX or one
decompiled function. Obfuscation may erase names and high-level Kotlin constructs without changing
runtime behavior.

For source-to-APK verification, first establish that the artifact belongs to the claimed build using
version, application ID, signing identity, reproducible-build evidence, or a documented build
record. Compare behavior and constants only after correspondence is credible.

## Native PE, ELF, and Mach-O

Confirm loader decisions before semantic analysis:

- CPU family, bitness, endianness, image base, relocations, sections/segments, and executable flags;
- compiler specification, calling convention, exception metadata, and stripped/debug symbols;
- imports, exports, delay/dynamic loading, TLS/initializers, and platform entry points;
- embedded resources, overlays, archives, or packed regions the loader may not analyze.

Start from bounded anchors relevant to the question: exported APIs, entry points, imported sensitive
functions, distinctive constants/strings, parser dispatch, or data references. Follow callers and
callees across thunks and indirect calls. Confirm important parameters and return values at the
instruction/calling-convention level rather than trusting variable names invented by the
decompiler.

## Headless and PyGhidra selection

Use headless Ghidra when the process should be reproducible across one or many artifacts and the
required extraction can be expressed by trusted scripts. Record the complete argument list and
script hashes. Keep project deletion or overwrite flags out of commands unless the exact disposable
target has been verified.

Use PyGhidra when Python must query Ghidra's program model, symbols, functions, references, p-code,
or decompiler APIs as part of a larger local workflow. PyGhidra bridges CPython to Ghidra through
JPype; it is not a lightweight standalone parser. Use the package bundled with the installed Ghidra
release and do not automatically install or upgrade packages during analysis.

## Evidence calibration

- **High confidence:** direct bytes/instructions/data plus validated loader context and corroborating
  cross-references or runtime contract.
- **Medium confidence:** consistent decompiler/control-flow evidence with unresolved types, indirect
  calls, or incomplete dependencies.
- **Low confidence:** string proximity, naming, signatures, similarity, or decompiler shape without
  a reachable instruction/data path.

A string, imported API, or suspicious function name proves presence, not execution. A missing search
hit proves only that the searched representation was absent from the analyzed regions. Report the
scope precisely.

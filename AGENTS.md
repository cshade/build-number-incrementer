# AGENTS.md

## Purpose

This repository provides a small CLI for incrementing native mobile build numbers in two target files:

- iOS `Info.plist` via `CFBundleVersion`
- Android `build.gradle` via `versionCode`

The implementation is Python-first. Treat the Python module and `pyproject.toml` as the authoritative sources of behavior and packaging.

## Repository Layout

- `src/increment_build_number.py`: main CLI and file update logic
- `tests/test_increment_build_number.py`: unit test covering the core increment flow
- `pyproject.toml`: Python packaging, CLI entry point, dev dependencies, pytest and ruff config
- `package.json`: npm metadata and a secondary wrapper entry
- `.pre-commit-config.yaml`: local pre-commit hooks for ruff linting and formatting
- `README.md`: end-user usage and setup documentation

## Working Assumptions

- Prefer small, direct changes. This is a compact single-purpose project.
- Preserve Python 3.8 compatibility unless the user explicitly asks to raise the floor.
- Avoid adding dependencies for behavior that can be handled with the standard library.
- Keep CLI behavior explicit rather than highly configurable unless requested.

## Source Of Truth

- Python packaging and the console script live in `pyproject.toml`.
- The executable logic lives in `src/increment_build_number.py`.
- The npm package is secondary metadata. Do not treat `package.json` as the main implementation contract.

If behavior changes, update code, tests, and documentation together. If CLI invocation or packaging changes, check whether both `pyproject.toml` and `package.json` need coordinated edits.

## Environment Setup

Use Python tooling first:

```bash
python -m pip install -e ".[dev]"
```

Primary validation commands:

```bash
pytest
ruff check .
pre-commit run --all-files
```

If a command is unavailable in the environment, state that explicitly in the handoff.

## Code Conventions

- Follow the existing straightforward procedural style unless a refactor is justified by the task.
- Keep functions focused and easy to test.
- Prefer standard-library facilities where practical; the project currently has no runtime dependencies.
- Preserve file contents as much as possible outside the targeted version fields.
- When broadening parsing behavior, add tests for every newly accepted file format or syntax variant.

## Testing Expectations

- Add or update tests for any behavior change in plist parsing, Gradle rewriting, or CLI argument handling.
- Start with unit tests in `tests/test_increment_build_number.py`.
- Use targeted fixtures and temporary files rather than relying on manual verification.
- Run `pytest` after code changes when the environment supports it.

## CLI Expectations

The current CLI takes no required positional arguments. It supports optional path overrides:

- `--plist` with default `./ios/App/App/Info.plist`
- `--gradle` with default `./android/app/build.gradle`

Keep help text and README usage accurate if argument handling changes.

## Known Project-Specific Pitfalls

- The Android rewrite only changes `versionCode`; the current `versionName` substitution is effectively a no-op. Do not assume semantic version increments are part of this tool unless you intentionally implement them.
- The Gradle updater currently matches `versionCode` with a simple regex. If you broaden support for spacing, comments, or alternate file layouts, add coverage for each supported form.
- `package.json` exposes the script directly from `src/`, but `pyproject.toml` defines the primary console entry point. Be careful when changing module names or entry points.
- The existing test coverage is minimal. If you touch parsing or rewriting logic, strengthen tests rather than relying on the single happy-path test.

## Documentation Expectations

Update `README.md` when:

- CLI usage changes
- setup steps change
- supported file formats or default paths change
- user-visible behavior changes

Keep examples runnable and aligned with the actual command name: `increment-build-number`.

## Assistant Workflow

Before editing:

- Read `README.md`, `pyproject.toml`, and the relevant source/test files.

When making changes:

- Keep edits minimal and repo-specific.
- Prefer fixing the Python implementation over adding wrapper logic.
- Update tests in the same change when behavior changes.

Before handing off:

- Run the relevant validation commands when possible.
- Summarize code changes, tests run, and any commands you could not execute.

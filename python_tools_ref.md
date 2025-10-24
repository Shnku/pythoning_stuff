
# Python Tooling Manual — CLI-first (VS Code optional)

**Purpose**.

- A practical, command-line–first reference so you can install, run, and configure Python tooling (formatters, linters, type checkers, build tools) manually without relying on editor extensions.
- Includes step-by-step commands, recommended stacks, sample config files, pre-commit and CI examples, and troubleshooting for common conflicts (e.g., Pylance/Pyright vs mypy).

**Scope**.

- Tools covered: Ruff, Black, isort, autopep8, Flake8, Pylint, mypy, Pyright (CLI), pre-commit, Poetry, pip, GitHub Actions.
- Editor LSPs (Pylance/Pyright) are discussed only for context and to help you avoid duplicate diagnostics if you do use an editor.

**Table of contents**.

1. [Quick glossary](#1-quick-glossary-cli-view)
2. [Prerequisites](#2-prerequisites)
3. [Create and use a reproducible environment](#3-create-and-use-a-reproducible-environment)
4. [Install tools](#4-install-the-tools-you-need-pick-one-per-role)
5. [Basic commands (format, lint, type-check)](#5-basic-command-usage--format-lint-type-check)
6. [Pre-commit and CI](#6-pre-commit-recommended)
7. [Config file locations & examples](#7-ci-example-github-actions)
8. [Handling duplicates & conflicts](#8-config-files--where-to-put-them-and-examples)
9. [Common fixes & tricks](#9-how-to-handle-duplicates--conflicts-practical-cli-fixes)
10. [Troubleshooting (CLI-first)](#10-common-fixes--tricks)
11. [Recommended stacks](#11-troubleshooting-steps-cli-first)
12. [Commands cheat sheet](#12-recommended-stacks-cli-first)
13. [Editor notes (optional VS Code)](#13-commands-cheat-sheet)
14. [Next steps & maintenance](#14-extra-notes-about-editors-optional-vs-code-bits)  

Appendix: [example config and CI files follow for a repository.](#appendix-example-config-and-ci-files)

---

## 1) Quick glossary (CLI view)

- LSP (Language Server Protocol)
  - What: Protocol enabling editor features (completion, go-to-definition, refactors).
  - Purpose: Editor experience; often provides diagnostics and sometimes type checking.
  - Example: Pylance (VS Code extension, built on Pyright), Pyright (standalone).

- Linter
  - What: Static analysis for stylistic issues, potential bugs, unused imports, etc.
  - Purpose: Enforce code quality and style rules before runtime.
  - Example: Ruff, Flake8, Pylint.

- Formatter
  - What: Automatically rewrites code to a consistent style.
  - Purpose: Keep code formatting uniform and reduce style debate.
  - Example: Black, autopep8, isort (for imports). Ruff can also format.

- Type checker
  - What: Static type analysis validating types (function signatures, variable types).
  - Purpose: Catch type-related errors before runtime and enforce typing discipline.
  - Example: mypy (classic), Pyright (fast, used by Pylance).

- Build / Packaging tools
  - What: Manage dependencies and create installable packages/distributions.
  - Purpose: Streamline packaging and reproducible installs.
  - Example: pip, setuptools, poetry.

Summary:

- LSP: Editor protocol (Pylance/Pyright) — completions, go-to-definition, optional type diagnostics.
- Linter: Static code checks (ruff, flake8, pylint).
- Formatter: Reformat code (black, autopep8, ruff format).
- Type checker: Static types (mypy, pyright CLI).
- Build: Manage dependencies and packaging (pip, setuptools, poetry).

---

## 2) Prerequisites

- Python 3.8+ (3.10+ recommended)
- pip (or pipx), virtualenv or python -m venv
- git (for pre-commit / CI)
- Optional: Node/NPM or pipx if you want Pyright via npm/pipx; Poetry for dependency management

---

## 3) Create and use a reproducible environment

- Create and activate a venv:

  macOS / Linux

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

  Windows (PowerShell)

  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```

- Upgrade packaging tools:

  ```bash
  python -m pip install --upgrade pip setuptools wheel
  ```

Tips:

- Use pip-tools or Poetry to maintain pinned dev dependencies.
- Use pipx for global CLI tools you want outside venv.

---

## 4) Install the tools you need (pick one per role)

Example (Ruff + Black + isort + mypy):

```bash
pip install ruff black isort mypy
```

With Poetry:

```bash
poetry init --no-interaction
poetry add --dev ruff black isort mypy
```

Pyright (CLI):

```bash
# preferred via npm or pipx
npm i -g pyright
# or
pipx install pyright
```

Decision guidance:

- Linter: Ruff (fast, can replace flake8/pylint).
- Formatter: Black is common and stable; Ruff can also format.
- Type checker: Pyright/Pylance for fast editor feedback; mypy for strict CI-oriented checks (or pick one consistently).

---

## 5) Basic command usage — format, lint, type-check

Formatters

- Black:

  ```bash
  black .
  ```

- isort:

  ```bash
  isort .
  ```

- Ruff (formatter mode):

  ```bash
  ruff format .
  ```

Linters / quick checks

- Ruff (recommended modern linter):

  ```bash
  ruff check .
  # auto-fix many violations
  ruff check --fix .
  ```

- Flake8:

  ```bash
  pip install flake8
  flake8 .
  ```

- Pylint (more opinionated, verbose):

  ```bash
  pip install pylint
  pylint your_package
  ```

Type checkers

- mypy:

  ```bash
  mypy src/ --config-file mypy.ini
  ```

- Pyright (CLI):

  ```bash
  pyright
  ```

Run each tool from CLI to inspect authoritative outputs; don't rely solely on editor diagnostics when resolving conflicts.

Go Top: [Table of Contents](#python-tooling-manual--cli-first-vs-code-optional)

---

## 6) Pre-commit (recommended)

Install and activate:

```bash
pip install pre-commit
pre-commit install
# run on all files
pre-commit run --all-files
```

Use pre-commit to enforce formatting and linting at commit time. See example .pre-commit-config.yaml in the Appendix.

---

## 7) CI example (GitHub Actions)

A CI job typically:

- checks out the repo
- sets up Python
- installs dev tools
- runs black --check, isort --check-only, ruff check, mypy

Keep CI strict to fail early on style/type issues. Example workflow is in the Appendix.

---

## 8) Config files — where to put them and examples

Preferred central place: pyproject.toml supports many tools (Black, isort, Ruff). Use mypy.ini or [tool.mypy] in pyproject for mypy config. Use pyrightconfig.json for Pyright.

Short examples (full examples in Appendix):

pyproject.toml (short)

```toml
[tool.black]
line-length = 88
target-version = ["py39"]

[tool.isort]
profile = "black"

[tool.ruff]
line-length = 88
exclude = ["build", "dist", ".venv", "__pycache__"]

[tool.mypy]
python_version = 3.9
ignore_missing_imports = true
strict = false
```

mypy.ini

```ini
[mypy]
python_version = 3.9
ignore_missing_imports = True
strict_optional = True
disallow_untyped_defs = False
```

pyrightconfig.json

```json
{
  "typeCheckingMode": "basic",
  "exclude": ["**/node_modules", "**/.venv", "dist"],
  "reportMissingImports": false
}
```

.pre-commit-config.yaml (example)

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
  - repo: https://github.com/charliermarsh/ruff
    rev: "v0.1.0"   # pin to a valid version for your setup
    hooks:
      - id: ruff
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.9.0
    hooks:
      - id: mypy
        args: [--ignore-missing-imports]
```

.ruff.toml

```toml
[tool.ruff]
line-length = 88
exclude = ["build", "dist", ".venv", "__pycache__"]
# optionally select or ignore rules
```

---

## 9) How to handle duplicates & conflicts (practical CLI fixes)

Common conflict: Pylance/Pyright and mypy both report type diagnostics in-editor.

Strategies:

- Editor-first (fast feedback): Use Pyright/Pylance in editor and disable mypy in-editor. Keep mypy in CI/local CLI as your authoritative type checker.
- CLI-first (mypy authoritative): Run mypy from CLI/CI and configure your editor to NOT show Pyright/Pylance type diagnostics (set Pyright typeCheckingMode to "off" or equivalent).
- Always run a single authoritative type-checker in CI (prefer mypy for stricter rules, or pyright if you prefer its performance and rules).

Formatting conflict: Ruff vs Black

- Option A: Let Black format; use Ruff for linting only (run `ruff check` and `black .`).
- Option B: Use Ruff format and remove Black to avoid flip-flop changes.
Short rule: assign one tool per responsibility and configure tools to avoid overlapping responsibilities.

---

## 10) Common fixes & tricks

- Reformat the repository:

  ```bash
  black .
  isort .
  ruff format .   # if using ruff formatter
  ```

- Auto-fix lint issues:

  ```bash
  ruff check --fix .
  ```

- Incremental mypy adoption:
  - Start permissive:

    ```bash
    mypy --ignore-missing-imports src/
    ```

  - Tighten mypy.ini gradually (enable disallow_untyped_defs, strict_optional later).

- Run checks only on changed files when iterating:
  - Use `git diff --name-only HEAD` or pre-commit with `--from-ref/--to-ref` hooks.

---

## 11) Troubleshooting steps (CLI-first)

- Interpreter mismatch / module not found:
  - Make sure venv is active and install your package in editable mode:

    ```bash
    pip install -e .
    ```

- Stale caches / inconsistent diagnostics:
  - mypy: remove `.mypy_cache/`
  - pyright: remove `.pyright/`
  - ruff: no persistent cache by default (unless configured)

- Compare tools on the same file to isolate differences:

  ```bash
  ruff check file.py
  mypy file.py
  pyright file.py
  ```

- If CI fails but local passes:
  - Check Python versions and pinned tool versions in CI.
  - Ensure CI installs the same dev dependencies (use requirements-dev.txt or Poetry lock).

- If Pylance in VS Code behaves oddly (needs frequent restarts):
  - Use `"python.analysis.diagnosticMode": "openFilesOnly"` to reduce background work.
  - Ensure VS Code selects the correct interpreter (bottom-right status).
  - Restart Pylance: Command Palette -> "Python: Restart Language Server" or reload window.
  - Consider using CLI checks as source of truth instead of relying on editor diagnostics.

---

## 12) Recommended stacks (CLI-first)

- Minimal & fast (recommended for many projects):
  - Ruff (lint + some formatting) + Black (if preferred formatting) + mypy in CI

- Editor-friendly:
  - Pyright/Pylance in editor for quick feedback + mypy for authoritative CI checks + Ruff/Black in pre-commit

- Strict type-safety:
  - mypy (strict) + Ruff for lint + Black for formatting

Go Top: [Table of Contents](#python-tooling-manual--cli-first-vs-code-optional)

---

## 13) Commands cheat sheet

Setup & tools

```bash
python -m venv .venv
source .venv/bin/activate
pip install ruff black isort mypy pre-commit
pre-commit install
```

Format

```bash
black .
isort .
ruff format .
```

Lint

```bash
ruff check .
flake8 .
pylint your_package
```

Type check

```bash
mypy src/
pyright
```

Build & local dev

```bash
pip install -e .
python -m build
```

---

## 14) Extra notes about editors (optional VS Code bits)

- You asked to avoid relying on extensions. Use editors for convenience, but run checks from CLI and CI as the authoritative source.
- VS Code tips (if you sometimes use it):
  - Ensure the selected interpreter matches your project's venv.
  - Avoid duplicate diagnostics by choosing one type-checker for the editor:
    - To use Pylance/Pyright as editor type-checker: keep `"python.analysis.typeCheckingMode": "basic" | "strict"` and disable mypy in-editor.
    - To use mypy as authoritative: set Pyright type checking off and run `mypy` from CLI/CI.
  - Restart Pylance when necessary (Command Palette -> "Python: Restart Language Server").

---

## 15) Next steps & maintenance

- Add pre-commit to enforce formatting and linting at commit time.
- Add CI to run checks on push/PR so issues are caught in automated runs.
- Adopt type checking incrementally: start permissive and tighten rules over time.
- Pin tool versions in requirements-dev.txt or use Poetry lock for reproducible CI.
- Run `pre-commit run --all-files` before first push after adding hooks to fix many issues automatically.

---

### Appendix: example config and CI files

Example config files (copy these into your repo and adjust versions/paths):

pyproject.toml

```toml
[tool.black]
line-length = 88
target-version = ['py39']

[tool.isort]
profile = "black"

[tool.ruff]
line-length = 88
exclude = ["build", "dist", ".venv", "__pycache__"]

[tool.mypy]
python_version = 3.9
ignore_missing_imports = true
strict = false
files = ["src"]
```

.pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3
  - repo: https://github.com/charliermarsh/ruff
    rev: "v0.1.0"  # replace with latest stable version tag
    hooks:
      - id: ruff
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.9.0  # replace with valid mypy mirror rev
    hooks:
      - id: mypy
        args: [--ignore-missing-imports]
```

mypy.ini

```ini
[mypy]
python_version = 3.9
ignore_missing_imports = True
strict_optional = True
disallow_untyped_defs = False
```

pyrightconfig.json

```json
{
  "typeCheckingMode": "basic",
  "exclude": ["**/node_modules", "**/.venv", "dist"],
  "reportMissingImports": false
}
```

.ruff.toml

```toml
[tool.ruff]
line-length = 88
exclude = ["build", "dist", ".venv", "__pycache__"]
# If you prefer ruff JUST as a linter, enable/disable rules accordingly
```

.github/workflows/ci.yml (example)

```yaml
name: ci
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ruff black isort mypy
      - name: Format check (Black)
        run: black --check .
      - name: Import sort check (isort)
        run: isort --check-only .
      - name: Lint (Ruff)
        run: ruff check .
      - name: Type check (mypy)
        run: mypy src/ --config-file mypy.ini
```

Go Top: [Table of Contents](#python-tooling-manual--cli-first-vs-code-optional)

---

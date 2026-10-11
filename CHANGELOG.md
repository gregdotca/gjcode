# Changelog

## Unreleased

### 2026-10-10

- Remove `rand_print()` from `gjcode.rand`. It only printed the result
  of `rand()`, so callers can use `print(rand(...))` instead. This
  breaks any code that calls `gjcode.rand.rand_print`; `grandom` only
  uses `rand()`, so it's unaffected.
- Format the option count in `get_headers()` with thousands separators
  (`Options: 1,000`), matching how the roll count is already shown.
- Point the project URLs in `pyproject.toml` at `gregdotca/gjcode`
  instead of `chetcuti/gjcode`, which only reached the repo through a
  GitHub redirect.
- Fix the "Bug Tracker" project URL label in `pyproject.toml`, which
  had a stray trailing quote (`"Bug Tracker'"`) that PyPI displayed as
  part of the link text.
- Update the `LICENSE` copyright line to
  `Copyright (c) 2022-2026 Greg Chetcuti <greg@chetcuti.com>`, adding
  the current year and contact email.
- Stop shipping the local scratch script as `gjcode.test`. It sat in
  `src/gjcode/`, so setuptools packaged it into the 0.0.13 wheel and
  sdist, where importing it fails (`import rand`). It now lives,
  untracked, in the repo root.
- Ignore `__pycache__` directories in `.gitignore`.
- Add `CLAUDE.md` with guidance for Claude Code: how `gjcode.rand`
  works, build and release commands, and files to leave alone.
- Add `ACR.md` with the project's [AI Code Rating](https://aicoderating.com/)
  (B0a: all package code is hand-written), and an ACR badge to the
  README, so readers can see how AI was used.
- Add this changelog.

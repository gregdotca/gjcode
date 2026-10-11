# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Source for the `gjcode` package on PyPI (https://pypi.org/project/gjcode/): Greg's personal Python code, reused across his own projects. It's a `src/`-layout setuptools package with no runtime dependencies (standard library only).

The only module so far is `gjcode.rand`. Other projects import it as `from gjcode import rand` (for example `grandom` in the gregdotca/gtools repo), so `rand.rand()` and its signature are the public API. Changing or removing public functions breaks those callers and needs a version bump that reflects it.

## How `gjcode.rand` works

`rand(options, rolls, details)` rolls `random.randint(1, options)` `rolls` times, tallies the results, and sorts them by frequency (descending):

- `details` falsy: returns the most frequent option number (an `int`).
- `details` truthy: returns a formatted string: headers (`Options` and `Rolls` with thousands separators), a blank line, then one `#<option> - <count> (<percent>%)` line per option, with ` -- WINNER!` on the first.

The helpers (`get_results`, `sort_results`, `get_sorted_results`, `get_headers`, `get_details`, `get_full_details`) each do one step of that pipeline.

## Commands

The local `venv/` only has pip and wheel; install `build`, `twine`, and `bumpver` into it before using them.

```sh
source venv/bin/activate
pip install -e .                 # editable install for local use
```

To release, bump the version first, then build and upload:

```sh
bumpver update --patch           # bump the version
rm -rf dist                      # clear old builds
python -m build                  # builds dist/*.whl and dist/*.tar.gz
twine upload dist/*              # publish to PyPI
```

- **Versioning:** `bumpver` updates the version in both `pyproject.toml` (`version` and `current_version`) and `src/gjcode/__init__.py`. It's configured with `commit = false`, `tag = false`, and `push = false`, so commits are made by hand and there are no git tags. Commits for releases have used the version as the message (e.g. `v0.0.13`).
- **Clear `dist/` before building** a new release, or `twine upload dist/*` will try to re-upload old versions.
- **Everything under `src/gjcode/` ships:** setuptools packages every module in that directory, so keep scratch and local-only files out of it.
- **PyPI metadata is per release:** changes to `pyproject.toml` metadata (description, URLs, and so on) only show on PyPI once a new version is published.

## Tests

There's no test suite: `tests/` is empty. For a quick manual check, `test.py` in the repo root is a local scratch script (not tracked, excluded via `.git/info/exclude`). Run it against the source tree:

```sh
PYTHONPATH=src python test.py
```

## Files to leave alone

`private-api-token` and `private-readme` in the repo root are local-only and excluded via `.git/info/exclude`. Never read the token, commit either file, or include them in a build.

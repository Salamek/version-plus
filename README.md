# Version+

[![Python tests](https://github.com/Salamek/version/actions/workflows/python-test.yml/badge.svg)](https://github.com/Salamek/version/actions/workflows/python-test.yml)

The `+` / `++` / `+++` release tool. Version+ keeps version strings in sync and can commit, tag, and push a release—all with one short command.

```console
$ version +       # 1.2.3 -> 1.2.4
$ version ++      # 1.2.3 -> 1.3.0
$ version +++     # 1.2.3 -> 2.0.0
```

Get started in four commands:

```console
$ uv tool install version-plus
$ version init
$ version ++ --dry
$ version ++
```

`version init` detects common project metadata and creates `.version.yml`. `--dry` previews the complete release without modifying files, creating commits or tags, or pushing anything.

## Why Version+?

Version+ is designed for projects that store their version in more than one place and want a simple, explicit local release workflow.

- Update any number of files using named regular expressions and glob patterns.
- Verify that all configured files contain the same version before releasing.
- Set an exact version or increment patch, minor, or major with `+` notation.
- Optionally update changelogs from Git commits.
- Commit, tag, and push from the same command.
- Preview everything safely with `--dry`.

It is intentionally Git-focused and configuration-driven. There is no required commit convention, plugin system, or hosted service unless you enable optional changelog generation.

| If you want... | Version+ gives you... |
| --- | --- |
| A memorable release command | `+` for patch, `++` for minor, `+++` for major |
| One version across different stacks | Regex and glob matching for any text file |
| A safe local workflow | Consistency checks, dirty-tree protection, and `--dry` |
| Git release automation | Optional commit, annotated tag, and push |

## Installation

Install Version+ as an isolated command-line tool:

```console
$ uv tool install version-plus
```

or:

```console
$ pipx install version-plus
```

The distribution is named `version-plus`; the command remains the pleasantly short `version`. The `version` distribution on PyPI belongs to an unrelated project.

To install the latest development version directly from GitHub:

```console
$ uv tool install git+https://github.com/Salamek/version.git
```

You can also install it from the project package repositories.

### Debian and derivatives

```console
$ wget -O- https://repository.salamek.cz/deb/salamek.gpg.key | sudo apt-key add -
$ echo "deb https://repository.salamek.cz/deb/pub all main" | sudo tee /etc/apt/sources.list.d/salamek.cz.list
$ sudo apt update
$ sudo apt install version
```

### Arch Linux

Add the repository to `/etc/pacman.conf`:

```ini
[salamek]
Server = https://repository.salamek.cz/arch/pub
SigLevel = Optional
```

Then install Version+:

```console
$ sudo pacman -Sy version
```

## Quick start

From the root of your project, detect common version files and create `.version.yml`:

```console
$ version init
Created /path/to/project/.version.yml
Review it, then preview your first release with `version + --dry`.
```

Version+ recognizes version fields in `pyproject.toml`, `Cargo.toml`, `package.json`, `setup.py`, and `Chart.yaml`, plus Python `__version__` assignments in conventional version modules. It will stop if the discovered files contain different versions, and it never replaces an existing configuration unless you pass `--force`.

The generated configuration commits and tags releases but leaves automatic pushing disabled. Review it before your first release:

```yaml
GIT:
  AUTO_COMMIT: true
  AUTO_TAG: true
  AUTO_PUSH: false
  COMMIT_MESSAGE: "Release {version}"

REGEXPS:
  python: '__version__\s*=\s*"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"'
  package: 'pkgver\s*=\s*(?P<version>.*)'

VERSION_FILES:
  version/__init__.py: python
  archlinux/PKGBUILD: package
```

You can also create this file manually. Only `REGEXPS` and `VERSION_FILES` are required. For backward compatibility, omitted Git actions default to enabled; generated configurations set `AUTO_PUSH` to `false` explicitly.

Check that all configured files agree:

```console
$ version
Current version is 1.2.3
```

Preview and release a minor version:

```console
$ version ++ --dry
$ version ++
```

Version+ displays the planned version and enabled Git actions before asking for confirmation.

## Commands

Show the current project version:

```console
$ version
$ version status
```

Set an exact version:

```console
$ version 2.1.0
$ version mark 2.1.0
```

Increment a version component:

| Command | Result from `1.2.3` |
| --- | --- |
| `version +` | `1.2.4` |
| `version ++` | `1.3.0` |
| `version +++` | `2.0.0` |
| `version +10` | `1.2.13` |
| `version ++2` | `1.4.0` |
| `version +++2` | `3.0.0` |

Useful options:

| Option | Purpose |
| --- | --- |
| `init` | Detect common version files and create `.version.yml` |
| `--dry` | Preview without changing files or Git state |
| `-y`, `--all_yes` | Skip the confirmation prompt |
| `-f`, `--force` | Allow a dirty worktree or a non-increasing version |
| `-p DIR`, `--project_dir=DIR` | Operate on another project directory |
| `-c FILE`, `--config_file=FILE` | Use another configuration file |

Run `version --help` for the complete CLI reference.

## Configuration reference

```yaml
GIT:
  # Add version and changelog files to a release commit.
  AUTO_COMMIT: true

  # Create an annotated tag named after the new version.
  AUTO_TAG: true

  # Push the commit and tag. Use false to disable, true for origin,
  # or a remote name such as upstream.
  AUTO_PUSH: true

  COMMIT_MESSAGE: "New version {version}"

  # Required only when CHANGE_LOGS is configured.
  COMMIT_PARSER: "version.commit_parser.Sematic:Sematic"

REGEXPS:
  python: '__version__\s*=\s*"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"'
  package: 'pkgver\s*=\s*(?P<version>.*)'

VERSION_FILES:
  version/__init__.py: python
  archlinux/PKGBUILD: package

CHANGE_LOGS:
  CHANGELOG.md:
    generator: version.change_log.Debian
    types: [fix, feat]
    arguments:
      project_name: example-project
      stability: unstable
      urgency: medium
```

Each regular expression must expose either:

- a `version` named group containing the complete version; or
- `major`, `minor`, and optional `patch`, `prerelease`, and `prerelease_num` named groups.

`VERSION_FILES` maps file paths or recursive glob patterns to regular-expression names.

## Changelog generation

Changelog generation is optional. When configured, Version+ parses Git commits between releases and passes them to the selected generator.

```console
$ version changelog info
$ version changelog generate 1.2.3 1.3.0 --dry
```

## Development

Run the tests with:

```console
$ python -m pip install . pytest
$ python -m pytest
```

Build distributable packages with:

```console
$ python -m pip install build
$ python -m build
```

## Mirrors

The project is also mirrored at <https://gitlab.com/Salamek/version>.

Version+ is licensed under GPL-3.0.

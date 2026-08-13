import os
import subprocess
import sys
from pathlib import Path

import yaml
from git import Repo

from version import __version__
from version.Version import Version


def make_options(project_dir: Path, version: str, *, dry: bool = False) -> dict:
    return {
        "--all_yes": False,
        "--config_file": None,
        "--dry": dry,
        "--force": False,
        "--project_dir": str(project_dir),
        "<version>": version,
    }


def test_version_option_prints_package_version(tmp_path: Path) -> None:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(Path(__file__).parent.parent)
    result = subprocess.run(
        [sys.executable, "-m", "version", "--version"],
        cwd=tmp_path,
        env=environment,
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout.strip() == __version__


def test_project_dir_resolves_to_selected_directory(tmp_path: Path) -> None:
    project_dir = tmp_path / "project"
    project_dir.mkdir()
    Repo.init(project_dir)
    (project_dir / ".version.yml").write_text(
        "REGEXPS:\n  python: '__version__ = \\\"(?P<version>[^\\\"]+)\\\"'\nVERSION_FILES:\n  version.py: python\n",
        encoding="utf-8",
    )
    (project_dir / "version.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")

    version = Version(make_options(project_dir, "+"))

    assert Path(version.get_project_dir()) == project_dir


def test_dry_run_is_non_interactive_and_does_not_modify_files(tmp_path: Path) -> None:
    project_dir = tmp_path / "project"
    project_dir.mkdir()
    Repo.init(project_dir)
    config = """\
GIT:
  AUTO_COMMIT: true
  AUTO_TAG: true
  AUTO_PUSH: false
REGEXPS:
  python: '__version__ = "(?P<version>[^"]+)"'
VERSION_FILES:
  version.py: python
"""
    (project_dir / ".version.yml").write_text(config, encoding="utf-8")
    version_file = project_dir / "version.py"
    original = '__version__ = "1.2.3"\n'
    version_file.write_text(original, encoding="utf-8")

    Version(make_options(project_dir, "++", dry=True)).mark()

    assert version_file.read_text(encoding="utf-8") == original
    assert not list(Repo(project_dir).tags)


def run_cli(project_dir: Path, *arguments: str) -> subprocess.CompletedProcess:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(Path(__file__).parent.parent)
    return subprocess.run(
        [sys.executable, "-m", "version", *arguments],
        cwd=project_dir,
        env=environment,
        capture_output=True,
        text=True,
    )


def test_init_detects_common_version_files(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "example"\nversion = "1.2.3"\n',
        encoding="utf-8",
    )
    package_dir = tmp_path / "example"
    package_dir.mkdir()
    (package_dir / "__init__.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")

    result = run_cli(tmp_path, "init")

    assert result.returncode == 0, result.stdout + result.stderr
    config = yaml.safe_load((tmp_path / ".version.yml").read_text(encoding="utf-8"))
    assert config["GIT"]["AUTO_COMMIT"] is True
    assert config["GIT"]["AUTO_TAG"] is True
    assert config["GIT"]["AUTO_PUSH"] is False
    assert config["VERSION_FILES"] == {
        "pyproject.toml": "toml",
        "example/__init__.py": "python",
    }


def test_init_does_not_overwrite_configuration_without_force(tmp_path: Path) -> None:
    config_path = tmp_path / ".version.yml"
    config_path.write_text("keep: me\n", encoding="utf-8")
    (tmp_path / "package.json").write_text('{"version": "1.2.3"}\n', encoding="utf-8")

    result = run_cli(tmp_path, "init")

    assert result.returncode == 1
    assert "already exists" in result.stdout
    assert config_path.read_text(encoding="utf-8") == "keep: me\n"


def test_init_refuses_different_versions(tmp_path: Path) -> None:
    (tmp_path / "package.json").write_text('{"version": "1.2.3"}\n', encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "example"\nversion = "2.0.0"\n',
        encoding="utf-8",
    )

    result = run_cli(tmp_path, "init")

    assert result.returncode == 1
    assert "different versions" in result.stdout
    assert not (tmp_path / ".version.yml").exists()


def test_status_outside_git_repository_has_friendly_error(tmp_path: Path) -> None:
    (tmp_path / ".version.yml").write_text(
        "REGEXPS:\n  python: '__version__ = \"(?P<version>[^\"]+)\"'\n"
        "VERSION_FILES:\n  sample.py: python\n",
        encoding="utf-8",
    )
    (tmp_path / "sample.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")

    result = run_cli(tmp_path, "status")

    assert result.returncode == 1
    assert "not a Git repository" in result.stdout
    assert "Traceback" not in result.stderr

"""Create a Version+ configuration from common project metadata files."""

import os
import re
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

import yaml

from version.exception import ConfigurationError


IGNORED_DIRECTORIES = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".tox",
    ".venv",
    "build",
    "dist",
    "node_modules",
    "test",
    "tests",
    "venv",
}

DETECTORS = {
    "python": {
        "filenames": {"__init__.py", "_version.py", "about.py", "version.py"},
        "suffixes": None,
        "regexp": r"__version__\s*=\s*['\"](?P<version>[^'\"]+)['\"]",
    },
    "toml": {
        "filenames": {"pyproject.toml", "Cargo.toml"},
        "suffixes": None,
        "regexp": r"^version\s*=\s*['\"](?P<version>[^'\"]+)['\"]",
    },
    "package-json": {
        "filenames": {"package.json"},
        "suffixes": None,
        "regexp": r"['\"]version['\"]\s*:\s*['\"](?P<version>[^'\"]+)['\"]",
    },
    "setup-py": {
        "filenames": {"setup.py"},
        "suffixes": None,
        "regexp": r"version\s*=\s*['\"](?P<version>[^'\"]+)['\"]",
    },
    "chart-yaml": {
        "filenames": {"Chart.yaml"},
        "suffixes": None,
        "regexp": r"^version\s*:\s*['\"]?(?P<version>[^'\"\s]+)['\"]?",
    },
}


def _candidate_files(project_dir: Path) -> Iterable[Path]:
    for root, directories, filenames in os.walk(project_dir):
        directories[:] = [
            directory for directory in directories
            if directory not in IGNORED_DIRECTORIES and not directory.endswith(".egg-info")
        ]
        root_path = Path(root)
        for filename in filenames:
            yield root_path / filename


def _detector_for(path: Path) -> Optional[Tuple[str, Dict[str, object]]]:
    # setup.py needs its more specific expression before the general Python one.
    detector_items = sorted(DETECTORS.items(), key=lambda item: item[0] == "python")
    for name, detector in detector_items:
        filenames = detector["filenames"]
        suffixes = detector["suffixes"]
        if (filenames and path.name in filenames) or (suffixes and path.suffix in suffixes):
            return name, detector
    return None


def discover_version_files(project_dir: Path) -> Tuple[Dict[str, str], Dict[str, str]]:
    """Return regexps and matching project-relative version files."""
    regexps: Dict[str, str] = {}
    version_files: Dict[str, str] = {}
    found_versions: Dict[str, str] = {}

    for path in _candidate_files(project_dir):
        detected = _detector_for(path)
        if not detected:
            continue
        name, detector = detected
        try:
            contents = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        match = re.search(str(detector["regexp"]), contents, re.MULTILINE)
        if not match:
            continue

        relative_path = path.relative_to(project_dir).as_posix()
        regexps[name] = str(detector["regexp"])
        version_files[relative_path] = name
        found_versions[relative_path] = match.group("version")

    if not version_files:
        raise ConfigurationError(
            "No version strings found. Version+ currently detects pyproject.toml, "
            "Cargo.toml, package.json, setup.py, Chart.yaml, and Python __version__ values."
        )

    version_counts = Counter(found_versions.values())
    if len(version_counts) > 1:
        details = ", ".join(
            "{}={}".format(path, version) for path, version in sorted(found_versions.items())
        )
        raise ConfigurationError(
            "Found version files with different versions ({}). Make them agree and run `version init` again.".format(
                details
            )
        )

    return regexps, version_files


def initialize_project(options: dict) -> Path:
    """Discover version files and write a conservative .version.yml."""
    project_dir = Path(options.get("--project_dir") or os.getcwd()).resolve()
    if not project_dir.is_dir():
        raise ConfigurationError("Project directory {} not found".format(project_dir))

    config_option = options.get("--config_file")
    config_path = Path(config_option).resolve() if config_option else project_dir / ".version.yml"
    if config_path.exists() and not options.get("--force"):
        raise ConfigurationError(
            "Configuration {} already exists; use --force to replace it".format(config_path)
        )

    regexps, version_files = discover_version_files(project_dir)
    config = {
        "GIT": {
            "AUTO_COMMIT": True,
            "AUTO_TAG": True,
            "AUTO_PUSH": False,
            "COMMIT_MESSAGE": "Release {version}",
        },
        "REGEXPS": regexps,
        "VERSION_FILES": version_files,
    }
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        yaml.safe_dump(config, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )
    return config_path

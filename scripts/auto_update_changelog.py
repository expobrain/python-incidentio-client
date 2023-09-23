import textwrap
from pathlib import Path

import click
import toml
from pkg_resources import parse_version
from pkg_resources.extern.packaging.version import Version  # type: ignore[import]

CHANGELOG_TEMPLATE = textwrap.dedent(
    """
    # v{version}

    - {message}
"""
).strip()


class AutoUpdateChangelogException(Exception):
    pass


class VersionKeyNotFoundError(Exception):
    pass


def get_version_number(pyproject_path: Path) -> Version:
    with pyproject_path.open() as f:
        content = toml.load(f)

    try:
        version_str = content["tool"]["poetry"]["version"]
    except KeyError:
        raise VersionKeyNotFoundError("Key `version` in `[tool.poetry]` section not found")

    version = parse_version(str(version_str))

    return version


def increase_major_version(version: Version) -> Version:
    if version.major == 0:
        major = 0
        minor = version.minor + 1
    else:
        major = 0
        minor = version.minor + 1

    version_str = f"{major}.{minor}.0"
    version = Version(version_str)

    return version


def update_changelog(changelog_path: Path, version: Version, message: str) -> None:
    changelog = CHANGELOG_TEMPLATE.format(version=version, message=message)
    changelog += "\n\n"
    changelog += changelog_path.read_text()

    changelog_path.write_text(changelog)


@click.command()
@click.option(
    "--pyproject",
    required=True,
    type=click.Path(file_okay=True, resolve_path=True),
    help="Path to the pyproject.toml file",
)
@click.option(
    "--changelog",
    required=True,
    type=click.Path(file_okay=True, resolve_path=True),
    help="Path to the CHANGELOG.md file",
)
@click.option("--message", required=True, help="Message to be added to the CHANGELOG.md")
def main(pyproject: str, changelog: str, message: str) -> None:
    """
    Updates the CHANGELOG by increasing the version number and
    adding the automaica update of the Incident.io API client.
    """
    pyproject_path = Path(pyproject)
    changelog_path = Path(changelog)

    # Get version from pyproject.toml
    version = get_version_number(pyproject_path)

    # Increase version number
    version = increase_major_version(version)

    # Update CHANGELOG.md
    update_changelog(changelog_path, version, message)


if __name__ == "__main__":
    main()

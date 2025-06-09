import dataclasses
import textwrap
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Union

import click
from ruamel.yaml import YAML

NAV_API_REFERENCE_KEY = "API Reference"
MARKDOWN_TEMPLATE = textwrap.dedent(
    """
    # {module_path}

    ::: {module_path}
    """
).strip()


@dataclasses.dataclass(frozen=True)
class Context:
    package_path: Path
    docs_path: Path
    mkdocs_path: Path


def get_markdown_file(context: Context, current_path: Path) -> Path:
    relative_path = current_path.relative_to(context.package_path.resolve())
    markdown_file = (context.docs_path / relative_path).with_suffix(".md")

    return markdown_file


def get_markdown_file_for_nav(context: Context, current_path: Path) -> str:
    relative_path = (context.docs_path / "..").resolve()
    markdown_file = get_markdown_file(context, current_path).relative_to(relative_path).as_posix()

    return markdown_file


def get_fully_qualified_module_name(context: Context, current_path: Path) -> str:
    relative_path = current_path.relative_to((context.package_path / "..").resolve())
    module_path = relative_path.with_suffix("").as_posix().replace("/", ".")

    return module_path


def generate_markdown(context: Context, current_path: Path) -> None:
    module_name = get_fully_qualified_module_name(context, current_path)
    markdown_file = get_markdown_file(context, current_path)
    content = MARKDOWN_TEMPLATE.format(module_path=module_name)

    markdown_file.parent.mkdir(parents=True, exist_ok=True)
    markdown_file.write_text(content)


def build_docs(context: Context, current_path: Path) -> None:
    for item in current_path.iterdir():
        if item.is_dir():
            build_docs(context, item)
        else:
            if item.suffix == ".py" and item.stem != "__init__":
                generate_markdown(context, item)


def is_processable_item(item: Path) -> bool:
    return (not item.stem.startswith("__")) and (item.is_dir() or item.suffix == ".py")


def sort_items_for_nav(items: Iterable[Path]) -> list[Path]:
    return sorted(items, key=lambda item: (item.parent, item.is_dir(), item.name))


def build_nav(context: Context, current_path: Path) -> Iterator[dict]:
    items = [item for item in current_path.iterdir() if is_processable_item(item)]
    items = sort_items_for_nav(items)

    for item in items:
        name = item.with_suffix("").name
        nav_item: Union[str, list[dict]]

        if item.is_dir():
            nav_item = list(build_nav(context, item))
        else:
            nav_item = get_markdown_file_for_nav(context, item)

        yield {name: nav_item}


def update_nav(context: Context, nav: list[dict]) -> None:
    yaml = YAML()
    yaml.indent(offset=2, sequence=4)

    mkdocs_config: dict = yaml.load(context.mkdocs_path)
    mkdocs_nav: list[dict] = mkdocs_config.setdefault("nav", [])
    mkdocs_api_reference = next(
        (item for item in mkdocs_nav if NAV_API_REFERENCE_KEY in item.keys()), None
    )
    if mkdocs_api_reference is None:
        mkdocs_api_reference = {NAV_API_REFERENCE_KEY: nav}
        mkdocs_nav.append(mkdocs_api_reference)
    else:
        mkdocs_api_reference[NAV_API_REFERENCE_KEY] = nav

    yaml.dump(mkdocs_config, context.mkdocs_path)


@click.command()
@click.option(
    "--package-path",
    "-p",
    required=True,
    type=click.Path(file_okay=False, dir_okay=True, readable=True, resolve_path=True),
    help="Path to the Python package",
)
@click.option(
    "--docs-path",
    "-d",
    required=True,
    type=click.Path(file_okay=False, dir_okay=True, writable=True, resolve_path=True),
    help="Path to the API docs directory",
)
@click.option(
    "--mkdocs-path",
    "-m",
    required=True,
    type=click.Path(file_okay=True, dir_okay=False, writable=True, resolve_path=True),
    help="Path to the mkdocs.yaml file",
)
def main(package_path: str, docs_path: str, mkdocs_path: str) -> None:
    context = Context(
        package_path=Path(package_path), docs_path=Path(docs_path), mkdocs_path=Path(mkdocs_path)
    )

    build_docs(context, context.package_path)
    nav = list(build_nav(context, context.package_path))

    update_nav(context, nav)


if __name__ == "__main__":
    main()

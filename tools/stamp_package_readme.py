"""Use the SDK README as package metadata without relying on upstream banners."""

import ast
from pathlib import Path


def stamp(setup_path: Path, readme_path: Path) -> None:
    source = setup_path.read_bytes()
    tree = ast.parse(source.decode("utf-8"))
    for node in tree.body:
        if not (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "setup"
        ):
            continue
        for keyword in node.value.keywords:
            if keyword.arg != "long_description":
                continue
            value = keyword.value
            if value.end_lineno is None or value.end_col_offset is None:
                raise ValueError("Generated long_description has no source location")
            lines = source.splitlines(keepends=True)
            start = sum(map(len, lines[: value.lineno - 1])) + value.col_offset
            end = sum(map(len, lines[: value.end_lineno - 1])) + value.end_col_offset
            description = repr(readme_path.read_text(encoding="utf-8")).encode("utf-8")
            result = source[:start] + description + source[end:]
            ast.parse(result.decode("utf-8"))
            setup_path.write_bytes(result)
            return
    raise ValueError("Generated setup.py has no setup(long_description=...) field")


if __name__ == "__main__":
    stamp(Path("setup.py"), Path("README.md"))

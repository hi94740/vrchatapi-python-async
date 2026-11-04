"""Validate the exact checked-in stable release without regenerating or stamping."""

import ast
import re
from pathlib import Path

from download_spec import load_pin


def assignment(path: Path, name: str) -> str:
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise ValueError(f"Missing {name} in {path}")


def check() -> str:
    version = load_pin()["version"]
    if re.fullmatch(r"\d+\.\d+\.\d+", version) is None:
        raise ValueError("Source releases require a pinned stable specification")
    if assignment(Path("setup.py"), "VERSION") != version or assignment(
        Path("vrchatapi/__init__.py"), "__version__"
    ) != version:
        raise ValueError("Source release versions must match the pinned specification")
    source = Path("vrchatapi/__init__.py").read_text(encoding="utf-8")
    if f"The version of the OpenAPI document: {version}\n" not in source:
        raise ValueError("Generated sources do not match the pinned specification")
    return version


if __name__ == "__main__":
    print(check())

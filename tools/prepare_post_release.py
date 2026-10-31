"""Stamp a new post release without fetching or regenerating the API specification."""

import re
import sys
from pathlib import Path

from stamp_version import main as stamp_version


def prepare_post_release(suffix: str) -> str:
    """Validate an increasing post number and preserve the existing base version."""
    if re.fullmatch(r"\.post[1-9][0-9]*", suffix) is None:
        raise ValueError("Post releases require a suffix such as .post6")
    versions = []
    for path, name in (
        (Path("setup.py"), "VERSION"),
        (Path("vrchatapi/__init__.py"), "__version__"),
    ):
        match = re.search(rf'^{name} = "([^\"]+)"$', path.read_text(), re.MULTILINE)
        if match is None:
            raise ValueError(f"Missing {name} in {path}")
        version = re.fullmatch(r"(\d+\.\d+\.\d+)(?:\.?post(\d+))?", match[1])
        if version is None:
            raise ValueError("Post releases require an existing stable SDK version")
        versions.append((version[1], int(version[2] or 0)))
    if versions[0] != versions[1]:
        raise ValueError("Package and import versions must match")
    base, previous_post = versions[0]
    if int(suffix.removeprefix(".post")) <= previous_post:
        raise ValueError("The new post release must be newer than the current version")
    source = Path("client/highlevel")
    shipped = Path("vrchatapi/highlevel")
    if not source.is_dir() or not shipped.is_dir():
        raise ValueError("Missing canonical or shipped high-level sources")
    for path in source.glob("*.py"):
        if path.read_bytes() != (shipped / path.name).read_bytes():
            raise ValueError(f"Shipped high-level source differs: {path.name}")
    spec = re.search(
        r"The version of the OpenAPI document: (\S+)",
        Path("vrchatapi/__init__.py").read_text(),
    )
    if spec is None or spec[1] != base:
        raise ValueError("The SDK base version must match the existing specification")
    version = base + suffix
    stamp_version(version)
    return version


if __name__ == "__main__":
    print(prepare_post_release(sys.argv[1]))

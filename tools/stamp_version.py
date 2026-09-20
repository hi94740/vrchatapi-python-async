"""Stamp a release version in generated packaging and import metadata."""

import re
import sys
from pathlib import Path


def main(version: str) -> None:
    for path, name in [
        (Path("setup.py"), "VERSION"),
        (Path("vrchatapi/__init__.py"), "__version__"),
    ]:
        text, count = re.subn(
            rf'^{name} = "[^"]*"$',
            f'{name} = "{version}"',
            path.read_text(),
            flags=re.MULTILINE,
        )
        if count != 1:
            raise ValueError(f"Expected exactly one {name} in {path}")
        path.write_text(text)


if __name__ == "__main__":
    main(sys.argv[1])

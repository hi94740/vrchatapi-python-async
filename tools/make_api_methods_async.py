#!/usr/bin/env python3
"""Make generated API modules await async ApiClient serialization methods."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


SERIALIZE_DEF = re.compile(r"^    def (_[a-z0-9_]+_serialize)\(", re.MULTILINE)
SERIALIZE_CALL = re.compile(r"(?<!await )self\._[a-z0-9_]+_serialize\(")


def process(path: Path) -> bool:
    """Add awaits to generated ApiClient serialization calls."""
    with path.open(encoding="utf-8", newline="") as file:
        text = file.read()
    original = text
    text = re.sub(
        r"(?<!await )self\.api_client\.param_serialize\(",
        "await self.api_client.param_serialize(",
        text,
    )
    text = SERIALIZE_DEF.sub(r"    async def \1(", text)
    text = SERIALIZE_CALL.sub(lambda match: f"await {match.group()}", text)
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if "return self.api_client.response_deserialize(" not in line:
            continue
        for end_index in range(index + 1, len(lines)):
            ending = lines[end_index].strip()
            if ending == ").data":
                lines[index] = line.replace(
                    "return self.api_client", "return (await self.api_client"
                )
                lines[end_index] = lines[end_index].replace(").data", ")).data")
                break
            if ending == ")":
                lines[index] = line.replace(
                    "return self.api_client", "return await self.api_client"
                )
                break
    text = "".join(lines)
    if text == original:
        return False
    with path.open("w", encoding="utf-8", newline="") as file:
        file.write(text)
    return True


def main() -> None:
    """Process generated API modules."""
    parser = argparse.ArgumentParser()
    parser.add_argument("api_dir", type=Path)
    args = parser.parse_args()
    for path in sorted(args.api_dir.glob("*_api.py")):
        process(path)


if __name__ == "__main__":
    main()

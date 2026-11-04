#!/usr/bin/env python3
"""Download the pinned public specification and verify it before generation."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen


LOCK_FILE = Path(__file__).resolve().parents[1] / "specification.json"


def load_pin() -> dict[str, str]:
    return json.loads(LOCK_FILE.read_text(encoding="utf-8"))


def download(destination: Path, pin: dict[str, str]) -> None:
    url = (
        "https://github.com/vrchatapi/specification/releases/download/"
        f"{pin['tag']}/{pin['bundle']}"
    )
    with urlopen(url, timeout=60) as response:
        data = response.read()
    if hashlib.sha256(data).hexdigest() != pin["sha256"]:
        raise ValueError("Downloaded specification does not match its pinned SHA256")
    destination.write_bytes(data)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", type=Path, nargs="?")
    parser.add_argument("--version", action="store_true")
    args = parser.parse_args()
    pin = load_pin()
    if args.version:
        print(pin["version"])
        return
    download(args.destination or Path(pin["bundle"]), pin)


if __name__ == "__main__":
    main()

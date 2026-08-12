#!/usr/bin/env python3
"""Make every generated pydantic model field optional (default None).

The OpenAPI spec frequently marks fields as required that the live VRChat API
returns as null (e.g. CurrentUser.currentAvatar for fresh accounts). The
python-legacy SDK never enforced required fields, so responses with nulls
always deserialized. The new pydantic-based generator rejects such payloads.

This post-processing step rewrites the generated model files so every declared
field is ``Optional[...]`` with a ``default=None``, exactly matching the legacy
"all fields default to None" behavior.

Run by generate.sh after code generation; safe to re-run.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

FIELD_RE = re.compile(r"^(?P<indent> {4})(?P<name>[a-z_][a-z0-9_]*): (?P<rest>.*)$")
SKIP_PREFIXES = ("ClassVar", "Optional[Self")
SKIP_NAMES = ("__", "model_config", "openapi_types", "attribute_map")


def _rewrite(name: str, rest: str) -> str:
    if rest.startswith("Optional["):
        if " = Field(" in rest:
            head, field_args = rest.split(" = Field(", 1)
            if "default=" not in field_args:
                return f"{name}: {head} = Field(default=None, {field_args}"
            return f"{name}: {rest}"
        # ``Optional[X] = <default>`` is already a valid pydantic field with a
        # default; only bare ``Optional[X]`` needs an explicit ``= None``.
        if " = " in rest:
            return f"{name}: {rest}"
        return f"{name}: {rest} = None"

    if " = Field(" in rest:
        type_part, field_args = rest.split(" = Field(", 1)
        if "default=" not in field_args:
            return f"{name}: Optional[{type_part}] = Field(default=None, {field_args}"
        return f"{name}: Optional[{type_part}] = Field({field_args}"

    if " = " in rest:
        head, default = rest.split(" = ", 1)
        return f"{name}: Optional[{head}] = {default}"
    return f"{name}: Optional[{rest}] = None"


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "BaseModel" not in text:
        return False
    out = []
    changed = False
    for line in text.splitlines():
        m = FIELD_RE.match(line)
        if m and not m.group("name").startswith(SKIP_NAMES):
            rest = m.group("rest")
            if not rest.startswith(SKIP_PREFIXES):
                new_line = m.group("indent") + _rewrite(m.group("name"), rest)
                if new_line != line:
                    line = new_line
                    changed = True
        out.append(line)
    if changed:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("models_dir", type=Path)
    args = parser.parse_args()
    changed_files = 0
    for path in sorted(args.models_dir.glob("*.py")):
        if process(path):
            changed_files += 1
    print(f"made lenient: {changed_files} model files")


if __name__ == "__main__":
    main()

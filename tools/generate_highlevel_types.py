#!/usr/bin/env python3
"""Generate raw-response TypedDicts from a bundled OpenAPI document."""

from __future__ import annotations

import argparse
import ast
import json
import shutil
import subprocess
from collections import OrderedDict
from pathlib import Path
from typing import Any

ROOT_SCHEMAS = (
    "AccountDeletionLog",
    "Badge",
    "CurrentUser",
    "CurrentUserPresence",
    "DiscordDetails",
    "InstanceContentSettings",
    "PastDisplayName",
    "User",
    "World",
)

PRIMITIVE_TYPES = {
    "boolean": "bool",
    "integer": "int",
    "number": "float",
    "string": "str",
}


def _load_document(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        document = json.loads(text)
    except json.JSONDecodeError:
        document = None

    if document is None:
        try:
            import yaml  # type: ignore[import-not-found]
        except ImportError:
            document = _load_with_command(path, "yq")
        else:
            document = yaml.safe_load(text)

    if not isinstance(document, dict):
        raise ValueError(f"OpenAPI document must be an object: {path}")
    return document


def _load_with_command(path: Path, command: str) -> dict[str, Any]:
    if command == "yq":
        executable = shutil.which("yq")
        args = [executable, "-o=json", str(path)] if executable else None
    else:
        executable = shutil.which("ruby")
        args = (
            [
                executable,
                "-ryaml",
                "-rjson",
                "-e",
                "puts JSON.generate(YAML.safe_load_file(ARGV[0], aliases: true))",
                str(path),
            ]
            if executable
            else None
        )
    if args is None:
        if command == "yq":
            return _load_with_command(path, "ruby")
        raise RuntimeError(
            "Parsing an OpenAPI YAML document requires PyYAML, yq, or Ruby"
        )

    result = subprocess.run(args, check=True, capture_output=True, text=True)
    document = json.loads(result.stdout)
    if not isinstance(document, dict):
        raise ValueError(f"OpenAPI document must be an object: {path}")
    return document


def _pascal_case(value: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in value.split("_"))


class TypedDictGenerator:
    def __init__(self, document: dict[str, Any]) -> None:
        components = document.get("components", {})
        self.schemas: dict[str, dict[str, Any]] = components["schemas"]
        self.generated: OrderedDict[str, dict[str, Any]] = OrderedDict()

    def generate(self) -> str:
        for name in ROOT_SCHEMAS:
            if name not in self.schemas:
                raise KeyError(f"OpenAPI schema is missing: {name}")
            self._collect(name, self.schemas[name])

        lines = [
            '"""Generated raw-response types; do not edit manually."""',
            "",
            "from __future__ import annotations",
            "",
            "from typing import Any, TypedDict",
            "",
            "",
        ]
        for name, schema in self.generated.items():
            lines.extend(self._render_class(name, schema))
        lines.extend(
            [
                "__all__ = [",
                *[f'    "{name}",' for name in self.generated],
                "]",
                "",
            ]
        )
        return "\n".join(lines)

    def _collect(self, name: str, schema: dict[str, Any]) -> str:
        if name in self.generated:
            return name
        self.generated[name] = {}
        normalized = dict(schema)
        self.generated[name] = normalized
        for property_name, property_schema in normalized.get(
            "properties", {}
        ).items():
            self._type_expression(name, property_name, property_schema)
        return name

    def _render_class(self, name: str, schema: dict[str, Any]) -> list[str]:
        lines = [f"class {name}(TypedDict, total=False):"]
        properties = schema.get("properties", {})
        if not properties:
            lines.append("    pass")
        else:
            for property_name, property_schema in properties.items():
                if not property_name.isidentifier():
                    raise ValueError(
                        "Cannot render OpenAPI property as Python identifier: "
                        f"{name}.{property_name}"
                    )
                type_name = self._type_expression(
                    name, property_name, property_schema
                )
                lines.append(f"    {property_name}: {type_name}")
        lines.extend(("", ""))
        return lines

    def _type_expression(
        self,
        parent: str,
        property_name: str,
        schema: dict[str, Any],
        *,
        array_item: bool = False,
    ) -> str:
        if "$ref" in schema:
            name = self._ref_name(schema["$ref"])
            target = self.schemas[name]
            if self._is_object(target):
                type_name = self._collect(name, target)
            else:
                type_name = self._scalar_type(target)
        elif schema.get("type") == "array":
            items = schema.get("items", {})
            type_name = (
                "list["
                + self._type_expression(
                    parent, property_name, items, array_item=True
                )
                + "]"
            )
        elif self._is_object(schema):
            if schema.get("properties"):
                name = self._inline_name(parent, property_name, array_item)
                type_name = self._collect(name, schema)
            else:
                additional = schema.get("additionalProperties")
                if isinstance(additional, dict):
                    value_type = self._type_expression(
                        parent, property_name, additional
                    )
                    type_name = f"dict[str, {value_type}]"
                else:
                    type_name = "dict[str, Any]"
        else:
            type_name = self._scalar_type(schema)

        if schema.get("nullable") and "None" not in type_name:
            type_name = f"{type_name} | None"
        return type_name

    def _scalar_type(self, schema: dict[str, Any]) -> str:
        schema_type = schema.get("type")
        if not isinstance(schema_type, str):
            return "Any"
        return PRIMITIVE_TYPES.get(schema_type, "Any")

    @staticmethod
    def _is_object(schema: dict[str, Any]) -> bool:
        return schema.get("type") == "object" or "properties" in schema

    @staticmethod
    def _ref_name(ref: str) -> str:
        return ref.rsplit("/", 1)[-1]

    @staticmethod
    def _inline_name(
        parent: str, property_name: str, array_item: bool
    ) -> str:
        name = parent + _pascal_case(property_name)
        return f"{name}Inner" if array_item else name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    generated = TypedDictGenerator(_load_document(args.spec)).generate()
    ast.parse(generated)
    args.output.write_text(generated, encoding="utf-8")
    print(f"generated high-level types: {args.output}")


if __name__ == "__main__":
    main()

"""Pinned specification and high-level type generation contracts."""

import ast
import hashlib
from io import BytesIO
from pathlib import Path

import pytest

from tools import download_spec
from tools.generate_highlevel_types import ROOT_SCHEMAS, TypedDictGenerator
from tools.stamp_package_readme import stamp


def test_specification_pin():
    pin = download_spec.load_pin()
    assert pin["version"] == "1.23.0"
    assert pin["tag"] == "v" + pin["version"]
    assert pin["bundle"] == "openapi-3.0.yaml"
    assert len(pin["sha256"]) == 64
    assert len(pin["commit"]) == 40


def test_download_checks_sha256_before_writing(tmp_path, monkeypatch):
    data = b"openapi: 3.0.4\n"
    seen = []

    def fetch(url, *, timeout):
        seen.append((url, timeout))
        return BytesIO(data)

    monkeypatch.setattr(download_spec, "urlopen", fetch)
    pin = {
        "tag": "v1.23.0",
        "bundle": "openapi-3.0.yaml",
        "sha256": hashlib.sha256(data).hexdigest(),
    }
    target = tmp_path / "openapi.yaml"
    download_spec.download(target, pin)
    assert target.read_bytes() == data
    assert seen == [(
        "https://github.com/vrchatapi/specification/releases/download/"
        "v1.23.0/openapi-3.0.yaml", 60,
    )]
    target.write_bytes(b"keep existing input")
    pin["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="SHA256"):
        download_spec.download(target, pin)
    assert target.read_bytes() == b"keep existing input"


def test_referenced_map_array_and_nullable_types():
    schemas = {name: {"type": "object"} for name in ROOT_SCHEMAS}
    schemas.update({
        "CurrentUser": {
            "type": "object",
            "properties": {
                "details": {"$ref": "#/components/schemas/OpenMap"},
                "counts": {"$ref": "#/components/schemas/CountMap"},
                "names": {"$ref": "#/components/schemas/Names"},
                "note": {"$ref": "#/components/schemas/NullableString"},
            },
        },
        "OpenMap": {"type": "object", "additionalProperties": True},
        "CountMap": {"type": "object", "additionalProperties": {"type": "integer"}},
        "Names": {"type": "array", "items": {"type": "string"}},
        "NullableString": {"type": "string", "nullable": True},
    })
    result = TypedDictGenerator({"components": {"schemas": schemas}}).generate()
    ast.parse(result)
    for annotation in (
        "details: dict[str, Any]", "counts: dict[str, int]",
        "names: list[str]", "note: str | None",
    ):
        assert annotation in result
    assert "class OpenMap" not in result


def test_canonical_sources_match_shipped_copies():
    root = Path(__file__).resolve().parents[1]
    for source in (root / "client/highlevel").glob("*.py"):
        assert source.read_bytes() == (root / "vrchatapi/highlevel" / source.name).read_bytes()
    assert (root / "websocket/websocket.py").read_bytes() == (
        root / "vrchatapi/websocket.py"
    ).read_bytes()


def test_package_readme_does_not_depend_on_upstream_banner(tmp_path):
    setup = tmp_path / "setup.py"
    readme = tmp_path / "README.md"
    setup.write_text('setup(name="sdk", long_description="""Upstream text\nchanged""")\n')
    readme.write_text('SDK description with "quotes", 中文, and a newline.\n')
    stamp(setup, readme)
    call = ast.parse(setup.read_text()).body[0].value
    values = {keyword.arg: ast.literal_eval(keyword.value) for keyword in call.keywords}
    assert values == {"name": "sdk", "long_description": readme.read_text()}
    before = setup.read_bytes()
    stamp(setup, readme)
    assert setup.read_bytes() == before


def test_package_readme_refuses_unexpected_setup_shape(tmp_path):
    setup = tmp_path / "setup.py"
    readme = tmp_path / "README.md"
    setup.write_text('setup(name="sdk")\n')
    readme.write_text("SDK description")
    before = setup.read_bytes()
    with pytest.raises(ValueError, match="long_description"):
        stamp(setup, readme)
    assert setup.read_bytes() == before


@pytest.mark.parametrize("package_version", ["1.23.0", "1.21.0.post6"])
def test_source_release_checks_version_without_writing(tmp_path, package_version):
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[1]
    (tmp_path / "vrchatapi").mkdir()
    (tmp_path / "setup.py").write_text(f'VERSION = "{package_version}"\n')
    (tmp_path / "vrchatapi/__init__.py").write_text(
        '# The version of the OpenAPI document: 1.23.0\n'
        f'__version__ = "{package_version}"\n'
    )
    before = {p: p.read_bytes() for p in tmp_path.rglob("*.py")}
    result = subprocess.run(
        [sys.executable, str(root / "tools/check_source_release.py")],
        cwd=tmp_path, capture_output=True, text=True,
    )
    assert (result.returncode == 0) == (package_version == "1.23.0")
    if result.returncode == 0:
        assert result.stdout.strip() == "1.23.0"
    assert all(p.read_bytes() == data for p, data in before.items())

"""Post release stamping preserves the checked-in specification and SDK sources."""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def release_tree(tmp_path):
    root = Path(__file__).resolve().parents[1]
    (tmp_path / "tools").mkdir()
    for name in ("prepare_post_release.py", "stamp_version.py"):
        shutil.copy(root / "tools" / name, tmp_path / "tools" / name)
    (tmp_path / "vrchatapi").mkdir()
    (tmp_path / "setup.py").write_text('VERSION = "1.21.0post5"\n')
    (tmp_path / "vrchatapi/__init__.py").write_text(
        '# The version of the OpenAPI document: 1.21.0\n__version__ = "1.21.0post5"\n'
    )
    (tmp_path / "vrchatapi/models.py").write_text("SPEC_SENTINEL = 'unchanged'\n")
    for directory in ("client/highlevel", "vrchatapi/highlevel"):
        (tmp_path / directory).mkdir(parents=True)
        (tmp_path / directory / "account.py").write_text("# canonical source\n")
    return tmp_path


def test_post_release_preserves_spec(release_tree):
    result = subprocess.run(
        [sys.executable, "tools/prepare_post_release.py", ".post6"],
        cwd=release_tree,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "1.21.0.post6"
    assert (release_tree / "setup.py").read_text() == 'VERSION = "1.21.0.post6"\n'
    assert (release_tree / "vrchatapi/__init__.py").read_text() == (
        '# The version of the OpenAPI document: 1.21.0\n__version__ = "1.21.0.post6"\n'
    )
    assert (
        release_tree / "vrchatapi/models.py"
    ).read_text() == "SPEC_SENTINEL = 'unchanged'\n"


@pytest.mark.parametrize(
    "suffix", [".post5", ".post4", ".post0", "rc1", "1.22.0.post1", ".post6; echo bad"]
)
def test_invalid_post_release_leaves_sources_unchanged(release_tree, suffix):
    before = {path: path.read_bytes() for path in release_tree.rglob("*.py")}
    result = subprocess.run(
        [sys.executable, "tools/prepare_post_release.py", suffix],
        cwd=release_tree,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert all(path.read_bytes() == data for path, data in before.items())


@pytest.mark.parametrize("version", ["1.21.0.post5", "1.21.0post5"])
def test_post_release_accepts_normalized_current_version(release_tree, version):
    for path in (release_tree / "setup.py", release_tree / "vrchatapi/__init__.py"):
        path.write_text(path.read_text().replace("1.21.0post5", version))
    subprocess.run(
        [sys.executable, "tools/prepare_post_release.py", ".post6"],
        cwd=release_tree,
        check=True,
    )
    assert '"1.21.0.post6"' in (release_tree / "setup.py").read_text()


@pytest.mark.parametrize(
    "path,replacement",
    [
        ("setup.py", 'VERSION = "1.22.0post5"\n'),
        ("client/highlevel/account.py", "# uncopied source\n"),
        (
            "vrchatapi/__init__.py",
            '# The version of the OpenAPI document: 1.22.0\n__version__ = "1.21.0post5"\n',
        ),
    ],
)
def test_post_release_rejects_inconsistent_sources(release_tree, path, replacement):
    (release_tree / path).write_text(replacement)
    before = {path: path.read_bytes() for path in release_tree.rglob("*.py")}
    result = subprocess.run(
        [sys.executable, "tools/prepare_post_release.py", ".post6"],
        cwd=release_tree,
        capture_output=True,
        check=False,
    )
    assert result.returncode != 0
    assert all(path.read_bytes() == data for path, data in before.items())

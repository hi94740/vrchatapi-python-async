"""Presence and location regression tests."""

from __future__ import annotations

import pytest

from vrchatapi.highlevel.presence import (
    is_user_in_game,
    parse_vrchat_location_string,
    process_vrchat_string,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        pytest.param(None, None, id="none"),
        pytest.param("", None, id="empty"),
        pytest.param("value", "value", id="value"),
    ],
)
def test_process_vrchat_string(value: str | None, expected: str | None) -> None:
    """Test empty VRChat strings are treated as missing."""
    assert process_vrchat_string(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        pytest.param(None, (None, None), id="missing"),
        pytest.param("offline", ("offline", "offline"), id="special"),
        pytest.param(
            "wrld_test:instance", ("wrld_test", "instance"), id="world_instance"
        ),
        pytest.param("wrld_test", ("wrld_test", None), id="world"),
        pytest.param("instance", (None, "instance"), id="instance"),
    ],
)
def test_parse_vrchat_location_string(
    value: str | None, expected: tuple[str | None, str | None]
) -> None:
    """Test VRChat location parsing."""
    result = parse_vrchat_location_string(value)

    assert result == expected
    assert all(type(part) is str for part in result if part is not None)


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        pytest.param({}, None, id="missing"),
        pytest.param({"location": "offline"}, False, id="offline"),
        pytest.param({"world": "wrld_test"}, True, id="world"),
        pytest.param({"instance": "offline:offline"}, False, id="offline_instance"),
    ],
)
def test_is_user_in_game(data: dict[str, str], expected: bool | None) -> None:
    """Test whether a user is in a VRChat world."""
    assert is_user_in_game(data) is expected


@pytest.mark.parametrize(
    ("user_data", "expected"),
    [
        pytest.param({}, None, id="missing_location"),
        pytest.param({"location": "offline"}, False, id="offline"),
        pytest.param({"location": "offline:offline"}, False, id="offline_location"),
        pytest.param(
            {"location": "wrld_offline"}, True, id="world_id_contains_offline"
        ),
        pytest.param({"location": "wrld_123"}, True, id="in_world"),
        pytest.param({"location": ""}, None, id="empty_location"),
        pytest.param(
            {"presence": {"location": "wrld_123"}},
            None,
            id="presence_location_is_not_used",
        ),
    ],
)
def test_is_user_in_game_matches_original_binary_sensor(
    user_data: dict[str, object], expected: bool | None
) -> None:
    """Test that the shared presence logic matches the removed binary sensor."""
    assert is_user_in_game(user_data) is expected

"""VRChat location and presence interpretation."""

from __future__ import annotations

from enum import Enum
from typing import Any, Final


def process_vrchat_string(s: str | None = None):
    """Process a string value returned by the VRChat API. Treat empty string as None."""
    return None if s is None or len(s) <= 0 else s


def is_user_in_game(user_data: dict[str, Any]) -> bool | None:
    """Return whether a user is present in a VRChat world."""
    location = (
        process_vrchat_string(user_data.get("location"))
        or process_vrchat_string(user_data.get("world"))
        or process_vrchat_string(user_data.get("instance"))
    )
    if location is None:
        return None
    return location not in {
        VRChatSpecialLocationString.OFFLINE,
        "offline:offline",
    }


class VRChatSpecialLocationString(str, Enum):
    """VRChat special location string."""

    TRAVELING = "traveling"
    PRIVATE = "private"
    OFFLINE = "offline"


VRCHAT_SPECIAL_LOCATION_STRINGS = set(VRChatSpecialLocationString)
VRCHAT_LOCATION_STRING_DELIMITER: Final = ":"
VRCHAT_WORLD_ID_PREFIX: Final = "wrld_"


def parse_vrchat_location_string(s: str | None = None):
    """Process a VRChat location string."""
    world_id: str | None = None
    instance_id: str | None = None
    s = process_vrchat_string(s)
    if s is not None:
        for ss in VRCHAT_SPECIAL_LOCATION_STRINGS:
            if s.startswith(ss):
                world_id = ss.value
                instance_id = ss.value
                break
        if world_id is None:
            if VRCHAT_LOCATION_STRING_DELIMITER in s:
                world_id, instance_id = s.split(VRCHAT_LOCATION_STRING_DELIMITER, 1)
            elif s.startswith(VRCHAT_WORLD_ID_PREFIX):
                world_id = s
            else:
                instance_id = s
    return world_id, instance_id

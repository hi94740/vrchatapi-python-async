"""High-level dictionary types.

The schema-backed types are generated into ``_generated_types.py`` from the
bundled VRChat OpenAPI document. The cookie type is local to the client
implementation and is not part of the API schema.
"""

from __future__ import annotations

from typing import Any, TypedDict

from ._generated_types import (
    AccountDeletionLog,
    Badge,
    CurrentUser,
    CurrentUserPlatformHistoryInner,
    CurrentUserPresence,
    DiscordDetails,
    InstanceContentSettings,
    PastDisplayName,
    User,
    World,
)


class HighLevelUserData(User, total=False):
    """User data after the high-level client adds derived fields."""

    friend_of: str
    imageUrl: str
    presence: dict[str, Any]
    travelingToWorldId: str


class VRChatAuthCookie(TypedDict, total=False):
    """Portable authentication cookies; this is not an API schema."""

    auth: str
    twoFactorAuth: str


__all__ = [
    "AccountDeletionLog",
    "Badge",
    "CurrentUser",
    "CurrentUserPlatformHistoryInner",
    "CurrentUserPresence",
    "DiscordDetails",
    "HighLevelUserData",
    "InstanceContentSettings",
    "PastDisplayName",
    "User",
    "VRChatAuthCookie",
    "World",
]

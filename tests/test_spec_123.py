"""Public SDK contracts affected by the specification 1.23 upgrade."""

import json
from typing import Any, get_type_hints

import pytest

import vrchatapi
from vrchatapi.api.authentication_api import AuthenticationApi
from vrchatapi.api.users_api import UsersApi
from vrchatapi.highlevel import _generated_types, types


def test_highlevel_platform_history_keeps_legacy_export():
    assert types.CurrentUserPlatformHistoryInner is _generated_types.PlatformHistoryEntry
    hints = get_type_hints(_generated_types.CurrentUser)
    assert hints["platform_history"] == list[_generated_types.PlatformHistoryEntry]
    assert hints["appleDetails"] == dict[str, Any]


def test_generated_response_annotations():
    assert (
        get_type_hints(AuthenticationApi.get_current_user)["return"]
        is vrchatapi.CurrentUserLoginResponse
    )
    assert get_type_hints(UsersApi.get_user)["return"] is vrchatapi.UserResponse
    assert get_type_hints(UsersApi.update_user_note)["return"] is object


def test_mime_type_keeps_legacy_alias():
    assert vrchatapi.MIMEType.IMAGE_SLASH_SVG_XML is vrchatapi.MIMEType.IMAGE_SLASH_SVG_PLUS_XML
    assert vrchatapi.MIMEType.IMAGE_SLASH_SVG_XML.value == "image/svg+xml"


@pytest.mark.parametrize(
    "kwargs,expected",
    [
        ({"status": None, "status_description": "hello"}, {"statusDescription": "hello"}),
        ({"status": "active"}, {"status": "active"}),
        ({"status": None, "status_description": ""}, {"statusDescription": ""}),
    ],
)
async def test_update_user_sends_only_intended_fields(kwargs, expected):
    async with vrchatapi.ApiClient() as client:
        payload = client.sanitize_for_serialization(vrchatapi.UpdateUserRequest(**kwargs))
        assert payload == expected


def test_nullable_partial_models_and_new_enum_values():
    partial = vrchatapi.CurrentUserLoginResponse.from_dict({"currentAvatar": None})
    assert partial.id is None
    assert vrchatapi.UnityPackage.from_dict({"pluginUrl": None}).plugin_url is None
    user = vrchatapi.UserResponse.from_dict({"last_activity": "", "last_login": ""})
    assert user.last_login == ""
    assert vrchatapi.InstanceRegion("unknown").value == "unknown"
    assert vrchatapi.ProductType("avatar").value == "avatar"


@pytest.mark.parametrize("body", ["User note cleared.", [], {"results": [], "totalCount": 0}])
async def test_untyped_response_preserves_wire_shape(body):
    async with vrchatapi.ApiClient() as client:
        assert client.deserialize(json.dumps(body), "object", "application/json") == body


async def test_create_request_does_not_invent_removed_defaults():
    async with vrchatapi.ApiClient() as client:
        payload = client.sanitize_for_serialization(vrchatapi.CreateWorldRequest(name="World"))
        assert "releaseStatus" not in payload
        payload = client.sanitize_for_serialization(vrchatapi.CreateFileRequest(name="Image"))
        assert "mimeType" not in payload

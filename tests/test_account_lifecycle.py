"""Transactional membership changes without consumer-specific lifecycle state."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, Mock

import pytest
from test_highlevel import CURRENT, FRIEND

from vrchatapi.websocket import VRChatEvent

pytest_plugins = ("test_highlevel",)


async def test_remove_waits_for_consumer_and_serializes_readd(account):
    entered = asyncio.Event()
    release = asyncio.Event()
    observed = []

    async def before_remove(user_id):
        assert account.users[user_id] is old
        entered.set()
        await release.wait()
        assert account.users[user_id] is old

    account.before_user_remove = before_remove
    old = await account.async_set_user(FRIEND)
    account.on_remove = lambda user_id: observed.append(user_id not in account.users)
    removed = account.request_remove_user(FRIEND["id"])
    added = account.request_set_user({**FRIEND, "displayName": "Replacement"})
    await entered.wait()
    assert not removed.done()
    assert not added.done()
    other = await account.async_set_user({**FRIEND, "id": "usr_other"})
    assert other.id == "usr_other"
    release.set()
    await removed
    replacement = await added
    assert replacement is not old
    assert old.closed
    assert observed == [True]
    assert replacement.data["displayName"] == "Replacement"


async def test_reentrant_removal_does_not_mutate_notification_stack(account):
    account.before_user_remove = AsyncMock()
    await account.async_set_user(FRIEND)
    pending = []
    observed = []

    def changed(user, world_update):
        pending.append(account.request_remove_user(user.id))
        observed.append(account.users[user.id].data["status"])

    account.on_user = changed
    await account.async_set_user({**FRIEND, "status": "busy"})
    await asyncio.gather(*pending)
    assert observed == ["busy"]
    assert FRIEND["id"] not in account.users


@pytest.mark.skipif(not hasattr(asyncio, "eager_task_factory"), reason="Python 3.12+")
async def test_eager_factory_still_defers_membership_changes(account):
    account.before_user_remove = AsyncMock()
    loop = asyncio.get_running_loop()
    previous = loop.get_task_factory()
    loop.set_task_factory(asyncio.eager_task_factory)
    try:
        task = account.request_set_user(FRIEND)
        assert FRIEND["id"] not in account.users
        await task
        removed = account.request_remove_user(FRIEND["id"])
        assert FRIEND["id"] in account.users
        await removed
    finally:
        loop.set_task_factory(previous)


async def test_sync_methods_rejected_only_when_opted_in(account):
    original = account.set_user(FRIEND)
    callback = account.on_remove = Mock()
    account.remove_user(FRIEND["id"])
    callback.assert_called_once_with(FRIEND["id"])
    assert original.closed
    account.before_user_remove = AsyncMock()
    with pytest.raises(RuntimeError, match="request_"):
        account.set_user(FRIEND)
    with pytest.raises(RuntimeError, match="request_"):
        account.remove_user(FRIEND["id"])


async def test_cleanup_failure_is_not_committed_and_can_be_retried(account):
    account.before_user_remove = AsyncMock(side_effect=ValueError("cleanup failed"))
    user = await account.async_set_user(FRIEND)
    removed_callback = account.on_remove = Mock()
    removed = account.request_remove_user(user.id)
    replacement = account.request_set_user({**FRIEND, "displayName": "Replacement"})
    with pytest.raises(ValueError, match="cleanup failed"):
        await removed
    with pytest.raises(ValueError, match="cleanup failed"):
        await replacement
    assert account.users[user.id] is user
    assert not user.closed
    removed_callback.assert_not_called()
    with pytest.raises(RuntimeError, match="removal has not completed"):
        await account.async_set_user(FRIEND)
    account.before_user_remove = AsyncMock()
    await account.async_remove_user(user.id)
    assert user.id not in account.users
    removed_callback.assert_called_once_with(user.id)


async def test_cancelled_cleanup_is_not_committed(account):
    account.before_user_remove = AsyncMock(side_effect=asyncio.CancelledError())
    user = await account.async_set_user(FRIEND)
    with pytest.raises(asyncio.CancelledError):
        await account.async_remove_user(user.id)
    assert account.users[user.id] is user
    assert not user.closed
    account.before_user_remove = AsyncMock()
    await account.async_remove_user(user.id)
    assert user.id not in account.users


async def test_callback_cannot_await_own_queue(account):
    async def before_remove(user_id):
        await account.async_set_user(FRIEND)

    account.before_user_remove = before_remove
    user = await account.async_set_user(FRIEND)
    with pytest.raises(RuntimeError, match="own queue"):
        await account.async_remove_user(user.id)
    assert account.users[user.id] is user


async def test_close_cancels_pending_cleanup_and_queued_readd(account):
    entered = asyncio.Event()
    cancelled = asyncio.Event()

    async def before_remove(user_id):
        entered.set()
        try:
            await asyncio.Future()
        finally:
            cancelled.set()

    account.before_user_remove = before_remove
    await account.async_set_user(FRIEND)
    removed = account.request_remove_user(FRIEND["id"])
    added = account.request_set_user(FRIEND)
    await entered.wait()
    await account.close()
    assert cancelled.is_set()
    assert removed.cancelled()
    assert added.cancelled()
    assert not account._mutation_tasks
    with pytest.raises(RuntimeError, match="closed"):
        account.request_set_user(FRIEND)


async def test_world_updates_suppressed_while_removing_and_after_readd(account):
    entered = asyncio.Event()
    release = asyncio.Event()

    async def before_remove(user_id):
        entered.set()
        await release.wait()

    account.before_user_remove = before_remove
    user = await account.async_set_user(FRIEND)
    callback = account.on_user = Mock()
    removed = account.request_remove_user(user.id)
    await entered.wait()
    user._world_updated({})
    callback.assert_not_called()
    release.set()
    await removed
    await account.async_set_user(FRIEND)
    callback.reset_mock()
    user._world_updated({})
    callback.assert_not_called()


async def test_late_rest_update_cannot_modify_replacement(account):
    entered = asyncio.Event()
    release = asyncio.Event()

    async def update_user(user_id, request):
        entered.set()
        await release.wait()
        return {**FRIEND, "displayName": "Stale response"}

    account.before_user_remove = AsyncMock()
    account.update_user = update_user
    old = await account.async_set_user(FRIEND)
    update = asyncio.create_task(old.update_user({}))
    await entered.wait()
    await account.async_remove_user(old.id)
    replacement = await account.async_set_user({**FRIEND, "displayName": "New"})
    release.set()
    await update
    assert replacement.data["displayName"] == "New"


async def test_ensure_user_fetch_is_ordered_before_requested_remove(account):
    entered = asyncio.Event()
    release = asyncio.Event()

    async def get_user(user_id):
        entered.set()
        await release.wait()
        return FRIEND.copy()

    account.before_user_remove = AsyncMock()
    account.api.get_user = get_user
    ensure = asyncio.create_task(account.ensure_user(FRIEND["id"]))
    await entered.wait()
    removed = account.request_remove_user(FRIEND["id"])
    release.set()
    await ensure
    await removed
    assert FRIEND["id"] not in account.users


async def test_pipeline_delete_uses_pre_remove_hook(account):
    seen = []

    async def before_remove(user_id):
        seen.append(account.users[user_id].id)

    account.before_user_remove = before_remove
    await account.async_set_user(FRIEND)
    await account.handle_event(VRChatEvent("friend-delete", {"userId": FRIEND["id"]}))
    assert seen == [FRIEND["id"]]
    assert FRIEND["id"] not in account.users


async def test_snapshot_reconciliation_uses_pre_remove_hook(account):
    account.before_user_remove = AsyncMock()
    await account.async_set_user(FRIEND)
    account.current_user_data = {**CURRENT, "friends": []}
    await account.fetch_users()
    account.before_user_remove.assert_awaited_once_with(FRIEND["id"])
    assert set(account.users) == {CURRENT["id"]}


async def test_direct_user_mutation_cannot_bypass_transaction(account):
    account.before_user_remove = AsyncMock()
    user = await account.async_set_user(FRIEND)
    with pytest.raises(RuntimeError, match="queued account"):
        user.data = {**FRIEND, "status": "busy"}
    assert user.data["status"] == "active"


async def test_snapshot_started_before_delete_cannot_revive_user(account):
    entered = asyncio.Event()
    release = asyncio.Event()

    async def friends(offline):
        entered.set()
        await release.wait()
        return [FRIEND.copy()] if offline else []

    account.before_user_remove = AsyncMock()
    await account.async_set_user(FRIEND)
    account.current_user_data = CURRENT.copy()
    account._get_friends = friends
    snapshot = asyncio.create_task(account.fetch_users())
    await entered.wait()
    await account.async_remove_user(FRIEND["id"])
    release.set()
    await snapshot
    assert FRIEND["id"] not in account.users


async def test_snapshot_cannot_remove_new_user_added_during_fetch(account):
    entered = asyncio.Event()
    release = asyncio.Event()

    async def friends(offline):
        entered.set()
        await release.wait()
        return []

    account.before_user_remove = AsyncMock()
    account.current_user_data = {**CURRENT, "friends": []}
    account._get_friends = friends
    snapshot = asyncio.create_task(account.fetch_users())
    await entered.wait()
    user = await account.async_set_user(FRIEND)
    release.set()
    await snapshot
    assert account.users[user.id] is user

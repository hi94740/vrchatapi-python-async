"""Explicitly owned, shareable world metadata cache."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable
from datetime import datetime, timedelta, timezone

from .types import World

_LOGGER = logging.getLogger(__name__)
VRCHAT_WORLD_DATA_CACHE_TTL = timedelta(days=1)
VRCHAT_WORLD_DATA_OBJECT_PRUNE_INTERVAL_SECOND = 3600


class WorldCache:
    """Cache worlds using a caller-owned API; close after the last consumer."""

    def __init__(
        self, fetch: Callable[[str], Awaitable[World]], *, retry_delay: float = 60
    ) -> None:
        self.fetch = fetch
        self.retry_delay = retry_delay
        self.registry: dict[str, VRChatWorldData] = {}
        self.last_pruned = datetime.min.replace(tzinfo=timezone.utc)
        self.closed = False
        self._sorted_names: tuple[str, ...] | None = None

    @property
    def sorted_names(self) -> tuple[str, ...]:
        """Return unique loaded world names without fetching metadata.

        Update worlds through get() or by assigning world.data. Direct mutation
        of registry or world.data dictionaries bypasses cache invalidation.
        """
        if self._sorted_names is None:
            self._sorted_names = tuple(
                sorted(
                    {
                        name or world.id
                        for world in self.registry.values()
                        if (data := world.data) is not None
                        and (name := data.get("name")) is not None
                    }
                )
            )
        return self._sorted_names

    def get(self, world_id: str, data: World | None = None) -> VRChatWorldData:
        if self.closed:
            raise RuntimeError("World cache is closed")
        now = datetime.now(timezone.utc)
        if (
            now - self.last_pruned
        ).total_seconds() >= VRCHAT_WORLD_DATA_OBJECT_PRUNE_INTERVAL_SECOND:
            for key, world in list(self.registry.items()):
                if (
                    world.should_invalidate
                    and not world.subscribers
                    and world.task is None
                ):
                    del self.registry[key]
                    self._sorted_names = None
            self.last_pruned = now
        if (world := self.registry.get(world_id)) is None:
            world = self.registry[world_id] = VRChatWorldData(self, world_id, data)
            self._sorted_names = None
        elif data is not None:
            world.data = data
        return world

    async def close(self) -> None:
        self.closed = True
        tasks = [
            world.task for world in self.registry.values() if world.task is not None
        ]
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        self.registry.clear()
        self._sorted_names = ()


class VRChatWorldData:
    """World metadata with a shared in-flight fetch and change subscriptions."""

    def __init__(
        self, cache: WorldCache, world_id: str, data: World | None = None
    ) -> None:
        self.cache = cache
        self.id = world_id
        self.task: asyncio.Task[World] | None = None
        self.subscribers: list[Callable[[World | None], None]] = []
        self._data = data
        self.last_updated = datetime.now(timezone.utc)

    @property
    def data(self) -> World | None:
        return self._data

    @data.setter
    def data(self, value: World | None) -> None:
        old_name = self._data.get("name") if self._data is not None else None
        new_name = value.get("name") if value is not None else None
        if old_name != new_name:
            self.cache._sorted_names = None
        self._data = value
        self.last_updated = datetime.now(timezone.utc)
        for callback in list(self.subscribers):
            try:
                callback(value)
            except Exception:
                _LOGGER.exception("World subscriber failed")

    @property
    def should_invalidate(self) -> bool:
        return (
            datetime.now(timezone.utc) - self.last_updated > VRCHAT_WORLD_DATA_CACHE_TTL
        )

    async def get_data(self) -> World | None:
        if self.cache.closed:
            raise RuntimeError("World cache is closed")
        if self.data is None or self.should_invalidate:
            if self.task is None:
                self.task = asyncio.create_task(self._get_data())
            # One disappearing subscriber must not cancel another subscriber's fetch.
            await asyncio.shield(self.task)
        return self.data

    async def _get_data(self) -> World:
        try:
            if self.data is None:
                # Let the pipeline's embedded world metadata arrive first.
                await asyncio.sleep(1)
            while self.data is None or self.should_invalidate:
                try:
                    self.data = await asyncio.wait_for(
                        self.cache.fetch(self.id), self.cache.retry_delay
                    )
                except Exception:
                    _LOGGER.warning(
                        "Fetching world %s failed; retrying", self.id, exc_info=True
                    )
                    await asyncio.sleep(self.cache.retry_delay)
            return self.data
        finally:
            self.task = None

    def subscribe(self, callback: Callable[[World | None], None]) -> Callable[[], None]:
        self.subscribers.append(callback)
        return lambda: self.unsubscribe(callback)

    def unsubscribe(self, callback: Callable[[World | None], None]) -> None:
        if callback in self.subscribers:
            self.subscribers.remove(callback)

from __future__ import annotations
from typing import Any, Callable, Generic, TypeVar
from .interfaces import Channel, Emoji, Message, Snowflake
from .utils import RequestError, RequestSuccess
from .qrequester import QRequester


T = TypeVar("T")


class DiscordPromise(Generic[T]):
    def _default_catch(self, error: RequestError):
        if self._has_catch:
            raise error

    def __init__(self, requester: QRequester):
        self.requester = requester
        self.requester.failed.connect(self._default_catch)
        self._has_catch = False

    def then(self, function: Callable[[RequestSuccess[T]], Any]) -> DiscordPromise[T]:
        self.requester.finished.connect(function)
        return self

    def catch(self, function: Callable[[RequestError], Any]) -> DiscordPromise[T]:
        self.requester.failed.connect(function)
        self._has_catch = True
        return self


def get_channel(channel_id: int) -> DiscordPromise[Channel]:
    return DiscordPromise(QRequester(f"channels/{channel_id}", Channel))


def modify_channel(channel_id: int, data: dict) -> DiscordPromise[Channel]:
    """
    https://discord.com/developers/docs/resources/channel#modify-channel
    """
    return DiscordPromise(QRequester(f"channels/{channel_id}", Channel, "PATCH", data))


def delete_channel(channel_id: int) -> DiscordPromise[Channel]:
    return DiscordPromise(QRequester(f"channels/{channel_id}", Channel, "DELETE"))


def create_message(channel_id: int, data: dict) -> DiscordPromise[Message]:
    """
    https://discord.com/developers/docs/resources/channel#create-message
    """

    return DiscordPromise(QRequester(
        f"channels/{channel_id}/messages", Message, "POST", data))


def create_reaction(channel_id: int, message_id: int, emoji: str) -> DiscordPromise[None]:
    # raise NotImplementedError("Emoji does not do things")
    return DiscordPromise(QRequester(
        f"channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", Channel, "PUT"))

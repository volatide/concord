from typing import Any, Callable
from .interfaces import Channel, Emoji, Message, Snowflake
from .utils import RequestError
from .qrequester import QRequester


def _default_catch(error: RequestError):
    raise error


def get_channel(channel_id: int, then: Callable[[Channel], Any], catch: Callable[[RequestError], Any] = _default_catch):
    requester = QRequester(f"channels/{channel_id}", Channel)
    requester.finished.connect(then)
    requester.failed.connect(catch)


def modify_channel(channel_id: int, data: dict, then: Callable[[Channel], Any], catch: Callable[[RequestError], Any] = _default_catch):
    """
    https://discord.com/developers/docs/resources/channel#modify-channel
    """
    requester = QRequester(f"channels/{channel_id}", Channel, "PATCH", data)
    requester.finished.connect(then)
    requester.failed.connect(catch)


def delete_channel(channel_id: int, then: Callable[[Channel], Any], catch: Callable[[RequestError], Any] = _default_catch):
    requester = QRequester(f"channels/{channel_id}", Channel, "DELETE")
    requester.finished.connect(then)
    requester.failed.connect(catch)


def create_message(channel_id: int, data: dict, then: Callable[[Channel], Any], catch: Callable[[RequestError], Any] = _default_catch):
    """
    https://discord.com/developers/docs/resources/channel#create-message
    """

    requester = QRequester(
        f"channels/{channel_id}/messages", Message, "POST", data)
    requester.finished.connect(then)
    requester.failed.connect(catch)


def create_reaction(channel_id: int, message_id: int, emoji: str, then: Callable, catch: Callable[[RequestError], Any] = _default_catch):
    # raise NotImplementedError("Emoji does not do things")
    requester = QRequester(
        f"channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", Channel, "PUT")
    requester.finished.connect(then)
    requester.failed.connect(catch)

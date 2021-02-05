from __future__ import annotations
from typing import Any, Callable, Generic, TypeVar

from PySide2.QtCore import Slot
from .interfaces import Channel, Emoji, LoginResponse, Message, MfaAuthFinishedResponse, SmsAuthResponse, Snowflake
from .utils import RequestError, RequestInfo, RequestSuccess
from .qrequester import QRequester


T = TypeVar("T")


class DiscordPromise(Generic[T]):

    # TODO: Fix this, should throw error if no catch handler
    def _default_catch(self, error: RequestError, info: RequestInfo):
        print("Catch")
        if not self._has_catch:
            raise error

    def __init__(self, requester: QRequester):
        self.requester = requester
        self.requester.failed.connect(self._default_catch)
        self._has_catch = False

    def then(self, function: Callable[[T, RequestInfo], Any]) -> DiscordPromise[T]:
        self.requester.finished.connect(function)
        return self

    def catch(self, function: Callable[[RequestError, RequestInfo], Any]) -> DiscordPromise[T]:
        self.requester.failed.connect(function)
        self._has_catch = True
        return self


def get_channel(channel_id: int) -> DiscordPromise[Channel]:
    return DiscordPromise(QRequester(f"channels/{channel_id}", Channel))


def edit_channel(channel_id: int, data: dict) -> DiscordPromise[Channel]:
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


def edit_message(channel_id: int, message_id: int, data: dict) -> DiscordPromise[Message]:
    return DiscordPromise(QRequester(
        f"channels/{channel_id}/messages/{message_id}", Message, "PATCH", data))


def delete_message(channel_id: int, message_id: int) -> DiscordPromise[None]:
    return DiscordPromise(QRequester(
        f"channels/{channel_id}/messages/{message_id}", Message, "DELETE"))


def create_reaction(channel_id: int, message_id: int, emoji: str) -> DiscordPromise[None]:
    # raise NotImplementedError("Emoji does not do things")
    return DiscordPromise(QRequester(
        f"channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", Channel, "PUT"))


def create_login(email: str, password: str) -> DiscordPromise[LoginResponse]:
    return DiscordPromise(QRequester(f"auth/login", LoginResponse, "POST", {"email": email, "password": password}, skip_auth=True))


def send_login_sms(ticket: str) -> DiscordPromise[SmsAuthResponse]:
    return DiscordPromise(QRequester(f"auth/mfa/sms/send", SmsAuthResponse, "POST", {"ticket": ticket}, skip_auth=True))


def submit_login_sms(ticket: str, code: str) -> DiscordPromise[MfaAuthFinishedResponse]:
    return DiscordPromise(QRequester(f"auth/mfa/sms", MfaAuthFinishedResponse, "POST", {"ticket": ticket, "code": code}, skip_auth=True))


def submit_totp_code(ticket: str, code: str) -> DiscordPromise[MfaAuthFinishedResponse]:
    return DiscordPromise(QRequester(f"auth/mfa/totp", MfaAuthFinishedResponse, "POST", {"ticket": ticket, "code": code}, skip_auth=True))

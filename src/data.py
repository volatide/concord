

from dataclasses import dataclass
from PySide2.QtCore import QObject
from typing import List, Literal, Optional, Union
from PySide2.QtCore import Slot, Signal
import PySide2.QtCore
import typing

from paramiko import Channel

from api.interfaces import Guild, Message, User


@dataclass
class LocalVoiceState:
    mute: bool = False
    deaf: bool = False


class State(QObject):
    # Also means there are new messages
    new_channel = Signal(Optional[Channel])
    # Also means that there is a new channel
    new_guild = Signal(Optional[Guild])
    new_voice_state = Signal(LocalVoiceState)
    change_settings_open = Signal(bool)

    def __init__(self, parent: Optional[QObject]) -> None:
        super().__init__(parent=parent)
        self._channel: Optional[Channel] = None
        self._messages: List[Message] = []
        self._guild: Optional[Guild] = None
        self._voice_state = LocalVoiceState()
        self._settings_open: bool = False

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value: Optional[Channel]):
        self._channel = value
        self.new_channel.emit(value)

    @property
    def guild(self):
        return self._guild

    @guild.setter
    def guild(self, value: Guild):
        self._guild = value
        self.new_guild.emit(value)

    @property
    def settings_open(self):
        return self._settings_open

    @settings_open.setter
    def settings_open(self, value: bool):
        self._settings_open = value
        self.change_settings_open.emit(value)

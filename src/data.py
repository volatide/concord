

from dataclasses import dataclass
from PySide2.QtCore import QObject
from typing import List, Literal, Optional, Union
from PySide2.QtCore import Slot, Signal
import PySide2.QtCore
import typing

from paramiko import Channel


class Data(QObject):
    new_channel = Signal(str)
    new_guild = Signal(str)
    new_voice_state = Signal(VoiceState)

    def __init__(self, parent: Optional[QObject]) -> None:
        super().__init__(parent=parent)
        self._channel: Optional[str] = None
        self._guild: str = "@me"
        self._voice_state = VoiceState()

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value: Optional[str]):
        self._channel = value

from dataclasses import dataclass
from PySide2.QtCore import QObject
from typing import List, Optional
from PySide2.QtCore import Signal
from .api.interfaces import Channel
from .api.interfaces import Guild, Message


@dataclass
class LocalVoiceState:
    mute: bool = False
    deaf: bool = False


class State(QObject):
    new_messages = Signal(List[Message])
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
        
        self.new_channel.connect(self._handle_new_channel)
        self.new_guild.connect(self._handle_new_guild)
    
    def _handle_new_guild(self, guild: Optional[Guild]):
        self.new_channel.emit(self.channel)
    
    def _handle_new_channel(self, channel: Optional[Channel]):
        self.new_messages.emit(self._messages)

    @property
    def messages(self):
        return self._messages

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

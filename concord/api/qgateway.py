from signal import SIGINT, signal
from typing import Any, Optional, TypedDict
from PySide2 import QtWebSockets
from PySide2.QtCore import QByteArray, QCoreApplication, QObject, QUrl, QTimer, Signal
from PySide2.QtWebSockets import QWebSocket
import sys
import json
from .interfaces import GatewayPayload, Message
from .utils import TOKEN, map_types
from zlib import decompressobj

ZLIB_SUFFIX = b'\x00\x00\xff\xff'

LOGIN_PAYLOAD = {
    "op": 2,
    "d": {
        "token": TOKEN,
        "properties": {
            "$os": "linux",
            "$browser": "concord",
            "$device": "concord"
        }
    }
}


class QGateway(QObject):
    new_event = Signal(object)

    def __init__(self):
        super().__init__()
        self.socket = QWebSocket()
        self._inflator = decompressobj()
        self._buffer = bytearray()
        self._heartbeat_timer = QTimer()
        self.socket.open(
            QUrl("wss://gateway.discord.gg/?encoding=json&v=8&compress=zlib-stream"))
        self.socket.binaryMessageReceived.connect(self._handle_bin)
        self.socket.textMessageReceived.connect(self._handle_text)
        self._heartbeat_timer.timeout.connect(self._send_heartbeat)
        self._has_ack = True

    def _send_heartbeat(self):
        if not self._has_ack:
            pass
            # self.socket.close()
        self.socket.sendTextMessage(json.dumps({"op": 1, "d": 0}))

    def _handle_bin(self, raw_data: QByteArray):
        data = raw_data.data()
        self._buffer.extend(data)
        if data.endswith(ZLIB_SUFFIX):
            data = self._inflator.decompress(data)
        self._buffer.clear()
        self._handle_text(data.decode("utf-8"))

    def _handle_text(self, str_data: str):
        data: dict = json.loads(str_data)
        payload = map_types(GatewayPayload, data)

        if payload.op == 0:
            self.new_event.emit(payload.d)
        elif payload.op == 10:
            self.socket.sendTextMessage(json.dumps(LOGIN_PAYLOAD))
            interval = payload.d["heartbeat_interval"]
            print("Sending heartbeats evert", interval/1000, "seconds")
            self._heartbeat_timer.start(interval)
        elif payload.op == 1:
            pass
        elif payload.op == 11:
            print("Heartbeat received")

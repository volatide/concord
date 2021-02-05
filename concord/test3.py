from signal import SIGINT, signal
from PySide2.QtCore import QCoreApplication, QUrl, QTimer
from PySide2.QtWebSockets import QWebSocket
import sys
import json
from api.utils import TOKEN
from zlib import decompressobj

app = QCoreApplication(sys.argv)

login = {
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


socket = QWebSocket()
heartbeat_timer = QTimer()
last_beat = None

ZLIB_SUFFIX = b'\x00\x00\xff\xff'
inflator = decompressobj()
buffer = bytearray()


def send_heartbeat():
    print("Send heartbeat")
    socket.sendTextMessage(json.dumps({"op": 1, "d": last_beat}))


def print_text_message(message):
    data = json.loads(message)
    if data["op"] == 0:
        print(str(data)[0:200], "...")

    if data["op"] == 10:
        socket.sendTextMessage(json.dumps(login))
        interval = data["d"]["heartbeat_interval"]
        print("Sending heartbeats evert", interval/1000, "seconds")
        heartbeat_timer.start(interval)

    if data["op"] == 1:
        global last_beat
        last_beat = data["d"]
        print(f"Received heartbeat seq id={last_beat}")

    if data["op"] == 11:
        print(f"Recv heartbeat ACK")


def print_bin_message(data: bytes):
    buffer.extend(data)
    if len(data) < 4 or data[-4:] != ZLIB_SUFFIX:
        return
    str_data = inflator.decompress(data).decode("utf-8")
    # print(json.loads(str_data))
    print_text_message(str_data)
    buffer.clear()
    # print(data.hex())


socket.open(
    QUrl("wss://gateway.discord.gg/?encoding=json&v=8&compress=zlib-stream"))  #

socket.textMessageReceived.connect(print_text_message)
socket.binaryMessageReceived.connect(print_bin_message)
socket.connected.connect(lambda: print("Connected"))
heartbeat_timer.timeout.connect(send_heartbeat)

# while 1:
#     sleep(0.1)


def sigint_handler(*args):
    app.quit()


signal(SIGINT, sigint_handler)

sys.exit(app.exec_())

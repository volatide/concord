from typing import Union
import sys
import json
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QByteArray, QObject, QUrl, Signal, Slot
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

app = QApplication(sys.argv)

class DiscordPostRequest(QObject):
    finished = Signal(dict)

    def __init__(self, url: str, token: str, payload: dict = {}):
        super().__init__()
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self.handle_finished)
        self.request = QNetworkRequest(QUrl(url))
        self.request.setRawHeader(QByteArray("Authorization".encode("utf-8")), QByteArray(token.encode("utf-8")))
        self.manager.get(self.request)
    
    def send(self):
        pass
    
    def handle_finished(self, reply: QNetworkReply):
        jsonsak = json.loads(str(reply.readAll().data(), "utf-8"))

        self.finished.emit(jsonsak)

with open("token.txt") as file:
    token = file.read().strip()
sak = DiscordPostRequest("https://discord.com/api/v8/users/@me/guilds", token)
sak.finished.connect(print)
# sak.send()
while 1:
    app.processEvents()
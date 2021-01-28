from typing import Union
import sys
import json
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QByteArray, QObject, QUrl, Signal, Slot
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

app = QApplication(sys.argv)

# define a new slot that receives a string and has
# 'saySomeWords' as its name
@Slot(str)
def say_some_words(words):
    print(words)

class Communicate(QObject):
    # create a new signal on the fly and name it 'speak'
    speak = Signal(str)

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
        self.finished.emit(json.loads(str(reply.readAll().data(), "utf-8")))

class DiscordApi(QObject):
    auth = Signal(str)

someone = Communicate()

# connect signal and slot
someone.speak.connect(say_some_words)

# emit 'speak' signal
someone.speak.emit("Hello everybody!")

sak = DiscordPostRequest("https://discord.com/api/v8/users/@me/guilds", "mfa.mG6il8Vxgc9gf8hHveslPaI1sx93FaUuqFpREbRdWCFQRD5iowar-UGFLhCrNUycoWfk0kVR1EIHUho79c7T")
sak.finished.connect(print)
# sak.send()
while 1:
    app.processEvents()
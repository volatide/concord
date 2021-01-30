import sys
from PySide2.QtWidgets import QApplication
from api.interfaces import Channel, Emoji, Guild, Member, Role, User
from api.qrequester import QRequester

app = QApplication(sys.argv)

sak = QRequester("channels/732359989196357646", Channel)

sak.finished.connect(print)

while 1:
    app.processEvents()

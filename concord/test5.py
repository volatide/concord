
from PySide2.QtCore import QCoreApplication
from .api.qgateway import QGateway
import sys

app = QCoreApplication(sys.argv)

gateway = QGateway()

def on_message(message):
    print(str(message)[0:200], "...")

gateway.new_event.connect(on_message)

sys.exit(app.exec_())
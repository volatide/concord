from api.endpoints import get_channel
from PySide2.QtCore import QCoreApplication
import sys
from signal import signal, SIGINT

app = QCoreApplication(sys.argv)

get_channel(574383922167808003).then(print)

def sigint_handler(*args):
    app.quit()

signal(SIGINT, sigint_handler)

sys.exit(app.exec_())
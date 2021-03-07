
from PySide2.QtCore import QCoreApplication
from .api.qgateway import QGateway
import sys

app = QCoreApplication(sys.argv)

gateway = QGateway()

gateway.new_event.connect(lambda x: print(str(x)[0:200], "..."))

sys.exit(app.exec_())
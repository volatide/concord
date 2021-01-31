from api.endpoints import get_channel
from PySide2.QtCore import QCoreApplication
import sys

app = QCoreApplication(sys.argv)


def handle_response(data, info):
    print(data, info)
    app.quit()

def catch_err(error, info):
    app.quit()
    raise error

get_channel(574383922167808003).then(handle_response).catch(catch_err)

sys.exit(app.exec_())

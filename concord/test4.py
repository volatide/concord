from datetime import datetime
from .api.endpoints import create_message, delete_message, edit_message, get_channel
from PySide2.QtCore import QCoreApplication
import sys

from .api.interfaces import Message, Snowflake

app = QCoreApplication(sys.argv)

requests_left = 2


def handle_response(data, info):
    global requests_left
    requests_left -= 1
    print(data, info)
    print("="*100)
    if not requests_left:
        app.quit()


def catch_err(error, info):
    global requests_left
    requests_left -= 1
    if not requests_left:
        app.quit()
    raise error


def handle_edit(message: Message, info):
    delete_message(409073849905315847, int(message.id)).then(
        handle_response).catch(catch_err)


def handle_message(message: Message, info):
    edit_message(
        409073849905315847, int(message.id), {
            "content": "hej"}).then(handle_edit).catch(catch_err)


get_channel(574383922167808003).then(handle_response).catch(catch_err)
create_message(409073849905315847, {"content": "hejsan", "nonce": int(
    Snowflake.from_date(datetime.now()))}).then(handle_message).catch(catch_err)

sys.exit(app.exec_())

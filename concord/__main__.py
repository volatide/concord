from typing import List, cast

from concord.api.utils import has_token
from sys import argv
from PySide2.QtQuick import QQuickItem, QQuickView
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QObject, QSize, QUrl, Qt
from PySide2.QtQml import QQmlApplicationEngine, QQmlFile
from pathlib import Path

entry_path = Path(__file__).parent
token = None

def relative_qurl(relative_path: str) -> QUrl:
    return QUrl.fromLocalFile(str(entry_path.joinpath(relative_path).resolve()))

def main(argv: List[str]):
    app = QApplication(argv)
    engine = QQmlApplicationEngine()

    concord_view = QQuickView(relative_qurl("./view.qml"))
    concord_view.show()
    
    if has_token():
        print("Token! :)")
    else:
        print("No token :(")
        page = cast(QDialog, concord_view.rootObject().findChild(QObject, "loginDialog"))
        page.open()
        # fileDialog = cast(QDialog, concord_view.findChild(QDialog, "loginDialog"))
        # fileDialog.open()

        
    # engine = QQmlApplicationEngine()
    # engine.load()
    # login.setModality(Qt.WindowModality.ApplicationModal)
    # window.setMinimumSize(QSize(400, 250))
    # print(view.children())
    # print(view.rootObject().findChild(QQmlComponent, "test"))
    return app.exec_()





if __name__ == "__main__":
    exit(main(argv))

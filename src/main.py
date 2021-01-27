from sys import argv
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, QSize, QUrl, Qt
from PySide2.QtQml import QQmlApplicationEngine, QQmlComponent
from pathlib import Path

entry_path = Path(__file__).parent
token = None


def main(argv):
    app = QApplication(argv)
    view = QQuickView(QUrl.fromLocalFile(
        str(entry_path.joinpath("./view.qml").resolve())))
    
    # engine = QQmlApplicationEngine()
    # engine.load()
    # login.setModality(Qt.WindowModality.ApplicationModal)
    # window.setMinimumSize(QSize(400, 250))
    print(view.children())
    print(view.rootObject().findChild(QQmlComponent, "test"))
    view.show()

    return app.exec_()


if __name__ == "__main__":
    exit(main(argv))

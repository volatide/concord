from sys import argv
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QUrl
from pathlib import Path

entry_path = Path(__file__).parent


def main(argv):
    app = QApplication(argv)
    login = QQuickView(QUrl.fromLocalFile(
        entry_path.joinpath("./login.qml").as_posix()))
    login.show()

    return app.exec_()


if __name__ == "__main__":
    exit(main(argv))

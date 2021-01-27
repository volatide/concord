from sys import argv
from PySide2.QtQuick import QQuickView
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QSize, QUrl, Qt
from pathlib import Path

entry_path = Path(__file__).parent


def main(argv):
    app = QApplication(argv)
    view = QQuickView(QUrl.fromLocalFile(
        entry_path.joinpath("./view.qml").as_posix()))
    
    # login.setModality(Qt.WindowModality.ApplicationModal)
    # window.setMinimumSize(QSize(400, 250))
    view.show()

    return app.exec_()


if __name__ == "__main__":
    exit(main(argv))

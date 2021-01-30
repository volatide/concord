from typing import Any, Callable, Dict, TypeVar
from PySide2.QtCore import QByteArray, QUrl, QObject, Signal, Slot
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from .endpoints import APIRequest, Method
from .utils import map_types
import json


class QRequester(QObject):
    # Is fired when the reply finishes and returns json data
    finished = Signal(object)

    def __init__(self, url, meta: Callable, method: Method = "GET", data: dict = {}) -> None:
        super().__init__()
        self.meta = meta
        self.request = APIRequest(url, method, data)
        self.manager = QNetworkAccessManager()
        request = QNetworkRequest(QUrl(self.request.url))
        request.setHeader(
            QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
        args = [request, QByteArray(self.request.method.encode("utf-8"))]

        for key, value in self.request.headers.items():
            request.setRawHeader(QByteArray(key.encode(
                "utf-8")), QByteArray(value.encode("utf-8")))

        if self.request.method not in ["GET"]:
            args.append(QByteArray(json.dumps(
                self.request.data).encode("utf-8")))

        self.manager.finished.connect(self._handle_request)
        self.manager.sendCustomRequest(*args)

    @Slot(QNetworkReply)
    def _handle_request(self, reply: QNetworkReply):
        data: dict = json.loads(str(reply.readAll().data(), "utf-8"))
        self.finished.emit(map_types(self.meta, data))

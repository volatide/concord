from typing import Any, Callable, Dict, TypeVar
from PySide2.QtCore import QByteArray, QUrl, QObject, SIGNAL, Signal, Slot
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from .utils import RequestError, map_types, APIRequest, Method
import json

_manager = QNetworkAccessManager()

class QRequester(QObject):
    # Is fired when the reply finishes and returns json data
    finished = Signal(object)
    failed = Signal(RequestError)

    def __init__(self, url, meta: Callable, method: Method = "GET", data: dict = {}, *, skip_auth: bool = False) -> None:
        super().__init__()
        self.meta = meta
        self.request = APIRequest(url, method, data, skip_auth=skip_auth)
        request = QNetworkRequest(QUrl(self.request.url))
        
        args = []
        for key, value in self.request.headers.items():
            request.setRawHeader(QByteArray(key.encode(
                "utf-8")), QByteArray(value.encode("utf-8")))

        if self.request.method in ["POST", "PUT", "PATCH"]:
            request.setHeader(
                QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
            args.append(QByteArray(json.dumps(
                self.request.data).encode("utf-8")))
        
        args.append(QByteArray(self.request.method.encode("utf-8")))
        args.append(request)
        
        reply = _manager.sendCustomRequest(*args[::-1])
        reply.finished.connect(lambda: self._handle_request(reply))

    @Slot(QNetworkReply)
    def _handle_request(self, reply: QNetworkReply):
        data: dict = json.loads(str(reply.readAll().data(), "ascii"))
        try:
            self.finished.emit(map_types(self.meta, data))
        except RequestError as error:
            self.failed.emit(error)

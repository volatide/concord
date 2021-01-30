from typing import Any, Dict
from PySide2.QtCore import QByteArray, QUrl, QObject, Signal, Slot
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from .endpoints import APIRequest, Method
import json

class QRequester(QObject):
    finished = Signal(dict)  # Is fired when the reply finishes and returns json data
    
    def __init__(self, url, method: Method = "GET", data: Dict[str, Any] = {}) -> None:
        super().__init__()
        self.request = APIRequest(url, method, data)
        self.manager = QNetworkAccessManager()
        request = QNetworkRequest(QUrl(self.request.url))
        request.setHeader(
            QNetworkRequest.KnownHeaders.ContentTypeHeader, "application/json")
        args = [request, QByteArray(self.request.method.encode("ascii"))]
        
        if self.request.method not in ["GET"]:
            args.append(QByteArray(json.dumps(self.request.data).encode("ascii")))

        self.manager.sendCustomRequest(*args)

    @Slot(QNetworkReply)
    def _handle_request(self, reply: QNetworkReply):
        pass
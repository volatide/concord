from collections import namedtuple
from pprint import pprint
from types import SimpleNamespace
from typing import Any, Callable, ClassVar, Dict, List, NamedTuple, NewType, Optional, Type, TypeVar, Union, cast, get_origin
import sys
import json
import typing
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QByteArray, QObject, QUrl, Signal, Slot
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from dataclasses import fields
from api.interfaces import Channel, Emoji, Guild, Member, Role, Snowflake, User
from api.utils import map_types

app = QApplication(sys.argv)


def make(type: Any, kv: dict) -> object:
    return type(**kv)


def map_using_typehints(meta: Callable, data: dict, depth=0) -> object:
    print("  "*depth, [meta, data])
    if meta in [Snowflake]:
        return meta(data)
    if type(data) != dict:
        return data
    new_obj = {}
    if not any(map(lambda x: type(x) in [dict, list, tuple], data.values())):
        # try:
        return meta(**data)
        # except TypeError:
        #     return SimpleNamespace(**data)
    hints: Dict[str, Type] = typing.get_type_hints(meta)
    for field, _type in hints.items():
        if field in data:
            if type(data[field]) in [list, tuple]:
                new_obj[field] = []
                for item in data[field]:
                    first = None
                    for curr_type in typing.get_args(_type):
                        try:
                            first = map_using_typehints(
                                curr_type, item, depth+1)
                        except TypeError:
                            continue
                    new_obj[field].append(first)

            else:
                for curr_type in typing.get_args(_type):
                    new_obj[field] = map_using_typehints(
                        _type, data[field], depth+1)
    return meta(**new_obj)



class DiscordPostRequest(QObject):
    finished = Signal(dict)

    def __init__(self, url: str, token: str, payload: dict = {}):
        super().__init__()
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self.handle_finished)
        self.request = QNetworkRequest(QUrl(url))
        self.request.setRawHeader(QByteArray("Authorization".encode(
            "utf-8")), QByteArray(token.encode("utf-8")))
        self.manager.get(self.request)

    def send(self):
        pass

    def handle_finished(self, reply: QNetworkReply):
        jsonsak = json.loads(str(reply.readAll().data(), "utf-8"))
        print(jsonsak)
        print("=====>")
        channel = map_types(Channel, jsonsak)
        print(channel)

        self.finished.emit(jsonsak)


with open("token.txt") as file:
    token = file.read().strip()
sak = DiscordPostRequest(
    "https://discord.com/api/v8/channels/732359989196357646", token)
# sak.finished.connect(print)
# sak.send()
while 1:
    app.processEvents()

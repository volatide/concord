from collections import namedtuple
from pprint import pprint
from types import SimpleNamespace
from typing import Any, Callable, Dict, NamedTuple, Type, Union, get_origin
import sys
import json
import typing
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QByteArray, QObject, QUrl, Signal, Slot
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from dataclasses import fields
from api.interfaces import Emoji, Guild, Role

app = QApplication(sys.argv)

def make(type:Any,kv:dict) -> object:
    return type(**kv)

def map_using_typehints(meta:Callable, data:dict) -> object:
    # if type(data) != dict:
    #     return data
    # hints: Dict[str, Type] = typing.get_type_hints(meta)
    # for field,_type in hints.items():
    #     if field in data:
    #         data[field] = map_using_typehints(get_origin(_type), data[field])
    # return
    if type(data) != dict:
        return data
    new_obj = {}
    if not any(map(lambda x: type(x) in [dict, list, tuple], data.values())):
        # try:
        return meta(**data)
        # except TypeError:
        #     return SimpleNamespace(**data)
    hints: Dict[str, Type] = typing.get_type_hints(meta)
    for field,_type in hints.items():
        if field in data:
            if type(data[field]) in [list, tuple]:
                new_obj[field] = []
                for item in data[field]:
                    first = None
                    for things in typing.get_args(_type):
                        try:
                            first = map_using_typehints(things, item)
                        except TypeError:
                            continue
                    new_obj[field].append(first)
                    
            else:
                new_obj[field] = map_using_typehints(_type, data[field])
    return meta(**new_obj)
                
        # if get_origin(_type) in [list, tuple]:
            


class DiscordPostRequest(QObject):
    finished = Signal(dict)

    def __init__(self, url: str, token: str, payload: dict = {}):
        super().__init__()
        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self.handle_finished)
        self.request = QNetworkRequest(QUrl(url))
        self.request.setRawHeader(QByteArray("Authorization".encode("utf-8")), QByteArray(token.encode("utf-8")))
        self.manager.get(self.request)
    
    def send(self):
        pass
    
    def handle_finished(self, reply: QNetworkReply):
        jsonsak = json.loads(str(reply.readAll().data(), "utf-8"))
        pprint(map_using_typehints(Guild, jsonsak))
        # jsonsak["roles"] = list(map(lambda r: make(Role, r), jsonsak["roles"]))
        # jsonsak["emojis"] = list(map(lambda e: make(Emoji, e), jsonsak["emojis"]))

        # sak = Guild(**jsonsak)
        # print(sak)

        self.finished.emit(jsonsak)

with open("token.txt") as file:
    token = file.read().strip()
sak = DiscordPostRequest("https://discord.com/api/v8/guilds/409073849414713356", token)
# sak.finished.connect(print)
# sak.send()
while 1:
    app.processEvents()
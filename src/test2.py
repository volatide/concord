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
from api.interfaces import Emoji, Guild, Role, Snowflake

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


def map_types(meta: Callable, data: Any) -> Any:
    """
    Takes in an object and a dictionary from a json response and parses it using typedefs from the object into that object, recursively

    Example:
    ```py
    @dataclass
    class Bar:
        value: str
        another_value: list[int]

    @dataclass
    class Example:
        foo: Bar

    map_types(Example, {
        "foo": {
            "value": "Some text", 
            another_value: [1, 2, 3, 4]
        }
    })  #=> Example(foo=Foo(value="Some text", another_value=[1, 2, 3, 4]))
    ```
    """

    # If the data is in it's base form, cast it to that (example, int, Snowflake)
    if type(data) not in [dict, list, tuple]:

        # A nullable field should not be cast to it's type (for example, str(None) #=> 'None')
        if data == None:
            return data
        return meta(data)

    # If the data is iterable (list or tuple),
    # map each item individually using list type args
    if type(data) in [list, tuple]:
        new = []
        for item in data:
            first = None
            types = typing.get_args(meta)
            if not types:
                types = [meta]

            # This is due to Optional arguments (Union[T, None])
            for _type in types:
                try:
                    first = map_types(_type, item)
                except TypeError:
                    continue
            new.append(first)
        return new

    # If the data is a dict, it should be mapped to it's meta (meta can be dict),
    # but should recurse as much as possible while there are typehints
    if type(data) == dict:
        new = {}
        hints: Dict[str, Type] = typing.get_type_hints(meta)
        for field, _type in hints.items():
            first = None
            if field not in data:
                continue
            types = typing.get_args(_type)
            if not types:
                types = [_type]

            # This is due to Optional arguments (Union[T, None])
            for __type in types:
                try:
                    first = map_types(__type, data[field])
                except TypeError:
                    continue
            new[field] = first

        # Create object from own meta with named arguments
        return meta(**new)


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
        pprint(map_types(Guild, jsonsak))
        # jsonsak["roles"] = list(map(lambda r: make(Role, r), jsonsak["roles"]))
        # jsonsak["emojis"] = list(map(lambda e: make(Emoji, e), jsonsak["emojis"]))

        # sak = Guild(**jsonsak)
        # print(sak)

        self.finished.emit(jsonsak)


with open("token.txt") as file:
    token = file.read().strip()
sak = DiscordPostRequest(
    "https://discord.com/api/v8/guilds/409073849414713356", token)
# sak.finished.connect(print)
# sak.send()
while 1:
    app.processEvents()

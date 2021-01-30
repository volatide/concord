
from typing import Any, AnyStr, Dict, Literal, Optional, Type
from .interfaces import ChannelType
from urllib.parse import urlencode
from pathlib import Path

Method = Literal[
    "GET", "POST", 
    "PATCH", "PUT", 
    "DELETE", "HEAD",
    "CONNECT", "OPTIONS",
    "TRACE"
]

API_VERSION = 8
API_ENTRY = f"https://discord.com/api/v{API_VERSION}/"

TOKEN_FILE = Path(__file__).joinpath("../token.txt").resolve()

with TOKEN_FILE.open() as file:
    TOKEN = file.read().strip()

class APIRequest:
    def __init__(self, url, method: Method = "GET", data: Dict[str, Any] = {}):
        self.url = API_ENTRY + url
        self.method = method
        self.data = data
        self.headers = {"Authorization": TOKEN}

    def data_as_query_str(self) -> str:
        return urlencode(self.data)
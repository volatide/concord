from signal import SIGINT, signal
import sys
from types import SimpleNamespace
from typing import Dict, Optional, Union
from PySide2.QtCore import QCoreApplication, QTextStream, Slot
from PySide2.QtWidgets import QApplication
from api.interfaces import Channel, Emoji, Guild, Member, Role, User
from api.qrequester import QRequester
from dataclasses import dataclass
from time import sleep

from api.utils import RequestInfo, RequestSuccess

app = QCoreApplication(sys.argv)

# sak = QRequester("channels/732359989196357646", Channel)
# sak.finished.connect(print)

@dataclass
class LoginResp:
    token: Optional[str]
    mfa: bool
    sms: bool
    ticket: Optional[str]

# @dataclass
# class Errors:


# @dataclass
# class ErrorResp:
#     code: int
#     errors: Errors
ticketid = None
# @Slot(dict)

def handle_token(resp: dict, info: RequestInfo):
    print("Token:", resp["token"])

def handle_sms(resp: dict, info: RequestInfo):
    print("Sms sent to:", resp["phone"])
    sak = QRequester("auth/mfa/sms", dict, "POST", {"ticket": ticketid, "code": input("Enter sms: ")}, skip_auth=True)
    sak.finished.connect(handle_token)


# @Slot(RequestSuccess[LoginResp])
def handle_login(resp: LoginResp, info: RequestInfo):
    print(resp)
    if resp.token:
        print(resp.token)
    elif resp.sms:
        print("Sending sms")
        sak = QRequester("auth/mfa/sms/send", dict, "POST", {"ticket": resp.ticket}, skip_auth=True)
        sak.finished.connect(handle_sms)

        sak.failed.connect(print)
        global ticketid
        ticketid = resp.ticket
    elif resp.mfa:
        sak = QRequester("auth/mfa/totp", dict, "POST", {"ticket": resp.ticket, "code": input("Enter MFA code: ")}, skip_auth=True)
        sak.finished.connect(handle_token)

        sak.failed.connect(print)
    else:
        raise ValueError("Login failed")

email = input("Enter email: ")
password = input("Enter password: ")
loginthing = QRequester("auth/login", LoginResp, "POST", {"email": email, "password": password}, skip_auth=True)
loginthing.finished.connect(handle_login)
loginthing.failed.connect(print)

# while 1:
#     sleep(0.1)

def sigint_handler(*args):
    app.quit()

signal(SIGINT, sigint_handler)

sys.exit(app.exec_())
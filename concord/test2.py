import sys
from typing import Optional
from PySide2.QtCore import QCoreApplication
from api.endpoints import create_login, send_login_sms, submit_login_sms, submit_totp_code
from api.interfaces import LoginResponse, Member, MfaAuthFinishedResponse, SmsAuthResponse
from getpass import getpass

from api.utils import save_token


app = QCoreApplication(sys.argv)

email = input("Enter email: ")
password = getpass("Enter password: ")

def catcher(*args):
    print(*args)
    app.quit()

def process_token(token: str):
    print("Token: ", token)
    save_token(token)
    print("Saved token!")
    app.quit()


def handle_token(resp: MfaAuthFinishedResponse, info):
    process_token(resp.token)


def handle_sms(ticket: Optional[str], resp: SmsAuthResponse, info):
    print("Sms sent to", resp.phone)
    code = input("Enter mfa code from sms: ")
    submit_login_sms(ticket or "", code).then(handle_token).catch(catcher)


def handle_login(resp: LoginResponse, info):
    if resp.token:
        process_token(resp.token)
    elif resp.ticket:
        if resp.sms:
            send_login_sms(resp.ticket).then(
                lambda x, y: handle_sms(resp.ticket, x, y)).catch(catcher)
        elif resp.mfa:
            code = input("Enter mfa code from totp app: ")
            submit_totp_code(resp.ticket, code).then(handle_token).catch(catcher)
    else:
        raise ValueError("No ticket for some reason")


create_login(email, password).then(handle_login).catch(catcher)

sys.exit(app.exec_())

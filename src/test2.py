import sys
from typing import Optional
from PySide2.QtCore import QCoreApplication
from api.endpoints import create_login, send_login_sms, submit_login_sms, submit_totp_code
from api.interfaces import LoginResponse, Member, MfaAuthFinishedResponse, SmsAuthResponse
from getpass import getpass


app = QCoreApplication(sys.argv)

email = input("Enter email: ")
password = getpass("Enter password: ")

def handle_token2(resp: MfaAuthFinishedResponse, info):
    print("Token:", resp.token)
    app.quit()

def handle_sms2(ticket: Optional[str], resp: SmsAuthResponse, info):
    print("Sms sent to", resp.phone)
    code = input("Enter mfa code from sms: ")
    submit_login_sms(ticket or "", code).then(handle_token2)

def handle_login2(resp: LoginResponse, info):
    if resp.token:
        print("Token:", resp.token)
        app.quit()
    elif resp.ticket:
        if resp.sms:
            send_login_sms(resp.ticket).then(lambda x,y: handle_sms2(resp.ticket, x,y))
        elif resp.mfa:
            code = input("Enter mfa code from totp app: ")
            submit_totp_code(resp.ticket, code).then(handle_token2)
    else:
        raise ValueError("No ticket for some reason")

create_login(email, password).then(handle_login2)

sys.exit(app.exec_())
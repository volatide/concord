import sys
from typing import Any
from PySide2.QtCore import QCoreApplication
from .api.endpoints import get_guild_audit_log
from .api.interfaces import AuditLog, AuditLogEvent

app = QCoreApplication(sys.argv)


def catcher(*args):
    print(*args)
    app.quit()



def print_request(resp: AuditLog, info):
    print(resp.audit_log_entries)
    quit(1)



get_guild_audit_log(409073849414713356, {"action_type": AuditLogEvent.MEMBER_DISCONNECT.value, "limit": 100}).then(print_request).catch(catcher)

sys.exit(app.exec_())

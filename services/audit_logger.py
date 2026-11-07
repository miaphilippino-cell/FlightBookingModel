from datetime import datetime
from models.audit import AuditLog # type: ignore


class AuditLogger:

    def __init__(self):
        self.logs = []


    def log_event(
        self,
        actor,
        action,
        result,
        details=None
    ):

        log = AuditLog(
            actor=actor,
            action=action,
            result=result,
            timestamp=datetime.now(),
            details=details
        )

        self.logs.append(log)

        return log


    def get_logs(self):

        return self.logs
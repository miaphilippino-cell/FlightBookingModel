class AuditLog:

    def __init__(
        self,
        actor,
        action,
        result,
        timestamp,
        details=None
    ):

        self.actor = actor
        self.action = action
        self.result = result
        self.timestamp = timestamp
        self.details = details

        # supports your OCL requirement
        self.tamper_resistant = True
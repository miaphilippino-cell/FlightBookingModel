from datetime import datetime, timedelta
import uuid


class Session:

    def __init__(self):
        self.token = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(hours=1)
        self.invalidated = False


    def is_valid(self):

        return (
            not self.invalidated
            and datetime.now() < self.expires_at
        )


    def invalidate(self):
        self.invalidated = True
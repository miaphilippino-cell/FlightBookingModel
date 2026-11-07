from datetime import datetime


class UserAccount:

    def __init__(
        self,
        username,
        password_hash,
        role="PASSENGER"
    ):

        self.username = username
        self.password_hash = password_hash
        self.role = role

        self.failed_login_attempts = 0
        self.account_status = "ACTIVE"

        self.created_at = datetime.now()
        self.is_authenticated = False

        # stores current login session
        self.active_session = None
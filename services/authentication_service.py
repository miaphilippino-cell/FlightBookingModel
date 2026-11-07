rom models.session import Session  # type: ignore
from security.rate_limiter import RateLimiter  # type: ignore


class AuthenticationService:
    def __init__(self, audit_logger):

        self.audit_logger = audit_logger

        self.rate_limiter = RateLimiter(max_requests=5, time_window=60)

    def login(self, user_account, password):

        username = user_account.username

        # Rate limiting protection
        if not self.rate_limiter.allow_request(username):

            self.audit_logger.log_event(
                username, "LOGIN_ATTEMPT", "BLOCKED", "Rate limit exceeded"
            )

            return None

        # Check account status
        if user_account.account_status == "LOCKED":

            self.audit_logger.log_event(
                username, "LOGIN_ATTEMPT", "DENIED", "Account locked"
            )

            return None

        # Password verification
        if password != user_account.password_hash:

            user_account.record_failed_login()

            self.audit_logger.log_event(
                username, "LOGIN_FAILED", "DENIED", "Invalid password"
            )

            return None

        # Successful login
        user_account.reset_failed_attempts()
        user_account.is_authenticated = True

        # Create session using your existing Session class
        session = Session()

        user_account.active_session = session

        self.audit_logger.log_event(username, "LOGIN_SUCCESS", "AUTHORIZED")

        return session
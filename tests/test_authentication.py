from services.audit_logger import AuditLogger # type: ignore
from services.authentication_service import AuthenticationService # type: ignore
from models.user_account import UserAccount # type: ignore


def test_login_success():

    logger = AuditLogger()

    auth = AuthenticationService(logger)

    user = UserAccount(
        "mia",
        "password123"
    )

    session = auth.login(
        user,
        "password123"
    )

    assert session is not None
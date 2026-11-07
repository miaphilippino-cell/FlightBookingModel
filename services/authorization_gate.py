from models.enums import UserRole # type: ignore


class AuthorizationGate:

    def __init__(self, audit_logger):
        self.audit_logger = audit_logger


    def authorize(self, user_account, action):

        if not user_account.is_authenticated:
            return False

        if user_account.role == UserRole.PASSENGER.value:

            passenger_actions = [
                "SEARCH_FLIGHTS",
                "CREATE_BOOKING",
                "VIEW_BOOKING",
                "CANCEL_BOOKING"
            ]

            return action in passenger_actions


        if user_account.role == UserRole.ADMIN.value:

            admin_actions = [
                "UPDATE_FLIGHT_STATUS"
            ]

            return action in admin_actions


        return False
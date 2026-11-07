from models.enums import FlightStatus # type: ignore


class AdminService:


    def __init__(self, audit_logger):

        self.audit_logger = audit_logger



    def add_flight(
        self,
        flight_list,
        flight
    ):

        flight_list.append(
            flight
        )


        self.audit_logger.log_event(
            "ADMIN",
            "FLIGHT_CREATED",
            "SUCCESS"
        )


        return True



    def cancel_flight(
        self,
        flight
    ):

        flight.status = FlightStatus.CANCELLED


        self.audit_logger.log_event(
            "ADMIN",
            "FLIGHT_CANCELLED",
            "SUCCESS"
        )


        return True



    def delay_flight(
        self,
        flight
    ):

        flight.status = FlightStatus.DELAYED


        self.audit_logger.log_event(
            "ADMIN",
            "FLIGHT_DELAYED",
            "SUCCESS"
        )


        return True
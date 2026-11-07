from models.booking import Booking  # type: ignore
from services.payment_gateway import PaymentGateway  # type: ignore
from services.seat_inventory_service import SeatInventoryService  # type: ignore


class BookingService:
    def __init__(self, audit_logger):

        self.audit_logger = audit_logger
        self.seat_service = SeatInventoryService()
        self.payment_gateway = PaymentGateway(audit_logger)

    def get_username(self, passenger):
        """
        Returns the account username if the passenger has an account.
        Otherwise, returns the passenger's name for guest bookings.
        """
        if passenger.user_account is not None:
            return passenger.user_account.username

        return passenger.full_name

    def create_booking(self, passenger, flight, seats):

        # Only check authentication if an account exists
        if (
            passenger.user_account is not None
            and not passenger.user_account.is_authenticated
        ):
            raise Exception("Passenger must be authenticated")

        self.seat_service.reserve_seats(flight, seats)

        booking = Booking(passenger, flight, seats)

        passenger.bookings.append(booking)

        self.audit_logger.log_event(
            self.get_username(passenger),
            "BOOKING_CREATED",
            "SUCCESS"
        )

        return booking

    def confirm_booking(self, booking):

        booking.confirm()

        self.audit_logger.log_event(
            self.get_username(booking.passenger),
            "BOOKING_CONFIRMED",
            "SUCCESS"
        )

        return booking

    def cancel_booking(self, booking):

        booking.cancel()

        self.seat_service.release_seats(
            booking.flight,
            booking.seat_numbers
        )

        self.audit_logger.log_event(
            self.get_username(booking.passenger),
            "BOOKING_CANCELLED",
            "SUCCESS"
        )

        return booking

    def process_booking_payment(self, booking, payment):

        username = self.get_username(booking.passenger)

        success = self.payment_gateway.process_payment(
            payment,
            username
        )

        if success:

            booking.payment = payment

            booking.confirm()

            self.audit_logger.log_event(
                username,
                "BOOKING_CONFIRMED",
                "SUCCESS"
            )

        return success

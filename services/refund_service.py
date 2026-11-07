from models.enums import PaymentStatus, BookingStatus # type: ignore


class RefundService:


    def __init__(self, audit_logger):

        self.audit_logger = audit_logger



    def process_refund(
        self,
        booking
    ):

        username = booking.passenger.user_account.username


        if booking.payment is None:

            raise Exception(
                "No payment found"
            )


        if booking.payment.status != PaymentStatus.COMPLETED:

            raise Exception(
                "Payment cannot be refunded"
            )


        booking.payment.refund()

        booking.status = BookingStatus.REFUNDED


        booking.flight.release_seats(
            booking.seat_numbers
        )


        self.audit_logger.log_event(
            username,
            "REFUND_PROCESSED",
            "SUCCESS"
        )


        return True
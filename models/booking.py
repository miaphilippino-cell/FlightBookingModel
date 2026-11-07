import uuid
from datetime import datetime

from models.enums import BookingStatus # type: ignore


class Booking:


    def __init__(
        self,
        passenger,
        flight,
        seats
    ):

        if len(seats) > flight.capacity:
            raise ValueError(
                "Too many seats requested"
            )


        self.booking_id = str(uuid.uuid4())

        self.passenger = passenger
        self.flight = flight

        self.seat_numbers = seats

        self.booking_date = datetime.now()

        self.status = BookingStatus.PENDING

        self.payment = None

        self.audit_logs = []



    def confirm(self):

        self.status = BookingStatus.CONFIRMED



    def cancel(self):

        self.status = BookingStatus.CANCELLED
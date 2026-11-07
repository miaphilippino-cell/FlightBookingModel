from datetime import datetime, timedelta

from models.user_account import UserAccount # type: ignore
from models.passenger import Passenger # type: ignore
from models.flight import Flight # type: ignore
from services.booking_service import BookingService # type: ignore
from services.audit_logger import AuditLogger # type: ignore


def test_booking_creation():

    user = UserAccount(
        "mia",
        "password123"
    )

    user.is_authenticated = True

    passenger = Passenger(
        "Mia",
        "mia@email.com",
        "555-5555",
        user
    )

    flight = Flight(
        "AA101",
        datetime.now(),
        datetime.now() + timedelta(hours=5),
        100,
        250,
        "American Airlines"
    )

    logger = AuditLogger()

    service = BookingService(logger)

    booking = service.create_booking(
        passenger,
        flight,
        ["12A", "12B"]
    )

    assert booking is not None
    assert flight.seats_available == 98
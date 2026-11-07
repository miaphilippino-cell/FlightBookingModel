from models.enums import FlightStatus # type: ignore
import threading


class Flight:

    def __init__(
        self,
        flight_id,
        departure_time,
        arrival_time,
        capacity,
        price,
        airline
    ):

        if departure_time >= arrival_time:
            raise ValueError(
                "Invalid flight schedule"
            )

        self.flight_id = flight_id

        self.departure_time = departure_time
        self.arrival_time = arrival_time

        self.capacity = capacity
        self.seats_available = capacity

        self.base_price = price
        self.airline = airline

        self.status = FlightStatus.ACTIVE

        self.reserved_seats = []

        # Prevents overbooking/race condition attacks
        self.lock = threading.Lock()


    def check_availability(self, number):

        return self.seats_available >= number


    def reserve_seat(self, seats):

        with self.lock:

            if not self.check_availability(len(seats)):
                raise Exception(
                    "Not enough seats available"
                )

            for seat in seats:

                self.reserved_seats.append(seat)

            self.seats_available -= len(seats)


    def release_seats(self, seats):

        with self.lock:

            for seat in seats:

                if seat in self.reserved_seats:

                    self.reserved_seats.remove(seat)

                    self.seats_available += 1


    def calculate_fare(self, passengers=1):

        return self.base_price * passengers


    def update_status(self, new_status):

        self.status = new_status
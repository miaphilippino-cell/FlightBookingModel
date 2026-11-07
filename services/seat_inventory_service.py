from models.flight import Flight # type: ignore


class SeatInventoryService:


    def reserve_seats(self, flight: Flight, seats):

        # Validate seat availability
        if not flight.check_availability(len(seats)):
            raise Exception(
                "Not enough seats available"
            )


        # Reserve seats using Flight locking logic
        flight.reserve_seat(seats)


        return True



    def release_seats(self, flight: Flight, seats):

        flight.release_seats(seats)

        return True
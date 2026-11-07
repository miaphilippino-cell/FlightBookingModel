class Route:


    def __init__(
        self,
        route_id,
        origin,
        destination,
        distance,
        duration
    ):

        self.route_id = route_id
        self.origin = origin
        self.destination = destination

        self.distance = distance
        self.duration = duration

        self.flights = []


    def add_flight(self, flight):

        self.flights.append(flight)
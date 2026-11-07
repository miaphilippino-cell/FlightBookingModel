import random
from datetime import datetime, timedelta

from models.flight import Flight  # type: ignore
from models.passenger import Passenger  # type: ignore
from models.payment import Payment  # type: ignore
from models.user_account import UserAccount  # type: ignore
from services.audit_logger import AuditLogger  # pyright: ignore[reportMissingImports]
from services.booking_service import ( # type: ignore
    BookingService,
)  # pyright: ignore[reportMissingImports]

# =====================================================
# POPULAR U.S. AIRPORTS
# =====================================================

airports = {
    "ATL": "Atlanta, GA (Hartsfield-Jackson)",
    "LAX": "Los Angeles, CA",
    "JFK": "New York, NY (John F. Kennedy)",
    "EWR": "Newark, NJ",
    "LGA": "New York, NY (LaGuardia)",
    "ORD": "Chicago, IL (O'Hare)",
    "DFW": "Dallas/Fort Worth, TX",
    "DEN": "Denver, CO",
    "SFO": "San Francisco, CA",
    "SEA": "Seattle, WA",
    "LAS": "Las Vegas, NV",
    "MCO": "Orlando, FL",
    "MIA": "Miami, FL",
    "BOS": "Boston, MA",
    "CLT": "Charlotte, NC",
    "PHX": "Phoenix, AZ",
    "IAD": "Washington Dulles, VA",
    "DCA": "Washington Reagan, DC",
    "MSP": "Minneapolis, MN",
    "DTW": "Detroit, MI",
    "PHL": "Philadelphia, PA",
    "BNA": "Nashville, TN",
    "SAN": "San Diego, CA",
    "TPA": "Tampa, FL",
    "HNL": "Honolulu, HI",
}


# =====================================================
# AIRLINES
# =====================================================

airlines = {
    "1": {
        "name": "American Airlines",
        "code": "AA",
        "aircraft": ["Boeing 737-800", "Airbus A321", "Boeing 787-9 Dreamliner"],
    },
    "2": {
        "name": "Delta",
        "code": "DL",
        "aircraft": ["Airbus A220", "Airbus A321neo", "Boeing 757-200"],
    },
    "3": {
        "name": "United",
        "code": "UA",
        "aircraft": ["Boeing 737 MAX 9", "Boeing 777-200", "Airbus A320"],
    },
    "4": {
        "name": "JetBlue",
        "code": "B6",
        "aircraft": ["Airbus A220", "Airbus A321LR", "Embraer E190"],
    },
    "5": {
        "name": "Southwest",
        "code": "WN",
        "aircraft": ["Boeing 737-700", "Boeing 737-800", "Boeing 737 MAX 8"],
    },
}


# =====================================================
# ESTIMATED TAXES AND FEES
# =====================================================

airline_fees = {
    "American Airlines": 35,
    "Delta": 32,
    "United": 38,
    "JetBlue": 28,
    "Southwest": 20,
}


# =====================================================
# SEAT CLASSES
# =====================================================

seat_classes = {
    "1": {"name": "First Class", "cash": 1200, "points": 90000},
    "2": {"name": "Business", "cash": 750, "points": 60000},
    "3": {"name": "Premium Economy", "cash": 450, "points": 35000},
    "4": {"name": "Economy", "cash": 250, "points": 18000},
}


# =====================================================
# HELPER FUNCTIONS
# =====================================================


def get_seat_type(seat):

    seat = seat.upper().strip()

    if len(seat) < 2:
        return "Unknown"

    letter = seat[-1]

    if letter in ["A", "F"]:
        return "Window"

    elif letter in ["C", "D"]:
        return "Aisle"

    elif letter in ["B", "E"]:
        return "Middle"

    return "Unknown"


def generate_flight_number(code):

    return f"{code}{random.randint(100,9999)}"


def generate_departure_time():

    times = [(6, 30), (9, 0), (12, 45), (15, 30), (18, 15), (21, 0)]

    return random.choice(times)


def calculate_duration(origin, destination):

    long_routes = [("BOS", "LAX"), ("JFK", "SEA"), ("MIA", "SFO"), ("HNL", "BOS")]

    if (origin, destination) in long_routes or (destination, origin) in long_routes:

        return random.randint(6, 7)

    return random.randint(2, 5)


# =====================================================
# MAIN PROGRAM
# =====================================================


def main():

    print("=" * 60)
    print("              FLIGHT BOOKING SYSTEM")
    print("=" * 60)

    logger = AuditLogger()

    booking_service = BookingService(logger)

    # =================================================
    # USER ACCOUNT
    # =================================================

    create_account = input("\nCreate airline account? (Y/N): ").upper()

    user = None

    if create_account == "Y":

        username = input("Create Username: ")

        password = input("Create Password: ")

        user = UserAccount(username, password)

        user.is_authenticated = True

        print("\nAccount created successfully!")

    else:

        print("\nContinuing as Guest...")

    # =================================================
    # PASSENGER INFORMATION
    # =================================================

    print("\nPassenger Information")

    name = input("Full Name: ")

    email = input("Email: ")

    phone = input("Phone Number: ")

    passenger = Passenger(name, email, phone, user)

    # =================================================
    # AIRPORT SELECTION
    # =================================================

    print("\nPopular U.S. Airports")

    print("-" * 40)

    for code, airport in airports.items():

        print(f"{code} - {airport}")

    origin = input("\nDeparture Airport Code: ").upper()

    while origin not in airports:

        print("Invalid airport code.")

        origin = input("Departure Airport Code: ").upper()

    destination = input("Destination Airport Code: ").upper()

    while destination not in airports or destination == origin:

        if destination == origin:

            print("Destination cannot match departure.")

        else:

            print("Invalid airport code.")

        destination = input("Destination Airport Code: ").upper()

    # =================================================
    # AIRLINE SELECTION
    # =================================================

    print("\nAvailable Airlines")

    print("-" * 40)

    for key, airline in airlines.items():

        print(f"{key}. {airline['name']}")

    airline_choice = input("\nChoose Airline: ")

    while airline_choice not in airlines:

        print("Invalid selection.")

        airline_choice = input("Choose Airline: ")

    airline_info = airlines[airline_choice]

    airline = airline_info["name"]

    aircraft = random.choice(airline_info["aircraft"])

    flight_number = generate_flight_number(airline_info["code"])

    print(f"\nAircraft Assigned: {aircraft}")

    print(f"Flight Number: {flight_number}")

    # =================================================
    # TRIP TYPE
    # =================================================

    print("\nTrip Type")

    print("1. One Way")

    print("2. Round Trip")

    trip_choice = input("Choose: ")

    while trip_choice not in ["1", "2"]:

        trip_choice = input("Choose 1 or 2: ")

    # =================================================
    # DEPARTURE DATE
    # =================================================

    departure_input = input("\nDeparture Date (YYYY-MM-DD): ")

    departure = datetime.strptime(departure_input, "%Y-%m-%d")

    hour, minute = generate_departure_time()

    departure = departure.replace(hour=hour, minute=minute)

    duration = calculate_duration(origin, destination)

    arrival = departure + timedelta(hours=duration)

    # =================================================
    # RETURN DATE
    # =================================================

    return_departure = None
    return_arrival = None

    if trip_choice == "2":

        return_input = input("Return Date (YYYY-MM-DD): ")

        return_departure = datetime.strptime(return_input, "%Y-%m-%d")

        return_departure = return_departure.replace(hour=hour, minute=minute)

        return_arrival = return_departure + timedelta(hours=duration)

        # =================================================
    # SEAT CLASS SELECTION
    # =================================================

    print("\nSeat Classes")

    print("-" * 40)

    for key, seat in seat_classes.items():

        print(
            f"{key}. {seat['name']} "
            f"- ${seat['cash']} "
            f"({seat['points']:,} points)"
        )

    class_choice = input("\nChoose Seat Class: ")

    while class_choice not in seat_classes:

        print("Invalid selection.")

        class_choice = input("Choose Seat Class: ")

    selected_class = seat_classes[class_choice]

    seat_class = selected_class["name"]

    base_price = selected_class["cash"]

    points_required = selected_class["points"]

    # =================================================
    # SEAT MAP
    # =================================================

    print("\n" + "=" * 50)

    print("                 SEAT MAP")

    print("=" * 50)

    print("        A   B   C     D   E   F")

    for row in range(1, 31):

        print(f"Row {row:2}   O   O   O     O   O   O")

    print("\nO = Available")

    print("Window: A/F")

    print("Middle: B/E")

    print("Aisle: C/D")

    seat = input("\nChoose Seat (Example 14A): ").upper()

    seat_type = get_seat_type(seat)

    print(f"\nSeat Selected: {seat}")

    print(f"Seat Type: {seat_type}")

    # =================================================
    # TAXES AND FEES
    # =================================================

    taxes = airline_fees[airline]

    total_price = base_price + taxes

    # =================================================
    # PAYMENT TYPE
    # =================================================

    print("\nPayment Options")

    print("1. Cash")

    print("2. Airline Points")

    print("3. Cash + Points")

    payment_choice = input("Choose Payment Type: ")

    payment_types = {"1": "Cash", "2": "Points", "3": "Cash + Points"}

    while payment_choice not in payment_types:

        print("Invalid option.")

        payment_choice = input("Choose Payment Type: ")

    payment_type = payment_types[payment_choice]

    if payment_type == "Cash":

        amount_due = total_price

        points_used = 0

    elif payment_type == "Points":

        amount_due = taxes

        points_used = points_required

    else:

        points_used = points_required // 2

        amount_due = base_price // 2 + taxes

    # =================================================
    # FLIGHT CREATION
    # =================================================

    flight = Flight(flight_number, departure, arrival, 100, base_price, airline)

    flight.aircraft = aircraft

    flight.origin = origin

    flight.destination = destination

    if return_departure:

        flight.return_departure = return_departure

        flight.return_arrival = return_arrival

    # =================================================
    # BOOKING CREATION
    # =================================================

    booking = booking_service.create_booking(passenger, flight, [seat])

    # =================================================
    # BOOKING SUMMARY BEFORE PAYMENT
    # =================================================

    print("\n")
    print("=" * 60)
    print("              BOOKING SUMMARY")
    print("=" * 60)

    print(f"Passenger      : {name}")

    print(f"Route          : {origin} -> {destination}")

    print(f"Airline        : {airline}")

    print(f"Aircraft       : {aircraft}")

    print(f"Flight Number  : {flight_number}")

    print(f"\nDeparture      : " f"{departure.strftime('%B %d, %Y %I:%M %p')}")

    print(f"Arrival        : " f"{arrival.strftime('%B %d, %Y %I:%M %p')}")

    if return_departure:

        print("\nReturn Flight")

        print(f"Return Depart  : " f"{return_departure.strftime('%B %d, %Y %I:%M %p')}")

        print(f"Return Arrival : " f"{return_arrival.strftime('%B %d, %Y %I:%M %p')}")

    print(f"\nSeat Class     : {seat_class}")

    print(f"Seat           : {seat}")

    print(f"Seat Type      : {seat_type}")

    print(f"\nBase Fare      : ${base_price}")

    print(f"Taxes & Fees   : ${taxes}")

    if payment_type == "Points":

        print(f"Points Used    : {points_used:,}")

        print(f"Cash Due       : ${amount_due}")

    elif payment_type == "Cash + Points":

        print(f"Points Used    : {points_used:,}")

        print(f"Cash Due       : ${amount_due}")

    else:

        print(f"Total Due      : ${amount_due}")

    print("=" * 60)

    confirm = input("\nConfirm Booking? (Y/N): ").upper()

    if confirm != "Y":

        print("\nBooking Cancelled.")

        return

    # =================================================
    # PAYMENT PROCESSING
    # =================================================

    print("\n")
    print("=" * 50)
    print("              PAYMENT")
    print("=" * 50)

    if payment_type == "Cash":

        payment_method = "Cash"

    elif payment_type == "Points":

        payment_method = "Points Redemption"

    else:

        payment_method = "Cash + Points"

    payment = Payment(amount_due, "USD", payment_method)

    booking_service.process_booking_payment(booking, payment)

    # =================================================
    # FINAL RECEIPT
    # =================================================

    print("\n")
    print("=" * 65)
    print("          THANK YOU FOR FLYING WITH US!")
    print("=" * 65)

    print(f"Booking ID      : {booking.booking_id}")

    print(f"Passenger       : {name}")

    if user:

        print(f"Username        : {user.username}")

    else:

        print("Username        : Guest")

    print(f"\nAirline         : {airline}")

    print(f"Flight          : {flight_number}")

    print(f"Aircraft        : {aircraft}")

    print(f"\nRoute           : " f"{origin} -> {destination}")

    print(f"Departure       : " f"{departure.strftime('%B %d, %Y %I:%M %p')}")

    print(f"Arrival         : " f"{arrival.strftime('%B %d, %Y %I:%M %p')}")

    print(f"\nSeat Class      : {seat_class}")

    print(f"Seat            : {seat}")

    print(f"Seat Type       : {seat_type}")

    print(f"\nPayment Type    : {payment_type}")

    print(f"Payment Method  : {payment_method}")

    print(f"Payment Status  : {payment.status}")

    print(f"\nBooking Status  : {booking.status}")

    print(f"Seats Remaining : {flight.seats_available}")

    print("=" * 65)

    print("Have a safe flight!")

    print("=" * 65)


# =====================================================
# PROGRAM START
# =====================================================

if __name__ == "__main__":

    main()
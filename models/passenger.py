class Passenger:

    def __init__(self, name, email, phone, user_account=None):

        # BookingService expects this name
        self.full_name = name

        self.name = name
        self.email = email
        self.phone = phone

        # Connected account
        self.user_account = user_account

        # Store bookings
        self.bookings = []


    def add_booking(self, booking):

        self.bookings.append(booking)
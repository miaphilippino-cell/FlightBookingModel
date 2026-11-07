import sqlite3


class Repository:


    def __init__(
        self,
        database_name="flight_booking.db"
    ):

        self.connection = sqlite3.connect(
            database_name
        )

        self.create_tables()



    def create_tables(self):

        cursor = self.connection.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password_hash TEXT,
            role TEXT

        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_id TEXT,
            airline TEXT,
            capacity INTEGER,
            seats_available INTEGER

        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id TEXT,
            username TEXT,
            flight_id TEXT,
            status TEXT

        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payment_id TEXT,
            amount REAL,
            status TEXT

        )
        """)


        self.connection.commit()



    def save_user(
        self,
        user
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            INSERT INTO users
            (username, password_hash, role)
            VALUES (?, ?, ?)
            """,
            (
                user.username,
                user.password_hash,
                user.role
            )
        )


        self.connection.commit()



    def save_flight(
        self,
        flight
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            INSERT INTO flights
            (flight_id, airline, capacity, seats_available)
            VALUES (?, ?, ?, ?)
            """,
            (
                flight.flight_id,
                flight.airline,
                flight.capacity,
                flight.seats_available
            )
        )


        self.connection.commit()



    def save_booking(
        self,
        booking
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            INSERT INTO bookings
            (booking_id, username, flight_id, status)
            VALUES (?, ?, ?, ?)
            """,
            (
                booking.booking_id,
                booking.passenger.user_account.username,
                booking.flight.flight_id,
                booking.status.value
            )
        )


        self.connection.commit()



    def save_payment(
        self,
        payment
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            INSERT INTO payments
            (payment_id, amount, status)
            VALUES (?, ?, ?)
            """,
            (
                payment.payment_id,
                payment.amount,
                payment.status.value
            )
        )


        self.connection.commit()
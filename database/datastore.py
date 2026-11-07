import sqlite3


DATABASE_NAME = "flight_booking.db"



def get_connection():

    return sqlite3.connect(
        DATABASE_NAME
    )



def create_tables():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
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


    connection.commit()

    connection.close()
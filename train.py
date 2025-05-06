from database import Session
from Models.booking import Booking

from database import engine

def test_connection():
    print("Testing database connection...")
    try:
        with engine.connect() as connection:
            print("Connection successful!")
    except Exception as e:
        print("Connection failed:", e)


def test_db_connection():
    print("Testing database connection...")
    try:
        print("Creating session...")
        session = Session()
        print("Querying bookings...")
        bookings = session.query(Booking).all()
        print(f"Found {len(bookings)} bookings in the database.")
        for booking in bookings:
            print(f"Booking ID: {booking.id}, User ID: {booking.user_id}, Activity ID: {booking.activity_id}")
    except Exception as e:
        print("Database connection failed or query error:", e)
    finally:
        print("Closing session...")
        session.close()

if __name__ == "__main__":
    #test_connection()
    test_db_connection()

from database import Session
from Models.review import Review
import datetime

def seed_reviews():
    session = Session()

    review1 = Review(
        booking_id=1,
        user_id=1,
        score=5,
        comment="So much fun, amazing sensations!",
        date=datetime.datetime(2025, 5, 8, 10, 0, 0)
    )

    review2 = Review(
        booking_id=2,
        user_id=2,
        score=4,
        comment="Great experience, but the weather could have been better.",
        date=datetime.datetime(2025, 5, 6, 15, 30, 0)
    )

    review3 = Review(
        booking_id=3,
        user_id=1,
        score=3,
        comment="Nice activity, but the equipment was a bit old.",
        date=datetime.datetime(2025, 5, 5, 18, 45, 0)
    )

    session.add_all([review1, review2, review3])
    session.commit()
    session.close()



from database import Session
from Models.booking import Booking
import datetime

def seed_bookings():
    session = Session()

    # Booking 1
    booking1 = Booking(
        activity_id=1,
        user_id=1,
        people=1,
        extras=None,
        promotion=True,
        promotion_id="UGVdqdUIwvg2iAbDag0q",
        status="progress",
        booking_type="slots",
        start_date=datetime.datetime.fromisoformat("2025-05-07T19:00:00"),
        end_date=datetime.datetime.fromisoformat("2025-05-07T20:30:00"),
        reservation_date=datetime.datetime.fromisoformat("2025-05-04T22:39:47.770647"),
        activity_price=None,
        total_price=54000,
        asked_for_rating=False,
        is_rated=False,
        cancellation_policies=[
            {"hours": 96, "refund_percentage": 50},
            {"hours": 48, "refund_percentage": 25}
        ],
        refund={"is_refunded": False},
        payment_intent_id="pi_3RL7SEJQFhlvgMTv0icqiO9x"
    )

    # Booking 2
    booking2 = Booking(
        activity_id=1,
        user_id=2,
        people=1,
        extras={"Action Camera Rental": 5000},
        promotion=True,
        promotion_id="UGVdqdUIwvg2iAbDag0q",
        status="progress",
        booking_type="slots",
        start_date=datetime.datetime.fromisoformat("2025-05-05T14:30:00"),
        end_date=datetime.datetime.fromisoformat("2025-05-05T16:00:00"),
        reservation_date=datetime.datetime.fromisoformat("2025-05-04T22:53:57.185785"),
        activity_price=None,
        total_price=32000,
        asked_for_rating=False,
        is_rated=False,
        cancellation_policies=[
            {"hours": 96, "refund_percentage": 50},
            {"hours": 48, "refund_percentage": 25}
        ],
        refund={"is_refunded": False},
        payment_intent_id="pi_3RL7fvJQFhlvgMTv2ckfi7a9"
    )

    # Booking 3
    booking3 = Booking(
        activity_id=2,
        user_id=1,
        people=1,
        extras=None,
        promotion=True,
        promotion_id="UGVdqdUIwvg2iAbDag0q",
        status="progress",
        booking_type="slots",
        start_date=datetime.datetime.fromisoformat("2025-05-04T23:30:00"),
        end_date=datetime.datetime.fromisoformat("2025-05-05T01:00:00"),
        reservation_date=datetime.datetime.fromisoformat("2025-05-04T22:22:43.615227"),
        activity_price=None,
        total_price=27000,
        asked_for_rating=False,
        is_rated=False,
        cancellation_policies=[
            {"hours": 96, "refund_percentage": 50},
            {"hours": 48, "refund_percentage": 25}
        ],
        refund={"is_refunded": False},
        payment_intent_id="pi_3RL7BhJQFhlvgMTv1Xllwmu4"
    )

    session.add_all([booking1, booking2, booking3])
    session.commit()
    session.close()


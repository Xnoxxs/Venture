
from database import Session
from Models.transaction import Transaction
from Models.booking import Booking
import datetime

def seed_transactions():
    session = Session()

    # Helper: get booking by payment_intent_id
    def get_booking_id(payment_intent_id):
        booking = session.query(Booking).filter_by(payment_intent_id=payment_intent_id).first()
        return booking.id if booking else None

    # Transaction 1 (for booking1)
    transaction1 = Transaction(
        booking_id=1,
        transaction_date=datetime.datetime.fromisoformat("2025-05-04T22:39:47.770647"),
        release_date=datetime.datetime.fromisoformat("2025-05-07T20:30:00.000"),
        commission_percentage=20.0,
        transaction_amount=54000,
        stripe_fee=160,
        currency="eur",
        payment_method="unknown",
        payment_status="succeeded",
        payment_intent_id="pi_3RL7SEJQFhlvgMTv0icqiO9x"
    )

    # Transaction 2 (for booking3)
    transaction2 = Transaction(
        booking_id=2,
        transaction_date=datetime.datetime.fromisoformat("2025-05-04T22:22:43.615227"),
        release_date=datetime.datetime.fromisoformat("2025-05-05T01:00:00.000"),
        commission_percentage=20.0,
        transaction_amount=32000,
        stripe_fee=160,
        currency="eur",
        payment_method="unknown",
        payment_status="succeeded",
        payment_intent_id="pi_3RL7BhJQFhlvgMTv1Xllwmu4"
    )

    # Transaction 3 (for booking2)
    transaction3 = Transaction(
        booking_id=3,
        transaction_date=datetime.datetime.fromisoformat("2025-05-04T22:53:57.185785"),
        release_date=datetime.datetime.fromisoformat("2025-05-05T16:00:00.000"),
        commission_percentage=20.0,
        transaction_amount=27000,
        stripe_fee=160,
        currency="eur",
        payment_method="unknown",
        payment_status="succeeded",
        payment_intent_id="pi_3RL7fvJQFhlvgMTv2ckfi7a9"
    )

    session.add_all([transaction1, transaction2, transaction3])
    session.commit()
    session.close()


from sqlalchemy import Column, Integer, Text, Boolean, TIMESTAMP, Numeric, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)

    activity_id = Column(Integer, ForeignKey('activities.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    people = Column(Integer)
    extras = Column(Integer)

    promotion = Column(Text)
    promotion_id = Column(Text)

    status = Column(Text)
    booking_type = Column(Text)

    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
    reservation_date = Column(TIMESTAMP)

    activity_price = Column(Numeric)
    total_price = Column(Numeric)

    payment_intent_id = Column(Text)

    asked_for_rating = Column(Boolean, default=False)
    is_rated = Column(Boolean, default=False)

    cancellation_policies = Column(JSON)  # List of { hours, refund_percentage }
    refund = Column(JSON)  # Object with refund fields

from sqlalchemy import Column, Integer, Text, Boolean, TIMESTAMP, Numeric, ForeignKey, JSON, ARRAY
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=False)

    name = Column(Text, nullable=False)
    description = Column(Text)
    rental_condition_message = Column(Text)

    city = Column(Text)
    country = Column(Text)
    location_name = Column(Text)
    street_address = Column(Text)

    allow_split_payment = Column(Boolean, default=False)

    type = Column(Text)  # 'event', 'class', etc.
    booking_type = Column(Text)  # 'slots' or 'dateRange'
    verified = Column(Boolean, default=False)
    verification_date = Column(TIMESTAMP)
    created = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    price_amount = Column(Integer)
    price_amount_in_currency = Column(Numeric)
    price_currency = Column(Text)

    categories = Column(ARRAY(Text))
    collections = Column(ARRAY(Text))
    keywords = Column(ARRAY(Text))

    details = Column(JSON)
    extra = Column(JSON)
    included = Column(JSON)
    media = Column(JSON)
    split_payment_milestones = Column(JSON)
    cancellation_policies = Column(JSON)

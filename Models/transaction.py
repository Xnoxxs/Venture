
from sqlalchemy import Column, Integer, Text, TIMESTAMP, Numeric, ForeignKey
import datetime
from Models.base.base import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    __table_args__ = {'schema': 'Venture'}

    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('Venture.bookings.id'), nullable=False)
    transaction_date = Column(TIMESTAMP, default=datetime.datetime.now)  # Timestamp of the transaction
    release_date = Column(TIMESTAMP)  # Scheduled release date
    commission_percentage = Column(Numeric(5, 2))  # Commission percentage
    transaction_amount = Column(Integer)  # Amount in cents (e.g., 9000 = 90 euros)
    stripe_fee = Column(Integer)  # Stripe fee in cents
    currency = Column(Text)  # Currency code (e.g., 'eur')
    payment_method = Column(Text)  # Payment method (card, apple pay, google pay)
    payment_status = Column(Text)  # Payment status (e.g., 'Success')
    payment_intent_id = Column(Text)  # Stripe payment intent ID

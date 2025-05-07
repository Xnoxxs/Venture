
from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey, CheckConstraint
import datetime
from Models.base.base import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)

    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    score = Column(Integer, nullable=False)
    comment = Column(Text)
    date = Column(TIMESTAMP, default=datetime.datetime.now)

    __table_args__ = (
        CheckConstraint('score BETWEEN 0 AND 5', name='score_range_check'),
    )

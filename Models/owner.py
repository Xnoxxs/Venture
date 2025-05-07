
from sqlalchemy import Column, Integer, Text, Boolean, TIMESTAMP, ARRAY, ForeignKey
import datetime
from Models.base.base import Base

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(Text, nullable=False)
    created = Column(TIMESTAMP, default=datetime.datetime.now)
    photo = Column(Text)
    description = Column(Text)
    activities = Column(ARRAY(Integer))
    stripe_connected_account_id = Column(Text)
    stripe_subscription_id = Column(Text)
    push_notifications_permission = Column(Boolean, default=True)

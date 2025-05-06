
from sqlalchemy import Column, Integer, Text, Boolean, TIMESTAMP, ARRAY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(Text, nullable=False)
    created = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    photo = Column(Text)
    description = Column(Text)
    activities = Column(ARRAY(Integer))
    stripe_connected_account_id = Column(Text)
    subscription_id = Column(Text)
    push_notifications_permission = Column(Boolean, default=True)

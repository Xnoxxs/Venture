
from sqlalchemy import Column, Integer, Text, Boolean, ARRAY
from Models.base.base import Base

class ActivityType(Base):
    __tablename__ = 'activity_types'
    __table_args__ = {'schema': 'Venture'}

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True, nullable=False)
    image = Column(Text)
    categories = Column(ARRAY(Integer))  # Stores category IDs as an array of integers (foreign keys)
    activities_available = Column(Boolean, default=False)
    events_available = Column(Boolean, default=False)
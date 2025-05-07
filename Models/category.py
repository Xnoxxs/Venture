
from sqlalchemy import Column, Integer, Text
from Models.base.base import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True, nullable=False)
    image = Column(Text)
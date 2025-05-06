from database import Session
from models import User

def seed():
    session = Session()
    user = User(name="Ilyess", email="hamza@example.com", owner=True, favourites=[1], devices_tokens=[])
    session.add(user)
    session.commit()
    session.close()


from database import Session
from models import User

def create_user(name, email):
    session = Session()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.close()

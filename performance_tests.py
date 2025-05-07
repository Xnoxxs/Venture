
import time
from database import Session
from Models import User

def create_user(name, email, password="password123"):
    session = Session()
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    session.close()
    
def test_create_users():
    start = time.time()
    for i in range(1000):
        create_user(f"User{i}", f"user{i}@example.com", "password123")
    print("Finished in", time.time() - start, "seconds")
    # Finished in 49.061002016067505 seconds

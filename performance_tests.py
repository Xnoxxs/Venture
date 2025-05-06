
import time
from operations import create_user

def test_create_users():
    start = time.time()
    for i in range(100000):
        create_user(f"User{i}", f"user{i}@example.com")
    print("Finished in", time.time() - start, "seconds")

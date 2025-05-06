import threading
from operations import create_user

def attempt_create_user(i):
    try:
        create_user(f"User{i}", f"user{i}@example.com")
    except Exception as e:
        print(f"Thread {i} failed:", e)

def test_isolation():
    threads = [threading.Thread(target=attempt_create_user, args=(i,)) for i in range(10)]
    for t in threads: t.start()
    for t in threads: t.join()

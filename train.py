

from database import engine

def test_connection():
    print("Testing database connection...")
    try:
        with engine.connect() as connection:
            print("Connection successful!")
    except Exception as e:
        print("Connection failed:", e)


if __name__ == "__main__":
    test_connection()

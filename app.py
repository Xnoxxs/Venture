from database import create_tables
from seed import seed
from performance_tests import test_create_users
from isolation_test import test_isolation

if __name__ == "__main__":
    create_tables()
    seed()
    test_create_users()
    test_isolation()

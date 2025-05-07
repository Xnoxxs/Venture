from database import create_tables
from Seed import seed_all
from performance_tests import test_create_users
from isolation_test import test_isolation

if __name__ == "__main__":
    create_tables()
    seed_all()
    test_create_users()
    #test_isolation()

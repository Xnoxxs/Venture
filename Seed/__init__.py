from Seed.users import seed_users
from Seed.owners import seed_owners
from Seed.categories import seed_categories
from Seed.activities import seed_activity
from Seed.bookings import seed_bookings
from Seed.transactions import seed_transactions
from Seed.reviews import seed_reviews

def seed_all():
    print("Seeding users...")
    seed_users()
    print("Seeding owners...")
    seed_owners()
    print("Seeding categories..")
    seed_categories()
    print("Seeding activities...")
    seed_activity()
    print("Seeding bookings...")
    seed_bookings()
    print("Seeding transactions...")
    seed_transactions()
    print("Seeding reviews...")
    seed_reviews()
    print("Seeding complete.")
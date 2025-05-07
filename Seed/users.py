
from database import Session
from Models.user import User
import datetime

def seed_users():
    session = Session()

    user1 = User(
        name="Ilyess",
        email="hamza.jaebak_ida@ast.ma",
        password="gAAAAABmw7V0Jv_0SvyL-Mzi0j_CIU1IAG0wGmoU9ghDAmqhK0UTZQ6KBJwhdSGw4Iln2HZw4Nw==",
        created=datetime.datetime(2025, 5, 3, 19, 50),
        customer_id="cu_XXXX",
        customer_created=datetime.datetime(2025, 5, 3, 19, 50),
        payment_method_default="default",
        card_brand="visa",
        card_payment_method_id="pi_XXXXXXX",
        card_last4=3333,
        card_expiry_month=5,
        card_expiry_year=26,
        last_logged_in=datetime.datetime(2025, 4, 14),
        last_logged_out=None,
        photo="https://ui-avatars.com/api/?name=h&background=8B0000&color=fff&size=200",
        push_notifications_permission=True,
        owner=True,
        favourites=[1],
        devices_tokens=[]
    )

    user2 = User(
        name="Anna",
        email="anna@example.com",
        password="gAAAAABmw7V0Jv_0SvyL-Mzi0j_CIU1IAG0wGmoU9ghDAmqhK0UTZQ6KBJwhdSGw4Iln2HZw4Nw==",
        created=datetime.datetime(2025, 5, 4, 10, 30),
        customer_id="cu_YYYY",
        customer_created=datetime.datetime(2025, 5, 4, 10, 30),
        payment_method_default="card",
        card_brand="mastercard",
        card_payment_method_id="pi_YYYYYYY",
        card_last4=4444,
        card_expiry_month=8,
        card_expiry_year=27,
        last_logged_in=datetime.datetime(2025, 4, 15),
        last_logged_out=None,
        photo="https://ui-avatars.com/api/?name=a&background=00008B&color=fff&size=200",
        push_notifications_permission=True,
        owner=True,
        favourites=[1],
        devices_tokens=[]
    )

    session.add_all([user1, user2])
    session.commit()
    session.close()


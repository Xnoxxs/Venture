
from database import Session
from Models.owner import Owner
from Models.user import User
import datetime

def seed_owners():
    session = Session()

    owner1 = Owner(
        user_id=1,
        name="Skr",
        created=datetime.datetime.now(),
        photo="https://picsum.photos/seed/779/600",
        description="Owner of water activities",
        activities=[1, 2],
        stripe_connected_account_id="acct_XXXXX",
        stripe_subscription_id="sub_XXXXX",
        push_notifications_permission=True
    )

    owner2 = Owner(
        user_id=1,
        name="Anna Owner",
        created=datetime.datetime.now(),
        photo="https://picsum.photos/seed/780/600",
        description="Owner of adventure activities",
        activities=[2],
        stripe_connected_account_id="acct_YYYYY",
        stripe_subscription_id="sub_YYYYY",
        push_notifications_permission=True
    )

    session.add_all([owner1, owner2])
    session.commit()
    session.close()


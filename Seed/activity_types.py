
from database import Session
from Models.activity_type import ActivityType

def seed_activity_types():
    session = Session()

    activity_type1 = ActivityType(
        name="Boats",
        image="https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%20Collections%2FBoat.jpg?alt=media&token=539bc412-0f65-494f-911f-8cc966f74d08",
        categories=[1],
        activities_available=True,
        events_available=False
    )

    activity_type2 = ActivityType(
        name="Paddle",
        image="https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%20Collections%2FPaddle.png?alt=media&token=a874629c-cedb-4550-b6f9-dda02ce45c6e",
        categories=[3],
        activities_available=True,
        events_available=False
    )

    activity_type3 = ActivityType(
        name="Ski Nautique",
        image="https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%20Collections%2FSki%20Nautique.png?alt=media&token=40df5d10-fafb-4dad-8e9d-a9a167e90411",
        categories=[1],
        activities_available=True,
        events_available=False
    )


    session.add_all([activity_type1, activity_type2, activity_type3])
    session.commit()
    session.close()


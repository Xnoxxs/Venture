
from database import Session
from Models.activity import Activity
import datetime

def seed_activity():
    session = Session()

    # Activity 1: WaveRider
    activity1 = Activity(
        owner_id=1,
        name="WaveRider",
        description="Get ready for an exhilarating water skiing event! WaveRider invites thrill-seekers and water enthusiasts...",
        categories=[1],
        collections=["Ski Nautique"],
        keywords=["water skiing", "event", "sports", "adventure"],
        city="Miami",
        country="USA",
        location_name="Sunny Isles Beach",
        street_address="105 Ocean Drive",
        geo_point={"lat": 25.7617, "lng": -80.1918},
        verified=True,
        verification_date=datetime.datetime(2024, 12, 1, 10, 0, 0),
        created=datetime.datetime(2025, 2, 28, 3, 11, 55, 3000),
        price_amount=30000,
        price_amount_in_currency=300,
        price_currency="eur",
        type="event",
        booking_type="slots",
        details=[
            {"text": "Instructors - Professional water skiing coaches available for guidance."},
            {"text": "Equipment - High-quality water skis and safety gear provided."},
            {"text": "Location - Beautiful and safe waters of Sunny Isles Beach, perfect for water skiing."}
        ],
        extra=[
            {"name": "Action Camera Rental", "price": 5000},
            {"name": "Photo Package", "price": 10000},
            {"name": "Extra Ski Time", "price": 7500}
        ],
        included=[
            {
                "category": "Safety",
                "items": [
                    {"condition": "Good", "name": "go", "usageCount": 0}
                ]
            },
            {
                "category": "Gear",
                "items": [
                    {"condition": "Good", "name": "Water Skis", "usageCount": 30},
                    {"condition": "Good", "name": "Ropes", "usageCount": 25}
                ]
            },
            {
                "category": "Fun",
                "items": [
                    {"condition": "Good", "name": "Refreshments", "usageCount": 50},
                    {"condition": "Good", "name": "Music System", "usageCount": 10}
                ]
            }
        ],
        media=[
            {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%2FVt6tMDWUftCCi67oc2vb%2FSki%20Nautique.png?alt=media&token=7a8b43d3-9e0f-4483-a1d2-22a19040597a"
            },
            {
                "type": "video",
                "url": "https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%2FVt6tMDWUftCCi67oc2vb%2FVideo-highlight.mp4?alt=media&token=993e1279-ec73-40a0-bb15-ab1f0c6a85e6",
                "fileSize": "20MB"
            },
            {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%2FVt6tMDWUftCCi67oc2vb%2F02-04-2025-milliseconds=1743603735831.jpg?alt=media&token=ea8e5dfd-f528-426f-8e95-74690ecf3f3f"
            }
        ],
        split_payment_milestones=[
            {
                "deadline": "2024-12-01",
                "penaltyPercentage": 5,
                "percentage": 30,
                "description": "Secure your spot with a deposit",
                "bookingCanceled": 3
            },
            {
                "deadline": "2024-12-12",
                "penaltyPercentage": 0,
                "percentage": 70,
                "description": "Complete payment before the event",
                "bookingCanceled": 1
            }
        ],
        cancellation_policies=[
            {"hours": 96, "refundPercentage": 50},
            {"hours": 48, "refundPercentage": 25}
        ],
        rental_condition_message="Please arrive 20 minutes early to complete registration and safety checks.",
        allow_split_payment=True
    )

    # Activity 2: Sea Ray 230
    activity2 = Activity(
        owner_id=1,
        name="Sea Ray 230",
        description="Enjoy an unforgettable experience with Sea Ray 230, perfect for relaxing and enjoying the sea or lake.",
        categories=[1],
        collections=["Boats"],
        keywords=["sea", "luxury", "boat", "cruise"],
        city="Barcelona",
        country="Spain",
        location_name="Marina Port",
        street_address="Harbor Avenue 101",
        geo_point={"lat": 36.7783, "lng": -119.4179},
        verified=False,
        verification_date=None,
        created=datetime.datetime(2025, 3, 1, 1, 0, 0, 597000),
        price_amount=120000,
        price_amount_in_currency=1200,
        price_currency="eur",
        type="activity",
        booking_type="dateRange",
        details=[
            {"text": "Captain included for boat guidance."},
            {"text": "Life jackets provided."},
            {"text": "Bluetooth speaker on board."}
        ],
        extra=[
            {"name": "Champagne Bottle", "price": 5000},
            {"name": "Sunset Tour Extension", "price": 7000}
        ],
        included=[
            {
                "category": "Safety",
                "items": [
                    {"condition": "Good", "name": "Life Jackets", "usageCount": 10},
                    {"condition": "Good", "name": "First Aid Kit", "usageCount": 2}
                ]
            },
            {
                "category": "Comfort",
                "items": [
                    {"condition": "Good", "name": "Sunshade", "usageCount": 5},
                    {"condition": "Good", "name": "Cushions", "usageCount": 8}
                ]
            }
        ],
        media=[
            {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%2FOc2WyoMYNqjnCcSC4m4X%2FBoat.jpg?alt=media&token=ed50418a-b174-453b-8b42-9448c4e024f9"
            }
        ],
        split_payment_milestones=[],
        cancellation_policies=[
            {"hours": 72, "refundPercentage": 50},
            {"hours": 24, "refundPercentage": 0}
        ],
        rental_condition_message="Please bring ID. Arrive 15 minutes early. All safety instructions must be followed.",
        allow_split_payment=False
    )

    # Activity 3: Paddle Swing
    activity3 = Activity(
        owner_id= 2,
        name="Paddle Swing",
        description="Enjoy an unforgettable experience with Paddle Swing, perfect for relaxing and enjoying the sea or lake.",
        categories=[3],
        collections=["Paddle"],
        keywords=["paddle", "lake", "relax", "adventure"],
        city="Annecy",
        country="France",
        location_name="Lake Side Station",
        street_address="Harbor Avenue 101",
        geo_point={"lat": 36.7783, "lng": -119.4179},
        verified=False,
        verification_date=None,
        created=datetime.datetime(2025, 3, 1, 1, 0, 0, 597000),
        price_amount=120000,
        price_amount_in_currency=1200,
        price_currency="eur",
        type="activity",
        booking_type="slots",
        details=[
            {"text": "Captain included for boat guidance."},
            {"text": "Life jackets provided."},
            {"text": "Bluetooth speaker on board."}
        ],
        extra=[
            {"name": "Champagne Bottle", "price": 5000},
            {"name": "Sunset Tour Extension", "price": 7000}
        ],
        included=[
            {
                "category": "Safety",
                "items": [
                    {"condition": "Good", "name": "Life Jackets", "usageCount": 10},
                    {"condition": "Good", "name": "First Aid Kit", "usageCount": 2}
                ]
            },
            {
                "category": "Comfort",
                "items": [
                    {"condition": "Good", "name": "Sunshade", "usageCount": 5},
                    {"condition": "Good", "name": "Cushions", "usageCount": 8}
                ]
            }
        ],
        media=[
            {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Activities%2FG5ID2gdWWwJZeWZ6QTtE%2FPaddle.png?alt=media&token=b1906875-0673-405a-91af-c09b59507c42"
            }
        ],
        split_payment_milestones=[],
        cancellation_policies=[
            {"hours": 72, "refundPercentage": 50},
            {"hours": 24, "refundPercentage": 10}
        ],
        rental_condition_message="Please bring ID. Arrive 15 minutes early. All safety instructions must be followed.",
        allow_split_payment=False
    )


    session.add_all([activity1, activity2, activity3])
    session.commit()
    session.close()


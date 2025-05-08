
import threading
from database import Session
from Models.review import Review

def leave_review(booking_id, user_id, score, comment):
    session = Session()

    # Check if a review already exists for this booking and user
    existing = session.query(Review).filter_by(booking_id=booking_id, user_id=user_id).first()
    if not existing:
        review = Review(
            booking_id=booking_id,
            user_id=user_id,
            score=score,
            comment=comment
        )
        session.add(review)
        try:
            session.commit()
        except Exception as e:
            print("Commit failed:", e)
    session.close()

def isolation_test():

    """
    A booking can only have one review, so this test makes sure that this rule is applied
    by making 10 reviews for the same booking at the same time using thread and at the end only
    one review should be made
    """

    # Clean the reviews table before testing
    session = Session()
    session.query(Review).delete()
    session.commit()
    session.close()

    booking_id = 1  # Use a real booking ID
    user_id = 1     # Use a real user ID

    def review_thread():
        leave_review(booking_id, user_id, 5, "Great experience!")

    threads = [threading.Thread(target=review_thread) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Check how many reviews were created for this booking and user
    session = Session()
    count = session.query(Review).filter_by(booking_id=booking_id, user_id=user_id).count()
    session.close()
    print(f"Number of reviews for booking {booking_id} by user {user_id}: {count}")

if __name__ == "__main__":
    isolation_test()
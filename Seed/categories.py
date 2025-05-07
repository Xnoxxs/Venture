
from database import Session
from Models.category import Category

def seed_categories():
    session = Session()

    category1 = Category(
        name="Kids",
        image="https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Categories%2FKids.jpg?alt=media&token=b4979608-1371-40a6-829d-63dc48b01642"
    )

    category2 = Category(
        name="Nature",
        image="https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Categories%2FNature.jpg?alt=media&token=c83ce096-9309-434e-beef-589b7735ee0c"
    )

    category3 = Category(
        name="Sports",
        image="https://firebasestorage.googleapis.com/v0/b/anchita-5673c.appspot.com/o/Categories%2FSports.jpg?alt=media&token=dc40cfb4-6010-4149-97d4-995844ecd82b"
    )

    session.add_all([category1, category2, category3])
    session.commit()
    session.close()

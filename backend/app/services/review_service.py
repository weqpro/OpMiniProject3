from sqlalchemy.orm import Session
from backend.app import crud, models, schemas

class ReviewService:
    async def create_review(self, db: Session, review: schemas.review.ReviewCreate):
        """
        Create a new review in the database.
        """
        return crud.reviews.crud.create_review(db, review)
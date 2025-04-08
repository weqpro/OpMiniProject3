from sqlalchemy.orm import Session
from backend.app import models, schemas

def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews_by_volunteer(db: Session, volunteer_id: int):
    return db.query(models.Review).filter(models.Review.volunteer_id == volunteer_id).all()

def report_review(db: Session, review_id: int):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if review:
        review.reported = True
        db.commit()
        db.refresh(review)
    return review
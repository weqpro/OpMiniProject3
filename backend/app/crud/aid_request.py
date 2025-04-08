from sqlalchemy.orm import Session
from app import models, schemas

def create_aid_request(db: Session, aid_request: schemas.AidRequestCreate):
    db_aid_request = models.AidRequest(**aid_request.dict())
    db.add(db_aid_request)
    db.commit()
    db.refresh(db_aid_request)
    return db_aid_request
from sqlalchemy.orm import Session
from app import models, schemas

def create_aid_request(db: Session, aid_request: schemas.AidRequestCreate):
    db_aid_request = models.AidRequest(**aid_request.dict())
    db.add(db_aid_request)
    db.commit()
    db.refresh(db_aid_request)
    return db_aid_request

def update_aid_request_status(db: Session, aid_request_id: int, status: models.AidRequestStatus):
    db_aid_request = db.query(models.AidRequest).filter(models.AidRequest.id == aid_request_id).first()
    if db_aid_request:
        db_aid_request.status = status
        db.commit()
        db.refresh(db_aid_request)
    return db_aid_request


def set_volunteer_deadline(db: Session, aid_request_id: int, deadline: datetime.datetime):
    db_aid_request = db.query(models.AidRequest).filter(models.AidRequest.id == aid_request_id).first()
    if db_aid_request:
        db_aid_request.volunteer_deadline = deadline
        db.commit()
        db.refresh(db_aid_request)
    return db_aid_request
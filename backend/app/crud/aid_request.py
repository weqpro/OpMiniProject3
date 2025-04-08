from sqlalchemy.orm import Session
from backend.app import models, schemas
import datetime

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

def delete_aid_request(db: Session, aid_request_id: int, soldier_id: int):
    aid_request = db.query(models.AidRequest).filter(models.AidRequest.id == aid_request_id, models.AidRequest.soldier_id == soldier_id).first()
    
    if aid_request:
        db.delete(aid_request)
        db.commit()
        return True
    return False

def reject_aid_request(db: Session, aid_request_id: int, volunteer_id: int):
    aid_request = db.query(models.AidRequest).filter(models.AidRequest.id == aid_request_id).first()
    
    if aid_request:
        if volunteer_id in [volunteer.id for volunteer in aid_request.volunteers]:
            aid_request.status = 'Очікування'
            db.commit()
            return True
    return False
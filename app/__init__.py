from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/surveys")
def create_survey(payload: dict, db: Session = Depends(get_db)):
    obj = models.Survey(**payload)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/surveys")
def list_surveys(db: Session = Depends(get_db)):
    return db.query(models.Survey).all()

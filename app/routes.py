from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models

router = APIRouter()
# ───────── helpers ─────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ───────── CRUD ─────────

# Create
@router.post("/surveys")
def create_survey(payload: dict, db: Session = Depends(get_db)):
    obj = models.Survey(**payload)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# Read All
@router.get("/surveys")
def list_surveys(db: Session = Depends(get_db)):
    return db.query(models.Survey).all()

# Read One
@router.get("/surveys/{survey_id}")
def get_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = db.query(models.Survey).filter(models.Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey

# Update
@router.put("/surveys/{survey_id}")
def update_survey(survey_id: int, payload: dict, db: Session = Depends(get_db)):
    survey = db.query(models.Survey).filter(models.Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    for key, value in payload.items():
        setattr(survey, key, value)

    db.commit()
    db.refresh(survey)
    return survey

# Delete
@router.delete("/surveys/{survey_id}")
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = db.query(models.Survey).filter(models.Survey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    db.delete(survey)
    db.commit()
    return {"detail": f"Survey {survey_id} deleted"}

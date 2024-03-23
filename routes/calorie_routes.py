from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date

from db.database import SessionLocal
from models.models import CalorieEntry as CalorieEntryModel
from schemas.schemas import CalorieEntry, CalorieEntryCreate

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/calories/", response_model=CalorieEntry)
def create_calorie_entry(entry: CalorieEntryCreate, db: Session = Depends(get_db)):
    db_entry = CalorieEntryModel(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry



@router.get("/calories/{entry_id}", response_model=CalorieEntry)
def read_calorie_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(CalorieEntryModel).filter(CalorieEntryModel.id == entry_id).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Calorie entry not found")
    return db_entry


@router.get("/calories/date/{entry_date}", response_model=List[CalorieEntry])
def read_calories_by_date(entry_date: date, db: Session = Depends(get_db)):
    db_entries = db.query(CalorieEntryModel).filter(CalorieEntryModel.date == entry_date).all()
    return db_entries


@router.put("/calories/{entry_id}", response_model=CalorieEntry)
def update_calorie_entry(entry_id: int, entry: CalorieEntryCreate, db: Session = Depends(get_db)):
    db_entry = db.query(CalorieEntryModel).filter(CalorieEntryModel.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Calorie entry not found")
    for var, value in vars(entry).items():
        setattr(db_entry, var, value) if value else None
    db.commit()
    db.refresh(db_entry)
    return db_entry


@router.delete("/calories/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_calorie_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(CalorieEntryModel).filter(CalorieEntryModel.id == entry_id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Calorie entry not found")
    db.delete(db_entry)
    db.commit()
    return {"ok": True}



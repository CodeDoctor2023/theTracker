# models/models.py

from sqlalchemy import Column, Integer, String, Float, Date
from db.database import Base

class CalorieEntry(Base):
    __tablename__ = "calorie_entries"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    calories = Column(Float, index=True)
    description = Column(String, index=True)
    

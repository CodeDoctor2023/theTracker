# schemas/schemas.py

from datetime import date
from pydantic import BaseModel

class CalorieEntryBase(BaseModel):
    date: date
    calories: float
    description: str

class CalorieEntryCreate(CalorieEntryBase):
    pass  # No additional fields for creation, but defined for clarity and future extension

class CalorieEntry(CalorieEntryBase):
    id: int  # Include the id in the main schema used for reading entries

    class Config:
        orm_mode = True  # Allows the schema to work with ORM models (like SQLAlchemy models)

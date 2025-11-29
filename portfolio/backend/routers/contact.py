from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from portfolio.backend import crud, schemas

router = APIRouter(prefix="/contact", tags=["Contact"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Contact)
def submit_contact(data: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, data)

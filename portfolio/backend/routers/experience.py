from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from portfolio.backend import crud, schemas

router = APIRouter(prefix="/experience", tags=["Experience"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Experience])
def get_all_experience(db: Session = Depends(get_db)):
    return crud.get_experience(db)

@router.post("/", response_model=schemas.Experience)
def create_experience(exp: schemas.ExperienceCreate, db: Session = Depends(get_db)):
    return crud.create_experience(db, exp)

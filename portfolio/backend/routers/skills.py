from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from portfolio.backend import crud, schemas

router = APIRouter(prefix="/skills", tags=["Skills"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Skill])
def get_all_skills(db: Session = Depends(get_db)):
    return crud.get_skills(db)

@router.post("/", response_model=schemas.Skill)
def create_new_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    return crud.create_skill(db, skill)

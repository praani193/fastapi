from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from portfolio.backend import crud, schemas

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Project])
def get_all_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)

@router.post("/", response_model=schemas.Project)
def create_new_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)

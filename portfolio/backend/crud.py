from sqlalchemy.orm import Session
from portfolio.backend import models, schemas

# PROJECT CRUD
def get_projects(db: Session):
    return db.query(models.Project).all()

def create_project(db: Session, data: schemas.ProjectCreate):
    project = models.Project(**data.dict())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

# SKILL CRUD
def get_skills(db: Session):
    return db.query(models.Skill).all()

def create_skill(db: Session, data: schemas.SkillCreate):
    skill = models.Skill(**data.dict())
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill

# EXPERIENCE CRUD
def get_experience(db: Session):
    return db.query(models.Experience).all()

def create_experience(db: Session, data: schemas.ExperienceCreate):
    exp = models.Experience(**data.dict())
    db.add(exp)
    db.commit()
    db.refresh(exp)
    return exp

# CONTACT CRUD
def create_contact(db: Session, data: schemas.ContactCreate):
    contact = models.Contact(**data.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

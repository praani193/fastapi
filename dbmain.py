from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, get_db, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SQLAlchemy with FastAPI is working!"}

@app.get("/students", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student:
        return student
    return {"error": "Student Not Found"}

@app.post("/students", response_model=schemas.Student)
def create_new(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.delete("/students/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id)
    if student:
        return {"message": "Student deleted!"}
    return {"error": "Student not found"}

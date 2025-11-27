from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Sample student database
students = [
    {"id": 1, "name": "Praanesh", "age": 20, "course": "AI/ML"},
    {"id": 2, "name": "Nithesh", "age": 21, "course": "CSE"},
    {"id": 3, "name": "Megh", "age": 22, "course": "ECE"},
    {"id": 4, "name": "Aman", "age": 19, "course": "AI/ML"}
]

@app.get("/")
def home():
    return {"message": "Welcome to Student API"}

@app.get("/students")
def get_all_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"error": "Student not found"}

# ✅ Query Parameters Example
@app.get("/search")
def search_students(
    name: Optional[str] = None,
    min_age: Optional[int] = None,
    course: Optional[str] = None
):
    results = students
    if name:
        results = [s for s in results if s["name"].lower() == name.lower()]
    if min_age:
        results = [s for s in results if s["age"] >= min_age]
    if course:
        results = [s for s in results if s["course"].lower() == course.lower()]
    return results

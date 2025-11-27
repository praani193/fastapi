from fastapi import FastAPI
from typing import Optional

app = FastAPI()

students = [
    {"id": 1, "name": "Praanesh", "age": 20, "course": "AI/ML"},
    {"id": 2, "name": "Nithesh", "age": 21, "course": "CSE"},
    {"id": 3, "name": "Megh", "age": 22, "course": "ECE"},
    {"id": 4, "name": "Aman", "age": 19, "course": "AI/ML"}
]

# ------------ GET ------------
@app.get("/students")
def get_students():
    return students

# ------------ POST ------------
@app.post("/students")
def add_student(student: dict):
    student["id"] = len(students) + 1
    students.append(student)
    return student

# ------------ PUT ------------
@app.put("/students/{student_id}")
def update_student(student_id: int, data: dict):
    for s in students:
        if s["id"] == student_id:
            s.update(data)
            return s
    return {"error": "Student not found"}

# ------------ PATCH (partial update) ------------
@app.patch("/students/{student_id}")
def patch_student(student_id: int, data: dict):
    for s in students:
        if s["id"] == student_id:
            for key, value in data.items():
                s[key] = value
            return s
    return {"error": "Student not found"}

# ------------ DELETE ------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            return {"message": "deleted"}
    return {"error": "not found"}

# ------------ OPTIONS ------------
@app.options("/students")
def options_students():
    return {
        "allowed_methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    }

# ------------ HEAD ------------
@app.head("/students")
def head_students():
    return {}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str

students = []

@app.post("/students")
def create_student(student: Student):
    student_dict = student.model_dump()
    student_dict["id"] = len(students) + 1
    students.append(student_dict)
    return student_dict
"""
ChatGPT said:

BaseModel is one of the MOST important concepts in FastAPI because it comes from Pydantic, the library that FastAPI uses for automatic:

✅ Data validation
✅ Data parsing
✅ Data type checking
✅ Auto-documentation (Swagger)
✅ Error handling

✅ What is BaseModel?

BaseModel is a class from Pydantic.
When you create a class that inherits from BaseModel, you create a data model.

A data model tells FastAPI:

what fields the request must contain

what data types they must be

which fields are optional

how to validate the data

how to return the response in structured form
"""
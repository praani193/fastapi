from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    course: str

# For creating new student
class StudentCreate(StudentBase):
    pass

# For returning student with ID
class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True  # IMPORTANT for ORM

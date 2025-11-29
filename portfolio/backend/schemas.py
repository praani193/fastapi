from pydantic import BaseModel

# Project
class ProjectBase(BaseModel):
    title: str
    description: str
    link: str | None = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    class Config:
        orm_mode = True

# Skill
class SkillBase(BaseModel):
    name: str
    level: str

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    class Config:
        orm_mode = True

# Experience
class ExperienceBase(BaseModel):
    role: str
    company: str
    duration: str
    description: str

class ExperienceCreate(ExperienceBase):
    pass

class Experience(ExperienceBase):
    id: int
    class Config:
        orm_mode = True

# Contact
class ContactBase(BaseModel):
    name: str
    email: str
    message: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    class Config:
        orm_mode = True

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine

# Routers
from portfolio.backend.routers import projects, skills, experience, contact

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio Backend")

# CORS (for React frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(experience.router)
app.include_router(contact.router)

@app.get("/")
def home():
    return {"message": "Portfolio Backend Running"}

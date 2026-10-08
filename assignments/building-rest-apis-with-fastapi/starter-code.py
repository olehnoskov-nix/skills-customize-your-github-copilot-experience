from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Write Python code", "completed": False},
    {"id": 2, "title": "Review API design", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: Add endpoints to list tasks, create tasks, and fetch a task by ID

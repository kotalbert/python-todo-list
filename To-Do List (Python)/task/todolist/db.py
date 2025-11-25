"""Database module for To-Do List application using SQLite."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Task

# Create engine once
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Create tables
Base.metadata.create_all(engine)

def get_db():
    """Returns a database session."""

    return Session(engine)

def get_all_tasks():
    """Fetches all tasks from the database."""

    with get_db() as session:
        tasks = session.query(Task).all()
        return tasks

def add_task(task: str) -> None:
    """Adds a new task to the database."""

    with get_db() as session:
        new_task = Task(task=task)
        session.add(new_task)
        session.commit()
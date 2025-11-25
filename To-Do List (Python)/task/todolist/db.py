"""Database module for To-Do List application using SQLite."""
from datetime import datetime, timedelta, date

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Task

# Create engine once
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Create tables
Base.metadata.create_all(engine)

def get_db() -> Session:
    """Returns a database session."""

    return Session(engine)

def get_all_tasks()-> list[type[Task]]:
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

def get_today_tasks() -> list[type[Task]]:
    """Fetches today's tasks from the database."""

    today = datetime.today().date()

    with get_db() as session:
        tasks = session.query(Task).filter(Task.deadline == today).all()
        return tasks

def get_task_by_date(target_date: date) -> list[type[Task]]:
    """Fetches tasks for a specific date from the database."""

    with get_db() as session:
        tasks = session.query(Task).filter(Task.deadline == target_date).all()
        return tasks

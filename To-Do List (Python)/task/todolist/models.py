"""Models for To-Do List application."""
from datetime import date

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for declarative models."""
    pass

class Task(Base):
    """Model for a task in the to-do list."""
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    deadline = Column(Date, default=date.today())

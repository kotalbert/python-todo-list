"""Models for To-Do List application."""
from datetime import date

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    """Model for a task in the to-do list."""
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    deadline = Column(Date, default=date.today())

"""Database module for To-Do List application using SQLite."""
import sqlite3

def get_db():
    """Establishes a connection to the SQLite database and returns the connection object."""
    conn = sqlite3.connect('sqlite:///todo.db?check_same_thread=False')
    return conn
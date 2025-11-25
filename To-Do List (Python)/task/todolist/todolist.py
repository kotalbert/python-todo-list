"""Main module for the To-Do List application."""
import sys
from datetime import datetime

from db import get_all_tasks, add_task, get_today_tasks


def main():

    while True:
        show_menu()
        handle_command()


def display_all_tasks() -> None:
     tasks = get_all_tasks()
     if len(tasks) == 0:
         print('Nothing to do!')
     for i, t in enumerate(tasks):
         d = t.deadline.strftime("%d %b")
         print(f"{i+1}. {t.task}. {d}")


def handle_command() -> None:
    """Handles user commands for the To-Do List application."""

    command = input()
    if command == '1':
        display_today_tasks()
    elif command == '2':
        pass
    elif command == '3':
        display_all_tasks()
    elif command == '4':
        enter_task()
    elif command == '0':
        end_program()
    else:
        print("Invalid option")


def end_program() -> None:
    print("Bye!")
    sys.exit(0)


def enter_task() -> None:
    print("Enter a task")
    task = input()
    add_task(task)


def display_today_tasks() -> None:
    today = datetime.today()
    day = today.strftime("%d")
    month = today.strftime("%b")
    print(f"Today  {day} {month}:")
    tasks = get_today_tasks()
    if len(tasks) == 0:
        print('Nothing to do!')
    for t in tasks:
        print(f"{t.id}. {t.task}")


def show_menu() -> None:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Add task")
    print("0) Exit")


if __name__ == '__main__':
    main()

"""Main module for the To-Do List application."""
from db import get_all_tasks, add_task

import sys


def main():

    while True:
        show_menu()
        handle_command()

def handle_command() -> None:
    """Handles user commands for the To-Do List application."""

    command = input()
    if command == '1':
        display_today_tasks()
    elif command == '2':
        enter_task()
    elif command == '0':
        end_program()
    else:
        print("Invalid option")


def end_program():
    print("Bye!")
    sys.exit(0)


def enter_task():
    print("Enter a task")
    task = input()
    add_task(task)


def display_today_tasks():
    print("Today's tasks")
    tasks = get_all_tasks()
    if len(tasks) == 0:
        print('Nothing to do!')
    for t in tasks:
        print(f"{t.id}. {t.task}")


def show_menu() -> None:
    print("1) Today's tasks")
    print("2) Add a task")
    print("0) Exit")


if __name__ == '__main__':
    main()

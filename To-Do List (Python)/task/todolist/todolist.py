"""Main module for the To-Do List application."""
import sys
from datetime import datetime, timedelta

from db import get_all_tasks, add_task, get_today_tasks, get_task_by_date, get_missed_tasks, delete_task_by_id


def main():
    while True:
        show_menu()
        handle_command()


def display_all_tasks() -> None:
    tasks = get_all_tasks()
    if len(tasks) == 0:
        print("Nothing to do!")
    for i, t in enumerate(tasks):
        month = t.deadline.strftime("%b")
        day = t.deadline.day
        d = f"{day} {month}"
        print(f"{i + 1}. {t.task}. {d}")


def display_week_tasks():
    for day in range(7):
        date = datetime.today().date()
        target_date = date + timedelta(days=day)
        day_name = target_date.strftime("%A")
        day_num = target_date.day
        month = target_date.strftime("%b")
        print(f"{day_name} {day_num} {month}:")
        tasks = get_task_by_date(target_date)
        if len(tasks) == 0:
            print("Nothing to do!")
        for i, t in enumerate(tasks):
            print(f"{i + 1}. {t.task}.")
        print()


def display_missed_tasks():
    tasks = get_missed_tasks()
    if len(tasks) == 0:
        print("All tasks have been completed!")
    print("Missed tasks:")
    for i, t in enumerate(tasks):
        month = t.deadline.strftime("%b")
        day = t.deadline.day
        d = f"{day} {month}"
        print(f"{i + 1}. {t.task}. {d}")
    print()


def delete_task():
    tasks = get_all_tasks()
    if len(tasks) == 0:
        print("Nothing to delete")
        return
    print("Choose the number of the task you want to delete:")
    for i, t in enumerate(tasks):
        month = t.deadline.strftime("%b")
        day = t.deadline.day
        d = f"{day} {month}"
        print(f"{t.id}. {t.task}. {d}")
    delete_task_by_id(t.id)
    print("The task has been deleted!")


def handle_command() -> None:
    """Handles user commands for the To-Do List application."""

    command = input()
    if command == '1':
        display_today_tasks()
    elif command == '2':
        display_week_tasks()
    elif command == '3':
        display_all_tasks()
    elif command == '4':
        display_missed_tasks()
    elif command == '5':
        enter_task()
    elif command == '6':
        delete_task()
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
    print("Enter a deadline")
    deadline_str = input()
    try:
        deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d")
        add_task(task, deadline_date)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


def display_today_tasks() -> None:
    today = datetime.today()
    day = today.day
    month = today.strftime("%b")
    print(f"Today  {day} {month}:")
    tasks = get_today_tasks()
    if len(tasks) == 0:
        print('Nothing to do!')
    for i, t in enumerate(tasks):
        print(f"{i + 1}. {t.task}")


def show_menu() -> None:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add a task")
    print("6) Delete a task")
    print("0) Exit")


if __name__ == '__main__':
    main()

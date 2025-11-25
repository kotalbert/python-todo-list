"""Main module for the To-Do List application."""
import sys


def main():

    while True:
        show_menu()
        handle_command()

def handle_command() -> None:
    """Handles user commands for the To-Do List application."""

    command = input()
    if command == '1':
        print("Today's tasks")
    elif command == '2':
        print("Add a task")
    elif command == '0':
        print("Bye!")
        sys.exit(0)
    else:
        print("Invalid option")


def show_menu() -> None:
    print("1) Today's tasks")
    print("2) Add a task")
    print("0) Exit")


if __name__ == '__main__':
    main()
